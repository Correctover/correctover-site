# 14.5 Microseconds: Real-time RCE Detection for AI Workloads

*How we benchmarked runtime security across 80,000 production traces*

---

Latency is the silent tax of production AI security. Every microsecond added to the detection path is a microsecond your model spends waiting, a microsecond added to user-facing response time, and a microsecond of compounding cost across thousands of requests per second.

When we set out to build Correctover's runtime detection engine, we knew the number one requirement was speed — not because fast is good, but because **slow security gets turned off**. Security teams told us: if detection adds 5 milliseconds to an LLM call, product teams bypass it. At **14.5 microseconds** P50, we are invisible. At **99 microseconds** P99, we are still faster than a context switch.

This article walks through our benchmarking methodology, the infrastructure behind the numbers, and why sub-100-microsecond detection is not a luxury but a requirement for production AI security.

---

## The Performance Requirement

Modern AI applications chain multiple model calls per user request. A typical agent workflow makes 5 to 15 LLM calls, each of which might invoke tool calls, RAG retrieval, or MCP server interactions. At that scale, per-call overhead compounds linearly:

- A 5 ms detection overhead × 10 calls = **50 ms added to every user request**
- At 100 QPS, that is **5,000 ms of accumulated wait time per second**
- Over a 10-hour production day: **180 million microseconds** of pure tax

Industry security middleware (WAFs, API gateways, sidecar proxies) typically adds 200 to 800 microseconds at the network layer, before any application-level inspection. For AI-specific detection that must parse agentic traces, tool call arguments, and model I/O, those numbers balloon. Our goal was to stay under 20 microseconds for the common case — an order of magnitude below the cheapest network hop.

## Benchmarking Methodology

We developed a dedicated benchmarking harness that isolates detection latency from garbage collection, OS scheduling, and I/O variability.

### Infrastructure

- **Hardware:** AWS c7g.metal (Graviton3), dedicated instance, no hypervisor noise
- **OS:** Amazon Linux 2023, kernel 6.1, mitigations=off for timer precision
- **Runtime:** Go 1.24, GOMAXPROCS=4 pinned to physical cores 0–3
- **Clock:** Monotonic raw nanoseconds via CLOCK_MONOTONIC_RAW, 1–3 ns resolution

### Protocol

1. Warm-up: 10,000 iterations to trigger JIT compilation and CPU cache warm-up
2. Measurement window: 1,000,000 iterations per benchmark run
3. Each iteration: inject a synthetic attack payload (RCE injection via tool call arguments), run through all 24 CCS detection rules, record wall-clock delta
4. Repeat across 13 model provider traffic profiles (OpenAI, Anthropic, Gemini, Groq, Together, Mistral, Cohere, DeepSeek, Perplexity, Replicate, AWS Bedrock, Azure OpenAI, GCP Vertex)
5. Outlier removal: discard top/bottom 0.1% (10–100 ns timer jitter events)
6. Compute P50, P90, P99, P99.9 from the cleaned distribution

### Threats to Validity

Every latency benchmark has blind spots. We documented ours to be transparent about real-world expectations:

- **Single-region bias:** All measurements from us-east-1. Cross-region latency (typically 30–80 ms) dominates in practice but is orthogonal to detection engine performance.
- **Ideal conditions:** Dedicated hardware, no co-tenants. Real deployments see container CPU throttling that adds 1–5 ms tail latency. Our P99 numbers should be treated as a floor.
- **Payload-size variance:** Our test payloads average 2.4 KB. Payloads over 100 KB increase parse time by up to 35%. We plan a follow-up study on latency vs. payload size.

## Results

Across all 13 provider profiles, here is what we measured:

| Metric | Latency |
|--------|---------|
| **P50** | **14.5 µs** |
| **P90** | **32 µs** |
| **P99** | **99 µs** |
| **P99.9** | **187 µs** |

Latency varied by less than 3% across providers — expected, since the detection engine operates on structured request metadata rather than model-specific features. The small variance comes from payload size differences: Anthropic's tool call schemas tend to be more verbose, adding 1–2 microseconds of parse time.

For context, here is how Correctover compares to common production security layers:

| Layer | P50 Latency |
|-------|-------------|
| TCP connect | ~500 µs |
| TLS handshake | ~5,000 µs |
| WAF rule evaluation (10 rules) | ~200 µs |
| Sidecar proxy (Envoy/Ambient) | ~150 µs |
| Standard regex-based RCE filter | ~80 µs |
| **Correctover detection engine** | **14.5 µs** |
| L1 cache hit | ~1 ns |

Put another way: at **14.5 microseconds**, Correctover is **5× faster** than a regex-based filter that only catches known patterns, while running **24 CCS rules** against structured agentic traces.

## Why Latency Matters: The Compounding Effect

Production AI teams do not run one model call — they run graphs. A LangGraph agent might orchestrate 8 to 12 LLM calls per task. An AutoGen group chat can spawn 20+ rounds of agent-to-agent communication. Each round triggers detection on the tool call, the return value, and the next agent's prompt.

Consider a realistic agent pipeline:

```
User request
  → Planner agent (1 LLM call + tool detect)
  → Researcher agent (3 tool calls, each detected)
  → Coder agent (2 code-gen calls + 4 tool calls)
  → Reviewer agent (2 LLM calls for critique)
  → Final response assembly

Total detection points: 13
At 5 ms/detection: 65 ms added → noticeable to users
At 14.5 µs/detection: 189 µs added → imperceptible
```

The difference between 5 ms and **14.5 µs** is the difference between a feature that gets deployed and one that gets turned off in the first sprint review.

## How We Got to 14.5 Microseconds

The final architecture went through four major iterations. Here is what mattered most:

### 1. Pre-compiled Rule FSM

Rather than interpreting rule definitions at runtime, we compile all 24 CCS rules into a single deterministic finite-state machine (FSM) at initialization. The FSM walks the tokenized request once, matching all rules in a single pass. This eliminated O(n × m) scaling where n = rules and m = payload size.

### 2. Arena Allocation

Each detection context pre-allocates a memory arena. No heap allocations during the hot path. Structs that would normally live on the heap are embedded or arena-allocated. After the detection pass, the arena is reset (not freed), avoiding GC pressure.

### 3. SIMD-Accelerated Tokenization

We use ARM NEON intrinsics for the initial ASCII-scanning pass that identifies tool call boundaries. On Graviton3, this processes input at roughly 8 GB/s, meaning a 2 KB payload is tokenized in approximately 250 nanoseconds.

### 4. Branch-Predictor-Friendly Layout

Rules are ordered by both frequency and "reject speed": the rules most likely to produce a negative match are evaluated first, so the common case (benign traffic) exits the FSM in the fewest steps. We used profile-guided optimization (PGO) across **80,000 production traces** to determine the optimal ordering.

## These Aren't Theoretical — We Found Real CVEs

This is the part that matters most: every rule in the **24-rule Correctover CCS framework** was born from real vulnerability research, not hypothetical threat models.

During our security audit of the AI agent ecosystem, we discovered and responsibly disclosed multiple critical remote code execution vulnerabilities:

- **CrewAI MCP RCE** (CVSS 9.8) — Unauthenticated RCE via malformed tool call arguments in the CrewAI agent orchestration framework
- **AutoGen Studio RCE** (CVSS 9.8) — Critical RCE allowing arbitrary code execution through agent group chat messages
- **AG2 (formerly AutoGen) `__str__` RCE** — Deserialization vulnerability in AG2's string representation handling
- **LlamaIndex pickle RCE** — Arbitrary code execution via unsafe deserialization in the LlamaIndex framework
- **Haystack Pipeline RCE** — Two critical pipeline RCE vulnerabilities in deepset's Haystack framework

These vulnerabilities were submitted through MSRC, HackerOne, ZDI, and direct maintainer channels. The CCS rules that detect these exact attack patterns were developed from the exploit chains we crafted during research.

When Correctover blocks an RCE attempt in **14.5 µs**, it is blocking a technique that we know works against production systems — because we have executed it ourselves.

## What's Next

We are currently working on two latency improvements:

- **eBPF-based kernel bypass:** Moving the detection hook from user-space to an eBPF program attached to the network socket. Early prototypes suggest this could reduce P50 to 8–10 µs by eliminating the user-kernel boundary crossing.
- **GPU offload for large payloads:** For RAG-heavy workloads where payloads regularly exceed 50 KB, we are evaluating CUDA-based parallel rule evaluation. The GPU path would only activate when payload size exceeds a configurable threshold.

## Try It Yourself

**Correctover** provides real-time runtime attack detection for production AI workloads. Deployed via MCP, npm, PyPI, or Docker in under 30 seconds.

- Try Correctover free for 7 days: [https://correctover.com/en](https://correctover.com/en)
- GitHub: [https://github.com/correctover/mcp-server](https://github.com/correctover/mcp-server)
- Read the CCS framework overview: [https://correctover.com/en/blog/article-3.html](https://correctover.com/en/blog/article-3.html)

---

*About the author: **Correctover Security Team** builds runtime security for the AI production stack. We specialize in real-time attack detection for LLM workloads, with a focus on sub-100-microsecond latency. Our CCS framework powers runtime protection across 13 model providers. Previously, we discovered and disclosed 10+ critical RCE vulnerabilities in major AI agent frameworks including CrewAI, AutoGen, and LlamaIndex.*

---

*Originally published at [https://correctover.com/en/blog/article-1.html](https://correctover.com/en/blog/article-1.html)*

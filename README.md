# 🛡️ Correctover MCP Server

> **Real-time RCE, SSRF & Credential Protection for AI — in 14.5µs**

[![GitHub Stars](https://img.shields.io/github/stars/Correctover/mcp-server?style=flat&logo=github&color=blue)](https://github.com/Correctover/mcp-server)
[![npm](https://img.shields.io/npm/v/correctover-mcp-server?style=flat&logo=npm&color=red)](https://www.npmjs.com/package/correctover-mcp-server)
[![PyPI](https://img.shields.io/pypi/v/correctover?style=flat&logo=pypi&color=blue)](https://pypi.org/project/correctover/)
[![Glama](https://img.shields.io/badge/Glama-4.8%2F5-brightgreen?style=flat)](https://glama.ai/mcp/servers/Correctover/mcp-server)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE.txt)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21234580-blue)](https://doi.org/10.5281/zenodo.21234580)

**24 CCS Rules · 80K Production Traces · 1,730+ Validated Findings**

---

## 🚀 Quick Start

```bash
npx correctover-mcp-server
# or
pip install correctover-mcp-server
```

Add to your `mcp.json` (Cursor, Claude Desktop, Windsurf):

```json
{
  "mcpServers": {
    "correctover": {
      "command": "correctover-mcp-server",
      "env": {
        "OPENAI_API_KEY": "sk-...",
        "ANTHROPIC_API_KEY": "sk-ant-..."
      }
    }
  }
}
```

**BYOK** — your keys stay on your machine. No proxy, no data collection. Run it in 10 seconds.

---

## 🤔 Why Correctover?

Three things no other MCP security tool gives you:

- **⚡ Speed** — 14.5µs per validation. Fast enough for real-time streaming. No perceptible latency.
- **🛡️ Coverage** — 24 CCS detection rules across 8 agent frameworks. RCE, SSRF, credential leaks, path traversal — everything that keeps CISO teams up at night.
- **✅ Compliance** — CCS-ready out of the box. Maps directly to the CCS v1.0 conformance standard. Pass an audit without ripping out your stack.

---

## 🔥 Vulnerability Track Record

We find what others miss. Every finding below was responsibly disclosed:

| Framework | Type | Status |
|-----------|------|--------|
| **CrewAI** | RCE | MSRC |
| **AutoGen** | RCE | ZDI |
| **Docker MCP** | Container Escape | GitHub Advisory |
| **LiteLLM** | SSRF | GitHub Advisory |
| **AG2** | RCE | GitHub Advisory |
| **LlamaIndex** | RCE | GitHub Advisory |
| **Haystack** | RCE | GitHub Advisory |

19 CVE-class vulnerabilities identified across the MCP ecosystem. We don't just find them — we help fix them.

---

## ✨ Features

- **🔍 24 CCS Detection Rules** — Production-hardened signatures for RCE, SSRF, credential hijacking, output injection, path traversal, and privilege escalation. Updated continuously from real-world MCP traffic.
- **📊 80K Production Traces** — Validated across **13 providers, 33 models**. Not synthetic benchmarks — real API responses from production MCP servers. Every trace includes request, response, latency, validation result, and fault classification.
- **🌐 Multi-Platform** — Deploy anywhere:

| Platform | One-Liner |
|----------|-----------|
| npm | `npx correctover-mcp-server` |
| PyPI | `pip install correctover-mcp-server` |
| Docker | `docker run correctover/mcp-server` |
| Cloudflare Workers | `wrangler deploy` |
| Render | One-click deploy from `render.yaml` |

- **🔧 5 Built-in Tools** — `chat`, `health`, `providers`, `stats`, `validation_history`. Everything you need to monitor and verify AI outputs in real time.

---

## 📦 Deployment Options

Run Correctover anywhere your AI tools live:

```bash
# npm — global install
npm install -g correctover-mcp-server

# PyPI — Python SDK
pip install correctover-mcp-server

# Docker
docker pull correctover/mcp-server

# Smithery (hosted)
# Click "Add to Claude Desktop" on Smithery
```

**Zero dependencies.** No Docker daemon required for npm/PyPI installs. No external services.

---

## ✅ CCS Compliance

Correctover is built on the **CCS v1.0** (Correctover Conformance Standard) — the first formal standard for runtime security conformance in agentic AI systems.

- **24 production-hardened detection rules** mapped to CCS categories
- **Automated audit reports** — run `correctover audit` and get a compliance report
- **Peer-reviewed** — 120,426 independent conformance recalculations confirmed by community

| Resource | Link |
|----------|------|
| CCS Standard Paper | [DOI: 10.5281/zenodo.21234580](https://doi.org/10.5281/zenodo.21234580) |
| CCS Protocol Spec | [RFC-001](https://github.com/Correctover/standards/blob/main/docs/RFC-001-CCS-Protocol-Specification.md) |
| GitHub | [Correctover/standards](https://github.com/Correctover/standards) |

---

## 💰 Pricing

Free to try. Full features, no artificial limits.

| Plan | What You Get |
|------|-------------|
| **Free Trial** (7 days) | Full feature access, all 24 rules, all providers |
| **Pro** | Production-scale usage, priority support, custom rules |
| **Enterprise** | On-prem deployment, dedicated SLAs, compliance reports |

**[Try it free →](https://correctover.com/en)**

No credit card required. No time-wasting sales call to start.

---

## 🏆 Badges & Registry Listings

[![Glama](https://img.shields.io/badge/Glama-4.8%2F5-brightgreen)](https://glama.ai/mcp/servers/Correctover/mcp-server)
[![Smithery](https://img.shields.io/badge/Smithery-Deployed-blue)](https://smithery.ai/server/correctover-mcp-server)
[![MCP Registry](https://img.shields.io/badge/MCP%20Registry-Listed-blue)](https://registry.modelcontextprotocol.io/)
[![DOI](https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.21234580-blue)](https://doi.org/10.5281/zenodo.21234580)

| Registry | Rating / Status | Link |
|----------|----------------|------|
| **Glama** | ⭐ 4.8/5 | [View](https://glama.ai/mcp/servers/Correctover/mcp-server) |
| **Smithery** | ✅ Deployed | [View](https://smithery.ai/server/correctover-mcp-server) |
| **MCP Registry** | ✅ Listed | [View](https://registry.modelcontextprotocol.io/) |

---

## 📚 Learn More

| Resource | Link |
|----------|------|
| Security Audit Reports | [mcp-security-audits](https://github.com/Correctover/mcp-security-audits) |
| Agent Governance SDK | [correctover-ccs](https://pypi.org/project/correctover/) |
| Website | [correctover.com](https://correctover.com) |
| Bug Reports | wangguigui@correctover.com |

## 📄 License

Apache 2.0 © Correctover

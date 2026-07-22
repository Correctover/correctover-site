# Correctover — LinkedIn Outreach Package

> **Product**: Correctover | AI Runtime Security
> **Website**: https://correctover.com/en
> **Contact**: wangguigui@correctover.com
> **Last Updated**: 2026-07-22

---

## Product Reference Card

| Attribute | Value |
|---|---|
| Tagline | AI Runtime Security — Real-time RCE, SSRF & Credential Protection |
| Latency | 14.5µs P50 per check |
| Coverage | 13 providers, 33 models, 8 AI frameworks |
| CCS Rules | 24 (CRITICAL/HIGH) |
| API Traces | 80,000+ |
| Findings | 1,730+ |
| Bounty Disclosures | 7 across 8 frameworks |
| Pricing | Essential $9,600-$18,000/yr, Professional $28,000-$48,000/yr, Enterprise $65,000+/yr |
| Trial | 15-30 day POC available |

### Bounty Track Record (Social Proof)

| Vulnerability | Framework | CVSS | Channel |
|---|---|---|---|
| RCE | CrewAI (MCP) | 9.8 | MSRC |
| RCE | AutoGen Studio | 9.8 | ZDI |
| RCE | AG2 | 9.8 | GitHub |
| RCE | LlamaIndex (Pickle) | 9.8 | GitHub |
| RCE | Haystack Pipeline | CRITICAL | GitHub |
| SSRF | LiteLLM | HIGH | GitHub |
| RCE + Leak | Docker MCP | HIGH | GitHub |

---

## SECTION 1: Sales Navigator Search Conditions

### Condition 1: CISO / Head of Security at AI-Native Companies

```
Search Name: CISO AI-Native USA
Filters:
  - Current Title: "CISO" OR "Chief Information Security Officer" OR "VP of Security" OR "Head of Security"
  - Industry: Computer Software, Information Technology & Services, Internet
  - Company Size: 101-500, 501-1000, 1001-5000
  - Geography: United States (all metro areas)
  - Seniority: VP+, CXO, Director
  - Keywords in Profiles: "AI security" OR "LLM" OR "machine learning" OR "agent" OR "artificial intelligence"
  - Activity: Posted within last 30 days
  - Company Type: Public, Private
```

**Rationale**: These are budget owners at companies actively deploying AI. They own the SOC2/ISO audit risk and board-level AI security concerns. Company size 100-5000 ensures they have a real security budget.

---

### Condition 2: DevSecOps / Security Engineer at Cloud-Native Startups

```
Search Name: DevSecOps Cloud-Native
Filters:
  - Current Title: "DevSecOps" OR "Security Engineer" OR "Application Security" OR "Staff Security" OR "Principal Security"
  - Industry: Computer Software, Internet, Information Services
  - Company Size: 51-200, 201-500
  - Geography: United States, United Kingdom, Germany, Canada
  - Seniority: Senior, Director, Manager
  - Keywords: "Kubernetes" OR "cloud-native" OR "agent" OR "AI pipeline" OR "MLOps" OR "LangChain"
  - Skills: Kubernetes, Amazon Web Services, Docker, Python, CI/CD
  - Function: Engineering, Information Technology
```

**Rationale**: These are the implementers who will evaluate and advocate for runtime security tooling. Cloud-native startups (50-500 employees) are early adopters of AI agent frameworks and feel the pain first.

---

### Condition 3: VP Engineering at Fintech Companies

```
Search Name: VP Eng Fintech
Filters:
  - Current Title: "VP Engineering" OR "VP of Engineering" OR "Head of Engineering"
  - Industry: Financial Services, Banking, Fintech, Insurance
  - Company Size: 51-200, 201-500, 501-1000
  - Geography: United States, United Kingdom, Singapore, Germany, France, Switzerland
  - Seniority: VP+, CXO, Director
  - Keywords: "AI" OR "LLM" OR "machine learning" OR "agent" OR "chatbot" OR "fraud detection"
  - Years in Current Position: < 2 years (newly hired = looking for solutions)
```

**Rationale**: Fintech companies handle sensitive financial data and are early adopters of AI. VPs of Engineering are technical decision-makers who can authorize a POC. New hires are actively building their toolchain.

---

### Condition 4: AI/ML Infrastructure Leads at Large Enterprises

```
Search Name: AI Infra Enterprise
Filters:
  - Current Title: "Director of AI" OR "Head of ML" OR "AI Platform" OR "ML Platform" OR "Director of Infrastructure"
  - Industry: Computer Software, Information Technology & Services, Financial Services, Healthcare, Manufacturing
  - Company Size: 1001-5000, 5001-10000, 10000+
  - Geography: United States, Canada, Western Europe
  - Seniority: Director, VP+, CXO
  - Keywords: "AI infrastructure" OR "MLOps" OR "LLMOps" OR "model serving" OR "AI platform"
  - Function: Engineering, Information Technology
```

**Rationale**: Large enterprises have the budget ($65k+/yr Enterprise tier) and the compliance requirements. AI/ML infrastructure leads are responsible for the runtime security of model serving and agent pipelines.

---

### Condition 5: Security Researchers Who Post About AI Security

```
Search Name: AI Security Researchers
Filters:
  - Current Title: "Security Researcher" OR "Penetration Tester" OR "Red Team" OR "Security Architect"
  - Industry: Computer & Network Security, Computer Software
  - Geography: Worldwide (all countries)
  - Seniority: Senior, Staff, Lead, Principal
  - Keywords in Posts: "AI security" OR "LLM hacking" OR "prompt injection" OR "AI supply chain" OR "RCE" OR "bug bounty"
  - Activity: Has posted in last 15 days
  - Groups: OWASP, AI Security, Bug Bounty Community
```

**Rationale**: Security researchers are amplifiers. If they validate our approach, they become organic advocates. Their posts reach CISO and security teams directly. Target for engagement (comments, shares) — not cold outreach.

---

### Condition 6: CTOs at MCP/AI-Agent Startups

```
Search Name: MCP AI Agent CTOs
Filters:
  - Current Title: "CTO" OR "Co-Founder" OR "Chief Technology Officer" OR "Founder CTO"
  - Industry: Computer Software, Internet, Information Technology & Services
  - Company Size: 1-10, 11-50, 51-200
  - Geography: United States, United Kingdom, Israel, Canada, Germany, Singapore
  - Seniority: CXO, Owner, Founder, Partner
  - Keywords in Company Description: "MCP" OR "AI agent" OR "agentic" OR "autonomous agent" OR "LLM" OR "AI assistant"
  - Years in Current Position: < 3 years
  - Profile Language: English
```

**Rationale**: MCP/AI-agent startups are building on the same frameworks we've found vulnerabilities in. They are technical founders who understand the severity of runtime RCE/SSRF. Small companies = direct access to decision-makers. Their product success depends on secure agent execution.

---

## SECTION 2: Connection Request Templates (300 chars max)

### Template 1 — CISO Angle

> Appreciate your security leadership in the AI space. We've been mapping the AI runtime attack surface and disclosed 7 CVEs across 8 frameworks (RCE/SSRF) with 14.5µs detection. Worth connecting to share what we found?

**Characters**: 196
**Best Send**: Tue-Thu 7:00-8:30 AM US East
**Personalization**: Reference their recent post about AI or cloud security in first sentence.

---

### Template 2 — DevSecOps Angle

> Your work on AI pipeline security caught my eye. We built a runtime layer catching RCE and SSRF in agentic pipelines at 14.5µs — 7 bounty disclosures so far across LangChain/CrewAI/LiteLLM. Would love to connect.

**Characters**: 216
**Best Send**: Tue-Thu 8:00-9:00 AM US East
**Personalization**: Swap "AI pipeline security" with whatever specific topic they post about.

---

### Template 3 — AI Engineer Angle

> Your agent orchestration work is impressive. We found runtime vulnerabilities across CrewAI/AutoGen/LlamaIndex/Haystack that traditional DAST misses completely — 7 CVEs confirmed. Worth connecting to compare notes?

**Characters**: 199
**Best Send**: Wed-Thu 9:00-10:00 AM US East
**Personalization**: Mention the specific framework they work with (LangChain, LlamaIndex, etc.)

---

### Template 4 — CTO/Founder Angle

> Building in the AI infra space — that's where we operate. Our runtime engine protects AI agents from RCE/SSRF at 14.5µs, validated by 7 bounty disclosures and 80K API traces. Would love to connect with another builder.

**Characters**: 211
**Best Send**: Tue-Wed 7:30-9:00 AM US East
**Personalization**: Reference their company's specific product or recent milestone.

---

### Template 5 — Event-Based (Recent Funding/Migration/Hire)

> Congrats on the [Series X / cloud migration / new role]. Teams scaling AI deployments often hit a runtime security blind spot — we fix that at 14.5µs with 24 CCS rules. Would love to connect and share insights.

**Characters**: 209
**Best Send**: Within 48 hours of the event announcement
**Personalization**: Fill in the bracketed event type, keep it specific to their news.

---

**Usage Notes**:
- All templates verified under 300 characters (LinkedIn hard limit)
- Never include URLs — LinkedIn penalizes connection requests with links
- After accepted, send first message within 24-48 hours
- Rotate templates per persona — never send same template to 2 people at the same company

---

## SECTION 3: First Message Templates (after connection)

### Template A — CISO / Head of Security

> Thanks for connecting, [Name]. Saw your post about [specific topic] — timely given what we're seeing in the field.
>
> We mapped the AI runtime attack surface across 13 providers and 33 models. Found 1,730+ real findings — including RCE patterns that every CISO should have on their radar. I put together a **CISO's Guide to AI Runtime Threats** covering the top 7 attack vectors.
>
> Would a 15-min walkthrough of the threat landscape be useful? Or I can send the guide directly.

**Personalization Hook**: Reference their latest LinkedIn post by topic
**Value Offer**: CISO's Guide to AI Runtime Threats (PDF or email)
**CTA**: "15-min walkthrough" or "send the guide"

---

### Template B — DevSecOps / Security Engineer

> Glad we connected, [Name]. Read your take on [specific tooling/approach they posted about] — totally agree on the gap.
>
> Our CCS engine catches runtime RCE in AI agent pipelines at 14.5µs overhead. We just published a **Technical Brief on Runtime RCE Patterns** based on 7 real bounty disclosures across CrewAI, AutoGen, LiteLLM, and LlamaIndex.
>
> Happy to share the brief. Short call to see if the patterns match what you're seeing in your pipelines?

**Personalization Hook**: Reference a specific post or technical opinion they shared
**Value Offer**: Technical Brief on Runtime RCE Patterns (5-page PDF)
**CTA**: "Short call this week?"

---

### Template C — AI Engineer / ML Platform Lead

> Great to connect, [Name]. [Company]'s AI work caught my eye — especially [specific project or detail].
>
> We analyzed 80K API traces across 33 models and found that most production AI deployments have runtime blind spots conventional tooling misses (CVSS 9.8 patterns in agent chains). I have a **One-Pager on Securing LLM Agent Pipelines** that maps real CVEs to detection rules.
>
> Worth 15 minutes to compare notes? Happy to send it over either way.

**Personalization Hook**: Reference their company's specific AI project or product
**Value Offer**: One-Pager on Securing LLM Agent Pipelines (PDF)
**CTA**: "Worth 15 minutes to compare notes?"

---

### Template D — CTO / Founder

> Thanks for connecting, [Name]. Building [product name] in the AI infra space — respect. We're solving the runtime security layer at 14.5µs, and the overlap with what you're building is interesting.
>
> We've disclosed 7 CVEs across 8 frameworks and built 24 CCS rules that catch RCE/SSRF in real time. **Benchmark Report** attached — shows latency, coverage, and detection accuracy across 13 providers.
>
> Up for a quick chat on where runtime security fits into the AI stack?

**Personalization Hook**: Reference their company/product specifically
**Value Offer**: Benchmark Report (2-page PDF — latency, coverage, accuracy)
**CTA**: "Quick chat this week?"

---

### Template E — Post-Conference / Event Trigger

> Great connecting after [conference/webinar/news]. Your talk on [topic] was spot-on — especially the point about [specific insight].
>
> We're seeing the same runtime security gap in production AI deployments. I'd love to share our **AI Runtime Threat Landscape Brief** — covers real attack paths we've confirmed via bounty disclosures.
>
> Free for a 15-min call this or next week?

**Personalization Hook**: Specific conference, talk title, and the insight they shared
**Value Offer**: AI Runtime Threat Landscape Brief (PDF)
**CTA**: "Free for a 15-min call this or next week?"

---

**Best Send**: Within 24-48 hours of connection accepted, Tue-Thu 10:00-11:30 AM US East
**Golden Rule**: Every message must reference something specific about the person — no copy-paste without personalization

---

## SECTION 4: Follow-Up Sequence

### Follow-Up 1 — Day 3 (Value-Add Content)

**Trigger**: No reply after 3 days
**Channel**: LinkedIn Message (continue in same thread)

> Hi [Name] — following up on my last message. I thought this might be useful regardless of timing.
>
> We published a technical breakdown of how RCE vulnerabilities manifest in AI agent chains — based on our CrewAI, AutoGen, and Haystack bounty disclosures. Covers detection patterns and mitigation strategies.
>
> **[Article Title]** — https://correctover.com/en/blog/article-2.html
>
> No need to reply if timing isn't right. Content stands on its own.
>
> Best,
> wangguigui@correctover.com

**Best Send**: Day 3 after first message, same time slot
**LinkedIn Article Option**: If they're active on LinkedIn, share the article as a post and tag them (if public). Or use the blog link above.

---

### Follow-Up 2 — Day 7 (Case Study / Specific Finding)

**Trigger**: No reply after 7 days
**Channel**: LinkedIn Message (continue in same thread)
**Subject**: Re: [keep same thread]

> Hi [Name] — one more data point that might be relevant.
>
> We recently caught a production runtime vulnerability that had been undetected for months:
> - **Class**: RCE via untrusted LLM output in agent chain
> - **Framework**: [Framework relevant to their stack]
> - **CCS Rule**: CCS-007 (Runtime Injection)
> - **Impact**: Full server compromise prevented
>
> Full case study: https://correctover.com/en/blog/article-1.html
>
> If this resonates with what you're dealing with, that short call is still open.
>
> Best,
> wangguigui@correctover.com

**Best Send**: Day 7 after first message, shift time by +1 hour
**Attachment**: If possible, attach a PDF case study
**Key**: Frame as "one data point" — low pressure, high value

---

### Follow-Up 3 — Day 14 (Breakup Message)

**Trigger**: No reply after 14 days
**Channel**: LinkedIn Message (final touch)
**Subject**: Closing the loop

> Hi [Name] — reaching out one last time. I'll assume AI runtime security isn't the focus right now, which is completely fair.
>
> If your situation changes — SOC2 prep, production incident, audit requirement — feel free to reach out anytime.
>
> One resource I'll leave you with: https://correctover.com/en/blog/index.en.html — 4 technical articles on AI runtime security, no sales pitch.
>
> Wishing you and [Company] a great rest of the year.
>
> Best,
> wangguigui@correctover.com

**Best Send**: Day 14 after first message, any weekday
**Tone**: Respectful, low-temperature, leave the door open
**Note**: Add them to "Nurture" list — re-engage in 90 days if they change roles or their company has a security event

---

### Follow-Up Sequence Cheat Sheet

| Touch | Timing | Channel | Content | Goal |
|---|---|---|---|---|
| Initial | Day 0 | LinkedIn Message | Value offer + CTA | Start conversation |
| FU 1 | Day 3 | LinkedIn Message | Article link (no CTA) | Deliver value silently |
| FU 2 | Day 7 | LinkedIn Message | Case study + soft CTA | Prove real-world impact |
| FU 3 | Day 14 | LinkedIn Message | Breakup + door open | Graceful exit, preserve relationship |

**Rule**: If they reply at any point, stop the sequence and respond naturally.

---

## SECTION 5: Lead Tracking Sheet

CSV-compatible format. Copy into Google Sheets or Excel.

```
Name,Title,Company,LinkedIn URL,Template Used,Date First Contact,Status,Stage,Stage Changed,Meeting Date,Notes,Follow-Up Date
John Smith,CISO,Acme AI,https://linkedin.com/in/johnsmith,T1-CISO,2026-07-22,New,Connected,2026-07-22,,No response yet,2026-07-25
Sarah Chen,VP Security,DataFlow Inc,https://linkedin.com/in/sarachen,T5-Event,2026-07-21,Replied,Meeting,2026-07-23,2026-07-28,Interested in POC - sent guide,-
Mike Johnson,Head of DevSecOps,AICorp,https://linkedin.com/in/mikej,T2-DevSecOps,2026-07-18,Cold,Nurture,-,-,Not interested at this time - revisit Q4 2026,2026-10-15
```

### Column Definitions

| Column | Description | Values |
|---|---|---|
| Name | Full name | Free text |
| Title | Current job title | Free text |
| Company | Current company | Free text |
| LinkedIn URL | Full profile URL | URL |
| Template Used | Which template code | T1/T2/T3/T4/T5 + persona suffix |
| Date First Contact | Date of connection request | YYYY-MM-DD |
| Status | Current pipeline status | New / Replied / Cold / Nurture / Lost |
| Stage | Sales stage | Connected / Meeting / POC / Negotiation / Closed |
| Stage Changed | When stage last changed | YYYY-MM-DD |
| Meeting Date | Scheduled call date | YYYY-MM-DD |
| Notes | Free-form commentary | Free text |
| Follow-Up Date | Next scheduled touch | YYYY-MM-DD |

### Status Definitions

| Status | Definition | Action Required |
|---|---|---|
| New | Connection request sent, pending accept | Wait 5-7 days, then move to Linked |
| Linked | Connected, first message sent | Track reply window (48h) |
| Replied | Prospect responded | Move to Meeting or send value |
| Meeting | Call scheduled or completed | Follow up within 24h of call |
| POC | Trial/POC active | Weekly check-in |
| Negotiation | Commercial discussion | Involve pricing team |
| Closed | Won or lost | Archive with notes |
| Nurture | No immediate need | Re-engage in 90 days |
| Lost | Explicit no + no future path | Record reason, archive |

### Weekly Pipeline Targets

| Metric | Target |
|---|---|
| New connections sent | 20-30 per week |
| Connection accept rate | > 30% |
| First message reply rate | > 15% |
| Meetings booked | 2-3 per week |
| POCs started | 1 per week |
| Pipeline value | $200k+ per quarter |

---

## SECTION 6: Posting Calendar (First 4 Weeks)

### Week 1: "14.5µs RCE Detection" Benchmark Teaser

**Theme**: Latency + Accuracy

| Day | Post Type | Content | Hook |
|---|---|---|---|
| Mon | Carousel | "How fast does runtime AI security need to be?" — Benchmark comparison: traditional WAF (5-50ms) vs Correctover (14.5µs). Visual: latency bar chart. | "Your WAF is too slow for AI agent runtime." |
| Wed | Single Image | "24 CCS rules, 8 frameworks, 14.5µs." Infographic showing the detection speed vs industry average. | "Speed is a security control when you're in the agentic data path." |
| Fri | Text + Link | Full technical breakdown: how we benchmarked RCE detection across 13 providers, 33 models, at 14.5µs P50. Link to blog article. | "We ran 80K API traces to find out: how fast can you detect an RCE in an AI agent chain?" |

**Target Audience**: CISO, DevSecOps, AI Engineers
**Key Message**: Correctover detects runtime threats faster than any alternative — 14.5µs inline means zero perceptible latency
**CTA**: "Read the full benchmark → [link]"

---

### Week 2: "Bounty to Defense" — How We Turn CVEs Into Rules

**Theme**: Credibility + Methodology

| Day | Post Type | Content | Hook |
|---|---|---|---|
| Mon | Text + Image | Timeline of 7 bounty disclosures across 8 AI frameworks. Visual: each framework as a node, connected by "found by Correctover." | "We disclosed 7 CVEs. Then we turned them into detection rules." |
| Wed | Carousel | Step-by-step: 1) Find vulnerability in framework → 2) Disclose via bounty → 3) Analyze root cause → 4) Write CCS rule → 5) Deploy for all customers within 24h. | "This is the loop: every CVE we find becomes a shield for our users." |
| Fri | Text + Link | Deep dive into one disclosure story (e.g., CrewAI MCP RCE → MSRC). Timeline, root cause, detection rule. Link to blog article. | "How a CVSS 9.8 RCE in CrewAI went from bounty disclosure to detection rule in 24 hours." |

**Target Audience**: Security Researchers, DevSecOps, CTO
**Key Message**: Every vulnerability we discover is weaponized as a defense — real-time rule updates
**CTA**: "See how we close the loop → [link]"

---

### Week 3: "CCS Compliance" — 24-Rule Framework

**Theme**: Structure + Compliance

| Day | Post Type | Content | Hook |
|---|---|---|---|
| Mon | Carousel | "What 24 CCS rules cover." Breakdown by category: RCE (8 rules), SSRF (6), Credential Leak (5), Protocol Abuse (3), Policy (2). | "You can't secure what you can't classify. Here's our taxonomy." |
| Wed | Checklist Image | "CCS Compliance: A 24-point AI Runtime Security Checklist." Printable visual. | "CISO question of the week: 'Are our AI agents compliant?' Here's how to answer." |
| Fri | Text + Link | How the CCS framework maps to SOC2, ISO27001, and OWASP AI Security. Link to blog article. | "24 rules. 80K traces. 1,730+ findings. The CCS framework is the closest thing to an AI runtime security standard today." |

**Target Audience**: CISO, Compliance Officers, Security Architects
**Key Message**: CCS provides a structured, auditable framework for AI runtime security — not a black box
**CTA**: "Download the CCS compliance checklist → [link]"

---

### Week 4: "AI Runtime Threat Landscape" — CISO Guide

**Theme**: Thought Leadership + Industry Perspective

| Day | Post Type | Content | Hook |
|---|---|---|---|
| Mon | Carousel | "7 AI Runtime Threats Every CISO Should Know in 2026." Each threat: name, attack vector, real-world example (from our findings), mitigation. | "The AI attack surface has shifted from the prompt to the runtime." |
| Wed | Text + Image | Heatmap showing vulnerability density across AI frameworks: LangChain, CrewAI, AutoGen, LlamaIndex, LiteLLM, Haystack, Docker MCP, Semantic Kernel. | "We scanned 8 AI frameworks. Every single one had runtime vulnerabilities." |
| Fri | Text + Link | "The CISO's Guide to AI Runtime Security" — comprehensive article covering threat model, detection framework, deployment architecture. Link to blog article. | "AI security isn't about prompt filters anymore. It's about runtime RCE, SSRF, and credential leaks in the agentic data path." |

**Target Audience**: CISO, VP Security, Enterprise Architects
**Key Message**: The AI threat landscape has evolved — runtime security is the new perimeter
**CTA**: "Read the full CISO guide → [link]"

---

### Content Calendar Summary

| Week | Theme | Monday | Wednesday | Friday |
|---|---|---|---|---|
| 1 | 14.5µs Benchmark | Carousel: Speed | Infographic: 24 rules | Blog: Benchmark deep-dive |
| 2 | Bounty to Defense | Timeline: 7 disclosures | Carousel: CVE-to-rule loop | Blog: CrewAI RCE disclosure story |
| 3 | CCS Compliance | Carousel: 24 rules breakdown | Checklist: CCS compliance | Blog: CCS → SOC2/ISO mapping |
| 4 | Threat Landscape | Carousel: 7 threats for CISO | Heatmap: Framework density | Blog: CISO's Guide |

### Posting Best Practices

- **Format**: LinkedIn posts perform best when they start with a hook sentence (not a headline), use line breaks generously, and end with a question or CTA
- **Image specs**: 1200 x 627 px (LinkedIn link preview), 1080 x 1080 px (square carousel), PNG format
- **Carousels**: 3-5 slides max, first slide must hook in < 2 seconds, last slide = CTA
- **Hashtags**: 3-5 max — #AIRuntimeSecurity #CyberSecurity #AI #AIEngineering #LLM
- **Tagging**: Tag 1-2 relevant connections per post (not more — looks spammy)
- **Best time**: Tue-Thu 8:00-10:00 AM US East, 12:00-1:00 PM US East for engagement
- **Frequency**: 3x/week (Mon/Wed/Fri) — don't exceed or you'll annoy the feed

---

## Appendix A: Quick Reference — Which Template for Which Persona

| Persona | Sales Nav Search | Connection Template | First Message Template | Content Week Focus |
|---|---|---|---|---|
| CISO / Head of Security | #1 (CISO AI-Native) | T1 (CISO Angle) | Template A | Week 3 (CCS Compliance), Week 4 (Threat Landscape) |
| DevSecOps / Security Engineer | #2 (DevSecOps Cloud-Native) | T2 (DevSecOps Angle) | Template B | Week 1 (Benchmark), Week 2 (Bounty to Defense) |
| AI Engineer / ML Director | #4 (AI Infra Enterprise) | T3 (AI Engineer Angle) | Template C | Week 1 (Benchmark), Week 2 (Bounty to Defense) |
| CTO / Founder | #6 (MCP AI Agent CTOs) | T4 (CTO/Founder Angle) | Template D | Week 2 (Bounty to Defense), Week 3 (CCS Compliance) |
| Security Researcher | #5 (AI Security Researchers) | — (Engage via comments first) | — | Week 2 (Bounty to Defense) — engage, don't sell |
| Event-based / Any | #1-4 (depending on title) | T5 (Event-Based) | Template E | Match to persona above |

## Appendix B: LinkedIn Profile Optimization Checklist

Before starting outreach, ensure the Correctover company page and your personal profile are optimized:

**Personal Profile**:
- [ ] Headline includes: "AI Runtime Security" + "RCE/SSRF Detection" or similar keywords
- [ ] About section mentions: 14.5µs latency, 24 CCS rules, 7 bounty disclosures, 80K API traces
- [ ] Featured section: link to correctover.com/en, top blog article, one-pager
- [ ] Profile photo: professional, approachable
- [ ] Open to Work: No (signals in-demand, not desperate)

**Company Page**:
- [ ] Tagline updated: "AI Runtime Security — Real-time RCE, SSRF & Credential Protection"
- [ ] Description includes: technical differentiator (14.5µs), social proof (7 bounty disclosures), target customer
- [ ] Featured posts: top 3 blog articles pinned
- [ ] Products tab: add Correctover Essential, Professional, Enterprise tiers
- [ ] Page followers: target 500+ before scaling outreach

---

## Appendix C: Performance Benchmarks

| Metric | Good | Great | Outstanding |
|---|---|---|---|
| Connection accept rate | 25% | 40% | 55%+ |
| First message reply rate | 10% | 20% | 35%+ |
| Meeting booking rate | 5% | 10% | 15%+ |
| POC conversion rate | 20% | 35% | 50%+ |
| Average deal cycle | 60 days | 45 days | 30 days |
| Pipeline per rep/month | $50k | $150k | $300k+ |

**Benchmarking Note**: These are B2B SaaS security benchmarks adjusted for a new category (AI Runtime Security). If numbers are significantly lower, check: targeting accuracy, message personalization depth, or product-market fit signals.

---

*End of LinkedIn Outreach Package. Review quarterly or after any major product release, pricing change, or new bounty disclosure.*

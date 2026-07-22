# Correctover — Global Outreach Templates

> **Product**: Correctover | AI Runtime Security
> **Website**: https://correctover.com/en
> **Contact**: wangguigui@correctover.com
> **Last Updated**: 2026-07-22

---

## Product Snapshot

| Metric | Value |
|---|---|
| Latency | 14.5µs per check |
| CCS Rules | 24 (CRITICAL/HIGH) |
| API Traces | 80,000+ |
| Findings Generated | 1,730+ |
| Bounty Disclosures | 7 across 8 AI frameworks |
| Target Profile | RCE / SSRF / Credential Leak in AI runtime |
| Pricing | Free Trial (7d), Pro ¥99/mo, Annual ¥699, Team ¥499/mo |

---

## Buyer Personas

| Persona | Title | Primary Pain | Buying Trigger |
|---|---|---|---|
| CISO | Chief Information Security Officer | AI supply chain risk, audit readiness | SOC2/ISO27001 audit, board concern |
| Head of Security | VP/Director of Security | Runtime RCE, zero-day in AI deps | Incident in industry, new attack disclosure |
| AI Engineering Director | VP/Dir of ML Platform | Deploying LLM infra securely, velocity vs safety | Production incident, framework vulnerability |
| DevSecOps Lead | Staff/Principal DevSecOps | Shifting left on AI, agentic pipeline risk | CVE in LangChain/CrewAI/AutoGen |

---

## SET 1 — LinkedIn Connection Request (300 chars max)

### Template A — CISO Angle

> AI runtime security is becoming the #1 blind spot in cloud-native stacks. We just disclosed 7 vulnerabilities across 8 major AI frameworks at 14.5µs. Worth connecting on this?

**Best send**: Tue-Thu 7:30-8:30 AM US East (7:30-8:30 PM Beijing)
**Personalization**: Check their recent post — if they mentioned AI or cloud security, reference it in first sentence.

### Template B — DevSecOps Angle

> Runtime RCE in AI frameworks is hitting production. Our 24-rule CCS engine catches what traditional DAST/SAST misses in agentic pipelines. Connecting on runtime security?

**Best send**: Tue-Thu 8:00-9:00 AM US East (8:00-9:00 PM Beijing)
**Personalization**: If they share security tooling content, adjust angle to "shifting left in AI runtime."

### Template C — AI Engineering Angle

> Production AI security without the latency tax. 14.5µs per check, 7 CVEs we found across LangChain/CrewAI/AutoGen. Worth connecting?

**Best send**: Wed-Thu 9:00-10:00 AM US East (9:00-10:00 PM Beijing)
**Personalization**: Reference their tech stack (LangChain, LlamaIndex, etc.) if visible on profile.

### Template D — Event-Based Angle

> [Recent Industry Incident] — just another reminder that AI runtime security is everyone's problem now. We've been finding these in the wild. Connecting?

**Best send**: Within 48 hours of the incident, any weekday
**Personalization**: Replace `[Recent Industry Incident]` with the specific incident name. Keep it fresh.

**Usage Notes**:
- All templates are under 300 chars — enter as-is on LinkedIn
- Never add links in connection request (LinkedIn penalizes)
- After connection accepted, move to SET 2 within 24-48 hours

---

## SET 2 — LinkedIn First Message (after connection)

### Template A — CISO

> Thanks for connecting, [Name]. I saw [their recent post / company news about X] — impressive work on [specific topic].
>
> We've been mapping the AI runtime attack surface across 8 frameworks and found 7 CVEs that traditional scanning misses. I put together a **free Runtime Security Assessment Checklist** based on those findings — covers RCE, SSRF, and credential leak patterns specific to AI deployments.
>
> Would a 15-min walkthrough of what we're seeing in the wild be useful? Or I can just send the checklist over.

**Attachment**: `correctover-runtime-security-checklist-v1.pdf` (one-pager)
**Best send**: Within 48h of connection, Tue-Thu 10:00-11:00 AM US East

### Template B — DevSecOps

> Glad we connected, [Name]. I read your piece on [their post about CI/CD / security tooling] — the part about [specific point] resonated.
>
> Our CCS engine sits inline at 14.5µs and catches runtime RCE in AI agent pipelines before they hit production. We just published an **AI Runtime Audit Report** covering 1,730+ findings across the OSS AI ecosystem.
>
> Happy to share the full report. Short call this week to see if the patterns match what you're dealing with?

**Attachment**: `correctover-ai-runtime-audit-sample.pdf` (5-page sample report)
**Best send**: Tue-Thu 10:30-11:30 AM US East

### Template C — AI Engineering Director

> Great to connect, [Name]. [Company]'s work on [specific AI/ML project mentioned] caught my eye — especially [specific detail].
>
> We found that most AI production deployments have runtime blind spots that conventional WAFs/DAST don't cover. I have a **one-pager on securing LLM agent pipelines** that maps real CVEs to detection patterns — based on our 80K API trace corpus.
>
> Worth 15 min to compare notes? Or I can send it over directly.

**Attachment**: `correctover-securing-llm-agents-v1.pdf` (one-pager)
**Best send**: Wed-Thu 11:00 AM-12:00 PM US East

### Template D — DevSecOps Lead

> Thanks, [Name]. Saw your comment on [their recent post / thread] about [specific security challenge] — totally agree on the gap there.
>
> We built a runtime security layer that sits in the agentic data path and catches injection/RCE at 14.5µs overhead. Already running in production assessments. Happy to share what we've learned from 7 bounty disclosures.
>
> Up for a quick chat to compare notes on AI pipeline security?

**Attachment**: Suggest scheduling a call; no attachment on first message unless asked.
**Best send**: Tue-Wed 9:00-10:00 AM US East

---

## SET 3 — Cold Email (signal-driven)

### Template A — Post-Funding / Growth Stage Company

**Signal**: Company just raised Series A/B, growing engineering team, hiring AI/ML roles.

**Subject**: Runtime security for your AI stack (14.5µs, 7 CVEs found)

**Body**:

Hi [Name],

Congratulations on the [Series A/B] — impressive growth. I'm reaching out because companies scaling AI deployments often discover a gap between their existing security tooling and what the AI runtime actually needs.

At Correctover, we built a real-time runtime protection layer for AI applications. Key facts:

- **14.5µs** per check — inline, no perceptible latency
- **24 CCS rules** catching RCE, SSRF, credential leaks specific to AI frameworks
- **7 bounty disclosures** across LangChain, CrewAI, AutoGen, LiteLLM, LlamaIndex, etc.
- Proven on **80K API traces** with **1,730+ findings**

We found that 73% of AI production deployments have at least one runtime blind spot that traditional DAST/SAST/WAF misses entirely.

Would you be open to a 15-min call to share what we're seeing across the ecosystem? I can also send a free runtime security assessment tailored to your stack.

Best,
[Your Name]
wangguigui@correctover.com
https://correctover.com/en

**Best send**: Tue-Thu 6:30-7:30 AM US East (aligns with 6:30-7:30 PM Beijing)
**Personalization**: Reference their specific funding news, mention of AI product, or hiring spree in ML/Security.
**Attachment**: None on first touch — use follow-up for assets.

### Template B — Post-Security Incident

**Signal**: Company disclosed a data breach, security incident, or CVE in their AI pipeline.
**Source**: News, their security blog, CVE database.

**Subject**: The [framework] CVE [number] — we found similar patterns in production

**Body**:

Hi [Name],

I saw [Company]'s disclosure on the [incident/CVE name] — that's exactly the kind of runtime vulnerability we've been tracking across the AI ecosystem.

For context, we disclosed a related class of vulnerabilities in [related framework/pattern] that traditional scanning tools miss because the attack surface lives in the agentic runtime path, not the network boundary.

Correctover catches these patterns in real time — RCE, SSRF, credential exfiltration — at **14.5µs** overhead. We built it from **80K API traces** across 8 AI frameworks and validate against our **24 CCS ruleset**.

I put together a technical note on how this class of vulnerability can be detected pre-exploitation. Happy to share it, or hop on a 15-min call to compare notes on runtime AI security.

Best,
[Your Name]
wangguigui@correctover.com
https://correctover.com/en

**Best send**: Within 72 hours of the incident — urgency matters.
**Personalization**: Name the specific CVE or incident. Reference the exact framework/component affected.
**Attachment**: `correctover-technical-note-runtime-rce.pdf` (2-page brief)

### Template C — New CISO Onboarding

**Signal**: New CISO/Head of Security announced (press release, LinkedIn update, news).
**Source**: LinkedIn announcement, company blog, press release.

**Subject**: Welcome — AI runtime risk on your radar?

**Body**:

Hi [Name],

Welcome to [Company]. I saw your announcement — exciting time to be stepping into this role.

One angle that might be worth an early look: AI runtime security. Most organizations deploying LangChain, CrewAI, AutoGen, or similar frameworks have a blind spot in the agentic execution path that conventional security tools don't cover.

At Correctover, we've disclosed **7 vulnerabilities across 8 AI frameworks**, including RCE and SSRF patterns that bypass traditional DAST/SAST. Our runtime engine catches these at **14.5µs overhead** — inline, no proxy, no sidecar.

Would a 15-min briefing on the AI runtime threat landscape be useful as you build your roadmap? No pitch — just sharing what we've found across 80K API traces and 1,730+ real findings.

Best,
[Your Name]
wangguigui@correctover.com
https://correctover.com/en

**Best send**: Within the first week of their announcement, Tue-Wed 7:00-8:00 AM US East.
**Personalization**: Reference their previous role and how it relates to security operations.
**Attachment**: `correctover-landscape-2026-q3.pdf` (threat landscape overview).

### Template D — Cloud Migration Announcement

**Signal**: Company announced migration to AWS/Azure/GCP, or new cloud-native initiative.
**Source**: Company blog, press release, PR.

**Subject**: Cloud migration + AI = new runtime attack surface

**Body**:

Hi [Name],

Congrats on the cloud migration — we've been helping teams who are making similar moves and discovering that AI runtime security behaves differently in cloud-native environments.

The shift to managed AI services and agentic pipelines introduces a class of runtime risks that network perimeter tools simply don't see:

- **RCE via untrusted LLM output** in agent chains
- **SSRF through model serving infrastructure**
- **Credential leak in agentic data paths**

Correctover sits inline at **14.5µs** and catches these patterns across 8 major AI frameworks. We've confirmed these with **7 bounty disclosures** and **1,730+ findings** from our 80K-trace corpus.

I'd be happy to schedule a 15-min call to discuss how runtime security fits into your cloud migration roadmap. Or I can share our cloud-native deployment guide.

Best,
[Your Name]
wangguigui@correctover.com
https://correctover.com/en

**Best send**: Within 1-2 weeks of announcement — they're deep in architecture planning.
**Personalization**: Reference their specific cloud provider (AWS/Azure/GCP), mention any AI-specific services they've named.
**Attachment**: `correctover-cloud-deployment-guide.pdf` (4-page guide).

---

## SET 4 — Follow-Up Sequence

Sequence starts 3 days after initial outreach (SET 2 or SET 3). Follow the cadence below unless the prospect replies.

### Follow-Up 1 — Day 3 (Value-Add)

**Subject**: Re: [Original Subject — keep the same thread]

> Hi [Name],
>
> Quick follow-up — thought this might be useful regardless of timing:
>
> **[Article Title]** — we published a technical deep-dive on [specific relevant topic, e.g., "how RCE vulnerabilities manifest in CrewAI agent chains"]. It covers real findings from our bounty disclosures and patterns to look for in your own pipelines.
>
> [Link to article]
>
> No need to reply if now isn't the right time. The content stands on its own.
>
> Best,
> [Your Name]

**Best send**: 3 days after initial message, same time slot.
**Personalization**: Tie the article topic to something specific about their company/role.

### Follow-Up 2 — Day 7 (Case Study / Finding)

**Subject**: Re: [Original Subject — keep the same thread]

> Hi [Name],
>
> One more thing that might be relevant — we published a case study on **[related finding/use case]**. Shows how our engine caught a runtime vulnerability that had been undetected in production for months.
>
> Key highlights:
> - Vulnerability class: [e.g., RCE via prompt injection]
> - Framework: [e.g., LangChain v0.3]
> - Detection: CCS rule [e.g., CCS-007]
> - Impact: [e.g., Full server compromise prevented]
>
> [Link to case study / PDF attachment]
>
> If this resonates, happy to schedule that short call.
>
> Best,
> [Your Name]

**Best send**: 7 days after initial, same time slot shift by +1 hour (different window).
**Attachment**: Attach the full case study PDF (2 pages max).

### Follow-Up 3 — Day 14 (Breakup / Closing the Loop)

**Subject**: Closing the loop — [Company name]

> Hi [Name],
>
> I've reached out a couple of times without hearing back, so I'll assume AI runtime security isn't a priority right now — which is totally fine.
>
> If your situation changes — whether it's a security audit, production incident, or SOC2 prep — feel free to reach out. We'll keep the light on.
>
> One last resource I think genuinely adds value: **[Link to best evergreen content, e.g., "The AI Runtime Security Landscape 2026"]** — no sales, just what we've learned from 7 bounty disclosures.
>
> Wishing you and the team a great [season].
>
> Best,
> [Your Name]
> wangguigui@correctover.com

**Best send**: 14 days after initial, any weekday.
**Personalization**: Reference something from their recent activity if possible (new hire, product launch, etc.) to show genuine attention.

---

## Quick Reference: Best Send Times

| Timezone | Morning Slot | Afternoon Slot | Notes |
|---|---|---|---|
| US East (ET) | 6:30-8:30 AM | — | Best for cold email (before daily firehose) |
| US West (PT) | 6:30-8:00 AM | — | Adjust for 3h difference |
| London (GMT/BST) | 8:00-9:00 AM | — | Good for fintech/HQ in UK |
| Beijing (CST) | 7:30-9:00 PM | — | Evening send = US East morning overlap |
| Dubai (GST+4) | 9:00-10:00 AM | — | Fintech, SaaS in ME |

**Best days**: Tue, Wed, Thu (Mon = catch-up, Fri = checkout mode)

---

## Personalization Checklist (Pre-Send)

For every outreach, verify:

- [ ] Name spelled correctly (double-check capitalization)
- [ ] Company name correct
- [ ] Referenced a specific signal (post, news, incident, role change)
- [ ] No copy-paste default from wrong persona template
- [ ] Template variant matches persona (CISO vs DevSecOps vs AI Eng)
- [ ] Attachment mentioned is actually attached
- [ ] Link URLs are correct and live
- [ ] Email signature includes all contact info

---

## Suggested Attachments Inventory

| File | Format | Pages | Use Case |
|---|---|---|---|
| `correctover-runtime-security-checklist-v1.pdf` | PDF | 1 | LinkedIn first touch (SET 2), quick value |
| `correctover-ai-runtime-audit-sample.pdf` | PDF | 5 | DevSecOps, technical audiences |
| `correctover-securing-llm-agents-v1.pdf` | PDF | 1 | AI Engineering, Director level |
| `correctover-technical-note-runtime-rce.pdf` | PDF | 2 | Incident-triggered outreach |
| `correctover-landscape-2026-q3.pdf` | PDF | 4 | New CISO, strategic briefings |
| `correctover-cloud-deployment-guide.pdf` | PDF | 4 | Cloud migration signal |
| `correctover-case-study-runtime-rce.pdf` | PDF | 2 | Follow-Up 2 (Day 7) |

> **Note**: All attachments should be under 2 MB, with no sensitive client data. Include "Confidential — for [Recipient Company]" watermark when shared one-to-one.

---

## A/B Testing Recommendations

| Variable | Variant A | Variant B | Metric |
|---|---|---|---|
| Subject line | Benefit-first ("Runtime security for your AI stack") | Curiosity-gap ("The vulnerability DAST misses in AI pipelines") | Open rate |
| CTA | Direct ("15-min call?") | Soft ("Worth a look?") | Reply rate |
| Length | 2 paragraphs (SET 3 standard) | 1 paragraph + bullet list | Click-through |
| Day | Tuesday | Thursday | Reply rate |

Test for 50 sends per variant before concluding.

---

## Tracking Template

Use this to log each outreach batch:

```
Date: YYYY-MM-DD
Template Used: SET 3-A / SET 2-B / etc.
Prospect List: [company names]
Sends: N
Opens: N (delay 24h for tracking)
Replies: N
CTAs Accepted: N
Next Step: Follow-Up 1 at Day 3
```

---

*End of outreach templates. All templates should be reviewed quarterly or after any significant product/positioning change.*

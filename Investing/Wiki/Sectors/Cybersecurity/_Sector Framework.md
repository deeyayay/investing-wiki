# Cybersecurity — Sector Framework

_Created: 2026-05-18 | Review quarterly or after major sector events_

---

## Why This Sector Exists in the Portfolio

Cybersecurity spending is one of the few categories that grows during economic downturns. The reason is structural: the cost of a breach far exceeds the cost of prevention. The average enterprise ransomware attack costs $4.5M+ in recovery; a supply chain compromise can cost billions. As organizations migrate to cloud infrastructure, expand their AI workloads, and accumulate more sensitive data, the attack surface grows faster than the security budget. This is not a cyclical IT spend item — it is mandatory infrastructure with regulated compliance requirements in most industries.

The portfolio currently holds **RBRK (Rubrik)** as its single cybersecurity position. Rubrik represents a specific thesis within a large sector: **data security and resilience is the last line of defense when every other security layer has been breached.** Endpoint protection, network security, and identity tools try to prevent attackers from getting in. Rubrik's value proposition is different — it guarantees that when an attack succeeds (and attacks always eventually succeed), the organization can recover its data within hours without paying a ransom.

The broader cybersecurity landscape is covered here as a reference framework for future position additions, but the active thesis is concentrated on data security/backup for now.

---

## How Value Is Created in This Sector

**1. Mandatory spend with regulatory enforcement.** Healthcare (HIPAA), finance (SOC 2, PCI-DSS), and critical infrastructure (CISA directives) mandate data protection and incident response capabilities. This creates a portion of cybersecurity spend that is budget-inelastic — CISOs cannot not spend on it without exposing their organization to regulatory fines and personal liability. Rubrik's compliance and audit readiness features tie directly into this mandatory spend category.

**2. Subscription ARR compounding on a growing installed base.** Best-in-class cybersecurity companies sell multi-year subscription contracts with high net revenue retention (NRR). Rubrik's NRR of 125%+ means existing customers are buying more product annually — they are not just renewing flat. This ARR compounding creates a predictable revenue engine that diverges sharply from one-time license models in terms of valuation quality.

**3. Zero-trust data access as the next architectural shift.** Traditional backup was tape-and-restore: slow, manually-operated, and frequently compromised (attackers target backups deliberately). Rubrik's immutable, zero-trust architecture means attackers cannot encrypt or delete the backup data even if they compromise the primary environment. This architectural differentiation creates a compelling upgrade cycle from legacy backup vendors (Veeam, Cohesity, Commvault) whose architecture was not designed with ransomware in mind.

**4. AI-powered threat intelligence as a moat extender.** Rubrik's Ruby AI layer analyzes backup telemetry to detect anomalous data access patterns before an attack triggers, identify blast radius of a breach, and recommend recovery points that predate the compromise. As the trained dataset of attack signatures grows, the intelligence layer improves — creating a data network effect that legacy backup vendors cannot replicate quickly.

---

## Industry Structure — Value Chain Map

| Layer | Role | Key Players | Moat Type | Margin Profile |
|-------|------|-------------|-----------|----------------|
| **Data Security / Resilience** | Immutable backup, ransomware recovery, data posture | RBRK, Cohesity, Commvault, Veeam | Architecture + AI threat intel + switching costs | High, subscription |
| **Endpoint Security** | Antivirus, EDR, XDR | CRWD, SentinelOne, MSFT Defender | Telemetry network effects + AI model training | High, subscription |
| **Identity & Access Management** | Zero-trust identity, MFA, PAM | Okta, CyberArk, MSFT Entra | Identity graph + SSO integrations | Very high, sticky |
| **Network Security** | Firewall, SASE, SD-WAN | Palo Alto, Zscaler, Fortinet | Platform breadth + secure access architecture | High, expanding |
| **Cloud Security** | CSPM, CWPP, CNAPP | Wiz, Lacework, Prisma Cloud | Cloud-native architecture + API coverage | High, growing |
| **SIEM / SOAR** | Security event correlation and response | Splunk (CSCO), Elastic, IBM QRadar | Data ingestion volume + analyst workflow lock-in | Medium-high |
| **Threat Intelligence** | IOC feeds, dark web monitoring | Recorded Future, Mandiant (GOOGL) | Data collection depth + analyst relationships | Medium |

**Structural insight:** The highest-return cybersecurity positions are in categories with the strongest architectural moats and regulatory mandates: data resilience (RBRK), identity (Okta/CyberArk), and cloud security (Wiz). Network security is a larger market but more commoditized at the firewall layer. Endpoint security is a duopoly forming between CRWD and SentinelOne/MSFT. Future portfolio additions should prioritize categories where the market leader hasn't yet been established.

---

## Company Archetypes and How to Evaluate Them

### Archetype 1: Data Security / Resilience Platform (RBRK)

_Zero-trust data backup and recovery platform — the last line of defense against ransomware_

**What matters most:** ARR growth rate (the primary health metric — should be 25–35% annually), net revenue retention (NRR) — should be 120%+, indicating the existing customer base is expanding, cloud ARR vs. on-premise (cloud is the strategic migration — accelerating cloud mix is a positive re-rating signal), customer count in the enterprise segment (500+ employee organizations pay $100K–$1M+ annually), and gross margin trajectory (should approach 75–80% at scale as cloud mix improves).

**RBRK-specific dynamics:** Rubrik went public in April 2024. The early IPO phase is characterized by high growth rates masking the underlying economics; the key metrics to watch are not revenue but ARR growth and NRR. Rubrik's competitive positioning is against:
- **Legacy backup vendors (Veeam, Commvault):** Architectural replacement cycle. Customers upgrade when a ransomware event or audit failure creates urgency. This is event-driven demand — not a smooth upgrade curve.
- **Cohesity:** Most direct architectural peer. Both sell immutable, zero-trust data platforms. Competitive differentiation is on AI features, cloud integration depth, and enterprise relationships.
- **Microsoft (Azure Backup):** Underpriced competitive threat. MSFT includes basic backup in E5 licensing — watch for MSFT expanding backup capabilities to displace standalone vendors in the SMB segment.

**The Ruby AI layer** is the emerging differentiation: it turns backup telemetry into threat intelligence. Every Rubrik customer's backup data (file access patterns, encryption events, unusual deletion activity) trains the Ruby AI model. The model improves as the customer base grows — a data network effect that is genuinely defensible against competitors.

**Valuation:** EV/ARR is the primary metric for subscription SaaS businesses in the early growth phase. At 10–18x EV/ARR for a 30%+ ARR grower with 120%+ NRR and a clear path to 75%+ gross margins, the risk/reward is attractive relative to peers. Transition to EV/FCF or P/E as profitability emerges.

**Warning signs:** ARR growth decelerating below 20%, NRR declining below 115%, Microsoft materially expanding Azure Backup (enterprise-grade), gross margins failing to expand toward 75% as cloud mix grows, Cohesity closing the feature gap in AI threat detection.

---

### Archetype 2: Endpoint Security Platform (general reference — no current position)

_EDR/XDR with AI-powered threat detection — the primary perimeter tool against modern attacks_

**What matters most:** Annual recurring revenue, net new ARR per quarter (the acceleration or deceleration is the primary signal), net revenue retention (120%+ is the industry benchmark), platform module adoption (EDR → identity → cloud workload = expansion revenue), and competitive win rates vs. SentinelOne and MSFT Defender.

**Valuation:** EV/ARR at 15–25x for a hypergrowth endpoint platform (sub-30% ARR growers should trade at 10–15x). The compression from peak multiples (30–40x ARR in 2021) to current levels (12–18x) reflects rate normalization, not business deterioration.

---

### Archetype 3: Identity / Zero Trust (general reference — no current position)

_Identity is the new perimeter — access control, MFA, and privileged access management_

**What matters most:** Number of enterprise identity integrations (more SSO connections = harder to remove), net revenue retention (identity is extremely sticky — NRR of 110–120%+ expected), customer count growth in >$1M ARR segment, and platform expansion from core IAM to PAM, CIEM, and non-human identity (the emerging market).

---

## Where We Are in the Industry Cycle

**Current phase: Structural growth with consolidation (2025–2028)**

Cybersecurity spend is growing 12–15% annually and is not correlated with IT infrastructure cycles. The key dynamic of this phase is platform consolidation: CISOs are reducing the number of vendors from 30–40 to 10–15 by buying platforms that cover multiple use cases. This consolidation favors companies with broad product portfolios (PANW, CRWD) and creates headwinds for single-product vendors.

For RBRK specifically, the phase is early-commercial: the company IPO'd in 2024, is growing ARR rapidly, and is establishing the data security/resilience category as a distinct, mandatory budget line. The risk is that platform consolidation pushes data protection into a broader security suite rather than a standalone purchase.

**Signals that the data security category is maturing:**
- RBRK NRR stabilizing above 125% (customers expanding — not churning)
- First GAAP profitable quarter for RBRK (projected 2027–2028)
- Consolidation M&A: if PANW or CRWD acquires Cohesity, it validates the category but intensifies competition

**The 2027–2030 horizon:** Cybersecurity AI features (Ruby AI, Charlotte AI at CRWD) become table stakes. The moat shifts toward the company with the most attack telemetry — which favors the largest installed bases.

---

## Valuation Reference Points by Archetype

| Archetype | Primary Metric | Fair Value Range | Peak Enthusiasm | Trough Fear |
|-----------|---------------|-----------------|-----------------|-------------|
| Data Security / Resilience | EV/ARR | 10–18x | 25x+ | 6x |
| Endpoint Security | EV/ARR | 12–20x | 30x+ | 8x |
| Identity / Zero Trust | EV/ARR | 12–18x | 28x+ | 7x |
| Network Security (platform) | EV/ARR | 8–14x | 22x+ | 5x |

---

## Cross-Sector Signal Relationships

Cybersecurity is largely **self-contained** — it does not emit or receive strong signals from other portfolio sectors, but there are important indirect relationships:

| Signal | Cybersecurity read-through |
|--------|-----------------------------|
| AI Infrastructure buildout (IREN, SMCI) | ↑ Attack surface expansion → ↑ demand for data security at hyperscale |
| Enterprise software consolidation (Salesforce, MSFT) | ↑ Risk of MSFT Security Suite displacing best-of-breed vendors in SMB segment |
| Geopolitical escalation / nation-state cyberattacks | ↑ Government and critical infrastructure cybersecurity spending |
| Financial sector volatility (SOFI, HOOD) | → Fintech companies are high-value targets; increased demand for data resilience products |
| GenAI adoption (NVDA, AI Infrastructure) | ↑ AI-powered attacks increase frequency and sophistication → ↑ mandatory security spend |

---

## Sector Bull / Base / Bear Cases

**Bull case (40%):** Ransomware attack frequency doubles as AI-powered attacks automate phishing and lateral movement. Regulatory mandates (SEC cyber disclosure rules, critical infrastructure requirements) force every public company to implement certified backup and recovery. RBRK ARR grows 40%+ for 3 consecutive years; NRR reaches 130%+. Ruby AI becomes the industry standard for breach detection via backup telemetry.

**Base case (45%):** Cybersecurity spend grows 12–15% annually. RBRK grows ARR at 25–30% through 2027, reaching $1.5–2B ARR. NRR holds at 120–125%. Gross margins expand toward 76% as cloud mix crosses 70%. RBRK reaches GAAP profitability in 2028. Platform consolidation creates headwinds in SMB but enterprise expansion accelerates.

**Bear case (15%):** Microsoft expands Azure Backup to enterprise-grade at E5 pricing, displacing Rubrik in mid-market accounts. RBRK ARR growth decelerates to 15–18%. NRR drops below 115% as customers consolidate onto broader MSFT or PANW security platforms. Gross margins stall below 70%. Cohesity closes the product gap and steals competitive wins. RBRK trades at 7–9x ARR (vs. 12–14x in base case).

---

## Key Questions to Ask Every Quarter

1. What is RBRK's ARR growth rate and is it accelerating or decelerating? _(primary thesis health metric)_
2. What is RBRK's net revenue retention? _(customer expansion signal — must hold above 115%)_
3. What percentage of RBRK's ARR is cloud-delivered vs. on-premise? _(architectural modernization pace)_
4. Has Microsoft announced meaningful improvements to Azure Backup at enterprise scale? _(primary competitive threat)_
5. What is RBRK's gross margin trajectory? _(path to long-term 75–80% target)_
6. Is RBRK winning or losing competitive evaluations against Cohesity? _(market share signal)_
7. What is the pace of new enterprise logo additions (customers with >$100K ARR)? _(distribution and market penetration)_
8. Are any major ransomware events driving increased inbound demand for data resilience products? _(event-driven demand catalyst)_

---

## Research Log

- **2026-05-18** — Framework created. Coverage: RBRK. Key gap to close next: populate Earnings & Financials table with ARR and NRR quarterly data; add Microsoft competitive risk section to RBRK Investment Thesis; run `/ticker-monitor --deep RBRK` to capture recent analyst coverage.

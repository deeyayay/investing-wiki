# AI Buildout Opportunity Framework
*Created: 2026-05-20 | Apply this to any sector or company in the AI capital deployment cycle*

---

## Purpose

This framework converts an investment thesis about an AI-adjacent sector or company into a structured evaluation across six axes. It was built from the Agentic Security / NHI analysis in the Cybersecurity sector framework and is designed to be applied consistently across every sector in this wiki.

The central question the framework answers: **what kind of opportunity is this, and what has to be true for it to pay off?**

---

## The Six Evaluation Axes

### Axis 1 — Forcing Function Type

What is causing demand to exist or accelerate?

| Rating | Definition | Example |
|--------|-----------|---------|
| **Deterministic** | Economics or physics make adoption inevitable regardless of specific events. The "when" is uncertain; the "whether" is not. | AI data centers require power (physics). Autonomous vehicles require edge compute (physics). |
| **Probabilistic** | Demand depends on a specific event — a breach, a regulation, a customer announcement, a standard — that may or may not happen in your investment horizon. | NHI/agentic security requires a major breach or mandate to trigger enterprise adoption at scale. |
| **Already Fired** | The forcing function has already happened. Demand exists now; the debate is pace of growth, not existence of demand. | AI training demand for GPUs. Optical transceivers for 800G clusters. AI infrastructure capex committed. |

**Why it matters:** Deterministic and Already-Fired opportunities can be sized with reasonable confidence; Probabilistic ones require explicit option-value thinking — you're underwriting a catalyst, not a trend.

---

### Axis 2 — Order in the AI Value Chain

Where does this sector sit relative to the AI model/product itself?

| Order | Definition | Examples |
|-------|-----------|---------|
| **1st Order** | *Is* the AI product or the primary compute platform. Revenue exists because AI exists. | NVDA (the GPU that runs AI), MSFT Azure AI, OpenAI API |
| **2nd Order** | Infrastructure that AI *requires*. No substitution, no workaround. Demand is derived from AI infrastructure buildout. | Optical transceivers (COHR, LITE), Data center power (VRT, IREN), HBM memory (MU), networking silicon (MRVL, CRDO) |
| **3rd Order** | *Enabled by* AI or *called into existence* by AI's downstream effects. Demand is real but mediated — you need another step in the chain. | Cybersecurity (AI expands attack surface → more security spend), Clean Energy (AI needs power → nuclear re-rate), Agentic identity governance (AI agents need permissions → SAIL) |

**Why it matters:** 1st and 2nd order opportunities tend to have faster, more visible revenue conversion. 3rd order requires more links in the chain — each link is a risk that the thesis doesn't materialize.

---

### Axis 3 — Revenue Timing

When does economic value convert to investable cash flows?

| Rating | Definition |
|--------|-----------|
| **Cash Flows Now** | Revenue and earnings exist today. Valuation is a multiple exercise, not an option-value exercise. |
| **12–24 Months** | Revenue is ramping or approaching inflection. Guidance exists; execution risk is the primary uncertainty. |
| **24–48 Months Option** | Revenue is pre-commercial or contingent on a catalyst (regulatory, product launch, customer win). Discounted option value. |
| **Deep Option (4+ Years)** | Speculative; value primarily depends on a long-dated scenario. High variance, small position sizing warranted. |

---

### Axis 4 — Moat Type

What prevents competition from eroding the margin?

| Moat Type | Mechanism | Duration | Examples |
|-----------|-----------|----------|---------|
| **Ecosystem Lock-in** | Switching cost is extreme because the ecosystem (developer tools, trained models, workflows) is built on the platform | Very long (5–10 yrs) | NVDA CUDA, Salesforce, ServiceNow |
| **Process IP + Certification** | Manufacturing knowledge or regulatory qualification that takes years to replicate | Long (3–7 yrs) | TSMC node leadership, AXTI InP substrates, AMBA automotive ISO 26262 |
| **Supply Scarcity** | Physical constraint that cannot be quickly resolved (land, permits, spectrum, rare earths) | Medium (2–5 yrs; erodes as new supply builds) | IREN permitted power, ASTS FCC spectrum, MP rare earth reserves |
| **Data Network Effects** | Each additional customer/data point makes the product better, creating a self-reinforcing moat | Long (5–10 yrs) | CRWD Threat Graph, SAIL identity graph, OUST sensor fusion datasets |
| **Connector Depth** | Deep integrations into customer workflows that are expensive to rip out | Medium-long (3–7 yrs) | SAIL 150+ enterprise connectors, VRT embedded data center infrastructure |
| **Regulatory Certification** | Barriers created by mandatory certifications that take 18–36 months to obtain | Long but fragile (depends on regulatory stability) | OKLO NRC licensing, AMBA automotive, FDA-cleared medical devices |
| **Cost Curve Leadership** | Lowest cost producer in a commodity space — durable only if process advantage is maintained | Medium (2–4 yrs) | Memory fabs (MU), solar panel manufacturing |

---

### Axis 5 — Cycle Phase

Where in the adoption S-curve is this sector?

| Phase | Characteristics | Investment Implication |
|-------|----------------|----------------------|
| **Phase 1 — Awareness** | Sector exists as a concept; early proof-of-concept deployments; no revenue at scale; specialists only | Deep option sizing; high variance; may require 3–5 year horizon |
| **Phase 2 — Early Adoption** | First customers deploying; revenue visible but not at scale; debate about TAM and timing is active | Option + small position; monitor for forcing function signals |
| **Phase 3 — Forcing Function** | Catalyst fires or becomes clearly imminent; adoption accelerates; institutional attention arrives | Inflection point; highest risk-adjusted entry before consensus forms |
| **Phase 4 — Scale** | Mass adoption underway; revenue visible and growing; consensus recognizes the opportunity; multiples expand | Growth execution play; downside protection diminishes; focus on quality |
| **Phase 5 — Maturity / Commoditization** | Market penetration plateaus; pricing pressure increases; consolidation begins | Harvest or rotate; only hold the last-standing platform players |

---

### Axis 6 — Platform / Bundle Risk

Who could absorb or commoditize this sector's value?

The three dominant platform risks in the AI buildout:

| Platform Risk | Who | Mechanism | Sectors Most Exposed |
|---------------|-----|-----------|---------------------|
| **Hyperscaler vertical integration** | MSFT, AMZN, GOOGL, META | Build in-house what was previously purchased (custom chips, in-house cooling, in-house networking) | Semiconductors (custom silicon), AI Infrastructure (servers, cooling), Networking |
| **NVDA ecosystem expansion** | NVIDIA | Extend platform from GPU to networking (Spectrum-X), storage (Grace-Hopper), software (CUDA ecosystem) | Photonics (CPO), Networking, Edge AI |
| **Microsoft enterprise bundle** | Microsoft | Fold security, identity, and SaaS tools into M365/Azure at package pricing | Cybersecurity, Fintech (payments), Identity/IAM |

**How to assess:** For each sector, ask — "could Microsoft/NVDA/a hyperscaler do this at zero marginal cost by integrating it into their existing platform?" If the answer is yes within 3 years, the moat is weaker than it appears.

---

## The "What You're Actually Buying" Framework

Every AI buildout investment falls into one of four valuation archetypes:

### Type A — Pure DCF
Cash flows exist now, growing predictably. You're buying a multiple of today's earnings or revenue.
- **Apply when:** Revenue timing = Cash Flows Now, Forcing Function = Already Fired
- **Method:** DCF / forward P/E / EV/EBITDA relative to peers
- **Examples:** NVDA data center revenue, VRT backlog, MELI e-commerce

### Type B — DCF + Expansion Option
Core business has cash flows, but AI buildout unlocks a meaningful TAM expansion that is not yet in consensus estimates.
- **Apply when:** Revenue timing = 12–24 months, Forcing Function = Deterministic or Already Fired
- **Method:** Base DCF for existing business + option value (probability × incremental NPV) for expansion scenario
- **Examples:** MRVL (core networking + custom ASIC expansion), SAIL (IGA core + machine identity expansion), COHR (transceiver business + CPO expansion)

### Type C — Option on Catalyst
No meaningful cash flows from AI buildout yet. Entire thesis depends on forcing function firing.
- **Apply when:** Revenue timing = 24–48 months, Forcing Function = Probabilistic
- **Method:** Assign probability to catalyst, model payoff, discount back. Size position as % of portfolio proportional to probability × payoff.
- **Examples:** OKLO (dependent on NRC approval + first reactor commercial), ASTS (dependent on BlueBird constellation + subscriber growth), SAIL NHI thesis (dependent on major breach / enterprise mandate)

### Type D — Compounding Platform
Secular structural growth, no single catalyst required. Compounding returns through multiple cycles.
- **Apply when:** Moat = Ecosystem Lock-in + Data Network Effects, Phase = 3–5, Forcing Function = Already Fired
- **Method:** Quality-adjusted growth multiple; focus on moat durability over 5–7 year horizon
- **Examples:** NVDA CUDA ecosystem, CRWD Threat Graph, MELI financial services network

---

## Sector Comparison Table

*Assessed as of 2026-05-20. Update when sector-level forcing functions change.*

| Sector | Forcing Function | Value Chain Order | Revenue Timing | Primary Moat | Cycle Phase | Platform Risk | Valuation Type |
|--------|----------------|-------------------|----------------|--------------|-------------|---------------|---------------|
| **Semiconductors (AI Compute)** | Already Fired | 1st | Cash Flows Now | Ecosystem lock-in | Phase 4 | Hyperscaler custom silicon | D |
| **Semiconductors (Memory)** | Already Fired | 2nd | Cash Flows Now | Process IP + cost curve | Phase 4 (cyclical) | Commoditization | A |
| **Semiconductors (Custom Silicon)** | Already Fired | 2nd | 12–24 months | Architecture + customer lock-in | Phase 3–4 | Hyperscaler in-house | B |
| **Photonics & Optical** | Already Fired | 2nd | Cash Flows Now / 12–24M | Process IP + supply chokepoints | Phase 3–4 | Silicon photonics / CPO | B |
| **AI Infrastructure (DC Operators)** | Already Fired | 2nd | 12–24 months | Supply scarcity (power/land) | Phase 3–4 | Hyperscaler self-build | B |
| **AI Infrastructure (Thermal/Power)** | Already Fired | 2nd | Cash Flows Now | Connector depth + process IP | Phase 4 | Hyperscaler in-house cooling | A |
| **AI Infrastructure (Networking)** | Already Fired | 2nd | Cash Flows Now | Merchant silicon + software | Phase 4 | NVDA Spectrum-X / InfiniBand | A |
| **Cybersecurity (Perimeter)** | Already Fired | 3rd | Cash Flows Now | Data network effects | Phase 4 | Microsoft bundle (mid-market) | D |
| **Cybersecurity (Agentic / NHI)** | Probabilistic | 3rd | 12–24 months | Connector depth + identity graph | Phase 2–3 | Microsoft Entra bundle | B/C |
| **Robotics & Edge AI** | Deterministic | 2nd | 12–24 months | Process IP + certification cycles | Phase 2–3 | NVDA Jetson platform | B |
| **Clean Energy** | Deterministic | 3rd enabler | 24–48 months | Regulatory certification + scarcity | Phase 1–2 | Utility incumbents + policy | C |
| **Space & Comms** | Probabilistic | 3rd | 24–48 months | FCC spectrum + launch capability | Phase 2 | Starlink / Kuiper | C |
| **Fintech & E-Commerce** | Deterministic (orthogonal) | 3rd | Cash Flows Now / 12–24M | Network effects + bank charter | Phase 3–4 | Big Tech financial services | A/B |
| **Metals & Mining** | Deterministic | 3rd input | Cash Flows Now | Resource endowment + permits | Phase 3 | Recycling / substitution | A |

---

## Common Mistakes When Applying This Framework

**1. Confusing "AI adjacent" with "AI infrastructure."**
Just because a sector benefits from AI doesn't make it 2nd order. Cybersecurity is 3rd order — AI creates the attack surface, security is the response. 3rd order theses require more links to pay off and carry more timing risk.

**2. Treating Probabilistic as Deterministic.**
Clean energy, agentic security, and space connectivity all have plausible AI tailwinds. But "plausible" is not "inevitable in your investment horizon." Probabilistic forcing functions require option-sizing, not full-position conviction.

**3. Underestimating platform risk from NVDA and Microsoft.**
Both companies have the capital, distribution, and ecosystem leverage to absorb adjacent market value. Any sector that sits close to the NVDA GPU stack or the Microsoft enterprise bundle is at risk of being bundled out of existence. The question is not "can they do this?" but "when, and how quickly?"

**4. Confusing revenue timing with moat durability.**
A company generating cash flows now is not necessarily a better long-term investment than a pre-revenue option. Revenue timing answers "when do I get paid?"; moat durability answers "for how long?". Both axes matter. A cash-flowing business with a 2-year moat (commodity hardware) is worse than a pre-revenue business with a 7-year moat (CUDA ecosystem expansion).

**5. Missing the cycle phase inflection.**
The highest return entry points in most sectors are Phase 2→3 transitions — when the forcing function is clearly approaching but institutional coverage is still sparse. By Phase 4, the opportunity is consensus and priced in. The goal is to identify Phase 2 sectors where the forcing function characteristics are deterministic or clearly approaching.

---

## Apply It to a New Sector: Template

Use this structure when evaluating any new sector or company for the AI buildout angle:

```
## AI Buildout Opportunity Profile

**Forcing Function:** [Deterministic / Probabilistic / Already Fired]  
*What is it:* [one sentence]  
*Why it matters:* [one sentence on certainty and timing]

**Value Chain Order:** [1st / 2nd / 3rd]  
*Mechanism:* [how does AI demand flow to this sector?]

**Revenue Timing:** [Cash Flows Now / 12–24M / 24–48M Option / Deep Option]

**Primary Moat:** [type from Axis 4] — [one sentence explaining the specific mechanism]

**Cycle Phase:** [Phase 1–5] — [one sentence on where adoption currently sits]

**Platform Risk:** [who, what mechanism, timeline estimate]

**Valuation Type:** [A / B / C / D] — [one sentence on valuation method]

**What Has to Be True:** [2–3 bullet points of the specific conditions required for this thesis to pay off at the assumed valuation]

**What Kills It:** [2–3 bullet points of the specific scenarios that invalidate the thesis]
```

---

## Framework Maintenance

*Update this document when:*
- A new sector is added to the portfolio (add a row to the Sector Comparison Table)
- A sector changes phase (update the row + note the date and catalyst in the Research Log below)
- A new platform risk emerges (add to Axis 6)

---

## Research Log

- **2026-05-20** — Framework created. Built from Agentic Security / NHI analysis in Cybersecurity sector framework. Covers all 9 portfolio sectors as of this date.

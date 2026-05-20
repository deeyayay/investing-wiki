# AI Infrastructure — Sector Framework

_Created: May 15, 2026 | Review quarterly or after major sector events_

---

## Why This Sector Exists in the Portfolio

AI infrastructure is the physical layer that makes AI possible at scale. Models don't train and serve in the cloud — they run in buildings with power, cooling, networking, and servers. That physical layer is a multi-hundred-billion-dollar buildout happening right now, funded by the most cash-rich companies in the world. The names in this sector are the ones building, equipping, and operating those buildings.

The thesis is distinct from the semiconductor or photonics thesis: **you don't have to pick the winning AI model or the winning GPU — you just need the electricity and the real estate to be scarce.** Every hyperscaler, every AI lab, and every enterprise AI initiative needs power, cooling, and servers. Supply of large-scale, grid-connected, GPU-ready data center capacity is genuinely constrained. That constraint is the moat.

---

## How Value Is Created in This Sector

**1. Power and land scarcity.** The primary bottleneck in AI infrastructure is not GPUs or money — it's permitted, grid-connected power at scale. A 500MW campus takes 5–7 years to permit and build from scratch. Companies that already have permitted power pipelines (IREN's 3GW) have a head start that cannot be quickly replicated. This is a structural moat, not a product advantage.

**2. Vertical integration eliminating margin leakage.** The traditional hyperscaler model rents capacity from REITs like Equinix or Digital Realty, buys servers from OEMs, and pays cloud intermediaries. Vertically integrated operators (IREN) eliminate the landlord markup, the cloud markup, and the OEM margin by owning and operating the full stack. This is why IREN can offer 85% EBITDA margins on the Microsoft contract — there's no middleman.

**3. GPU density and architectural differentiation.** Not all data centers are equivalent. AI clusters require extreme power density (10–50 kW/rack vs. 5–10 kW for traditional compute), liquid cooling, and high-speed networking. Companies that have built to AI specifications — or can retrofit to them quickly — command premium pricing. Those still operating legacy air-cooled facilities cannot.

**4. Anchor tenant lock-in.** Multi-billion-dollar, multi-year contracts with hyperscalers (Microsoft, Amazon, Google) or strategic investors (NVIDIA) create durable revenue visibility. The economics of a 5-year contract with a hyperscaler at guaranteed utilization are fundamentally different from spot-market capacity rental.

---

## Industry Structure — Value Chain Map

| Layer | Role | Key Players | Moat Type | Margin Profile |
|-------|------|-------------|-----------|----------------|
| **Land & Power** | Permitted sites, grid connections, renewable PPAs | IREN, DLR, AMT | Regulatory + location scarcity | High, once built |
| **Colocation / Hyperscale DC** | Facilities, power, cooling | EQIX, DLR, IREN | Relationships + location + scale | Medium-high, recurring |
| **AI Data Center Operators** | Vertically integrated GPU cluster operators | IREN, CoreWeave | Vertical integration + GPU allocation | Very high potential |
| **Servers / Systems** | GPU servers, AI racks | SMCI, DELL, HPE | Cooling innovation + ODM relationships | Low-medium |
| **Cooling & Power** | Liquid cooling, UPS, busbar | VRT, NVENT, EATON | Thermal design IP + installed base | Medium-high |
| **Networking** | High-speed switching for AI clusters | ANET, CSCO, MRVL | Merchant silicon + software stack | High, sticky |
| **Bitcoin Mining Crossover** | Dynamic capacity buffer (GPU/BTC reallocation) | IREN, RIOT, MARA | Optionality + balance sheet | High, volatile |

**Structural insight:** The highest-value positions are where supply is most constrained: permitted power (IREN) and AI-grade cooling at scale (VRT). Server manufacturing (SMCI) has lower moat because GPU allocation from NVIDIA matters more than who builds the enclosure — but SMCI's cooling design advantage (direct liquid cooling) is meaningful during the transition to liquid-cooled racks.

---

## Company Archetypes and How to Evaluate Them

### Archetype 1: Vertically Integrated AI DC Operator (IREN)

_Own the land, power, cooling, and GPU relationships — capture the full stack margin_

**What matters most:** Power utilization rate (MW deployed vs. total permitted), AI Cloud revenue growth rate (QoQ, not just YoY — this business is inflecting), anchor tenant contract depth (not just announced value, but revenue recognition pace), share dilution trajectory (high capex requires equity — watch dilution vs. revenue growth ratio), cash runway vs. buildout timeline.

**What IREN-specific metrics to track:**
- AI Cloud revenue ($33.6M Q3 FY2026, +94% QoQ — this is the primary thesis metric)
- GPU utilization rate (number of GPUs deployed vs. total contracted)
- Sweetwater Campus MW milestones (NVIDIA DSX flagship site)
- Cash: $2.6B as of April 30 (adequate through 2026 buildout; monitor equity raise cadence)

**Valuation:** EV/Revenue during the ramp phase, transitioning to EV/EBITDA as the AI Cloud segment matures. The Microsoft 85% EBITDA margin data point is the best comparable. A fully ramped 460MW / 140K GPU / $3.4B ARR scenario should support a 15–20x EV/EBITDA multiple — back into the stock price from there.

**Warning signs:** QoQ AI Cloud revenue growth decelerating below 30%, GPU deployment falling behind committed timelines, share dilution outpacing revenue growth, anchor customer contract restructuring, power procurement costs rising materially.

---

### Archetype 2: AI Server Manufacturer (SMCI)

_The GPU-in-a-box builder — important but low-moat; differentiated only on cooling_

**What matters most:** Revenue per GPU deployed (SMCI builds at slim margins), direct liquid cooling adoption rate (SMCI's architectural advantage), NVIDIA GPU allocation share (primary constraint on growth), audit / accounting quality (SMCI had a 2024 delay filing — watch compliance track record), gross margin trajectory (should be 15–18% in normalized environment).

**Valuation:** P/E or EV/EBITDA — at 15–25x forward P/E for a 15–20% grower, fair value. The risk/reward is asymmetric on the downside if GPU allocation shifts or accounting concerns resurface.

**Warning signs:** NVIDIA reducing SMCI's GPU allocation (shifts to Dell/HPE), gross margin declining below 14%, regulatory or accounting issues (2024 precedent), hyperscaler in-sourcing server builds.

---

### Archetype 3: Thermal / Power Infrastructure (VRT)

_The picks-and-shovels of power management — every AI data center needs VRT's products_

**What matters most:** Data center order backlog (primary leading indicator — VRT books 12–18 months ahead of revenue), liquid cooling product mix shift (higher margin than air), hyperscaler direct relationship depth (MSFT, GOOGL, AMZN are primary customers), acquisition integration (Generac's data center business).

**What to track:** Order intake QoQ, backlog-to-revenue ratio, liquid cooling revenue as % of total, gross margin on liquid cooling vs. legacy UPS.

**Valuation:** EV/EBITDA or P/E. VRT historically traded at 20–30x P/E during growth phases. The AI DC buildout extends its growth runway meaningfully — a 35–45x P/E may be warranted if order intake is accelerating.

**Warning signs:** Order backlog declining for 2+ quarters, hyperscalers developing proprietary cooling solutions, air-cooled alternatives extending viability (delaying liquid adoption), rising steel/aluminum input costs compressing margins.

---

### Archetype 4: AI Networking (ANET)

_The spine of every AI cluster — high-speed Ethernet switching is mandatory infrastructure_

**What matters most:** Cloud Titan (hyperscaler) revenue growth rate (the primary AI demand signal for ANET), AI backend network spend (spine/leaf topology for GPU clusters — distinct from frontend internet traffic), 800G adoption timeline (the current transition), competitive pressure from Cisco and InfiniBand (NVIDIA's proprietary network, which competes with Ethernet).

**ANET-specific dynamics:** The AI backend networking debate (InfiniBand vs. Ethernet) is the primary controversy. NVIDIA favors InfiniBand for tightly-coupled training clusters; ANET's Ethernet wins on cost and openness for inference and loosely-coupled clusters. Monitor which architecture wins at scale — a decisive InfiniBand victory would compress ANET's AI TAM.

**Valuation:** P/E or EV/Revenue. ANET has historically commanded 35–50x forward P/E given high margins and consistent execution. The AI networking tailwind should sustain growth — but the InfiniBand/Ethernet split is a watch item.

**Warning signs:** Hyperscalers shifting AI backend to InfiniBand, ANET losing Cloud Titan market share to Cisco or white-box alternatives, 800G adoption slower than projected.

---

## Where We Are in the Industry Cycle

**Current phase: Early infrastructure buildout (2025–2028)**

This is the equivalent of the late 1990s when every telecom company was laying fiber — but the difference is the demand is provably monetizable today. Microsoft, Google, and Amazon are earning AI-driven revenue now. The buildout is funded by that revenue, not by speculation.

Phase characteristics right now:
- Power and GPU capacity are the binding constraints — not demand
- Multi-year contracts at premium rates (IREN's Microsoft 85% EBITDA margin is the data point)
- New entrants proliferating (CoreWeave, Lambda, etc.) but differentiated operators pulling away
- Valuations reflect the growth opportunity but not yet the maturity

**The 2028–2030 transition:** As power supply catches up to demand, spot pricing for GPU capacity will compress. Winners will be those with the lowest-cost power (renewable, low-cost grid regions) and highest GPU utilization rates. IREN's mining-to-GPU arbitrage capability and low-cost Texas power position it well for this phase.

**Signals that the buildout phase is ending:**
- Spot GPU instance pricing declining for 2+ consecutive quarters
- Hyperscaler capex guidance cuts (the #1 leading indicator)
- Power development timelines extending further (grid infrastructure bottleneck)
- New entrant price war on colocation rates

---

## Valuation Reference Points by Archetype

| Archetype | Primary Metric | Fair Value Range | Peak Enthusiasm | Trough Fear |
|-----------|---------------|-----------------|-----------------|-------------|
| Vertically Integrated Operator | EV/Revenue (ramp) → EV/EBITDA (mature) | 8–15x rev / 15–20x EBITDA | 25x rev | 3x rev |
| AI Server Manufacturer | Forward P/E | 15–25x | 35x+ | 8x |
| Thermal / Power Infrastructure | Forward P/E or EV/EBITDA | 25–40x | 55x+ | 15x |
| AI Networking | Forward P/E | 30–50x | 65x+ | 20x |

---

## Cross-Sector Signal Relationships

This sector is primarily a **downstream receiver** of signals from Semiconductors and Photonics, and an **upstream emitter** for power/energy infrastructure:

| Signal source | AI Infrastructure read-through |
|---------------|-------------------------------|
| NVDA raises capex or announces new platform | ↑ IREN (GPU deployment demand), ↑ SMCI (server orders), ↑ VRT (cooling demand), ↑ ANET (networking demand) |
| Hyperscaler AI capex guidance raise | ↑ Entire sector — primary leading indicator |
| COHR/LITE optical demand signals | ↑ ANET (co-packaged optics adoption pace) |
| Power grid investment (OKLO, utilities) | → Enables IREN buildout — watch for IREN power procurement announcements |
| IREN Sweetwater Campus milestones | ↑ Emits signal to COHR/LITE/FN/AAOI: hyperscale AI DC at this power density requires massive transceiver volumes |

---

## Sector Bull / Base / Bear Cases

**Bull case (45%):** Hyperscaler AI capex sustains at $300B+/year through 2027. Power permitting accelerates as governments prioritize AI infrastructure. IREN executes to 460MW / $3.4B ARR by end-2026. VRT's liquid cooling becomes the dominant architecture by 2027, pulling forward its revenue recognition. ANET wins the Ethernet-vs-InfiniBand debate at hyperscalers.

**Base case (40%):** Orderly buildout with modest permitting delays. IREN reaches 60–70% of its 2026 targets; dilution is manageable. SMCI margins stabilize after accounting cleanup. VRT backlog grows 25–30% annually. ANET sustains Cloud Titan share.

**Bear case (15%):** Macro recession causes hyperscaler capex pause. Power permitting extends by 18+ months. IREN dilution outpaces revenue ramp, requiring a larger equity raise than guided. SMCI accounting concerns resurface. InfiniBand wins the AI backend networking standard, compressing ANET's AI TAM.

---

## Key Questions to Ask Every Quarter

1. What did MSFT, GOOGL, AMZN, META guide for data center capex? _(sector health check — #1 leading indicator)_
2. What is IREN's AI Cloud QoQ revenue growth rate? _(primary thesis validation metric)_
3. What is IREN's GPU utilization rate and MW deployed vs. total permitted? _(execution scorecard)_
4. Is VRT's order backlog building or depleting? _(18-month forward demand signal)_
5. Is ANET gaining or losing Cloud Titan market share? _(networking competitive positioning)_
6. What is the power development timeline at IREN's Sweetwater and other campuses? _(moat validation)_
7. Is IREN's share dilution (equity raise cadence) outpacing revenue growth? _(primary financial risk)_
8. InfiniBand vs. Ethernet: which architecture is winning at new hyperscaler AI cluster deployments? _(ANET TAM question)_

---

## AI Buildout Opportunity Profile
*See [[AI Buildout Framework]] for axis definitions.*

**Forcing Function:** Already Fired
*What it is:* Hyperscaler AI capex commitments ($300B+/yr in 2025) have already created locked-in multi-year demand for power, cooling, and networking infrastructure — contracts are signed, land is permitted, equipment is on order.
*Why it matters:* Already-Fired allows DCF valuation against visible backlog and revenue; execution risk (construction timelines, dilution, cost overruns) is larger than demand risk.

**Value Chain Order:** 2nd Order
*Mechanism:* Every GPU cluster requires power, cooling, and high-speed networking. No substitution is possible at the infrastructure layer — physics dictates requirements.

**Revenue Timing:** Cash Flows Now (VRT backlog, ANET orders) / 12–24 Months (IREN ramp — AI Cloud revenue inflecting)

**Primary Moat:** Supply scarcity (IREN — permitted power/land; 5–7 yr build lead time) | Connector depth + process IP (VRT — embedded in data center builds; switching costs after installation) | Merchant silicon + software stack (ANET — Ethernet co-packaged optics; 3–5 yr moat)

**Cycle Phase:** Phase 3–4 — Forcing function fired; large-scale buildout underway. VRT and ANET are in Phase 4 (scale). IREN is in Phase 3 (ramp phase; not yet at operating leverage inflection). Infrastructure saturation is years away.

**Platform Risk:** Hyperscaler vertical integration — MSFT building proprietary cooling, AMZN building proprietary networking switches, GOOGL operating its own campuses. Each in-sourcing decision removes a potential revenue pool. The risk is highest for server manufacturers (SMCI); lowest for power/land scarcity plays (IREN).

**Valuation Type:** B (IREN — core ramp + Sweetwater/NVDA option value) | A (VRT, ANET — DCF on visible backlog)

**What Has to Be True:**
- Hyperscaler AI capex stays elevated ($200B+/yr) through 2027 — any multi-quarter deceleration stalls the buildout
- IREN executes on power permitting and GPU deployment timelines without equity dilution outpacing revenue growth
- Liquid cooling becomes the dominant architecture by 2027 (VRT thesis validation)

**What Kills It:**
- Hyperscaler AI spending pause (macro recession or AI ROI disappointment)
- IREN dilution-to-revenue ratio deteriorates — equity raises outpace contracted revenue
- InfiniBand wins the AI backend networking standard decisively, compressing ANET's AI cluster TAM

---

## Research Log

- **2026-05-15** — Framework created. Coverage: IREN, SMCI, VRT, ANET. Key gap to close next: populate SMCI, VRT, ANET ticker notes with Investment Thesis and Management sections — currently only IREN is fully populated.
- **2026-05-20** — Added AI Buildout Opportunity Profile. AI Infrastructure is pure 2nd-order Already-Fired; primary risk is hyperscaler in-sourcing and IREN execution, not demand existence.

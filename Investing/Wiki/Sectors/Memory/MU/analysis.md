# MU — Analysis
*Layer 2 — Thesis, conviction, and scoring. Updated by: /score-ticker, /ticker-monitor (conviction + analyst + catalyst), /add-ticker (initial stub).*
*Last updated: 2026-06-17*

---

## One-Line Thesis
Only US-domiciled HBM supplier — stacked on every NVDA GPU — with structural AI demand tailwind and a NAND upside that the market is underpricing.

---

## Investment Thesis

> **Thesis established:** 2026-05-07
> **Last validated:** 2026-06-17
> **Drift status:** On track — HBM4 ramp on schedule; CY2026 supply contracted; earnings in 7 days (2026-06-24)

Micron is a cyclical semiconductor company that has found a secular growth engine inside the AI capex supercycle. HBM3E is stacked directly onto NVDA's H200 and Blackwell GPUs — roughly 30% of the GPU's bill of materials — meaning every GPU shipped is a Micron revenue event. Historically memory was a brutal commodity business (DRAM, NAND), but HBM is different: it requires advanced packaging expertise, has a limited supplier base (Micron, SK Hynix, Samsung), and commands premium pricing with long-term supply agreements. Micron is gaining share vs. SK Hynix and is the only US-domiciled HBM supplier — giving it geopolitical tailwinds as the US pushes to onshore critical semiconductor supply.

The underappreciated secondary driver is NAND: agentic AI workloads require NVMe enterprise SSDs (RAG knowledge bases, document stores, retrieval indices) and edge NAND (automotive, laptop agents). This is a separate demand vector from HBM that accrues incrementally to Micron's NAND segment. The Technology Preferences registry (Race 1) rates NAND as the preferred AI memory architecture for agentic workloads — Micron has partial exposure to this thesis alongside SNDK (primary exposure).

**Key moat:** One of three HBM suppliers globally; US-domiciled (CHIPS Act); advanced packaging capability; DRAM/NAND vertical integration; long-term supply agreements with HBM pricing discipline.

**Key risks:** Memory cycle downturn in commodity DRAM/NAND; SK Hynix HBM lead; Samsung price competition; CapEx intensity ($25B+); cyclicality.

---

## Scoring Summary
_Last scored: 2026-06-17 | [[Scoring Rubric]]_

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Product (Love Factor) | 3/5 | One of three HBM suppliers; US-domiciled; switching costs high in HBM tier. NAND/DRAM still ~50%+ revenue — commodity competitive dynamics limit score |
| Pricing Power | 3/5 | HBM: long-term supply agreements with premium pricing; FY2025 gross margins +17pp to 41%. Commodity DRAM/NAND is price-taking; mixed story overall |
| Leadership & Alignment | 3/5 | Mehrotra is SanDisk co-founder (founder-equivalent); executed major HBM pivot since 2017; ~$25.4M equity comp aligns incentives. Specific share count not in wiki |
| Financial Health | 3/5 | FY2025 revenue ~$37.4B (+50% YoY), gross margin 41%; HBM ~$8B annualized run rate. Demand chain FCF-funded (NVDA + hyperscalers). $25B+ capex commitment is elevated; balance sheet specifics insufficient in wiki |
| Macro Environment | 4/5 | Multiple secular AI tailwinds; CHIPS Act geopolitical tailwind; NAND is preferred tech for agentic AI (Race 1, partial exposure); HBM is neutral/priced-in per Technology Preferences. 5-year demand visibility |
| Future Potential | 3/5 | HBM4 ramp (CY2026 supply contracted), NAND enterprise SSD (agentic AI), CXL memory modules adjacency. Thesis not yet fully validated beyond HBM; limited early NAND agentic revenue data in wiki |
| **Composite** | **6.5/10** | **Strong** |

**Valuation:** Insufficient data — analyst coverage blank; run /ticker-monitor --deep MU to populate. Earnings in 7 days (2026-06-24).
**Growth Potential:** — (pending real-time data integration)

## Risk Flags
_Evaluated: 2026-06-17_

| Flag | Status | Notes |
|------|--------|-------|
| Capex sustainability | WATCH | $25B+ capex commitment; FCF trajectory positive (FY2025 revenue +50%) but capex scale is aggressive; no debt/EBITDA ratio in wiki — run /ticker-monitor for balance sheet details |
| Demand chain health | CLEAR | Primary HBM customer is NVDA (FCF-funded); hyperscalers are downstream end-customer for AI compute; commodity DRAM/NAND demand diversified |
| Customer concentration | WATCH | NVDA likely top customer given HBM is ~30% of GPU BOM; specific % of revenue from NVDA not in wiki — run /ticker-monitor for 10-K customer data |
| Circular revenue exposure | WATCH | Minor: HBM → NVDA → AI cloud → hyperscaler loop; NVDA and hyperscalers are FCF-funded anchors so loop risk is limited, but neocloud end-customer exposure is partially circular |
| Rate sensitivity | WATCH | Insufficient data on debt terms; $25B+ capex program likely carries variable-rate debt exposure; run /ticker-monitor --deep for 10-K balance sheet |

---

## Conviction Log

| Date | Event | Δ Conviction | Why |
|------|-------|-------------|-----|
| 2026-05-07 | Note initialized; HBM thesis identified | → Neutral | Priority research candidate from NVDA ecosystem map; HBM as structural differentiator from prior memory cycles |
| 2026-05-19 | NVDA Q1 FY2027 earnings beat; MU named as HBM + SSD supplier | ↑ Strengthened | NVDA demand beat = direct pull-through on MU HBM3E allocation and pricing power heading into HBM4 ramp |
| 2026-06-17 | Score-ticker run; composite 6.5/10 Strong | → Neutral | Thesis confirmed: AI HBM demand is structural; NAND underappreciated. Score constrained by insufficient data (analyst coverage, balance sheet, ownership %) and partial tech alignment vs. SNDK pure-play |

---

## Cross-Ticker Signals

| Date | Direction | Other Ticker | Signal | Implication |
|------|-----------|-------------|--------|-------------|
| 2026-05-19 | Receives | NVDA | NVDA Q1 FY2027 earnings event; MU named in earnings shockwave infographic as HBM and SSD supplier | HBM is ~30% of GPU BOM — NVDA demand beat is a direct pull-through on MU HBM3E allocation and pricing power heading into HBM4 ramp |

---

## Catalyst Timeline
- [ ] Q3 FY2026 earnings (2026-06-24) — HBM revenue %, HBM4 ramp update, NAND gross margin recovery
- [ ] HBM4 (>11 Gbps) volume ramp — on track for Q2 CY2026; CY2026 supply already contracted
- [ ] CHIPS Act funding disbursements (Idaho Boise fab, New York fab)
- [ ] SK Hynix / Samsung HBM competitive positioning update
- [ ] AI server demand from hyperscalers (proxy for HBM pull-through)
- [ ] NAND margin recovery as enterprise SSD cycle inflects (agentic AI storage demand)

---

## Analyst Coverage
*(Rating changes, price target moves, notable commentary — append-only)*
*(No entries yet. Run /ticker-monitor --deep MU to populate from EDGAR + news sources.)*

---

## Technology Alignment
*Maps this ticker to active technology races in [[Technology Preferences]]. Drives the Macro Environment score and relative weighting vs. sector peers.*

| Technology | Preference | This Ticker's Exposure | Weighting Implication |
|-----------|-----------|----------------------|----------------------|
| NAND Flash (Race 1) | ↑ High conviction — preferred for agentic AI | Partial (~50%+ revenue) | Market weight (SNDK is the pure-play overweight; MU is partial beneficiary) |
| HBM4 (Race 1) | → Neutral (priced in; GPU-tied) | Partial (HBM narrative; supply agreements through CY2026) | Market weight — HBM thesis is already well-recognized |
| CXL Memory (Race 4 adjacency) | Watch | Indirect (early-stage modules) | No weighting change |

**Net tech alignment:** Partial tailwind — NAND exposure to preferred agentic AI thesis is real but not pure-play. HBM is neutral/priced-in. Net position is market weight vs. memory sector peers; underweight vs. SNDK on tech preference.

---

## Ecosystem Links
- [[SNDK]] — NAND pure-play; primary in Race 1; overweight vs. MU on tech alignment
- [[NVDA]] — Primary HBM demand source; cross-ticker signal emitter (NVDA earnings → MU HBM read-through)
- [[Investing/Wiki/Sectors/Memory/_Supply Chain Map]] — Memory sector supply chain map

# Semiconductors — Sector Framework

_Created: May 15, 2026 | Review quarterly or after major sector events_

---

## Why This Sector Exists in the Portfolio

Semiconductors are the foundational layer of the AI era. Every model trained, every inference served, every data center built requires chips — and the specificity of which chips matters enormously. This is not a monolithic sector: memory behaves differently from compute, compute behaves differently from networking silicon, and test equipment behaves differently from all of them. The portfolio holds semiconductors not as a bet on the sector broadly, but as exposure to specific chokepoint positions: the AI compute monopoly (NVDA), the HBM memory constraint (MU), the custom silicon arms race (MRVL), and the power semiconductor test bottleneck (AEHR).

The investment thesis across all four names is structural, not cyclical: AI capital expenditure is a multi-year, cash-flow-funded buildout by the largest companies in the world. The chips enabling it are not optional and cannot be cheaply substituted. That structural demand makes the sector's near-term cycles more navigable — the question is not "if" but "how much" and "who captures the most."

---

## How Value Is Created in This Sector

**1. Monopoly or oligopoly in a mandatory input.** NVDA's CUDA ecosystem, TSMC's leading-edge process node, and ASML's EUV lithography are the three clearest examples in semiconductors. Within our coverage, NVDA's position is the purest — every major AI workload runs on CUDA, and CUDA runs on NVIDIA GPUs. Switching is not economically viable for frontier models.

**2. Architectural transitions forcing re-procurement.** Each compute generation (H100 → H200 → B200 → Rubin) is a full hardware replacement cycle. Each memory generation (DDR5 → HBM3 → HBM4) requires new validation and qualification. Each networking standard (100G → 400G → 800G Ethernet) forces new switch and NIC purchases. Companies at the frontier of each transition capture outsized margins in the 18–24 months when demand exceeds supply.

**3. Cyclical leverage at the bottom.** Memory (MU) and test equipment (AEHR) are inherently cyclical. The return profile in these names is asymmetric: buy when inventories are elevated and the cycle is clearly bottoming, sell or reduce when lead times collapse and every analyst has upgraded. The cycle bottom is the opportunity, not the mid-cycle consensus.

---

## Industry Structure — Value Chain Map

| Layer | Role | Key Players | Moat Type | Margin Profile |
|-------|------|-------------|-----------|----------------|
| **AI Compute** | GPU/accelerator for training + inference | NVDA, AMD, Intel | CUDA ecosystem + GPU architecture | Very high, expanding |
| **Memory** | HBM (AI), DRAM, NAND | MU, SK Hynix, Samsung | Scale + process IP | Medium, highly cyclical |
| **Custom Silicon** | ASIC/DPU/networking chips | MRVL, AVGO, AMZN/GOOGL | Architecture + customer lock-in | High, stable |
| **Power Semis** | SiC/GaN for EVs, industrials, AI power | ON, WOLF, ST | Process IP + qualification lead | Medium |
| **Test Equipment** | Validating chips (burn-in, wafer-level) | AEHR, AMAT, KLAC, LRCX | Installed base + switching costs | Medium, cyclical |
| **EDA / IP** | Chip design tools and libraries | SNPS, CDNS, ARM | Switching cost moat | Very high, recurring |
| **Foundry** | Manufacturing leading-edge nodes | TSMC, Samsung, Intel | Process IP + capex scale | Medium-high |

**Structural insight:** In semiconductors, the highest-value positions are at the top (NVDA) and at the invisible bottleneck layers (HBM, test). The foundry and memory layers are capital-intensive and cyclical — they create value, but returns cluster at the tails of the cycle. The design/IP layer (NVDA, MRVL, ARM) generates the best risk-adjusted returns over time because capex is light and switching costs are high.

---

## Company Archetypes and How to Evaluate Them

### Archetype 1: AI Compute Platform (NVDA)

_Monopoly ecosystem play with software moat compounding on hardware leadership_

**What matters most:** Data center revenue growth rate (the primary health metric), CUDA adoption as a lock-in signal, hyperscaler capex guidance (leading indicator), competitive benchmarks from AMD/Google TPU/Amazon Trainium (threats to monitor, not yet existential).

**Valuation:** EV/Revenue or forward P/E relative to data center revenue growth. At 50x+ forward P/E, the market is pricing in sustained 20–30%+ earnings growth for 5+ years. The bull case justifies this; the bear case (export controls, capex slowdown) does not. Price in scenarios.

**Warning signs:** Hyperscaler capex guidance deceleration, hyperscaler custom silicon winning non-training workloads (inference is the next battleground), export control expansion, CUDA developer ecosystem cracks (would show as training job migration to alternatives).

**Cross-sector signal:** When NVDA raises capex guidance or announces a new platform → positive read-through for COHR, LITE, FN, AAOI (optical demand), MU (HBM demand), MRVL (networking silicon demand), IREN (AI data center demand).

---

### Archetype 2: Memory (MU)

_Cyclical commodity with AI-specific premium in HBM; buy the trough, sell the consensus upgrade_

**What matters most:** HBM revenue as % of total (growing to 50%+ by 2027 per management targets), DRAM pricing trends (leading indicator: spot vs. contract spread), inventory levels at end-customers (weeks of supply = cycle position), gross margin trajectory (trough margins are the buy signal).

**Valuation:** P/Book or EV/EBITDA adjusted for cycle position. At cycle trough: 1–2x P/Book. At cycle peak: 4–6x P/Book. The HBM mix shift should structurally elevate the midpoint. Key insight: HBM3E is capacity-constrained and the AI-driven demand is sticky — MU is not a pure commodity play anymore, but it's still cyclical.

**Warning signs:** Spot DRAM prices declining for 3+ consecutive months, hyperscalers shifting HBM allocation to SK Hynix/Samsung, MU's HBM yield problems persisting, customer inventory builds resuming.

---

### Archetype 3: Custom Silicon / Networking (MRVL)

_The arms race enabler — custom ASICs for hyperscalers + networking infrastructure for AI clusters_

**What matters most:** Custom ASIC design-win pipeline (hyperscaler ASIC revenue is 3–5 year visibility), Data Infrastructure segment growth (AI-driven networking is the primary growth driver), 5G infrastructure revenue (still a drag — watch for recovery), gross margin expansion (should improve as ASIC revenue mix grows).

**Valuation:** Forward P/E on non-GAAP EPS, adjusted for amortization of acquired IP. MRVL's ASIC revenue has 18–24 month design-to-revenue cycles, so backlog visibility is unusually high. At 30–40x forward P/E for 20–25% EPS growth, the risk/reward is reasonable; above 50x requires accelerating win rates.

**Warning signs:** Hyperscalers slowing custom silicon investment, Google TPU/Amazon Trainium capturing inference at MRVL's expense, 5G recovery failing to materialize, margins stagnating.

**Cross-sector signal:** MRVL networking silicon wins at hyperscalers → positive for ANET (co-packaged optics opportunity) and Photonics names (higher port density = more optical demand).

---

### Archetype 4: Test Equipment — Power Semis (AEHR)

_Small-cap binary: if SiC adoption inflects as expected, AEHR has a near-monopoly on wafer-level burn-in_

**What matters most:** AEHR has one primary product (FOX-XP wafer-level burn-in) for one primary market (SiC power devices for EVs and industrials). Thesis is simple: SiC adoption grows → AEHR system orders grow. The binary question is whether the SiC ramp is on schedule or delayed.

Revenue signals: System shipments (each FOX-XP system is $3–5M), recurring WaferPak consumable revenue, EV production ramp at Tier 1 automotive OEMs (the primary demand driver), and any customer announcements.

**Valuation:** Price to revenue at this stage. AEHR is small enough that one major design-win or system order can be 20–30% of annual revenue. At 10–15x revenue, you're pricing in meaningful growth — verify with quarterly order intake.

**Warning signs:** EV adoption curve slowing (reduces SiC demand timing), a major SiC fab insourcing burn-in capability, AEHR's wafer-level approach losing share to packaged device testing, management guidance cuts.

---

## Where We Are in the Industry Cycle

**AI Compute (NVDA): Early-to-mid hypergrowth (2025–2028)**

The Blackwell → Rubin → Vera Rubin upgrade cycle is a multi-year capex commitment. Hyperscalers have disclosed $300B+ in combined AI capex for 2025 alone. The risk is not demand — it's the pace of supply (TSMC CoWoS capacity, HBM3E production, networking buildout) and the regulatory environment (export controls).

**Memory (MU): Recovery / early-upcycle (2025–2026)**

DRAM pricing recovered through 2025; HBM3E is sold out through 2026 per multiple suppliers. The memory cycle still exists but HBM's AI-driven demand adds a sticky floor beneath commodity DRAM pricing. The next concern is whether non-AI DRAM (PC, mobile) recovery materializes or drags on the blended average.

**Custom Silicon (MRVL): Structural growth, multi-year runway**

Every major hyperscaler now has a custom chip program. MRVL is the primary arms-length ASIC partner (Google, Amazon, Microsoft confirmed). This is a secular growth driver, not a cycle story.

**Power Semi Test (AEHR): Cycle-dependent on EV ramp**

EV adoption timing is the primary risk. SiC penetration into EV drivetrains is ongoing but slower than 2022–2023 projections. AEHR needs sustained EV volume growth to hit its revenue targets.

**Signals that the AI compute phase is ending:**
- Hyperscaler capex guidance cuts for 2+ consecutive quarters
- AI inference monetization disappointing (reduces ROI justification for capex)
- AMD gaining >30% of frontier training workloads
- CUDA alternatives reaching developer critical mass

---

## Valuation Reference Points by Archetype

| Archetype | Primary Metric | Fair Value Range | Peak Enthusiasm | Trough Fear |
|-----------|---------------|-----------------|-----------------|-------------|
| AI Compute Platform | Forward P/E | 30–50x | 65x+ | 20x |
| Memory (cycle-adjusted) | P/Book | 2–4x | 6x+ | 1x |
| Custom Silicon / Networking | Forward P/E | 28–40x | 55x+ | 18x |
| Power Semi Test | EV/Revenue | 8–15x | 25x+ | 3x |

---

## Cross-Sector Signal Relationships

This sector is the primary **upstream emitter** of signals for the rest of the portfolio:

| NVDA signal | Read-through |
|-------------|-------------|
| Raises capex guidance / new platform announced | ↑ COHR, LITE, FN, AAOI (optical demand), MU (HBM), IREN (AI DC buildout) |
| Export control expansion | ↓ Revenue exposure quantification needed; watch China % of data center revenue |
| Hyperscaler capex guidance (MSFT, GOOGL, AMZN, META) | Leading indicator for entire AI infrastructure stack |
| AMD gaining in inference market | → Neutral-to-slight negative for NVDA moat; watch 2-year trend, not one quarter |

| MU signal | Read-through |
|-----------|-------------|
| HBM pricing increases | ↑ Confirms AI compute capex is sustainable |
| DRAM spot prices declining | Early warning for broader semiconductor inventory cycle |

---

## Sector Bull / Base / Bear Cases

**Bull case (45%):** AI capex supercycle extends to 2028+. NVDA maintains 80%+ GPU market share in training. HBM demand grows faster than supply, keeping MU margins elevated. MRVL wins 3+ additional hyperscaler ASIC programs. EV ramp recovers and AEHR books $100M+ in system revenue by FY2027.

**Base case (40%):** Orderly AI capex growth with modest export control headwinds. NVDA grows data center revenue 30–40% annually through 2027. MU HBM captures 50% of revenue by 2027. MRVL compounds at 20–25% EPS growth. AEHR grows slower than hoped as EV ramp delays continue.

**Bear case (15%):** Macro recession + hyperscaler AI spending pause. Export control expansion materially cuts NVDA China revenue. AMD/Google TPU achieve meaningful training share. Memory cycle turns down again. AEHR misses SiC system shipment targets by >30%.

---

## Key Questions to Ask Every Quarter

1. What did MSFT, GOOGL, AMZN, META guide for AI capex? _(sector health check — #1 leading indicator)_
2. Is NVDA data center revenue accelerating, stable, or decelerating? _(CUDA moat check)_
3. What are HBM3E spot prices and lead times? _(MU margin and demand signal)_
4. Has MRVL announced any new hyperscaler ASIC design wins? _(custom silicon TAM expansion)_
5. What is EV production volume at AEHR's top SiC customers? _(AEHR demand driver)_
6. Are AMD MI-series GPUs winning any frontier training workloads? _(NVDA competitive moat)_
7. What are TSMC CoWoS capacity allocations? _(NVDA supply constraint signal)_

---

## Cross-Sector Signal Map (Emitted to Other Portfolio Sectors)

```
NVDA capex guidance raises
  → ↑ Photonics (COHR, LITE, FN, AAOI): optical transceiver demand
  → ↑ AI Infrastructure (IREN, SMCI, VRT): GPU deployment demand
  → ↑ MU: HBM demand
  → ↑ MRVL: networking silicon demand

MU HBM pricing → ↑ AI capex confidence signal for entire stack

MRVL ASIC wins → ↑ ANET (networking co-packaged optics)
```

---

## Research Log

- **2026-05-15** — Framework created. Coverage: NVDA, MU, MRVL, AEHR. Key gap to close next: populate Earnings & Financials tables for MU, MRVL, AEHR with historical data to enable cycle position analysis.

---

## Social Mentions

*Sector-level signals and commentary. Maintained by `/ingest-sentiment`.*

| Date | Signal | Source | Summary |
|------|--------|--------|---------|
| 2026-05-17 | [[2026-05-17-sive-when-i-see]] | tweet | LPK is "the ASML of glass substrates" supplying ~80% of global players; waiting game for volume ramp |
| 2026-05-17 | [[2026-05-17-axti-inp-substrate-export]] | tweet | InP substrate export controls — US/allied leverage over China's frontier semiconductor development |
| 2026-05-17 | [[2026-05-17-stm-mcu-theme-play]] | tweet | MCU theme as the hidden common denominator across space, robotics, AI infrastructure, EVs — STM, TXN, NXPI as top plays |

# AMD — Analysis
*Layer 2 — Thesis, conviction, and scoring. Updated by: /score-ticker, /ticker-monitor (conviction + analyst + catalyst), /add-ticker (initial stub).*
*Last updated: 2026-06-16*

---

## One-Line Thesis
AMD leverages Zen and CDNA architecture leadership to capture data center compute share as the credible, open-source alternative to Nvidia's AI GPU monopoly.

---

## Investment Thesis

> **Thesis established:** 2026-06-16
> **Last validated:** 2026-06-16
> **Drift status:** On track — MI300/MI350 ramping; AI GPU revenue tracking $14-15B CY2026

Advanced Micro Devices designs and sells high-performance CPUs and GPUs across three segments: Data Center (EPYC server CPUs + Instinct AI accelerators), Client (Ryzen desktop/laptop CPUs + Radeon GPUs), and Embedded/Gaming. AMD is fabless — it designs chips and outsources manufacturing to TSMC — which keeps capex light and lets it ride TSMC's leading-edge process nodes. The Data Center segment has become the primary revenue and earnings driver, accounting for $5.8B of Q1 2026's $10.3B total revenue (+57% YoY).

AMD is executing a textbook "credible second source" strategy in AI infrastructure. Hyperscalers and cloud providers are structurally motivated to avoid single-vendor GPU lock-in, and AMD's MI300/MI350 Instinct accelerators have delivered the performance headroom necessary to earn rack space alongside Nvidia. AI accelerator revenue is tracking toward $14–15B in CY2026, up from near-zero in 2022. EPYC server CPUs have taken meaningful share from Intel across every major cloud. Lisa Su's annual cadence of architecture refreshes (CDNA 3 → CDNA 4 → CDNA Next) keeps AMD competitive on a roadmap basis, and ROCm's open-source positioning is a deliberate long-term answer to CUDA lock-in.

AMD's durable advantage rests on three interlocking pillars: (1) proprietary Zen CPU microarchitecture — AMD now leads Intel on performance-per-watt in server; (2) x86 duopoly with Intel — only two companies can design x86 server CPUs, creating a structural floor; and (3) the CDNA accelerator platform paired with ROCm, an open-source software stack that reduces switching costs vs. Nvidia CUDA and appeals to hyperscalers building multi-vendor AI infrastructure.

Nvidia commands ~86% of AI accelerator market share and has an 18-year head start building the CUDA software ecosystem — developer mindshare, pre-trained models, and toolchains are deeply entrenched. ROCm compatibility gaps remain a real friction point in enterprise and research workloads. US-China export controls are directly impairing AMD's China data center revenue (China was ~20–25% of data center sales prior to controls). At ~58x forward P/E, AMD's valuation embeds significant execution on a $14B+ AI revenue trajectory — any guidance miss or hyperscaler capex digestion pause could compress multiples sharply.

**Key moat:** x86 server CPU duopoly + proprietary CDNA architecture + open-source ROCm differentiates AMD as the credible multi-vendor AI alternative.

**Key risks:** Nvidia CUDA ecosystem lock-in, US-China export controls, hyperscaler custom silicon (TPU/Trainium/Maia), and 58x multiple leaving no room for execution misses.

---

## Scoring Summary
_Last scored: — | [[Scoring Rubric]]_

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Product (Love Factor) | —/5 | |
| Pricing Power | —/5 | |
| Leadership & Alignment | —/5 | |
| Financial Health | —/5 | |
| Macro Environment | —/5 | |
| Future Potential | —/5 | |
| **Composite** | **—/10** | |

**Valuation:** — (not yet scored)
**Growth Potential:** — (pending)

---

## Conviction Log
<!-- Append-only. One row per event that shifts or confirms your view. -->
<!-- Δ Conviction: ↑ Strengthened / ↓ Weakened / → Neutral -->

| Date | Event | Δ Conviction | Why |
|------|-------|-------------|-----|

---

## Cross-Ticker Signals
<!-- Log signals this ticker emits to or receives from other monitored names. -->

| Date | Direction | Other Ticker | Signal | Implication |
|------|-----------|-------------|--------|-------------|

---

## Catalyst Timeline
- [ ] Q2 FY2026 earnings (~late July/early August 2026) — data center guidance key
- [ ] MI350 (CDNA 4) volume ramp milestones — watch for hyperscaler design-win announcements
- [ ] ROCm major release — each improvement closes gap to CUDA; watch developer adoption metrics
- [ ] China export control developments — any relaxation is direct upside to data center TAM

---

## Analyst Coverage
*(Rating changes, price target moves, notable commentary — append-only)*

---

## Technology Alignment

| Technology | Preference | This Ticker's Exposure | Weighting Implication |
|-----------|-----------|----------------------|----------------------|
| AI Accelerators (GPU/ASIC) | Strong tailwind | Primary — MI300/MI350 Instinct line | Overweight vs. traditional semi peers |
| Server CPUs (x86) | Tailwind | Primary — EPYC taking Intel share | Positive; structural multi-year share gain |
| ROCm / Open ML Software | Emerging tailwind | Core strategic bet | Long-dated; depends on developer adoption |

**Net tech alignment:** Tailwind — directly exposed to AI infrastructure capex buildout at L05

---

## Ecosystem Links
- [[Compute Hardware/_Sector Framework.md]]
- [[Compute Hardware/NVDA/analysis.md]] — primary competitor; AMD positions as open alternative
- [[Interconnect/CRDO/analysis.md]] — AMD EPYC servers use high-speed SerDes interconnect
- [[Semiconductor Foundry/TSM]] — AMD fabless; fully dependent on TSMC for leading-edge nodes

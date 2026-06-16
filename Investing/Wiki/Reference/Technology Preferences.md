# Technology Preferences Registry
*Last updated: 2026-06-07*
*Purpose: Application-layer-first conviction on which technologies win specific demand waves. Informs portfolio weighting beyond ticker-level scoring. Sector-agnostic — applicable to AI, crypto, healthcare, energy, or any sector where competing technologies create investable differentiation.*

---

## How to Use This Framework

The mental model, in order:

1. **Start at the application layer.** What does the actual deployed product or service do at scale? (An agentic AI workflow is not the same workload as model training. An L2 rollup serves a different user than an L1 chain.)
2. **Derive the technology implication.** What does that behavioral pattern demand from the underlying technology stack?
3. **Name the horse race.** What competing technologies are vying to serve that demand? Document your preferred outcome and the reasoning.
4. **Map to tickers.** Which companies have primary vs. partial vs. indirect exposure to the winning technology?
5. **State the weighting implication.** Adjust position sizing relative to sector peers based on tech alignment.

Conviction shifts here should trigger a Conviction Log entry (`↑` or `↓`) in the relevant `analysis.md` files.

---

## Conviction Scale

| Label | Meaning | Portfolio Action |
|-------|---------|-----------------|
| **High** | Strong application-layer evidence; technology preference durable 2–3+ years | Overweight pure-plays vs. sector peers |
| **Medium** | Directional preference with 1–2 unresolved uncertainties | Slight tilt toward preferred; monitor key inflection signals |
| **Low / Watch** | Early signal; thesis not yet validated by demand data | No weighting change; document reasoning and watch |
| **Resolved** | Race has a clear winner; no longer contested | Lock in weighting; archive entry with outcome noted |

---

## How This Connects to the Scoring Rubric

Technology preference alignment is expressed through the **Macro Environment (criterion 5)**. See the rubric for how primary vs. partial exposure maps to score levels. The **Technology Alignment section in `analysis.md`** is the per-ticker expression of this registry — it makes the connection explicit and auditable rather than buried in a score.

---

---

## Sector Group: AI Ecosystem

---

### Race 1 — Memory Architecture for Agentic AI: NAND vs. HBM4

**Preference: NAND over HBM4 for the agentic AI demand wave**
**Conviction: High**
**Last validated: 2026-06-07**
**Status: Active**

#### Application-Layer Driver

The shift from "AI" to **agentic AI** changes the compute and memory workload profile fundamentally:

| Dimension | Training (consensus thesis) | Agentic AI (current reality) |
|-----------|----------------------------|------------------------------|
| Memory pattern | Streaming weights through on-package bandwidth | Retrieval from large persistent stores (RAG, vector DB, session state) |
| Memory type needed | HBM — on-package, bandwidth-first | NAND + DRAM — NVMe tier plus working memory |
| Read pattern | Sequential weight streaming | Random reads from large context and knowledge stores |
| Persistence required | No — weights live in DRAM/HBM during run | Yes — session state, audit logs, tool-call history must survive restarts |
| Cost driver | FLOPS per dollar (GPU-first) | Storage dollars per agent-hour (cost-per-bit matters) |
| Edge deployment | No — data center only | Yes — automotive, robotics, enterprise laptop agents all need local NAND |

Every enterprise deploying agentic workflows adds NVMe enterprise SSDs (knowledge bases, document stores, retrieval indices), edge NAND (on-device checkpoints and local context for autonomous agents), and data center NAND tiering (hot/warm storage below DRAM, above tape). None of this is HBM. HBM sits on the GPU die — it is a training and frontier inference technology.

#### Why NAND Wins This Workload

- **Non-volatile persistence.** Agent session state must survive power cycles. DRAM and HBM cannot. NAND can.
- **Cost-per-bit economics.** Agentic workloads scale horizontally (many parallel agents), not vertically (bigger GPU). NAND wins cost-per-bit by ~100x over HBM.
- **TAM expansion.** HBM4 TAM is bounded by GPU units shipped. NAND TAM covers every storage tier from hyperscale data center to laptop edge agent — the incremental agentic demand accrues mostly to NAND.
- **Enterprise SSD refresh cycle.** Enterprises standing up RAG systems and document intelligence are buying NVMe SSDs, not HBM stacks. This is a multi-year replacement cycle in early innings.

#### Consensus vs. Reality Gap

| What the Market Believes | What Is Actually Happening |
|--------------------------|---------------------------|
| "Memory = HBM = the AI memory play" | HBM is a GPU-tied, already-recognized story; NAND's agentic AI TAM is underappreciated |
| "NAND is commodity, limited moat" | Leading-edge QLC and enterprise NVMe have meaningful process differentiation; SanDisk/KIOXIA at cutting edge |
| "HBM4 is the next big upgrade cycle" | HBM4 serves incremental GPU bandwidth; NAND serves horizontal scale-out of deployed agentic infrastructure |

#### Ticker Exposure Map

| Ticker | Technology | Exposure Level | Weighting Implication | Notes |
|--------|-----------|----------------|----------------------|-------|
| SNDK | NAND Flash | **Primary** | Overweight vs. memory peers | ~100% revenue from NAND; pure-play enterprise + client SSD |
| MU | HBM4 + NAND | **Partial** | Market weight | HBM is the narrative; NAND is still >50% of revenue. Watch NAND margin recovery as the underappreciated driver |
| LRCX | NAND capex equipment | **Indirect** | No direct weighting change | #1 HARC etch tool for NAND; NAND capex cycle = LRCX revenue pull-through |
| 4369.T | Wafer → NAND fab input | **Indirect** | No direct weighting change | NAND demand expansion pulls silicon wafer volume at Shin-Etsu |

#### Bull Case (2026–2028)
- Enterprise SSD attach per agentic deployment grows from near-zero to standard infrastructure
- Automotive NAND (in-vehicle agents, OTA model updates) is underpenetrated and accelerating
- QLC NAND cost-per-bit reaches crossover displacing hard drives in warm storage tier
- NAND pricing recovers from 2023–2024 oversupply trough; supply discipline restored

#### Bear / Risk
- Compute-in-memory architectures (NDP, PIM) compress the NAND read bottleneck long-term
- Chinese NAND producers (YMTC) gain market access and compress ASPs
- HBM capacity expands faster than expected, pulling investment narrative from NAND
- Agentic workloads shift toward stateless designs (no persistent session state needed)

---

### Race 2 — Compute Architecture for Agentic AI: CPU / Custom ASIC / GPU

**Preference: CPU (orchestration layer) + Custom ASIC (training / frontier inference) — GPU dominant but architecture is bifurcating**
**Conviction: Medium**
**Last validated: 2026-06-07**
**Status: Active**

#### Application-Layer Driver

Agentic AI systems have three distinct compute layers with different optimal silicon:

| Layer | Task | Optimal Silicon | Why |
|-------|------|-----------------|-----|
| **Orchestration** | Tool dispatch, prompt routing, memory management, agent scheduling | **CPU** | Sequential logic, OS calls, I/O scheduling — GPU is overkill and expensive here |
| **Frontier inference** | Running the largest LLMs (multi-billion parameter) | **GPU / Custom ASIC** | Tensor parallelism at scale; GPU first, custom ASIC growing share |
| **Edge inference** | On-device reasoning (vehicles, robots, enterprise laptops) | **NPU / Custom ASIC** | Power-constrained; GPU doesn't fit in a battery-powered device |

The pure-GPU narrative oversimplifies. CPU-bound orchestration layers mean high-core-count server CPUs don't disappear — they become the coordination fabric around GPU inference clusters. ARM's efficiency advantage compounds at the edge: agents running in vehicles, robots, and laptops must operate within strict power budgets.

#### Technology Preference Logic

- **CPUs remain relevant.** Every GPU server still needs 1–2 CPUs to orchestrate workloads. Agentic frameworks (LangChain, CrewAI, AutoGen) run on CPU; only the model inference call hits the GPU.
- **Custom ASICs take training / frontier inference share.** Hyperscaler capex is bifurcating: merchant GPU for general workloads + custom ASIC (TPU, Trainium, MTIA) for optimized training and inference. AVGO and MRVL are the primary beneficiaries of this shift.
- **ARM wins the edge.** NPU IP is the critical differentiator for battery-constrained agents. ARM's ISA is in 99% of smartphones and is rapidly growing in server (Graviton, Neoverse) — the edge inference cycle is the next leg.
- **GPU (NVDA) is still dominant.** CUDA's 4M+ developer ecosystem is an irreplaceable moat. GPU share erodes at the margin to custom ASIC; it does not collapse.

#### Ticker Exposure Map

| Ticker | Technology | Exposure Level | Weighting Implication | Notes |
|--------|-----------|----------------|----------------------|-------|
| ARM | ARM ISA / NPU IP | **Primary** | Overweight for edge inference cycle | 99% of smartphones; fast-growing server; NPU IP is the edge AI core — high P/E reflects this |
| AVGO | Custom ASIC | **Primary** | Overweight for custom silicon wave | Google TPU, Meta MTIA hyperscaler custom ASIC; #1 custom silicon partner |
| MRVL | Custom ASIC + SerDes | **Primary** | Overweight; Amazon Trainium2 design win validates thesis | Custom ASIC + networking PHY; two beneficiary vectors |
| NVDA | GPU (AI accelerator) | **Primary** | Market weight; CUDA moat unrivaled but custom ASIC captures incremental share | Still dominant; position reflects moat not upside from architecture shift |
| AMD | GPU + x86 CPU (hybrid) | **Partial** | Market weight | MI300X credible; EPYC CPU diversification is the hedge play |
| INTC | x86 CPU (server) | **Partial** | Underweight vs. ARM on architecture preference | IFS foundry is a separate thesis; CPU ISA losing server share structurally |

#### Bull Case
- Hyperscaler custom ASIC capex grows from ~10% to ~30% of silicon budget over 3 years
- ARM server CPU reaches 25% of data center sockets by 2028
- Edge AI inference (automotive, robotics) — next 100M unit market — is won by ARM / RISC-V NPU

#### Bear / Risk
- CUDA moat proves stronger than expected; custom ASICs remain sub-scale and high-NRE
- AMD catches NVDA before ARM disrupts CPUs — pure GPU narrative extends another cycle
- RISC-V open-source pressure erodes ARM's edge licensing power

---

### Race 3 — Optical Interconnect: Pluggable Transceivers vs. Co-Packaged Optics (CPO)

**Preference: CPO is the structural winner — but pluggable extends 2–3 more years**
**Conviction: Medium**
**Last validated: 2026-06-07**
**Status: Active**

#### Application-Layer Driver

AI cluster networking at 1.6T+ per port requires optical interconnects. The question is *where* the optic lives relative to the switch ASIC:

- **Pluggable:** Discrete transceiver in a QSFP-DD or OSFP cage, plugged into a switch port. Electrical trace from ASIC to cage = power loss + bandwidth ceiling.
- **CPO:** Optical engine co-packaged directly on or beside the switch ASIC die. Eliminates the electrical trace; lower power, higher bandwidth density.

At 1.6T/port and beyond, the electrical trace to a pluggable cage burns too much power. CPO is the only viable architecture past that threshold.

#### Technology Preference Logic

- **Pluggable wins today (2024–2026).** Installed base of pluggable-capable switches is massive. 400G and 800G pluggables are profitable, deployed at scale. The 1.6T pluggable (100G/lane) extends the runway 2–3 more years.
- **CPO wins at 3.2T+ (2026–2028+).** At 3.2T/port, the power budget for pluggable collapses. Every major switch ASIC roadmap (Broadcom, Marvell, Intel) assumes CPO transition. TSMC's N45SiPh and Intel IFS are the primary SiPh PDK holders for CPO integration.

The investable asymmetry: pluggable pure-plays generate strong free cash flow *now*, while CPO-first companies (pre-revenue) have the higher structural upside but 2–3 year timing risk.

#### Ticker Exposure Map

| Ticker | Technology | Exposure Level | Weighting Implication | Notes |
|--------|-----------|----------------|----------------------|-------|
| AAOI | Pluggable + CPO transition | **Primary** | Overweight on pluggable cycle; watch CPO readiness | 800G VCSEL and EML; CPO development underway — best near-term + optionality |
| SIVE | Pluggable (EML laser chip) | **Primary** | Market weight; near-term revenue; CPO optionality | EML chip supplier; CPO creates EML-on-interposer opportunity |
| COHR | Pluggable (coherent + datacom) | **Primary** | Market weight; CPO is a structural risk for incumbent module revenue | Broadest datacom line; CPO transition risk is highest for established module makers |
| POET | CPO platform (optical interposer) | **Primary (CPO-first)** | High upside if CPO ramps; binary risk if pluggable extends beyond 2027 | Optical interposer is CPO-native; pre-revenue; timing is the key risk variable |
| GLW | Fiber cable | **Indirect** | No weighting change | Fiber demand is agnostic to pluggable vs. CPO; Corning benefits either way |

#### Bull Case
- 1.6T pluggable proves too power-hungry at scale; hyperscalers pull CPO forward into 2026
- POET or another CPO platform wins a major switch ASIC design-in — proof of concept at revenue
- CPO eliminates the QSFP-DD connector tier entirely; incumbent module makers face structural disruption ahead of schedule

#### Bear / Risk
- 1.6T pluggable works well enough at hyperscale; CPO pushed to 2028+ giving pluggable more runway
- CPO integration complexity (co-packaging requires foundry + photonics alignment) causes repeated delays
- CPO solution is captive and in-house (NVIDIA, Intel) — investable pure-plays don't capture the design win

---

### Race 4 — Memory & Storage for Connectomics & Artificial-Brain Workloads

**Preference: A tiered "petabytes + speed" stack — HBF & QLC NAND for capacity-at-bandwidth, HAMR HDD for cold archive, photonic interconnect to move it — not a single "HBM" play**
**Conviction: Watch**
**Last validated: 2026-06-15**
**Status: Active (Watch)**

#### Application-Layer Driver

"Building an artificial brain" (connectomics, whole-brain emulation, large-scale neuroscience) and "running" one (brain-scale inference, invasive BCI) are two different memory/storage problems:

| Dimension | The map (connectome) | The running model (inference / BCI) |
|-----------|----------------------|-------------------------------------|
| Bound by | Capacity & cost-per-bit | Bandwidth & latency |
| Tier | Cold / warm archive | Near-compute working set |
| Data scale | ~1.4 PB per mm³ (Harvard/Google H01, *Science* 2024); whole human brain ≈ exabyte–zettabyte | Neuralink N1 ~1,024 electrodes ≈ ~200 Mbps raw — **6–9 orders of magnitude smaller** than the connectome |
| Winning tech | High-capacity QLC NAND + HAMR HDD + tape/archival | HBM, **HBF**, CXL-pooled memory |

The signal: petabyte-to-exabyte capacity *and* the bandwidth to feed it. That is a tiered hierarchy, not one chip. Today the demand is research/government/pharma (NIH BRAIN CONNECTS, IARPA MICrONS, Allen Institute) — real but long-dated and lumpy, not yet a volume commercial market.

#### Why a Tiered Stack Wins (not HBM alone)

- **Capacity-at-bandwidth bridge = HBF.** SanDisk's High-Bandwidth Flash (HBF) targets ~1.6 TB/s read (within ~2.2% of HBM) at **8–16× HBM capacity** — purpose-built for models/datasets too large for HBM. TAB formed Jul 2025; SK Hynix standardization MOU Aug 2025; samples H2 2026, products 2027–2028.
- **Cold archive = HAMR HDD.** Seagate Mozaic 44TB shipping in volume (Mar 2026), 100TB on the roadmap; HDD still costs **4–22× less per TB** than QLC SSD in 2026, so it owns the exabyte-scale connectome archive tier for years.
- **Movement = photonics.** Moving PB-scale datasets between storage and compute is the "interconnect wall"; CPO / silicon photonics / coherent DWDM (NVIDIA & Broadcom CPO 2025–2026) are the unavoidable tax.
- **Brain-mimicking compute = neuromorphic.** A literal artificial brain is non-von-Neumann (in-memory / spiking). Public exposure is thin and speculative.

#### Consensus vs. Reality Gap

| What the Market Believes | What Is Actually Happening |
|--------------------------|---------------------------|
| "AI memory = HBM" | Capacity-bound brain-scale workloads need NAND/HBF + HDD archive far more than incremental HBM bandwidth |
| "Flash will displace HDD for archive soon" | QLC is still 4–22× costlier per TB than HAMR HDD in 2026; cold-tier displacement slips past 2028 |
| "Neuromorphic is the brain-chip play" | Only one public pure-play (BrainChip), micro-cap and pre-profit; mostly research (Intel/IBM) or private |

#### Ticker Exposure Map

| Ticker | Technology | Exposure Level | Weighting Implication | Notes |
|--------|-----------|----------------|----------------------|-------|
| SNDK | HBF + QLC enterprise NAND | **Primary** | Overweight vs. memory peers | HBF (1.6 TB/s, 8–16× HBM capacity; SK Hynix MOU Aug 2025; samples H2 2026); pure-play NAND post Feb-2025 WDC spin |
| STX | HAMR nearline HDD (cold archive) | **Primary** | Overweight on the archive tier | Mozaic 44TB shipping Mar 2026, 100TB roadmap; HDD retains 4–22× $/TB advantage for cold/nearline |
| MU | HBM + NAND + CXL | **Partial** | Market weight | Only US HBM maker; NAND still >50% of revenue; CXL memory modules |
| ALAB | CXL memory fabric / retimers | **Partial** | Market weight | Memory pooling/expansion between HBM and SSD tiers |
| COHR / LITE / CIEN | Photonic interconnect (data movement) | **Indirect** | No direct weighting change | CPO/EML (COHR; LITE ~50–60% EML share); coherent DWDM scale-across (CIEN) |
| BRCHF | Neuromorphic / in-memory compute | **Speculative** | Starter / watch only | Sole public neuromorphic pure-play (Akida); micro-cap, pre-profit (FY2025 rev ~$1.9M, net loss ~$20M) |
| LRCX | NAND / HARC capex equipment | **Indirect** | No direct weighting change | #1 HARC etch for NAND; capex upcycle pull-through |

#### Bull Case
- Connectome programs scale (NIH BRAIN CONNECTS, IARPA MICrONS), pulling exabyte-class archival demand into commercial cloud over time
- HBF productizes 2027–2028, giving NAND an HBM-adjacent, capacity-led TAM it never had
- QLC/PLC cost-per-bit keeps falling until it crosses into the warm-storage tier, displacing HDD there
- Brain-scale and agentic inference both demand large persistent memory tiers below HBM — exactly HBF/NAND/CXL
- Photonic interconnect becomes mandatory at 1.6T+/CPO, a structural tax that accrues to the optics basket

#### Bear / Risk
- Connectomics is research/government/pharma today — long-dated, lumpy, not a volume market; whole-brain emulation may never become a storage end-market
- HBF is sampling-stage (H2 2026), spec not finalized; meaningful revenue is a 2027–2030 story
- HDD keeps a commanding $/TB lead (QLC 4–22× costlier in 2026), so NAND archival displacement slips
- Neuromorphic has been "near commercialization" for a decade; BrainChip is micro-cap and deeply pre-profit
- A memory oversupply cycle compresses NAND ASPs before the agentic/brain-scale demand materializes

---

---

## Sector Group: Crypto & Digital Assets

*No active technology races yet. Add entries as coverage expands.*

**Candidate races to document when ready:**
- Proof-of-Work vs. Proof-of-Stake (energy/validator economics; mining hardware exposure)
- L1 chain settlement vs. L2 rollup execution (scaling architecture; who captures fee revenue)
- Custodial vs. non-custodial infrastructure (regulatory and security architecture divergence)

---

---

## Sector Group: Healthcare & Biotech

*No active technology races yet. Add entries as coverage expands.*

**Candidate races to document when ready:**
- CRISPR-based gene editing vs. traditional gene therapy vectors (AAV) (delivery mechanism; in-vivo vs. ex-vivo application)
- mRNA platform vs. conventional vaccine / antibody manufacturing (platform breadth; per-dose economics)
- GLP-1 agonist delivery formats: injectable vs. oral (compliance curve; addressable patient population)

---

---

## Cross-Reference Index

| Sector Group | Technology | Preferred? | Primary Tickers |
|---|---|---|---|
| AI Ecosystem | NAND Flash | ↑ High conviction | SNDK |
| AI Ecosystem | HBM4 | → Neutral (priced in) | MU (partial) |
| AI Ecosystem | ARM ISA / NPU IP | ↑ High (edge inference cycle) | ARM |
| AI Ecosystem | Custom ASIC | ↑ Medium | AVGO, MRVL |
| AI Ecosystem | x86 CPU | ↓ Medium (structural share loss) | INTC |
| AI Ecosystem | GPU (AI accelerator) | ↑ High (still dominant) | NVDA |
| AI Ecosystem | Co-Packaged Optics (CPO) | ↑ High (structural, 2027+) | POET |
| AI Ecosystem | Pluggable Transceiver | → Neutral (cycle play, 2024–2026) | AAOI, SIVE, COHR |
| Crypto & Digital Assets | — | — | — |
| Healthcare & Biotech | — | — | — |

---

## Research Log

- **2026-06-07** — Registry created. Framework designed as sector-agnostic with per-sector groupings. Three AI Ecosystem technology races documented with full application-layer reasoning: NAND vs HBM4 (High conviction), compute architecture bifurcation (Medium), pluggable vs CPO (Medium with 2–3 year lag). Placeholder sections added for Crypto & Digital Assets and Healthcare & Biotech.

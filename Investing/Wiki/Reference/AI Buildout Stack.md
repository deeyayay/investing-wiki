# AI Buildout Stack — Canonical Layer Map
*Last updated: 2026-06-10 — adopted the 12-layer vertical model as the canonical taxonomy*

This file is the **authoritative taxonomy** for the wiki, mapped word-for-word from the *AI Buildout Supply Chain* blueprint graphic. The AI buildout is modeled as a single vertical dependency stack — **12 layers** from Application (top) down to Critical Minerals (bedrock), wrapped by **3 cross-cutting rails** (Power Infrastructure, Thermal Management, Security) and capped by the **Edge & Physical AI deployment surface**.

> *Cross-cutting at every layer: **Power comes in**, **Heat comes out**, **Security wraps around** the whole stack. **Edge & Physical AI** is the deployment paradigm — where the stack meets the physical world.*

Each layer is composed of **sub-boxes** (categories). Sub-box **labels are canonical** (verbatim from the graphic); each is wired to an existing `(sector, tier)` in the per-sector `_Supply Chain Map.md` files so the rich tier/company data and chokepoint flags are reused. Where the graphic names a category the knowledge base does not yet cover, the sub-box carries `"gap": true` — it renders muted ("unmapped") and is a coverage gap to fill via `/map-sector` or `/scout-tickers` (see the table at the bottom). Intra-layer groupings (e.g. L07 Scale-Up / Scale-Out / Scale-Across / Components; L10 Lithography) are a lightweight `"group"` **tag** rendered as a visual band — *not* a third drill-down level. The layers are the canonical *navigation and organizing structure*; sector folders remain the physical home of each ticker (see the Monitor Registry).

**Reading the stack:** each layer *runs on* the layer below it. Physical constraints propagate upward (a chokepoint at L9 Foundry starves everything above); demand signals flow downward (an application boom at L1 pulls compute at L5, which pulls silicon at L9–L12). The `⧫` marker flags supply-chain chokepoints.

The `daily-dashboard` skill reads the JSON block below to regenerate the dashboard's `STACK` object. It is the single source of truth — keep it in sync with `Investing/Output/Dashboard/index.html`.

---

## The 12 Layers

| # | Layer | What it is | Feeding sector(s) |
|---|-------|------------|-------------------|
| L01 | **Application** | AI-native products & vertical apps | Fintech & Commerce AI, Robotics & Edge AI |
| L02 | **AI Model** | Foundation models, alignment, training data | AI Model Infrastructure |
| L03 | **Software Infrastructure** | Orchestration, serving, MLOps, APIs | AI Model Infrastructure |
| L04 | **Cloud Infrastructure** | Hyperscalers, neoclouds, colocation, storage | Compute Infrastructure |
| L05 | **Compute Hardware** | GPUs, custom ASICs, CPUs, design IP | Semiconductors |
| L06 | **Memory** | HBM, HBF, DRAM, NAND, LPDDR | Semiconductors (IDMs), Memory (NAND pure-play) |
| L07 | **Interconnect** | Networking silicon, optics, SerDes, fiber | Compute Infrastructure, Photonics & Optical, Semiconductors |
| L08 | **Advanced Packaging** | CoWoS, stacking, IC substrates | Semiconductors, Electronic Components |
| L09 | **Semiconductor Foundry** | Leading-edge & specialty wafer fab | Semiconductors |
| L10 | **Semiconductor Equipment** | Litho, deposition/etch, metrology, test | Semiconductors |
| L11 | **Semiconductor Materials** | Wafers, photoresist, chemicals, substrates | Semiconductors, Electronic Components |
| L12 | **Critical Minerals & Raw Elements** | The bedrock — mined & refined inputs | Materials & Mining |

### Cross-cutting rails + deployment surface

| Panel | Side | Flow | Function | Feeding sector(s) |
|-------|------|------|----------|-------------------|
| **Power Infrastructure** | left | power in | Powers the entire stack: generation → grid → rack → board | Energy & Power, Semiconductors (power devices) |
| **Thermal Management** | right | heat out | Cools compute & memory (cross-cuts L4–L9) | Compute Infrastructure (cooling) |
| **Security** | right | wraps | Secures every layer of the stack | Cybersecurity |
| **Edge & Physical AI** | right | *deployment surface* | Where the stack deploys into the physical world — plus the parallel-compute paradigms (quantum, neuromorphic, photonic) that sit beside it | Robotics & Edge AI |

Power, Thermal and Security are true **cross-cutting rails** — they touch every layer. **Edge & Physical AI** is reclassified as the stack's **deployment surface** (the physical-world counterpart to L01's software output), carrying two tag groups: *Edge & Physical AI* and *Parallel Compute Paradigms*. It is folded into the single ecosystem view — not a separate tab.

---

## D1–D5 crosswalk (legacy)

The previous five-dimension stack is superseded but maps cleanly onto the layers, so historical notes still resolve:

| Legacy | Maps to layers |
|--------|----------------|
| D5 — AI Applications | L01 + Edge rail |
| D4 — AI Enablement | L02, L03 + Security rail |
| D3 — AI Infrastructure | L04 + Power & Thermal rails |
| D2 — AI Connectivity | L07 (interconnect) |
| D1 — AI Manufacturing Base | L05, L06, L08–L12 |

---

## Machine-readable definition

```json
{
  "generated": "2026-06-20",
  "layers": [
    {"num":"01","name":"Application","hue":235,"tag":"AI-native apps · agents · vertical SaaS","boxes":[
      {"label":"AI Assistants & Chatbots","gap":true,"chips":["META","GOOGL","MSFT"]},
      {"label":"Agentic AI Platforms (multi-step reasoning, tool use)","gap":true,"chips":["PLTR"]},
      {"label":"Enterprise AI SaaS (Copilot-style integrations)","gap":true,"chips":["MSFT","CRM"]},
      {"label":"AI-Native Vertical Applications (coding, video, drug discovery)","sector":"Application","slug":"application","tier":"AI-Native Fintech & Commerce","chips":["MELI","SOFI","HOOD","NU"]}
    ]},
    {"num":"02","name":"AI Model","hue":255,"tag":"foundation models · serving · agents","boxes":[
      {"label":"Foundation Models (LLMs, multimodal)","sector":"AI Model","slug":"ai-model","tier":"Foundation Model Development","chips":["META"]},
      {"label":"Fine-tuned / Specialized Models","sector":"AI Model","slug":"ai-model","tier":"Alignment & Safety Tuning","chips":[]},
      {"label":"Inference Serving Infrastructure","sector":"AI Model","slug":"ai-model","tier":"Inference Serving & Scaling","chips":[]},
      {"label":"Model Orchestration & Agentic Frameworks","sector":"AI Model","slug":"ai-model","tier":"Model API & Developer Platform","chips":["CFLT"]}
    ]},
    {"num":"03","name":"Software Infrastructure","hue":268,"tag":"frameworks · kernels · orchestration","boxes":[
      {"label":"ML Frameworks (training)","sector":"Software Infrastructure","slug":"software-infrastructure","tier":"ML Frameworks","chips":["CRWV","AMD"]},
      {"label":"GPU Programming Layer (low-level kernels)","sector":"Software Infrastructure","slug":"software-infrastructure","tier":"GPU Programming Layer","chips":["NVDA","AMD"]},
      {"label":"Distributed Training Systems","sector":"Software Infrastructure","slug":"software-infrastructure","tier":"Distributed Training Systems","chips":[]},
      {"label":"Container Orchestration (Kubernetes)","sector":"Software Infrastructure","slug":"software-infrastructure","tier":"Container Orchestration & MLOps","chips":["DDOG","SNOW","PLTR","MDB"]},
      {"label":"Inference Optimization Stack","sector":"Software Infrastructure","slug":"software-infrastructure","tier":"Inference Optimization Stack","chips":[]}
    ]},
    {"num":"04","name":"Cloud Infrastructure","hue":288,"tag":"hyperscalers · neoclouds · colocation","boxes":[
      {"label":"Hyperscaler Clouds","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Hyperscaler & Colocation Operation","chips":["MSFT","AMZN","GOOGL","ORCL"]},
      {"label":"NeoClouds (GPU-specialized)","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"NeoClouds & GPU-Specialized Cloud","chips":["CRWV","IREN"]},
      {"label":"Edge / Inference Colocation","gap":true,"chips":["EQIX","VRT"]},
      {"label":"Data Center Colocation","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Data Center Facility & MEP","chips":[]}
    ]},
    {"num":"05","name":"Compute Hardware","hue":55,"tag":"GPUs · ASICs · CPUs · NICs","boxes":[
      {"label":"Training GPUs","sector":"Compute Hardware","slug":"compute-hardware","tier":"AI Training GPUs","chips":["NVDA","AMD"]},
      {"label":"Inference GPUs","sector":"Compute Hardware","slug":"compute-hardware","tier":"AI Inference GPUs","chips":["NVDA","AMD"]},
      {"label":"Custom AI ASICs (hyperscaler silicon)","sector":"Compute Hardware","slug":"compute-hardware","tier":"Custom AI ASICs","chips":["AVGO","MRVL"]},
      {"label":"Dedicated Inference Accelerators","sector":"Compute Hardware","slug":"compute-hardware","tier":"Dedicated Inference Accelerators","chips":[]},
      {"label":"Server CPUs (orchestration, agentic workloads)","sector":"Compute Hardware","slug":"compute-hardware","tier":"Server CPUs","chips":["ARM","INTC"]},
      {"label":"Networking ASICs (switch silicon)","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Switch ASIC & NIC Silicon","chips":["ANET","AVGO","MRVL"]}
    ]},
    {"num":"06","name":"Memory","hue":92,"tag":"HBM · HBF · DRAM · NAND · LPDDR","boxes":[
      {"label":"HBM (current AI server standard)","sector":"Memory","slug":"memory","tier":"HBM (High-Bandwidth Memory)","chips":["MU","000660.KS","005930.KS"]},
      {"label":"HBF (high-bandwidth flash)","sector":"Memory","slug":"memory","tier":"HBF (High-Bandwidth Flash)","chips":["SNDK","000660.KS"]},
      {"label":"DRAM (system memory)","sector":"Memory","slug":"memory","tier":"DRAM (System & Server Memory)","chips":["MU","005930.KS","000660.KS"]},
      {"label":"NAND Flash (storage)","sector":"Memory","slug":"memory","tier":"NAND Flash (Storage)","chips":["SNDK","285A.T","005930.KS","MU"]},
      {"label":"LPDDR (mobile / edge inference)","sector":"Memory","slug":"memory","tier":"LPDDR (Low-Power & Edge Memory)","chips":["MU","005930.KS"]}
    ]},
    {"num":"07","name":"Interconnect","hue":42,"tag":"scale-up · scale-out · scale-across","boxes":[
      {"label":"Co-Packaged Optics (CPO)","group":"Scale-Up · within the rack, chip to chip","sector":"Interconnect","slug":"interconnect","tier":"Co-Packaged Optics (CPO)","chips":["COHR","LITE"]},
      {"label":"NVLink-style fabrics","group":"Scale-Up · within the rack, chip to chip","sector":"Interconnect","slug":"interconnect","tier":"NVLink-Style GPU Fabrics","fn":"Proprietary high-bandwidth GPU-to-GPU interconnect fabric — NVLink and NVSwitch — connecting GPUs within a server node or multi-node DGX SuperPOD at 900GB/s bidirectional per link, enabling all-reduce and collective communication without traversing the PCIe bus. NVLink is NVIDIA's answer to the distributed training bandwidth bottleneck: by bypassing PCIe and using direct GPU-to-GPU copper or optical links with dedicated NVSwitch routing chips, NVLink achieves 18x the bandwidth of PCIe Gen4. NVIDIA's NVLink fabric is a closed proprietary system with no third-party silicon alternatives at comparable bandwidth — the defining scale-up interconnect for all NVIDIA GPU clusters.","chokepoint":"Y","capital_intensity":"Very High","moat_type":"Proprietary closed ecosystem — no third-party silicon alternatives","margin_profile":"Very High","chips":["NVDA","ALAB"]},
      {"label":"On-package optical engines","group":"Scale-Up · within the rack, chip to chip","sector":"Interconnect","slug":"interconnect","tier":"Silicon Photonics — On-Package Engines","chips":["POET","LWLG"]},
      {"label":"SerDes · Retimers","group":"Scale-Up · within the rack, chip to chip","sector":"Interconnect","slug":"interconnect","tier":"SerDes & Retimer Silicon","fn":"Serializer/deserializer (SerDes) PHY circuits and signal retimer chips that amplify, equalize, and re-time high-speed electrical signals at 112G/224G PAM4 per lane across PCB traces, backplane connectors, and copper cable assemblies inside AI servers and rack-to-rack cable runs. SerDes and retimer silicon is the signal integrity foundation of every AI cluster: as GPU-to-switch links operate at 112G/224G per lane, electrical signal degradation over connectors and traces requires retimer chips to restore signal quality before entering the switch ASIC. Credo Technology's AEC (active electrical cable) architecture integrates SerDes and retimer into the cable assembly, reducing PCB component count.","chokepoint":"Partial","capital_intensity":"Low–Medium","moat_type":"Process IP + Switching cost (recipe qualification)","margin_profile":"Very High","chips":["CRDO","ALAB"]},
      {"label":"Pluggable Optical Transceivers","group":"Scale-Out · between racks, within data center","sector":"Interconnect","slug":"interconnect","tier":"Pluggable Optical Transceivers","chips":["COHR","LITE","FN","AAOI"]},
      {"label":"Linear Pluggable Optics (LPO)","group":"Scale-Out · between racks, within data center","sector":"Interconnect","slug":"interconnect","tier":"Linear Pluggable Optics","chips":["AAOI"]},
      {"label":"High-speed Ethernet / InfiniBand","group":"Scale-Out · between racks, within data center","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"High-Speed Networking","chips":["ANET","AVGO"]},
      {"label":"Coherent Optical Transport","group":"Scale-Across · between data centers","sector":"Interconnect","slug":"interconnect","tier":"Coherent Optical Transport","chips":["CIEN"]},
      {"label":"Long-haul DWDM","group":"Scale-Across · between data centers","sector":"Interconnect","slug":"interconnect","tier":"Long-Haul DWDM","chips":["CIEN","GLW"]},
      {"label":"External Light Sources (CW lasers)","group":"Components · used across all three scales","sector":"Interconnect","slug":"interconnect","tier":"Photonic Device Fabrication","chips":["IPGP","LITE","LASR"]},
      {"label":"Optical Engines","group":"Components · used across all three scales","sector":"Interconnect","slug":"interconnect","tier":"Silicon Photonics — Discrete Optical Engines","chips":["POET","IPGP"]},
      {"label":"Fiber Array Units (FAU)","group":"Components · used across all three scales","sector":"Interconnect","slug":"interconnect","tier":"Fiber Array Units (FAU)","chips":["FOCI"]},
      {"label":"Optical Connectors","group":"Components · used across all three scales","sector":"Interconnect","slug":"interconnect","tier":"Passive Optical Components","chips":["GLW","VIAV"]},
      {"label":"Fiber Cables","group":"Components · used across all three scales","sector":"Interconnect","slug":"interconnect","tier":"Fiber Cables & Preforms","chips":["GLW"]}
    ]},
    {"num":"08","name":"Advanced Packaging","hue":150,"tag":"CoWoS · stacking · substrates","boxes":[
      {"label":"Wafer-Level Packaging (CoWoS, SoIC)","sector":"Advanced Packaging","slug":"advanced-packaging","tier":"CoWoS & SoIC Wafer-Level Packaging","fn":"Integrate multiple heterogeneous die — GPU compute die, HBM memory stacks, I/O chiplets — onto a silicon interposer via CoWoS or via direct 3D hybrid bonding using SoIC, enabling bandwidth and performance levels that monolithic die cannot achieve. CoWoS (Chip-on-Wafer-on-Substrate) is the TSMC advanced packaging process that NVIDIA's H100/H200/B200 depend on: GPU and HBM are placed on a shared silicon interposer enabling 1.2TB/s memory bandwidth. TSMC CoWoS capacity was the binding constraint on H100 production in 2023 with 52+ week lead times. SoIC (System on Integrated Chips) advances further with face-to-face hybrid bonding at <10-micron bump pitch for TB/s die-to-die bandwidth.","chokepoint":"Y","capital_intensity":"Very High","moat_type":"Process IP + Scale (TSMC near-monopoly)","margin_profile":"Very High","chips":["TSM","AMKR","BESI"]},
      {"label":"HBM Stacking & Integration","sector":"Advanced Packaging","slug":"advanced-packaging","tier":"HBM Stacking & Memory Integration","fn":"Stack DRAM die 8–16 high using through-silicon vias (TSVs) and mount the resulting HBM stack on-package beside the GPU via a CoWoS interposer — achieving ~1.2TB/s memory bandwidth per stack at HBM3e, scaling with HBM4. HBM stacking is the capacity-constrained chokepoint that limits AI accelerator production: each H100 requires 6 HBM3e stacks, each requiring TSV bonding, micro-bump attach, and interposer integration at TSMC's CoWoS line. Supply is allocated 12–18 months ahead of production — SK Hynix (~50%), Samsung, and Micron are the only three manufacturers capable of producing HBM at commercial volumes. The transition from HBM3 to HBM3e to HBM4 is accelerating, each generation requiring TSMC CoWoS interposer redesign.","chokepoint":"Y","capital_intensity":"Very High","moat_type":"TSV process IP + Scale (three-supplier oligopoly)","margin_profile":"High (cyclical)","chips":["MU","TSM"]},
      {"label":"FC-BGA Substrates","sector":"Electronic Components","slug":"electronic-components","tier":"IC Substrate Manufacturing","chips":[],"choke":true},
      {"label":"Glass Core Substrates (emerging)","sector":"Electronic Components","slug":"electronic-components","tier":"Substrate & Laminate Materials","chips":["GLW","INTC","LPK"]},
      {"label":"Thermal Interface Materials (TIM)","gap":true,"chips":[]}
    ]},
    {"num":"09","name":"Semiconductor Foundry","hue":162,"tag":"leading-edge · specialty · OSAT","boxes":[
      {"label":"Leading-Edge Logic Foundry (3nm, 2nm)","sector":"Semiconductor Foundry","slug":"semiconductor-foundry","tier":"Leading-Edge Logic Foundry","fn":"Execute 1,000+ precisely sequenced process steps — EUV lithography, ALD gate dielectric, fin/nanosheet patterning, metal interconnect, CMP — to manufacture transistors at 3nm, 2nm, and below for the AI accelerators, CPUs, and custom ASICs that power the AI buildout. Leading-edge logic foundry is the single most capital-intensive and geographically concentrated manufacturing activity in the AI supply chain: TSMC and Samsung together produce 100% of the world's sub-5nm chips and >90% of sub-7nm chips. A 3nm wafer costs $17,000–$20,000 to process; a leading-edge fab costs $20B+ to build and 18 months to qualify. No AI training GPU exists without leading-edge foundry access — TSMC's N4P node is the exclusive manufacturing process for NVIDIA's H100 and H200.","chokepoint":"Y","capital_intensity":"Very High","moat_type":"Process IP + Scale (two-supplier duopoly TSMC/Samsung)","margin_profile":"Very High","chips":["TSM","INTC"]},
      {"label":"Specialty / Mature Logic Foundry (analog, mixed-signal)","sector":"Semiconductor Foundry","slug":"semiconductor-foundry","tier":"Specialty & Mature Node Foundry","fn":"Manufacture analog, mixed-signal, RF, power management, and specialty digital chips at 28nm–180nm nodes using differentiated process modules (BCD, HV CMOS, RF CMOS, SOI, SiGe) that leading-edge foundries have discontinued. Specialty foundry is a structurally growing market: the AI buildout requires analog front-ends, power management ICs, SerDes PHYs, and RF components that are not manufactured at 3nm — their performance metrics (voltage headroom, breakdown voltage, noise figure) improve with specialized process architectures, not transistor scaling. GlobalFoundries' 22FDX and 12LP platforms, XFAB's BCD and automotive processes, and Tower Semiconductor's RF and specialty platforms serve these requirements at mature nodes where capital intensity is lower and margins are more stable than leading-edge.","chokepoint":"N","capital_intensity":"Medium–High","moat_type":"Specialty process differentiation + Customer qualification lock-in","margin_profile":"Medium–High","chips":["GFS","XFAB"]},
      {"label":"Silicon Photonics Foundry","sector":"Semiconductor Foundry","slug":"semiconductor-foundry","tier":"Silicon Photonics Foundry","fn":"Fabricate silicon photonic integrated circuits — waveguides, ring resonators, Mach-Zehnder modulators, and germanium photodetectors — on standard CMOS-compatible silicon wafers using photolithography adapted for optical device fabrication. Silicon photonics foundry services enable the production of optical transceivers, LIDAR chips, quantum photonic processors, and co-packaged optical engines at CMOS foundry scale and cost. GlobalFoundries' GF Fotonix process (300mm SiPh), TSMC's iSiPP (integrated Silicon Photonics Platform), and Intel Foundry's integrated photonic process are the primary production-capable SiPh foundries. SiPh foundry capacity is gated by germanium deposition expertise and passivation chemistry that not all CMOS fabs can replicate.","chokepoint":"Partial","capital_intensity":"High","moat_type":"Process IP + Limited number of qualified fabs","margin_profile":"High","chips":["GFS","POET","INTC"]},
      {"label":"Compound Semiconductor Foundry (GaN, SiC, InP)","sector":"Semiconductor Foundry","slug":"semiconductor-foundry","tier":"Compound Semiconductor Foundry","fn":"Fabricate GaN, SiC, InP, and GaAs semiconductor devices using specialized foundry processes not available at CMOS silicon fabs — MOCVD epitaxial growth, III-V wet etch, and ohmic contact metallization adapted for compound semiconductor crystal systems. Compound semiconductor foundries serve three high-value markets: GaN-on-SiC power and RF devices (5G base stations, radar, AI datacenter power), InP and GaAs photonic devices (datacenter laser chips, photodetectors), and SiC power MOSFETs (EV inverters, datacenter UPS). These foundries are structurally supply-constrained: the MOCVD epitaxial growth tool is shared between GaN, InP, and GaAs device production, and capacity additions require 18–24 months per tool installation and qualification.","chokepoint":"Y","capital_intensity":"High","moat_type":"Specialty process IP + Geographic concentration","margin_profile":"High","chips":["STM","WOLF"]},
      {"label":"OSAT (outsourced assembly and test)","sector":"Advanced Packaging","slug":"advanced-packaging","tier":"OSAT — Assembly & Test","fn":"Dice wafers into individual die, flip-chip or wire-bond attach die to substrates, overmold in epoxy compound, and test finished packages at high volume — the outsourced semiconductor assembly and test tier that handles the majority of global chip packaging volume beneath the advanced packaging layer. OSAT is the high-scale final manufacturing step that turns tested wafers into packaged, marked, and tested devices ready for PCB assembly. The market is dominated by ASE Technology (Taiwan), Amkor Technology (US-listed), and JCET (China) — three companies handling >60% of outsourced assembly volume. Advanced flip-chip, SiP, and fan-out packaging for AI chips concentrates at Taiwan-based OSATs due to the substrate and equipment ecosystem.","chokepoint":"Partial","capital_intensity":"High","moat_type":"Scale + Customer lock-in","margin_profile":"Medium","chips":["ASX","AMKR"]}
    ]},
    {"num":"10","name":"Semiconductor Equipment","hue":192,"tag":"litho · etch · metrology · test","boxes":[
      {"label":"EUV (leading edge)","group":"Lithography","sector":"Semiconductor Equipment","slug":"semiconductor-equipment","tier":"EUV Lithography","fn":"Project photomask circuit patterns onto photoresist-coated wafers using extreme ultraviolet light at 13.5nm wavelength — the only technology capable of printing transistors at 7nm and below in high volume. ASML holds an absolute monopoly on EUV scanners: no other company has simultaneously solved the laser-plasma EUV light source, tin droplet target system, collector mirror optics, and projection lens. A single High-NA EUV scanner costs €380M, weighs 180 tons, requires 40 shipping containers to deliver, and must be assembled by ASML engineers on-site. Without EUV, chips cannot be manufactured at leading-edge nodes — making ASML the single point of failure for all advanced semiconductor production globally. Export controls block EUV shipments to China.","chokepoint":"Y","capital_intensity":"Very High","moat_type":"Absolute monopoly — no alternative supplier exists","margin_profile":"Very High","chips":["ASML"]},
      {"label":"DUV (mature nodes)","group":"Lithography","sector":"Semiconductor Equipment","slug":"semiconductor-equipment","tier":"DUV Lithography","fn":"Project photomask patterns onto wafers using deep ultraviolet light at 193nm wavelength (immersion, with water as the refractive medium) to manufacture chips at 7nm–90nm nodes — the production workhorse for the majority of global chip volume by unit count. DUV immersion scanners (ASML TWINSCAN NXT series, ASML/Canon/Nikon at older nodes) remain dominant for mature logic, analog, power, and memory manufactured below the leading edge. DUV serves analog front-ends, power management ICs, RF chips, and the mature-node chips that account for >70% of semiconductor unit volume. US and Netherlands export controls have restricted DUV shipments to China's leading-edge fabs, making DUV equipment the second major export control battleground after EUV.","chokepoint":"Partial","capital_intensity":"Very High","moat_type":"Oligopoly (ASML ~85% DUV share, Canon/Nikon remainder)","margin_profile":"High","chips":["ASML","CAJ"]},
      {"label":"NIL (nanoimprint, photonics)","group":"Lithography","gap":true,"chips":["CAJ"]},
      {"label":"Deposition (CVD, PVD, ALD)","sector":"Semiconductor Equipment","slug":"semiconductor-equipment","tier":"Deposition Equipment","fn":"Deposit thin-film layers atom-by-atom through chemical vapor deposition (CVD), physical vapor deposition (PVD), and atomic layer deposition (ALD) to build the transistor gate stacks, metal interconnects, dielectric isolation layers, and barrier liners that constitute a working integrated circuit across 500–1,500 process steps. ALD has become critical for sub-3nm nodes: it deposits materials one atomic monolayer at a time in a self-limiting surface reaction, enabling conformality in gate-all-around nanosheet transistors and high-aspect-ratio capacitor trenches. Applied Materials leads CVD and PVD; Lam Research leads ALD; Tokyo Electron (TEL) holds ~15% across both categories. Switching costs are absolute — each deposition recipe is qualified on specific equipment over months of process development.","chokepoint":"Partial","capital_intensity":"High","moat_type":"Process IP + Switching cost (recipe qualification)","margin_profile":"High","chips":["AMAT","LRCX"]},
      {"label":"Etch (plasma, wet)","sector":"Semiconductor Equipment","slug":"semiconductor-equipment","tier":"Etch Equipment","fn":"Remove material with sub-angstrom dimensional control through plasma etch and wet chemistries — etching features in silicon, dielectrics, and metals to define transistor source/drain structures, contact holes, and metal interconnect trenches with pattern fidelity that lithography alone cannot achieve. The etch equipment market is a functional duopoly: Lam Research and Applied Materials together control ~80% of plasma etch equipment revenue. Switching costs are absolute — each etch recipe is qualified on a specific equipment model over months of process development, and re-qualifying on a competitor's tool requires repeating the entire customer qualification process. Etch equipment is subject to the same export control framework as ASML for advanced-node shipments to China.","chokepoint":"Partial","capital_intensity":"High","moat_type":"Process IP + Switching cost (recipe qualification)","margin_profile":"High","chips":["LRCX","AMAT"]},
      {"label":"Metrology & Inspection","sector":"Semiconductor Equipment","slug":"semiconductor-equipment","tier":"Inspection & Metrology","fn":"Measure every critical dimension across each process layer and detect every printable defect before and after exposure — providing the real-time feedback loop that enables yield learning, statistical process control, and overlay correction. KLA Corporation holds ~55% of the process control equipment market: fab engineers develop thousands of inspection recipes tuned to KLA tool optics and algorithms, making switching to Onto Innovation or other tools a multi-year re-qualification effort. As chip density increases and defect budget shrinks, inspection tool requirements become more stringent — demanding new architectures rather than incremental improvements at each node transition.","chokepoint":"Partial","capital_intensity":"Medium","moat_type":"Switching cost + Certification (recipe library)","margin_profile":"High","chips":["KLAC","ONTO","FORM"]},
      {"label":"Burn-in & Reliability Testing","sector":"Semiconductor Equipment","slug":"semiconductor-equipment","tier":"Test & Burn-In","fn":"Electrically verify every die at wafer probe and every packaged device after assembly; stress-screen for latent defects through elevated temperature and voltage burn-in; and characterize performance bins that determine whether a chip ships as a high-end or cost-reduced variant. The ATE (automated test equipment) market is a duopoly: Teradyne (~50%) and Advantest (~35%) supply virtually all SoC and memory testers used in production. Burn-in — running chips at 125°C+ and elevated voltage for 24–168 hours — screens the 'infant mortality' failure population, ensuring shipped parts meet reliability specifications. Wafer-level burn-in for SiC (Aehr Test Systems) is a specialty niche with near-monopoly characteristics as EV-powertrain SiC volume scales.","chokepoint":"Partial","capital_intensity":"Low–Medium","moat_type":"Certification + Switching cost (test program investment)","margin_profile":"Low–Medium","chips":["AEHR","COHU","6857.T"]},
      {"label":"Compound Semi Growth (MOCVD for InP/GaAs)","gap":true,"chips":["AMAT","AIXA.DE"]}
    ]},
    {"num":"11","name":"Semiconductor Materials","hue":32,"tag":"wafers · substrates · chemicals","boxes":[
      {"label":"Silicon Wafers (300mm)","sector":"Semiconductor Materials","slug":"semiconductor-materials","tier":"Silicon Wafers (300mm)","fn":"Slice, grind, etch, and polish single-crystal silicon boules into atomically flat 300mm substrates on which all CMOS logic, memory, and analog devices are fabricated. The 300mm silicon wafer market is a mature duopoly: Shin-Etsu Handotai (SEH) and Sumco together supply ~60% of 300mm wafers consumed by TSMC, Samsung, Intel, and SK Hynix. The Czochralski (CZ) growth process pulls a 300mm boule at precisely controlled thermal gradients over 24–72 hours — any vibration creates crystalline defects that reduce die yield. After slicing, lapping, etching, and polishing, surface roughness must be below 0.1nm for sub-2nm EUV photolithography.","chokepoint":"Y","capital_intensity":"High","moat_type":"Scale + Process IP (duopoly)","margin_profile":"Medium","chips":["4043.T","4369.T"]},
      {"label":"SOI Substrates (for GPU)","sector":"Semiconductor Materials","slug":"semiconductor-materials","tier":"SOI Substrates","fn":"Bond a thin crystalline silicon device layer onto a buried oxide (BOX) layer on a standard silicon handle wafer — producing silicon-on-insulator (SOI) substrates that eliminate bulk silicon leakage currents, reduce parasitic capacitance, and enable fully-depleted transistor architectures (FD-SOI) with superior electrostatic control at sub-28nm nodes. SOI substrates are used in GlobalFoundries' 22FDX and 12FDX FD-SOI processes, which deliver CMOS performance approaching leading-edge FinFET with lower power consumption — advantageous for RF front-ends, IoT processors, and automotive applications. Soitec (SOI.PA) holds a near-monopoly on commercial SOI substrate supply, with its SmartCut bonding technology protected by foundational patents. RF-SOI substrates are also used in iPhone RF front-end chips — a structural consumer electronics demand anchor.","chokepoint":"Y","capital_intensity":"High","moat_type":"Near-monopoly (Soitec SmartCut IP)","margin_profile":"High","chips":["SOI.PA"]},
      {"label":"InP Substrates (for lasers)","sector":"Semiconductor Materials","slug":"semiconductor-materials","tier":"InP Substrates","fn":"Produce single-crystal indium phosphide (InP) wafers via the liquid-encapsulated Czochralski (LEC) or vertical gradient freeze (VGF) method for use as substrates on which laser diodes, VCSELs, electroabsorption modulators, and high-speed photodetectors are epitaxially grown. InP is the dominant substrate for 100G–800G laser chips used in AI datacenter transceivers: its direct bandgap at 0.74–1.35eV enables efficient photon emission at 1310nm and 1550nm telecom wavelengths, and its high electron mobility enables >100GHz transistors for microwave and mm-wave applications. Global InP wafer supply is highly concentrated — fewer than five companies supply semiconductor-grade InP at the volumes AI transceiver demand now requires, with AXT Inc. as the primary US-listed supplier.","chokepoint":"Y","capital_intensity":"High","moat_type":"Process IP + Geographic concentration (few suppliers)","margin_profile":"High","chips":["AXTI"]},
      {"label":"GaAs Substrates (RF, optoelectronics)","sector":"Semiconductor Materials","slug":"semiconductor-materials","tier":"GaAs Substrates","fn":"Produce single-crystal gallium arsenide (GaAs) wafers for RF power amplifiers, solar cells, VCSELs, and optoelectronic components. GaAs's direct bandgap and high electron mobility make it essential for 5G RF power amplifiers in base stations and smartphones, where its 5x higher electron mobility than silicon enables lower noise and higher frequency operation. GaAs VCSELs are the standard light source for 3D sensing (Face ID, LiDAR), datacenter optical interconnects, and industrial laser applications. AXT Inc. supplies both InP and GaAs substrates, making it a dual-purpose critical materials supplier for photonic interconnect and RF applications.","chokepoint":"Partial","capital_intensity":"High","moat_type":"Process IP + Oligopoly supply","margin_profile":"High","chips":["AXTI"]},
      {"label":"SiC Wafers (power)","sector":"Semiconductor Materials","slug":"semiconductor-materials","tier":"SiC Wafers","fn":"Grow silicon carbide (SiC) single crystals using physical vapor transport (PVT) at 2,000°C+ to produce boules that are sliced into 150mm and 200mm wafers for SiC MOSFET and Schottky diode fabrication. SiC wafer production is one of the most technically demanding and supply-constrained processes in the semiconductor materials supply chain: a single SiC boule takes 1–3 weeks to grow versus hours for silicon, wafers cost $300–$1,000 each, and SiC growth defects (micropipes, threading screw dislocations) directly determine device yield and reliability. Wolfspeed (Mohawk Valley, 200mm SiC) controls the world's largest SiC wafer production capacity outside China, with no credible pure-play US alternative. China has aggressively built competing SiC wafer capacity as a strategic chokepoint, creating geopolitical supply risk.","chokepoint":"Y","capital_intensity":"Very High","moat_type":"Process IP + Scale (Wolfspeed/Coherent dominant)","margin_profile":"High","chips":["WOLF","STM"]},
      {"label":"Specialty Gases (neon, krypton, xenon for excimer lasers)","sector":"Semiconductor Materials","slug":"semiconductor-materials","tier":"Specialty Process Gases","fn":"Supply ultra-high-purity specialty and bulk gases — neon and krypton for DUV excimer laser lithography, nitrogen trifluoride (NF₃) for chamber cleaning, silane (SiH₄) for CVD deposition, ammonia (NH₃) and hydrogen chloride (HCl) for epitaxial growth — that every semiconductor fab step consumes as process consumables. Specialty gases are an undersized but disproportionately critical supply chain link: neon and krypton are sourced primarily from cryogenic air separation units co-located with Ukrainian and Russian steel mills, creating geographic concentration that was acutely demonstrated during the 2022 Ukraine invasion when neon prices spiked 600%. Linde and Air Products are the largest US-listed industrial gas suppliers with electronics-grade specialty gas units. No fab operates without an uninterrupted specialty gas supply — consumption is continuous and inventory lead times are days, not months.","chokepoint":"Y","capital_intensity":"High","moat_type":"Scale + Geographic monopoly (specialty gas sourcing)","margin_profile":"High","chips":["LIN","APD"]},
      {"label":"Anti-Stick Coatings (PFAS-free for NIL)","gap":true,"chips":["ENTG"]},
      {"label":"Photoresist (lithography chemicals)","sector":"Semiconductor Materials","slug":"semiconductor-materials","tier":"Photoresist & Lithography Chemicals","fn":"Synthesize the chemically amplified photoresists (CARs) for DUV and EUV lithography, anti-reflective coatings (ARCs), developer solutions, and rinse chemicals that enable the photolithography exposure step to transfer circuit patterns from photomasks to wafer surfaces at sub-2nm resolution. EUV photoresist is arguably the most technically sophisticated material in semiconductor manufacturing: it must simultaneously absorb 13.5nm EUV photons, chemically amplify the latent image through acid-catalyzed deprotection reactions at 20–50nm critical dimensions, and develop to leave precisely vertical resist profiles with roughness below 1nm. The EUV photoresist market is controlled by JSR (Japan), Shin-Etsu Chemical (Japan), and Tokyo Ohka Kogyo (Japan/TOK) — three companies whose decade-long R&D lead represents an insurmountable barrier to new entrants. US advanced logic fabrication at TSMC's Arizona facility requires JSR/Shin-Etsu EUV photoresist sourced from Japan.","chokepoint":"Y","capital_intensity":"High","moat_type":"Process IP + Oligopoly (JSR/Shin-Etsu/TOK)","margin_profile":"High","chips":["ENTG","4369.T","5201.T"]}
    ]},
    {"num":"12","name":"Critical Minerals & Raw Elements","hue":350,"tag":"the bedrock everything depends on","boxes":[
      {"label":"Silicon (base material for all chips)","sector":"Critical Minerals","slug":"critical-minerals","tier":"Silicon & SiC Precursor Production","chips":["WOLF"]},
      {"label":"Copper (interconnect, power delivery)","sector":"Critical Minerals","slug":"critical-minerals","tier":"Bulk Mining & Ore Extraction","chips":["FCX","VALE","RIO"]},
      {"label":"Gallium (GaN power semis, GaAs RF, InP photonics)","sector":"Semiconductor Materials","slug":"semiconductor-materials","tier":"Gallium & Gallium Compounds","fn":"Produce refined gallium metal and gallium compounds — gallium arsenide (GaAs), gallium nitride (GaN), gallium phosphide (GaP) — that are the elemental foundation of compound semiconductor devices spanning RF power amplifiers, datacenter laser transceivers, solar cells, and power electronics. Gallium is a byproduct of aluminum (bauxite) refining, with China controlling ~80% of global primary gallium production — a concentration that became a strategic flashpoint in August 2023 when China announced export restrictions on gallium compounds, directly targeting the US semiconductor supply chain. Gallium demand is accelerating: GaN-on-SiC for 5G and AI datacenter power conversion, and GaAs for RF amplifiers and datacom VCSELs, are both growth markets. US gallium refining capacity is minimal — AXT Inc. (AXTI) is the primary US-listed company with InP and GaAs substrate production sourcing commercial-grade gallium outside China.","chokepoint":"Y","capital_intensity":"Medium","moat_type":"Geographic monopoly (China controls ~80% production) + Export control risk","margin_profile":"High (strategic material premium)","chips":["AXTI","WOLF"]},
      {"label":"Indium (InP lasers, transparent conductors)","sector":"Semiconductor Materials","slug":"semiconductor-materials","tier":"Indium & Indium Compounds","fn":"Produce refined indium metal and indium compounds — indium phosphide (InP), indium tin oxide (ITO), and indium gallium arsenide (InGaAs) — that are essential inputs for datacenter laser diodes, high-efficiency multijunction solar cells, infrared photodetectors, and transparent conductive electrodes in touchscreens and displays. Indium is a rare trace metal recovered as a byproduct of zinc smelting, with global production of only ~900 tonnes annually — one of the rarest commercially refined metals. China and South Korea control the majority of global indium refining. InP is the substrate material for the 1310nm and 1550nm laser diodes inside every AI datacenter optical transceiver, making indium supply a critical upstream dependency for the global AI networking buildout. Export restrictions on indium would directly impact the transceiver supply chain that NVIDIA's GPU clusters depend on.","chokepoint":"Y","capital_intensity":"Medium","moat_type":"Geographic monopoly (scarce metal + China/Korea refining control)","margin_profile":"High (strategic material premium)","chips":["AXTI"]},
      {"label":"Germanium (optical fiber, compound semis)","sector":"Interconnect","slug":"interconnect","tier":"Optical Fiber & Preform Manufacturing","chips":["GLW"]},
      {"label":"Hafnium (high-k dielectric in leading-edge logic)","gap":true,"chips":["INTC","ATI"]},
      {"label":"Tantalum (capacitors)","sector":"Electronic Components","slug":"electronic-components","tier":"Film & Electrolytic Capacitor Mfg","chips":["VSH"]},
      {"label":"Cobalt (energy storage)","sector":"Critical Minerals","slug":"critical-minerals","tier":"Battery Material Precursor Production","chips":["ELMT"]},
      {"label":"Lithium (energy storage)","sector":"Critical Minerals","slug":"critical-minerals","tier":"Lithium & Battery Metals","chips":["ALB"]},
      {"label":"Rare Earths (Neodymium, Dysprosium — motors, magnets)","sector":"Critical Minerals","slug":"critical-minerals","tier":"Rare Earth Separation & Critical Mineral Refining","chips":["MP","NB"]}
    ]}
  ],
  "connectors": [
    {"label":"calls models via API"},
    {"label":"runs on"},
    {"label":"deployed on"},
    {"label":"running on physical compute"},
    {"label":"each compute unit needs"},
    {"label":"compute and memory need to talk via","choke":true},
    {"label":"all compute, memory, interconnect requires","choke":true},
    {"label":"made by"},
    {"label":"foundries depend on"},
    {"label":"equipment processes"},
    {"label":"materials derived from","choke":true}
  ],
  "rails": [
    {"id":"power","side":"left","flow":"in","title":"Power Infrastructure","cap":"Power comes in — generation → grid → rack → board.","groups":[
      {"label":"Power Generation","boxes":[
        {"label":"Nuclear (baseload for hyperscale)","sector":"Power Infrastructure","slug":"power-infrastructure","tier":"Nuclear Baseload Generation","chips":["CEG","VST"]},
        {"label":"Natural Gas Turbines","sector":"Power Infrastructure","slug":"power-infrastructure","tier":"Natural Gas & Peaker Generation","chips":["GEV"]},
        {"label":"Small Modular Reactors (emerging)","sector":"Power Infrastructure","slug":"power-infrastructure","tier":"Advanced Nuclear — SMR & Microreactor","chips":["OKLO"]}
      ]},
      {"label":"Grid Infrastructure","boxes":[
        {"label":"Transformers","sector":"Power Infrastructure","slug":"power-infrastructure","tier":"Grid Transformers","chips":["GEV","ETN"]},
        {"label":"Substations","sector":"Power Infrastructure","slug":"power-infrastructure","tier":"Substation Infrastructure","chips":["ETN"]},
        {"label":"High-Voltage Distribution","sector":"Power Infrastructure","slug":"power-infrastructure","tier":"High-Voltage Distribution Networks","chips":["GEV"]}
      ]},
      {"label":"Data Center Power","boxes":[
        {"label":"UPS Systems","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Data Center UPS Systems","chips":["VRT","ETN"]},
        {"label":"800V DC Bus Architecture","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"800V DC Bus & Power Conversion","chips":["VRT","NVTS"],"choke":true},
        {"label":"Rack-Level Power Delivery","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Rack-Level Power Delivery","chips":["VRT"]}
      ]},
      {"label":"Power Semiconductors","boxes":[
        {"label":"GaN (high-frequency switching)","sector":"Compute Hardware","slug":"compute-hardware","tier":"GaN Power Semiconductors","chips":["NVTS","IFX"]},
        {"label":"SiC (high-voltage)","sector":"Compute Hardware","slug":"compute-hardware","tier":"SiC Power Devices","chips":["WOLF","STM"]},
        {"label":"Power Management ICs","sector":"Electronic Components","slug":"electronic-components","tier":"Power Management ICs & Gate Drivers","chips":["MPWR"]},
        {"label":"MLCC and Passive Components","sector":"Electronic Components","slug":"electronic-components","tier":"MLCC Manufacturing","chips":["VSH"]}
      ]}
    ]},
    {"id":"thermal","side":"right","flow":"out","title":"Thermal Management","cap":"Heat comes out — cools compute & memory across L4–L9.","groups":[
      {"label":"Cooling Stack","boxes":[
        {"label":"Air Cooling (legacy)","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Air Cooling Systems","chips":[]},
        {"label":"Direct-to-Chip Liquid Cooling","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Direct-to-Chip Liquid Cooling","chips":["VRT"]},
        {"label":"Immersion Cooling","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Immersion Cooling","chips":[]},
        {"label":"Two-Phase Cooling","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Two-Phase Cooling","chips":[]},
        {"label":"Thermal Interface Materials (TIM)","gap":true,"chips":[]},
        {"label":"Heat Exchangers and CDUs","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Coolant Distribution Units & Heat Exchangers","chips":["VRT","MOD","NVT","6367.T"]}
      ]}
    ]},
    {"id":"security","side":"right","flow":"wrap","title":"Security","cap":"Security wraps around the whole stack — cross-cutting at every layer.","groups":[
      {"label":"Stack Security","boxes":[
        {"label":"AI Model Security (alignment, jailbreak defense)","sector":"Security","slug":"security","tier":"AI-Native Security","chips":[]},
        {"label":"Cybersecurity for AI Infrastructure","sector":"Security","slug":"security","tier":"Cloud Security Posture (CSPM/CNAPP)","chips":["PANW","CRWD","FTNT","SAIL","RBRK"]},
        {"label":"Post-Quantum Cryptography","gap":true,"chips":[]},
        {"label":"Optical Network Encryption","sector":"Interconnect","slug":"interconnect","tier":"Coherent Line Systems & ROADM","chips":["CIEN","VIAV"]},
        {"label":"Hardware Root of Trust","sector":"Security","slug":"security","tier":"Hardware Security Root","chips":[]}
      ]}
    ]},
    {"id":"edge","side":"right","kind":"surface","title":"Edge & Physical AI","cap":"Deployment paradigm — where the stack meets the physical world.","groups":[
      {"label":"Edge & Physical AI","boxes":[
        {"label":"Autonomous Vehicles","sector":"Edge & Physical AI","slug":"edge-physical-ai","tier":"Autonomous Vehicles & ADAS","chips":["MBLY","OUST","LAZR"]},
        {"label":"Humanoid Robotics","sector":"Edge & Physical AI","slug":"edge-physical-ai","tier":"System Integration & OEM Assembly","chips":[]},
        {"label":"Drones and UAVs","sector":"Edge & Physical AI","slug":"edge-physical-ai","tier":"UAV & Drone Systems","chips":["AVAV","JOBY","ACHR"]},
        {"label":"Driver / Behavior Monitoring Systems","sector":"Edge & Physical AI","slug":"edge-physical-ai","tier":"Perception Layer","chips":["AMBA"]},
        {"label":"Edge Inference Chips","sector":"Edge & Physical AI","slug":"edge-physical-ai","tier":"Edge Compute Module","chips":["AMBA"]},
        {"label":"AR / VR Devices","gap":true,"chips":["KOPN","META"]}
      ]},
      {"label":"Parallel Compute Paradigms","boxes":[
        {"label":"Quantum Computing","gap":true,"chips":["IONQ","RGTI","QBTS"]},
        {"label":"Superconducting qubits","gap":true,"chips":["RGTI"]},
        {"label":"Trapped ion / photonic qubits","gap":true,"chips":["IONQ"]},
        {"label":"Cryogenic control electronics","gap":true,"chips":[]},
        {"label":"Dilution refrigerators","gap":true,"chips":[]},
        {"label":"Neuromorphic Computing (emerging)","gap":true,"chips":["BRCHF"]},
        {"label":"Optical / Photonic Computing (emerging)","gap":true,"chips":["LWLG","POET"]}
      ]}
    ]}
  ]
}
```

---

## Coverage gaps (`"gap": true` sub-boxes)

These blueprint categories still have no faithful `(sector, tier)` in the knowledge base. They render
muted ("unmapped") on the dashboard and are the queue for `/map-sector` / `/scout-tickers`. The
**2026-06-15 pass closed 17 gaps** (L03 GPU Programming Layer; L07 On-package optical engines / External
Light Sources / Optical Engines / Fiber Array Units / Optical Connectors / Fiber Cables; L08 Glass Core
Substrates; L09 Silicon Photonics Foundry; L11 Specialty Gases; L12 Gallium / Indium / Germanium /
Tantalum; Power-rail Power Management ICs / MLCC; Security Optical Network Encryption; Edge Autonomous
Vehicles / Drones and UAVs) by wiring them to existing or newly-added tiers and onboarding IPGP, MPWR,
VSH, LIN, MBLY, AVAV. Remaining open gaps:

| Layer | Sub-box | Suggested home |
|-------|---------|----------------|
| L01 | AI Assistants & Chatbots; Agentic AI Platforms; Enterprise AI SaaS; AI-Native Vertical Applications | New **Application / AI-native apps** sector (Fintech & Commerce AI is the only L01 coverage today) |
| L04 | Edge / Inference Colocation | Compute Infrastructure — new tier (chips EQIX/VRT pending tier) |
| L08 | Thermal Interface Materials (TIM) | Electronic Components / Compute Infra (thermal) |
| L10 | NIL (nanoimprint, photonics); Compound Semi Growth (MOCVD) | Semiconductors — equipment sub-tiers (chips CAJ / AMAT, AIXA.DE) |
| L11 | Anti-Stick Coatings (PFAS-free) | Semiconductors / Electronic Components — materials (chip ENTG) |
| L12 | Hafnium | Materials & Mining / specialty metals — no listed pure-play (chips INTC/ATI) |
| Thermal rail | Thermal Interface Materials (TIM) | Compute Infra / Electronic Components — materials |
| Security rail | Post-Quantum Cryptography | Cybersecurity — new tier (no investable pure-play yet) |
| Edge surface | AR / VR Devices | Robotics & Edge AI — deployment-form tier (chips KOPN/META) |
| Edge surface | Parallel Compute Paradigms (quantum, neuromorphic, photonic) | New **Parallel Compute** sector |

The rails are now **fully scaffolded**: every Power / Thermal / Security / Edge sub-component is an individual box wired to its KB tier (or flagged `gap`), matching the main-layer sub-box treatment.

---

## Maintenance

- When `/map-sector` adds or rebuilds a `_Supply Chain Map.md`, wire the relevant `gap` sub-box to the new `(sector, tier)` (remove `"gap": true`, add `slug`/`tier`/`chips`) and update both this JSON block and the dashboard.
- Sub-box **labels are canonical** (verbatim from the graphic) — change them only if the blueprint changes. `group` tags cluster boxes visually; `gap` marks unmapped boxes; neither adds a drill-down level.
- Keep this JSON block and the `STACK` object in `Investing/Output/Dashboard/index.html` in sync — `/daily-dashboard --refresh-data` regenerates the dashboard from this file.
- Cross-layer dependency edges (the labeled arrows) are distilled in `connectors[]`; the full edge list lives in `Ecosystem Interrelationships.md`.
</content>
</invoke>

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
  "generated": "2026-06-16",
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
      {"label":"ML Frameworks (training)","sector":"Software Infrastructure","slug":"software-infrastructure","tier":"Distributed Training Orchestration","chips":["CRWV","AMD"]},
      {"label":"GPU Programming Layer (low-level kernels)","sector":"Software Infrastructure","slug":"software-infrastructure","tier":"Distributed Training Orchestration","chips":["NVDA","AMD"]},
      {"label":"Distributed Training Systems","sector":"Software Infrastructure","slug":"software-infrastructure","tier":"Distributed Training Orchestration","chips":[]},
      {"label":"Container Orchestration (Kubernetes)","sector":"Software Infrastructure","slug":"software-infrastructure","tier":"MLOps & Model Lifecycle Management","chips":["DDOG","SNOW","PLTR","MDB"]},
      {"label":"Inference Optimization Stack","sector":"Software Infrastructure","slug":"software-infrastructure","tier":"Model Optimization & Compilation","chips":[]}
    ]},
    {"num":"04","name":"Cloud Infrastructure","hue":288,"tag":"hyperscalers · neoclouds · colocation","boxes":[
      {"label":"Hyperscaler Clouds","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Hyperscaler & Colocation Operation","chips":["MSFT","AMZN","GOOGL","ORCL"]},
      {"label":"NeoClouds (GPU-specialized)","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Hyperscaler & Colocation Operation","chips":["CRWV","IREN"]},
      {"label":"Edge / Inference Colocation","gap":true,"chips":["EQIX","VRT"]},
      {"label":"Data Center Colocation","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Data Center Facility & MEP","chips":[]}
    ]},
    {"num":"05","name":"Compute Hardware","hue":55,"tag":"GPUs · ASICs · CPUs · NICs","boxes":[
      {"label":"Training GPUs","sector":"Compute Hardware","slug":"compute-hardware","tier":"Chip Design (Fabless & IDM)","chips":["NVDA","AMD"]},
      {"label":"Inference GPUs","sector":"Compute Hardware","slug":"compute-hardware","tier":"Chip Design (Fabless & IDM)","chips":["NVDA","AMD"]},
      {"label":"Custom AI ASICs (hyperscaler silicon)","sector":"Compute Hardware","slug":"compute-hardware","tier":"Chip Design (Fabless & IDM)","chips":["AVGO","MRVL"]},
      {"label":"Dedicated Inference Accelerators","sector":"Compute Hardware","slug":"compute-hardware","tier":"Chip Design (Fabless & IDM)","chips":[]},
      {"label":"Server CPUs (orchestration, agentic workloads)","sector":"Compute Hardware","slug":"compute-hardware","tier":"Chip Design (Fabless & IDM)","chips":["ARM","INTC"]},
      {"label":"Networking ASICs (switch silicon)","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"High-Speed Networking","chips":["ANET","AVGO","MRVL"]}
    ]},
    {"num":"06","name":"Memory","hue":92,"tag":"HBM · HBF · DRAM · NAND · LPDDR","boxes":[
      {"label":"HBM (current AI server standard)","sector":"Memory","slug":"memory","tier":"HBM (High-Bandwidth Memory)","chips":["MU","000660.KS","005930.KS"]},
      {"label":"HBF (high-bandwidth flash)","sector":"Memory","slug":"memory","tier":"HBF (High-Bandwidth Flash)","chips":["SNDK","000660.KS"]},
      {"label":"DRAM (system memory)","sector":"Memory","slug":"memory","tier":"DRAM (System & Server Memory)","chips":["MU","005930.KS","000660.KS"]},
      {"label":"NAND Flash (storage)","sector":"Memory","slug":"memory","tier":"NAND Flash (Storage)","chips":["SNDK","285A.T","005930.KS","MU"]},
      {"label":"LPDDR (mobile / edge inference)","sector":"Memory","slug":"memory","tier":"LPDDR (Low-Power & Edge Memory)","chips":["MU","005930.KS"]}
    ]},
    {"num":"07","name":"Interconnect","hue":42,"tag":"scale-up · scale-out · scale-across","boxes":[
      {"label":"Co-Packaged Optics (CPO)","group":"Scale-Up · within the rack, chip to chip","sector":"Interconnect","slug":"interconnect","tier":"Transceiver & Module Integration","chips":["COHR","LITE"]},
      {"label":"NVLink-style fabrics","group":"Scale-Up · within the rack, chip to chip","sector":"Interconnect","slug":"interconnect","tier":"Interconnect & SerDes Silicon","chips":["NVDA","ALAB"]},
      {"label":"On-package optical engines","group":"Scale-Up · within the rack, chip to chip","sector":"Interconnect","slug":"interconnect","tier":"Silicon Photonics Platform","chips":["POET","LWLG"]},
      {"label":"SerDes · Retimers","group":"Scale-Up · within the rack, chip to chip","sector":"Interconnect","slug":"interconnect","tier":"Interconnect & SerDes Silicon","chips":["CRDO","ALAB"]},
      {"label":"Pluggable Optical Transceivers","group":"Scale-Out · between racks, within data center","sector":"Interconnect","slug":"interconnect","tier":"Transceiver & Module Integration","chips":["COHR","LITE","FN","AAOI"]},
      {"label":"Linear Pluggable Optics (LPO)","group":"Scale-Out · between racks, within data center","sector":"Interconnect","slug":"interconnect","tier":"Transceiver & Module Integration","chips":["AAOI"]},
      {"label":"High-speed Ethernet / InfiniBand","group":"Scale-Out · between racks, within data center","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"High-Speed Networking","chips":["ANET","AVGO"]},
      {"label":"Coherent Optical Transport","group":"Scale-Across · between data centers","sector":"Interconnect","slug":"interconnect","tier":"Coherent Line Systems & ROADM","chips":["CIEN"]},
      {"label":"Long-haul DWDM","group":"Scale-Across · between data centers","sector":"Interconnect","slug":"interconnect","tier":"Coherent Line Systems & ROADM","chips":["CIEN","GLW"]},
      {"label":"External Light Sources (CW lasers)","group":"Components · used across all three scales","sector":"Interconnect","slug":"interconnect","tier":"Photonic Device Fabrication","chips":["IPGP","LITE","LASR"]},
      {"label":"Optical Engines","group":"Components · used across all three scales","sector":"Interconnect","slug":"interconnect","tier":"Silicon Photonics Platform","chips":["POET","IPGP"]},
      {"label":"Fiber Array Units (FAU)","group":"Components · used across all three scales","sector":"Interconnect","slug":"interconnect","tier":"Optical Fiber & Preform Manufacturing","chips":["FOCI"]},
      {"label":"Optical Connectors","group":"Components · used across all three scales","sector":"Interconnect","slug":"interconnect","tier":"Passive Optical Components","chips":["GLW","VIAV"]},
      {"label":"Fiber Cables","group":"Components · used across all three scales","sector":"Interconnect","slug":"interconnect","tier":"Optical Fiber & Preform Manufacturing","chips":["GLW"]}
    ]},
    {"num":"08","name":"Advanced Packaging","hue":150,"tag":"CoWoS · stacking · substrates","boxes":[
      {"label":"Wafer-Level Packaging (CoWoS, SoIC)","sector":"Advanced Packaging","slug":"advanced-packaging","tier":"Advanced Packaging (CoWoS / SoIC)","chips":["TSM","AMKR"]},
      {"label":"HBM Stacking & Integration","sector":"Advanced Packaging","slug":"advanced-packaging","tier":"Advanced Packaging (CoWoS / SoIC)","chips":["MU","TSM"]},
      {"label":"FC-BGA Substrates","sector":"Electronic Components","slug":"electronic-components","tier":"IC Substrate Manufacturing","chips":[],"choke":true},
      {"label":"Glass Core Substrates (emerging)","sector":"Electronic Components","slug":"electronic-components","tier":"Substrate & Laminate Materials","chips":["GLW","INTC","LPK"]},
      {"label":"Thermal Interface Materials (TIM)","gap":true,"chips":[]}
    ]},
    {"num":"09","name":"Semiconductor Foundry","hue":162,"tag":"leading-edge · specialty · OSAT","boxes":[
      {"label":"Leading-Edge Logic Foundry (3nm, 2nm)","sector":"Semiconductor Foundry","slug":"semiconductor-foundry","tier":"Wafer Fabrication (Foundry / IDM)","chips":["TSM","INTC"]},
      {"label":"Specialty / Mature Logic Foundry (analog, mixed-signal)","sector":"Semiconductor Foundry","slug":"semiconductor-foundry","tier":"Wafer Fabrication (Foundry / IDM)","chips":["GFS"]},
      {"label":"Silicon Photonics Foundry","sector":"Semiconductor Foundry","slug":"semiconductor-foundry","tier":"Silicon Photonics Platform","chips":["GFS","POET","INTC"]},
      {"label":"Compound Semiconductor Foundry (GaN, SiC, InP)","sector":"Semiconductor Foundry","slug":"semiconductor-foundry","tier":"Compound Semiconductor & SiC Substrate","chips":["STM","WOLF"]},
      {"label":"OSAT (outsourced assembly and test)","sector":"Advanced Packaging","slug":"advanced-packaging","tier":"OSAT — Assembly & Test","chips":["ASX","AMKR"]}
    ]},
    {"num":"10","name":"Semiconductor Equipment","hue":192,"tag":"litho · etch · metrology · test","boxes":[
      {"label":"EUV (leading edge)","group":"Lithography","sector":"Semiconductor Equipment","slug":"semiconductor-equipment","tier":"Lithography Equipment","chips":["ASML"]},
      {"label":"DUV (mature nodes)","group":"Lithography","sector":"Semiconductor Equipment","slug":"semiconductor-equipment","tier":"Lithography Equipment","chips":["ASML","CAJ"]},
      {"label":"NIL (nanoimprint, photonics)","group":"Lithography","gap":true,"chips":["CAJ"]},
      {"label":"Deposition (CVD, PVD, ALD)","sector":"Semiconductor Equipment","slug":"semiconductor-equipment","tier":"Deposition & Etch Equipment","chips":["AMAT","LRCX"]},
      {"label":"Etch (plasma, wet)","sector":"Semiconductor Equipment","slug":"semiconductor-equipment","tier":"Deposition & Etch Equipment","chips":["LRCX","AMAT"]},
      {"label":"Metrology & Inspection","sector":"Semiconductor Equipment","slug":"semiconductor-equipment","tier":"Inspection & Metrology","chips":["KLAC","ONTO","FORM"]},
      {"label":"Burn-in & Reliability Testing","sector":"Semiconductor Equipment","slug":"semiconductor-equipment","tier":"Test & Burn-In","chips":["AEHR","COHU","6857.T"]},
      {"label":"Compound Semi Growth (MOCVD for InP/GaAs)","gap":true,"chips":["AMAT","AIXA.DE"]}
    ]},
    {"num":"11","name":"Semiconductor Materials","hue":32,"tag":"wafers · substrates · chemicals","boxes":[
      {"label":"Silicon Wafers (300mm)","sector":"Semiconductor Materials","slug":"semiconductor-materials","tier":"Silicon Wafer Production","chips":["4043.T","4369.T"]},
      {"label":"SOI Substrates (for GPU)","sector":"Semiconductor Materials","slug":"semiconductor-materials","tier":"Silicon Wafer Production","chips":["SOI.PA"]},
      {"label":"InP Substrates (for lasers)","sector":"Semiconductor Materials","slug":"semiconductor-materials","tier":"Compound Semiconductor & SiC Substrate","chips":["AXTI"]},
      {"label":"GaAs Substrates (RF, optoelectronics)","sector":"Semiconductor Materials","slug":"semiconductor-materials","tier":"Compound Semiconductor & SiC Substrate","chips":["AXTI"]},
      {"label":"SiC Wafers (power)","sector":"Semiconductor Materials","slug":"semiconductor-materials","tier":"Compound Semiconductor & SiC Substrate","chips":["WOLF","STM"]},
      {"label":"Specialty Gases (neon, krypton, xenon for excimer lasers)","sector":"Semiconductor Materials","slug":"semiconductor-materials","tier":"Raw Materials & Specialty Chemicals","chips":["LIN","APD"]},
      {"label":"Anti-Stick Coatings (PFAS-free for NIL)","gap":true,"chips":["ENTG"]},
      {"label":"Photoresist (lithography chemicals)","sector":"Semiconductor Materials","slug":"semiconductor-materials","tier":"Raw Materials & Specialty Chemicals","chips":["ENTG","4369.T","5201.T"]}
    ]},
    {"num":"12","name":"Critical Minerals & Raw Elements","hue":350,"tag":"the bedrock everything depends on","boxes":[
      {"label":"Silicon (base material for all chips)","sector":"Critical Minerals","slug":"critical-minerals","tier":"Silicon & SiC Precursor Production","chips":["WOLF"]},
      {"label":"Copper (interconnect, power delivery)","sector":"Critical Minerals","slug":"critical-minerals","tier":"Bulk Mining & Ore Extraction","chips":["FCX","VALE","RIO"]},
      {"label":"Gallium (GaN power semis, GaAs RF, InP photonics)","sector":"Semiconductor Materials","slug":"semiconductor-materials","tier":"III-V Substrate & Epitaxial Wafer Growth","chips":["AXTI","WOLF"]},
      {"label":"Indium (InP lasers, transparent conductors)","sector":"Semiconductor Materials","slug":"semiconductor-materials","tier":"III-V Substrate & Epitaxial Wafer Growth","chips":["AXTI"]},
      {"label":"Germanium (optical fiber, compound semis)","sector":"Interconnect","slug":"interconnect","tier":"Optical Fiber & Preform Manufacturing","chips":["GLW"]},
      {"label":"Hafnium (high-k dielectric in leading-edge logic)","gap":true,"chips":["INTC","ATI"]},
      {"label":"Tantalum (capacitors)","sector":"Electronic Components","slug":"electronic-components","tier":"Film & Electrolytic Capacitor Mfg","chips":["VSH"]},
      {"label":"Cobalt (energy storage)","sector":"Critical Minerals","slug":"critical-minerals","tier":"Battery Material Precursor Production","chips":["ELMT"]},
      {"label":"Lithium (energy storage)","sector":"Critical Minerals","slug":"critical-minerals","tier":"Battery Material Precursor Production","chips":["ALB"]},
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
        {"label":"Nuclear (baseload for hyperscale)","sector":"Power Infrastructure","slug":"power-infrastructure","tier":"Primary Power Generation","chips":["CEG","VST"]},
        {"label":"Natural Gas Turbines","sector":"Power Infrastructure","slug":"power-infrastructure","tier":"Primary Power Generation","chips":["GEV"]},
        {"label":"Small Modular Reactors (emerging)","sector":"Power Infrastructure","slug":"power-infrastructure","tier":"Advanced Nuclear — SMR & Microreactor","chips":["OKLO"]}
      ]},
      {"label":"Grid Infrastructure","boxes":[
        {"label":"Transformers","sector":"Power Infrastructure","slug":"power-infrastructure","tier":"High-Voltage Transmission & Grid Infrastructure","chips":["GEV","ETN"]},
        {"label":"Substations","sector":"Power Infrastructure","slug":"power-infrastructure","tier":"High-Voltage Transmission & Grid Infrastructure","chips":["ETN"]},
        {"label":"High-Voltage Distribution","sector":"Power Infrastructure","slug":"power-infrastructure","tier":"High-Voltage Transmission & Grid Infrastructure","chips":["GEV"]}
      ]},
      {"label":"Data Center Power","boxes":[
        {"label":"UPS Systems","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Data Center Power Infrastructure","chips":["VRT","ETN"]},
        {"label":"800V DC Bus Architecture","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Data Center Power Infrastructure","chips":["VRT","NVTS"],"choke":true},
        {"label":"Rack-Level Power Delivery","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Data Center Power Infrastructure","chips":["VRT"]}
      ]},
      {"label":"Power Semiconductors","boxes":[
        {"label":"GaN (high-frequency switching)","sector":"Compute Hardware","slug":"compute-hardware","tier":"Compound Semiconductor & SiC Substrate","chips":["NVTS","IFX"]},
        {"label":"SiC (high-voltage)","sector":"Compute Hardware","slug":"compute-hardware","tier":"Compound Semiconductor & SiC Substrate","chips":["WOLF","STM"]},
        {"label":"Power Management ICs","sector":"Electronic Components","slug":"electronic-components","tier":"Power Management ICs & Gate Drivers","chips":["MPWR"]},
        {"label":"MLCC and Passive Components","sector":"Electronic Components","slug":"electronic-components","tier":"MLCC Manufacturing","chips":["VSH"]}
      ]}
    ]},
    {"id":"thermal","side":"right","flow":"out","title":"Thermal Management","cap":"Heat comes out — cools compute & memory across L4–L9.","groups":[
      {"label":"Cooling Stack","boxes":[
        {"label":"Air Cooling (legacy)","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Thermal Management & Cooling","chips":[]},
        {"label":"Direct-to-Chip Liquid Cooling","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Thermal Management & Cooling","chips":["VRT"]},
        {"label":"Immersion Cooling","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Thermal Management & Cooling","chips":[]},
        {"label":"Two-Phase Cooling","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Thermal Management & Cooling","chips":[]},
        {"label":"Thermal Interface Materials (TIM)","gap":true,"chips":[]},
        {"label":"Heat Exchangers and CDUs","sector":"Cloud Infrastructure","slug":"cloud-infrastructure","tier":"Thermal Management & Cooling","chips":["VRT","MOD","NVT","6367.T"]}
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

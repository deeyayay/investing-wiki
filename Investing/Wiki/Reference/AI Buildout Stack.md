# AI Buildout Stack — Canonical Layer Map
*Last updated: 2026-06-10 — adopted the 12-layer vertical model as the canonical taxonomy*

This file is the **authoritative taxonomy** for the wiki. The AI buildout is modeled as a single vertical dependency stack — **12 layers** from Application (top) down to Critical Minerals (bedrock), plus **4 cross-cutting rails** (Power Infrastructure, Thermal Management, Security, Edge & Physical AI).

Each layer is composed of **sub-boxes** (categories). Every sub-box maps to an existing `(sector, tier)` in the per-sector `_Supply Chain Map.md` files, so the rich tier/company data and chokepoint flags are reused — the layers are the canonical *navigation and organizing structure*; sector folders remain the physical home of each ticker (see the Monitor Registry).

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
| L06 | **Memory** | HBM, DRAM, NAND | Semiconductors |
| L07 | **Interconnect** | Networking silicon, optics, SerDes, fiber | Compute Infrastructure, Photonics & Optical, Semiconductors |
| L08 | **Advanced Packaging** | CoWoS, stacking, IC substrates | Semiconductors, Electronic Components |
| L09 | **Semiconductor Foundry** | Leading-edge & specialty wafer fab | Semiconductors |
| L10 | **Semiconductor Equipment** | Litho, deposition/etch, metrology, test | Semiconductors |
| L11 | **Semiconductor Materials** | Wafers, photoresist, chemicals, substrates | Semiconductors, Electronic Components |
| L12 | **Critical Minerals & Rare Earths** | The bedrock — mined & refined inputs | Materials & Mining |

### Cross-cutting rails

| Rail | Side | Function | Feeding sector(s) |
|------|------|----------|-------------------|
| **Power Infrastructure** | left | Powers the entire stack: generation → grid → rack → board | Energy & Power, Semiconductors (power devices) |
| **Thermal Management** | right | Cools compute & memory (cross-cuts L4–L9) | Compute Infrastructure (cooling) |
| **Security** | right | Secures every layer | Cybersecurity |
| **Edge & Physical AI** | right | Deploys intelligence into the physical world | Robotics & Edge AI |

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
  "generated": "2026-06-10",
  "layers": [
    {"num":"01","name":"Application","hue":235,"tag":"AI-native products & vertical apps","boxes":[
      {"label":"Fintech & Commerce AI","sector":"Fintech & Commerce AI","slug":"fintech-commerce-ai","tier":"Embedded Finance & Commerce APIs","chips":["MELI","SOFI","NU"]},
      {"label":"Consumer Finance Platforms","sector":"Fintech & Commerce AI","slug":"fintech-commerce-ai","tier":"Personal Finance & Wealth Management Platforms","chips":["HOOD","SOFI","AFRM"]},
      {"label":"Credit & Risk Decisioning AI","sector":"Fintech & Commerce AI","slug":"fintech-commerce-ai","tier":"Credit Decisioning & Underwriting AI","chips":["SOFI"]},
      {"label":"Payments & Settlement","sector":"Fintech & Commerce AI","slug":"fintech-commerce-ai","tier":"Payment Network Rails & Settlement","chips":["PYPL","SQ"]}
    ]},
    {"num":"02","name":"AI Model","hue":255,"tag":"foundation models · alignment · data","boxes":[
      {"label":"Foundation Model Development","sector":"AI Model Infrastructure","slug":"ai-model-infrastructure","tier":"Foundation Model Development","chips":["META"]},
      {"label":"Alignment & Safety Tuning","sector":"AI Model Infrastructure","slug":"ai-model-infrastructure","tier":"Alignment & Safety Tuning","chips":[]},
      {"label":"Training Data & Curation","sector":"AI Model Infrastructure","slug":"ai-model-infrastructure","tier":"Training Data & Curation","chips":[]}
    ]},
    {"num":"03","name":"Software Infrastructure","hue":268,"tag":"orchestration · serving · MLOps","boxes":[
      {"label":"Distributed Training Orchestration","sector":"AI Model Infrastructure","slug":"ai-model-infrastructure","tier":"Distributed Training Orchestration","chips":["CRWV","AMD"]},
      {"label":"Inference Serving & Scaling","sector":"AI Model Infrastructure","slug":"ai-model-infrastructure","tier":"Inference Serving & Scaling","chips":[]},
      {"label":"MLOps & Data Platforms","sector":"AI Model Infrastructure","slug":"ai-model-infrastructure","tier":"MLOps & Model Lifecycle Management","chips":["DDOG","SNOW","PLTR","MDB"]},
      {"label":"Model API & Dev Platform","sector":"AI Model Infrastructure","slug":"ai-model-infrastructure","tier":"Model API & Developer Platform","chips":["CFLT"]}
    ]},
    {"num":"04","name":"Cloud Infrastructure","hue":288,"tag":"hyperscalers · neoclouds · colocation","boxes":[
      {"label":"Hyperscale & GPU Clouds","sector":"Compute Infrastructure","slug":"compute-infrastructure","tier":"Hyperscaler & Colocation Operation","chips":["MSFT","AMZN","GOOGL","ORCL","IREN"]},
      {"label":"Server & Node ODM","sector":"Compute Infrastructure","slug":"compute-infrastructure","tier":"Compute Node Design & ODM Assembly","chips":["SMCI"]},
      {"label":"Storage Systems","sector":"Compute Infrastructure","slug":"compute-infrastructure","tier":"Storage Systems","chips":["P","NTAP","WDC","STX"]},
      {"label":"Data Center Facility & MEP","sector":"Compute Infrastructure","slug":"compute-infrastructure","tier":"Data Center Facility & MEP","chips":[]}
    ]},
    {"num":"05","name":"Compute Hardware","hue":55,"tag":"GPUs · custom ASICs · CPUs","boxes":[
      {"label":"AI Accelerators (GPU / ASIC)","sector":"Semiconductors","slug":"semiconductors","tier":"Chip Design (Fabless & IDM)","chips":["NVDA","AMD","AVGO","MRVL"]},
      {"label":"CPUs & Design IP","sector":"Semiconductors","slug":"semiconductors","tier":"EDA & Design IP","chips":["ARM","SNPS","CDNS"]}
    ]},
    {"num":"06","name":"Memory","hue":92,"tag":"compute is useless without memory","boxes":[
      {"label":"HBM · DRAM · NAND Flash","sector":"Semiconductors","slug":"semiconductors","tier":"Memory (HBM · DRAM · NAND)","chips":["MU"]}
    ]},
    {"num":"07","name":"Interconnect","hue":42,"tag":"compute & memory need to talk","boxes":[
      {"label":"Networking Silicon & Switches","sector":"Compute Infrastructure","slug":"compute-infrastructure","tier":"High-Speed Networking","chips":["ANET","AVGO","MRVL"]},
      {"label":"Optical Transceivers","sector":"Photonics & Optical","slug":"photonics-optical","tier":"Transceiver & Module Integration","chips":["COHR","LITE","FN","AAOI"]},
      {"label":"SerDes · Retimers · Cables","sector":"Semiconductors","slug":"semiconductors","tier":"Chip Design (Fabless & IDM)","chips":["CRDO","ALAB"]},
      {"label":"Fiber & Coherent Line Systems","sector":"Photonics & Optical","slug":"photonics-optical","tier":"Coherent Line Systems & ROADM","chips":["CIEN","GLW"]}
    ]},
    {"num":"08","name":"Advanced Packaging","hue":150,"tag":"CoWoS · stacking · substrates","boxes":[
      {"label":"CoWoS / Advanced Packaging","sector":"Semiconductors","slug":"semiconductors","tier":"Packaging (OSAT & Advanced)","chips":["TSM","AMKR","ASX"],"choke":true},
      {"label":"IC Substrates (ABF)","sector":"Electronic Components","slug":"electronic-components","tier":"IC Substrate Manufacturing","chips":[],"choke":true}
    ]},
    {"num":"09","name":"Semiconductor Foundry","hue":162,"tag":"where the dies are made","boxes":[
      {"label":"Leading-Edge & Specialty Logic","sector":"Semiconductors","slug":"semiconductors","tier":"Wafer Fabrication (Foundry / IDM)","chips":["TSM","INTC","GFS"]}
    ]},
    {"num":"10","name":"Semiconductor Equipment","hue":192,"tag":"the tools that build the chips","boxes":[
      {"label":"Lithography","sector":"Semiconductors","slug":"semiconductors","tier":"Lithography Equipment","chips":["ASML"]},
      {"label":"Deposition & Etch","sector":"Semiconductors","slug":"semiconductors","tier":"Deposition & Etch Equipment","chips":["AMAT","LRCX"]},
      {"label":"Metrology & Inspection","sector":"Semiconductors","slug":"semiconductors","tier":"Inspection & Metrology","chips":["KLAC","ONTO","FORM"]},
      {"label":"Test & Burn-In","sector":"Semiconductors","slug":"semiconductors","tier":"Test & Burn-In","chips":["6857.T","AEHR","COHU"]}
    ]},
    {"num":"11","name":"Semiconductor Materials","hue":32,"tag":"wafers · chemicals · substrates","boxes":[
      {"label":"Silicon Wafers","sector":"Semiconductors","slug":"semiconductors","tier":"Silicon Wafer Production","chips":["4043.T","4369.T"]},
      {"label":"Photoresist & Process Chemicals","sector":"Semiconductors","slug":"semiconductors","tier":"Raw Materials & Specialty Chemicals","chips":["4369.T","5201.T","ENTG"]},
      {"label":"Compound Substrates (SiC / III-V)","sector":"Semiconductors","slug":"semiconductors","tier":"Compound Semiconductor & SiC Substrate","chips":["STM","VNP","WOLF"]},
      {"label":"PCB & Passive Materials","sector":"Electronic Components","slug":"electronic-components","tier":"Dielectric & Conductor Materials","chips":[]}
    ]},
    {"num":"12","name":"Critical Minerals & Rare Earths","hue":350,"tag":"the bedrock everything depends on","boxes":[
      {"label":"Rare Earth Separation","sector":"Materials & Mining","slug":"metals-mining","tier":"Rare Earth Separation & Critical Mineral Refining","chips":["MP"]},
      {"label":"Silicon & SiC Precursor","sector":"Materials & Mining","slug":"metals-mining","tier":"Silicon & SiC Precursor Production","chips":["WOLF"]},
      {"label":"Copper & Base Metals","sector":"Materials & Mining","slug":"metals-mining","tier":"Bulk Mining & Ore Extraction","chips":["FCX","VALE","RIO"]},
      {"label":"Battery & Refractory Metals","sector":"Materials & Mining","slug":"metals-mining","tier":"Battery Material Precursor Production","chips":["ALB","ELMT"]}
    ]}
  ],
  "connectors": [
    {"label":"calls inference via API"},
    {"label":"runs on"},
    {"label":"runs on"},
    {"label":"runs on physical compute"},
    {"label":"feeds / paired with memory"},
    {"label":"compute & memory talk via","choke":true},
    {"label":"dies assembled & co-packaged","choke":true},
    {"label":"packaged from wafers","choke":true},
    {"label":"fabbed using","choke":true},
    {"label":"processed with"},
    {"label":"refined from","choke":true}
  ],
  "rails": [
    {"id":"power","side":"left","title":"Power Infrastructure","cap":"Powers the entire stack — generation → grid → rack → board.","groups":[
      {"label":"Power Generation","chips":["GEV","VST","CEG","OKLO","NEE"]},
      {"label":"Grid Infrastructure","chips":["ENR.DE","GEV"]},
      {"label":"Data Center Power","chips":["VRT","ETN","2308.TW","BE"]},
      {"label":"Power Semiconductors","chips":["STM","IFX","NVTS","WOLF"]}
    ]},
    {"id":"thermal","side":"right","title":"Thermal Management","cap":"Cools compute & memory (cross-cuts L4–L9).","groups":[
      {"label":"Liquid · Immersion · Air","chips":["VRT","MOD","NVT","6367.T"]}
    ]},
    {"id":"security","side":"right","title":"Security","cap":"Secures every layer of the stack.","groups":[
      {"label":"Identity · EDR · SecOps","chips":["SAIL","CRWD","PANW","FTNT","RBRK"]}
    ]},
    {"id":"edge","side":"right","title":"Edge & Physical AI","cap":"Deploys intelligence into the physical world.","groups":[
      {"label":"Robotics · AV · Sensors","chips":["AMBA","OUST","RKLB"]}
    ]}
  ]
}
```

---

## Maintenance

- When `/map-sector` adds or rebuilds a `_Supply Chain Map.md`, assign each new tier to a layer or rail sub-box here and add it to the JSON block.
- Keep this JSON block and the `STACK` object in `Investing/Output/Dashboard/index.html` identical — `/daily-dashboard --refresh-data` regenerates the dashboard from this file.
- Cross-layer dependency edges (the labeled arrows) are distilled in `connectors[]`; the full edge list lives in `Ecosystem Interrelationships.md`.
</content>
</invoke>

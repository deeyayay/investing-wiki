# Compute Infrastructure — Supply Chain Map
*Mapped: 2026-05-24 | Anchor: GPU compute cluster ready for AI training workload*
*Dimension: D3 — AI Infrastructure*
*Folder slug: `AI Infrastructure`*

---

## Framework Status
- [x] Supply chain mapped
- [x] Process/product depth added (2026-05-24)
- [x] Interrelationship Anchors documented (2026-05-24)
- [ ] Nodes registered (`/add-ticker TICKER --layer "Layer"` for each below)
- [ ] Ground truth pulled (`/stock-research TICKER` per node)
- [ ] Customer matrix built (`/build-customer-matrix "Compute Infrastructure"`)
- [ ] Sector Framework written (only after above steps complete)

---

## Value Chain

| Tier | Function | Processes | Key Products / Materials | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|-----------|--------------------------|------------|-------------------|-----------|----------------|
| Compute Node Design & ODM Assembly | Design and assemble the server trays, HGX/MGX baseplates, and GPU compute nodes that house the accelerators | Motherboard design (PCB layout, PDN design, thermal simulation, BIOS/UEFI bring-up); HGX/MGX baseplate mechanical design (NVLink bridge routing, copper busbar to GPU VRM, water block mounting); SMT assembly (GPU BGA/LGA socket placement, VRM power stage, NVMe slot); chassis sheet metal fabrication (1U/2U/4U/8U rack-mount); cable harness assembly (PCIe retimer, OCP NIC, backplane power); POST and system-level test (memory training, GPU initialize, thermal stress test); hyperscaler custom ODM design (open compute / OCP specification compliance) | HGX H200 / HGX B200 server tray (8× GPU, NVLink4 bridge); MGX compute node (modular GPU tray format); 1U/2U CPU-only server; NVMe storage server (24×2.5" JBOF); OCP-compliant compute node; PCIe Gen 5 retimer chip; power shelf (ORV3 / CRPS 3kW) | Partial | Medium | Scale + Customer lock-in (hyperscaler rack integration qualifications are 12–18 months; approved vendor list is small) | Low–Medium |
| High-Speed Networking | Design, integrate, and operate the switches, NICs, and fabric interconnects that move data between GPUs, between servers, and between racks at AI-cluster scale | Switch ASIC tape-out (Broadcom Tomahawk/Jericho, Marvell Teralynx — 51.2T–102.4T switching capacity); switch chassis mechanical design (fixed 1U/2U, modular line-card chassis); NOS (network operating system) development and maintenance (Arista EOS, SONIC, cumulus); NIC driver development and firmware tuning (RDMA over Converged Ethernet, RoCE v2); InfiniBand fabric management (OpenSM subnet manager, UFM); cable plant engineering (DAC, AOC, 400G-DR4 active optic selection and qualification); network telemetry pipeline (INT / gRPC streaming telemetry → TSDB) | 51.2Tbps fixed-form Ethernet switch (Arista 7800, Nexus 93600); 400G/800G spine switch line card; ConnectX-7/8 InfiniBand/Ethernet SmartNIC; 400G-DR4 / 400G-SR4 QSFP-DD transceiver (sourced from Photonics & Optical); InfiniBand NDR 400G / XDR 800G switch (NVDA Quantum-3); 400G OSFP active optical cable | Yes | High | Ecosystem + Switching cost (EOS/JunOS CLI familiarity, management automation, and certification lock-in; 7-year refresh cycles) | Very High |
| Storage Systems | Design, integrate, and operate the flash and object storage systems that hold AI training datasets, model checkpoints, and inference artifacts | NVMe SSD qualification (die type: TLC/QLC/MLC, interface: PCIe Gen 5 NVMe 2.0, endurance binning, thermal throttle characterization); all-flash array design (dual-controller, NVMe-oF fabric attachment, inline deduplication + compression, RAID6/erasure coding); object storage system build (S3-compatible API layer, metadata index, erasure coding stripe, CRUSH mapping); storage fabric: NVMe-oF over RoCE v2 or FC-NVMe (25G/100G lossless fabric); hyperscaler object store (S3, GCS, Azure Blob — software-defined over commodity hardware); GPU-direct storage path (NVMe → GPUDirect RDMA → HBM, bypassing CPU) | All-flash NVMe array (Pure FlashArray//XL, NetApp AFF A-series); JBoF (NVMe-oF JBOF, 24–36×15.36TB NVMe drives); PCIe Gen 5 NVMe SSD (15.36TB U.2 / E3.S form factor); object storage node (2U×72TB JBOD, Ceph / MinIO); Kioxia / Samsung 192-layer TLC NAND die; GPUDirect Storage NVMe driver (NVIDIA CUDA 12+) | No | Medium | Switching cost (storage protocol, data services, and management software lock-in; data migration is operationally expensive) | High |
| Data Center Power Infrastructure | Deliver, transform, condition, and distribute electrical power from utility feed to server board-level power rails, with protection and backup at each stage | Utility service entrance: medium-voltage switchgear (15kV/35kV class, SF6 or vacuum interrupter); step-down transformer (MV→480V/277V, oil-immersed or dry-type, 2–10MVA); UPS topology: modular double-conversion (rectifier → battery bank → inverter, 96–98% efficiency), or DRUPS (diesel rotary), or HVDC flywheel; HVDC distribution: 480VAC rectifier → 800VDC or 400VDC bus → server-embedded DC-DC converter (removes AC UPS and PDU stages); PDU design: per-outlet current metering, remote switching, phase balancing; busway: plug-in busway (Siemens Sivacon, Eaton Pow-R-Way) versus conduit-and-wire; generator: standby diesel genset (Cummins, Caterpillar, 1–3MW per unit) ATS transfer | Medium-voltage switchgear (15kV VCB); dry-type transformer (1600kVA, 480V secondary); modular UPS (50kW–250kW module, hot-swap, 96% efficiency); 800VDC HVDC bus architecture (rectifier + SiC MOSFET DC-DC converter); intelligent PDU (per-outlet metering, C13/C19 outlets); busway section (600A, 4-wire + PE); standby diesel generator (2MW, 12-cylinder) | Yes | Very High | Scale + Certification (HVDC 800V requires redesigned servers, PDUs, and protection devices; no backward compatibility with AC distribution; ecosystem lock-in once architecture is chosen) | Medium–High |
| Thermal Management & Cooling | Remove heat from compute nodes and reject it from the facility using the minimum energy input consistent with the server's thermal design | Air cooling: CRAC/CRAH design (chilled water coil or DX refrigerant, EC fan, 45–60kW capacity per unit), hot/cold aisle containment, overhead blanking panels; direct liquid cooling (DLC): CDU (cooling distribution unit — plate heat exchanger, secondary loop pump, delta-T 40/60°C), manifold routing, cold plate installation on CPU/GPU; immersion cooling: open-bath single-phase (mineral oil or engineered dielectric fluid, 35°C inlet), two-phase (fluorocarbon fluid, phase-change heat rejection at 56°C, 3M Novec EOL → Solvay Galden HT170 migration); rear-door heat exchanger: passive/active coil mounted on rack door; chilled water plant: centrifugal chiller (COP 5–7), cooling tower (wet or adiabatic), hydronic distribution; free cooling economizer (direct or indirect, applicable when outdoor wet-bulb ≤ 18°C) | CDU (40kW–500kW capacity, plate heat exchanger, variable-speed pump); single-phase immersion tank (rack-in-tank, 100kW–300kW per tank); cold plate (Cu or Al, GPU socket-contact, Rth ≤ 0.05 K/W); rear-door HX (passive water coil, 15kW–30kW per rack); chilled water plant (centrifugal chiller, 1000RT capacity); Solvay Galden HT170 / Chemours Opteon dielectric fluid (replacing 3M Novec); cooling tower (evaporative, 6000RT) | No | Very High | Scale + Geographic (data center siting: power cost, water availability, cooling climate determine PUE and economics) | Medium |
| Data Center Facility & MEP | Construct and operate the physical plant: structure, electrical infrastructure, mechanical systems, network entry, and physical security that define a data center tier | Site selection: geotechnical survey, utility capacity confirmation (grid interconnect study), flood/seismic risk; structural: reinforced concrete shell (>200psf floor loading), raised access floor or slab-on-grade, fire suppression (pre-action dry-pipe sprinkler or clean-agent FM-200/Novec 1230); electrical MEP: medium-voltage switchgear room, N+1 generator yard, cable vault, grounding grid; mechanical MEP: chiller plant, cooling tower yard, CDU room, CRAC rows; low-voltage: fiber MDA (main distribution area), structured cabling (OM4/SMF, MPO-24 trunk), telco DEMARC; commissioning: load bank testing, integrated systems test (IST), BMS (building management system) tuning | Pre-action dry-pipe fire suppression (Viking, Tyco); raised access floor panel (600×600mm, 1250kg point load); MPO-24 trunk cable (OM4/SMF); building management system (BMS / DCIM platform); diesel fuel storage (500,000L UST); medium-voltage cable (15kV XLPE, per-section); modular data center container (1MW self-contained module) | No | Very High | Geographic monopoly (specific grid-connected sites with >100MW capacity are genuinely scarce) | Medium |
| Hyperscaler & Colocation Operation | Operate the data center as a service platform: provision capacity, manage workloads, sell compute/storage/network as a service, and maintain SLA commitments | Capacity provisioning: rack deployment, cross-connect wiring, IP address allocation, DNS/DHCP/NTP setup; workload orchestration: Kubernetes cluster management (kubeadm / EKS / GKE), SLURM job scheduler for HPC/AI training, Ray for distributed ML; infrastructure automation: Terraform / Pulumi IaC, Ansible configuration management, GitOps CD pipeline; SLA monitoring: uptime metrics (Tier III 99.982% / Tier IV 99.995%), incident response, NOC 24×7; power metering: per-rack kWh billing (colocation), aggregate PUE monitoring; network interconnect: BGP peering at internet exchange (Equinix, DE-CIX), private connectivity (Direct Connect, ExpressRoute, Cloud Interconnect) | AI training cluster (GPU HPC cluster, 10,000–100,000 GPU scale); Cloud GPU instance (A100, H100, H200 ×8 per node); colocation cage (>1MW, dual-feed, N+1 cooling); internet exchange cross-connect (1G/10G/100G port); DCIM software (Nlyte, Sunbird, or in-house); BGP transit ASN; SLO-backed inference endpoint (GPU/TPU millisecond latency) | Partial | Very High | Scale + Ecosystem (hyperscaler lock-in via API/SDK ecosystem, egress pricing, colocation switching cost via cross-connect lock-in) | High |

---

## Publicly-Traded Nodes

| Tier | Ticker | Company | Mkt Cap | In Registry | Notes |
|------|--------|---------|---------|-------------|-------|
| Compute Node Design & ODM Assembly | SMCI | Super Micro Computer | Large | Yes | #1 AI server ODM by design innovation; HGX/MGX tray specialist |
| Compute Node Design & ODM Assembly | 2308.TW | Delta Electronics (Taiwan) | Large | No | Taiwan-listed; power supplies + server designs; major Nvidia system integrator |
| Compute Node Design & ODM Assembly | 6669.TW | Wistron Corporation | Large | No | Taiwan ODM; AI server and OCP production for US hyperscalers |
| Compute Node Design & ODM Assembly | 3017.TW | Tatung Company | Small | No | Taiwan; ODM server (also industrial / display); smaller AI server exposure |
| Compute Node Design & ODM Assembly | 3324.TW | Inventec Corporation | Large | No | Taiwan ODM; high AI server revenue growth; HP/HPE + hyperscaler customer |
| Compute Node Design & ODM Assembly | 6367.T | Mitsubishi Electric (partial) | Large | No | Japan; some server/cooling for data center; not a primary AI server play |
| High-Speed Networking | ANET | Arista Networks | Large | Yes | #1 hyperscale Ethernet switching; EOS software moat; 800G transition |
| High-Speed Networking | — | *Broadcom AVGO (switch ASIC)* | Large | No | ⚠️ Switch ASIC (Tomahawk, Jericho) — registered in Semiconductors sector |
| High-Speed Networking | — | *NVDA NVSwitch / Quantum-3* | Large | No | ⚠️ InfiniBand switch — registered in Semiconductors sector |
| Storage Systems | P | Pure Storage | Large | Yes | #1 pure-play enterprise all-flash; FlashArray//XL; AI storage positioning |
| Storage Systems | NTAP | NetApp | Large | No | All-flash arrays + object storage (ONTAP / StorageGRID); strong AI pipeline |
| Storage Systems | WDC | Western Digital | Large | No | NVMe SSD + HDD; enterprise flash for hyperscalers; NAND vertically integrated |
| Storage Systems | STX | Seagate Technology | Large | No | HDD dominant; high-capacity nearline storage for object stores |
| Data Center Power Infrastructure | VRT | Vertiv Holdings | Large | Yes | PDUs, UPS (modular Li-ion), busway, switchgear; strong 800VDC transition exposure |
| Data Center Power Infrastructure | ETN | Eaton Corporation | Large | No | Modular UPS (93PM), PDUs, busway, switchgear; broad power management |
| Data Center Power Infrastructure | NVT | nVent Electric | Large | No | Enclosures, cable management, liquid cooling components |
| Thermal Management & Cooling | VRT | Vertiv Holdings | Large | Yes | CDUs, precision cooling (CRV, CRH), CRAC/CRAH; thermal + power integrated |
| Thermal Management & Cooling | MOD | Modine Manufacturing | Mid | No | CDUs, cold plates, dry coolers for liquid cooling; AI data center focused pivot |
| Thermal Management & Cooling | NVT | nVent Electric | Large | No | Enclosures + thermal solutions for IT racks |
| Thermal Management & Cooling | — | *Asetek A/S* | Small | No | ⚠️ Denmark-listed (ASETEK); liquid cooling for HPC — not US-listed |
| Thermal Management & Cooling | — | *CoolIT Systems* | — | No | ⚠️ Private; CDU supplier to hyperscalers; major market share |
| Data Center Facility & MEP | — | *Equinix (EQIX)* | Large | No | ⚠️ Colocation REIT — primarily a real estate / interconnect business, not compute supply chain |
| Data Center Facility & MEP | — | *QTS / Digital Realty* | Large | No | ⚠️ DC REIT — facility operators, not supply chain nodes |
| Hyperscaler & Colocation Operation | AMZN | Amazon (AWS) | Large | No | #1 cloud (AWS); dominant AI training (P5 H100, P4d A100, Trainium) |
| Hyperscaler & Colocation Operation | GOOGL | Alphabet (GCP) | Large | No | GCP + TPU v5; custom silicon self-reinforcing hyperscaler moat |
| Hyperscaler & Colocation Operation | MSFT | Microsoft (Azure) | Large | No | Azure AI; Copilot cloud; deepest OpenAI integration |
| Hyperscaler & Colocation Operation | META | Meta Platforms | Large | No | Private cloud; MTIA custom ASIC; largest organic GPU capex |
| Hyperscaler & Colocation Operation | ORCL | Oracle Cloud | Large | No | OCI GPU clusters; NVIDIA preferred partner; GenAI workload momentum |
| Hyperscaler & Colocation Operation | IREN | IREN Limited | Mid | Yes | HPC/AI compute (pivoting from Bitcoin mining); low-cost power sites |

---

## Structural Gaps

### Gap: Thermal Management — Two-Phase Immersion Cooling Fluid (Post-Novec)
3M discontinued Novec engineering fluids (PFAS-related regulatory pressure), forcing immersion cooling vendors to migrate to alternatives: Solvay Galden HT170, Chemours Opteon, Engineered Fluids HFE-7100/7200. None of the fluid suppliers are US-listed pure-plays — Solvay (Belgium, Euronext: SOLB) and Chemours (CC, US-listed but diversified specialty chemicals) are the closest. The two-phase immersion market is growing rapidly (Nvidia's NVL72 rack reference design specifies liquid cooling readiness) but the fluid supply chain is fragile. **Watch for:** CC (Chemours) Opteon product revenue; any Solvay spin-off of the specialty fluids division.

### Gap: Smart NIC / DPU (Data Processing Unit)
The DPU/SmartNIC layer (NVIDIA BlueField, Marvell Octeon, Intel IPU) offloads network, storage, and security processing from host CPUs. This is a critical architectural tier for disaggregated compute. NVDA's BlueField-3 and -4 are sold as part of NVDA platform but are primarily semiconductor products. Marvell Octeon (MRVL) is registered in Semiconductors. There is no pure-play publicly listed DPU company outside of these. **Watch for:** Any fabless DPU startup (Fungible — acquired by MSFT) going public; Broadcom Stingray portfolio.

### Gap: Colocation / Hyperscale Facility
Digital Realty (DLR), Equinix (EQIX), and Iron Mountain (IRM) are the major listed colocation operators, but they are REITs structured around real estate cash flows — not a compute supply chain play in the traditional sense. Private developers (Switch, QTS before acquisition) have been taken private. The actual AI training clusters inside these facilities are owned by the hyperscalers themselves. **Watch for:** Any data center developer going public as a compute-focused (not real estate REIT) entity; hyperscaler facility spin-offs.

---

## Key Questions to Answer Before Writing the Sector Framework

1. Does the 800VDC HVDC architecture transition happen fast enough to be a 2026–2028 revenue inflection for Vertiv and power infrastructure vendors — or is the rack-level electrical redesign a multi-year replacement cycle that delays meaningful revenue?
2. Is Arista's software moat (EOS) durable against SONIC (open-source NOS backed by Microsoft/Google/Alibaba) as hyperscalers increasingly self-supply network software?
3. With Taiwan ODMs (SMCI, Quanta, Wistron, Inventec) controlling the majority of AI server assembly, what is the geopolitical risk to the AI server supply chain — and which US-friendly alternatives exist?
4. As immersion cooling becomes standard for >300W GPU trays, does the CDU/immersion segment become a genuine chokepoint — or does commoditization keep margins low despite volume growth?
5. Does Pure Storage's all-flash positioning survive contact with hyperscaler object storage (S3/GCS) at scale, or is enterprise all-flash only a training cluster use case that eventually moves to cloud-native object storage?
6. Is the GPU compute market (AWS/GCP/Azure) structurally constrained by NVDA chip allocation, or is the arrival of AMD MI300X, Google TPU v5, AWS Trainium2, and Microsoft Maia sufficient to break the allocation control?

---

## Interrelationship Anchors

### Inputs (this sector consumes from)

| From Sector | From Tier | Product / Signal |
|---|---|---|
| Semiconductors | Design (Compute) | GPU (H200/B200), CPU (EPYC/Xeon), networking ASIC (Tomahawk, ConnectX-8), custom ASIC (TPU, Trainium, Maia) → compute node |
| Semiconductors | Design (Memory) | HBM3/HBM3e stack → GPU memory subsystem; DDR5 DIMM → CPU memory channel |
| Semiconductors | Power Devices | SiC MOSFET → 800VDC HVDC rectifier module + DC-DC converter stage |
| Electronic Components | PCB Fabrication | 24L+ HDI PCB → server motherboard, GPU tray baseplate, switch line card |
| Electronic Components | MLCC Manufacturing | X5R/X7R MLCC (100V class) → server PCB decoupling array, VRM output filter |
| Electronic Components | IC Substrate Mfg | ABF flip-chip BGA substrate → GPU/CPU package mount |
| Electronic Components | Connector & Socket Mfg | PCIe Gen 5 edge connector, QSFP-DD cage, C13/C19 power outlet → server chassis |
| Electronic Components | PCB Assembly (EMS) | Populated PCBA (motherboard, GPU board, PSU board) → server chassis integration |
| Photonics & Optical | Transceiver & Module | 400G/800G/1.6T QSFP-DD/OSFP transceiver → spine/leaf switch port, GPU server NIC |
| Photonics & Optical | Optical Fiber & Preform | Single-mode fiber trunk (MPO-24) → intra-DC structured cabling, inter-DC backbone |
| Photonics & Optical | Coherent Line Systems | ROADM chassis → inter-DC wavelength-switched optical network layer |
| Energy & Power | Power Conversion | 800VDC HVDC bus (AC→800VDC rectifier) → server-embedded DC-DC stage |
| Energy & Power | Grid-Scale Storage | Li-ion UPS / BESS → uninterruptible power feed (N+1 backup) |
| Energy & Power | Power Generation | Utility grid interconnect (33kV / 110kV) → on-site substation → data center MV bus |

### Outputs (this sector supplies to)

| To Sector | To Tier | Product / Signal |
|---|---|---|
| Semiconductors | Design (Compute) | Hyperscaler GPU capex guidance → AI chip demand pull (primary forward indicator for NVDA/AMD/AVGO) |
| Energy & Power | Power Generation | Data center power purchase agreements (PPAs) → utility-scale solar, wind, nuclear FID signals |
| Cybersecurity | Security Operations | Infrastructure telemetry, VPC flow logs, API audit logs → SIEM/XDR ingestion and threat detection |
| Robotics & Edge AI | Edge Inference | Cloud inference API (LLM endpoint, vision model) → robot remote cognition; model checkpoint download → edge update |
| Fintech & Commerce AI | AI Model Serving | GPU cluster → real-time fraud scoring, credit model training, LLM inference for commerce AI |
| Energy & Power | Thermal Recovery | CDU / immersion coolant waste heat (40–70°C) → facility heat recovery or district heating loop |
| Space & Communications | Ground Segment | Cloud compute + storage → satellite telemetry processing, ground segment mission control |

---

## Research Log
- **2026-05-24** — Initial map-sector run. 7 tiers, 2 chokepoints (Y/Partial): High-Speed Networking (Y — EOS moat, switch ASIC duopoly), Data Center Power Infrastructure (Y — 800VDC architecture lock-in once chosen). 3 structural gaps: two-phase immersion fluid (post-Novec, no US pure-play), SmartNIC/DPU (NVDA/MRVL embedded in Semiconductors), DC facility (REIT structure, not compute supply chain node). Already registered in AI Infrastructure: IREN, ANET, VRT, SMCI, P. Not yet in registry (files exist): AMZN, GOOGL, META, MSFT, ORCL, MOD, NVT, 2308.TW, 3017.TW, 3324.TW, 6367.T, 6669.TW. New candidates not yet registered: NTAP, WDC, STX, ETN.

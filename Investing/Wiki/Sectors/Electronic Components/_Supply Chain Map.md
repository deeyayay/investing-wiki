# Electronic Components — Supply Chain Map
*Mapped: 2026-05-24 | Anchor: populated PCB ready for system assembly*
*Dimension: D1 — AI Manufacturing Base*

---

## Framework Status
- [x] Supply chain mapped
- [x] Process/product depth added (2026-05-24)
- [x] Interrelationship Anchors documented (2026-05-24)
- [ ] Nodes registered (`/add-ticker TICKER --layer "Layer"` for each below)
- [ ] Ground truth pulled (`/stock-research TICKER` per node)
- [ ] Customer matrix built (`/build-customer-matrix "Electronic Components"`)
- [ ] Sector Framework written (only after above steps complete)

---

## Value Chain

| Tier | Function | Processes | Key Products / Materials | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|-----------|--------------------------|------------|-------------------|-----------|----------------|
| Dielectric & Conductor Materials | Synthesize and refine the functional materials that passive components are built from | Barium titanate (BaTiO₃) synthesis via solid-state reaction or hydrothermal method; high-purity copper foil rolling (electrolytic deposition to 9–70µm); polypropylene / polyester film extrusion and biaxial stretching; tantalum powder reduction (sodium metallothermic); aluminum foil etching (AC electrochemical etch to increase surface area); nickel powder synthesis (CVD or wet-chemical reduction) | Barium titanate powder (X5R/X7R/C0G grade); electrolytic copper foil (9µm, 12µm, 18µm); biaxially oriented polypropylene (BOPP) film; tantalum powder and pellet; etched aluminum foil; nickel internal electrode paste | Yes | Medium | Process IP + Geographic monopoly (BaTiO₃: Sakai, Ferro/Johnson Matthey; Ta: Cabot, Global Advanced Metals) | Medium |
| Substrate & Laminate Materials | Produce the insulating base layers and build-up films that PCBs and IC substrates are constructed from | FR-4 glass-fabric prepreg (epoxy resin + E-glass weave impregnation + B-stage cure); high-frequency laminate production (PTFE + ceramic filler + woven glass); ABF (Ajinomoto build-up film) coating (epoxy + filler on PET release liner); Megtron / Rogers laminate layup; low-loss dielectric characterization (Dk/Df measurement); adhesive-less laminate (rolled copper on polyimide for flex) | FR-4 prepreg / copper-clad laminate (CCL); ABF substrate film; PTFE/ceramic high-frequency laminate (Rogers 4350B, Megtron 6); polyimide flex laminate; BT (bismaleimide triazine) resin laminate (for IC substrates) | Yes | Medium | Process IP + Qualification (ABF: Ajinomoto sole supplier of the film itself; BT resin: Mitsubishi Gas Chemical) | Medium–High |
| MLCC Manufacturing | Stack, fire, and terminate ceramic multilayer chip capacitors — the most ubiquitous passive component on any PCB | Ceramic slurry casting (tape casting of BaTiO₃ + binder to 1–3µm green tape); screen printing of Ni internal electrodes; layer stacking and lamination (hundreds to thousands of layers); co-firing (sintering at 1200–1300°C in reducing atmosphere); barrel tumbling and termination (Ag/Ni/Sn end caps); electrical testing (capacitance, dissipation factor, IR, withstanding voltage); taping and reeling | MLCC (0402, 0201, 01005 case sizes; X5R/X7R/C0G dielectric; 4V–1kV); Ni internal electrode (base metal); BaTiO₃ dielectric body; Ag-Pd or Cu termination alloy | Partial | High | Scale + Process IP (ultra-thin tape casting and Ni electrode co-fire at scale are hard to replicate) | Medium–High |
| Film & Electrolytic Capacitor Mfg | Produce high-voltage and high-capacitance capacitors for power electronics, filtering, and energy storage | BOPP film winding (film + aluminum foil, dry winding or oil-impregnated); metallization (vacuum Al or Zn deposition on BOPP to create self-healing electrode); wet electrolytic: anode foil formation (anodizing etched Al foil to grow Al₂O₃ dielectric); cathode foil etching; electrolyte fill and sealing; tantalum wet/solid: Ta powder pressing + sintering + anodizing + MnO₂ or PEDOT counter-electrode coating | Metallized polypropylene film capacitor (MKP, 250V–2kV range); wet aluminum electrolytic capacitor (low-ESR, 16V–450V); solid tantalum capacitor (Ta/MnO₂, Ta/PEDOT); polymer aluminum electrolytic (low-ESR, long life) | No | Medium | Scale + Process IP | Medium |
| Inductor & Transformer Mfg | Wind, press, or print inductive components for power conversion, filtering, and signal isolation | Wire-wound inductor: toroidal / drum core winding (Cu wire on ferrite or iron powder core); multilayer chip inductor: ferrite paste printing and cofiring (similar to MLCC process); power inductor: metal composite core pressing (Fe-Si-Cr alloy powder + binder, compression molding); planar transformer: PCB winding etching + ferrite core assembly; wireless charging coil: Litz wire winding or printed coil | Wire-wound ferrite chip inductor (0402–1210 case); metal composite power inductor (high Isat, low DCR); ferrite core (MnZn, NiZn); planar transformer; common mode choke (CMC) for EMI filtering | No | Medium | Scale + Certification | Medium |
| PCB Fabrication | Etch, drill, plate, and laminate copper circuit layers onto insulating substrates to create printed circuit boards | Inner layer imaging (DES: dry film lamination → UV exposure → develop → etch → strip); multilayer lamination (oxide treatment + prepreg + outer copper foil, hydraulic press cure); mechanical drilling + laser via drilling (CO₂ for microvias); electroless copper plating (PTH: catalysis → electroless → electrolytic Cu fill); solder mask application (LPI coating, UV cure, develop); ENIG / HASL / OSP surface finish; electrical test (flying probe or bed-of-nails) | Multi-layer PCB (4L–32L+); HDI PCB (high-density interconnect, microvia); rigid-flex PCB; copper-clad laminate (CCL) input; solder mask (LPI); ENIG / HASL / OSP surface finish | No | Medium | Scale + Certification | Low–Medium |
| IC Substrate Manufacturing | Build the fine-pitch interposer layers that bridge IC die to PCB — the most technically demanding segment of the package supply chain | Coreless substrate build-up: seed layer sputtering → SAP (semi-additive process) Cu plating → photolithography (L/S down to 2µm/2µm) → dielectric (ABF) lamination → laser via drilling → repeat for each layer; BGA ball attach; impedance testing; automated optical inspection (AOI); SLT electrical test | ABF (build-up film) IC substrate (flip-chip BGA, 2–12 layer); coreless substrate (for CoWoS interposer support); BT resin substrate (wire-bond BGA); solder ball (SAC305 / SnAgCu); substrate test coupon | Yes | High | Process IP + Qualification (advanced node substrates qualified per foundry PDK — switching cost extremely high) | High |
| Connector & Socket Manufacturing | Form, plate, and assemble the mechanical and electrical interfaces that link boards, modules, cables, and racks | Metal stamping (Cu alloy strip → progressive die stamping of contact geometry); electroplating (Ni underplate + Au or Pd-Ni on contact surfaces); insert molding (thermoplastic housing over contacts); assembly and force testing; high-speed signal testing (insertion loss, return loss, crosstalk to 112 Gbps PAM4); coax cable assembly (crimping, soldering, torque spec) | High-speed PCIe Gen 5/6 edge connector; DDR5 DIMM socket; SFP+ / QSFP-DD cage and connector; coaxial RF connector (SMA, SMPM, BMA); board-to-board mezzanine connector; power connector (blade, press-fit) | No | Medium | Switching cost + Certification | Medium–High |
| PCB Assembly (EMS / PCBA) | Place and solder all components onto populated PCBs at volume; the final integration step before system-level assembly | Solder paste printing (stencil printing, Cp >1.67); SMT pick-and-place (high-speed chip shooter + precision placer); reflow soldering (N₂ atmosphere, lead-free SAC305 profile); selective soldering / wave soldering (through-hole); automated optical inspection (AOI); X-ray inspection (BGA joint verification); in-circuit test (ICT / bed-of-nails); conformal coating; depaneling | Populated PCBA (server motherboard, GPU board, power supply board); solder paste (SAC305 / low-Ag alloy); SMT stencil; flux; underfill (for BGA/flip-chip joints); conformal coating | No | Low–Medium | Scale + Customer lock-in | Low–Medium |

---

## Publicly-Traded Nodes

| Tier | Ticker | Company | Mkt Cap | In Registry | Notes |
|------|--------|---------|---------|-------------|-------|
| Dielectric & Conductor Materials | 6981.T | Murata Manufacturing | Large | No | #1 MLCC globally; also controls significant BaTiO₃ supply internally |
| Dielectric & Conductor Materials | CCMP | CMC Materials (Entegris sub) | — | No | Specialty chemical materials; overlap with Semiconductors Raw Materials tier |
| Dielectric & Conductor Materials | — | *Cabot Microelectronics / Global Advanced Metals* | — | No | ⚠️ Ta powder — mostly private or embedded in diversified miners |
| Substrate & Laminate Materials | — | *Ajinomoto Fine-Techno* | — | No | ⚠️ ABF film — sole supplier; Ajinomoto parent is food company (not investable on ABF alone) |
| Substrate & Laminate Materials | RCI | Rogers Corporation | Mid | No | High-frequency PTFE/ceramic laminates (Rogers 4000 series); antenna substrates |
| Substrate & Laminate Materials | — | *Mitsubishi Gas Chemical* | — | No | ⚠️ BT resin for IC substrates — Japan-listed, BT is minority of revenue |
| MLCC Manufacturing | 6981.T | Murata Manufacturing | Large | No | ~40% global MLCC share; dominant in high-layer-count, small case sizes |
| MLCC Manufacturing | 6762.T | TDK Corporation | Large | No | #2 MLCC; also ferrite cores, inductors, sensors |
| MLCC Manufacturing | 2327.TW | Yageo Corporation | Large | No | #3 MLCC globally; Taiwan-listed; KEMET acquisition |
| MLCC Manufacturing | AVX | Kyocera AVX | Mid | No | US-listed; Kyocera subsidiary; MLCC + tantalum + connectors |
| Film & Electrolytic Capacitor Mfg | 6762.T | TDK Corporation | Large | No | Aluminum electrolytic + film cap exposure via EPCOS brand |
| Film & Electrolytic Capacitor Mfg | 2327.TW | Yageo Corporation | Large | No | KEMET acquisition brought film and electrolytic capacity |
| Film & Electrolytic Capacitor Mfg | VSH | Vishay Intertechnology | Mid | No | Broad passive portfolio: tantalum, film, electrolytic, resistors |
| Film & Electrolytic Capacitor Mfg | — | *WIMA / Würth Elektronik* | — | No | ⚠️ Film cap for power electronics — mostly private German companies |
| Inductor & Transformer Mfg | 6762.T | TDK Corporation | Large | No | Power inductors (EPCOS brand) + ferrite cores |
| Inductor & Transformer Mfg | 6981.T | Murata Manufacturing | Large | No | Chip inductors; common mode chokes |
| Inductor & Transformer Mfg | CODA | Coda Octopus (not relevant) | — | No | — |
| Inductor & Transformer Mfg | VSH | Vishay Intertechnology | Mid | No | Inductors + transformers in passive line |
| PCB Fabrication | TTM | TTM Technologies | Mid | No | #1 US PCB; advanced PCBs for AI servers, aerospace |
| PCB Fabrication | 4063.TW | Tripod Technology | Mid | No | Taiwan-listed; AI server HDI PCBs |
| PCB Fabrication | ZD | Zhen Ding Technology | Large | No | Taiwan-listed; flex PCB leader (Apple + AI infrastructure) |
| PCB Fabrication | CMK | CMK Corporation | Small | No | Japan-listed; high-layer PCBs for servers |
| IC Substrate Manufacturing | 3036.TW | Unimicron Technology | Large | No | #1 IC substrate globally; advanced ABF substrates for AMD/Intel |
| IC Substrate Manufacturing | 8046.TW | Nan Ya PCB | Large | No | #2 IC substrate; also conventional PCBs |
| IC Substrate Manufacturing | 3037.TW | Ibiden Co. | Large | No | Japan-listed; #3 IC substrate; ABF-based; NVIDIA customer |
| IC Substrate Manufacturing | 3044.TW | Kinsus Interconnect Technology | Mid | No | Taiwan-listed; advanced IC substrates |
| Connector & Socket Manufacturing | TEL | TE Connectivity | Large | No | Broadest connector portfolio; automotive + data center + industrial |
| Connector & Socket Manufacturing | APH | Amphenol Corporation | Large | No | #2 connector; strong data center and AI infrastructure exposure |
| Connector & Socket Manufacturing | MDD | Molex (private, Koch Industries) | — | No | ⚠️ #3 connector — private |
| Connector & Socket Manufacturing | JBL | Jabil (straddles EMS) | Large | No | Also significant EMS / PCBA volume |
| PCB Assembly (EMS / PCBA) | JBL | Jabil Inc. | Large | No | #2 EMS globally; AI server PCBA + power supply assembly |
| PCB Assembly (EMS / PCBA) | CLS | Celestica | Mid | No | EMS; growing AI infrastructure PCBA share |
| PCB Assembly (EMS / PCBA) | BHE | Benchmark Electronics | Small | No | Specialty EMS; defense + industrial |
| PCB Assembly (EMS / PCBA) | — | *Foxconn / Hon Hai* | Large | No | ⚠️ #1 EMS globally — Taiwan-listed (2317.TW); not pure-play US-accessible |

---

## Structural Gaps

### Gap: Dielectric & Conductor Materials — Barium Titanate
BaTiO₃ is the dielectric backbone of every MLCC. The major producers (Sakai Chemical, Ferro/Johnson Matthey, Fuji Titanium, Solvay) are either Japan-listed subsidiaries or private. No US-listed pure-play. Murata produces much of its own BaTiO₃ internally. **Watch for:** Any BaTiO₃ producer spin-off or specialty chemical IPO in Japan.

### Gap: Substrate & Laminate Materials — ABF Film
Ajinomoto Build-up Film (ABF) is the sole-source dielectric used in advanced IC substrates (flip-chip BGA, CoWoS support). The supplier is Ajinomoto Fine-Techno, a division of Ajinomoto Co. (food company). ABF is ~2% of Ajinomoto's revenue — no investable pure-play. This is the single most structurally important gap in the electronic components supply chain: every AI chip packaging capacity increase at TSMC/AMKR depends on ABF throughput. **Watch for:** Any Ajinomoto reporting of capacity expansion plans; substrate maker capex as a proxy.

### Gap: Substrate & Laminate Materials — BT Resin
Bismaleimide triazine (BT) resin is used in wire-bond IC substrates (BGA packages for mid-range chips). Mitsubishi Gas Chemical dominates. Japan-listed, BT is a small revenue line. No US-listed exposure.

### Gap: Film Capacitors for Power Electronics (HVDC)
The 800–1000V polypropylene film capacitors required for HVDC data center architecture (800VDC bus) are produced primarily by WIMA (Germany, private), Würth Elektronik (Germany, private), and Nichicon (Japan). Vishay has some exposure but it is not the primary source. This is a direct dependency of the 800VDC DC power shift — as HVDC architecture scales, this gap becomes a monitoring priority. **Watch for:** Vishay film cap revenue breakout; Nichicon (Japan-listed) guidance on high-voltage film cap demand.

### Gap: EMS at Scale — Foxconn
Hon Hai / Foxconn (2317.TW) is the #1 EMS globally by a wide margin but is Taiwan-listed and not a pure-play electronic components player. Its AI server assembly volume (NVIDIA GB200 NVL racks) makes it a critical node. **Watch for:** Any Hon Hai ADR issuance or US-listed subsidiary.

---

## Key Questions to Answer Before Writing the Sector Framework

1. As AI server power density increases (from 10kW to 100kW+ per rack), which passive component specs are the binding constraint — MLCC voltage rating, film cap energy density, or inductor current saturation?
2. Does the 800VDC data center architecture shift create a measurable revenue inflection for film capacitor and connector manufacturers before 2028?
3. Is the ABF substrate gap a resolvable capacity problem (Ibiden/Unimicron capex) or a materials science problem (no ABF alternative exists at scale)?
4. Which IC substrate makers are qualified for the CoWoS HBM3e/HBM4 interposer process, and does that qualification confer pricing power?
5. Does the CPO (co-packaged optics) transition eliminate the QSFP-DD connector tier or create a new, higher-value photonic connector tier?
6. Are the major MLCC makers (Murata, TDK, Yageo) supply-constrained or demand-constrained entering 2027 — and does AI server PCB BOM density increase their TAM materially?

---

## Interrelationship Anchors

### Inputs (Electronic Components consumes from)

| From Sector | From Tier | Product / Signal |
|---|---|---|
| Materials & Mining | Copper Mining & Refining | High-purity electrolytic copper foil (9–18µm) → MLCC terminations, PCB inner layers, IC substrate SAP plating |
| Materials & Mining | Rare Earth & Specialty Metals | Tantalum powder → solid tantalum capacitor; Nickel powder → MLCC internal electrode paste; Palladium → high-rel Ag-Pd termination alloy |
| Materials & Mining | Barium / Titanium Chemicals | Barium carbonate + titanium dioxide → BaTiO₃ dielectric powder for MLCC |
| Semiconductors | Packaged ICs | GPU, CPU, ASIC, memory die → SMT placement on PCBA (Electronic Components provides the board; Semiconductors provides the components placed on it) |
| Energy & Power | Grid Power | Fab-grade power → MLCC kiln firing (1200°C reducing atmosphere), PCB plating baths, laminate press |

### Outputs (Electronic Components supplies to)

| To Sector | To Tier | Product / Signal |
|---|---|---|
| Compute Infrastructure | Server Assembly | Populated PCBA (motherboard, GPU board, NIC, PSU board) → server chassis integration |
| Compute Infrastructure | Server Assembly | MLCC (X5R/X7R, 100V class) → decoupling on every server PCB |
| Compute Infrastructure | Networking | High-speed PCIe/QSFP-DD connector → switch/NIC port; PCB backplane → chassis interconnect |
| Compute Infrastructure | Power Distribution | IC substrate (flip-chip BGA) → CPU/GPU package; ABF substrate → TSMC/AMKR advanced packaging input |
| Energy & Power | Power Conversion | 900V polypropylene film capacitor → HVDC rectifier DC bus filter |
| Energy & Power | Power Conversion | Metal composite power inductor → DC-DC converter output filter |
| Energy & Power | Power Conversion | DC-rated connector → 800VDC bus bar termination |
| Semiconductors | Packaging (OSAT) | ABF IC substrate → flip-chip BGA package; BT resin substrate → wire-bond BGA |
| Photonics & Optical | Transceiver Mfg | High-frequency PTFE/ceramic PCB (Rogers 4350B) → optical transceiver RF board |
| Photonics & Optical | Transceiver Mfg | QSFP-DD / SFP56 cage + connector → transceiver module housing and electrical interface |
| Robotics & Edge AI | Actuator & Sensor Integration | Multi-layer PCB, connectors → robot compute and power board assembly |
| Space & Communications | Satellite Bus | High-rel MLCC (MIL-PRF-55681 rated) → satellite PCB; space-grade connector → harness assembly |

---

## Research Log
- **2026-05-24** — Initial map-sector run. 9 tiers mapped, 4 chokepoints (Y or Partial): Dielectric & Conductor Materials (Y), Substrate & Laminate Materials (Y), MLCC Manufacturing (Partial), IC Substrate Manufacturing (Y). 4 structural gaps flagged: BaTiO₃, ABF film, BT resin, high-voltage film caps for HVDC. No tickers currently in registry for this sector. New candidates: 6981.T (Murata), 6762.T (TDK), 2327.TW (Yageo), RCI (Rogers), VSH (Vishay), TTM (TTM Technologies), 3036.TW (Unimicron), 3037.TW (Ibiden), 8046.TW (Nan Ya PCB), TEL (TE Connectivity), APH (Amphenol), JBL (Jabil), CLS (Celestica).

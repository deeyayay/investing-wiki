# Semiconductors — Supply Chain Map
*Mapped: 2026-05-24 | Rebuilt: 2026-05-24 | Anchor: packaged chip ready for electronic assembly*
*Dimension: D1 — AI Manufacturing Base*

---

## Framework Status
- [x] Supply chain mapped
- [x] Process/product depth added (2026-05-24)
- [x] Interrelationship Anchors documented (2026-05-24)
- [ ] Nodes registered (`/add-ticker TICKER --layer "Layer"` for each below)
- [ ] Ground truth pulled (`/stock-research TICKER` per node)
- [x] Customer matrix built (`/build-customer-matrix "Semiconductors"`) — 2026-05-24
- [ ] Sector Framework written (only after above steps complete)

*Note: 7 tickers already registered (NVDA, MU, MRVL, AEHR, ALAB, CRDO, AMKR). Run `/add-ticker TICKER --layer "Layer"` to backfill the Layer field for existing names, and to onboard new candidates below.*

---

## Value Chain

| Tier | Function | Processes | Key Products / Materials | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|-----------|--------------------------|------------|-------------------|-----------|----------------|
| Raw Materials | Purify silicon; produce specialty gases, CMP slurries, photoresists, and process chemicals | Siemens process (trichlorosilane → polysilicon); Czochralski crystal growth (boule); chemical synthesis (photoresist PAGs, solvents); slurry formulation (colloidal silica + abrasive + chemistry) | Polysilicon ingot; silicon boule (300mm, 200mm); ultra-high-purity gases (SiH₄, NF₃, NH₃, HCl, O₂); EUV photoresist (chemically amplified); BARC / TARC; CMP slurry; cleaning solvents | Partial | Medium | Geographic monopoly (Japan/Germany concentrate specialty chemicals and photoresist) | Medium |
| Wafer Production | Slice, lap, etch, polish, and certify silicon wafers to sub-nanometer flatness | Wire-saw slicing; lapping; KOH/TMAH etching; double-side polishing (DSP); chemical-mechanical polishing (CMP); epitaxial deposition (CVD); wafer inspection (laser scanning) | Prime silicon wafer (300mm); epi wafer; silicon-on-insulator (SOI) wafer; SiC wafer (4H-SiC for power); GaN-on-silicon wafer | Yes | High | Scale + Process IP | Medium |
| EDA & Design IP | Provide software tools and licensable IP cores for chip architecture, RTL design, and physical implementation | RTL design (Verilog/SystemVerilog); logic synthesis; place & route (P&R); static timing analysis (STA); DRC/LVS sign-off; GDSII/OASIS tape-out; formal verification; simulation (SPICE, VCS); IP integration (ARM CPU cores, PCIe/USB PHY) | EDA software license; RTL netlist; gate-level netlist; GDSII layout file; standard cell library; ARM Cortex / Neoverse CPU IP; PCIe / CXL / USB PHY IP | Yes | Low | Switching cost + Ecosystem | Very High |
| Lithography Equipment | Project circuit patterns onto wafers using UV or EUV light; etch features at sub-3nm nodes | EUV light generation (CO₂ laser → tin plasma → 13.5nm photons); multilayer mirror optics (Mo/Si); wafer stage positioning (<1nm accuracy); DUV (ArF immersion, 193nm); multiple patterning (SAQP) | EUV scanner (ASML NXE/EXE series); DUV scanner (ArF immersion); photomask (quartz + Cr + EUV absorber); EUV pellicle; photomask blank; reticle pod (SMIF) | Yes | Very High | Process IP + Geographic monopoly | Very High |
| Deposition & Etch Equipment | Deposit thin films atom-by-atom (CVD/ALD) and etch features with atomic precision | Chemical vapor deposition (CVD); atomic layer deposition (ALD); physical vapor deposition (PVD / sputtering); plasma-enhanced CVD (PECVD); atomic layer etch (ALE); deep reactive ion etch (DRIE); wet etch (HF, SC-1, SC-2) | CVD reactor; ALD chamber; PVD sputter target; etch tool; process gases (WF₆, TiCl₄, TDMAT, TEOSi); thin film stacks (High-K dielectric, metal gate, BEOL Cu interconnect) | Partial | High | Process IP + Switching cost | High |
| Inspection & Metrology | Measure and verify each process step; detect defects before they propagate through subsequent layers | Optical wafer inspection (bright-field, dark-field); e-beam inspection; CD-SEM (critical dimension); OCD (optical critical dimension scatterometry); overlay metrology; film thickness measurement (ellipsometry, XRF); defect review SEM | KLA Surfscan; CD-SEM system; overlay metrology tool; ellipsometer; inline defect map; process control data stream | Partial | Medium | Switching cost + Certification | High |
| Wafer Fabrication (Foundry) | Run wafers through 500–1,000+ process steps to produce functional die | FEOL (transistor formation: gate oxide growth, ion implantation, source/drain anneal); BEOL (interconnect: Cu damascene, low-K ILD, barrier metal); CMP between layers; multi-patterning lithography; process integration across 100+ modules | FEOL process recipe; BEOL Cu interconnect stack; finished 300mm wafer (functional die); process design kit (PDK) | Yes | Very High | Process IP + Scale + Certification | High (cyclical) |
| Power Devices | Design and fabricate SiC / GaN power transistors for high-voltage, high-efficiency switching | SiC boule growth (Lely / modified Lely); SiC wafer slicing + polishing; SiC epitaxial deposition (CVD); ion implantation; gate oxide formation; metallization; SiC MOSFET cell layout; GaN HEMT (MOCVD growth on SiC or Si); module packaging (wire bond or sintered silver) | SiC MOSFET (650V, 1200V, 1700V classes); GaN-on-SiC HEMT; SiC power module (half-bridge, full-bridge); 4H-SiC substrate; SiC epi wafer | Yes | High | Process IP + Certification | High |
| Test (Wafer-Level) | Electrically probe die on wafer before dicing; burn-in for reliability screening | Wafer probing (parametric test, functional test); wafer-level burn-in (WLBI) — apply voltage/thermal stress to accelerate latent defects; WLBI is mandatory for SiC reliability qualification | Wafer prober; WLBI tool; parametric test data; wafer map (pass/fail per die) | Partial | Medium | Certification + Switching cost | Medium |
| Packaging (OSAT) | Dice wafers; mount and connect die into packages; advanced packaging stacks multiple die | Dicing (blade saw, laser dicing); flip-chip attach (solder bump reflow); wire bonding; underfill dispense and cure; overmold (epoxy); solder ball attach (BGA); advanced packaging: CoWoS (die + HBM on silicon interposer), SoIC (face-to-face bonding), 3D-IC (TSV stacking) | Die (singulated); flip-chip BGA package; CoWoS interposer; HBM stack; substrate (ABF build-up); underfill epoxy; solder mask | Partial | High | Process IP (advanced) / Scale (legacy) | Medium |
| Final Test & Burn-In | Functional and parametric test of packaged devices; thermal stress screening at system-level | ATE (automated test equipment) program execution; functional test vectors; IDDQ leakage test; thermal cycling; burn-in (elevated temperature + voltage); SLT (system-level test) — full system emulation on real silicon | ATE (Advantest V93000, Teradyne UltraFLEX); test socket / handler; burn-in board; JEDEC standard test vectors | No | Low–Medium | Certification | Low–Medium |
| System Integration | Assemble chips + memory + networking into boards, modules, or complete systems | PCB layout and assembly (SMT pick-and-place, reflow); module assembly (GPU board, HBM module); rack integration; firmware flashing; system-level validation | Server PCB; GPU board; NIC; memory DIMM; populated rack unit | No | Low | None (commoditized) | Low |

---

## Publicly-Traded Nodes

| Tier | Ticker | Company | Mkt Cap | In Registry | Notes |
|------|--------|---------|---------|-------------|-------|
| Raw Materials | 4369.T | Shin-Etsu Chemical | Large | Yes | Dominant silicon wafer supplier; also photoresist |
| Raw Materials | 5201.T | AGC Inc. | Large | Yes | Specialty glass, photomask substrates |
| Raw Materials | ICHR | Ichor Holdings | Small | No | Ultrapure gas delivery systems for fabs |
| Raw Materials | ENTG | Entegris | Mid | No | Specialty chemicals, filters, materials for advanced nodes |
| Wafer Production | 4043.T | Sumco Corporation | Large | Yes | #2 silicon wafer supplier globally |
| Wafer Production | SK Hynix | SK Hynix | Large | Yes | Wafer + DRAM/HBM fab (vertically integrated) |
| EDA & Design IP | SNPS | Synopsys | Large | No | #1 EDA; chip design software |
| EDA & Design IP | CDNS | Cadence Design Systems | Large | No | #2 EDA; also simulation/verification |
| EDA & Design IP | ARM | Arm Holdings | Large | No | Dominant CPU/GPU IP licensor; in nearly every chip |
| Lithography Equipment | ASML | ASML Holding | Large | Yes | Sole supplier of EUV; also DUV |
| Deposition & Etch Equipment | LRCX | Lam Research | Large | No | #1 etch and deposition equipment |
| Deposition & Etch Equipment | AMAT | Applied Materials | Large | No | Broadest equipment portfolio; deposition, CMP, implant |
| Inspection & Metrology | KLAC | KLA Corporation | Large | No | #1 inspection/metrology; process control |
| Inspection & Metrology | ONTO | Onto Innovation | Mid | No | Optical metrology; advanced packaging inspection |
| Wafer Fabrication (Foundry) | TSM | Taiwan Semiconductor Mfg. | Large | Yes | #1 foundry; sole manufacturer of leading-edge nodes |
| Wafer Fabrication (Foundry) | GFS | GlobalFoundries | Mid | Yes | Mature nodes; specialty RF, automotive |
| Wafer Fabrication (Foundry) | INTC | Intel Corporation | Large | Yes | IDM + foundry (Intel 18A ramp in progress) |
| Wafer Fabrication (Foundry) | Samsung | Samsung Electronics | Large | Yes | #2 foundry + memory (vertically integrated) |
| Wafer Fabrication (Foundry) | STM | STMicroelectronics | Large | Yes | IDM; SiC power semis, automotive |
| Power Devices | STM | STMicroelectronics | Large | Yes | SiC MOSFET leader; automotive and EV exposure |
| Power Devices | WOLF | Wolfspeed | Mid | No | Pure-play SiC substrate + device; highest SiC revenue exposure |
| Power Devices | ON | ON Semiconductor | Large | No | SiC MOSFET + EV charging; growing SiC share |
| Test (Wafer-Level) | AEHR | Aehr Test Systems | Small | Yes | Near-monopoly on wafer-level burn-in for SiC |
| Packaging (OSAT) | AMKR | Amkor Technology | Mid | Yes | #2 OSAT globally; advanced packaging (TSMC partner) |
| Packaging (OSAT) | ASX | Advanced Semiconductor Engineering | Large | No | #1 OSAT globally (ASE Group) |
| Design (Fabless — Compute) | NVDA | NVIDIA Corporation | Large | Yes | AI GPU monopoly; CUDA ecosystem |
| Design (Fabless — Compute) | AMD | Advanced Micro Devices | Large | Yes | CPU/GPU; MI-series AI accelerators |
| Design (Fabless — Compute) | AVGO | Broadcom | Large | Yes | Custom ASICs + networking silicon |
| Design (Fabless — Compute) | MRVL | Marvell Technology | Large | Yes | Custom ASICs + data infrastructure networking |
| Design (Fabless — Memory) | MU | Micron Technology | Large | Yes | #3 DRAM/NAND; growing HBM share |
| Design (Fabless — Connectivity) | ALAB | Astera Labs | Mid | Yes | PCIe/CXL connectivity for AI infrastructure |
| Design (Fabless — Connectivity) | CRDO | Credo Technology | Small | Yes | High-speed SerDes for AI networking |
| Design (Fabless — Connectivity) | NXPI | NXP Semiconductors | Large | Yes | Automotive + IoT MCUs |
| Design (Fabless — Connectivity) | TXN | Texas Instruments | Large | Yes | Analog + embedded; broad industrial/auto |
| Final Test & Burn-In | COHU | Cohu Inc. | Small | No | Packaged device handlers and testers |
| Final Test & Burn-In | — | *No dominant public pure-play* | — | — | ⚠️ Structural gap — test handled in-house or by Advantest (Japan-listed) |

---

## Structural Gaps

### Gap: Raw Materials — Specialty Photoresists
No US-listed pure-play. JSR Corporation (Japan, taken private 2024) and Shin-Etsu dominate EUV photoresist. EUV photoresist is manufactured by 2–3 companies globally — a genuine hard chokepoint. **Watch for:** Any JSR re-listing, or Shin-Etsu/TOK (Tokyo Ohka Kogyo) ADR issuance.

### Gap: Final Test — Packaged Device
Cohu (COHU) exists but is small and diversified. Advantest (6857.T, Japan-listed) is dominant for AI chip test. Teradyne (TER) straddles wafer and final test. **Watch for:** Teradyne earnings calls — management discusses AI chip test demand explicitly.

### Gap: Power Devices — GaN Pure-Play
Wolfspeed (WOLF) is SiC-focused. No US-listed pure-play GaN-on-SiC HEMT manufacturer at scale. MACOM and Qorvo have GaN exposure but it is a minority of revenue. **Watch for:** GaN power-stage adoption in 800VDC data center rectifiers — would materially expand GaN TAM.

---

## Key Questions to Answer Before Writing the Sector Framework

1. Which foundry tier wins as advanced packaging (CoWoS, HBM stacking) becomes the primary differentiator — TSMC or OSATs?
2. Which equipment tiers are most exposed to export control risk (China revenue concentration)?
3. Is the EDA duopoly (SNPS/CDNS) structurally threatened by any open-source or cloud-native alternative?
4. Where does AI-driven demand create the next capacity constraint after HBM?
5. Which raw material suppliers are most exposed to a Japan/Taiwan geopolitical disruption?
6. When does 800VDC data center adoption drive SiC MOSFET demand to the point it creates a new substrate-level bottleneck?

---

## Interrelationship Anchors

### Inputs (Semiconductors consumes from other sectors)

| From Sector | From Tier | Product / Signal |
|---|---|---|
| Materials & Mining | Silicon Refining | Polysilicon ingot → CZ boule growth; 300mm wafer substrate |
| Materials & Mining | Rare Earth Separation | SiC powder (silicon carbide precursor) → SiC boule growth |
| Materials & Mining | Rare Earth Separation | Gallium, Indium, Arsenic → compound semiconductor epi (InGaAs, GaAs, InP) |
| Electronic Components | Substrates (ABF) | ABF build-up film substrate → flip-chip BGA packaging |
| Photonics & Optical | Laser Sources | EUV light source (CO₂ laser → tin plasma → 13.5nm) → ASML EUV scanner |
| Energy & Power | Grid / Fab Power | Ultra-stable, high-quality AC power → fab operations (power quality deviations >0.1% cause yield loss) |

### Outputs (Semiconductors supplies to other sectors)

| To Sector | To Tier | Product / Signal |
|---|---|---|
| Compute Infrastructure | Server Assembly | GPU, CPU, ASIC, SoC (packaged die) → compute node PCB |
| Compute Infrastructure | Networking | SerDes PHY / PCIe / CXL chip → NIC, switch ASIC |
| Electronic Components | PCB Assembly | Packaged ICs → board-mount population |
| Energy & Power | Power Conversion | SiC MOSFET / GaN HEMT → inverter modules, HVDC rectifiers, UPS H-bridges |
| Photonics & Optical | Transceiver Mfg | Photonic IC, VCSEL, EML chip → optical transceiver module |
| Robotics & Edge AI | Inference Layer | Edge AI SoC, MCU → robot compute platform |

---

## Research Log
- **2026-05-24** — Initial map-sector run. 11 tiers mapped, 6 chokepoints (Y or Partial), 2 structural gaps flagged. Registered: NVDA, MU, MRVL, AEHR, ALAB, CRDO, AMKR, TSM, GFS, INTC, Samsung, STM, ASML, 4043.T, 4369.T, 5201.T. Candidates not yet registered: SNPS, CDNS, ARM, LRCX, AMAT, KLAC, ENTG, ICHR, ONTO, ASX, COHU, NXPI (registry check needed).
- **2026-05-24** — Rebuilt with process/product depth. Added Processes and Key Products columns. Added Power Devices as explicit tier (previously folded into Wafer Fabrication). Added Interrelationship Anchors section. New candidates surfaced: WOLF, ON (SiC power devices). Status updated to `partial` in Dimension Map (nodes not yet re-registered with layer tags).

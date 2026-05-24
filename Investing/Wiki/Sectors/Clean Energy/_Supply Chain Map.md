# Energy & Power — Supply Chain Map
*Mapped: 2026-05-24 | Anchor: firm 24/7 clean power delivered to AI data center*
*Dimension: D3 — AI Infrastructure*
*Folder slug: `Clean Energy`*

---

## Framework Status
- [x] Supply chain mapped
- [x] Process/product depth added (2026-05-24)
- [x] Interrelationship Anchors documented (2026-05-24)
- [ ] Nodes registered (`/add-ticker TICKER --layer "Layer"` for each below)
- [ ] Ground truth pulled (`/stock-research TICKER` per node)
- [ ] Customer matrix built (`/build-customer-matrix "Energy & Power"`)
- [ ] Sector Framework written (only after above steps complete)

---

## Value Chain

| Tier | Function | Processes | Key Products / Materials | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|-----------|--------------------------|------------|-------------------|-----------|----------------|
| Primary Power Generation | Convert a primary energy source (nuclear fission, combustion, photovoltaics, wind) into three-phase AC electricity at transmission voltage | Nuclear: uranium fuel pellet loading → controlled fission chain reaction → steam cycle (Rankine, 290°C/7MPa) → turbine-generator → 20kV step-up; CCGT: natural gas → gas turbine (Brayton) + heat recovery steam generator (HRSG) → steam turbine (combined ~62% efficiency); Solar PV: photon absorption in silicon/perovskite cell → minority carrier generation → DC current collection → string to array wiring; Wind: aerodynamic lift on blade → rotor torque → DFIG or PMSG generator → low-frequency AC; Nuclear fuel cycle: UF6 enrichment → UO2 pellet sintering → zircaloy cladding → fuel assembly loading | PWR / BWR reactor (1,000–1,600 MWe); CCGT plant (400–600 MWe, GE 7F/9F or Siemens SGT5); utility-scale solar PV array (200–500 MWac, bifacial TOPCon module); onshore wind turbine (4–6 MW per unit, 130–160m rotor); offshore wind turbine (12–18 MW); uranium fuel assembly (17×17 array, 264 fuel rods, 4.5% enriched UO2) | No | Very High | Geographic monopoly (plant siting) + Scale + Certification (nuclear: NRC license = 10-year process) | Cyclical (regulated utilities), High (merchant generators in tight markets) |
| High-Voltage Transmission & Grid Infrastructure | Transform, transmit, and switch electrical power at EHV/HV levels (66kV–800kV) from generation source to load center | Transformer design: core-form construction (GOES lamination stacking + vacuum-pressure impregnation in mineral oil), nameplate MVA rating, OLTC (on-load tap changer) integration; HVDC converter station: VSC (voltage source converter) or LCC (line commutated converter) topology, valve hall assembly (IGBT press packs, 3.3kV–6.5kV rating), smoothing reactor, harmonic filter; EHV line construction: tower erection (lattice steel, guyed / self-supporting), conductor stringing (ACSR, HTLS, ACCC), insulator strings (glass disc or polymer), sag-tension calculation; GIS (gas-insulated switchgear): SF6 pressure assembly, bus bar, disconnector, CT/VT; substation commissioning: protection relay coordination (overcurrent, distance, differential), SCADA integration | EHV transformer (800kV, 1,000 MVA; GOES core; mineral oil; OLTC); HVDC VSC converter station (±800kV, 2,000 MW, press-pack IGBT valves); GIS switchgear (245kV, SF6, bay extension module); HTLS conductor (ACCC Cardinal, 795 kcmil, 150°C sag limit); underground cable (230kV XLPE, for submarine or urban routing); protection relay (SEL-421 distance relay, IEC 61850) | Yes | Very High | Scale + Certification + Geographic monopoly (easement and transmission rights are permanent assets) | Medium (regulated RAB return) |
| Grid-Scale Energy Storage (BESS) | Store bulk electrical energy in electrochemical form and discharge on demand to provide capacity, frequency response, and arbitrage | Battery pack design: LFP or NMC cylindrical/prismatic/pouch cell → module assembly (series-parallel string, 48V or 100V nominal) → battery rack (50–150 kWh); BMS design: cell voltage monitoring (ΔV < 5mV), SOC/SOH algorithm (Kalman filter), thermal runaway detection, passive/active balancing; PCS (power conversion system): three-phase bidirectional inverter (SiC MOSFET H-bridge, 1.5MVA–4MVA), grid-forming or grid-following control, reactive power injection; AC/DC integration: LV switchgear, DC fusing and contactors, transformer (LV→MV); BESS system integration: thermal management (liquid plate cooling), fire suppression (aerosol / water mist), outdoor enclosure; grid interconnection: utility protection study, SAT (site acceptance test), SCADA / EMS integration | LFP battery cell (280Ah prismatic, 3.2V, ≥6,000 cycles at 80% DOD); BESS containerized unit (2–4 MWh per 20-ft container); PCS inverter module (1.5 MVA, 99% round-trip AC efficiency); battery management system (BMS) hardware + SOC software; liquid thermal management plate (aluminum, glycol coolant); fire suppression enclosure (NOVEC 1230 or aerosol) | No | High | Scale + Software (BMS + energy management software are the differentiated layer; hardware is commoditizing rapidly) | Medium (project-dependent; merchant BESS economics are volatile) |
| Power Electronics & Conversion | Convert electrical power between AC and DC and across voltage levels at high efficiency using semiconductor switching devices | Inverter design: SiC MOSFET gate drive (isolated gate driver, 15V/-5V, 100ns td); three-phase two-level or three-level NPC topology; EMI filter design (common mode choke + X/Y capacitors); DSP/FPGA control (field-oriented control, DQ-frame current loop, PLLfor grid sync); motor drive: FOC (field-oriented control) of PMSM/IM, space-vector PWM at 4–16 kHz, dynamic braking resistor; DC-DC converter: LLC resonant (ZVS at full load, 94–98% efficiency), DAB (dual-active bridge for bidirectional), interleaved boost; rectifier: Vienna rectifier (PFC, 800VDC output, SiC MOSFET), diode bridge + active front-end; transformer design: planar transformer (PCB winding for LLC), nanocrystalline core (for high-frequency isolation) | SiC MOSFET module (1,200V, 450A, TO-247 or half-bridge power module); solar inverter (1.5 MVA, string or central); wind converter (full-power PMSG converter, 6MW); traction inverter (400A / 800V SiC, automotive class); data center HVDC rectifier (50kW–250kW, AC→800VDC, Vienna topology); industrial motor drive (22kW–1MW, IP55); LLC resonant DC-DC (48V→12V→1V server VR) | Yes | Medium–High | Process IP + Certification (SiC power module reliability qualification; IEC 62477 / UL 508C; automotive AEC-Q101 for SiC MOSFET) | Medium–High |
| Fuel Cell & Distributed Clean Generation | Generate electricity from an electrochemical reaction (H2 + O2 or reformed natural gas) at the point of use, with high efficiency and low/zero emissions | SOFC (solid oxide fuel cell): zirconia (YSZ) electrolyte tape casting → NiO/YSZ anode sintering → LSC cathode screen printing → cell stack assembly → internal reforming of NG (CH4 + H2O → CO + 3H2 at 700–900°C) → electrochemical oxidation → 50–60% electrical efficiency; PEMFC: Nafion membrane + Pt catalyst (ionomer + carbon black + PTFE binder) → MEA hot press → bipolar plate (graphite or SS316) → stack compression; electrolyzer: alkaline (KOH solution, Ni electrodes) or PEM (Nafion membrane, IrO2 anode, Pt cathode) → H2 production at 50–80 kWh/kgH2; microturbine: recuperated Brayton cycle, single-stage centrifugal compressor/turbine, air-bearing, 30–35% efficiency (60% in CHP mode) | Bloom Energy Box (250kW SOFC, NG-fed, 60% LHV efficiency); PEMFC stack (100kW automotive module); PEM electrolyzer (1–5 MW, 4.5 kWh/Nm³ H2); alkaline electrolyzer (10–100 MW, 4.2 kWh/Nm³ H2); liquid hydrogen storage tank (cryo-compressed, 700 bar); MEA (membrane electrode assembly, Pt loading 0.1–0.4 mg/cm²) | No | High | Process IP + Certification (SOFC requires 40,000-hour stack life qualification for utility acceptance) | High (if operating as baseload); Low (if capacity factor <70%) |
| Advanced Nuclear — SMR & Microreactor | Design, license, manufacture, and operate small modular reactors (SMR) and microreactors that provide firm, dispatchable, carbon-free power at 1–500 MWe scale | SMR design: passive safety systems (gravity-fed cooling, natural circulation — no active pumps required for safe shutdown); integral design (reactor vessel contains primary loop); module factory manufacturing (prefabricated reactor module, rail-shippable <350t); regulatory licensing (NRC Design Certification per 10 CFR Part 52; Preliminary Safety Analysis Report; design-basis accident analysis); site preparation: compact footprint (1–5 acres per module vs. 400 acres for conventional nuclear); HALEU fuel: 19.75% enriched UO2 or UN — required for fast-spectrum and most microreactors; microreactor thermal spectrum: heat pipe cooled (Na or K heat pipe) + Stirling engine or Brayton cycle generator | NuScale VOYGR-6 SMR module (77 MWe per module, PWR, integral design); Oklo Aurora (1.5 MWe, fast spectrum, metal fuel, heat-pipe cooled); X-energy Xe-100 (80 MWt HTGR pebble-bed module, 320 MWe 4-pack); TerraPower Natrium (345 MWe, Na-cooled fast, molten salt thermal storage); HALEU fuel (UN or UO2, 19.75% U-235); heat pipe module (Mo alloy, Na working fluid) | Partial | Very High | Certification + Process IP (NRC Design Certification is 7–12 year process; first mover gets a structural licensing lead) | Very High (if operating), N/A (if development) |
| Grid Software & Energy Management | Plan, dispatch, monitor, and optimize the flow of electricity across generation assets, transmission networks, and end-use loads using software and communications infrastructure | EMS (energy management system): state estimation (AC power flow, Ybus matrix), economic dispatch (SCUC/SCED LP/MILP optimization), contingency analysis (N-1, N-2); SCADA: RTU / IED polling (DNP3, IEC 60870-5-104, Modbus), historian (OSIsoft PI), alarm management; DERMS (distributed energy resource management system): DER aggregation (VPP), OpenADR demand response, IEEE 2030.5 smart inverter control, CIM data model; market software: bid submission (FERC Order 2222), settlement, real-time LMP forecasting; grid stability: PMU (phasor measurement unit) data stream → synchrophasor-based WAMPAC (wide-area monitoring, protection, and control); cybersecurity: NERC CIP compliance (critical infrastructure protection), OT/IT segmentation, incident response | EMS software platform (GE PSCAD / OSIsoft PI / Siemens Spectrum Power 7); RTU (GE D400, SEL-3530); PMU (SEL-421, Arbiter 1133A); DERMS platform (AutoGrid FLEX, Opus One GridOS); VPP control software (Fluence IQ, Tesla Autobidder); smart meter (ANSI C12.22, 15-min interval AMI); SCADA historian (OSIsoft PI, 1M tag capacity per server) | No | Low–Medium | Ecosystem + Switching cost (SCADA data model and historian integration lock-in; utility replacement cycles are 10–15 years) | High |

---

## Publicly-Traded Nodes

| Tier | Ticker | Company | Mkt Cap | In Registry | Notes |
|------|--------|---------|---------|-------------|-------|
| Primary Power Generation | VST | Vistra Energy | Large | No | Largest competitive power generator in US; nuclear (Comanche Peak, Braidwood) + CCGT; Texas merchant market |
| Primary Power Generation | GEV | GE Vernova | Large | No | Gas turbine (GE 7F.05, HA-class); onshore + offshore wind (Haliade-X); grid solutions |
| Primary Power Generation | CEG | Constellation Energy | Large | No | Largest US nuclear operator (21 GW); Microsoft + Amazon nuclear PPA winner |
| Primary Power Generation | NEE | NextEra Energy | Large | No | #1 US wind + solar; FPL nuclear fleet; NEER renewables arm; FID machine |
| Primary Power Generation | 7011.T | Mitsubishi Heavy Industries | Large | No | Japan-listed; gas turbines (M501G/JAC class); nuclear plant services |
| High-Voltage Transmission | GEV | GE Vernova | Large | No | Grid Solutions: HV transformers, HVDC converter stations, GIS switchgear |
| High-Voltage Transmission | ENR.DE | Siemens Energy | Large | No | Germany-listed; HV transformers (wait lists 2–4 years), HVDC BlueTec, switchgear |
| High-Voltage Transmission | — | *Hitachi Energy (Hitachi 6501.T)* | Large | No | ⚠️ Embedded in Hitachi; HVDC (HVDC Classic/Light), HV transformer, protection |
| High-Voltage Transmission | — | *ABB (ABBN.SW)* | Large | No | ⚠️ Switzerland-listed; HVDC, transformers, LV/MV switchgear; broad industrial |
| Grid-Scale Storage | FLNC | Fluence Energy | Mid | No | BESS system integrator (Siemens + AES JV); Gridstack product; IQ software |
| Grid-Scale Storage | — | *Tesla Megapack* | — | No | ⚠️ Embedded in TSLA; Megapack 2XL (3.9 MWh); LFP chemistry; fastest deployments |
| Grid-Scale Storage | — | *BYD (002594.SZ)* | Large | No | ⚠️ China-listed; largest global LFP BESS supplier; BYD Blade cell |
| Power Electronics & Conversion | GEV | GE Vernova | Large | No | Wind power converters + grid-forming inverters |
| Power Electronics & Conversion | — | *Siemens Energy ENR.DE* | Large | No | Industrial drives, traction inverters, rectifiers |
| Power Electronics & Conversion | — | *ABB* | Large | No | ACS880/890 industrial drive; LV/MV drives for HVAC, data center chiller |
| Power Electronics & Conversion | VRT | Vertiv Holdings | Large | Yes | 800VDC HVDC rectifier modules for data centers; power conversion integrated with cooling |
| Fuel Cell & Distributed Generation | BE | Bloom Energy | Mid | No | SOFC (solid oxide fuel cell); NG + H2 compatible; data center deployments |
| Fuel Cell & Distributed Generation | PLUG | Plug Power | Mid | No | PEMFC + PEM electrolyzer + liquid H2; material handling + stationary |
| Fuel Cell & Distributed Generation | FCEL | FuelCell Energy | Small | No | MCFC (molten carbonate) megawatt-scale combined heat and power |
| Fuel Cell & Distributed Generation | BLDP | Ballard Power | Small | No | PEMFC for transit and marine; H2 fuel cell stacks |
| Advanced Nuclear — SMR | OKLO | Oklo Inc. | Mid | Yes | Aurora microreactor (1.5 MWe, fast spectrum, heat-pipe cooled, metal fuel) |
| Advanced Nuclear — SMR | TE | T1 Energy Inc. | Small | Yes | Nuclear construction and services |
| Advanced Nuclear — SMR | LEU | Centrus Energy | Small | No | Only US HALEU enrichment capability (Piketon, OH cascade); critical SMR fuel supplier |
| Advanced Nuclear — SMR | SMR | NuScale Power | Small | No | VOYGR PWR SMR; Design Certification approved by NRC (first SMR); commercial challenges |
| Grid Software & Energy Management | — | *AutoGrid (Schneider subsidiary)* | — | No | ⚠️ Private (acquired by Schneider); DERMS / VPP software |
| Grid Software & Energy Management | ITRI | Itron Inc. | Mid | No | AMI smart meters + grid edge software; DERMS-adjacent |
| Grid Software & Energy Management | GDYN | Grid Dynamics Holdings | Small | No | Grid software and digital transformation; smaller pure-play |

---

## Structural Gaps

### Gap: HALEU Fuel Supply Chain
HALEU (High-Assay Low-Enriched Uranium, 5–19.75% U-235) is required for virtually all advanced reactor designs (NuScale uses standard LEU at 4.95%, but TerraPower Natrium, X-energy Xe-100, Oklo Aurora, and microreactors need HALEU). Centrus Energy (LEU) is the only US company with an NRC license to enrich HALEU, and it has a single demonstration cascade of 16 centrifuges at Piketon, OH. Urenco and Orano (European, government-linked) are the other enrichment players. There is no commercial-scale HALEU supply chain — this is the most critical structural gap for the SMR sector. **Watch for:** DOE HALEU enrichment contract awards; Centrus cascade expansion authorization; Urenco US HALEU license application.

### Gap: Large Power Transformer (LPT) Manufacturing Capacity
Large power transformers (LPT, 500kV+, >100 MVA) have an 18–36 month delivery lead time globally, and the US has essentially zero domestic manufacturing for the largest units. The primary suppliers are Hitachi Energy, Siemens Energy, ABB, and several Chinese manufacturers. Siemens Energy is running 2–4 year wait lists. The data center buildout + grid hardening demand is worsening this bottleneck. No US-listed pure-play exists. **Watch for:** Any announcement of domestic LPT manufacturing capacity investment; CPower (private) or grid infrastructure fund formation; GE Vernova Grid Solutions backlog disclosures.

### Gap: Long-Duration Energy Storage (>8 hours)
Li-ion BESS economics break down at 4–8 hours of storage duration. Beyond that, the technology options (iron-air: Form Energy; flow battery: ESS Inc.; liquid air: Highview Power; gravity: Energy Vault) are all either private or struggling with commercialization. This gap is critical for firming renewables at the scale data centers require. ESS Inc. (GEN) is listed but sub-$100M market cap. Form Energy is private (backed by ArcelorMittal). **Watch for:** Form Energy or Highview Power going public; any utility-scale LDES contract award >100 MWh at 12+ hours.

### Gap: Next-Generation Nuclear Fuel Fabrication
Converting HALEU feedstock into finished fuel assemblies (for advanced reactors) requires a new fabrication ecosystem. Framatome, Westinghouse, and Global Nuclear Fuel have conventional LEU fuel fabrication — none are qualified for the diverse fuel forms advanced reactors require (metallic uranium-molybdenum for Oklo, TRISO pebbles for X-energy). No publicly-listed company is a pure-play HALEU fuel fabricator. **Watch for:** NRC advanced fuel fabrication facility licensing; DOE critical minerals + fuel processing grants.

---

## Key Questions to Answer Before Writing the Sector Framework

1. Is the nuclear PPA model (Microsoft/Amazon paying cost-plus-return for dedicated nuclear capacity) scalable enough to finance the 50–100 new SMR units needed for AI hyperscaler power demand by 2035 — or is the permitting and supply chain timeline simply incompatible with the AI capex cycle?
2. Does 800VDC HVDC architecture at the data center create a durable structural shift in power electronics demand (SiC MOSFET → rectifier → on-site distribution) — or is it an optimization that gets absorbed by incumbent UPS and PDU vendors without creating new market share?
3. Is grid-scale BESS a commodity market (hardware price-driven, no moat) or a software-differentiated market (Fluence IQ, Tesla Autobidder, Stem)? What is the revenue durability of the software overlay versus the hardware BOM?
4. What is the realistic timeline from SMR Design Certification to first power (Oklo: 2027? NuScale: 2030+?), and does the hyperscaler power demand timeline create enough offtake urgency to pull SMR construction forward?
5. Is the LPT (large power transformer) bottleneck a genuine multi-year supply constraint that benefits GE Vernova and Siemens Energy grid businesses — or will lead times compress as new capacity enters the market?
6. Does distributed fuel cell generation (Bloom Energy SOFC) represent a credible bridge power solution for data centers while nuclear scales, or is the economics only favorable in specific utility rate structures (California, Northeast)?

---

## Interrelationship Anchors

### Inputs (this sector consumes from)

| From Sector | From Tier | Product / Signal |
|---|---|---|
| Materials & Mining | Battery Material Precursor | Lithium hydroxide (LiOH·H2O) + CoSO4 + NiSO4 → NMC/LFP cathode active material → BESS cell |
| Materials & Mining | Copper Mining & Refining | High-purity copper rod → transformer winding, overhead transmission conductor, underground cable, generator winding |
| Materials & Mining | Rare Earth Separation | Neodymium / Praseodymium → NdFeB permanent magnet → PMSG (permanent magnet synchronous generator) in direct-drive wind turbine |
| Materials & Mining | Silicon & SiC Precursor | SiC substrate → SiC MOSFET wafer → power inverter switching device |
| Semiconductors | Power Devices | SiC MOSFET (1,200V, 40mΩ Rdson) → three-phase inverter bridge → solar / wind / BESS converter |
| Semiconductors | Power Devices | GaN HEMT (650V, GaN-on-Si) → LLC resonant DC-DC converter → server VR at high switching frequency |
| Electronic Components | Film & Electrolytic Cap Mfg | 900V–1,200V polypropylene film capacitor → HVDC rectifier DC bus filter, wind/solar inverter DC link |
| Electronic Components | Inductor & Transformer Mfg | Nanocrystalline / ferrite core planar transformer → LLC resonant power stage isolation |
| Compute Infrastructure | Demand Signal | Hyperscaler power purchase agreements (PPAs) + data center electricity demand forecast → generation investment FID signal |

### Outputs (this sector supplies to)

| To Sector | To Tier | Product / Signal |
|---|---|---|
| Compute Infrastructure | Power Distribution | 800VDC HVDC bus (AC→800VDC rectified) → server-embedded DC-DC converter stage |
| Compute Infrastructure | Power Distribution | Grid-connected substation (33kV → 480V) → data center main switchboard |
| Compute Infrastructure | Power Distribution | BESS / HVDC UPS (battery-backed, no AC swing) → uninterruptible power feed for GPU cluster |
| Compute Infrastructure | Thermal Management | Chilled water supply (from district chiller or on-site plant) → CRAC / CDU cooling loop |
| Semiconductors | Power Devices | Grid-scale demand signal → SiC MOSFET capacity pull (inverter + rectifier design-win drives WOLF/STMicro orders) |
| Robotics & Edge AI | Actuators & Motors | Motor drive (variable-frequency drive, SiC-based) → servo motor torque control in robot joint |
| Space & Communications | Satellite Ground | BESS + diesel hybrid microgrid → off-grid / remote ground station power |
| Photonics & Optical | MOCVD Fab | Clean power supply → MOCVD reactor stable temperature (process-critical; MOCVD rejects batch on voltage sag) |

---

## Research Log
- **2026-05-24** — Initial map-sector run. 7 tiers, 2 chokepoints (Y / Partial): High-Voltage Transmission (Y — LPT lead times, HVDC concentration), Advanced Nuclear SMR (Partial — licensing moat but no commercial scale yet). 4 structural gaps: HALEU fuel supply chain, LPT manufacturing capacity, long-duration storage (>8 hours), advanced fuel fabrication. Registered in Clean Energy: OKLO, TE. Files exist but not registered: BE, FLNC, GEV, VST, 7011.T, ENR.DE. New candidates not in registry: CEG, NEE, LEU, SMR, PLUG, FCEL, BLDP, ITRI.

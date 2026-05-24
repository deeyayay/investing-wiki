# Photonics & Optical — Supply Chain Map
*Mapped: 2026-05-24 | Anchor: optical transceiver enabling AI cluster interconnect*
*Dimension: D2 — AI Connectivity*

---

## Framework Status
- [x] Supply chain mapped
- [x] Process/product depth added (2026-05-24)
- [x] Interrelationship Anchors documented (2026-05-24)
- [ ] Nodes registered (`/add-ticker TICKER --layer "Layer"` for each below)
- [ ] Ground truth pulled (`/stock-research TICKER` per node)
- [ ] Customer matrix built (`/build-customer-matrix "Photonics & Optical"`)
- [ ] Sector Framework written (only after above steps complete)

---

## Value Chain

| Tier | Function | Processes | Key Products / Materials | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|-----------|--------------------------|------------|-------------------|-----------|----------------|
| III-V Substrate & Epitaxial Wafer Growth | Grow the compound semiconductor wafers that laser diodes, VCSELs, photodetectors, and GaN power devices are fabricated on | InP substrate growth (LEC or VGF crystal pulling from InP polycrystal); GaAs substrate growth (VGF or LEC from GaAs melt); MOCVD epitaxial growth (trimethyl-Ga/In/Al + AsH3/PH3 precursors at 600–750°C → lattice-matched quantum well and barrier layers to Å-level control); substrate polishing (CMP to Ra <0.3 nm); wafer characterization (XRD rocking curve, PL mapping, SIMS) | InP wafer (50mm, 75mm, 100mm; Fe-doped or S-doped); GaAs wafer (100mm, 150mm; semi-insulating or n+); Ge wafer (for multi-junction solar / CPV); GaSb wafer (for mid-IR detectors); MOCVD epitaxial wafer (InGaAsP MQW for 1310/1550nm laser; InGaAs absorber for photodetector; AlGaAs/GaAs for VCSEL) | Yes | High | Process IP + Geographic concentration (InP: AXT/Wafer Technology/Sumitomo Electric — 3 suppliers; MOCVD epi: IQE dominant in foundry model) | High |
| Photonic Device Fabrication | Pattern, implant, metallize, and cleave epitaxial wafers to produce individual photonic chips — laser diodes, EMLs, VCSELs, photodetectors — at wafer scale | Photolithography (contact or stepper, 1–5µm features); wet chemical etch (InGaAsP mesa definition, H3PO4:H2O2:H2O); dry etch (RIE/ICP for vertical facets and ridge waveguides); SiNx passivation (PECVD); Ti/Pt/Au p-contact metallization (e-beam evaporation); Ge/Au/Ni/Au n-contact; proton implantation (VCSEL current confinement); HR/AR facet coating (PECVD SiNx/SiO2 stack); wafer-level test (LIV curve, wavelength at operating current); die singulation (scribe and cleave or dicing saw) | Fabry-Perot laser diode (1310nm, 1550nm, 850nm); DFB laser (1310nm, 1550nm, 100kHz linewidth); EML (electroabsorption-modulated laser, 25G–100G); VCSEL (850nm, 940nm, 1310nm; 25G–100G direct modulation); InGaAs PIN photodetector; avalanche photodiode (APD); semiconductor optical amplifier (SOA) | Yes | High | Process IP + Scale (full wafer-level photonic fab has high defectivity challenges; few players can produce volume with yield) | High |
| Silicon Photonics Platform | Integrate optical functions — waveguides, ring modulators, Mach-Zehnder modulators, Ge photodetectors — onto silicon wafers using CMOS-compatible processes to enable chiplet-level optical I/O | Silicon waveguide patterning (DUV lithography at 193nm on SOI wafer, 220nm Si layer); SiO2 cladding deposition (PECVD); grating coupler or edge coupler formation (e-beam or DUV litho); Mach-Zehnder modulator: p-n junction implant + heater waveguide (TiN); Ge photodetector: selective epitaxial growth of Ge in trench (700°C CVD); ring modulator: thermal tuning (microheater); fiber attach (V-groove passive alignment or active align + epoxy); WDM multiplexer (AWG on-chip) | SiPh interposer / photonic IC; SOI (silicon-on-insulator) wafer (220nm Si device layer, 2µm buried oxide); Ge-on-Si photodetector; SiN waveguide (for wide-band, low-loss applications); co-packaged optic (CPO) chiplet (e.g., 3.2T optical I/O in TSMC N45SiPh) | Partial | High | Ecosystem (SiPh PDKs are foundry-specific; design tools, IP, and fab qualification are tightly coupled — switching foundry is multi-year) | High |
| Optical Fiber & Preform Manufacturing | Produce the glass preforms and draw the optical fibers that carry photons between chips, racks, data centers, and continents | Preform: OVD (outside vapor deposition, SiCl4 flame hydrolysis → soot blank → consolidation in dry atmosphere); MCVD/PCVD (inside CVD, SiCl4 + GeCl4 in rotating tube → graded-index core); VAD (vapor axial deposition, Japanese standard); preform consolidation (dehydration in Cl2/He, sintering at 1500°C); fiber draw (2000°C graphite furnace, 10–30 m/s draw speed → 125µm glass fiber); UV acrylate coating (dual-layer, 245µm OD); spooling; screening (proof test, attenuation OTDR at 1310/1550nm); ribbon cabling | Standard single-mode fiber (SMF-28, ITU-T G.652D, <0.2 dB/km at 1550nm); ultra-low-loss fiber (ULL, <0.17 dB/km); multi-mode fiber (OM3/OM4/OM5, for 850nm VCSEL links); polarization-maintaining fiber (PM fiber, PANDA or bow-tie); large-mode-area (LMA) fiber (for fiber laser pump/signal); fiber ribbon (12F, 24F for MPO trunk) | Partial | Very High | Scale + Process IP (Corning and Prysmian/Furukawa-OFS control OVD and large-scale draw; new entrant capex >$500M for meaningful capacity) | Medium–High |
| Passive Optical Components | Filter, route, split, combine, and condition light at the wavelength or polarization level without active gain or modulation | Thin-film filter deposition (ion-assisted evaporation or magnetron sputtering of SiO2/TiO2/Ta2O5 stacks, <1nm layer control); AWG (arrayed waveguide grating): photolithography on silica PLC substrate; WSS (wavelength selective switch): MEMS mirror array + diffraction grating, or LCoS (liquid crystal on silicon) + grating; optical isolator assembly (YIG Faraday rotator + permanent magnet + polarizer wafer dicing); fiber Bragg grating (UV writing in Ge-doped fiber); polarization beam splitter (PBS) cube cementation; MUX/DEMUX (TFF or AWG based) | Thin-film bandpass filter (DWDM channel filter, 100GHz/50GHz ITU grid); AWG MUX/DEMUX (16ch, 40ch, 80ch); MEMS-based WSS (1×9, 1×20); LCoS WSS; optical isolator (single-stage 30dB isolation, dual-stage 60dB); polarization-maintaining beam splitter; fiber Bragg grating (FBG) for gain flattening | No | Medium | Process IP + Certification | Medium–High |
| Transceiver & Module Integration | Co-package laser, photodetector, driver IC, TIA, and DSP into pluggable optical modules that translate electrical signals to optical and back at data-center-relevant speeds | Die attach (flip-chip or wire bond of laser/PD die to submount); lens coupling (ball lens or GRIN lens alignment, UV-curable epoxy); TEC (thermoelectric cooler) assembly for temperature-stable DFB lasers; DSP ASIC placement (COHR / Marvell / InPhi DSP on PCB); RF connectorization; Fabrinet or similar CM assembly (pick-and-place, reflow, underfill); active alignment (6-axis laser-PD coupling to <0.5 dB insertion loss target); burn-in and test (TX power, extinction ratio, RX sensitivity, BER at rated temp range); MSA form-factor compliance (SFP28, QSFP56, QSFP-DD, OSFP, 800G, 1.6T) | 400G DR4 / FR4 QSFP-DD module; 800G OSFP module; 1.6T QSFP-DD800 module; coherent CFP2-DCO / QSFP-DCO (400G ZR/ZR+); oCAPI / CPO (co-packaged optics chiplet, not pluggable); SFP28 25G transceiver; AOC (active optical cable) | Partial | Medium | Scale + Customer lock-in (platform qualification cycles of 12–18 months create switching costs; hyperscaler approved vendor lists are small) | Medium–High |
| Coherent Line Systems & ROADM | Transmit, amplify, switch, and manage terabit-class optical signals over metro and long-haul fiber routes connecting data centers and backbone nodes | WaveLogic / DSP coherent modem design (ASIC: 400G ZR / 400G-OpenZR+ / 800G; QAM order: QPSK, 8QAM, 16QAM, 64QAM adaptive); coherent transceiver integration (narrow-linewidth tunable laser + IQ modulator + coherent receiver); EDFA (erbium-doped fiber amplifier) design and pump laser integration (976nm pump LD); Raman amplification (co-propagating / counter-propagating 1455nm pump); ROADM design (CDC-F: colorless, directionless, contentionless, flexible-grid); network management system (NMS) software; link engineering (OSNR budget, chromatic dispersion pre-compensation) | WaveLogic 5e / WaveLogic 6 coherent DSP chip; 400G/800G coherent transceiver line card; EDFA module (C-band, L-band, 20–30 dBm output); optical amplifier shelf; ROADM chassis (degree-4 to degree-20); transport management plane (YANG model, OpenConfig); FlexGrid spectrum allocation (12.5 GHz slot width) | Partial | High | Ecosystem + Switching cost (network orchestration software, NMS, and multi-year support contracts; Ciena and Nokia control the key coherent DSP ASIC design) | High |
| Photonic Sensing & LIDAR | Produce optically-based sensors and ranging systems for robotics, autonomous systems, industrial measurement, and environmental monitoring | Mechanical or solid-state LIDAR: VCSEL / fiber-coupled pulsed laser (905nm or 1550nm) + APD array (direct ToF) or FMCW (coherent detection, swept CW laser); beam steering: rotating mirror (mechanical), MEMS mirror array, OPA (optical phased array, SiPh-based), flash LIDAR (2D APD array, no scanning); range gate electronics (SPAD array readout, TDC); point cloud processing (FPGA/ASIC); optical coherence tomography (OCT): swept-source OCT laser + interferometer + balanced PD for medical / industrial scan; FMCW radar: VCO + photonic mixer for 77/300 GHz | Solid-state LIDAR module (32-, 64-, 128-line; 10 Hz frame rate; 200m range at 10% reflectivity); FMCW LIDAR chip (SiPh-based, no moving parts); 1D/2D SPAD array; OPA (optical phased array chip, SiPh); swept-source OCT engine; InGaAs APD array (1550nm, eye-safe); fiber-optic gyroscope (FOG) | Partial | Medium | Process IP + Certification (automotive LIDAR requires IATF 16949 / ISO 26262 ASIL-B qualification) | High |

---

## Publicly-Traded Nodes

| Tier | Ticker | Company | Mkt Cap | In Registry | Notes |
|------|--------|---------|---------|-------------|-------|
| III-V Substrate & Epitaxial Wafer Growth | AXTI | AXT Inc. | Small | Yes | InP, GaAs, Ge substrates; Mountain Pass-adjacent for Ga/In feedstock |
| III-V Substrate & Epitaxial Wafer Growth | IQE | IQE plc | Small | No | UK-listed (AIM: IQE); MOCVD epi foundry; VCSEL and GaN epi |
| III-V Substrate & Epitaxial Wafer Growth | SIVE | Sivers Semiconductors | Small | Yes | Stockholm-listed; GaAs/GaN device fab; 5G and photonics |
| Photonic Device Fabrication | COHR | Coherent Corp | Large | Yes | Laser diodes, VCSELs, EMLs, InP photonic ICs; largest US photonic device fab |
| Photonic Device Fabrication | LITE | Lumentum Holdings | Large | Yes | VCSEL (LiDAR + 3D sensing), DFB lasers, ROADMs; strong cloud customer base |
| Photonic Device Fabrication | AAOI | Applied Optoelectronics | Small | Yes | DFB laser, VCSEL; data center and cable TV transceiver market |
| Photonic Device Fabrication | LASR | nLIGHT Inc. | Small | Yes | High-power fiber-coupled semiconductor and fiber lasers; defense + industrial |
| Photonic Device Fabrication | MTSI | MACOM Technology Solutions | Mid | No | GaAs/InP/GaN chip fab; drivers, TIAs, photonic ICs; strong DC transceiver exposure |
| Silicon Photonics Platform | — | *TSMC N45SiPh / GlobalFoundries* | — | No | ⚠️ SiPh foundry services — embedded in diversified foundries; not investable as pure-play |
| Silicon Photonics Platform | POET | POET Technologies | Small | Yes | POET Optical Interposer platform (SiPh + III-V heterogeneous integration); pre-revenue |
| Silicon Photonics Platform | LWLG | Lightwave Logic | Small | Yes | Electro-optic polymer Mach-Zehnder modulator; pre-revenue R&D stage |
| Optical Fiber & Preform Manufacturing | GLW | Corning Incorporated | Large | No | ~50% global optical fiber market; OVD preform process; InfiniCor / SMF-28 Ultra |
| Optical Fiber & Preform Manufacturing | FOCI | FOCI Fiber Optic Communications | Small | Yes | Taiwan-listed (TPEX); specialty fiber cables and assemblies |
| Passive Optical Components | VIAV | Viavi Solutions | Mid | Yes | Thin-film filter coatings, fiber test (OTDR), network & service enablement |
| Passive Optical Components | COHR | Coherent Corp | Large | Yes | Also produces optical isolators, beam combiners, and passive WDM components |
| Passive Optical Components | — | *Browave Corporation* | Small | No | Taiwan-listed; WSS and ROADM passive optical components — in wiki as Browave.md |
| Transceiver & Module Integration | COHR | Coherent Corp | Large | Yes | 400G/800G/1.6T QSFP-DD/OSFP transceivers; coherent CFP2-DCO |
| Transceiver & Module Integration | LITE | Lumentum Holdings | Large | Yes | Pluggable transceivers; coherent and PAM4 portfolio |
| Transceiver & Module Integration | AAOI | Applied Optoelectronics | Small | Yes | 100G/400G QSFP28/QSFP-DD transceivers |
| Transceiver & Module Integration | FN | Fabrinet | Large | Yes | CM/EMS for optical modules; assembles for COHR, LITE, Ciena, Cisco |
| Transceiver & Module Integration | — | *Nextronics Engineering* | Small | No | Taiwan; board-level optical connectivity — in wiki as Nextronics.md |
| Transceiver & Module Integration | — | *PENG (Penguin Solutions)* | Small | No | Optical interconnect systems — in wiki as PENG.md |
| Coherent Line Systems & ROADM | CIEN | Ciena Corporation | Large | Yes | WaveLogic coherent DSP (best-in-class); 6500 platform ROADM; WaveServer |
| Coherent Line Systems & ROADM | LITE | Lumentum Holdings | Large | Yes | ROADM line cards, tunable lasers for DWDM |
| Coherent Line Systems & ROADM | COHR | Coherent Corp | Large | Yes | Coherent modules for Nokia/Infinera integration |
| Photonic Sensing & LIDAR | OUST | Ouster Inc. | Small | No | Solid-state LIDAR (digital LIDAR, SPAD-based); registered in Robotics & Edge AI sector |
| Photonic Sensing & LIDAR | LASR | nLIGHT Inc. | Small | Yes | High-power fiber lasers used in directed energy and industrial sensing |
| Photonic Sensing & LIDAR | VIAV | Viavi Solutions | Mid | Yes | Optical fiber sensing (distributed temperature/acoustic sensing — DTS/DAS) |

---

## Structural Gaps

### Gap: Silicon Photonics Foundry — No Investable Pure-Play
SiPh processes are offered by TSMC (N45SiPh), GlobalFoundries (GF Fotonix 45CLO), Tower/Intel Foundry, and Imec. None of these are investable as pure-play SiPh foundries — SiPh is a process option within a diversified foundry. The SiPh IP (PDK, design kit, active alignment process) is the actual moat, and it is locked inside foundry relationships. **Why it matters:** CPO (co-packaged optics) is the architectural direction for >1.6T switch ASICs — every major hyperscaler GPU cluster beyond the current generation likely ships with co-packaged SiPh optical I/O. The winners in CPO are the SiPh PDK holders + the foundries that offer them. **Watch for:** Any SiPh-focused fabless company (Ayar Labs, Lightelligence) going public; Intel IFS SiPh design-win announcements.

### Gap: Coherent DSP ASIC Design
The coherent DSP ASIC (Ciena WaveLogic, Nokia PSE series, Acacia Silicon One, Infinera ICE-X) is the core IP in a coherent transceiver. It is fabless designed and foundry manufactured. Ciena is the only pure-play listed company where coherent DSP is a primary revenue driver. Acacia was acquired by Cisco. Most other DSP ASIC designers are private or embedded in vertically integrated companies. **Watch for:** Ciena DSP generation roadmap (WaveLogic 6 / 7); any coherent DSP fabless IPO.

### Gap: Passive WSS (Wavelength Selective Switch) Components
The WSS is the routing element inside every ROADM and is a key bottleneck for flex-grid coherent networking. Dominant suppliers are II-VI (now Coherent), Lumentum, and Finisar (now Coherent) — all consolidated into COHR. The MEMS-based WSS manufacturing process (micro-mirror array, diffraction grating, hermetic packaging) is technically complex and controlled by 2–3 suppliers globally. **Watch for:** Consolidation-driven capacity constraints in COHR's passive component business unit.

### Gap: VCSEL Epitaxy for 3D Sensing and LiDAR at Scale
High-power VCSEL arrays (for Apple FaceID, ToF camera, automotive LIDAR illumination) require MOCVD epi that is structurally distinct from telecom laser epi. The suppliers are COHR, LITE, and II-VI (now COHR). IQE provides epi wafers to multiple customers. Scaling VCSEL production for automotive LIDAR volumes requires MOCVD reactor capacity that is currently shared with telecom laser production. **Watch for:** COHR/LITE VCSEL production capacity guidance in earnings calls; IQE VCSEL revenue mix.

---

## Key Questions to Answer Before Writing the Sector Framework

1. Does the CPO (co-packaged optics) transition replace the pluggable transceiver market within 5 years, or does it create a parallel market tier? Which companies survive the transition — SiPh foundry ecosystems or incumbent III-V transceiver makers?
2. Is Ciena's WaveLogic DSP moat durable against Nokia PSE-6s and the potential for hyperscaler custom coherent ASICs (Google/Meta routing their own DWDM)?
3. Does the convergence of GaN (RF power) and photonics (InP/GaAs) on a single III-V epi platform create a durable cross-sector moat for COHR and MTSI, or do they remain structurally separate markets?
4. Is the 1550nm vs. 905nm LIDAR wavelength battle settled — and does the answer lock in InGaAs APD (1550nm, eye-safe, higher cost) or Si SPAD (905nm, CMOS-compatible, lower cost) as the dominant sensor architecture for robotics?
5. What is the realistic timeline for SiPh-based CPO to reach volume production in GPU switch ASICs — and does POET's heterogeneous integration platform represent a credible alternative to pure TSMC SiPh?
6. Is Corning's ~50% global fiber share structurally defensible as the data center topology shifts from spine-leaf to liquid-cooled rack-scale clusters with shorter fiber runs?

---

## Interrelationship Anchors

### Inputs (this sector consumes from)

| From Sector | From Tier | Product / Signal |
|---|---|---|
| Materials & Mining | Rare Earth Separation | Gallium (6N), Indium (5N), Arsenic, Phosphorus → trimethyl-gallium (TMGa), trimethyl-indium (TMIn) MOCVD precursors → III-V epi wafer |
| Materials & Mining | Silicon & SiC Precursor | Germanium tetrachloride (GeCl4) → fiber preform core deposition (GeO2-doped silica, MCVD/OVD) → single-mode fiber with high-index core |
| Materials & Mining | Electrolytic Refining | High-purity erbium oxide → Er3+ dopant in silica glass → EDFA (erbium-doped fiber amplifier) gain medium |
| Semiconductors | Design (Connectivity) | SerDes / DSP ASIC (28nm–5nm node) → coherent transceiver modem, PAM4 host driver → transceiver electrical interface |
| Electronic Components | High-Frequency PCB | Rogers 4350B / Megtron 6 low-loss PCB → transceiver module RF board, ROADM line card |
| Electronic Components | Connector & Socket Mfg | QSFP-DD / OSFP mechanical cage + connector → pluggable module housing and electrical interface |
| Energy & Power | Power Conversion | Low-noise, regulated DC supply → MOCVD reactor (process gases at stable temperature), LIDAR laser driver (sub-ps timing jitter requirement) |

### Outputs (this sector supplies to)

| To Sector | To Tier | Product / Signal |
|---|---|---|
| Compute Infrastructure | Networking | 400G/800G/1.6T optical transceiver → spine switch port, GPU-to-GPU interconnect |
| Compute Infrastructure | Networking | ROADM / WSS → metro and inter-DC wavelength-switched optical networking layer |
| Compute Infrastructure | Networking | Single-mode fiber ribbon → intra-DC high-density trunk cabling |
| Semiconductors | Lithography Equipment | EUV light source (CO2-laser-driven Sn plasma, 13.5nm) → ASML EUV scanner illumination — photonics is the enabling technology for leading-edge chip manufacturing |
| Semiconductors | Packaging (OSAT) | SiPh interposer / CPO chiplet → GPU/switch ASIC optical I/O port (co-packaged optics, emerging) |
| Semiconductors | Power Devices | GaN-on-SiC epi wafer (MOCVD-grown) → GaN HEMT power amplifier and RF transistor |
| Robotics & Edge AI | Perception Layer | Solid-state LIDAR module, FMCW LIDAR chip → robot and autonomous vehicle 3D sensing |
| Space & Communications | Ground Segment | Coherent DWDM line card → terrestrial fiber backbone connecting satellite ground stations |
| Energy & Power | Grid Monitoring | Distributed acoustic sensing (DAS) / distributed temperature sensing (DTS) fiber system → power grid fault detection, pipeline integrity monitoring |

---

## Research Log
- **2026-05-24** — Initial map-sector run. 8 tiers, 3 hard chokepoints (Y): III-V Substrate & Epitaxial Wafer Growth (Y), Photonic Device Fabrication (Y), EUV light source within Coherent Line Systems; 4 structural gaps flagged: SiPh foundry (no investable pure-play), coherent DSP ASIC (Ciena only), WSS (COHR consolidation), VCSEL epi for automotive. Registered tickers already in Monitor Registry: COHR, LITE, FN, CIEN, VIAV, AAOI, AXTI, LWLG, LASR, SIVE, POET, FOCI. Existing ticker files not yet in registry: GLW, IQE, MTSI, Browave, Nextronics, PENG.

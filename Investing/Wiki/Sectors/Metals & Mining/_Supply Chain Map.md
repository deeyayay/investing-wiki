# Metals & Mining — Supply Chain Map
*Mapped: 2026-05-24 | Anchor: semiconductor-grade and battery-grade material outputs*
*Dimension: D1 — AI Manufacturing Base*

---

## Framework Status
- [x] Supply chain mapped
- [x] Process/product depth added (2026-05-24)
- [x] Interrelationship Anchors documented (2026-05-24)
- [ ] Nodes registered (`/add-ticker TICKER --layer "Layer"` for each below)
- [ ] Ground truth pulled (`/stock-research TICKER` per node)
- [ ] Customer matrix built (`/build-customer-matrix "Metals & Mining"`)
- [ ] Sector Framework written (only after above steps complete)

---

## Value Chain

| Tier | Function | Processes | Key Products / Materials | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|-----------|--------------------------|------------|-------------------|-----------|----------------|
| Geological Exploration & Resource Definition | Delineate ore bodies and estimate recoverable metal tonnage to justify mine capital commitment | Diamond core drilling; reverse circulation (RC) drilling; downhole geophysics (induced polarization, EM); assay sampling (fire assay, ICP-MS); geostatistical resource estimation (Kriging, simulation); feasibility study (PFS → DFS) | Drill core (0.5–5m intervals); assay certificates (ppm Au, % Cu, % REE); JORC / NI 43-101 resource estimate; 43-101 feasibility study; mining license | No | Low–Medium | Geographic monopoly (orebody is unique) | Very High (for successful discovery) / Low (for unsuccessful) |
| Bulk Mining & Ore Extraction | Break, load, and haul rock from the ore body to the processing plant | Open-pit: drill-and-blast (ANFO, emulsion explosive), shovel-truck loading (electric rope shovel), primary crushing (jaw/gyratory crusher); Underground: raise boring, drift development (jumbo drill), longhole stoping, paste backfill; Heap leach: crushed ore stacking on lined pad, dilute acid/alkaline solution application | Run-of-mine (ROM) ore (0.2–2% Cu equiv.); mine waste (tailings, waste rock); limestone (used as flux in smelting); water (process water recycling) | No | Very High | Geographic monopoly (deposit) + Scale | Cyclical |
| Mineral Processing & Concentration | Liberate and concentrate target minerals from gangue rock to produce a saleable or smeltable concentrate | Crushing (secondary/tertiary cone/HPGR); grinding (SAG + ball mill to P80 150–75µm); froth flotation (collector + frother → selective attachment of sulfide/oxide particles to air bubbles); magnetic separation (for Fe-bearing ores); dense media separation; thickening and filtration (pressure filter → moisture <9%); dewatering | Copper concentrate (25–30% Cu), zinc concentrate (50–55% Zn), lithium spodumene concentrate (5–6% Li₂O), rare earth fluorocarbonite or bastnäsite concentrate (40–60% TREO), tantalite-columbite concentrate, nickel sulfide concentrate | Partial | High | Scale + Location | Cyclical |
| Primary Smelting & Pyrometallurgy | Reduce metal from concentrate using heat and flux to produce crude metal or matte for further refining | Copper: flash smelting (Outotec / Mitsubishi process) → blister copper (99% Cu); nickel: flash smelting → nickel matte (35–70% Ni); rare earth: cracking & leaching of bastnäsite/monazite (NaOH or H2SO4 bake) → mixed rare earth carbonate; silicon metal: submerged-arc furnace (SAF) carbothermic reduction of quartz → metallurgical-grade Si (98.5%); aluminum smelting: Hall-Héroult electrolytic reduction (byproduct Ga) | Blister copper (99% Cu); nickel matte (>35% Ni); mixed rare earth carbonate (MREC, ~55% TREO); metallurgical-grade silicon (MG-Si, 98.5% Si); crude gallium (byproduct of Al smelting, ~ppm level in bauxite liquor) | Partial | Very High | Scale + Geographic concentration | Cyclical |
| Electrolytic Refining & Hydrometallurgy | Remove impurities from crude metal to produce refined metal at LME-delivery grade (99.99%+) | Copper: electrolytic refining (anode cast from blister → electrolyte (CuSO4/H2SO4) → cathodic plating of 99.999% Cu; SX-EW: acid leach → solvent extraction (Lix reagent) → electrowinning → cathode Cu); nickel: pressure oxidation (POX) → atmospheric leach → SX/SXEW → Class 1 Ni (>99.8%); cobalt: precipitation from Cu/Ni raffinate → CoSO4 crystallization; tantalum: acid digestion of coltan → liquid-liquid extraction (MIBK/TBP) → Ta₂O₅ powder | LME Grade A copper cathode (99.9995% Cu); Class 1 nickel rounds (>99.8% Ni); cobalt sulfate hexahydrate (CoSO4·7H2O, 20.5% Co); tantalum pentoxide (Ta₂O₅) powder; copper anode slimes (contain Ag, Au, Se, Te — precious metals byproduct) | No | High | Scale + Process IP | Cyclical |
| Rare Earth Separation & Critical Mineral Refining | Separate individual rare earth elements from mixed concentrate and refine critical byproduct metals to usable purity | REE solvent extraction cascade: dissolution in HCl or H2SO4 → multi-stage mixer-settler SX (40–80 stages, D2EHPA / PC88A / Cyanex extractants) → individual REE chloride → precipitation (oxalate) → calcination → individual REE oxide (>99.5% purity); Gallium: activated carbon adsorption from Bayer liquor → electrolysis → UHP Ga (6N); Germanium: zinc smelter flue dust → distillation (GeCl4) → hydrolysis → GeO2 → reduction → UHP Ge; Indium: electrolytic recovery from zinc leach residue → zone refining → 5N In | Neodymium oxide (Nd₂O₃, >99.5%); Praseodymium oxide (Pr₆O₁₁); Dysprosium oxide (Dy₂O₃); Terbium oxide (Tb₄O₇); Lanthanum oxide (La₂O₃); Cerium oxide (CeO₂); Ultra-high purity gallium (6N Ga, 99.9999%); Germanium metal (5N Ge); Indium metal (4N–5N In) | Yes | High | Geographic monopoly (China controls ~85–90% of SX separation capacity) + Process IP | High |
| Silicon & SiC Precursor Production | Upgrade metallurgical-grade silicon to polysilicon and SiC powder grades required for semiconductor and power-device manufacturing | Polysilicon (Siemens process): MG-Si + HCl → trichlorosilane (TCS, SiHCl3) via hydrochlorination → distillation → CVD deposition (TCS + H2 → Si + HCl) on slim rod at 1100°C → chunk polysilicon; FBR process: silane (SiH4) + fluidized seed → granular polysilicon; SiC powder (Acheson process): silica sand + petroleum coke (coke/sand ~0.5:1) in resistance furnace at 2200°C → α-SiC powder; high-purity SiC sublimation: SiC powder → PVT growth → 4H-SiC boule (150–200mm) | Electronic-grade polysilicon (>9N, 99.9999999% Si); granular polysilicon (FBR); trichlorosilane (TCS, 99.9%+); α-SiC powder (green / black Acheson); 4H-SiC boule; SiC wafer substrate (150mm, 200mm, n-type doped) | Yes | Very High | Process IP + Scale (Siemens reactor is capital-intensive; only ~8 companies globally produce electronic-grade poly) | High |
| Battery Material Precursor Production | Process lithium, nickel, cobalt, and manganese into battery-ready chemical forms suitable for cathode and electrolyte manufacturing | Lithium carbonate: spodumene concentrate → roasting (1100°C) + acid digestion → Li2SO4 solution → Na2CO3 precipitation → Li2CO3 (99.5%); lithium hydroxide: Li2CO3 + Ca(OH)2 → LiOH·H2O crystallization → battery-grade LiOH (>56.5% LiOH); NMC cathode precursor (pCAM): co-precipitation of NiSO4 + CoSO4 + MnSO4 in CSTR reactor at controlled pH → Ni(x)Co(y)Mn(z)(OH)2 hydroxide; LFP: solid-state or hydrothermal synthesis of LiFePO4 from Li2CO3 + FeSO4 + H3PO4 | Battery-grade lithium carbonate (>99.5% Li2CO3, <5ppm impurities); battery-grade lithium hydroxide monohydrate (>56.5% LiOH, low Na/K); NMC811 cathode precursor (Ni₀.₈Co₀.₁Mn₀.₁(OH)₂); NMC622 precursor; LFP (LiFePO4) powder; cobalt sulfate (CoSO4·7H2O); nickel sulfate (NiSO4·6H2O) | Partial | High | Process IP + Certification (automotive and storage cell makers qualify each supplier per chemistry) | Medium–High |

---

## Publicly-Traded Nodes

| Tier | Ticker | Company | Mkt Cap | In Registry | Notes |
|------|--------|---------|---------|-------------|-------|
| Geological Exploration | — | *Junior miners / explorers* | — | — | ⚠️ Structural gap for pure-play exploration; most are micro-cap |
| Bulk Mining & Ore Extraction | FCX | Freeport-McMoRan | Large | No (file exists) | #1 publicly-traded copper miner; Grasberg open pit (Indonesia); Americas portfolio |
| Bulk Mining & Ore Extraction | VALE | Vale S.A. | Large | No | World's largest nickel producer; iron ore dominant; cobalt byproduct |
| Bulk Mining & Ore Extraction | RIO | Rio Tinto | Large | No | Copper (Oyu Tolgoi), lithium (Rincon brine), iron ore dominant |
| Bulk Mining & Ore Extraction | BHP | BHP Group | Large | No | Copper (Escondida ~5% of world supply), nickel (WA operations), iron ore |
| Mineral Processing & Concentration | MP | MP Materials | Mid | No (file exists) | Only operating rare earth mine in US (Mountain Pass, CA); ships concentrate to China for separation currently |
| Mineral Processing & Concentration | LYC | Lynas Rare Earths | Large | No | Australia-listed (ASX: LYC); processes REE in Malaysia; building US facility |
| Mineral Processing & Concentration | ALB | Albemarle | Large | No | #1 lithium chemicals globally; Greenbushes spodumene (JV), Chilean brine |
| Mineral Processing & Concentration | SQM | Sociedad Química y Minera | Large | No | Chilean lithium brine (Atacama); #2 lithium producer globally |
| Primary Smelting & Pyrometallurgy | — | *Glencore (GLEN.L)* | Large | No | ⚠️ UK-listed; dominant copper and cobalt smelter; DRC cobalt control |
| Electrolytic Refining & Hydrometallurgy | FCX | Freeport-McMoRan | Large | No (file exists) | Integrated — own rod mills and cathode operations |
| Electrolytic Refining & Hydrometallurgy | LTHM | Arcadium Lithium (was Livent) | Mid | No | Lithium hydroxide production for EV/storage OEMs; acquired by Rio Tinto 2024 |
| Rare Earth Separation & Critical Mineral Refining | MP | MP Materials | Mid | No (file exists) | Building Stage III separation + magnet alloy at Mountain Pass; critical US dependency |
| Rare Earth Separation & Critical Mineral Refining | — | *China Northern Rare Earth Group* | Large | No | ⚠️ China-listed; controls ~35% of global HREE separation — no US-accessible investment |
| Rare Earth Separation & Critical Mineral Refining | — | *Vital Metals / NovaStar* | Small | No | ⚠️ Canada/Australia listed; processing not yet at scale |
| Silicon & SiC Precursor Production | DQNGY | Daqo New Energy | Mid | No | China-based but US ADR; #1 or #2 polysilicon volume globally |
| Silicon & SiC Precursor Production | WOLF | Wolfspeed | Mid | No | Only large-scale 4H-SiC substrate maker outside China; 150mm and 200mm wafers |
| Silicon & SiC Precursor Production | — | *Wacker Chemie (WCH.DE)* | Mid | No | ⚠️ Germany-listed; polysilicon + silicone; European exposure |
| Silicon & SiC Precursor Production | — | *Hemlock Semiconductor* | — | No | ⚠️ Private JV (DowCorning heritage); major US polysilicon producer |
| Battery Material Precursor Production | ALB | Albemarle | Large | No | Li2CO3 and LiOH production; key EV/storage supplier |
| Battery Material Precursor Production | SQM | Sociedad Química y Minera | Large | No | Li2CO3 from Atacama brine |
| Battery Material Precursor Production | LAC | Lithium Americas | Small | No | Thacker Pass (NV) — largest known US Li deposit; in development |
| Battery Material Precursor Production | — | *Umicore (UMI.BR)* | Mid | No | ⚠️ Belgium-listed; NMC cathode precursor (pCAM); cobalt refining |

---

## Structural Gaps

### Gap: Rare Earth Separation — No US/Western Pure-Play at Scale
China controls approximately 85–90% of global rare earth separation capacity. MP Materials ships mixed rare earth concentrate (MREC) from Mountain Pass to China for separation — it does not yet produce separated individual oxides at scale domestically (Stage III is under construction). Lynas (ASX-listed) separates in Malaysia. There is no US-listed company that currently separates individual heavy rare earths (Dy, Tb) at commercial scale. **Why it matters:** NdFeB permanent magnets (servo motors in robots, traction motors in EVs, voice coil actuators in hard drives) require Nd, Pr, Dy, Tb — all of which flow exclusively through Chinese separation. **Watch for:** MP Stage III commissioning milestones; any DoD-backed HREE separation announcements; Lynas US processing facility progress.

### Gap: Gallium / Germanium / Indium Refining
Gallium (GaAs VCSEL, GaN HEMT), germanium (fiber optic preform, IR optics, SiGe HBT), and indium (ITO, InGaAs photodetector) are byproducts of aluminum/zinc smelting. China produces >80% of refined gallium and >60% of refined germanium globally. Both were placed on China's export control list in 2023. No US- or Europe-listed company produces these at industrial scale. The silicon photonics shift (GaAs → SiPh) reduces but does not eliminate Ga demand; GaN-on-SiC for power devices increases it. **Watch for:** Any western zinc smelter (Teck, Boliden) announcing Ga/In byproduct recovery; critical mineral processing plant approvals in the US or EU.

### Gap: Polysilicon — China Concentration Risk
Despite DQNGY being a US ADR, approximately 90% of global polysilicon production is in China (Daqo, GCL Poly, Xinte, East Hope). Wacker Chemie (Germany) and Hemlock (US, private JV) are the only meaningful non-Chinese producers. Semiconductor-grade polysilicon (>9N) is even more concentrated than solar-grade. The Siemens CVD reactor process is well-understood but requires enormous capital and energy. **Watch for:** Any DOE loan guarantee or CHIPS Act-adjacent polysilicon program; Wacker capacity announcements.

### Gap: NdFeB Magnet Alloy Production
Separated rare earth oxides must be reduced to metal and alloyed (NdFeB: Nd2Fe14B) before magnet manufacturing. China controls the majority of this step as well. MP Materials is working toward domestic alloy production (Stage III). There is no US-listed company that currently produces NdFeB alloy at commercial scale — the gap sits between REE separation (above) and the magnet manufacturers (in Robotics & Edge AI sector).

---

## Key Questions to Answer Before Writing the Sector Framework

1. Will MP Materials' Stage III (separation → alloy → magnet) vertical integration succeed at cost-competitive scale, and on what timeline relative to DoD demand requirements?
2. Does the CHIPS Act's critical minerals funding mechanism create enough incentive to shift meaningful polysilicon or REE separation capacity outside China within a 5-year window?
3. Is Wolfspeed's SiC substrate expansion (150mm→200mm wafers) sufficient to meet the SiC MOSFET demand implied by 800VDC data center architecture at scale — or is SiC substrate supply a multi-year bottleneck for the entire power conversion sector?
4. With China's Ga and Ge export controls in force, is there a credible western supply chain for GaN-on-SiC power devices that doesn't route through Chinese-refined gallium?
5. How much of the REE processing gap is economic (Chinese producers sell below marginal western cost) vs. technical (Chinese process IP is genuinely superior)? What conditions would shift the economics?
6. Is there an investable battery material precursor play outside the lithium carbonate/hydroxide commodity cycle — specifically in NMC pCAM production or LFP synthesis?

---

## Interrelationship Anchors

### Inputs (this sector consumes from)

| From Sector | From Tier | Product / Signal |
|---|---|---|
| Energy & Power | Power Generation & Transmission | Grid power (high consumption: aluminum/Si smelting at 13–15 MWh/t Al; polysilicon at 60–120 kWh/kg; electrolytic Cu refining) |
| Electronic Components | Connector & Socket Mfg | Mining equipment sensors, automation connectors, haul truck electronics |
| Compute Infrastructure | Data & AI Systems | Ore body modeling (AI/ML for drill targeting, geological interpretation), autonomous haul truck control systems |

### Outputs (this sector supplies to)

| To Sector | To Tier | Product / Signal |
|---|---|---|
| Semiconductors | Wafer Production | Polysilicon (>9N) → CZ crystal growth → silicon wafer |
| Semiconductors | Power Devices | SiC powder → Acheson process → 4H-SiC boule → SiC substrate → SiC MOSFET |
| Semiconductors | Wafer Fabrication | UHP specialty gases (NF3, SiH4, WF6, NH3, HCl from chemical processing of mineral inputs) → CVD/ALD deposition and clean |
| Photonics & Optical | Epitaxial Growth | Gallium (6N), Indium (5N), Arsenic, Phosphorus → MOCVD source material → GaAs/InP/InGaAs epi wafer |
| Photonics & Optical | Optical Fiber | Germanium tetrachloride (GeCl4, derived from Ge metal) → vapor-phase MCVD/OVD process → GeO2-doped silica fiber preform (high-index core) |
| Electronic Components | MLCC Manufacturing | Barium carbonate + TiO2 (from ilmenite/rutile mining) → BaTiO3 dielectric powder |
| Electronic Components | MLCC Manufacturing | Nickel powder (from Class 1 Ni refining) → Ni internal electrode paste |
| Electronic Components | Film & Electrolytic Cap Mfg | Tantalum pentoxide (Ta2O5) → solid tantalum capacitor anode |
| Electronic Components | PCB & Substrate Mfg | Electrolytic copper foil (9–18µm, from refined copper cathode + rolling) → PCB inner layer, IC substrate SAP plating |
| Energy & Power | Grid-Scale Storage | Lithium carbonate / lithium hydroxide → NMC/LFP/NCA cathode active material |
| Energy & Power | Grid-Scale Storage | NiSO4 + CoSO4 → NMC cathode precursor (pCAM) |
| Energy & Power | Power Infrastructure | Copper rod + ingot → transformer winding, overhead conductor, underground cable, EV motor winding |
| Robotics & Edge AI | Actuators & Motors | Neodymium oxide, Praseodymium oxide, Dysprosium oxide → NdFeB alloy → sintered permanent magnet → servo motor, voice coil actuator, traction motor |

---

## Research Log
- **2026-05-24** — Initial map-sector run. 8 tiers, 3 hard chokepoints (Y): Rare Earth Separation, Silicon & SiC Precursor Production (polysilicon), NdFeB alloy (structural gap). 4 structural gaps flagged: REE separation (no western scale), Ga/Ge/In refining (China controlled), polysilicon (China ~90%), NdFeB magnet alloy. Existing ticker files (not yet in registry): FCX, MP. New candidates not yet in registry: VALE, RIO, BHP, ALB, SQM, DQNGY, WOLF, LAC, LYC (ASX).

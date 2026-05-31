# Monitor Registry
*The research-monitor skill reads this file on every run. Add tickers here — no skill update needed.*
*Last updated: May 24, 2026 — /map-sector Space & Communications run; IRDM, GSAT, VSAT, KTOS candidate stubs added*

---

## How to Add a Ticker
Run `/add-ticker TICKER [--sector "Sector Name"]` — the skill creates the wiki page, registers it here, and runs stock research automatically.

Manual fallback:
1. Find the right sector table (or create a new `##` section for a new sector)
2. Add a row: `| TICKER | Company Name | CIK | Exchange | Investing/Wiki/Sectors/[SECTOR]/[TICKER].md | — |`
3. For non-US filers with no SEC filing, set CIK to `none`

## How to Add a Sector
Add a new `## Sector Name` heading with a table using the same column structure.

---

## Robotics & Edge AI

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| AMBA | Ambarella, Inc. | 0001280263 | NASDAQ | Investing/Wiki/Sectors/Robotics & Edge AI/AMBA.md | 8.0 |
| OUST | Ouster, Inc. | 0001816581 | NASDAQ | Investing/Wiki/Sectors/Robotics & Edge AI/OUST.md | 6.5 |

---

## Photonics & Optical

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| COHR | Coherent Corp | 0000820318 | NYSE | Investing/Wiki/Sectors/Photonics & Optical/COHR.md | — |
| LITE | Lumentum Holdings | 0001633978 | NASDAQ | Investing/Wiki/Sectors/Photonics & Optical/LITE.md | — |
| FN | Fabrinet | 0001408710 | NYSE | Investing/Wiki/Sectors/Photonics & Optical/FN.md | — |
| CIEN | Ciena Corporation | 0000936395 | NYSE | Investing/Wiki/Sectors/Photonics & Optical/CIEN.md | — |
| VIAV | Viavi Solutions | 0000912093 | NASDAQ | Investing/Wiki/Sectors/Photonics & Optical/VIAV.md | — |
| AAOI | Applied Optoelectronics | 0001158114 | NASDAQ | Investing/Wiki/Sectors/Photonics & Optical/AAOI.md | — |
| AXTI | AXT Inc. | 0001051627 | NASDAQ | Investing/Wiki/Sectors/Photonics & Optical/AXTI.md | — |
| LWLG | Lightwave Logic | 0001325964 | NASDAQ | Investing/Wiki/Sectors/Photonics & Optical/LWLG.md | — |
| LASR | nLIGHT Inc. | 0001124796 | NASDAQ | Investing/Wiki/Sectors/Photonics & Optical/LASR.md | — |
| SIVE | Sivers Semiconductors | none | Nasdaq Stockholm | Investing/Wiki/Sectors/Photonics & Optical/SIVE.md | 5.5 |
| POET | POET Technologies | none | TSX Venture | Investing/Wiki/Sectors/Photonics & Optical/POET.md | — |
| FOCI | FOCI Fiber Optic Communications, Inc. | none | TPEX (Taiwan) | Investing/Wiki/Sectors/Photonics & Optical/FOCI.md | — |

<!-- CANDIDATE (/map-sector 2026-05-24): GLW (Corning Incorporated) — Optical Fiber & Preform Manufacturing layer. ~50% global optical fiber market; OVD preform; SMF-28. Run /add-ticker GLW --sector "Photonics & Optical" --layer "Optical Fiber & Preform Manufacturing" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): IQE (IQE plc, AIM: IQE) — III-V Substrate & Epitaxial Wafer Growth layer. MOCVD epi foundry; VCSEL and GaN epi for multiple customers. UK AIM-listed. Run /add-ticker IQE --sector "Photonics & Optical" --layer "III-V Substrate & Epitaxial Wafer Growth" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): MTSI (MACOM Technology Solutions) — Photonic Device Fabrication layer. GaAs/InP/GaN chip fab; drivers, TIAs, photonic ICs; strong DC transceiver exposure. Run /add-ticker MTSI --sector "Photonics & Optical" --layer "Photonic Device Fabrication" to onboard. -->
<!-- CANDIDATE (/scout-tickers 2026-05-31): 6965.T (Hamamatsu Photonics) — Photonic Sensing & LIDAR. Run /add-ticker 6965.T --sector "Photonics & Optical" --layer "Photonic Sensing & LIDAR" to onboard. -->
<!-- CANDIDATE (/scout-tickers 2026-05-31): PRY.MI (Prysmian S.p.A.) — Optical Fiber & Preform Manufacturing. Run /add-ticker PRY.MI --sector "Photonics & Optical" --layer "Optical Fiber & Preform Manufacturing" to onboard. -->
<!-- CANDIDATE (/scout-tickers 2026-05-31): 5801.T (Furukawa Electric) — Optical Fiber & Preform Manufacturing. Run /add-ticker 5801.T --sector "Photonics & Optical" --layer "Optical Fiber & Preform Manufacturing" to onboard. -->

---

## Semiconductors

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| NVDA | NVIDIA Corporation | 0001045810 | NASDAQ | Investing/Wiki/Sectors/Semiconductors/NVDA.md | 9.5 |
| MU | Micron Technology | 0000723125 | NASDAQ | Investing/Wiki/Sectors/Semiconductors/MU.md | — |
| MRVL | Marvell Technology | 0001058057 | NASDAQ | Investing/Wiki/Sectors/Semiconductors/MRVL.md | — |
| AEHR | Aehr Test Systems | 0001040896 | NASDAQ | Investing/Wiki/Sectors/Semiconductors/AEHR.md | — |
| ALAB | Astera Labs, Inc. | 0001736297 | NASDAQ | Investing/Wiki/Sectors/Semiconductors/ALAB.md | — |
| CRDO | Credo Technology Group Holding Ltd | 0001807794 | NASDAQ | Investing/Wiki/Sectors/Semiconductors/CRDO.md | — |
| AMKR | Amkor Technology, Inc. | 0001047127 | NASDAQ | Investing/Wiki/Sectors/Semiconductors/AMKR.md | — |

<!-- CANDIDATE (/map-sector 2026-05-24): SNPS (Synopsys) — EDA & Design IP layer. Run /add-ticker SNPS --sector "Semiconductors" --layer "EDA & Design IP" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): CDNS (Cadence Design Systems) — EDA & Design IP layer. Run /add-ticker CDNS --sector "Semiconductors" --layer "EDA & Design IP" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): ARM (Arm Holdings) — EDA & Design IP layer. Run /add-ticker ARM --sector "Semiconductors" --layer "EDA & Design IP" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): LRCX (Lam Research) — Deposition & Etch Equipment layer. Run /add-ticker LRCX --sector "Semiconductors" --layer "Deposition & Etch Equipment" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): AMAT (Applied Materials) — Deposition & Etch Equipment layer. Run /add-ticker AMAT --sector "Semiconductors" --layer "Deposition & Etch Equipment" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): KLAC (KLA Corporation) — Inspection & Metrology layer. Run /add-ticker KLAC --sector "Semiconductors" --layer "Inspection & Metrology" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): ENTG (Entegris) — Raw Materials layer. Run /add-ticker ENTG --sector "Semiconductors" --layer "Raw Materials" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): ICHR (Ichor Holdings) — Raw Materials layer. Run /add-ticker ICHR --sector "Semiconductors" --layer "Raw Materials" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): ONTO (Onto Innovation) — Inspection & Metrology layer. Run /add-ticker ONTO --sector "Semiconductors" --layer "Inspection & Metrology" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): ASX (ASE Technology / Advanced Semiconductor Engineering) — Packaging (OSAT) layer. Run /add-ticker ASX --sector "Semiconductors" --layer "Packaging (OSAT)" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): COHU (Cohu Inc.) — Final Test & Burn-In layer. Run /add-ticker COHU --sector "Semiconductors" --layer "Final Test & Burn-In" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): 6857.T (Advantest) — Final Test & Burn-In layer (Japan-listed; dominant AI chip tester). Run /add-ticker 6857.T --sector "Semiconductors" --layer "Final Test & Burn-In" to onboard. -->

---

## AI Infrastructure

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| IREN | IREN Limited | 0001704720 | NASDAQ | Investing/Wiki/Sectors/AI Infrastructure/IREN.md | — |
| ANET | Arista Networks | 0001313925 | NYSE | Investing/Wiki/Sectors/AI Infrastructure/ANET.md | — |
| VRT | Vertiv Holdings | 0001793309 | NYSE | Investing/Wiki/Sectors/AI Infrastructure/VRT.md | — |
| SMCI | Super Micro Computer | 0001375365 | NASDAQ | Investing/Wiki/Sectors/AI Infrastructure/SMCI.md | — |
| P | Everpure Inc. (fka Pure Storage) | 0001474432 | NYSE | Investing/Wiki/Sectors/AI Infrastructure/P.md | — |

<!-- CANDIDATE (/map-sector 2026-05-24): NTAP (NetApp) — Storage Systems layer. All-flash arrays + object storage (ONTAP / StorageGRID); strong AI storage pipeline. Run /add-ticker NTAP --sector "Compute Infrastructure" --layer "Storage Systems" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): WDC (Western Digital) — Storage Systems layer. NVMe SSD + HDD; enterprise flash for hyperscalers; NAND vertically integrated. Run /add-ticker WDC --sector "Compute Infrastructure" --layer "Storage Systems" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): STX (Seagate Technology) — Storage Systems layer. HDD dominant; high-capacity nearline storage for hyperscaler object stores. Run /add-ticker STX --sector "Compute Infrastructure" --layer "Storage Systems" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): ETN (Eaton Corporation) — Data Center Power Infrastructure layer. Modular UPS (93PM), PDUs, busway, switchgear; broad power management portfolio. Run /add-ticker ETN --sector "Compute Infrastructure" --layer "Data Center Power Infrastructure" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): MOD (Modine Manufacturing) — Thermal Management & Cooling layer. CDUs, cold plates, dry coolers for liquid cooling; pivoting to AI data center thermal. Run /add-ticker MOD --sector "Compute Infrastructure" --layer "Thermal Management & Cooling" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): NVT (nVent Electric) — Thermal Management & Cooling + Power Infrastructure layer. Enclosures, cable management, liquid cooling rack components. Run /add-ticker NVT --sector "Compute Infrastructure" --layer "Thermal Management & Cooling" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): 2308.TW (Delta Electronics Taiwan) — Compute Node Design & ODM Assembly layer. Taiwan-listed; power supplies + AI server designs; major Nvidia system integrator. Run /add-ticker 2308.TW --sector "Compute Infrastructure" --layer "Compute Node Design & ODM Assembly" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): 6669.TW (Wistron Corporation) — Compute Node Design & ODM Assembly layer. Taiwan ODM; AI server and OCP production for US hyperscalers. Run /add-ticker 6669.TW --sector "Compute Infrastructure" --layer "Compute Node Design & ODM Assembly" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): 3324.TW (Inventec Corporation) — Compute Node Design & ODM Assembly layer. Taiwan ODM; high AI server revenue growth; HPE + hyperscaler customer. Run /add-ticker 3324.TW --sector "Compute Infrastructure" --layer "Compute Node Design & ODM Assembly" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): AMZN (Amazon / AWS) — Hyperscaler & Colocation Operation layer. #1 cloud; dominant AI training (P5 H100, Trainium2); custom ASIC vertical integration. Run /add-ticker AMZN --sector "Compute Infrastructure" --layer "Hyperscaler & Colocation Operation" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): GOOGL (Alphabet / GCP) — Hyperscaler & Colocation Operation layer. GCP + TPU v5; custom silicon moat; AI-native cloud. Run /add-ticker GOOGL --sector "Compute Infrastructure" --layer "Hyperscaler & Colocation Operation" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): MSFT (Microsoft / Azure) — Hyperscaler & Colocation Operation layer. Azure AI; Copilot cloud; deepest OpenAI integration. Run /add-ticker MSFT --sector "Compute Infrastructure" --layer "Hyperscaler & Colocation Operation" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): ORCL (Oracle Cloud) — Hyperscaler & Colocation Operation layer. OCI GPU clusters; NVIDIA preferred partner; GenAI workload momentum. Run /add-ticker ORCL --sector "Compute Infrastructure" --layer "Hyperscaler & Colocation Operation" to onboard. -->

---

## Cybersecurity

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| RBRK | Rubrik Inc. | 0001943896 | NYSE | Investing/Wiki/Sectors/Cybersecurity/RBRK.md | — |
| SAIL | SailPoint, Inc. | 0002030781 | NASDAQ | Investing/Wiki/Sectors/Cybersecurity/SAIL.md | — |

---

## Fintech & E-Commerce

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| MELI | MercadoLibre Inc. | 0001099590 | NASDAQ | Investing/Wiki/Sectors/Fintech & E-Commerce/MELI.md | — |
| HOOD | Robinhood Markets | 0001783879 | NASDAQ | Investing/Wiki/Sectors/Fintech & E-Commerce/HOOD.md | — |
| SOFI | SoFi Technologies, Inc. | 0001818874 | NASDAQ | Investing/Wiki/Sectors/Fintech & E-Commerce/SOFI.md | 9.0 |

<!-- CANDIDATE (/map-sector 2026-05-24): AFRM (Affirm Holdings) — Buy Now Pay Later / Credit Decisioning layer. Real-time underwriting at checkout; BNPL market leader in US; AI credit model moat. Run /add-ticker AFRM --sector "Fintech & E-Commerce" --layer "Buy Now Pay Later & Credit Decisioning" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): PYPL (PayPal Holdings) — Payment Processing & Wallet layer. 430M active accounts; Venmo + PayPal wallet; Braintree gateway; AI fraud decisioning at scale. Run /add-ticker PYPL --sector "Fintech & E-Commerce" --layer "Payment Processing & Digital Wallet" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): SQ (Block, Inc.) — Payment Processing & Commerce Enablement layer. Square POS + Cash App; merchant acquiring + consumer wallet; Bitcoin integration. Run /add-ticker SQ --sector "Fintech & E-Commerce" --layer "Payment Processing & Commerce Enablement" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): NU (Nu Holdings) — Digital Banking & Neobank layer. Largest neobank in Latin America (Brazil, Mexico, Colombia); AI underwriting; 90M+ customers. Run /add-ticker NU --sector "Fintech & E-Commerce" --layer "Digital Banking & Neobank" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): UPST (Upstart Holdings) — AI Credit Underwriting layer. AI-native consumer lending platform; bank partnership model; macro-sensitive but AI-differentiating. Run /add-ticker UPST --sector "Fintech & E-Commerce" --layer "AI Credit Underwriting" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): FLYW (Flywire Corporation) — Vertical Payment Orchestration layer. High-value vertical payments (education, healthcare, travel); FX handling + receivables automation. Run /add-ticker FLYW --sector "Fintech & E-Commerce" --layer "Vertical Payment Orchestration" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): NCNO (nCino, Inc.) — Banking AI & Cloud Platform layer. AI-powered cloud banking platform; commercial loan origination; bank digital transformation. Run /add-ticker NCNO --sector "Fintech & E-Commerce" --layer "Banking AI & Cloud Platform" to onboard. -->

---

## Clean Energy

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| OKLO | Oklo Inc. | 0001828937 | NYSE | Investing/Wiki/Sectors/Clean Energy/OKLO.md | — |
| TE | T1 Energy Inc. | 0001992243 | NYSE | Investing/Wiki/Sectors/Clean Energy/TE.md | — |

<!-- CANDIDATE (/map-sector 2026-05-24): VST (Vistra Energy) — Primary Power Generation layer. Largest US competitive power generator; nuclear (Comanche Peak) + CCGT; Texas merchant market. Run /add-ticker VST --sector "Energy & Power" --layer "Primary Power Generation" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): GEV (GE Vernova) — Primary Power Generation + High-Voltage Transmission layer. Gas turbines (GE 7F.05, HA-class); wind (Haliade-X); Grid Solutions HV transformers + HVDC. Run /add-ticker GEV --sector "Energy & Power" --layer "Primary Power Generation" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): CEG (Constellation Energy) — Primary Power Generation layer. Largest US nuclear operator (21 GW); Microsoft + Amazon nuclear PPA winner. Run /add-ticker CEG --sector "Energy & Power" --layer "Primary Power Generation" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): NEE (NextEra Energy) — Primary Power Generation layer. #1 US wind + solar; FPL nuclear fleet; NEER renewables arm; largest FID machine for clean generation. Run /add-ticker NEE --sector "Energy & Power" --layer "Primary Power Generation" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): ENR.DE (Siemens Energy) — High-Voltage Transmission layer. Germany-listed; HV transformers (2-4 year wait lists); HVDC BlueTec; switchgear. Run /add-ticker ENR.DE --sector "Energy & Power" --layer "High-Voltage Transmission & Grid Infrastructure" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): FLNC (Fluence Energy) — Grid-Scale Storage layer. BESS system integrator (Siemens + AES JV); Gridstack product; Fluence IQ optimization software. Run /add-ticker FLNC --sector "Energy & Power" --layer "Grid-Scale Energy Storage (BESS)" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): BE (Bloom Energy) — Fuel Cell & Distributed Generation layer. SOFC (solid oxide fuel cell); NG + H2 compatible; data center deployments. Run /add-ticker BE --sector "Energy & Power" --layer "Fuel Cell & Distributed Clean Generation" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): LEU (Centrus Energy) — Advanced Nuclear SMR layer. Only US HALEU enrichment capability (Piketon, OH); critical fuel for all fast-spectrum SMRs. Run /add-ticker LEU --sector "Energy & Power" --layer "Advanced Nuclear — SMR & Microreactor" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): PLUG (Plug Power) — Fuel Cell & Distributed Generation layer. PEMFC + PEM electrolyzer + liquid H2; material handling + stationary power. Run /add-ticker PLUG --sector "Energy & Power" --layer "Fuel Cell & Distributed Clean Generation" to onboard. -->

---

## Space & Comms

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| ASTS | AST SpaceMobile | 0001780530 | NASDAQ | Investing/Wiki/Sectors/Space & Comms/ASTS.md | — |
| RKLB | Rocket Lab USA, Inc. | 0001819994 | NASDAQ | Investing/Wiki/Sectors/Space & Comms/RKLB.md | — |

<!-- CANDIDATE (/map-sector 2026-05-24): IRDM (Iridium Communications) — Satellite Connectivity Services + Spectrum & Orbital Operations layers. 66-satellite LEO constellation; L-band MSS; Iridium SBD IoT; Iridium Certus broadband; owns globally-coordinated ITU L-band spectrum. Run /add-ticker IRDM --sector "Space & Comms" --layer "Satellite Connectivity Services" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): GSAT (Globalstar Inc.) — Satellite Connectivity Services + Spectrum & Orbital Operations layers. S-band MSS constellation; Apple Emergency SOS royalty stream; Band 53/n53 terrestrial LTE spectrum asset; SPOT IoT messaging. Run /add-ticker GSAT --sector "Space & Comms" --layer "Satellite Connectivity Services" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): VSAT (Viasat Inc.) — Ground Segment & Network Operations + Satellite Connectivity Services + User Terminal Manufacturing layers. Ka-band HTS (ViaSat-3, >1 Tbps); in-flight broadband (Viasat IFC); government satcom; owns ground gateways and user terminals. Run /add-ticker VSAT --sector "Space & Comms" --layer "Ground Segment & Network Operations" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): KTOS (Kratos Defense & Security Solutions) — Payload Manufacturing + Ground Segment & Network Operations + Satellite Manufacturing Support & Testing layers. OpenSpace satcom ground systems software; GaN T/R module defense electronics; hypersonic test vehicles. Run /add-ticker KTOS --sector "Space & Comms" --layer "Ground Segment & Network Operations" to onboard. -->

---

## Metals & Mining

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| FCX | Freeport-McMoRan | 0000831259 | NYSE | Investing/Wiki/Sectors/Metals & Mining/FCX.md | — |
| MP | MP Materials Corp. | 0001801170 | NYSE | Investing/Wiki/Sectors/Metals & Mining/MP.md | — |

<!-- CANDIDATE (/map-sector 2026-05-24): VALE (Vale S.A.) — Bulk Mining & Ore Extraction layer. World's largest nickel producer; iron ore dominant; cobalt byproduct. Run /add-ticker VALE --sector "Metals & Mining" --layer "Bulk Mining & Ore Extraction" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): RIO (Rio Tinto) — Bulk Mining & Ore Extraction layer. Copper (Oyu Tolgoi), lithium (Rincon), iron ore. Run /add-ticker RIO --sector "Metals & Mining" --layer "Bulk Mining & Ore Extraction" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): BHP (BHP Group) — Bulk Mining & Ore Extraction layer. Escondida (~5% world copper supply), nickel (WA), iron ore. Run /add-ticker BHP --sector "Metals & Mining" --layer "Bulk Mining & Ore Extraction" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): ALB (Albemarle) — Mineral Processing + Battery Material Precursor layer. #1 lithium chemicals globally; Greenbushes spodumene JV; Chilean brine. Run /add-ticker ALB --sector "Metals & Mining" --layer "Battery Material Precursor Production" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): SQM (Sociedad Química y Minera) — Mineral Processing + Battery Material Precursor layer. #2 lithium producer; Atacama brine. Run /add-ticker SQM --sector "Metals & Mining" --layer "Battery Material Precursor Production" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): DQNGY (Daqo New Energy) — Silicon & SiC Precursor Production layer. China-based US ADR; #1–2 polysilicon volume globally. Run /add-ticker DQNGY --sector "Metals & Mining" --layer "Silicon & SiC Precursor Production" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): WOLF (Wolfspeed) — Silicon & SiC Precursor Production layer. Only large-scale 4H-SiC substrate maker outside China; 150mm and 200mm wafers. Run /add-ticker WOLF --sector "Metals & Mining" --layer "Silicon & SiC Precursor Production" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): LAC (Lithium Americas) — Battery Material Precursor Production layer. Thacker Pass (NV) — largest known US lithium deposit; development stage. Run /add-ticker LAC --sector "Metals & Mining" --layer "Battery Material Precursor Production" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): LYC (Lynas Rare Earths) — Mineral Processing + Rare Earth Separation layer. Australia-listed (ASX: LYC); processes REE in Malaysia; building US facility. Run /add-ticker LYC --sector "Metals & Mining" --layer "Rare Earth Separation & Critical Mineral Refining" to onboard. -->

---

## Electronic Components

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|

<!-- CANDIDATE (/map-sector 2026-05-24): 6981.T (Murata Manufacturing) — MLCC Manufacturing + Dielectric & Conductor Materials layer. ~40% global MLCC share; dominant in high-layer-count small case sizes. Run /add-ticker 6981.T --sector "Electronic Components" --layer "MLCC Manufacturing" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): 6762.T (TDK Corporation) — MLCC Manufacturing + Inductor & Transformer Mfg layer. #2 MLCC; also ferrite cores, inductors, EPCOS capacitors. Run /add-ticker 6762.T --sector "Electronic Components" --layer "MLCC Manufacturing" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): 2327.TW (Yageo Corporation) — MLCC Manufacturing + Film & Electrolytic Cap Mfg layer. #3 MLCC globally; KEMET acquisition adds film/electrolytic. Taiwan-listed. Run /add-ticker 2327.TW --sector "Electronic Components" --layer "MLCC Manufacturing" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): VSH (Vishay Intertechnology) — Film & Electrolytic Cap Mfg + Inductor & Transformer Mfg layer. Broad passive portfolio: tantalum, film, electrolytic, resistors. Run /add-ticker VSH --sector "Electronic Components" --layer "Film & Electrolytic Capacitor Mfg" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): RCI (Rogers Corporation) — Substrate & Laminate Materials layer. High-frequency PTFE/ceramic laminates (Rogers 4000 series); antenna and transceiver substrates. Run /add-ticker RCI --sector "Electronic Components" --layer "Substrate & Laminate Materials" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): TTM (TTM Technologies) — PCB Fabrication layer. #1 US PCB manufacturer; advanced AI server and aerospace PCBs. Run /add-ticker TTM --sector "Electronic Components" --layer "PCB Fabrication" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): 3036.TW (Unimicron Technology) — IC Substrate Manufacturing layer. #1 IC substrate globally; advanced ABF substrates for AMD/Intel. Taiwan-listed. Run /add-ticker 3036.TW --sector "Electronic Components" --layer "IC Substrate Manufacturing" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): 3037.TW (Ibiden Co.) — IC Substrate Manufacturing layer. #3 IC substrate; ABF-based; NVIDIA customer. Japan-listed. Run /add-ticker 3037.TW --sector "Electronic Components" --layer "IC Substrate Manufacturing" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): 8046.TW (Nan Ya PCB) — IC Substrate Manufacturing layer. #2 IC substrate; conventional PCBs also. Taiwan-listed. Run /add-ticker 8046.TW --sector "Electronic Components" --layer "IC Substrate Manufacturing" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): TEL (TE Connectivity) — Connector & Socket Manufacturing layer. Broadest connector portfolio; automotive + data center + industrial. Run /add-ticker TEL --sector "Electronic Components" --layer "Connector & Socket Manufacturing" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): APH (Amphenol Corporation) — Connector & Socket Manufacturing layer. #2 connector globally; strong data center and AI infrastructure exposure. Run /add-ticker APH --sector "Electronic Components" --layer "Connector & Socket Manufacturing" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): JBL (Jabil Inc.) — PCB Assembly (EMS / PCBA) layer. #2 EMS globally; AI server PCBA + power supply assembly. Run /add-ticker JBL --sector "Electronic Components" --layer "PCB Assembly (EMS / PCBA)" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): CLS (Celestica) — PCB Assembly (EMS / PCBA) layer. EMS; growing AI infrastructure PCBA share. Run /add-ticker CLS --sector "Electronic Components" --layer "PCB Assembly (EMS / PCBA)" to onboard. -->

---

*To add a new ticker: `/add-ticker TICKER [--sector "Sector Name"]`*

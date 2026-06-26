# Monitor Registry
*The research-monitor skill reads this file on every run. Add tickers here — no skill update needed.*
*Last updated: 2026-06-25 — Reorganized to Layer → Tier → Ticker taxonomy matching the AI Buildout Stack dashboard.*

---

## How to Add a Ticker
Run `/add-ticker TICKER [--sector "Sector Name"] [--layer "Layer Name"]` — the skill creates the wiki page, registers it here, and runs stock research automatically.

Manual fallback:
1. Find the right layer/tier section (or create a new `##` section for a new layer)
2. Add a row: `| TICKER | Company Name | CIK | Exchange | Investing/Wiki/Sectors/[LAYER]/[TIER]/[TICKER].md | — |`
3. For 3-layer tickers (folder), end the path with `/` (no `.md`)
4. For non-US filers with no SEC filing, set CIK to `none`

## How to Add a Layer/Tier Section
Add a new `## Layer · Tier` heading with a table using the same column structure.

---

## L01 Application · Insurance AI

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| LMND | Lemonade, Inc. | 0001728688 | NYSE | Investing/Wiki/Sectors/L01 Application/Insurance AI/LMND/ | — |

<!-- CANDIDATE: ROOT (Root Insurance) — Insurance AI tier. Digital auto insurer; telematics-driven underwriting. Run /add-ticker ROOT --sector "Application" --layer "Insurance AI" to onboard. -->
<!-- CANDIDATE: GWRE (Guidewire Software) — Insurance AI tier. Insurance platform SaaS; policy/claims/billing core systems. Run /add-ticker GWRE --sector "Application" --layer "Insurance AI" to onboard. -->
<!-- CANDIDATE: VRSK (Verisk Analytics) — Insurance AI tier. Risk analytics and data for P&C insurers. Run /add-ticker VRSK --sector "Application" --layer "Insurance AI" to onboard. -->

---

## L01 Application · AI-Native Fintech & Commerce

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| MELI | MercadoLibre Inc. | 0001099590 | NASDAQ | Investing/Wiki/Sectors/L01 Application/AI-Native Fintech & Commerce/MELI.md | — |
| SOFI | SoFi Technologies, Inc. | 0001818874 | NASDAQ | Investing/Wiki/Sectors/L01 Application/AI-Native Fintech & Commerce/SOFI/ | 9.0 |

<!-- CANDIDATE: HOOD (Robinhood Markets) — AI-Native Fintech & Commerce tier. Run /add-ticker HOOD --sector "Application" --layer "AI-Native Fintech & Commerce" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): AFRM (Affirm Holdings) — Buy Now Pay Later / Credit Decisioning layer. AI credit model moat. Run /add-ticker AFRM --sector "Application" --layer "AI-Native Fintech & Commerce" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): NU (Nu Holdings) — Digital Banking & Neobank layer. Largest neobank in Latin America; AI underwriting; 90M+ customers. Run /add-ticker NU --sector "Application" --layer "AI-Native Fintech & Commerce" to onboard. -->

---

## L01 Application · AI Drug Discovery

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| QTRX | Quanterix Corp | 0001503274 | NASDAQ | Investing/Wiki/Sectors/L01 Application/AI Drug Discovery/QTRX/ | — |

---

## L04 Cloud Infrastructure

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| IREN | IREN Limited | 0001704720 | NASDAQ | Investing/Wiki/Sectors/L04 Cloud Infrastructure/NeoClouds & AI-Specialized/IREN.md | — |
| VRT | Vertiv Holdings | 0001793309 | NYSE | Investing/Wiki/Sectors/L04 Cloud Infrastructure/Data Center Facility/VRT/ | — |
| SMCI | Super Micro Computer | 0001375365 | NASDAQ | Investing/Wiki/Sectors/L04 Cloud Infrastructure/Data Center Facility/SMCI.md | — |
| BRUN | Boost Run Inc. | 0002090646 | NASDAQ | Investing/Wiki/Sectors/L04 Cloud Infrastructure/NeoClouds & AI-Specialized/BRUN/ | 7.5 |

<!-- CANDIDATE (/map-sector 2026-05-24): AMZN (Amazon / AWS) — Hyperscaler Clouds tier. #1 cloud; dominant AI training; custom ASIC vertical integration. Run /add-ticker AMZN --sector "Cloud Infrastructure" --layer "Hyperscaler Clouds" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): GOOGL (Alphabet / GCP) — Hyperscaler Clouds tier. GCP + TPU v5; custom silicon moat; AI-native cloud. Run /add-ticker GOOGL --sector "Cloud Infrastructure" --layer "Hyperscaler Clouds" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): MSFT (Microsoft / Azure) — Hyperscaler Clouds tier. Azure AI; Copilot cloud; deepest OpenAI integration. Run /add-ticker MSFT --sector "Cloud Infrastructure" --layer "Hyperscaler Clouds" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): ORCL (Oracle Cloud) — Hyperscaler Clouds tier. OCI GPU clusters; NVIDIA preferred partner; GenAI workload momentum. Run /add-ticker ORCL --sector "Cloud Infrastructure" --layer "Hyperscaler Clouds" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): MOD (Modine Manufacturing) — Data Center Facility tier. CDUs, cold plates, dry coolers; pivoting to AI data center thermal. Run /add-ticker MOD --sector "Cloud Infrastructure" --layer "Data Center Facility" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): NVT (nVent Electric) — Data Center Facility tier. Enclosures, cable management, liquid cooling rack components. Run /add-ticker NVT --sector "Cloud Infrastructure" --layer "Data Center Facility" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): NTAP (NetApp) — Data Center Facility tier. All-flash arrays + object storage; strong AI storage pipeline. Run /add-ticker NTAP --sector "Cloud Infrastructure" --layer "Data Center Facility" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): STX (Seagate Technology) — Data Center Facility tier. HDD dominant; high-capacity nearline storage for hyperscaler object stores. Run /add-ticker STX --sector "Cloud Infrastructure" --layer "Data Center Facility" to onboard. -->

---

## L05 Compute Hardware

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| NVDA | NVIDIA Corporation | 0001045810 | NASDAQ | Investing/Wiki/Sectors/L05 Compute Hardware/Training GPUs/NVDA/ | 9.5 |
| ANET | Arista Networks | 0001313925 | NYSE | Investing/Wiki/Sectors/L05 Compute Hardware/Networking ASICs/ANET/ | — |
| MRVL | Marvell Technology | 0001058057 | NASDAQ | Investing/Wiki/Sectors/L05 Compute Hardware/Networking ASICs/MRVL/ | — |
| NVTS | Navitas Semiconductor Corp | 0001821769 | NASDAQ | Investing/Wiki/Sectors/L05 Compute Hardware/Power Management/NVTS.md | — |
| IFX | Infineon Technologies AG | none | XETRA (Frankfurt) | Investing/Wiki/Sectors/L05 Compute Hardware/Server CPUs/IFX.md | — |

<!-- CANDIDATE (/map-sector 2026-05-24): AMD (Advanced Micro Devices) — Training GPUs tier. MI300X GPU; ROCm ecosystem; gaining training share. Run /add-ticker AMD --sector "Compute Hardware" --layer "Training GPUs" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): AVGO (Broadcom) — Networking ASICs tier. Custom AI ASICs + networking chips; hyperscaler relationships. Run /add-ticker AVGO --sector "Compute Hardware" --layer "Networking ASICs" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): INTC (Intel) — Server CPUs tier. Xeon data center CPUs; Gaudi AI accelerators. Run /add-ticker INTC --sector "Compute Hardware" --layer "Server CPUs" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): ARM (Arm Holdings) — Server CPUs tier. CPU architecture licensor; dominant mobile + growing data center. Run /add-ticker ARM --sector "Compute Hardware" --layer "Server CPUs" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): QBTS (D-Wave Quantum) — Quantum Computing tier. Run /add-ticker QBTS --sector "Compute Hardware" --layer "Quantum Computing" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): RGTI (Rigetti Computing) — Quantum Computing tier. Run /add-ticker RGTI --sector "Compute Hardware" --layer "Quantum Computing" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): MPWR (Monolithic Power Systems) — Power Management tier. High-efficiency DC-DC converters for AI servers. Run /add-ticker MPWR --sector "Compute Hardware" --layer "Power Management" to onboard. -->

---

## L06 Memory

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| MU | Micron Technology | 0000723125 | NASDAQ | Investing/Wiki/Sectors/L06 Memory/HBM/MU/ | — |

<!-- CANDIDATE: SK Hynix — HBM tier. #1 HBM market share; HBM3E dominant supplier. Foreign-listed (KRX). Run /add-ticker SK Hynix --sector "Memory" --layer "HBM" to onboard. -->
<!-- CANDIDATE: Samsung Electronics — DRAM tier. #1 DRAM + NAND globally; HBM3E ramping. Foreign-listed (KRX). Run /add-ticker Samsung --sector "Memory" --layer "DRAM" to onboard. -->
<!-- CANDIDATE: SNDK (SanDisk / WD) — NAND Flash tier. Run /add-ticker SNDK --sector "Memory" --layer "NAND Flash" to onboard. -->

---

## L07 Interconnect

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| COHR | Coherent Corp | 0000820318 | NYSE | Investing/Wiki/Sectors/L07 Interconnect/Pluggable Optical Transceivers/COHR.md | — |
| LITE | Lumentum Holdings | 0001633978 | NASDAQ | Investing/Wiki/Sectors/L07 Interconnect/Pluggable Optical Transceivers/LITE.md | — |
| FN | Fabrinet | 0001408710 | NYSE | Investing/Wiki/Sectors/L07 Interconnect/Pluggable Optical Transceivers/FN.md | — |
| CIEN | Ciena Corporation | 0000936395 | NYSE | Investing/Wiki/Sectors/L07 Interconnect/Pluggable Optical Transceivers/CIEN.md | — |
| VIAV | Viavi Solutions | 0000912093 | NASDAQ | Investing/Wiki/Sectors/L07 Interconnect/Pluggable Optical Transceivers/VIAV.md | — |
| AAOI | Applied Optoelectronics | 0001158114 | NASDAQ | Investing/Wiki/Sectors/L07 Interconnect/Pluggable Optical Transceivers/AAOI.md | — |
| 5801.T | Furukawa Electric Co., Ltd. | none | TSE (Tokyo) | Investing/Wiki/Sectors/L07 Interconnect/Pluggable Optical Transceivers/5801.T.md | — |
| 6451.TW | ShunSin Technology Holdings Limited | none | TWSE (Taiwan) | Investing/Wiki/Sectors/L07 Interconnect/Pluggable Optical Transceivers/6451.TW/ | — |
| 6965.T | Hamamatsu Photonics K.K. | none | TSE (Tokyo) | Investing/Wiki/Sectors/L07 Interconnect/Silicon Photonics Engines/6965.T.md | — |
| 6841.T | Yokogawa Electric Corporation | none | TSE (Tokyo) | Investing/Wiki/Sectors/L07 Interconnect/Silicon Photonics Engines/6841.T.md | — |
| PRY.MI | Prysmian S.p.A. | none | Euronext Milan | Investing/Wiki/Sectors/L07 Interconnect/Coherent Optical Transport/PRY.MI.md | — |
| 6754.T | Anritsu Corporation | none | TSE (Tokyo) | Investing/Wiki/Sectors/L07 Interconnect/Coherent Optical Transport/6754.T.md | — |
| LWLG | Lightwave Logic | 0001325964 | NASDAQ | Investing/Wiki/Sectors/L07 Interconnect/External Light Sources (CW Lasers)/LWLG.md | — |
| LASR | nLIGHT Inc. | 0001124796 | NASDAQ | Investing/Wiki/Sectors/L07 Interconnect/External Light Sources (CW Lasers)/LASR.md | — |
| SIVE | Sivers Semiconductors | none | Nasdaq Stockholm | Investing/Wiki/Sectors/L07 Interconnect/External Light Sources (CW Lasers)/SIVE.md | 5.5 |
| POET | POET Technologies | none | TSX Venture | Investing/Wiki/Sectors/L07 Interconnect/External Light Sources (CW Lasers)/POET.md | — |
| FOCI | FOCI Fiber Optic Communications, Inc. | none | TPEX (Taiwan) | Investing/Wiki/Sectors/L07 Interconnect/External Light Sources (CW Lasers)/FOCI.md | — |
| ALAB | Astera Labs, Inc. | 0001736297 | NASDAQ | Investing/Wiki/Sectors/L07 Interconnect/High-Speed Connectivity ICs/ALAB.md | — |
| CRDO | Credo Technology Group Holding Ltd | 0001807794 | NASDAQ | Investing/Wiki/Sectors/L07 Interconnect/High-Speed Connectivity ICs/CRDO/ | — |

<!-- CANDIDATE (/map-sector 2026-05-24): GLW (Corning Incorporated) — Fiber Array Units & Connectors tier. ~50% global optical fiber market; OVD preform; SMF-28. Run /add-ticker GLW --sector "Interconnect" --layer "Fiber Array Units & Connectors" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): IQE (IQE plc, AIM: IQE) — (primary: Semiconductor Materials · InP & GaAs Substrates). MOCVD epi foundry; VCSEL and GaN epi for transceiver customers. -->
<!-- CANDIDATE (/map-sector 2026-05-24): MTSI (MACOM Technology Solutions) — Pluggable Optical Transceivers tier. GaAs/InP/GaN chip fab; drivers, TIAs, photonic ICs; strong DC transceiver exposure. Run /add-ticker MTSI --sector "Interconnect" --layer "Pluggable Optical Transceivers" to onboard. -->

---

## L08 Advanced Packaging

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| AMKR | Amkor Technology, Inc. | 0001047127 | NASDAQ | Investing/Wiki/Sectors/L08 Advanced Packaging/Wafer-Level Packaging (CoWoS)/AMKR.md | — |

<!-- CANDIDATE: BESI (BE Semiconductor Industries) — Packaging Equipment tier. Die attach + wire bonding equipment leader. Run /add-ticker BESI --sector "Advanced Packaging" --layer "Packaging Equipment" to onboard. -->
<!-- CANDIDATE: LPK — FC-BGA Substrates tier. Run /add-ticker LPK --sector "Advanced Packaging" --layer "FC-BGA Substrates" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): ASX (ASE Technology) — Wafer-Level Packaging (CoWoS) tier. OSAT. Run /add-ticker ASX --sector "Advanced Packaging" --layer "Wafer-Level Packaging (CoWoS)" to onboard. -->

---

## L10 Semiconductor Equipment

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| AEHR | Aehr Test Systems | 0001040896 | NASDAQ | Investing/Wiki/Sectors/L10 Semiconductor Equipment/Metrology & Inspection/AEHR/ | — |
| 6857.T | Advantest Corporation | none | TSE (Tokyo) | Investing/Wiki/Sectors/L10 Semiconductor Equipment/Metrology & Inspection/6857.T.md | — |
| FORM | FormFactor, Inc. | 0001039399 | NASDAQ | Investing/Wiki/Sectors/L10 Semiconductor Equipment/Metrology & Inspection/FORM.md | — |

<!-- CANDIDATE: ASML (ASML Holding) — EUV tier. Sole EUV scanner supplier; chokepoint. Run /add-ticker ASML --sector "Semiconductor Equipment" --layer "EUV" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): LRCX (Lam Research) — Deposition & Etch tier. Run /add-ticker LRCX --sector "Semiconductor Equipment" --layer "Deposition & Etch" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): AMAT (Applied Materials) — Deposition & Etch tier. Run /add-ticker AMAT --sector "Semiconductor Equipment" --layer "Deposition & Etch" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): KLAC (KLA Corporation) — Metrology & Inspection tier. Run /add-ticker KLAC --sector "Semiconductor Equipment" --layer "Metrology & Inspection" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): ONTO (Onto Innovation) — Metrology & Inspection tier. Run /add-ticker ONTO --sector "Semiconductor Equipment" --layer "Metrology & Inspection" to onboard. -->

---

## L09 Semiconductor Foundry

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|

<!-- CANDIDATE: TSM (TSMC) — Leading-Edge Logic Foundry tier. N3/N2 process leader; CoWoS packaging. Run /add-ticker TSM --sector "Semiconductor Foundry" --layer "Leading-Edge Logic Foundry" to onboard. -->
<!-- CANDIDATE: GFS (GlobalFoundries) — Leading-Edge Logic Foundry tier. Mature node + RF/mixed-signal. Run /add-ticker GFS --sector "Semiconductor Foundry" --layer "Leading-Edge Logic Foundry" to onboard. -->

---

## L11 Semiconductor Materials

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| AXTI | AXT Inc. | 0001051627 | NASDAQ | Investing/Wiki/Sectors/L11 Semiconductor Materials/InP & GaAs Substrates/AXTI.md | — |

<!-- CANDIDATE: IQE (IQE plc) — InP & GaAs Substrates tier. MOCVD epi foundry. UK AIM-listed. Run /add-ticker IQE --sector "Semiconductor Materials" --layer "InP & GaAs Substrates" to onboard. -->
<!-- CANDIDATE: WOLF (Wolfspeed) — SiC Wafers tier. Only large-scale 4H-SiC substrate maker outside China. Run /add-ticker WOLF --sector "Semiconductor Materials" --layer "SiC Wafers" to onboard. -->
<!-- CANDIDATE: 4043.T (Shin-Etsu Chemical) — Silicon Wafers tier. Largest silicon wafer maker globally. TSE-listed. Run /add-ticker 4043.T --sector "Semiconductor Materials" --layer "Silicon Wafers" to onboard. -->
<!-- CANDIDATE: LIN (Linde plc) — Photoresist & Specialty Gases tier. #1 industrial gases; critical semiconductor process gases. Run /add-ticker LIN --sector "Semiconductor Materials" --layer "Photoresist & Specialty Gases" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): ENTG (Entegris) — Photoresist & Specialty Gases tier. Run /add-ticker ENTG --sector "Semiconductor Materials" --layer "Photoresist & Specialty Gases" to onboard. -->

---

## L12 Critical Minerals

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| FCX | Freeport-McMoRan | 0000831259 | NYSE | Investing/Wiki/Sectors/L12 Critical Minerals/Copper/FCX.md | — |
| MP | MP Materials Corp. | 0001801170 | NYSE | Investing/Wiki/Sectors/L12 Critical Minerals/Rare Earths/MP.md | — |
| ELMT | The Elmet Group Co. | 0002101698 | NASDAQ | Investing/Wiki/Sectors/L12 Critical Minerals/Lithium & Specialty Metals/ELMT.md | — |

<!-- CANDIDATE (/map-sector 2026-05-24): VALE (Vale S.A.) — Copper/Nickel tier. World's largest nickel producer; iron ore dominant; cobalt byproduct. Run /add-ticker VALE --sector "Critical Minerals" --layer "Copper" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): ALB (Albemarle) — Lithium & Specialty Metals tier. #1 lithium chemicals globally. Run /add-ticker ALB --sector "Critical Minerals" --layer "Lithium & Specialty Metals" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): LYC (Lynas Rare Earths) — Rare Earths tier. ASX-listed; processes REE in Malaysia. Run /add-ticker LYC --sector "Critical Minerals" --layer "Rare Earths" to onboard. -->

---

## Power

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| OKLO | Oklo Inc. | 0001828937 | NYSE | Investing/Wiki/Sectors/Power/Nuclear & Advanced Fission/OKLO.md | — |
| TE | T1 Energy Inc. | 0001992243 | NYSE | Investing/Wiki/Sectors/Power/Nuclear & Advanced Fission/TE.md | — |
| ASPI | ASP Isotopes Inc. | 0001921865 | NASDAQ | Investing/Wiki/Sectors/Power/Nuclear & Advanced Fission/ASPI.md | — |

<!-- CANDIDATE (/map-sector 2026-05-24): VST (Vistra Energy) — Nuclear & Advanced Fission tier. Largest US competitive power generator; nuclear (Comanche Peak) + CCGT. Run /add-ticker VST --sector "Power" --layer "Nuclear & Advanced Fission" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): GEV (GE Vernova) — Gas Turbines & Grid Equipment tier. Gas turbines (GE 7F.05, HA-class); Grid Solutions HV transformers. Run /add-ticker GEV --sector "Power" --layer "Gas Turbines & Grid Equipment" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): ENR.DE (Siemens Energy) — Gas Turbines & Grid Equipment tier. HV transformers; HVDC BlueTec; switchgear. Germany-listed. Run /add-ticker ENR.DE --sector "Power" --layer "Gas Turbines & Grid Equipment" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): FLNC (Fluence Energy) — Energy Storage tier. BESS system integrator (Siemens + AES JV). Run /add-ticker FLNC --sector "Power" --layer "Energy Storage" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): BE (Bloom Energy) — Energy Storage tier. SOFC; NG + H2 compatible; data center deployments. Run /add-ticker BE --sector "Power" --layer "Energy Storage" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): CEG (Constellation Energy) — Nuclear & Advanced Fission tier. Largest US nuclear operator (21 GW). Run /add-ticker CEG --sector "Power" --layer "Nuclear & Advanced Fission" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): VICR (Vicor) — Power Semiconductors tier. Power conversion ICs for AI servers. Run /add-ticker VICR --sector "Power" --layer "Power Semiconductors" to onboard. -->

---

## Security

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| RBRK | Rubrik Inc. | 0001943896 | NYSE | Investing/Wiki/Sectors/Security/Endpoint & Cloud Security/RBRK.md | — |
| SAIL | SailPoint, Inc. | 0002030781 | NASDAQ | Investing/Wiki/Sectors/Security/Endpoint & Cloud Security/SAIL.md | — |

<!-- CANDIDATE: CRWD (CrowdStrike) — Endpoint & Cloud Security tier. Run /add-ticker CRWD --sector "Security" --layer "Endpoint & Cloud Security" to onboard. -->
<!-- CANDIDATE: PANW (Palo Alto Networks) — Endpoint & Cloud Security tier. Run /add-ticker PANW --sector "Security" --layer "Endpoint & Cloud Security" to onboard. -->
<!-- CANDIDATE: FTNT (Fortinet) — Endpoint & Cloud Security tier. Run /add-ticker FTNT --sector "Security" --layer "Endpoint & Cloud Security" to onboard. -->

---

## Edge & Physical AI

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| AMBA | Ambarella, Inc. | 0001280263 | NASDAQ | Investing/Wiki/Sectors/Edge & Physical AI/Edge Compute Module/AMBA.md | 8.0 |
| OUST | Ouster, Inc. | 0001816581 | NASDAQ | Investing/Wiki/Sectors/Edge & Physical AI/Perception Layer/OUST.md | 6.5 |
| P | Everpure Inc. (fka Pure Storage) | 0001474432 | NYSE | Investing/Wiki/Sectors/Edge & Physical AI/Perception Layer/P.md | — |

<!-- CANDIDATE: MBLY (Mobileye) — Perception Layer tier. Automotive perception AI. Run /add-ticker MBLY --sector "Edge & Physical AI" --layer "Perception Layer" to onboard. -->
<!-- CANDIDATE: BOT — Physical Systems tier. Run /add-ticker BOT --sector "Edge & Physical AI" --layer "Physical Systems" to onboard. -->

---

## Space & Comms

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| ASTS | AST SpaceMobile | 0001780530 | NASDAQ | Investing/Wiki/Sectors/Space & Comms/Satellite Constellations/ASTS.md | — |
| RKLB | Rocket Lab USA, Inc. | 0001819994 | NASDAQ | Investing/Wiki/Sectors/Space & Comms/Launch Vehicles/RKLB.md | 7.0 |

<!-- CANDIDATE (/map-sector 2026-05-24): IRDM (Iridium Communications) — Satellite Constellations tier. 66-satellite LEO constellation; L-band MSS; globally-coordinated ITU L-band spectrum. Run /add-ticker IRDM --sector "Space & Comms" --layer "Satellite Constellations" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): GSAT (Globalstar Inc.) — Satellite Constellations tier. S-band MSS; Apple Emergency SOS royalty stream; Band 53/n53 terrestrial LTE spectrum asset. Run /add-ticker GSAT --sector "Space & Comms" --layer "Satellite Constellations" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): VSAT (Viasat Inc.) — Ground Segment tier. Ka-band HTS (ViaSat-3); in-flight broadband; government satcom. Run /add-ticker VSAT --sector "Space & Comms" --layer "Ground Segment" to onboard. -->
<!-- CANDIDATE (/map-sector 2026-05-24): KTOS (Kratos Defense) — Ground Segment tier. OpenSpace satcom ground systems software; GaN T/R module defense electronics. Run /add-ticker KTOS --sector "Space & Comms" --layer "Ground Segment" to onboard. -->

---

*To add a new ticker: `/add-ticker TICKER [--sector "Sector Name"] [--layer "Layer Name"]`*

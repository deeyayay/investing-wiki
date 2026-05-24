# Monitor Registry
*The research-monitor skill reads this file on every run. Add tickers here — no skill update needed.*
*Last updated: May 24, 2026 — /map-sector Metals & Mining run; FCX + MP registered, 9 candidate stubs added*

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

---

## Clean Energy

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| OKLO | Oklo Inc. | 0001828937 | NYSE | Investing/Wiki/Sectors/Clean Energy/OKLO.md | — |
| TE | T1 Energy Inc. | 0001992243 | NYSE | Investing/Wiki/Sectors/Clean Energy/TE.md | — |

---

## Space & Comms

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| ASTS | AST SpaceMobile | 0001780530 | NASDAQ | Investing/Wiki/Sectors/Space & Comms/ASTS.md | — |
| RKLB | Rocket Lab USA, Inc. | 0001819994 | NASDAQ | Investing/Wiki/Sectors/Space & Comms/RKLB.md | — |

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

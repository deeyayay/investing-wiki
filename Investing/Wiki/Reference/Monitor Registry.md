# Monitor Registry
*The research-monitor skill reads this file on every run. Add tickers here — no skill update needed.*
*Last updated: May 24, 2026 — /map-sector Semiconductors run; candidate stubs added*

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

*To add a new ticker: `/add-ticker TICKER [--sector "Sector Name"]`*

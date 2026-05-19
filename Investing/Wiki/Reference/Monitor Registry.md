# Monitor Registry
*The research-monitor skill reads this file on every run. Add tickers here — no skill update needed.*
*Last updated: May 19, 2026 — ALAB (Astera Labs), CRDO (Credo Technology), AMKR (Amkor Technology) added to Semiconductors*

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

---

## Semiconductors

| Ticker | Company | CIK | Exchange | Path | Score |
|--------|---------|-----|----------|------|-------|
| NVDA | NVIDIA Corporation | 0001045810 | NASDAQ | Investing/Wiki/Sectors/Semiconductors/NVDA.md | — |
| MU | Micron Technology | 0000723125 | NASDAQ | Investing/Wiki/Sectors/Semiconductors/MU.md | — |
| MRVL | Marvell Technology | 0001058057 | NASDAQ | Investing/Wiki/Sectors/Semiconductors/MRVL.md | — |
| AEHR | Aehr Test Systems | 0001040896 | NASDAQ | Investing/Wiki/Sectors/Semiconductors/AEHR.md | — |
| ALAB | Astera Labs, Inc. | 0001736297 | NASDAQ | Investing/Wiki/Sectors/Semiconductors/ALAB.md | — |
| CRDO | Credo Technology Group Holding Ltd | 0001807794 | NASDAQ | Investing/Wiki/Sectors/Semiconductors/CRDO.md | — |
| AMKR | Amkor Technology, Inc. | 0001047127 | NASDAQ | Investing/Wiki/Sectors/Semiconductors/AMKR.md | — |

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

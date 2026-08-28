# Investment Watchlist
*Last updated: 2026-08-23*

**This file is the scope input for the daily pass.** `scripts/watchlist_refresh_fetch.py`
reads every ticker named in a table below and scans it for news and filings; `--all`
widens to the full registry. A ticker that is not here is not watched daily.

Themes are tracked separately in [Topics.yaml](Topics.yaml) — seven of them, covering
subjects the KB has no ticker for yet. Both feed one digest.

---

## Core Holdings (Active Positions)

> **Owner-maintained — currently empty.** Nothing else in the repo knows which of these
> names are actually held, and positions are not something to infer from a score. Fill
> this in and the daily pass will prioritise them above everything below.
>
> `Tier`: `core` · `rocket` (speculative) · `compounder`

| Ticker | Name | Tier | Thesis Summary | Score |
|--------|------|------|----------------|-------|

---

## High Conviction (scored ≥ 7.5)

*Derived from the Scoring Summary in each analysis.md. Refresh with `/dig TICKER --score`.*

| Ticker | Name | Sector | Score | One-Line Thesis |
|--------|------|--------|-------|-----------------|
| NVDA | NVIDIA Corporation | Compute Hardware | **9.5** | The dominant AI compute platform company; GPU monopoly in model training and inference with a rapidly ex… |
| SOFI | SoFi Technologies, Inc. | Application | **9.0** | Digital-native U.S. bank with a national charter; Galileo B2B platform + Financial Services Productivity… |
| SNDK | SanDisk Corporation | Memory | **8.5** | The pure-play NAND vehicle for the agentic-AI and brain-scale data wave — and the pioneer of High-Bandwi… |
| ANET | Arista Networks | Compute Hardware | **8.0** | The dominant Ethernet switching platform for hyperscaler AI clusters; as AI workloads shift from InfiniB… |
| CRDO | Credo Technology Group Hold… | Interconnect | **8.0** | Full-stack SerDes IP owner that has become the de facto AEC standard inside AI GPU clusters — FY2026 rev… |
| BRUN | Boost Run Inc. | Cloud Infrastructure | **7.5** | NVIDIA Exemplar Cloud-certified GPU neocloud (fewer than 10 globally) with 85%+ gross margins, $1.45B ta… |
| MRVL | Marvell Technology | Compute Hardware | **7.5** | Custom AI ASIC designer for hyperscalers (Google, Amazon) plus high-speed SerDes/DSP interconnect — prof… |
| AEHR | Aehr Test Systems | Semiconductor Equipment | **7.5** | Only production-ready wafer-level burn-in system at scale, pivoting from SiC/EV to AI processors — 3.5x… |

---

## Drift Watch

*Thesis drift flagged in analysis.md — these need a look before anything else.*

| Ticker | Name | Score | Drift Status |
|--------|------|-------|--------------|

---

## Active Coverage

*Thesis established, not yet high-conviction. 23 names.*

| Ticker | Name | Sector | Score | One-Line Thesis |
|--------|------|--------|-------|-----------------|
| LPK | LPKF Laser & Electronics… | Advanced Packaging | 6.5 | LPKF owns the sole industrial process for glass substrate via drilling, making it indispensabl… |
| LMND | Lemonade, Inc. | Application | — | AI-native full-stack insurer using a proprietary claims data flywheel to compress loss ratios… |
| AMZN | Amazon.com, Inc. | Cloud Infrastructure | — | AWS is the dominant AI cloud infrastructure platform, accelerating at 28% growth as proprietar… |
| GOOGL | Alphabet Inc. | Cloud Infrastructure | — | Google Cloud's 63% revenue growth and $462B backlog make Alphabet the vertically-integrated AI… |
| STX | Seagate Technology Holdin… | Cloud Infrastructure | — | The areal-density leader of the HDD duopoly — Seagate's HAMR "Mozaic" platform owns the exabyt… |
| AMD | Advanced Micro Devices, I… | Compute Hardware | — | AMD leverages Zen and CDNA architecture leadership to capture data center compute share as the… |
| INTC | Intel Corporation | Compute Hardware | 6.5 | Intel's EMIB packaging + 25-year in-house silicon photonics stack is the only IDM-foundry plat… |
| NB | NioCorp Developments Ltd. | Critical Minerals | — | The leading US development-stage source of niobium, scandium, titanium, and magnetic rare eart… |
| AVAV | AeroVironment, Inc. | Edge & Physical AI | — | The US military's primary small-drone and loitering-munitions supplier (Puma, Raven, Switchbla… |
| BRCHF | BrainChip Holdings Ltd | Edge & Physical AI | — | The only publicly listed neuromorphic pure-play — a high-risk, high-optionality call option on… |
| MBLY | Mobileye Global Inc. | Edge & Physical AI | — | Intel-controlled autonomous-driving and ADAS pure-play — the EyeQ system-on-chip, REM crowdsou… |
| 6451.TW | ShunSin Technology Holdin… | Interconnect | 5.5 | Foxconn's precision optical packaging arm — positioned to capture a structural margin step-up… |
| IPGP | IPG Photonics Corporation | Interconnect | — | The world's dominant vertically-integrated fiber-laser manufacturer; its CW and pulsed fiber l… |
| 285A.T | KIOXIA Holdings Corporati… | Memory | — | Kioxia's BiCS FLASH 3D NAND IP and Flash Ventures fab scale make it the pure-play beneficiary… |
| MU | Micron Technology | Memory | 6.5 | Only US-domiciled HBM supplier — stacked on every NVDA GPU — with structural AI demand tailwin… |
| CRWD | CrowdStrike Holdings, Inc. | Security | — | CrowdStrike is the AI-native cybersecurity platform consolidator whose Falcon data flywheel an… |
| PANW | Palo Alto Networks, Inc. | Security | — | Palo Alto Networks consolidates enterprise security into a unified AI-native platform, driving… |
| STM | STMicroelectronics N.V. | Semiconductor Foundry | — | STMicroelectronics' vertically integrated SiC power platform and STM32 MCU ecosystem lock in a… |
| XFAB | X-FAB Silicon Foundries SE | Semiconductor Foundry | 6.5 | EU's designated silicon photonics foundry for sovereign CPO supply chains — NVIDIA and Nokia c… |
| LIN | Linde plc | Semiconductor Materials | — | The world's largest industrial gas company and a quiet picks-and-shovels supplier to the leadi… |

---

## Not yet covered

42 of the 77 registered tickers have no One-Line Thesis, so they are absent above and
invisible to thesis-drift triage. A further 56 ticker pages exist on disk that the
registry does not claim at all (`python3 scripts/check_registry.py` lists them).
Run `/dig TICKER` to establish a thesis, or `/track TICKER` to register an unclaimed page.


# NVDA Ecosystem Map
*Last updated: May 7, 2026*

A structured map of companies with direct revenue, supply chain, or infrastructure relationships to NVIDIA. Organized by proximity to NVDA's core business.

---

## Tier 1 — Direct Supply Chain (Make NVDA possible)

| Ticker | Company | Relationship | Notes |
|--------|---------|-------------|-------|
| TSM / 2330.TW | TSMC | Fabricates every NVDA GPU | Most critical single dependency; 3nm/4nm CoWoS packaging |
| AMAT | Applied Materials | Supplies deposition/etch equipment to TSMC for NVDA chips | Picks-and-shovels on fab capex |
| ASML | ASML | EUV lithography machines — required for leading-edge nodes | Monopoly on EUV; no TSMC leading edge without ASML |
| KLAC | KLA Corp | Process control / inspection equipment at fabs | Every wafer that becomes an H100 passes through KLA tools |
| LRCX | Lam Research | Etch and deposition equipment | Deep TSMC relationship; benefits from CoWoS capacity expansion |
| MU | Micron | HBM3E memory stacked on every Blackwell GPU | HBM is ~30% of GPU BOM; Micron gaining share vs SK Hynix |
| AVGO | Broadcom | Custom AI ASICs (Google TPU, Meta MTIA) + networking | Dual role: NVDA competitor AND ecosystem participant via networking |

---

## Tier 2 — Infrastructure & Deployment (Run NVDA at scale)

| Ticker | Company | Relationship | Notes |
|--------|---------|-------------|-------|
| SMCI | Super Micro | Builds GPU servers and DGX-compatible rack systems | Largest NVDA ODM partner; controversial accounting history |
| VRT | Vertiv | Liquid cooling and power infrastructure for GPU clusters | Every NVL72 rack needs Vertiv-style thermal mgmt |
| ETN | Eaton | Power distribution and UPS for data centers | Grid-to-rack power chain beneficiary |
| DELL | Dell Technologies | Sells PowerEdge AI servers with NVDA GPUs | Enterprise AI server distribution play |
| HPE | Hewlett Packard Enterprise | AI server systems (Cray Supercomputers + ProLiant) | Government and HPC cluster exposure |
| CDNS | Cadence Design | EDA tools used to design NVDA chips | Design software monopoly alongside Synopsys |
| SNPS | Synopsys | EDA tools + IP cores used in GPU design | NVDA couldn't tape out without Cadence/Synopsys |

---

## Tier 3 — Networking & Interconnect (Connect NVDA clusters)

| Ticker | Company | Relationship | Notes |
|--------|---------|-------------|-------|
| MRVL | Marvell Technology | Custom AI ASICs + high-speed interconnect | Direct NVDA ecosystem + custom silicon for hyperscalers |
| CIEN | Ciena | Optical networking for data center interconnect | AI clusters need massive bandwidth between facilities |
| COHR | Coherent Corp | Optical transceivers for GPU cluster networking | 800G/1.6T transceivers are the data pipes between GPUs |
| LITE | Lumentum | Optical components; lasers inside transceivers | Upstream of COHR; laser chips inside every transceiver |
| ANET | Arista Networks | Ethernet switching inside hyperscaler AI clusters | NVDA clusters increasingly moving to Ethernet over InfiniBand |

---

## Tier 4 — Power & Energy (Feed the GPUs)

| Ticker | Company | Relationship | Notes |
|--------|---------|-------------|-------|
| CEG | Constellation Energy | Nuclear power for AI data centers | Microsoft/NVDA cluster power deals |
| VST | Vistra Energy | Power generation; data center electricity demand | AI power demand tailwind |
| OKLO | Oklo Inc. | Microreactor power for data centers | Already in portfolio; NVDA cluster power long-term |
| IREN | IREN Ltd. | Energy-efficient compute infrastructure | Already in portfolio |
| PWR | Quanta Services | Electrical infrastructure buildout for data centers | Grid connection and power delivery construction |

---

## Tier 5 — Software & Platforms (Built on NVDA)

| Ticker | Company | Relationship | Notes |
|--------|---------|-------------|-------|
| MSFT | Microsoft | Azure GPU cloud; OpenAI exclusive infra; Copilot | Largest NVDA customer by revenue |
| GOOGL | Alphabet | GCP GPU cloud; TPU alternative but still buys NVDA | Dual role: customer + competitor via TPU |
| AMZN | Amazon | AWS GPU instances (P4/P5); Trainium alternative | Same dual role dynamic |
| META | Meta | Largest single GPU buyer (400K H100s); MTIA chip | Pure AI infra spend; research + recommendation engines |
| CRWD | CrowdStrike | AI-powered cybersecurity running on GPU infra | Beneficiary of AI compute; not direct but thematically linked |

---

## Watch List Candidates from This Map
Tickers not yet in portfolio worth researching further:
- **MU** — HBM3E memory; direct NVDA BOM exposure
- **ANET** — AI networking; Ethernet switch for GPU clusters
- **MRVL** — Custom AI silicon + interconnect
- **VRT** — Liquid cooling; pure-play AI infra buildout
- **SMCI** — High risk/reward GPU server ODM

---

## Research Log
- **2026-05-07** — Ecosystem map initialized. Covers 5 tiers: supply chain, infrastructure, networking, power, and software. Cross-reference individual stock notes for deep dives.
- **2026-05-19** — Earnings Shockwave Map added from infographic sourced on NVDA Q1 FY2027 earnings day. Maps 20 companies across 7 functional categories. New tickers ALAB, CRDO, AMKR onboarded via /add-ticker.

---

## Earnings Shockwave Map — 2026-05-19
*Point-in-time earnings lens: "Which Industry Chains Will Feel the Earnings Shockwave?" Functional categorization sourced from infographic on NVDA Q1 FY2027 earnings day.*

### Foundry
| Ticker | Company | Role | Wiki Page |
|--------|---------|------|-----------|
| TSM | TSMC | Sole fabricator of NVDA GPUs; CoWoS advanced packaging | [[TSM]] |

### Packaging & Testing
| Ticker | Company | Role | Wiki Page |
|--------|---------|------|-----------|
| ASX | ASE Group | Advanced chip packaging and testing | — |
| AMKR | Amkor Technology | Advanced packaging and testing services | [[AMKR]] |

### Memory — HBM
| Ticker | Company | Role | Wiki Page |
|--------|---------|------|-----------|
| 000660.KS | SK Hynix | #1 HBM supplier; leading HBM3E/HBM4 share | — |
| MU | Micron Technology | US-domiciled HBM3E supplier; gaining share vs. Hynix | [[MU]] |
| 005930.KS | Samsung Electronics | HBM supplier; trailing in AI memory share | — |

### Memory — SSD
| Ticker | Company | Role | Wiki Page |
|--------|---------|------|-----------|
| 000660.KS | SK Hynix | Enterprise SSD for AI server storage | — |
| MU | Micron Technology | Enterprise NAND/SSD | [[MU]] |
| 005930.KS | Samsung Electronics | Enterprise SSD | — |
| SNDK | SanDisk | Consumer and enterprise SSD | — |

### Memory — HDD
| Ticker | Company | Role | Wiki Page |
|--------|---------|------|-----------|
| STX | Seagate Technology | HDD for AI training data storage | — |
| SNDK | SanDisk | Flash storage | — |
| WDC | Western Digital | HDD and enterprise SSD | — |

### Communication — Optical Module
| Ticker | Company | Role | Wiki Page |
|--------|---------|------|-----------|
| COHR | Coherent Corp | 800G/1.6T optical transceivers; NVDA strategic equity partner | [[COHR]] |
| FN | Fabrinet | Contract manufacturer for optical transceivers | [[FN]] |

### Communication — Copper Interconnect
| Ticker | Company | Role | Wiki Page |
|--------|---------|------|-----------|
| APH | Amphenol | Copper cable assemblies and connectors for AI racks | — |
| CRDO | Credo Technology | SerDes chips for copper interconnect in AI clusters | [[CRDO]] |

### Other Chips — Interconnect
| Ticker | Company | Role | Wiki Page |
|--------|---------|------|-----------|
| AVGO | Broadcom | Custom AI ASICs + networking chips | [[AVGO]] |
| ALAB | Astera Labs | PCIe/CXL interconnect retimer chips for AI servers | [[ALAB]] |
| MRVL | Marvell Technology | SerDes DSPs + custom AI ASICs for hyperscalers | [[MRVL]] |

### Other — Heat Dissipation
| Ticker | Company | Role | Wiki Page |
|--------|---------|------|-----------|
| VRT | Vertiv | Liquid cooling and power delivery for GPU clusters | [[VRT]] |

### Other — Power Supply
| Ticker | Company | Role | Wiki Page |
|--------|---------|------|-----------|
| MPWR | Monolithic Power Systems | Power management ICs for AI servers | — |
| NVTS | Navitas Semiconductor | GaN power ICs for next-gen data center PSUs | — |

### Other — PCB
| Ticker | Company | Role | Wiki Page |
|--------|---------|------|-----------|
| TTMI | TTM Technologies | Printed circuit boards for AI servers | — |

### ODM
| Ticker | Company | Role | Wiki Page |
|--------|---------|------|-----------|
| FLEX | Flex Ltd | Contract electronics manufacturing for AI servers | — |
| JBL | Jabil | Contract electronics manufacturing | — |

# Semiconductors — Supply Chain Map
*Mapped: May 24, 2026 | Anchor: packaged chip ready for electronic assembly*

---

## Framework Status
- [x] Supply chain mapped
- [ ] Nodes registered (`/add-ticker TICKER --layer "Layer"` for each below)
- [ ] Ground truth pulled (`/stock-research TICKER` per node)
- [x] Customer matrix built (`/build-customer-matrix "Semiconductors"`) — 2026-05-24
- [ ] Sector Framework written (only after above steps complete)

*Note: 7 tickers already registered (NVDA, MU, MRVL, AEHR, ALAB, CRDO, AMKR). Run `/add-ticker TICKER --layer "Layer"` to backfill the Layer field for existing names, and to onboard new candidates below.*

---

## Value Chain

| Tier | Function | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|------------|-------------------|-----------|----------------|
| Raw Materials | Purify silicon, grow wafer boules; produce specialty gases, CMP slurries, photoresists | Partial | Medium | Geographic monopoly (Japan/Germany concentrate specialty chemicals) | Medium |
| Wafer Production | Slice, polish, and certify silicon wafers to sub-nanometer flatness | Y | High | Scale + Process IP | Medium |
| EDA & Design IP | Software tools (Synopsys, Cadence) and licensable IP cores (ARM) that designers use to create chip layouts | Y | Low | Switching cost + Ecosystem | Very High |
| Lithography Equipment | Project circuit patterns onto wafers using UV/EUV light; ASML is sole EUV supplier | Y | Very High | Process IP + Geographic monopoly | Very High |
| Deposition & Etch Equipment | Deposit thin films (CVD/ALD) and etch circuit features; multiple steps per wafer | Partial | High | Process IP + Switching cost | High |
| Wafer Fabrication (Foundry) | Run wafers through 500–1,000 process steps to produce functional dies | Y | Very High | Process IP + Scale + Certification | High (cyclical) |
| Inspection & Metrology | Measure and verify each process step; catch defects before they propagate | Partial | Medium | Switching cost + Certification | High |
| Test (Wafer-Level) | Electrically test dies on the wafer before dicing; burn-in for reliability screening | Partial | Medium | Certification + Switching cost | Medium |
| Packaging (OSAT) | Dice wafers, mount dies into packages, wire-bond or flip-chip connect; advanced packaging (CoWoS, HBM stacking) is increasingly critical | Partial | High | Process IP (advanced) / Scale (legacy) | Medium |
| Final Test & Burn-In | Functional and parametric test of packaged devices; thermal stress screening | N | Low–Medium | Certification | Low–Medium |
| System Integration | Assemble chips + memory + networking into boards, modules, or complete systems | N | Low | None (commoditized assembly) | Low |

---

## Publicly-Traded Nodes

| Tier | Ticker | Company | Mkt Cap | In Registry | Notes |
|------|--------|---------|---------|-------------|-------|
| Raw Materials | 4369.T | Shin-Etsu Chemical | Large | Yes | Dominant silicon wafer supplier; also photoresist |
| Raw Materials | 5201.T | AGC Inc. | Large | Yes | Specialty glass, photomask substrates |
| Raw Materials | ICHR | Ichor Holdings | Small | No | Ultrapure gas delivery systems for fabs |
| Raw Materials | CMC | CMC Materials (Entegris sub) | — | No | CMP slurries; acquired by Entegris (ENTG) |
| Raw Materials | ENTG | Entegris | Mid | No | Specialty chemicals, filters, materials for advanced nodes |
| Wafer Production | 4043.T | Sumco Corporation | Large | Yes | #2 silicon wafer supplier globally |
| Wafer Production | SK Hynix | SK Hynix | Large | Yes | Wafer + DRAM/HBM fab (vertically integrated) |
| EDA & Design IP | SNPS | Synopsys | Large | No | #1 EDA; chip design software |
| EDA & Design IP | CDNS | Cadence Design Systems | Large | No | #2 EDA; also simulation/verification |
| EDA & Design IP | ARM | Arm Holdings | Large | No | Dominant CPU/GPU IP licensor; in nearly every chip |
| Lithography Equipment | ASML | ASML Holding | Large | Yes | Sole supplier of EUV; also DUV |
| Deposition & Etch Equipment | LRCX | Lam Research | Large | No | #1 etch and deposition equipment |
| Deposition & Etch Equipment | AMAT | Applied Materials | Large | No | Broadest equipment portfolio; deposition, CMP, implant |
| Deposition & Etch Equipment | KLAC | KLA Corporation | Large | No | #1 inspection/metrology (straddles this tier and Inspection) |
| Inspection & Metrology | KLAC | KLA Corporation | Large | No | Process control; yield management |
| Inspection & Metrology | ONTO | Onto Innovation | Mid | No | Optical metrology; advanced packaging inspection |
| Wafer Fabrication (Foundry) | TSM | Taiwan Semiconductor Mfg. | Large | Yes | #1 foundry; sole manufacturer of leading-edge nodes |
| Wafer Fabrication (Foundry) | GFS | GlobalFoundries | Mid | Yes | Mature nodes; specialty RF, automotive |
| Wafer Fabrication (Foundry) | INTC | Intel Corporation | Large | Yes | IDM + foundry (Intel 18A ramp in progress) |
| Wafer Fabrication (Foundry) | Samsung | Samsung Electronics | Large | Yes | #2 foundry + memory (vertically integrated) |
| Wafer Fabrication (Foundry) | STM | STMicroelectronics | Large | Yes | IDM; SiC power semis, automotive |
| Test (Wafer-Level) | AEHR | Aehr Test Systems | Small | Yes | Near-monopoly on wafer-level burn-in for SiC |
| Packaging (OSAT) | AMKR | Amkor Technology | Mid | Yes | #2 OSAT globally; advanced packaging (TSMC partner) |
| Packaging (OSAT) | ASX | Advanced Semiconductor Engineering | Large | No | #1 OSAT globally (ASE Group) |
| Design (Fabless — Compute) | NVDA | NVIDIA Corporation | Large | Yes | AI GPU monopoly; CUDA ecosystem |
| Design (Fabless — Compute) | AMD | Advanced Micro Devices | Large | Yes | CPU/GPU; MI-series AI accelerators |
| Design (Fabless — Compute) | AVGO | Broadcom | Large | Yes | Custom ASICs + networking silicon |
| Design (Fabless — Compute) | MRVL | Marvell Technology | Large | Yes | Custom ASICs + data infrastructure networking |
| Design (Fabless — Compute) | ARM | Arm Holdings | Large | No | CPU IP; also classifiable under EDA/IP |
| Design (Fabless — Memory) | MU | Micron Technology | Large | Yes | #3 DRAM/NAND; growing HBM share |
| Design (Fabless — Connectivity) | ALAB | Astera Labs | Mid | Yes | PCIe/CXL connectivity for AI infrastructure |
| Design (Fabless — Connectivity) | CRDO | Credo Technology | Small | Yes | High-speed SerDes for AI networking |
| Design (Fabless — Connectivity) | NXPI | NXP Semiconductors | Large | Yes | Automotive + IoT MCUs |
| Design (Fabless — Connectivity) | TXN | Texas Instruments | Large | Yes | Analog + embedded; broad industrial/auto |
| Final Test & Burn-In | COHU | Cohu Inc. | Small | No | Packaged device handlers and testers |
| Final Test & Burn-In | — | *No dominant public pure-play* | — | — | ⚠️ Structural gap — test handled in-house by IDMs or small private cos |

---

## Structural Gaps

### Gap: Raw Materials — Specialty Photoresists
No US-listed pure-play. JSR Corporation (Japan, taken private 2024) and Shin-Etsu dominate EUV photoresist. This is a genuine chokepoint: EUV photoresist is manufactured by 2–3 companies globally. **Watch for:** Any JSR re-listing, or Shin-Etsu/TOK (Tokyo Ohka Kogyo) ADR issuance.

### Gap: Final Test — Packaged Device
Cohu (COHU) exists but is small and diversified. The big test equipment names (Advantest, Teradyne) straddle wafer and final test. Advantest (6857.T) is Japan-listed and dominant for AI chip test. **Watch for:** Teradyne (TER) earnings calls — management discusses AI chip test demand explicitly.

---

## Key Questions to Answer Before Writing the Sector Framework

1. Which foundry tier wins as advanced packaging (CoWoS, HBM stacking) becomes the primary differentiator — TSMC or OSATs?
2. Which equipment tiers are most exposed to export control risk (China revenue concentration)?
3. Is the EDA duopoly (SNPS/CDNS) structurally threatened by any open-source or cloud-native alternative?
4. Where does AI-driven demand create the next capacity constraint after HBM?
5. Which raw material suppliers are most exposed to a Japan/Taiwan geopolitical disruption?

---

## Research Log
- **2026-05-24** — map-sector run. 11 tiers mapped, 6 chokepoints (Y or Partial), 2 structural gaps flagged. Already in registry: NVDA, MU, MRVL, AEHR, ALAB, CRDO, AMKR, TSM, GFS, INTC, Samsung, STM, ASML, 4043.T, 4369.T, 5201.T. Net new candidates not yet registered: SNPS, CDNS, ARM, LRCX, AMAT, KLAC, ENTG, ICHR, ONTO, ASX (6857.T), COHU, NXPI (already in registry check needed).

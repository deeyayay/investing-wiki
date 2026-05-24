# AI Buildout — Ecosystem Interrelationships
*Last updated: 2026-05-24 — Electronic Components sector map appended*

Each row is a directional dependency: **Source sector → Target sector**, documented at the process/product level. This file is the source of truth for cross-sector edges and is the data backbone for the future dashboard's flow diagram.

**Flow types:** `Material` · `Component` · `Service` · `Signal` (demand read-through, no physical transfer) · `Process` (a process from one sector executes inside another)

---

## Dependency Graph

| From Sector | From Tier | To Sector | To Tier | Flow Type | Product / Process | Chokepoint? | Notes |
|---|---|---|---|---|---|---|---|
| Materials & Mining | Silicon Refining | Semiconductors | Wafer Production | Material | Polysilicon ingot → CZ-grown boule | Yes | ~3 suppliers control >80% of semiconductor-grade silicon wafer supply (Shin-Etsu, Sumco, Siltronic) |
| Materials & Mining | Rare Earth Separation | Photonics & Optical | Epitaxial Growth | Material | Indium, Gallium, Arsenic → InGaAs/GaAs/InP epi | Partial | China controls ~60% of global rare earth separation capacity; Ga/In are byproducts of zinc/aluminum smelting |
| Materials & Mining | Rare Earth Separation | Semiconductors | Power Devices | Material | Silicon carbide precursor (SiC powder) → SiC boule growth | Yes | SiC substrate supply constrained; 4H-SiC crystal growth is slow and defect-sensitive |
| Materials & Mining | Copper Mining & Refining | Electronic Components | PCB & Substrate Mfg | Material | High-purity copper foil → PCB laminate, bus bar | Partial | Copper purity spec for signal-layer foil is tighter than structural copper; few rolling mills qualify |
| Materials & Mining | Lithium / Battery Materials | Energy & Power | Grid-Scale Storage | Material | Lithium carbonate/hydroxide → battery cathode (NMC/LFP) | Partial | Lithium carbonate supply is geographically concentrated (Li Triangle: Chile/Argentina/Bolivia) |
| Semiconductors | Power Devices | Energy & Power | Power Conversion | Component | SiC MOSFET / GaN HEMT → inverter and rectifier modules | Yes | SiC MOSFET is the only device that can efficiently switch 800V DC at high frequency; Si IGBT cannot |
| Semiconductors | Power Devices | Energy & Power | Power Conversion | Component | SiC MOSFET → HVDC rectifier module (AC→800VDC) | Yes | 800VDC data center architecture shift; each hyperscale conversion multiplies SiC demand per facility |
| Semiconductors | Power Devices | Energy & Power | Power Conversion | Component | SiC MOSFET → HVDC UPS H-bridge (no AC bypass) | Yes | HVDC UPS is a different product class from AC UPS — requires redesign by incumbent UPS vendors |
| Semiconductors | Design (Compute) | Compute Infrastructure | Server Assembly | Component | GPU / CPU / ASIC (packaged) → compute node PCB | Yes | NVDA H/B-series allocation controls data center build pace |
| Semiconductors | Design (Memory) | Compute Infrastructure | Server Assembly | Component | HBM stack / DRAM module → server memory subsystem | Yes | HBM supply bottleneck (CoWoS packaging capacity at TSMC) |
| Semiconductors | Design (Connectivity) | Compute Infrastructure | Networking | Component | SerDes PHY / PCIe / CXL chip → switch ASIC, NIC | Partial | |
| Semiconductors | Wafer Fabrication | Electronic Components | Substrate Mfg | Material | Bare die → flip-chip BGA substrate attach | No | OSAT substrate relationship; bare die is intermediate product |
| Photonics & Optical | Laser Sources | Semiconductors | Lithography Equipment | Component | EUV light source (CO2 laser-driven tin plasma) → ASML scanner | Yes | Single integrated supplier (Cymer, owned by ASML); no alternate EUV light source exists |
| Photonics & Optical | Transceiver Mfg | Compute Infrastructure | Networking | Component | 400G / 800G / 1.6T optical transceiver → spine switch port | Yes | Co-packaged optics (CPO) transition will reshape this flow; currently pluggable modules |
| Photonics & Optical | Optical Fiber & Cable | Compute Infrastructure | Networking | Material | Single-mode fiber jumper / ribbon cable → intra-DC spine | No | Corning/OFS duopoly but not a hard chokepoint at current demand levels |
| Photonics & Optical | Sensing & LIDAR | Robotics & Edge AI | Perception Layer | Component | LIDAR module / photonic sensor → robot perception stack | Partial | Solid-state LIDAR supply is concentrated in a few fabs |
| Electronic Components | MLCC | Compute Infrastructure | Server Assembly | Component | MLCC (X5R/X7R, 100V class) → server PCB BOM | Partial | Murata/TDK/Yageo order book is a leading indicator of server build rates; 3–6 month lead time |
| Electronic Components | Substrates (ABF) | Semiconductors | Packaging (OSAT) | Material | ABF (Ajinomoto build-up film) substrate → flip-chip BGA package | Yes | ABF substrate supply periodically constrains CoWoS/HBM advanced packaging throughput |
| Electronic Components | PCB & Substrate Mfg | Compute Infrastructure | Server Assembly | Material | Multi-layer PCB → server motherboard / switch board | Partial | High-layer-count PCBs (24L+) for AI servers are capacity-constrained |
| Electronic Components | Passives (Film Cap) | Energy & Power | Power Conversion | Component | 900V polypropylene film capacitor → HVDC rectifier / UPS | Partial | 800V-rated passives require different dielectric spec than 450V AC-side components; not a drop-in substitute |
| Electronic Components | Passives (Film Cap) | Compute Infrastructure | Power Distribution | Component | 900V film cap, DC arc-suppression contactor → rack PDU + server board | Partial | DC arc does not self-extinguish at zero-crossing; protection devices must be rated and tested differently |
| Energy & Power | Power Conversion | Compute Infrastructure | Power Distribution | Service | 800VDC bus → rack-level DC-DC → board power rail | Yes | 800VDC architecture shift; requires simultaneous re-spec of servers, racks, and facility power — no backward compatibility |
| Energy & Power | Grid-Scale Storage | Compute Infrastructure | Power Distribution | Service | Battery backup (AC or HVDC UPS) → uninterruptible power feed | No | Transition from AC UPS to HVDC UPS is underway; HVDC UPS is a product redesign, not an upgrade |
| Energy & Power | Thermal Management | Compute Infrastructure | Cooling | Process | Waste heat (CDU / immersion coolant loop) → facility heat rejection | No | Direct liquid cooling (DLC) and immersion are standard for >300W GPU trays; air cooling insufficient |
| Space & Communications | Satellite Connectivity | Compute Infrastructure | Edge Inference | Service | Low-latency LEO backhaul → edge AI inference node | No | Relevant for air-gapped / remote edge deployments |
| Compute Infrastructure | Demand Signal | Semiconductors | Design (Compute) | Signal | Hyperscaler GPU capex → fabless chip demand pull | No | Hyperscaler capex guidance is the primary forward indicator for NVDA/AMD/AVGO custom ASIC demand |
| Compute Infrastructure | Demand Signal | Energy & Power | Power Generation | Signal | Data center power purchase → utility-scale generation build | No | Microsoft/Google/Amazon PPA signings drive utility-scale nuclear and solar project FIDs |
| Compute Infrastructure | Demand Signal | Electronic Components | MLCC | Signal | Server build rate → MLCC volume orders | No | MLCC order book = 3–6 month leading indicator |
| Materials & Mining | Copper Mining & Refining | Electronic Components | PCB & Substrate Mfg | Material | High-purity electrolytic copper foil (9–18µm) → PCB inner layers, IC substrate SAP plating | Partial | Copper purity and foil thickness spec for signal-layer PCB is tighter than structural copper |
| Materials & Mining | Rare Earth & Specialty Metals | Electronic Components | MLCC Manufacturing | Material | Nickel powder → MLCC internal electrode; Palladium → Ag-Pd termination alloy | Partial | Ni electrode co-fire is the process that enabled base-metal MLCC; Pd exposure is legacy high-rel only |
| Materials & Mining | Rare Earth & Specialty Metals | Electronic Components | Film & Electrolytic Cap Mfg | Material | Tantalum powder → solid tantalum capacitor anode | Partial | Ta supply from conflict-mineral-regulated sources; Cabot and Global Advanced Metals are key processors |
| Electronic Components | IC Substrate Mfg | Semiconductors | Packaging (OSAT) | Material | ABF IC substrate (flip-chip BGA) → OSAT packaging line input | Yes | ABF substrate supply periodically constrains CoWoS and HBM advanced packaging throughput at TSMC/AMKR |
| Electronic Components | PCB Fabrication | Compute Infrastructure | Server Assembly | Material | Multi-layer PCB (24L+ HDI) → server motherboard / GPU board / switch board | Partial | High-layer-count AI server PCBs are capacity-constrained; TTM and Taiwanese PCB makers are key |
| Electronic Components | MLCC Manufacturing | Compute Infrastructure | Server Assembly | Component | MLCC (X5R/X7R, 100V class) → server PCB decoupling array | Partial | Murata/TDK/Yageo order book is a 3–6 month leading indicator of server build rates |
| Electronic Components | MLCC Manufacturing | Space & Communications | Satellite Bus | Component | High-rel MLCC (MIL-PRF-55681 / ESA-qualified) → satellite PCB passive decoupling | No | Space-grade MLCC is a distinct qualification; AVX/Kyocera and Vishay are primary suppliers |
| Electronic Components | Connector & Socket Mfg | Compute Infrastructure | Networking | Component | QSFP-DD / PCIe Gen 5 connector → NIC, switch, GPU server backplane | No | CPO transition may eventually eliminate pluggable transceiver connector tier |
| Electronic Components | Film & Electrolytic Cap Mfg | Energy & Power | Power Conversion | Component | 900V polypropylene film capacitor → HVDC rectifier DC bus filter; polymer Al electrolytic → UPS energy storage | Partial | 800V-rated film caps require different dielectric spec than 450V AC-side; not a drop-in substitute |
| Electronic Components | Inductor & Transformer Mfg | Energy & Power | Power Conversion | Component | Metal composite power inductor → DC-DC converter output filter stage | No | High-Isat inductors (metal composite core) required for high-frequency LLC converters in server PSUs |
| Electronic Components | PCB Assembly (EMS / PCBA) | Compute Infrastructure | Server Assembly | Component | Fully populated PCBA (motherboard, GPU board, PSU board) → server chassis integration at EMS/ODM | No | Jabil, Celestica, and Foxconn are primary AI server PCBA assemblers |
| Electronic Components | High-Frequency PCB | Photonics & Optical | Transceiver Mfg | Material | Rogers 4350B / Megtron 6 PCB → optical transceiver RF board | No | Low-loss dielectric PCB is required for 400G+ DSP signal integrity |

---

## Technology Shift Log

Structural architectural changes that affect multiple sectors simultaneously. Each shift generates new rows in the Dependency Graph above.

| Date Identified | Shift | Sectors Affected | Impact Level | Source Tiers Affected |
|---|---|---|---|---|
| 2026-05-24 | Data center power distribution migrating from AC to 800VDC bus architecture | Compute Infrastructure, Energy & Power, Semiconductors, Electronic Components | High | Power Distribution · Power Conversion · Power Devices · Passives & Protection |

---

## Maintenance

- When `/map-sector` creates or rebuilds a `_Supply Chain Map.md`, append new rows for that sector's Interrelationship Anchors here.
- When a structural technology shift is identified (e.g., via `/detect-shifts` or manual research), add rows to the Dependency Graph and log the shift in the Technology Shift Log table.
- Flow type `Signal` rows document demand read-throughs only — no physical product crosses sector boundaries.

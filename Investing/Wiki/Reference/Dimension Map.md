# AI Ecosystem — Dimension Map
*Last updated: 2026-06-25 — folder structure migrated to Layer → Tier → Ticker hierarchy. Layer folders renamed with L01–L12 prefix for sort order (e.g. `L01 Application/`). Rails remain plain names (`Power/`, `Security/`, etc.). Insurance AI nested under `L01 Application/Insurance AI/`.*

> **Canonical taxonomy moved.** The wiki now organizes the AI buildout as a **12-layer vertical stack** (Application → Critical Minerals) — mapped word-for-word from the *AI Buildout Supply Chain* blueprint graphic — wrapped by **3 cross-cutting rails** (Power / Thermal / Security) and capped by the **Edge & Physical AI deployment surface**. See **`AI Buildout Stack.md`** for the authoritative layer definitions and the machine-readable JSON the dashboard consumes. This file remains the **sector registry** (sector → folder slug → status) and the **D1–D5 → layer crosswalk** for legacy references.

---

## Sector → Layer crosswalk

The legacy five-dimension codes map onto the 12 layers as follows (full layer definitions in `AI Buildout Stack.md`):

| Legacy code | Name | Maps to layers |
|------|------|----------------|
| D5 | AI Applications | L01 Application + Edge & Physical AI deployment surface |
| D4 | AI Enablement | L02 AI Model, L03 Software Infrastructure + Security rail |
| D3 | AI Infrastructure | L04 Cloud Infrastructure + Power & Thermal rails |
| D2 | AI Connectivity | L07 Interconnect |
| D1 | AI Manufacturing Base | L05 Compute Hardware, L06 Memory, L08–L12 (packaging → minerals) |

---

## Sector Registry

Folder names now match layer names 1:1 — no slug overrides needed in the dashboard.

| Layer | Sector Folder | Stack | Status | Supply Chain Map |
|-------|---------------|-------|--------|-----------------|
| L01 | `L01 Application` | AI assistants · agents · vertical SaaS | partial | `_Supply Chain Map.md` — from Fintech & E-Commerce; run `/map-sector "Application"` to expand. Tiers: Insurance AI · AI-Native Fintech & Commerce · AI Drug Discovery · Materials Science AI |
| L02 | `L02 AI Model` | Foundation models · inference · orchestration | partial | `_Supply Chain Map.md` — from AI Model Infrastructure |
| L03 | `L03 Software Infrastructure` | ML frameworks · kernels · MLOps | planned | not yet created; run `/map-sector "Software Infrastructure"` |
| L04 | `L04 Cloud Infrastructure` | Hyperscalers · neoclouds · colocation · storage | partial | `_Supply Chain Map.md` — from AI Infrastructure |
| L05 | `L05 Compute Hardware` | GPUs · ASICs · CPUs · chip design IP | partial | see `Reference/Semiconductor Stack Supply Chain Map.md` (covers L05–L11) |
| L06 | `L06 Memory` | HBM · HBF · DRAM · NAND · LPDDR | planned | not yet created; run `/map-sector "Memory"` |
| L07 | `L07 Interconnect` | Scale-up · scale-out · scale-across · optics | partial | `_Supply Chain Map.md` — from Photonics & Optical; covers optical + SerDes |
| L08 | `L08 Advanced Packaging` | CoWoS/SoIC · HBM stacking · FC-BGA · glass core | partial | `_Supply Chain Map.md` — from Electronic Components (IC substrates) |
| L09 | `L09 Semiconductor Foundry` | Leading-edge · specialty · silicon photonics · OSAT | planned | not yet created; run `/map-sector "Semiconductor Foundry"` |
| L10 | `L10 Semiconductor Equipment` | Lithography · deposition · etch · metrology · test | planned | not yet created; run `/map-sector "Semiconductor Equipment"` |
| L11 | `L11 Semiconductor Materials` | Wafers · SOI · InP/GaAs/SiC · gases · photoresist | planned | not yet created; run `/map-sector "Semiconductor Materials"` |
| L12 | `L12 Critical Minerals` | Si · Cu · Ga · In · Ge · Hf · rare earths | partial | `_Supply Chain Map.md` — from Metals & Mining |
| Rail | `Power` | Generation → grid → rack → board | partial | `_Supply Chain Map.md` — from Clean Energy. Tiers: Nuclear & Advanced Fission · Gas Turbines & Grid Equipment · Energy Storage · Power Semiconductors |
| Rail | `Security` | Wraps every layer; identity · endpoint · network | partial | `_Supply Chain Map.md` — from Cybersecurity |
| Surface | `Edge & Physical AI` | Physical-world deployment + parallel compute | partial | `_Supply Chain Map.md` — from Robotics & Edge AI. Tiers: Edge Compute Module · Perception Layer · Actuators & Motors · Robot OS & Middleware · AI Model Training · System Integration · Fleet Management. Sub-map: `Robotics/_Supply Chain Map.md` (2026-07-01) — actuator supply chain depth; 15 new candidates |
| Cross | `Space & Comms` | Satellite constellations · launch vehicles · ground segment | partial | `_Supply Chain Map.md`. Tiers: Satellite Constellations · Launch Vehicles |
| Cross | `Electronic Components` | Passives · discretes · PCB (cross-layer; doesn't fit one L) | partial | `_Supply Chain Map.md` — moved to Advanced Packaging/ |

**Status values:**
- `complete` — supply chain map exists with Processes + Key Products columns + Interrelationship Anchors
- `partial` — supply chain map exists but missing process/product depth or anchors
- `framework-only` — narrative `_Sector Framework.md` exists but no supply chain map
- `planned` — sector defined in taxonomy, folder not yet created

---

## Stack Diagram

```
            ┌──────────────────────────────────────────────────┐
            │  L01  Application            (assistants · agents)│
            │  L02  AI Model               (foundation models)  │
            │  L03  Software Infrastructure(frameworks·kernels) │
  POWER     │  L04  Cloud Infrastructure   (hyperscalers)       │  THERMAL
  (power in)│  L05  Compute Hardware       (GPUs · ASICs · CPUs) │  (heat out)
            │  L06  Memory                 (HBM · DRAM · NAND)   │  SECURITY
            │  L07  Interconnect           (up · out · across)  │  (wraps)
            │  L08  Advanced Packaging     (CoWoS · substrates) │
            │  L09  Semiconductor Foundry  (wafer fab · OSAT)   │  EDGE &
            │  L10  Semiconductor Equipment(litho · etch · test)│  PHYSICAL AI
            │  L11  Semiconductor Materials(wafers · chemicals) │  (deployment
            │  L12  Critical Minerals & Raw Elements (bedrock)  │   surface)
            └──────────────────────────────────────────────────┘
```

Each layer **runs on** the one below it. Physical constraints flow **upward** — a chokepoint at L09 Foundry or L12 Minerals starves every layer above. Demand signals flow **downward** — an application boom at L01 pulls compute at L05, which pulls silicon at L09–L12. Three cross-cutting rails wrap the stack — **Power** comes in (left), **Heat** comes out and **Security** wraps around (right) — while **Edge & Physical AI** is the deployment surface where the stack meets the physical world (plus the parallel-compute paradigms beside it).

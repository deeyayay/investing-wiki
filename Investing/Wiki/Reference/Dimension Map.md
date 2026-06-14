# AI Ecosystem — Dimension Map
*Last updated: 2026-06-14 — "Robotics & Edge AI" renamed to "Physical AI"; sector expanded to 7-layer vertical stack.*

> **Canonical taxonomy moved.** The wiki now organizes the AI buildout as a **12-layer vertical stack** (Application → Critical Minerals) plus 4 cross-cutting rails. See **`AI Buildout Stack.md`** for the authoritative layer definitions and the machine-readable JSON the dashboard consumes. This file remains the **sector registry** (sector → folder slug → status) and the **D1–D5 → layer crosswalk** for legacy references.

---

## Sector → Layer crosswalk

The legacy five-dimension codes map onto the 12 layers as follows (full layer definitions in `AI Buildout Stack.md`):

| Legacy code | Name | Maps to layers |
|------|------|----------------|
| D5 | AI Applications | L01 Application + Edge & Physical AI rail |
| D4 | AI Enablement | L02 AI Model, L03 Software Infrastructure + Security rail |
| D3 | AI Infrastructure | L04 Cloud Infrastructure + Power & Thermal rails |
| D2 | AI Connectivity | L07 Interconnect |
| D1 | AI Manufacturing Base | L05 Compute Hardware, L06 Memory, L08–L12 (packaging → minerals) |

---

## Sector Registry

| Sector | Dimension | Folder Slug | Status | Supply Chain Map |
|--------|-----------|-------------|--------|-----------------|
| Semiconductors | D1 | `Semiconductors` | partial | `_Supply Chain Map.md` — rebuilt 2026-05-24, full process/product depth, Chip Design tier added |
| Electronic Components | D1 | `Electronic Components` | partial | `_Supply Chain Map.md` — mapped 2026-05-24, process/product depth |
| Materials & Mining | D1 | `Metals & Mining` | partial | `_Supply Chain Map.md` — mapped 2026-05-24, process/product depth |
| Photonics & Optical | D2 | `Photonics & Optical` | partial | `_Supply Chain Map.md` — mapped 2026-05-24, process/product depth |
| Space & Communications | D2 | `Space & Comms` | partial | `_Supply Chain Map.md` — mapped 2026-05-24, process/product depth |
| Compute Infrastructure | D3 | `AI Infrastructure` | partial | `_Supply Chain Map.md` — mapped 2026-05-24, process/product depth |
| Energy & Power | D3 | `Clean Energy` | partial | `_Supply Chain Map.md` — mapped 2026-05-24, process/product depth |
| Cybersecurity | D4 | `Cybersecurity` | partial | `_Supply Chain Map.md` — mapped 2026-05-24, process/product depth |
| AI Model Infrastructure | D4 | `AI Model Infrastructure` | partial | `_Supply Chain Map.md` — mapped 2026-05-31, 8-tier, process/product depth |
| Data & Software Platforms | D4 | *(reserved)* | planned | not yet created |
| Physical AI | D5 | `Physical AI` | partial | `_Supply Chain Map.md` — rebuilt 2026-06-14, 7-layer vertical stack (P07 data → P01 deployment), expanded from Robotics & Edge AI |
| Fintech & Commerce AI | D5 | `Fintech & E-Commerce` | partial | `_Supply Chain Map.md` — mapped 2026-05-24, process/product depth |
| Defense & Space | D5 | *(reserved)* | planned | not yet created |

**Status values:**
- `complete` — supply chain map exists with Processes + Key Products columns + Interrelationship Anchors
- `partial` — supply chain map exists but missing process/product depth or anchors
- `framework-only` — narrative `_Sector Framework.md` exists but no supply chain map
- `planned` — sector defined in taxonomy, folder not yet created

---

## Stack Diagram

```
            ┌──────────────────────────────────────────────────┐
            │  L01  Application            (fintech · commerce) │
            │  L02  AI Model               (foundation models)  │
            │  L03  Software Infrastructure(orchestration·MLOps)│
  POWER     │  L04  Cloud Infrastructure   (hyperscalers)       │  THERMAL
  (rail)    │  L05  Compute Hardware       (GPUs · ASICs)       │  SECURITY
            │  L06  Memory                 (HBM · DRAM · NAND)   │  EDGE &
            │  L07  Interconnect           (optics · networking) │  PHYSICAL AI
            │  L08  Advanced Packaging     (CoWoS · substrates) │  (rails)
            │  L09  Semiconductor Foundry  (wafer fab)          │
            │  L10  Semiconductor Equipment(litho · etch · test)│
            │  L11  Semiconductor Materials(wafers · chemicals) │
            │  L12  Critical Minerals & Rare Earths  (bedrock)  │
            └──────────────────────────────────────────────────┘
```

Each layer **runs on** the one below it. Physical constraints flow **upward** — a chokepoint at L09 Foundry or L12 Minerals starves every layer above. Demand signals flow **downward** — an application boom at L01 pulls compute at L05, which pulls silicon at L09–L12. The four rails (Power, Thermal, Security, Edge & Physical AI) cut across the stack rather than sitting at a single level.

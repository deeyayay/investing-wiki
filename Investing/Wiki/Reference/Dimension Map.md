# AI Ecosystem — Dimension Map
*Last updated: 2026-05-24 — Electronic Components sector mapped*

This file is the authoritative taxonomy for the five-dimension vertical stack. All sector supply chain maps and the Ecosystem Interrelationships graph reference the dimension codes here.

---

## Dimension Definitions

| Code | Name | Description |
|------|------|-------------|
| D1 | AI Manufacturing Base | Physical production of the components, materials, and devices that all higher layers consume. Constraints here propagate upward through the entire stack. |
| D2 | AI Connectivity | Moving data at the speed and distance AI requires — between chips, servers, data centers, and continents. |
| D3 | AI Infrastructure | Operating AI at scale: compute, power, cooling, and the physical facilities that house it. |
| D4 | AI Enablement | Software and security layers that make infrastructure usable and trustworthy. |
| D5 | AI Applications | End-use systems that deploy AI capability to solve domain-specific problems. |

---

## Sector Registry

| Sector | Dimension | Folder Slug | Status | Supply Chain Map |
|--------|-----------|-------------|--------|-----------------|
| Semiconductors | D1 | `Semiconductors` | partial | `_Supply Chain Map.md` — rebuilt 2026-05-24, process/product depth |
| Electronic Components | D1 | `Electronic Components` | partial | `_Supply Chain Map.md` — mapped 2026-05-24, process/product depth |
| Materials & Mining | D1 | `Metals & Mining` | partial | `_Supply Chain Map.md` — mapped 2026-05-24, process/product depth |
| Photonics & Optical | D2 | `Photonics & Optical` | partial | `_Supply Chain Map.md` — mapped 2026-05-24, process/product depth |
| Space & Communications | D2 | `Space & Comms` | framework-only | no map |
| Compute Infrastructure | D3 | `AI Infrastructure` | framework-only | no map |
| Energy & Power | D3 | `Clean Energy` | framework-only | no map |
| Cybersecurity | D4 | `Cybersecurity` | framework-only | no map |
| Data & Software Platforms | D4 | *(reserved)* | planned | not yet created |
| Robotics & Edge AI | D5 | `Robotics & Edge AI` | framework-only | no map |
| Fintech & Commerce AI | D5 | `Fintech & E-Commerce` | framework-only | no map |
| Defense & Space | D5 | *(reserved)* | planned | not yet created |

**Status values:**
- `complete` — supply chain map exists with Processes + Key Products columns + Interrelationship Anchors
- `partial` — supply chain map exists but missing process/product depth or anchors
- `framework-only` — narrative `_Sector Framework.md` exists but no supply chain map
- `planned` — sector defined in taxonomy, folder not yet created

---

## Stack Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│  D5 — AI Applications                                           │
│  Robotics & Edge AI · Fintech & Commerce AI · Defense & Space   │
├─────────────────────────────────────────────────────────────────┤
│  D4 — AI Enablement                                             │
│  Cybersecurity · Data & Software Platforms                      │
├─────────────────────────────────────────────────────────────────┤
│  D3 — AI Infrastructure                                         │
│  Compute Infrastructure · Energy & Power                        │
├─────────────────────────────────────────────────────────────────┤
│  D2 — AI Connectivity                                           │
│  Photonics & Optical · Space & Communications                   │
├─────────────────────────────────────────────────────────────────┤
│  D1 — AI Manufacturing Base                                     │
│  Semiconductors · Electronic Components · Materials & Mining    │
└─────────────────────────────────────────────────────────────────┘
```

Physical constraints flow upward. A capacity crunch at D1 propagates to D2, D3, D4, and D5 in sequence. Demand signals flow downward — AI application growth at D5 pulls compute at D3, which pulls silicon at D1.

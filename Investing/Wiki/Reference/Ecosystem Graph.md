# AI Ecosystem — Dependency Graph
*Generated 2026-05-24 from `Ecosystem Interrelationships.md` · 10 sectors · 31 unique cross-sector edges · 9 hard chokepoints*

Read this diagram bottom-to-top: physical constraints at D1 propagate upward; demand signals at D5 pull downward.

**Edge legend:**
- 🔴 Solid red arrow — hard chokepoint (Y): few producers, no near-term substitute
- 🟡 Dashed yellow arrow — partial chokepoint: geographic concentration or qualification barrier
- ⚫ Thin grey arrow — distributed / no structural bottleneck
- ↩ Return arrow — demand signal (no physical product crosses)

```mermaid
flowchart LR
    %% ── Dimension styles ──────────────────────────────────────────
    classDef d1 fill:#4a1942,color:#fff,stroke:#9d4edd,stroke-width:2px
    classDef d2 fill:#0d3b5e,color:#fff,stroke:#2196f3,stroke-width:2px
    classDef d3 fill:#1a3a1a,color:#fff,stroke:#4caf50,stroke-width:2px
    classDef d4 fill:#3a2800,color:#fff,stroke:#ff9800,stroke-width:2px
    classDef d5 fill:#1a1a3a,color:#fff,stroke:#e91e63,stroke-width:2px

    %% ── D1 — AI Manufacturing Base ─────────────────────────────────
    subgraph D1["D1 — AI Manufacturing Base"]
        MM["Materials & Mining"]:::d1
        SC["Semiconductors"]:::d1
        EC["Electronic Components"]:::d1
    end

    %% ── D2 — AI Connectivity ───────────────────────────────────────
    subgraph D2["D2 — AI Connectivity"]
        PO["Photonics & Optical"]:::d2
        SP["Space & Communications"]:::d2
    end

    %% ── D3 — AI Infrastructure ─────────────────────────────────────
    subgraph D3["D3 — AI Infrastructure"]
        CI["Compute Infrastructure"]:::d3
        EP["Energy & Power"]:::d3
    end

    %% ── D4 — AI Enablement ─────────────────────────────────────────
    subgraph D4["D4 — AI Enablement"]
        CY["Cybersecurity"]:::d4
    end

    %% ── D5 — AI Applications ───────────────────────────────────────
    subgraph D5["D5 — AI Applications"]
        RA["Robotics & Edge AI"]:::d5
        FI["Fintech & Commerce AI"]:::d5
    end

    %% ── HARD CHOKEPOINTS (Y) ────────────────────────────────────────
    MM -->|"SiC powder → boule growth [Y]"| SC
    MM -->|"NdFeB alloy → servo magnets [Y]"| RA
    MM -->|"NdFeB → PMSG wind turbine [Y]"| EP
    SC -->|"SiC MOSFET → HVDC inverter [Y]"| EP
    SC -->|"GPU/CPU/ASIC → compute node [Y]"| CI
    SC -->|"HBM CoWoS → GPU memory [Y]"| CI
    SC -->|"Jetson Orin NPU → robot edge [Y]"| RA
    PO -->|"EUV light source → lithography [Y]"| SC
    PO -->|"400G/800G transceiver → spine [Y]"| CI

    %% ── PARTIAL CHOKEPOINTS ─────────────────────────────────────────
    MM -. "REE/Ga/In → III-V epi [P]" .-> PO
    MM -. "Cu foil / REE → PCB/MLCC [P]" .-> EC
    MM -. "Li carbonate → battery cathode [P]" .-> EP
    MM -. "Al-Li / Inconel → launch vehicle [P]" .-> SP
    SC -. "Rad-hard ASIC → satellite payload [P]" .-> SP
    SC -. "GPU inference chip → fraud scoring [P]" .-> FI
    EC -. "MLCC / PCB → server assembly [P]" .-> CI
    EC -. "Film cap → HVDC rectifier [P]" .-> EP
    EP -. "Nuclear PPA → hyperscaler [P]" .-> CI

    %% ── DISTRIBUTED / NO CHOKEPOINT ────────────────────────────────
    MM --> EC
    SC --> EC
    EC --> SP
    EC --> PO
    EC --> CI
    PO --> SP
    PO --> RA
    PO --> FI
    PO --> EP
    EP --> CI
    EP --> RA
    SP --> CI
    CI --> CY
    CI --> RA
    CI --> FI
    CY --> FI
    RA --> CI
    RA --> CY
    FI --> SC
```

---

## Chokepoint Register

All hard-chokepoint edges (Chokepoint = Y), sorted by upstream dimension.

| # | From Sector | To Sector | Product / Process | Notes |
|---|-------------|-----------|-------------------|-------|
| 1 | Materials & Mining | Semiconductors | SiC powder → 4H-SiC boule growth | SiC substrate growth is slow, defect-sensitive; few suppliers |
| 2 | Materials & Mining | Robotics & Edge AI | NdFeB alloy → sintered permanent magnet → servo motor | China controls ~90% of NdFeB alloy; no western commercial-scale alt |
| 3 | Materials & Mining | Energy & Power | NdFeB → PMSG rotor → direct-drive wind turbine | ~1 tonne NdFeB per MW offshore; same China dependency |
| 4 | Semiconductors | Energy & Power | SiC MOSFET → HVDC rectifier / UPS H-bridge | Si IGBT cannot switch 800V at required frequency; hard technology gate |
| 5 | Semiconductors | Compute Infrastructure | GPU / CPU / ASIC → compute node; HBM CoWoS → GPU memory | NVDA H/B-series allocation + TSMC CoWoS capacity jointly gate server builds |
| 6 | Semiconductors | Robotics & Edge AI | Nvidia Jetson Orin / Ambarella CV3 NPU → robot edge module | Jetson Orin allocation is a gating item for humanoid and AMR production |
| 7 | Photonics & Optical | Semiconductors | EUV light source (CO2 laser-driven Sn plasma) → ASML scanner | Single integrated supplier (Cymer, owned by ASML); no alternate source |
| 8 | Photonics & Optical | Compute Infrastructure | 400G / 800G / 1.6T optical transceiver → spine switch port | CPO transition pending; current pluggable supply is concentrated |
| 9 | Electronic Components | Semiconductors | ABF (Ajinomoto build-up film) substrate → flip-chip BGA / CoWoS | ABF film: Ajinomoto sole-source (food company, ~2% rev); not investable |

---

## Sector Coverage

| Dimension | Sector | Inbound Edges | Outbound Edges |
|-----------|--------|---------------|----------------|
| D1 | Materials & Mining | 0 | 8 |
| D1 | Semiconductors | 3 | 6 |
| D1 | Electronic Components | 3 | 5 |
| D2 | Photonics & Optical | 1 | 6 |
| D2 | Space & Communications | 3 | 2 |
| D3 | Compute Infrastructure | 9 | 4 |
| D3 | Energy & Power | 5 | 2 |
| D4 | Cybersecurity | 2 | 1 |
| D5 | Robotics & Edge AI | 4 | 2 |
| D5 | Fintech & Commerce AI | 4 | 1 |

*Materials & Mining has no inbound edges — it is the physical root of the stack.*
*Cybersecurity and Fintech & Commerce AI are fully downstream — they consume but do not gate upstream production.*

# Robotics Stack — The 7 Layers of a Humanoid Robot

*Last updated: 2026-06-27 — created as a dedicated domain stack for the dashboard's Supply Chain domain switcher.*

This file is the **authoritative taxonomy** for the **Robotics** domain on the dashboard, mapped word-for-word from the *7 Layers of a Humanoid Robot* framework graphic. A humanoid robot is modeled as a **7-layer stack** from **AI Brains** (top — the robot's intelligence) down to **Energy & Rare Earth Materials** (bedrock — the fuel and raw materials in every joint and motor).

> *The winners may not be the robot makers — they may be the companies building the essential technology **inside** every robot.*

This is a **deliberately separate stack** from the 12-layer AI Buildout map (`AI Buildout Stack.md`). It renders through the same `renderL0()` engine via the dashboard's domain switcher (`STACKS["robotics"]` in `Investing/Output/Dashboard/index.html`). Unlike the AI Buildout stack, it has **no cross-cutting rails** — the humanoid framework is a clean linear stack.

**Scaffold status:** most layers reference tickers not yet onboarded to the wiki. They render as `chips` and degrade gracefully (click → "run /add-ticker" notice) until onboarded. Missing tickers are queued as CANDIDATE entries in `Monitor Registry.yaml` (`source: humanoid-robotics-framework`). Already-onboarded tickers (NVDA, OUST, AMBA, NVTS, STM, MPWR, MP, …) resolve to their existing wiki pages.

---

## The 7 Layers

| # | Layer | What it is | Companies (from the framework) |
|---|-------|------------|-------------------------------|
| L01 | **AI Brains** | The robot's intelligence | NVIDIA (Jetson · GR00T), Qualcomm (RB6) |
| L02 | **Sensors & Perception** | How the robot sees, hears, and understands the world | Ouster (lidar), Cognex (vision), Allegro (position), VPG (force) |
| L03 | **Edge AI Inference** | Real-time decision making inside the robot | Ambarella (vision SoC), CEVA (inference IP), Lattice (FPGA) |
| L04 | **Motors & Motion** | The muscles that create movement | Nidec, RBC Bearings, Regal Rexnord, AMETEK |
| L05 | **Joints & Precision Motion** | The mechanical system enabling human-like movement | Harmonic Drive, THK, Allient |
| L06 | **Power Electronics & Control** | Converting battery energy into controlled motion | Navitas, TI, Wolfspeed, Renesas, Infineon, STMicro, MPS, onsemi |
| L07 | **Energy & Rare Earth Materials** | The fuel and raw materials powering every robot | EnerSys, MP Materials, USA Rare Earth, Lynas, Energy Fuels |

---

## Machine-readable definition

The `daily-dashboard` skill copies the JSON block below verbatim into the `STACKS["robotics"].stack` assignment in `index.html`. Keep the two in sync.

```json
{
  "generated":"2026-06-27",
  "intro":"The humanoid robot as a <strong>7-layer stack</strong> — from AI brains at the top down to the rare-earth magnets in every joint. Each layer is its own supply chain. The winners may not be the robot makers — they may be the companies building the essential technology <strong>inside</strong> every robot. Click a <strong>box</strong> or a <strong>ticker</strong> to drill in.",
  "layers":[
    {"num":"01","name":"AI Brains","hue":235,"tag":"the robot's intelligence","boxes":[
      {"label":"AI Compute & Foundation Model (Jetson · GR00T)","slug":"robotics","tier":"Humanoid AI Compute","chips":["NVDA"],"fn":"Jetson platform for robotics, the GR00T humanoid foundation model, and the dominant pick in AI compute."},
      {"label":"Low-Power Robotics SoC (RB6)","slug":"robotics","tier":"Low-Power Robotics SoC","chips":["QCOM"],"fn":"Qualcomm Robotics RB6 platform — lower power than NVIDIA, with design wins in industrial robotics."}
    ]},
    {"num":"02","name":"Sensors & Perception","hue":205,"tag":"how the robot sees, hears, and understands the world","boxes":[
      {"label":"Solid-State Lidar","slug":"robotics","tier":"Lidar","chips":["OUST"],"fn":"Solid-state lidar — the leading small-cap pure-play."},
      {"label":"Industrial Machine Vision","slug":"robotics","tier":"Industrial Vision","chips":["CGNX"],"fn":"Industrial vision systems with a deeper enterprise presence."},
      {"label":"Magnetic Position Sensors","slug":"robotics","tier":"Position Sensing","chips":["ALGM"],"fn":"Magnetic position sensors — every joint needs them."},
      {"label":"Strain Gauges & Force Sensing","slug":"robotics","tier":"Force Sensing","chips":["VPG"],"fn":"Strain gauges and force sensing — a niche pure-play."}
    ]},
    {"num":"03","name":"Edge AI Inference","hue":172,"tag":"real-time decision making inside the robot","boxes":[
      {"label":"Edge Vision Processors","slug":"robotics","tier":"Edge Vision SoC","chips":["AMBA"],"fn":"Edge vision processors for automotive and robotics."},
      {"label":"DSP & AI Inference IP","slug":"robotics","tier":"Inference IP","chips":["CEVA"],"fn":"DSP and AI inference IP on a licensing model."},
      {"label":"Low-Power FPGAs","slug":"robotics","tier":"Low-Power FPGA","chips":["LSCC"],"fn":"Low-power FPGAs for sensor fusion and motor control."}
    ]},
    {"num":"04","name":"Motors & Motion","hue":138,"tag":"the muscles that create movement","boxes":[
      {"label":"Electric Motors (world's largest maker)","slug":"robotics","tier":"Electric Motors","chips":["NJDCY"],"fn":"Nidec — the world's largest motor maker. OTC: NJDCY."},
      {"label":"Precision Bearings","slug":"robotics","tier":"Bearings","chips":["RBC"],"fn":"RBC Bearings — precision components."},
      {"label":"Motors & Drives","slug":"robotics","tier":"Motors & Drives","chips":["RRX"],"fn":"Regal Rexnord — motors and drives."},
      {"label":"Precision Instruments & Motion","slug":"robotics","tier":"Precision Instruments","chips":["AME"],"fn":"AMETEK — precision instruments and motion."}
    ]},
    {"num":"05","name":"Joints & Precision Motion","hue":92,"tag":"the mechanical system that enables human-like movement","boxes":[
      {"label":"Strain Wave Gears","slug":"robotics","tier":"Strain Wave Gears","chips":["6324.T"],"fn":"Harmonic Drive Systems — the dominant strain wave gear maker (every Optimus joint uses one)."},
      {"label":"Linear Motion Bearings & Ball Screws","slug":"robotics","tier":"Linear Motion","chips":["6481.T"],"fn":"THK — linear motion bearings and ball screws."},
      {"label":"Integrated Motion Solutions","slug":"robotics","tier":"Integrated Motion","chips":["ALNT"],"fn":"Allient — integrated motion solutions, a small-cap pure-play."}
    ]},
    {"num":"06","name":"Power Electronics & Control","hue":45,"tag":"converting battery energy into controlled motion","boxes":[
      {"label":"GaN Power Semiconductors","slug":"robotics","tier":"GaN Power","chips":["NVTS"],"fn":"Navitas — GaN power semis, an asymmetric small-cap."},
      {"label":"Motor-Control MCUs","slug":"robotics","tier":"Motor Control MCUs","chips":["TXN"],"fn":"Texas Instruments — motor-control MCUs at scale."},
      {"label":"Silicon Carbide","slug":"robotics","tier":"Silicon Carbide","chips":["WOLF"],"fn":"Wolfspeed — pure-play silicon carbide."},
      {"label":"Industrial / Automotive Motor Control","slug":"robotics","tier":"Industrial Motor Control","chips":["RNECY"],"fn":"Renesas — dominant in automotive and industrial motor control."},
      {"label":"Automotive-Grade Power","slug":"robotics","tier":"Automotive Power","chips":["IFX"],"fn":"Infineon — dominant in automotive-grade power."},
      {"label":"Broad Motor-Control Portfolio","slug":"robotics","tier":"Broad Motor Control","chips":["STM"],"fn":"STMicroelectronics — broad motor-control portfolio."},
      {"label":"High-Efficiency DC-DC","slug":"robotics","tier":"DC-DC Conversion","chips":["MPWR"],"fn":"Monolithic Power Systems — high-efficiency DC-DC for compact systems."},
      {"label":"Power Management & Sensing","slug":"robotics","tier":"Power Management","chips":["ON"],"fn":"onsemi — power management and sensing."}
    ]},
    {"num":"07","name":"Energy & Rare Earth Materials","hue":350,"tag":"the fuel and raw materials powering every robot","boxes":[
      {"label":"Industrial Batteries","slug":"robotics","tier":"Batteries","chips":["ENS"],"fn":"EnerSys — industrial batteries."},
      {"label":"US Magnet Manufacturing","slug":"robotics","tier":"Magnet Manufacturing","chips":["MP"],"fn":"MP Materials — US pure-play magnet manufacturing."},
      {"label":"Rare-Earth Magnets","slug":"robotics","tier":"Rare Earth Magnets","chips":["USAR"],"fn":"USA Rare Earth — magnet manufacturing."},
      {"label":"Rare-Earth Production","slug":"robotics","tier":"Rare Earth Production","chips":["LYSCF"],"fn":"Lynas — the largest non-Chinese REE producer."},
      {"label":"Diversified Rare Earth & Uranium","slug":"robotics","tier":"Rare Earth & Uranium","chips":["UUUU"],"fn":"Energy Fuels — diversified rare earth and uranium."}
    ]}
  ],
  "connectors":[
    {"label":"perceives the world through"},
    {"label":"runs real-time inference on"},
    {"label":"issues motion commands to"},
    {"label":"actuated through"},
    {"label":"driven by"},
    {"label":"powered by"}
  ],
  "rails":[]
}
```

---

## Onboarding queue

These tickers from the framework are not yet in the wiki. They are queued as CANDIDATE entries in `Monitor Registry.yaml`. Onboard high-conviction names with `/add-ticker TICKER --sector "Robotics"` (a future pass — out of scope for the initial scaffold).

| Layer | Ticker | Company | Notes |
|-------|--------|---------|-------|
| Sensors & Perception | CGNX | Cognex | Industrial machine vision |
| Sensors & Perception | ALGM | Allegro MicroSystems | Magnetic position sensors |
| Sensors & Perception | VPG | Vishay Precision Group | Strain gauges, force sensing |
| Edge AI Inference | CEVA | CEVA Inc. | DSP / AI inference IP licensing |
| Edge AI Inference | LSCC | Lattice Semiconductor | Low-power FPGAs |
| Motors & Motion | NJDCY | Nidec (OTC ADR) | World's largest motor maker |
| Motors & Motion | RBC | RBC Bearings | Precision bearings |
| Motors & Motion | RRX | Regal Rexnord | Motors & drives |
| Motors & Motion | AME | AMETEK | Precision instruments & motion |
| Joints & Precision Motion | 6324.T | Harmonic Drive Systems | Strain wave gears (Tokyo) |
| Joints & Precision Motion | 6481.T | THK Co. | Linear motion (Tokyo) |
| Joints & Precision Motion | ALNT | Allient Inc. | Integrated motion |
| Power Electronics & Control | TXN | Texas Instruments | Motor-control MCUs |
| Power Electronics & Control | WOLF | Wolfspeed | Silicon carbide |
| Power Electronics & Control | RNECY | Renesas (OTC ADR) | Auto/industrial motor control |
| Power Electronics & Control | ON | onsemi | Power management & sensing |
| Energy & Rare Earth Materials | ENS | EnerSys | Industrial batteries |
| Energy & Rare Earth Materials | USAR | USA Rare Earth | Magnet manufacturing |
| Energy & Rare Earth Materials | LYSCF | Lynas Rare Earths (OTC ADR) | Largest non-Chinese REE producer |
| Energy & Rare Earth Materials | UUUU | Energy Fuels | Rare earth & uranium |

Already in the wiki (resolve to existing pages): **NVDA, OUST, AMBA, NVTS, STM, MPWR, MP, IFX** — note **IFX is Infineon**, so the Automotive-Grade Power chip uses IFX (not the IFNNY ADR) and resolves to the existing page. Verify exact homes in `Monitor Registry.yaml`.

---

## Maintenance

- Sub-box **labels and the 7 layer names are canonical** (verbatim from the framework graphic) — change them only if the source graphic changes.
- Keep this JSON block and `STACKS["robotics"].stack` in `index.html` in sync — `/daily-dashboard --refresh-data` regenerates the dashboard from the three stack files.
- As tickers onboard, their existing `(sector, tier)` home in `DATA.sectors` takes over the chip's drill-down automatically; no change needed here.

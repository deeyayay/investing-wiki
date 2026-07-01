# Robotics — Supply Chain Map
*Mapped: 2026-07-01 | Anchor: Humanoid & industrial robot supply chain — component manufacturers → OEM assembly → fleet operations*
*Dimension: Edge & Physical AI deployment surface (sub-sector of `Edge & Physical AI`)*

> **Scope note.** This map covers the physical/mechanical supply chain that feeds into humanoid and industrial robots. It uses the 7-tier structure already defined in the parent `Edge & Physical AI/_Supply Chain Map.md`. ADAS (Mobileye) and UAV (AeroVironment) tiers live in the parent map and are out of scope here. Upstream raw-material flows (NdFeB magnets, bearing steel, copper wire) are captured in `Ecosystem Interrelationships.md` rows from Critical Minerals and Electronic Components.

---

## Framework Status
- [x] Supply chain mapped
- [x] Process/product depth added (2026-07-01)
- [x] Interrelationship Anchors documented (2026-07-01)
- [ ] Nodes registered (`/add-ticker TICKER --sector "Edge & Physical AI"` for each below)
- [ ] Ground truth pulled (`/stock-research TICKER` per node)
- [ ] Customer matrix built (`/build-customer-matrix "Robotics"`)
- [ ] Sector Framework written (only after above steps complete)

---

## Value Chain

| Tier | Function | Processes | Key Products / Materials | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|-----------|--------------------------|------------|-------------------|-----------|----------------|
| Actuators & Motors | Converts electrical commands into precise physical motion — the single largest BOM item in a humanoid robot (40–60% of BOM per Barclays / BofA / McKinsey). Three sub-categories: (1) rotary precision reducers, (2) linear ball/roller screws, (3) frameless torque and servo motors | **Precision reducers:** harmonic drive flex spline hobbing + wave generator precision grinding; RV cycloidal disc profile grinding + pin-roller machining + gear lapping; preload/backlash measurement; 10,000-hour fatigue testing. **Linear motion:** ball screw shaft cylindrical grinding (C3/C5 pitch class, 0.01mm/300mm); ball nut raceway grinding + lapping; planetary roller screw thread milling + induction hardening; linear guide rail precision profile grinding + preload classification. **Motors:** stator lamination stamping + annealing; toroidal or distributed winding (CNC winding machine); NdFeB rotor magnet segment bonding + dynamic balancing; frameless kit assembly (stator ring + rotor ring, no housing); BLDC servo winding + resolver / encoder integration; FOC drive firmware development + EMC qualification | Harmonic drive gear unit (CSF/CSG series); RV reducer (Nabtesco RV-C / RV-E series); cycloidal gearbox; ball screw (C3/C5, Ø4–80mm); miniature ball screw (3mm lead, Ø6mm); planetary roller screw (Schaeffler PLSA); linear guide (LM rail + carriage block); frameless torque motor kit (stator ring + rotor ring); brushless servo motor (BLDC); integrated joint module (motor + reducer + encoder + F/T sensor); voice coil actuator; pneumatic soft actuator; SiC-based servo drive (48V / 400V) | Yes (reducers); Partial (ball screws, motors) | Medium | Mechanical precision / Long-qualification cycles / Process IP | Medium–High |
| Perception Layer | Provides multi-modal sensing of the physical environment (geometry, semantics, identity, force) for a robot operating in unstructured human spaces | Spinning/solid-state LIDAR point-cloud acquisition + SLAM processing; CMOS image sensor raw readout + ISP debayering; radar return processing (FMCW range-Doppler FFT); 6-DOF force-torque sensor strain gauge signal conditioning; tactile skin sensor array readout + contact localization; RGB-D structured light projection + depth map computation; sensor fusion (Kalman filter or learned fusion network); real-time 3D bounding box detection inference | Solid-state LIDAR module (Ouster OS2 / Hesai AT128); automotive-grade CMOS sensor; 77GHz radar front-end (Ti AWR); 9-DOF IMU (Bosch BNO085); Intel RealSense D435i RGB-D camera; 6-DOF force-torque sensor (ATI Nano17 / Rokubi); tactile skin patch (BeSense / Xela Robotics); time-of-flight depth sensor; multi-camera surround array | Partial | Medium | Process IP / Sensor design / ASIL safety certification | Medium–High |
| Edge Compute Module | Runs real-time perception, planning, and control inference at the robot — the "brain" of the system | GPU/NPU die selection + thermal design for fanless/sealed enclosure; LPDDR5X memory controller integration; NVMe SSD boot + log storage; power rail sequencing at board-level (48V bus → 5V/1.8V/0.9V rails); embedded Linux BSP bringup + device driver certification; EtherCAT master stack integration for deterministic actuator control; ROS 2 real-time executor latency tuning; TensorRT model compilation + INT8 quantization | Nvidia Jetson Orin NX (10–40 TOPS, key gating item for humanoid ramp); Ambarella CV3 SoC; Qualcomm RB6 GenAI module; Hailo-8 M.2 accelerator; edge TPU; SoM carrier board; EtherCAT slave controller IC (Beckhoff ET1100); LPDDR5X memory module | Yes (Jetson Orin allocation gates humanoid/AMR production) | Medium | Silicon design / Software stack / Certification | High |
| Robot OS & Middleware | Provides the software framework for sensor-actuator integration, inter-node communication, and system orchestration — the "nervous system" connecting compute to motion | ROS 2 node graph construction + QoS policy configuration; DDS middleware (Fast DDS / Cyclone DDS) domain configuration; URDF kinematic model authoring + joint limit enforcement; hardware abstraction layer (HAL) implementation per actuator driver; real-time executor (rclcpp) latency tuning; safety PLC integration (ISO 13849 Category 3/PLd SIL 2); EtherCAT master cycle time optimization (<1ms deterministic loop); whole-body controller (WBC) and model predictive control (MPC) implementation | ROS 2 Humble/Jazzy distribution; Nav2 navigation stack; MoveIt 2 manipulation planner; micro-ROS (bare-metal MCU); Isaac ROS (GPU-accelerated ROS 2 nodes); DDS transport layer; OROCOS real-time kernel; safety-rated I/O module (Pilz PNOZ / Sick FLEXI) | No | Low | Ecosystem / Developer lock-in | Low–Medium |
| AI Model Training & Deployment | Trains perception, manipulation, and language-conditioned task models; deploys quantized versions to edge hardware via OTA | Simulation-to-real (sim2real) domain randomization in Isaac Sim / Mujoco / Genesis; imitation learning from human teleoperation demonstrations (kinesthetic teaching + VR haptic replay); reinforcement learning policy training (PPO / SAC / TD-MPC2 on GPU cluster); robot foundation model pre-training on large multimodal corpora (video + proprioception + language); model quantization (INT8 / FP16) + TensorRT engine compilation; OTA model update orchestration + rollback; A/B policy evaluation in production fleet | Isaac Sim synthetic dataset; imitation learning demonstration corpus (teleop recordings); robot foundation model checkpoint (π₀ / OpenPI / Figure Neural Network); trained manipulation policy (ACT / Diffusion Policy); TensorRT engine file; OTA update package; sim2real transfer evaluation suite | Partial | Medium | Proprietary training data / Cloud training infrastructure | High |
| System Integration & OEM Assembly | Integrates subsystems (actuators, compute, perception, power) into a deployable robot and validates end-to-end system behavior — the OEM tier. Currently dominated by private companies | Mechanical CAD assembly with interference checking + tolerance analysis; robot calibration (hand-eye calibration, DH parameter identification); safety function integration (IEC 62443, ISO 10218, ISO 13849 PLd); EMC testing (FCC Part 15 / CE / MIC); field reliability test (MTBF target >10,000 hours); application-specific software customization; battery management system (BMS) integration (LiFePO4 / NMC 48V pack); final functional acceptance test | Humanoid robot chassis (aluminium + CFRP frame); AMR (autonomous mobile robot) base; collaborative robot arm (6/7-DOF); edge AI appliance enclosure; safety-rated I/O module; 48V LiFePO4 battery pack + BMS; cable harness; custom joint torque sensor; gripping end-effector | No | High | Systems engineering / Application knowledge / Safety certification | Low–Medium |
| Fleet Management & Operations Platform | Monitors and manages deployed robot fleets across sites in real time — the SaaS layer that generates recurring revenue from deployed hardware | Mission dispatch and scheduling (OSRF Fleet Adapter / VDA5050 protocol); remote teleoperation fallback via low-latency video stream (WebRTC, <50ms RTT); OTA firmware + model update orchestration with rollback; anomaly detection on joint torque, temperature, and sensor health telemetry; digital twin fleet simulation for predictive maintenance; OT/IT network segmentation and access control; utilization reporting and ROI dashboarding for enterprise customers | Fleet management SaaS; VDA5050-compliant traffic controller; remote teleop station (haptic gloves + VR headset); OTA update server; robot telemetry dashboard; digital twin simulation environment; predictive maintenance alert engine | No | Low | Data network effects / Switching cost | High |

---

## Publicly-Traded Nodes

| Tier | Ticker | Company | Exchange | Mkt Cap | In Registry | Notes |
|------|--------|---------|----------|---------|-------------|-------|
| Actuators & Motors — Precision Reducers | 6324.T | Harmonic Drive Systems | TSE Tokyo | Mid | No | Harmonic reducers (CSF/CSG series) for wrist, elbow, and shoulder joints; key pure-play |
| Actuators & Motors — Precision Reducers | 6268.T | Nabtesco | TSE Tokyo | Large | No | RV/cycloidal reducers for high-torque joints (hip, shoulder); dominant RV share |
| Actuators & Motors — Precision Reducers | TKR | Timken | NYSE | Large | No | Cycloidal/worm gearing + Rollon linear motion; US-listed |
| Actuators & Motors — Precision Reducers | 2049.TW | Hiwin Technologies | TWSE | Mid | No | Ball screws + linear guides + harmonic drives; Taiwan-listed |
| Actuators & Motors — Linear Motion | 6481.T | THK | TSE Tokyo | Large | No | Ball screws + linear guides; global leader |
| Actuators & Motors — Linear Motion | 6471.T | NSK | TSE Tokyo | Large | No | Ball screws + precision bearings |
| Actuators & Motors — Linear Motion | SKF-B | SKF | Nasdaq Stockholm | Large | No | Roller screws + precision bearings; Sweden |
| Actuators & Motors — Linear Motion | SFFLY | Schaeffler | Frankfurt / OTC | Large | No | Planetary roller screws + developing rotary actuators; Germany |
| Actuators & Motors — Linear Motion | AME | AMETEK | NYSE | Large | No | Ball screws + compact linear actuators; US pure-play |
| Actuators & Motors — Servo Motors | 6594.T | Nidec | TSE Tokyo | Large | No | BLDC/servo motors + reducers; integrated joint modules |
| Actuators & Motors — Servo Motors | RRX | Regal Rexnord | NYSE | Large | No | Frameless torque motors + ball screw / linear actuators |
| Actuators & Motors — Servo Motors | MOG.A | Moog | NYSE | Large | No | Frameless motors + electromechanical rotary/linear actuators |
| Actuators & Motors — Servo Motors | PH | Parker Hannifin | NYSE | Large | No | Frameless servo motors + electromechanical actuators |
| Actuators & Motors — Servo Motors | ALNT | Allient (Allied Motion) | NASDAQ | Small | No | Frameless + servo motors, drives, integrated motion modules |
| Actuators & Motors — Servo Motors | NOVT | Novanta | NASDAQ | Mid | No | Frameless direct-drive motors + precision encoders |
| Perception Layer | OUST | Ouster | NYSE | Small | Yes | Solid-state LIDAR (OS2 series); primary robot LIDAR supplier |
| Perception Layer | 6965.T | Hamamatsu Photonics | TSE Tokyo | Mid | Yes | Photonic sensors, ToF sensors, CMOS arrays |
| Perception Layer | LASR | nLIGHT | NASDAQ | Small | Yes | Fiber laser light sources for structured-light depth sensors |
| Edge Compute Module | NVDA | NVIDIA | NASDAQ | Mega | Yes | Jetson Orin NX — primary robot edge inference platform; allocation gates ramp |
| Edge Compute Module | AMBA | Ambarella | NASDAQ | Mid | Yes | CV3 SoC for vision-heavy robot platforms |
| Edge Compute Module | BRCHF | BrainChip Holdings | OTC / ASX | Small | Yes | Neuromorphic (Akida) NPU for ultra-low-power robot reflex |
| Robot OS & Middleware | — | *No pure-play public player* | — | — | — | ⚠️ Structural gap — ROS 2 is open-source; only integration/service revenue, not product |
| AI Model Training & Deployment | NVDA | NVIDIA | NASDAQ | Mega | Yes | Isaac Sim + Isaac Lab + GPU cluster for robot foundation model training |
| System Integration & OEM Assembly | — | *No pure-play public player* | — | — | — | ⚠️ Structural gap — all major humanoid OEMs are private (Figure ~$39B, Physical Intelligence ~$5.6B, Apptronik ~$5.5B, Boston Dynamics); TSLA/AMZN/AAPL have robotics buried in conglomerate revenue |
| Fleet Management & Operations Platform | — | *No pure-play public player* | — | — | — | ⚠️ Structural gap — fleet software revenue is nascent; closest analogues are private (Formant, Inorbit) or embedded in OEM platforms |

---

## Structural Gaps

**Robot OS & Middleware — No public pure-play.** ROS 2 is maintained by Open Robotics (non-profit) and PickNik (private). The safety-rated PLC layer (Pilz, Sick, Bosch Rexroth) is embedded within diversified industrials. Watch for: (1) a commercial ROS 2 distribution company (Intrinsic/Google spinout, Locus Robotics) that IPOs as fleet scale grows, or (2) a cloud-native robot orchestration SaaS that separates from OEMs.

**System Integration & OEM Assembly — No US-listed pure-play humanoid.** Tesla Optimus, Amazon Sequoia, Figure, Physical Intelligence, Apptronik, Boston Dynamics, and Agility Robotics are either private or buried inside mega-cap legacy revenue. The investable thesis per the Paradis Labs framework (May 2026) is that the component supply chain — specifically Tier 1 (Actuators & Motors) — is the right entry point today, not the OEM. Watch for: a Figure AI or Physical Intelligence IPO post-H1'28 volume ramp.

**Fleet Management & Operations Platform — No public pure-play.** Formant, Inorbit, Phantom Auto, and Sanctuary AI are all private. This tier likely monetizes via SaaS per-robot per-month licensing at scale — the highest-margin tier in the stack once fleets reach hundreds of units per customer. Watch for: an Inorbit or Formant SPAC or IPO as enterprise customers scale past 100-robot sites.

---

## Key Questions to Answer Before Writing the Sector Framework

1. **Reducer chokepoint durability:** China dominates actuator reducer supply — will Japanese (Harmonic Drive, Nabtesco) or Taiwanese (Hiwin) capacity be sufficient to supply the BofA-estimated 1M annual humanoid units by 2035 without a China-equivalent supply chain emerging in the West?
2. **Jetson Orin availability:** NVDA Jetson Orin allocation is cited as a near-term gating item for humanoid and AMR production. At what GPU cluster revenue level does this become a permanent bottleneck vs. a manageable ramp constraint?
3. **BOM evolution:** The 40–60% actuator BOM share assumes current servo motor + harmonic reducer architecture. If the field converges on direct-drive (no reducer) designs as motor efficiency improves, the reducer tier collapses — does this change the investment thesis for 6324.T and 6268.T?
4. **H1'28 volume ramp timing:** Multiple sell-side institutions (BofA, BCG) cite ~H1'28 as the commercial humanoid ramp. What are the leading indicators (OEM backlog, Tier 1 capex announcements, Jetson Orin order flow) to track for confirmation or delay?
5. **NdFeB magnet supply risk:** China controls ~90% of NdFeB alloy production. MP Materials (MP) is building US magnet manufacturing — will it be operational at scale before the ~H1'28 ramp? What is the fallback if Western supply is insufficient?
6. **ROI threshold:** Goldman Sachs projects humanoid unit price falling from ~$100K to ~$25K by 2030. At what unit price does enterprise ROI become unambiguous (vs. human labor) in key verticals — logistics, healthcare, construction — and how do current pilot deployments track against that threshold?

---

## Interrelationship Anchors

### Inputs (this sector consumes from)
| From Sector | From Tier | Product / Signal |
|---|---|---|
| Critical Minerals (L12) | Rare Earth Separation | NdFeB sintered magnet (Nd-Pr-Dy alloy) → BLDC servo motor rotor + voice coil actuator |
| Critical Minerals (L12) | Copper Mining & Refining | Enameled copper magnet wire → stator winding; copper foil → motor PCB |
| Critical Minerals (L12) | Specialty Metals | Bearing steel (M50 / AISI 52100) → precision reducer races and rolling elements |
| Semiconductor Materials (L11) | SiC Precursor | SiC MOSFET / GaN HEMT → servo drive power stage (SiC-based VFD) |
| Compute Hardware (L05) | Edge AI SoC | Jetson Orin NX / Ambarella CV3 → robot edge compute module |
| Interconnect (L07) | Photonic Sensing | Solid-state LIDAR (Ouster OS2) / photonic depth sensor → robot perception stack |
| Cloud Infrastructure (L04) | GPU Cluster | Isaac Sim sim2real + imitation learning + RL policy training → trained robot models |
| AI Model (L02) | Foundation Model | π₀ / OpenPI / Gemini Robotics weights + inference API → robot language instruction following + long-horizon planning |
| Power (Rail) | Motor Drive Electronics | SiC-based VFD / servo drive → joint actuator torque control |
| Electronic Components (L08) | MLCC + Passive | High-frequency MLCC + power inductor → servo drive PCB decoupling |

### Outputs (this sector supplies to)
| To Sector | To Tier | Product / Signal |
|---|---|---|
| Cloud Infrastructure (L04) | Demand Signal | Robot AI training workloads → GPU cloud demand pull (Isaac Sim, foundation model fine-tuning) |
| AI Model (L02) | Training Data | Robot teleoperation demonstration corpus + proprioception-language logs → foundation model training data |
| Security (Rail) | Security Operations | Robot fleet OT telemetry + OTA update logs → XDR / NDR monitoring for anomaly detection in converged OT/IT networks |
| Power (Rail) | Demand Signal | Large humanoid fleet deployment → industrial site power infrastructure upgrade demand |

---

## Research Log
- **2026-07-01** — map-sector run. 7 tiers, 2 chokepoints (Actuators/Reducers partial + Edge Compute Yes), 3 structural gaps (OS/Middleware, OEM Assembly, Fleet Software). New candidates not yet in registry: 6324.T · 6268.T · TKR · 2049.TW · 6481.T · 6471.T · SKF-B · SFFLY · AME · 6594.T · RRX · MOG.A · PH · ALNT · NOVT.
- **Source:** Paradis Labs @ParadisLabs X article (2026-05-29), stored at `Investing/Raw/Sentiment/2026-05-29-paradislabs-robotics-humanoid-supply-chain.md`

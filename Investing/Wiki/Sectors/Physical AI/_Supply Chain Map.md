# Physical AI — Supply Chain Map
*Mapped: 2026-06-14 | Anchor: Embodied AI systems — autonomous robots, vehicles, drones, and space platforms*
*Dimension: D5 — AI Applications (Edge & Physical AI rail)*

---

## Framework Status
- [x] Supply chain mapped
- [x] Process/product depth added (2026-06-14)
- [x] Interrelationship Anchors documented (2026-06-14)
- [ ] Nodes registered (`/add-ticker TICKER --sector "Physical AI"` for each below)
- [ ] Ground truth pulled (`/stock-research TICKER` per node)
- [ ] Customer matrix built (`/build-customer-matrix "Physical AI"`)
- [ ] Sector Framework written (only after above steps complete)

*Prior version (2026-05-24): 7-tier flat structure for "Robotics & Edge AI". Rebuilt 2026-06-14 as a 7-layer vertical dependency stack (P07 data → P06 training → P05 simulation → P04 edge compute → P03 perception → P02 actuation → P01 deployment) to reflect sector expansion into simulation, embodied AI training, and deployment platforms (AVs, eVTOL, space).*

---

## Value Chain

| Tier | Function | Processes | Key Products / Materials | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|-----------|--------------------------|------------|-------------------|-----------|----------------|
| P07 Real-World Data & Annotation | Capture, label, and curate real-world interaction datasets to train and fine-tune embodied AI models | Teleoperation data recording (wrist cameras, force-torque sensors), point-cloud labeling and semantic segmentation annotation, trajectory extraction and QA filtering, natural-language instruction pairing, dataset versioning and deduplication | Robot sensor logs (camera, LIDAR, IMU), annotated 3D point clouds, demonstration trajectories, NL instruction–action pairs, RLDS-format dataset | Partial | Low | Data network effects | Medium |
| P06 Embodied AI Training | Train the AI policies (perception → planning → action) running on physical machines using foundation models, imitation learning, and RL | Vision-language-action (VLA) pre-training on multi-modal corpora, sim-to-real transfer (Isaac Lab / Habitat), behavior cloning from human demos, PPO/SAC RL policy optimization, INT8 quantization and TensorRT compilation, OTA policy update and rollback | Foundation model checkpoints (GR00T, RT-2, Llama-Robotics), distilled on-device policies, reward models, PyTorch training run on H100 cluster | N | Low–Medium (software) | Data + Compute access | Very High (model layer) |
| P05 Simulation & Synthetic Data | Generate physics-accurate synthetic training data and validate system behavior without expensive real-world collection | Multi-physics simulation (rigid body, fluid, electromagnetic, sensor noise), photorealistic ray-traced rendering, domain randomization across lighting and texture, procedural environment generation, sim-to-real gap measurement and domain adaptation | Synthetic LIDAR point clouds, photorealistic camera frames with GT labels, physics-accurate torque trajectories, domain-randomized Isaac Sim environments | N | Low–Medium | Ecosystem (platform lock-in) | High (software) |
| P04 Edge Compute & Inference | Run perception, planning, and control inference on-device under strict power (<20 W) and latency (<10 ms) budgets | Neural network compilation (TensorRT, ONNX), INT8/INT4 quantization, sparse inference kernel optimization, sensor pre-processing on NPU, real-time OS scheduling (QNX, RT-Linux), hardware-in-the-loop (HIL) test certification | Ambarella CV3-AD SoC, NVIDIA Jetson AGX Orin / Thor module, Qualcomm RB5 / Snapdragon Ride, Hailo-8 M.2 NPU, SoM carrier board | Y | Medium | Silicon + Software ecosystem | Very High |
| P03 Perception & Sensing | Give machines spatial and semantic awareness of their environment | LIDAR point-cloud acquisition (pulsed ToF / FMCW), stereo vision depth estimation, radar CFAR detection and range-Doppler FFT, IMU fusion (EKF/UKF), multi-sensor extrinsic calibration, real-time 3D object detection and tracking (BEV / PointPillars) | Ouster OS2-128 LIDAR module, Mobileye EyeQ7 SoC + camera array, Continental ARS630 radar, Bosch BMI088 IMU, photonic CMOS arrays, time-of-flight sensor | Partial | Medium | Process IP + Certification | Medium–High |
| P02 Actuation & Motion Control | Convert digital torque commands into precise physical motion across joints, wheels, and flight surfaces | BLDC motor winding and lamination, harmonic/cycloidal drive gear machining and preload setting, FOC/SVM motor control loop tuning, absolute encoder calibration (EnDat/BiSS), SiC VFD power stage design, force-torque sensor integration | Nidec BLDC servo motor, Harmonic Drive SHA-CG unit, Parker EMC series electromechanical actuator, SiC-based 400V VFD module, absolute magnetic encoder | Partial | High | Process IP + Scale | Medium |
| P01 Deployment Platforms | Integrate all upstream tiers into a deployable autonomous machine and validate system-level behavior | System-level integration and calibration, BIL/HIL testing, functional safety analysis (HARA/FMEA per ISO 13849 / ISO 26262 / DO-178C), regulatory certification (FMVSS, FAA Part 135, EASA SC-VTOL), OTA update infrastructure rollout, fleet management software deployment | Humanoid robot platform (Optimus Gen 2, Atlas), L2+/L3 AV (EyeQ SuperVision), eVTOL airframe (Joby S4), LEO spacecraft bus (Neutron), AMR platform (Spot, OTTO 1500) | Partial | High | Systems engineering + Ecosystem | Medium (early stage) |

---

## Publicly-Traded Nodes

| Tier | Ticker | Company | Mkt Cap | In Registry | Notes |
|------|--------|---------|---------|-------------|-------|
| P07 Data & Annotation | — | *No liquid public player* | — | — | ⚠️ Structural gap: Scale AI (private ~$25B), Labelbox (private), Appen (APX:ASX micro-cap losing share) |
| P06 Embodied AI Training | META | Meta Platforms | Large | No | Open Llama robotics models; PyTorch; FAIR embodied AI research (EgoTopo, Habitat) |
| P06 Embodied AI Training | GOOGL | Alphabet | Large | No | RT-2 / Gemini Robotics VLA from DeepMind; AutoRT data collection at scale |
| P06 Embodied AI Training | NVDA | NVIDIA Corporation | Large | Yes (Semiconductors) | GR00T robot foundation model; Isaac Lab training environment |
| P05 Simulation | NVDA | NVIDIA Corporation | Large | Yes (Semiconductors) | Omniverse / Isaac Sim — dominant robot and AV simulation platform |
| P05 Simulation | ANSS | Ansys, Inc. | Large | No | Multi-physics simulation for robot component and system validation; being acquired by Synopsys |
| P04 Edge Compute | AMBA | Ambarella, Inc. | Small | Yes | CV3-AD SoC; <20 W GPU-class perception; default edge AI chip at scale |
| P04 Edge Compute | NVDA | NVIDIA Corporation | Large | Yes (Semiconductors) | Jetson AGX Orin / Thor; allocation gates humanoid robot production ramp |
| P04 Edge Compute | QCOM | Qualcomm | Large | No | RB5 robotics platform; Snapdragon Ride automotive compute |
| P03 Perception | OUST | Ouster, Inc. | Small | Yes | Digital LIDAR; CMOS photonic array; solid-state; Pentagon Blue UAS approved |
| P03 Perception | MBLY | Mobileye Global | Large | No | EyeQ SoC + camera; highest-volume AV perception platform in production; ~3B units shipped |
| P03 Perception | CGNX | Cognex Corporation | Mid | No | Machine vision leader for industrial automation and robotic bin-picking |
| P02 Actuation | 6594.T | Nidec Corporation | Large | No | World's largest precision motor maker; ~45% of industrial servo motor volume |
| P02 Actuation | PH | Parker Hannifin | Large | No | Linear and electromechanical actuators; motion and control; 13,000+ motion products |
| P01 Deployment | TSLA | Tesla, Inc. | Large | No | Optimus humanoid robot + FSD; vertically integrates AI training, chip design, and deployment |
| P01 Deployment | JOBY | Joby Aviation | Small | No | eVTOL air taxi; Toyota-backed; FAA Part 135 certification in process |
| P01 Deployment | RKLB | Rocket Lab USA | Small | Yes (Space & Comms) | Launch vehicle + satellite bus; physical AI at the edge of Earth |

---

## Structural Gaps

**P07 — Real-World Data & Annotation:** No liquid US-listed company dominates robot training data. Scale AI (~$25B private) is the market leader. The winner will have proprietary teleoperation datasets from deployed fleets — TSLA's Optimus demo data and FSD shadow mode fleet are the most valuable embodied AI dataset in existence, but inaccessible to outside investors. Watch for Appen (APX:ASX) as the only public proxy, though it is losing share.

**P02 — Precision Harmonic Drives:** Harmonic Drive Systems (6324.T, Tokyo) is the dominant supplier of strain-wave gears used in every robot joint requiring high torque density in a compact form factor. Each Optimus humanoid uses ~11 harmonic drive joints. No US-listed company occupies this niche — a structural chokepoint for humanoid scaling that has no near-term substitute technology.

**P06 — Embodied AI Foundation Model Labs:** The most advanced labs are private: Physical Intelligence (pi.ai), 1X Technologies, Agility Robotics (Amazon-owned), Boston Dynamics (Hyundai-owned), Figure AI. NVDA (GR00T), META (Llama-Robotics), and GOOGL (Gemini Robotics) are the best-positioned public proxies, but none are pure-play embodied AI.

---

## Key Questions to Answer Before Writing the Sector Framework

1. **Who owns the data flywheel?** Tesla fleet telemetry vs. Scale AI annotation pipelines vs. NVDA Isaac Lab synthetic data — which training data source wins for generalist robot policies?
2. **Does edge compute consolidate around Jetson or fragment?** NVDA Jetson Orin dominates today. Can AMBA CV3-AD or QCOM RB5 take meaningful AV and AMR share as Jetson supply tightens?
3. **What breaks first in humanoid scaling?** NdFeB magnets (rare earth chokepoint), harmonic drives (6324.T bottleneck), or Jetson Orin allocation (NVDA capacity)?
4. **Is simulation sufficient for dexterous manipulation?** The sim-to-real gap for fine manipulation remains unsolved. NVDA Omniverse (synthetic data at scale) vs. Physical Intelligence (real-world demos at scale) represent competing approaches.
5. **Does space belong inside Physical AI or as a separate sector?** RKLB and ASTS are in Space & Comms. As satellite autonomy matures, the boundary may need revisiting.

---

## Interrelationship Anchors

### Inputs (Physical AI consumes from)

| From Sector | From Tier | Product / Signal |
|---|---|---|
| Materials & Mining | Rare Earth Separation | Nd₂O₃, Pr₆O₁₁, Dy₂O₃ → NdFeB sintered magnet → BLDC servo motor, harmonic drive voice coil |
| Semiconductors | Chip Design (Edge AI) | Ambarella CV3-AD, NVDA Jetson Orin SoC → edge compute module |
| Photonics & Optical | Sensing & LIDAR | LIDAR module (Ouster OS2, Hesai AT128) → robot 3D point-cloud perception |
| Energy & Power | Power Electronics | SiC VFD (400V–800V, 4kW–1MW) → robot joint servo motor torque control |
| AI Model Infrastructure | Foundation Model Development | Foundation model weights (Llama-Robotics, Gemini Nano, Phi-3) → robot perception pipeline |
| Compute Infrastructure | AI Compute Service | GPU cluster (Isaac Sim, Isaac Lab, imitation learning) → trained robot policies |
| Space & Comms | Satellite Connectivity | LEO IoT messaging (Iridium SBD, ASTS NTN) → robot telemetry in GNSS-denied environments |

### Outputs (Physical AI supplies to)

| To Sector | To Tier | Product / Signal |
|---|---|---|
| Compute Infrastructure | Demand Signal | Robot foundation model training workloads → GPU cluster capex demand pull |
| Cybersecurity | Security Operations | Robot fleet OT telemetry + OTA update logs → XDR / NDR monitoring for converged OT/IT |
| Semiconductors | Demand Signal | Humanoid robot production ramp → edge AI SoC volume orders (AMBA CV3, Jetson Orin) |

---

## Research Log
- **2026-06-14** — Sector restructured from "Robotics & Edge AI" (2026-05-24 map, 7-tier flat) to "Physical AI" with a 7-layer vertical dependency stack (P07→P01). Expanded scope: added simulation (P05), embodied AI training (P06), data annotation (P07), and broadened deployment platforms (P01) to include AVs, eVTOL, and space. 10 public nodes identified: 2 already in registry (AMBA, OUST); 8 new candidates (META, GOOGL, NVDA cross-listed, ANSS, QCOM, MBLY, CGNX, 6594.T, PH, TSLA, JOBY). 3 structural gaps: data annotation, harmonic drives, embodied AI labs.

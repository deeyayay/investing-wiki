# Robotics & Edge AI — Supply Chain Map
*Mapped: 2026-05-24 | Anchor: Embodied AI systems — autonomous robots, edge inference, perception hardware*
*Dimension: D5 — AI Applications*

---

## Framework Status
- [x] Supply chain mapped
- [x] Process/product depth added (2026-05-24)
- [x] Interrelationship Anchors documented (2026-05-24)
- [ ] Nodes registered (`/add-ticker TICKER --layer "Layer"` for each below)
- [ ] Ground truth pulled (`/stock-research TICKER` per node)
- [ ] Customer matrix built (`/build-customer-matrix "Robotics & Edge AI"`)
- [ ] Sector Framework written (only after above steps complete)

---

## Value Chain

| Tier | Function | Processes | Key Products / Materials | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|-----------|--------------------------|------------|-------------------|-----------|----------------|
| Perception Layer | Provides multi-modal sensing of the physical environment (geometry, semantics, identity) | Spinning/solid-state LIDAR point cloud acquisition and SLAM processing, CMOS image sensor raw pixel readout and ISP debayering, radar return processing (FMCW range-Doppler FFT), sensor fusion (kalman filter or learned fusion network), real-time 3D bounding box detection inference | Solid-state LIDAR module (Ouster OS2, Hesai AT128), automotive-grade CMOS sensor, 77GHz radar front-end, 9-DOF IMU, time-of-flight depth sensor, multi-camera surround array | Partial | Medium | Process IP / Sensor design | Medium–High |
| Edge Compute Module | Runs real-time perception, planning, and control inference at the robot or device | GPU/NPU die selection and thermal design for fanless operation, LPDDR5X memory controller integration, NVMe SSD boot and log storage, power rail sequencing at board level, embedded Linux BSP bringup and device driver certification | Nvidia Jetson Orin NX, Ambarella CV3 SoC, Qualcomm RB6 GenAI module, Hailo-8 M.2 accelerator, edge TPU, SoM carrier board | Partial | Medium | Silicon design / Software stack | High |
| Actuators & Motors | Converts electrical commands into precise physical motion | Field-oriented control (FOC) algorithm execution on motor driver MCU, encoder signal decoding (sin/cos or EnDat absolute), harmonic drive gear reduction assembly and preload setting, force-torque sensor calibration, brushless servo winding and stator assembly | Brushless servo motor (BLDC), harmonic drive gear unit, planetary gearbox, hollow-shaft encoder, force-torque sensor, voice coil actuator, pneumatic soft actuator | No | Medium | Mechanical precision / Application-specific | Medium |
| Robot OS & Middleware | Provides the software framework for sensor-actuator integration, inter-node communication, and system orchestration | ROS 2 node graph construction and QoS policy configuration, DDS middleware (Fast DDS / Cyclone DDS) domain configuration, URDF kinematic model authoring and joint limit enforcement, hardware abstraction layer (HAL) implementation per actuator driver, real-time executor (Executor, rclcpp) latency tuning | ROS 2 Humble/Jazzy distribution, Nav2 navigation stack, MoveIt 2 manipulation planner, micro-ROS (bare-metal MCU), Isaac ROS (GPU-accelerated ROS 2 nodes), DDS transport layer | No | Low | Ecosystem / Developer lock-in | Low–Medium |
| AI Model Training & Deployment | Trains perception, planning, and language-conditioned task models; deploys quantized versions to edge | Simulation-to-real (sim2real) domain randomization in Isaac Sim / Gazebo, imitation learning from human demonstration teleoperation, reinforcement learning policy training (PPO/SAC in GPU cluster), model quantization (INT8/FP16) and TensorRT engine compilation, OTA model update and rollback | Isaac Sim synthetic dataset, imitation learning demonstration corpus, trained perception model (YOLOv8 / FoundationModel), TensorRT engine file, OTA update package | Partial | Medium | Data / Cloud training infra | High |
| System Integration & OEM Assembly | Integrates subsystems into a deployable robot or edge device and validates end-to-end system behavior | Mechanical CAD assembly with interference checking, robot calibration (hand-eye calibration, DH parameter identification), safety function integration (ISO 13849 Category 3/PLd), EMC testing (FCC/CE/UKCA), field reliability test (MTBF >10,000 hours), application-specific software customization | Humanoid robot chassis, AMR (autonomous mobile robot) base, collaborative robot arm, edge AI appliance enclosure, safety-rated I/O module | No | High | Systems engineering / Application knowledge | Low–Medium |
| Fleet Management & Operations Platform | Monitors and manages deployed robot fleets across sites in real time | Mission dispatch and scheduling (OSRF Fleet Adapter / VDA5050 protocol), remote teleoperation fallback via low-latency video stream, OTA firmware and model update orchestration, anomaly detection on joint torque and sensor health telemetry, digital twin fleet simulation | Fleet management SaaS, VDA5050-compliant traffic controller, remote teleop station, OTA update server, robot telemetry dashboard | No | Low | Data network effects / Switching cost | High |

---

## Interrelationship Anchors

Key cross-sector dependencies captured in `Ecosystem Interrelationships.md`:

| Direction | From Tier | To Sector | To Tier | Flow Type | Product / Process | Chokepoint? |
|-----------|-----------|-----------|---------|-----------|-------------------|-------------|
| Inbound | Photonics & Optical | Perception Layer | Component | LIDAR module / photonic sensor → robot perception stack | Partial |
| Inbound | Semiconductors | Edge Compute Module | Component | Jetson Orin SoC / Ambarella CV3 / Hailo-8 NPU → edge inference module | Yes |
| Inbound | Electronic Components | Perception Layer | Component | MLCC, film cap, RF connector → sensor electronics PCB | No |
| Inbound | Materials & Mining | Actuators & Motors | Material | NdFeB sintered magnet → BLDC servo motor rotor; rare earth alloy → motor winding | Yes |
| Inbound | Energy & Power | Actuators & Motors | Component | SiC-based VFD / motor drive → servo joint actuator torque control | No |
| Inbound | Compute Infrastructure | AI Model Training | Service | Cloud GPU cluster → sim2real training, imitation learning, RL policy training | No |
| Outbound | Fleet Management | Cybersecurity | Security Operations | Service | Robot fleet telemetry and OTA logs → XDR monitoring for anomaly detection in OT/IT converged networks | No |
| Outbound | AI Model Training | Compute Infrastructure | Demand Signal | Signal | Robot AI training workloads → GPU cloud demand pull (Isaac Sim, foundation model fine-tuning) | No |

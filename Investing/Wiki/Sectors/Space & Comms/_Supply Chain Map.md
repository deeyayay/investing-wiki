# Space & Communications — Supply Chain Map
*Mapped: 2026-05-24 | Anchor: LEO/MEO satellite constellations, launch vehicles, ground segment*
*Dimension: D2 — AI Connectivity*

---

## Framework Status
- [x] Supply chain mapped
- [x] Process/product depth added (2026-05-24)
- [x] Interrelationship Anchors documented (2026-05-24)
- [ ] Nodes registered (`/add-ticker TICKER --layer "Layer"` for each below)
- [ ] Ground truth pulled (`/stock-research TICKER` per node)
- [ ] Customer matrix built (`/build-customer-matrix "Space & Communications"`)
- [ ] Sector Framework written (only after above steps complete)

---

## Value Chain

| Tier | Function | Processes | Key Products / Materials | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|-----------|--------------------------|------------|-------------------|-----------|----------------|
| Launch Vehicle Manufacturing | Designs, fabricates, and integrates orbital launch vehicles | Structural airframe machining (Al-Li alloy, carbon fiber), engine assembly, propellant tank welding and pressure testing, avionics integration, stage separation system qualification, environmental stress screening | Electron small launch vehicle, Falcon 9 orbital vehicle, Neutron medium-lift (dev), Merlin/Rutherford engine, composite fairing | Partial | Very High | Process / Operational cadence | Low–Medium |
| Rocket Propulsion Systems | Develops and produces liquid and solid rocket engines | LOX/RP-1 turbopump cycle design, electric pump cycle integration (battery-fed), engine acceptance test (sea-level and altitude), specific impulse optimization | Rutherford LOX/kerosene engine (3D-printed Inconel), Curie/HyperCurie kick stages (storable biprop), LOX/CH4 engine (Archimedes, dev) | Partial | High | Process IP | Medium |
| Spacecraft Bus & Platform | Provides the standard structural, power, attitude, and comms infrastructure common to all payloads | Aluminum honeycomb bus panel bonding, solar array deployment and gimbal integration, Li-ion battery BMS, star tracker and reaction wheel assembly, RF transponder integration, harness routing | Photon satellite bus (Rocket Lab), CubeSat bus (6U–16U), triple-junction GaAs solar panel, star tracker assembly, reaction wheel assembly (RWA) | N | Medium | Product platform / Switching cost | Medium–High |
| Payload Integration (Comms) | Integrates satellite communication payloads: phased arrays, transponders, NTN radio nodes | Phased array antenna calibration (amplitude and phase weight per element), spot beam frequency plan coordination with ITU filing, transponder (TWTA/SSPA) integration, direct-to-cell 3GPP NTN software configuration, inter-satellite link alignment | Direct-to-cell phased array (ASTS BlueBird), geostationary Ku/Ka transponder, NTN 3GPP Rel-17 radio stack, ISL terminal | Yes | High | Technology / Spectrum license | High |
| Ground Segment & Network Operations | Operates terrestrial infrastructure for satellite commanding, telemetry, mission control, and gateway connectivity | Satellite C&T session scheduling, ephemeris propagation and antenna tracking, gateway Earth station RF uplink/downlink, TT&C encryption, spectrum coordination | Ground control software (Maestro, Atlas), X/S-band TT&C antenna system, gateway Earth station (Ka-band 3.8m dish), NOC workstation, orbital debris monitoring feed | N | Medium | Operational / Regulatory | Medium |
| Satellite Components Supply | Manufactures radiation-hardened electronic components and space-qualified materials | Proton irradiation testing (TID and SEE), rad-hard ASIC design (triple-redundancy voting logic), space-grade solar cell validation (AM0 spectrum), outgassing qualification per ASTM E595 | Rad-hard microprocessor (BAE RAD750 / GR740), triple-junction GaAs solar cell (>30% AM0 efficiency), space-grade Li-ion cell (Saft VES/VSX), space-qualified RF connector | Partial | Medium | Qualification / Certification | High |
| Spectrum & Orbital Rights | Coordinates and secures orbital slots and frequency licenses — the legal permission layer for satellite operations | ITU filing and coordination procedure (Article 9 and 21), FCC license application (Part 25 NGSO), frequency coordination with neighboring operators, orbital debris mitigation plan submission | ITU filing coordination record, FCC NGSO license, orbital slot assignment (GSO), debris mitigation compliance document, conjunction data message (CDM) | Yes | Low | Regulatory / First-mover | Very High |
| Satellite Internet Access (End Service) | Delivers broadband connectivity to end users via satellite terminal devices | DVB-S2X/DVB-RCS2 FEC modulation/demodulation, adaptive coding and modulation (ACM) link budget optimization, subscriber terminal self-pointing alignment, traffic QoS and fair-use policy enforcement | Starlink/ASTS subscriber terminal (flat phased array), VSAT modem, NTN-capable smartphone, satellite broadband backhaul circuit, maritime VSAT antenna | N | Low | Constellation scale / Spectrum | Medium–High |

---

## Interrelationship Anchors

Key cross-sector dependencies captured in `Ecosystem Interrelationships.md`:

| Direction | From Tier | To Sector | To Tier | Flow Type | Product / Process | Chokepoint? |
|-----------|-----------|-----------|---------|-----------|-------------------|-------------|
| Outbound | Satellite Internet Access | Compute Infrastructure | Edge Inference | Service | LEO broadband circuit → remote edge AI inference node (air-gapped, maritime, or rural) | No |
| Outbound | Ground Segment | Compute Infrastructure | Networking | Service | Ground station gateway backhaul → terrestrial fiber handoff to DC spine | No |
| Inbound | Semiconductors | Payload Integration | Component | Rad-hard ASIC, GaN PA die → satellite payload RF and baseband electronics | Partial |
| Inbound | Electronic Components | Satellite Components Supply | Component | Space-grade MLCC (MIL-PRF-55681), tantalum cap, rad-hard connector → satellite bus harness and PCB | No |
| Inbound | Photonics & Optical | Payload Integration | Component | ISL optical terminal, coherent modem → inter-satellite link optical communications | No |
| Inbound | Materials & Mining | Launch Vehicle Manufacturing | Material | Al-Li alloy extrusion, carbon fiber composite, Inconel 718 turbopump housing → launch vehicle structure and engine | Partial |
| Inbound | Photonics & Optical | Ground Segment | Component | Coherent DWDM line card / ROADM → terrestrial fiber backbone connecting satellite ground stations | No |

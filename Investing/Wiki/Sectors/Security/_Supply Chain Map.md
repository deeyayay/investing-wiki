# Cybersecurity — Supply Chain Map
*Mapped: 2026-05-24 | Anchor: AI-era software security stack*
*Dimension: D4 — AI Enablement*

---

## Framework Status
- [x] Supply chain mapped
- [x] Process/product depth added (2026-05-24)
- [x] Interrelationship Anchors documented (2026-05-24)
- [ ] Nodes registered (`/add-ticker TICKER --layer "Layer"` for each below)
- [ ] Ground truth pulled (`/stock-research TICKER` per node)
- [ ] Customer matrix built (`/build-customer-matrix "Cybersecurity"`)
- [ ] Sector Framework written (only after above steps complete)

---

## Value Chain

| Tier | Function | Processes | Key Products / Materials | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|-----------|--------------------------|------------|-------------------|-----------|----------------|
| Hardware Security Root | Provides silicon-level root of trust — the cryptographic anchor that all higher software tiers depend on for attestation and key storage | TPM 2.0 chip provisioning & PCR sealing; HSM key ceremony & FIPS 140-2/3 validation testing; secure enclave memory isolation (Intel TDX, AMD SEV-SNP, ARM TrustZone); firmware attestation measurement; certificate authority (CA) key generation in HSM | TPM 2.0 chip (Infineon SLB 9672, STMicro ST33); Hardware Security Module (Thales Luna, AWS CloudHSM); Intel TDX / AMD SEV-SNP virtual enclave; ARM TrustZone TEE; FIPS 140-3 validated key store | Partial | Medium | Certification · Process IP | High |
| Identity & Access Management (IAM/PAM) | Governs who and what can authenticate and authorize access to systems, data, and cloud resources — first control plane | SCIM 2.0 directory sync & provisioning workflows; SAML/OIDC/OAuth 2.0 federation brokering; MFA enrollment, push notification, and FIDO2/WebAuthn passkey authentication; privileged session recording and just-in-time (JIT) access vaulting; identity governance & access certification campaigns | SailPoint IdentityNow / IdentityIQ platform; Okta Workforce Identity Cloud; CyberArk Privileged Access Manager (PAM); Microsoft Entra ID (formerly AAD); FIDO2/WebAuthn passkey credential | Partial | Low | Switching cost · Ecosystem | Very High |
| Endpoint Detection & Response (EDR) | Monitors every process, file, registry, and network call on endpoints to detect and contain threats in real time | Kernel-level telemetry collection via lightweight sensor (≤1% CPU); behavioral ML model scoring on process trees; memory scanning and shellcode injection detection; automated threat containment (process kill, network isolation); threat hunting query interface (YARA, SQL-style) across fleet telemetry | CrowdStrike Falcon sensor + Threat Graph; SentinelOne Singularity platform; Microsoft Defender for Endpoint; YARA rule library; behavioral ML decision engine (on-device inference) | Partial | Low | Switching cost · Ecosystem · Scale | Very High |
| Network Detection & Response (NDR) | Inspects east-west and north-south traffic flows to detect anomalies, lateral movement, and command-and-control communications | Deep packet inspection (DPI) at line rate (10–100 Gbps); TLS fingerprinting and JA3/JA4 hash analysis; NetFlow / IPFIX metadata collection and baselining; zero-trust network access (ZTNA) policy enforcement via software-defined perimeter; DNS sinkholing and threat intelligence feed enrichment | Zscaler Zero Trust Exchange (ZTNA/SWG/CASB); Palo Alto Prisma Access; Fortinet FortiGate NGFW + SD-WAN; Vectra AI NDR platform; NetFlow / IPFIX metadata collector appliance | No | Medium | Scale · Switching cost | High |
| Cloud Security Posture (CSPM/CNAPP) | Continuously audits cloud infrastructure configurations and workload runtime behavior against security benchmarks and compliance frameworks | Agentless cloud resource enumeration across AWS/Azure/GCP APIs; CIS Benchmark / NIST 800-53 / SOC 2 posture scoring; container image scanning (CVE matching against NVD/OSV); Kubernetes admission control via OPA/Gatekeeper policy; cloud infrastructure entitlement management (CIEM) — excess IAM role detection | Wiz CNAPP platform; Palo Alto Prisma Cloud; CrowdStrike Falcon Cloud Security; Orca Security; Open Policy Agent (OPA) policy bundle | No | Low | Ecosystem · Switching cost | Very High |
| Data Security & Backup / Recovery | Protects data at rest and in motion through encryption, DLP, and immutable backup — and recovers from ransomware or deletion | Data classification scanning (regex + ML entity recognition) across structured and unstructured stores; DLP policy enforcement at email, web, and endpoint egress; AES-256 / RSA-4096 encryption key management (BYOK/HYOK workflows); immutable snapshot creation with air-gap or logical isolation; ransomware recovery orchestration (RTO/RPO testing, automated runbooks) | Rubrik Security Cloud (Zero Trust Data Management); Cohesity DataProtect; Varonis Data Security Platform; Zscaler DLP; AES-256 encrypted snapshot with cryptographic immutability guarantee | Partial | Medium | Switching cost · Certification | High |
| Security Operations (SIEM/SOAR/XDR) | Aggregates, correlates, and responds to telemetry from all other tiers — the analytical hub of the security stack | Log ingestion normalization (CEF/LEEF/JSON → common schema, 100TB+/day pipelines); UEBA (user and entity behavior analytics) baseline deviation scoring; SOAR playbook automation (Python/YAML-defined response workflows); threat intelligence enrichment via MITRE ATT&CK TTP tagging; SLA-tracked alert triage and case management | Palo Alto Cortex XSIAM; Microsoft Sentinel; CrowdStrike Falcon Complete XDR; Splunk Enterprise Security (SIEM); MITRE ATT&CK framework navigator | No | Low | Scale · Ecosystem · Switching cost | High |
| AI-Native Security | Secures AI/ML systems themselves and deploys AI agents for autonomous threat hunting — the emerging frontier tier | LLM prompt injection detection and output validation (guardrail models); AI model red-teaming and adversarial robustness testing (FGSM, PGD attacks); ML supply chain integrity verification (model card attestation, training data provenance); AI SOC co-pilot generation of detection logic (SIGMA rules from natural language); autonomous AI agent-driven threat hunting across graph databases | HiddenLayer Model Scanner; Protect AI Guardian; CrowdStrike Charlotte AI; Microsoft Security Copilot; SIGMA rule generation via LLM; NIST AI RMF compliance assessment | No | Low | Process IP · Ecosystem | Very High |

---

## Publicly-Traded Nodes

| Tier | Ticker | Company | Mkt Cap | In Registry | Notes |
|------|--------|---------|---------|-------------|-------|
| Hardware Security Root | — | *No public pure-play* | — | — | ⚠️ Structural gap — TPM/HSM are product lines within Infineon (IFNNY), STMicro (STM), Thales (HO); no pure-play public company |
| IAM/PAM | SAIL | SailPoint, Inc. | Large | Yes | Identity governance & administration (IGA); re-listed 2024 after Vista PE take-private |
| IAM/PAM | OKTA | Okta, Inc. | Large | No — candidate | Workforce + Customer Identity Cloud; OIDC/SAML federation; FIDO2 passkey leader |
| IAM/PAM | CYBR | CyberArk Software | Large | No — candidate | PAM market leader; JIT access, session recording, secrets management |
| EDR | CRWD | CrowdStrike Holdings | Large | No — candidate | Falcon platform; largest EDR market share; AI-native Threat Graph; moving to XDR/platform |
| EDR | S | SentinelOne | Mid | No — candidate | Singularity platform; autonomous EDR; Purple AI threat hunting; strong cloud workload protection |
| NDR / ZTNA | ZS | Zscaler | Large | No — candidate | Zero Trust Exchange; largest SSE (Security Service Edge) platform; ZTNA + SWG + CASB + DLP |
| NDR / Firewall | FTNT | Fortinet | Large | No — candidate | FortiGate NGFW + SD-WAN; FortiAnalyzer SIEM; vertically integrated hardware + software |
| CSPM / CNAPP | PANW | Palo Alto Networks | Large | No — candidate | Prisma Cloud CNAPP; Cortex XDR/XSIAM; largest pure-play cybersecurity company by revenue |
| Data Security / Backup | RBRK | Rubrik, Inc. | Mid | Yes | Zero Trust Data Management; ransomware recovery; immutable snapshots; cloud-native |
| SIEM / XDR | PANW | Palo Alto Networks | Large | No — candidate | Cortex XSIAM (AI-driven SOC platform); platformization strategy converging all tiers |

---

## Structural Gaps

**Hardware Security Root — No Pure-Play Public Equity:**
TPM 2.0 chips are manufactured by Infineon (IFNNY, ~40% global TPM share) and STMicroelectronics (STM), both of which are diversified semiconductor companies where TPM revenues are immaterial to valuation. HSM appliances are sold by Thales (HO, France), a large defense/aerospace conglomerate, and Entrust (private). Cloud HSM is offered as a service by AWS, Azure, and GCP directly. There is no public company where hardware root-of-trust is the core business. The structural moat here is FIPS 140-3 certification and CC EAL 4+ evaluation — extremely time-consuming to obtain and not transferable across product generations. Any new entrant (e.g., a startup building a RISC-V-based open-source TPM) faces a multi-year certification gap. Watch for: NIST PQC algorithm migration (CRYSTALS-Kyber, Dilithium) forcing a hardware refresh cycle in TPM/HSM that could create a re-rating opportunity in diversified suppliers.

**AI-Native Security — Pre-Revenue / Private:**
The companies defining LLM prompt injection detection (HiddenLayer, Protect AI, Robust Intelligence) are all venture-backed and pre-IPO. This tier is growing rapidly due to enterprise AI adoption creating new attack surfaces (model inversion, training data poisoning, jailbreak exploitation). The lack of public equity here is both a gap and an early signal — watch for IPOs or CRWD/PANW bolt-on acquisitions as the primary investment expression.

---

## Key Questions to Answer Before Writing the Sector Framework

1. **Platformization vs. best-of-breed:** CrowdStrike, Palo Alto, and Microsoft are each attempting to own the full stack (EDR + CSPM + SIEM + identity). Do customers consolidate to 1–2 platforms, or does best-of-breed persist in regulated verticals? The answer determines whether point-solution specialists (SAIL, ZS, CYBR) sustain premium multiples or compress.
2. **AI as threat vs. AI as moat:** LLM-powered phishing, deepfake social engineering, and autonomous vulnerability exploitation compress attacker dwell time. Does AI make the defender's detection-response loop faster (moat) or does it disproportionately benefit attackers (structural headwind)?
3. **Government and FedRAMP:** CRWD, PANW, and ZS all have FedRAMP High authorizations. RBRK and SAIL are pursuing them. Does federal spend (post-CISA mandate enforcement) create a durable revenue stream or a one-time pull-forward?
4. **Identity as the new perimeter:** With Zero Trust mandates (EO 14028, M-22-09), identity (IAM/PAM) is now the primary security control. Does this structurally re-rate SAIL and CYBR, or does Microsoft Entra commoditize this tier for most enterprises?
5. **OT/ICS security greenfield:** Industrial control system security (Claroty, Nozomi — both private) is underpenetrated and rapidly mandated by NERC CIP, NIS2, and TSA pipeline directives. No pure-play public company owns this tier — is it an acquisition target or an organic expansion vector for the platform players?
6. **Data security TAM expansion:** Every AI deployment creates a new data security surface (training data, model weights, inference logs). Does Rubrik's Zero Trust Data Management positioning capture AI data security spend, or does a new purpose-built AI data security category emerge?

---

## Interrelationship Anchors

### Inputs (this sector consumes from)
| From Sector | From Tier | Product / Signal |
|---|---|---|
| Semiconductors | Hardware Security Silicon | TPM 2.0 chip (Infineon SLB 9672 / STM ST33) → hardware root of trust for endpoint and server boot attestation |
| Semiconductors | Secure Enclave Design | Intel TDX / AMD SEV-SNP confidential computing silicon → cloud workload memory isolation for sensitive AI workloads |
| Compute Infrastructure | Cloud & Hyperscaler Operations | VPC flow logs, API audit logs, CloudTrail events → SIEM/XDR ingestion at petabyte scale |
| Energy & Power | OT/ICS & Grid Operations | SCADA telemetry, historian data, Modbus/DNP3 network traffic → OT security monitoring (NERC CIP compliance) |

### Outputs (this sector supplies to)
| To Sector | To Tier | Product / Signal |
|---|---|---|
| Compute Infrastructure | Cloud Workload Protection | Zero Trust network access (ZTNA) policy enforcement → cloud workload and API access control |
| Fintech & Commerce AI | Fraud & Identity Stack | Identity verification API, fraud detection behavioral model, transaction risk score → financial AI decisioning layer |
| Defense & Space | Sovereign Security Operations | Air-gap XDR architecture, classified SOC tooling, hardware-attested supply chain verification → defense cyber posture |

---

## Research Log
- **2026-05-24** — map-sector run. 8 tiers, 2 chokepoints (Partial: Hardware Security Root, IAM/PAM, Data Security), 2 structural gaps (Hardware Root pure-play, AI-Native Security). 11 public nodes identified (2 already in registry: RBRK, SAIL; 7 new candidates: CRWD, PANW, S, ZS, OKTA, CYBR, FTNT). 5 new cross-sector flows appended to Ecosystem Interrelationships.md.

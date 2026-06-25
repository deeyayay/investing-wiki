# Insurance AI — Supply Chain Map
*Mapped: 2026-06-25 | Anchor: AI-native insurance and AI-augmented underwriting platforms*
*Dimension: D5 — AI Applications (L01 Application)*

---

## Framework Status
- [x] Supply chain mapped
- [x] Process/product depth added (2026-06-25)
- [x] Interrelationship Anchors documented (2026-06-25)
- [ ] Nodes registered (`/add-ticker TICKER --sector "Insurance AI"` for each below)
- [ ] Ground truth pulled (`/stock-research TICKER` per node)
- [ ] Customer matrix built (`/build-customer-matrix "Insurance AI"`)
- [ ] Sector Framework written (only after above steps complete)

---

## Value Chain

| Tier | Function | Processes | Key Products / Materials | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|-----------|--------------------------|------------|-------------------|-----------|----------------|
| Actuarial Data & Risk Intelligence | Produces the statistical models, industry databases, and catastrophe models that form the pricing foundation for all P&C and life insurance products | Catastrophe model calibration runs (EP curve generation, AAL/PML computation), loss development triangle actualization, property exposure database construction and geocoding, industry loss statistics compilation, risk factor parameterization (IBNER/IBNR reserve factors), weather and climate data integration for nat-cat modeling, rate filing support under ISO actuarial certification | Catastrophe model output (AIR CATRADER, RMS RiskLink), industry loss warranty (ILW) reference curves, loss cost indications, property characteristics database (ISO), commercial lines policy statistics database, actuarial certification for rate filings | Y | Low | Proprietary data / Regulatory mandate / Certification | Very High |
| AI Underwriting & Risk Selection | Uses ML models, satellite imagery, telematics, and alternative data to automate and augment underwriting decisions at the point of application | Application data ingestion and normalization (structured + unstructured), ML classification model inference for risk eligibility, satellite/aerial imagery analysis for property condition assessment (roof age, debris, pool, trampolines), alternative data enrichment (credit score, behavioral telematics), automated coverage eligibility determination and real-time quote generation, portfolio exposure aggregation and concentration monitoring, adverse selection model refinement via champion/challenger testing | Underwriting eligibility score, risk classification output, automated quote, property aerial condition report (Cape Analytics / EagleView format), telematics driving behavior score, portfolio exposure heatmap | Partial | Low | Process IP / Proprietary training data | Very High |
| Policy Administration Systems (PAS) | Maintains the authoritative system of record for the full insurance policy lifecycle: issuance, endorsement, renewal, cancellation, and billing | Policy issuance and declarations page generation, mid-term endorsement processing and pro-rata premium computation, renewal rating cycle execution (re-underwriting + repricing), cancellation and non-renewal workflow and regulatory notice generation, premium billing cycle management and payment collections, reinsurance cession bordereau reporting, regulatory form filing management, API gateway for third-party distribution channels | Policy declarations page, endorsement form, renewal notice, premium invoice, reinsurance bordereau, regulatory filing package, PAS API for embedded distribution | N | Medium | Switching cost (12–36-month implementation cycle) | High |
| Claims AI & Automation | Automates claims intake, damage assessment, reserve setting, and settlement using computer vision, NLP, and workflow orchestration — the highest-volume human-labor tier in traditional insurance | FNOL (first notice of loss) intake via mobile app / voice IVR / web, AI computer vision damage assessment from photos and video (auto collision, structural damage, bodily injury documentation), medical record and bill extraction with ICD/CPT code classification via NLP, subrogation opportunity scoring from police reports and repair estimates, reserve adequacy estimation via ML, automated payment disbursement for fast-track claims, litigation risk prediction scoring | AI damage estimate (Xactimate-format property, Mitchell/CCC-format auto), medical bill review output, subrogation score, reserve recommendation, fast-track straight-through payment decision, litigation prediction score | Partial | Low | Process IP / Switching cost / Proprietary training data (claims corpus) | Very High |
| Fraud Detection & Investigation AI | Identifies fraudulent claims, applications, and staged accidents before and after payment using network graph analysis, anomaly detection, and industry-wide consortium data | Social network graph construction and claimant relationship analysis, medical provider billing pattern anomaly detection, vehicle history cross-referencing (VIN decode, title wash, total-loss history), staged accident pattern recognition from police report text, identity verification and synthetic identity detection at application, SIU (special investigation unit) workflow routing and case management, ISO ClaimSearch industry consortium database query | Fraud risk score, SIU referral queue, provider anomaly alert, network link visualization output, ISO ClaimSearch hit report, identity verification result, synthetic identity flag | Partial | Low | Proprietary data consortium (ClaimSearch, NICB) / Process IP | Very High |
| Telematics & IoT Risk Data Platforms | Collects and processes real-time behavioral, sensor, and environmental data to enable usage-based, behavior-based, and parametric insurance products | Telematics data ingestion from OBD-II dongles, smartphone accelerometers, and connected vehicle APIs (GM OnStar, Ford Pass, Tesla API), driving behavior event classification (hard braking, sharp cornering, speeding, distracted driving detection via phone screen-off proxy), property IoT data aggregation (Ting electrical fire sensor, Notion water leak sensor, Ring doorbell), parametric trigger monitoring (NOAA weather station, USGS earthquake seismograph, FlightAware delay data), feature engineering pipeline for UBI pricing model, real-time risk alert generation and automated premium adjustment | Driving behavior score report, UBI discount/surcharge recommendation, electrical fire risk alert, IoT-triggered parametric payout confirmation, weather event confirmation (named storm, hail, earthquake), vehicle telematics event log (hard events + trip data) | Partial | Low | Data consortium / Network effects (larger enrollee base → better model calibration) | High |
| AI-Native Digital Insurance Carriers | Vertically integrated digital-native carriers that own the full stack — underwriting model, policy issuance, claims processing, and customer relationship — eliminating traditional agent intermediaries and using AI to compress the loss ratio | AI-powered real-time underwriting at point of sale (seconds not days), instant quote-bind-issue via mobile app and API, AI claims bot FNOL intake and automated settlement (Lemonade's "Jim" bot), behavioral data and social graph risk scoring at onboarding, continuous portfolio re-underwriting via live ML model, embedded insurance API for third-party channel distribution, parametric micro-insurance product structuring, customer lifetime value optimization via AI personalization | Digital insurance policy (instant issuance), instant FNOL settlement (sub-3-minute for eligible claims), AI underwriting decision with explainability output, embedded insurance API for retail and e-commerce integration, parametric payout confirmation | N | Low–Medium (regulatory capital requirements scale with written premium) | Data flywheel (proprietary claims data → better loss models) / Low-cost distribution | Variable — improving as scale improves loss ratio |
| Reinsurance Analytics & ILS | Provides risk transfer capacity and capital markets structures (cat bonds, ILS) that allow primary insurers to underwrite volatile nat-cat and tail-risk exposures; AI models now central to cedent selection, pricing, and ILS structuring | Cedent exposure data normalization from policy bordereaux, cat model aggregation across cedents to produce portfolio-level EP curve, treaty pricing and attachment/exhaustion point optimization, ILS (cat bond) risk modeling and prospectus note drafting, facultative underwriting database query and pricing, collateral and reserve tracking for collateralized reinsurance vehicles, retrocession placement optimization, secondary market ILS pricing and analytics | Reinsurance treaty terms and pricing sheet, cat bond prospectus (Rule 144A offering), ILS annual report (Bermuda Form 3SPI equivalent), CRESTA-zone exposure summary, retrocession placement confirmation | Partial | Very High (balance sheet risk capital) | Capital scale / Proprietary cat model calibration / Cedent relationship network | Cyclical (hard vs. soft market) |

---

## Publicly-Traded Nodes

| Tier | Ticker | Company | Mkt Cap | In Registry | Notes |
|------|--------|---------|---------|-------------|-------|
| Actuarial Data & Risk Intelligence | VRSK | Verisk Analytics | Large | No | ISO + AIR CATRADER cat model + Xactimate claims estimating + PCS nat-cat data; multi-tier data chokepoint |
| Actuarial Data & Risk Intelligence | MCO | Moody's Corporation | Large | No | Acquired RMS (2021); Moody's RMS is AIR's primary cat model competitor; also has insurance analytics via Moody's Analytics |
| AI Underwriting & Risk Selection | LMND | Lemonade Inc. | Small | No | AI-native P&C + life carrier; built proprietary underwriting model on behavioral data; also listed as primary AI-Native Carrier |
| AI Underwriting & Risk Selection | ROOT | Root Insurance | Small | No | Telematics-first UBI auto insurer; smartphone-based driving score is the underwriting model |
| Policy Administration Systems | GWRE | Guidewire Software | Mid | No | Dominant P&C PAS + billing + claims (InsuranceSuite); 500+ carrier installations globally; Guidewire Cloud platform now primary focus |
| Claims AI & Automation | VRSK | Verisk Analytics | Large | No | Xactimate is used by ~80% of P&C adjusters for property damage estimation; Verisk Financial claims analytics |
| Claims AI & Automation | CCCS | CCC Intelligent Solutions | Small–Mid | No | Auto claims AI platform; 24M+ appraisals/year; used by insurers, collision repairers, OEMs; SaaS + AI damage assessment |
| Fraud Detection & Investigation AI | — | *No standalone public player* | — | — | ⚠️ Structural gap — ISO ClaimSearch (Verisk subsidiary), NICB (nonprofit), Shift Technology (private). Palantir has insurance fraud deployments but not a primary segment |
| Telematics & IoT Risk Data Platforms | — | *No standalone public player* | — | — | ⚠️ Structural gap — Cambridge Mobile Telematics (private, MIT spinout), Arity (Allstate subsidiary), LexisNexis Telematics Exchange (RELX subsidiary), Octo Telematics (private) |
| AI-Native Digital Insurance Carriers | LMND | Lemonade Inc. | Small | No | P&C + life; AI-native platform; growing renters/homeowners/auto/pet; Metromile acquisition added UBI auto |
| AI-Native Digital Insurance Carriers | ROOT | Root Insurance | Small | No | UBI auto; telematics underwriting; improving loss ratio trajectory |
| AI-Native Digital Insurance Carriers | OSCR | Oscar Health | Small | No | AI-native health insurer; individual ACA marketplace + employer; own care navigation platform |
| AI-Native Digital Insurance Carriers | HIPO | Hippo Holdings | Small | No | AI-native homeowners; post-restructuring (Spinnaker merger); watch for portfolio stabilization |
| Reinsurance Analytics & ILS | RNR | RenaissanceRe Holdings | Mid | No | Cat-analytics-driven reinsurer; proprietary Kauai cat model; considered the most analytically sophisticated reinsurer |
| Reinsurance Analytics & ILS | RGA | Reinsurance Group of America | Mid | No | Life/health re dominant; AI predictive mortality analytics; data moat in life underwriting |
| Reinsurance Analytics & ILS | EG | Everest Group | Mid | No | P&C re + specialty primary; growing insurance segment; analytical underwriting approach |

---

## Structural Gaps

**Fraud Detection & Investigation AI — No pure-play public player.** ISO ClaimSearch (Verisk subsidiary) is the industry-standard consortium database covering 1B+ claim records — but it is bundled inside Verisk's broader insurance analytics suite, not available as a standalone investment. NICB (National Insurance Crime Bureau) is a nonprofit. Shift Technology (AI fraud detection SaaS, Paris-based) is private. DataRobot and Gradient AI address sub-segments but are private. Watch for: a Shift Technology IPO; or acquisitions by an incumbent insurer / reinsurer seeking to internalize the fraud model capability.

**Telematics & IoT Risk Data Platforms — Ecosystem locked inside private companies and strategic subsidiaries.** Cambridge Mobile Telematics (CMT) is the dominant third-party telematics SDK supplier — private, MIT spinout, profitable. Arity is Allstate's telematics data subsidiary — not separately traded. LexisNexis Telematics Exchange is a RELX business unit — not separately tradeable. Octo Telematics (Italian, was NYSE-listed as OCTO, went private via buyout). The public market has zero pure-play exposure to telematics data generation — the best indirect exposure is VRSK (telematics data consortium participant) or connected-vehicle software companies that are also private.

**Property IoT Integration — Consumer electronics companies, not insurers.** Smart home IoT sensors that generate real-time property risk signals (Ting electrical sensors by Whisker Labs, Notion water sensors, SimpliSafe security) are private consumer electronics companies. The insurtech value here accrues to the insurer that aggregates the data, not the hardware maker. Watch for acquisition activity by large homeowners insurers.

---

## Key Questions to Answer Before Writing the Sector Framework

1. **Does LMND's AI underwriting actually outperform incumbents on loss ratio, or has CAT exposure (homeowners book in high-risk geographies) masked potentially strong non-CAT performance?** The gross loss ratio can be deconstructed — what does the attritional loss ratio look like ex-CAT and ex-prior-year development?
2. **Can AI-native carriers achieve structural reinsurance cost parity with incumbents?** LMND and ROOT both pay meaningfully higher reinsurance premiums than Allstate or Progressive because they lack the loss history and balance sheet that reinsurers price. At what written-premium scale does the proprietary data advantage overcome the reinsurance cost disadvantage?
3. **Does Guidewire (GWRE) maintain its PAS monopoly as insurers evaluate modular microservices architecture?** Duck Creek went private; Majesco pivoted; GWRE is the last large-cap P&C PAS public. Its Cloud migration (Guidewire Cloud) converts one-time license revenue to ARR — is the transition creating a durable SaaS moat, or is it extending the replacement cycle?
4. **Is Verisk's multi-tier data monopoly (actuarial data + claims estimating + cat model) a regulatory liability as well as a competitive asset?** The DOJ/FTC scrutiny on data monopolies in insurance (ISO rate-filing data is effectively mandatory to file rates in most states) is an underappreciated regulatory risk.
5. **At what scale does a digital carrier's proprietary claims training data become meaningfully better than a large incumbent's dataset?** LMND has ~2M policies; Allstate has 35M+; Progressive has 30M+ with 20+ years of telematics data. The data moat story requires an answer on when quality outweighs quantity.
6. **Does embedded insurance (API distribution via non-insurance platforms) structurally erode the broker/agent distribution moat, or does regulatory complexity keep intermediaries dominant?** If Cover Genius or LMND's API can replace an agent for simple P&C products, what happens to the ~$400B global agent commission market?

---

## Interrelationship Anchors

### Inputs (this sector consumes from)
| From Sector | From Tier | Product / Signal |
|---|---|---|
| Cloud Infrastructure | AI Model Serving (GPU cluster) | LLM inference API for claims document extraction, underwriting copilot, customer chatbot, and fraud reasoning — hosted on hyperscaler GPU (AWS Bedrock, Azure OpenAI, GCP Vertex) |
| AI Model | Foundation Model Development | LLM weights and inference API (GPT-4o, Claude, Gemini) → document understanding (policy, claims, medical records), customer service automation, underwriting narrative reasoning |
| Security | Identity & Access Management | KYC / identity verification at policyholder onboarding, synthetic identity detection at application, API authentication for policy and claims data |
| Edge & Physical AI | IoT Sensor Networks | Telematics vehicle data (OBD-II, smartphone SDK), smart home sensor data (water leak, electrical fire, security), property aerial imagery for underwriting risk assessment |
| Compute Hardware | Demand Signal | Growing ML inference workloads for underwriting, claims triage, and fraud scoring → GPU compute demand pull through hyperscalers |

### Outputs (this sector supplies to)
| To Sector | To Tier | Product / Signal |
|---|---|---|
| Cloud Infrastructure | Demand Signal | Insurance AI inference workloads (underwriting scoring, claims triage, fraud detection) → hyperscaler GPU capacity demand pull |
| Application (Fintech) | Embedded Finance | Insurance product APIs → embedded insurance integrated at point of mortgage origination, e-commerce checkout, auto purchase, travel booking |
| AI Model | Training Data Signal | Insurance claim text + outcomes data → high-value fine-tuning corpus for document extraction and actuarial reasoning models |

---

## Research Log
- **2026-06-25** — map-sector run. 8 tiers, 1 full chokepoint (Actuarial Data & Risk Intelligence), 3 partial chokepoints (Claims AI, Fraud AI, Telematics), 2 structural gaps (Fraud Detection pure-play, Telematics pure-play). New candidates not yet in registry: VRSK, GWRE, LMND, ROOT, CCCS, MCO, OSCR, HIPO, RNR, RGA, EG.

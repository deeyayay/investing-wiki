# Fintech & Commerce AI — Supply Chain Map
*Mapped: 2026-05-24 | Anchor: AI-powered financial services and commerce platforms*
*Dimension: D5 — AI Applications*

---

## Framework Status
- [x] Supply chain mapped
- [x] Process/product depth added (2026-05-24)
- [x] Interrelationship Anchors documented (2026-05-24)
- [ ] Nodes registered (`/add-ticker TICKER --layer "Layer"` for each below)
- [ ] Ground truth pulled (`/stock-research TICKER` per node)
- [ ] Customer matrix built (`/build-customer-matrix "Fintech & Commerce AI"`)
- [ ] Sector Framework written (only after above steps complete)

---

## Value Chain

| Tier | Function | Processes | Key Products / Materials | Chokepoint | Capital Intensity | Moat Type | Margin Profile |
|------|----------|-----------|--------------------------|------------|-------------------|-----------|----------------|
| Payment Network Rails & Settlement | Provides the clearing and settlement backbone for all money movement | Card network authorization routing, ACH file origination and batching, real-time gross settlement (RTGS) message processing, ISO 20022 message translation, chargeback and dispute workflow automation | Visa/Mastercard network APIs, ACH batch files, SWIFT MT/MX messages, FedWire settlement, SEPA credit transfer | Y | Low | Ecosystem / Scale | Very High |
| Core Banking & Ledger Systems | Maintains authoritative books of record for accounts, balances, and transactions | Double-entry ledger posting, general ledger reconciliation, nostro/vostro account management, interest accrual calculation, regulatory capital reserve computation, core system API gateway integration | Core banking platforms (Temenos T24, Finacle, nCino), ledger-as-a-service APIs, transaction journal, GAAP-compliant financial record | Partial | Medium | Switching cost | High |
| Risk & Fraud AI Models | Detects and suppresses fraudulent transactions and credit risk events in real time | Feature engineering from transaction sequences, gradient boosting and deep learning model training on labeled fraud corpora, real-time model inference (<50ms), model drift monitoring and champion/challenger A-B testing, supervised rule engine overlay | ML fraud scoring models (XGBoost, LightGBM, transformer-based), behavioral biometrics signals, device fingerprinting features, velocity rules engine | Partial | Low | Process IP / Switching cost | Very High |
| Identity Verification & KYC | Establishes and maintains verified identity for onboarding and ongoing compliance | Document capture and OCR extraction, liveness detection and facial match biometrics, database watchlist screening (OFAC, PEP, adverse media), eKYC workflow orchestration, customer due diligence (CDD) periodic review | Government ID scan + NFC chip read, liveness selfie biometric, KYC orchestration platform, AML watchlist database, eIDAS-compliant digital identity credential | Partial | Low | Certification / Switching cost | High |
| Credit Decisioning & Underwriting AI | Scores loan applications and prices risk using alternative and traditional data sources | Credit bureau data pull and tradeline parsing, alternative data ingestion (bank transaction history, payroll, utility), income verification via permissioned bank data (Plaid/MX), decision tree and gradient boosting model inference, regulatory fair-lending disparate impact testing, adverse action notice generation | Credit scoring model (FICO alternative), loan origination system (LOS), underwriting decisioning API, fair-lending monitoring report, income verification report | Partial | Low | Process IP / Data | Very High |
| Personal Finance & Wealth Management Platforms | Delivers end-user financial management, investment, and advisory experiences | Account aggregation via open banking API or screen-scrape, portfolio rebalancing engine (tax-loss harvesting, drift thresholds), LLM-powered financial advisory chatbot, retirement projection Monte Carlo simulation, fractional share order routing to broker-dealer | Account aggregation API (Plaid, MX, Finicity), robo-advisory engine, portfolio management software (Orion, Riskalyze), LLM financial assistant, SIPC-protected brokerage account | N | Low | Ecosystem / Switching cost | High |
| Embedded Finance & Commerce APIs | Delivers banking and payment capabilities inside non-financial applications via API | BaaS (Banking-as-a-Service) API provisioning, program management for co-branded card issuance, buy-now-pay-later (BNPL) checkout SDK integration, instant virtual card issuance, split-pay and installment plan calculation, merchant acquiring API | BaaS ledger API (Stripe Treasury, Unit, Column), virtual card BIN program, BNPL installment plan, payment gateway webhook, merchant acquiring token | N | Low | Ecosystem / Switching cost | High |
| Regulatory Compliance Tech (RegTech) | Automates compliance reporting, transaction monitoring, and regulatory filing obligations | Suspicious activity report (SAR) filing workflow, Currency Transaction Report (CTR) generation, Bank Secrecy Act (BSA) transaction monitoring rule execution, CCAR stress test data pipeline, automated regulatory change management, audit trail immutable logging | SAR/CTR filing system, BSA AML monitoring platform, CCAR data aggregation pipeline, regulatory change alert feed, immutable compliance audit log | N | Low | Certification / Switching cost | High |

---

## Publicly-Traded Nodes

| Tier | Ticker | Company | Mkt Cap | In Registry | Notes |
|------|--------|---------|---------|-------------|-------|
| Payment Network Rails & Settlement | — | *No pure-play public player at the rail level* | — | — | ⚠️ Structural gap — Visa (V) and Mastercard (MA) own the rails but are mega-cap; no mid-cap pure play |
| Core Banking & Ledger Systems | NCNO | nCino, Inc. | Mid | No | Cloud-native banking OS for commercial lending; strong bank adoption |
| Risk & Fraud AI Models | UPST | Upstart Holdings | Small | No | AI-native credit risk model; no FICO dependency |
| Risk & Fraud AI Models | AFRM | Affirm Holdings | Mid | No | Real-time underwriting at checkout; proprietary risk model |
| Identity Verification & KYC | — | *No standalone public player* | — | — | ⚠️ Structural gap — Jumio, Onfido, Socure are private; AU10TIX private |
| Credit Decisioning & Underwriting AI | UPST | Upstart Holdings | Small | No | Already listed above under Fraud AI |
| Credit Decisioning & Underwriting AI | SOFI | SoFi Technologies | Mid | Yes | Bank charter + proprietary credit model + Galileo BaaS platform |
| Personal Finance & Wealth Management | HOOD | Robinhood Markets | Mid | Yes | Commission-free retail brokerage + crypto; expanding into advisory |
| Personal Finance & Wealth Management | NU | Nu Holdings (Nubank) | Large | No | Largest digital bank in LatAm; AI-native credit and savings |
| Embedded Finance & Commerce APIs | MELI | MercadoLibre | Large | Yes | LatAm marketplace + MercadoPago embedded finance + Mercado Credito |
| Embedded Finance & Commerce APIs | SQ | Block, Inc. | Mid | No | Square merchant acquiring + Cash App consumer finance + BNPL (Afterpay) |
| Embedded Finance & Commerce APIs | PYPL | PayPal Holdings | Large | No | PayPal + Venmo + Braintree; embedded checkout ubiquity |
| Embedded Finance & Commerce APIs | FLYW | Flywire Corporation | Small | No | Vertical-specific payment rails for healthcare, education, travel |
| Regulatory Compliance Tech (RegTech) | — | *No standalone public pure-play* | — | — | ⚠️ Structural gap — Actimize (NICE), Napier, ComplyAdvantage are private or bundled |

---

## Structural Gaps

**Payment Network Rails & Settlement — No mid-cap public pure play.** Visa (V) and Mastercard (MA) own the core card rails but are mega-cap consumer staples stocks, not investable as fintech growth plays. The ACH / RTP / FedNow real-time rail infrastructure is operated by The Clearing House (private, bank-owned) and the Federal Reserve (public sector). This tier has essentially no investable mid-cap public node — the value accrues entirely to the two card network incumbents.

**Identity Verification & KYC — Privately held.** Leading players (Jumio, Socure, Onfido/Entrust, AU10TIX, Persona) are all private. Twilio and Stripe have embedded KYC into their broader platforms but it is not their primary revenue line. This represents a potential future IPO catalyst to watch.

**Regulatory Compliance Tech — Bundled or private.** NICE Actimize (embedded in NICE Systems, Nasdaq: NICE) and Fiserv (core banking + compliance bundled) provide the dominant AML/SAR solutions, but they are large-cap conglomerates where RegTech is not the primary revenue driver. Pure-play RegTech companies (Napier, ComplyAdvantage, Flagright) remain private. Watch for an IPO wave as BSA enforcement tightens.

---

## Key Questions to Answer Before Writing the Sector Framework

1. **BNPL credit cycle durability:** Do Affirm and SoFi's AI underwriting models outperform FICO-based lenders through a credit tightening cycle, or do charge-off rates converge with legacy banks at the trough?
2. **Bank charter advantage vs. BaaS moat:** Does SoFi's bank charter (deposit funding advantage) outcompete pure BaaS API platforms (Unit, Column) as funding costs normalize?
3. **LatAm digital banking runway:** How much of Nubank's and MercadoPago's TAM is still unpenetrated, and what is the credit quality risk as they expand into lower-income tiers?
4. **Open banking data moat:** As Plaid/MX data access becomes commoditized under Section 1033 (CFPB open banking rule), do incumbent aggregators retain their moat, or does data access become a utility?
5. **AI model commoditization:** Does the availability of foundation LLMs (GPT-4o, Claude, Gemini) erode the underwriting model moat of Upstart and Affirm, or do proprietary training datasets remain the durable differentiator?
6. **Regulatory rate risk:** How does the CFPB's evolving stance on BNPL classification (credit card equivalent vs. open-end credit) affect Affirm's disclosure and capital requirements?

---

## Interrelationship Anchors

### Inputs (this sector consumes from)
| From Sector | From Tier | Product / Signal |
|---|---|---|
| Compute Infrastructure | AI Model Serving (GPU cluster) | Real-time fraud scoring, credit decisioning, LLM-powered commerce AI inference — GPU cluster inference endpoint via AWS SageMaker / Azure ML / GCP Vertex |
| Cybersecurity | Identity & Access Management | SOC monitoring, identity verification integrations, fraud signal feeds, zero-trust API access controls |
| Semiconductors | Design (Compute) — HSM chiplet | Hardware Security Module (HSM) → payment terminal key management, PIN encryption, card issuer key ceremony |

### Outputs (this sector supplies to)
| To Sector | To Tier | Product / Signal |
|---|---|---|
| Compute Infrastructure | Demand Signal | Fintech AI inference workload growth → GPU cluster capacity pull (real-time scoring, LLM advisory, fraud models) |
| Robotics & Edge AI | Edge Commerce | Embedded payment and identity API → autonomous checkout, robot-mediated commerce, edge POS integration |

---

## Research Log
- **2026-05-24** — map-sector run. 8 tiers, 1 full chokepoint (Payment Rails), 2 partial chokepoints (Risk AI, Credit Decisioning), 3 structural gaps (KYC, Payment Rails pure-play, RegTech). New candidates not yet in registry: AFRM, PYPL, SQ, NU, UPST, FLYW, NCNO.

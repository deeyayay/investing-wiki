---
# Layer 1 — Facts KB (machine-readable)
# Written by: /add-ticker (initial), /ticker-monitor (earnings + filings updates).
# Read by: /score-ticker, /screen-stocks, /build-customer-matrix, /ticker-monitor, /daily-dashboard.
# Do NOT add prose to the body of this file.

ticker: SIVE
company: "Sivers Semiconductors"
cik: null
exchange: "Nasdaq Stockholm"
sector: "Interconnect"

management:
  - role: CEO
    name: "Dr. Vickram Vathulya"
    ownership_pct: null
    notes: "Appointed Jul 2024; semiconductor industry veteran"
  - role: CFO
    name: "Heine Thorsgaard"
    ownership_pct: null
    notes: "Appointed Sep 2025; PhD Finance (Copenhagen); prior CFO Napatech 2018–2025"

earnings:
  - quarter: Q1_FY2026
    date: "2026-05-29"
    revenue_b: 0.0619
    eps_nongaap: null
    beat: false
    guidance_next_b: null
    notes: "SEK 61.9M, -22% YoY; US gov shutdown + defense budget delays; pipeline $799M (+77% YTD); 2027 flagged as transformational"
  - quarter: FY2025_restated
    date: "2026-05-29"
    revenue_b: 0.3066
    eps_nongaap: null
    beat: null
    guidance_next_b: null
    notes: "PCAOB restatement: revenue SEK 306.6M, net loss SEK 222.6M (was 186.5M), operating loss SEK 177.8M"
  - quarter: FY2025
    date: "2026-03-01"
    revenue_b: 0.304
    eps_nongaap: null
    beat: null
    guidance_next_b: null
    notes: "+25% YoY; Q4 +17% QoQ; 2028 breakeven target; raised SEK 95M equity + $17M debt"

filings:
  - type: "Interim Report Q1"
    period: "Q1_FY2026"
    date: "2026-05-29"
    url: "https://www.sivers-semiconductors.com/press/sivers-semiconductors-ab-publ-publishes-interim-report-q1-january-march-2026/"
  - type: "Annual Report"
    period: "FY2025"
    date: "2026-05-01"
    url: "https://www.sivers-semiconductors.com/investors/financial-calendar/"

moat:
  type: "IP/Patent + Sole-source"
  pricing_power: "low-medium"
  competition_intensity: "high"
  made_in_usa: false
  notes: "InP DFB laser arrays with proprietary on-wafer coating (yield advantage); CW-WDM MSA founding promoter; Jabil asset-light model; mmWave beamforming for defense/5G/SATCOM"

tech_exposure:
  - technology: "Co-Packaged Optics (CPO)"
    exposure: primary
    notes: "InP ELS laser arrays are direct CPO input; CW-WDM MSA founding promoter; qualified in Ayar Labs SuperNova; Jabil 1.6T transceiver program"
  - technology: "mmWave / 5G / 6G"
    exposure: primary
    notes: "Wireless division: Daybreak 5G/6G ICs for FR3; Tier-1 telecom development contract (end-2026 delivery)"
  - technology: "Defense / Electronic Warfare"
    exposure: partial
    notes: "EW STAR Year 2 Pentagon CHIPS Act grant $6.6M (BAE/MIT LL/Columbia); $800K US defense supplier contract"
  - technology: "LiDAR"
    exposure: partial
    notes: "Strategic LiDAR customer targeting Q4 2026 high-volume ramp; $53–138M lifecycle value"
  - technology: "SATCOM"
    exposure: partial
    notes: "Ka-band: ALL.SPACE $8.2M production order (LEO/MEO/GEO, through 2027); Doosan $1.5M partnership"

demand_chain:
  customer_funding_type: "mixed"
  top_customer_pct: null
  top_3_customers_pct: null
  circular_exposure: "none"
  notes: "CPO: hyperscaler-funded via Ayar Labs, Jabil 1.6T; Defense: US DoD CHIPS Act; Telecom: Tier-1 vendor; SATCOM: ALL.SPACE (UK)"

metrics:
  score: 5.5
  score_label: "Average"
  last_scored: "2026-05-19"
  valuation_fpe: null
  analyst_pt: "SEK 8.0 (Northland, Outperform — as of May 2026)"
  analyst_upside_pct: null

last_updated: "2026-06-21"
next_earnings: null
---

---
ticker: MRVL
company: "Marvell Technology"
cik: "0001058057"
exchange: NASDAQ
sector: "Compute Hardware"

management:
  - role: CEO
    name: "Matt Murphy"
    ownership_pct: null
    notes: "Strong operator; transformed MRVL from storage chip company to AI silicon platform since July 2016; Best CEO in semiconductors (Institutional Investor 2018); not founder-led"
  - role: CFO
    name: "Willem Meintjes"
    ownership_pct: null
    notes: "CFO since Jan 2023; joined Marvell 2016 as SVP Finance, served as Chief Accounting Officer & Treasurer 2018–2023; continuity through full transformation"

earnings: []
# Revenue data from legacy file: FY2026 revenue $8.2B (42% YoY growth); FY2025 operating cash flow $1.68B; data center >70% of revenue
# Earnings table empty — no quarterly structured data yet. Run /ticker-monitor --deep MRVL to populate.

filings:
  - type: DEF 14A
    period: "FY2025"
    date: "2025-05-01"
    url: "https://investor.marvell.com"

moat:
  type: "Architecture + Customer Lock-in"
  pricing_power: "high"
  competition_intensity: "medium"
  made_in_usa: true
  notes: "Deep co-design relationships with hyperscalers (multi-year 3–5 year design cycles = switching cost); SerDes IP leadership; optical DSP technology; TSMC advanced node access. AVGO competes in same custom ASIC space."

tech_exposure:
  - technology: "Custom ASIC"
    exposure: primary
    notes: "Amazon Trainium2 design win confirmed; Google TPU involvement; Microsoft Maia adjacent. Primary beneficiary of hyperscaler custom silicon spend shift."
  - technology: "SerDes / Optical DSP"
    exposure: primary
    notes: "PAM4 DSP chips inside optical transceivers and switch fabrics; plumbing connecting GPUs to each other and to storage."

demand_chain:
  customer_funding_type: "fcf-hyperscaler"
  top_customer_pct: null
  top_3_customers_pct: null
  circular_exposure: "none"
  notes: "Primary customers are Amazon and Google — both FCF-generating hyperscalers. Customer concentration explicitly noted as key risk. Design cycles 18–24 months = lumpy but visible revenue."

metrics:
  score: 7.5
  score_label: "Strong"
  last_scored: "2026-06-17"
  valuation_fpe: null
  analyst_pt: null
  analyst_upside_pct: null

last_updated: "2026-06-17"
next_earnings: "2026-08-27"
---

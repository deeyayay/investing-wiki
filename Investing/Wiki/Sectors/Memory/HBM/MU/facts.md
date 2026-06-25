---
# Layer 1 — Facts KB (machine-readable)
# YAML frontmatter only. Obsidian renders this as a Properties panel.
# Written by: /add-ticker (initial), /ticker-monitor (earnings + filings updates).
# Read by: /score-ticker, /screen-stocks, /build-customer-matrix, /ticker-monitor, /daily-dashboard.
# Do NOT add prose to the body of this file — all content lives in the YAML block above the closing ---.

ticker: MU
company: "Micron Technology"
cik: "0000723125"
exchange: NASDAQ
sector: "Memory"

management:
  - role: CEO
    name: "Sanjay Mehrotra"
    ownership_pct: null
    notes: "Co-founder of SanDisk; joined Micron as CEO in 2017; led pivot from commodity DRAM/NAND to HBM and AI memory. FY2025 total comp ~$30.7M, ~$25.4M in equity awards."
  - role: CFO
    name: "Mark Murphy"
    ownership_pct: null
    notes: "EVP & CFO since 2022; prior CFO of Qorvo; 25+ years finance/GM experience; driving $25B+ CapEx program."

earnings: []
# Append new entries after each earnings event. Most recent first.
# FY2025 full year: Revenue ~$37.4B (+50% YoY), gross margins ~41% (+17pp YoY), HBM ~$2B in Q4 FY2025 (~$8B annualized run rate)

filings:
  - type: DEF 14A
    period: "FY2025"
    date: "2025-11-25"
    url: ""
    notes: "Accession 0000723125-25-000038. CEO equity comp ~$25.4M of ~$30.7M total."

moat:
  type: "Sole-source / IP/Patent"
  pricing_power: "medium"
  competition_intensity: "medium"
  made_in_usa: true
  notes: "One of three HBM suppliers globally (MU, SK Hynix, Samsung); only US-domiciled HBM manufacturer. HBM3E stacked directly on NVDA H200/Blackwell GPUs — ~30% of GPU BOM. Advanced packaging + DRAM/NAND vertical integration. CHIPS Act funding (Idaho, New York fabs). Commodity DRAM/NAND still ~50%+ of revenue — meaningful competitive pressure from SK Hynix and Samsung in non-HBM segments."

tech_exposure:
  - technology: "HBM4"
    exposure: partial
    notes: "Only US HBM maker; HBM is the narrative but NAND still >50% of revenue. HBM4 (>11 Gbps) on track to ramp Q2 CY2026; full CY2026 supply already contracted."
  - technology: "NAND Flash"
    exposure: partial
    notes: "NAND still >50% of revenue. Enterprise SSD and client NAND. Partial beneficiary of agentic AI NAND demand thesis."
  - technology: "CXL Memory"
    exposure: indirect
    notes: "CXL memory modules in development; early-stage adjacency."

demand_chain:
  customer_funding_type: "fcf-hyperscaler"
  top_customer_pct: null
  top_3_customers_pct: null
  circular_exposure: "minor"
  notes: "Primary HBM demand is NVDA (FCF-funded; H200/Blackwell GPU allocations). Hyperscalers are the downstream end-customer for AI compute. Some circular exposure: HBM → NVDA → AI cloud → hyperscaler loop, but anchored in real FCF. Commodity DRAM/NAND demand is diversified across PC, mobile, cloud."

metrics:
  score: 6.5
  score_label: "Strong"
  last_scored: "2026-06-17"
  valuation_fpe: null
  analyst_pt: null
  analyst_upside_pct: null

last_updated: "2026-06-17"
next_earnings: "2026-06-24"
---
# Migration note: migrated from legacy MU.md to three-layer structure 2026-06-17. Run /ticker-monitor --deep MU to populate earnings array and analyst coverage.

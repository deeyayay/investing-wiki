---
# Layer 1 — Facts KB (machine-readable)
# YAML frontmatter only. Obsidian renders this as a Properties panel.
# Written by: /add-ticker (initial), /ticker-monitor (earnings + filings updates).
# Read by: /score-ticker, /screen-stocks, /build-customer-matrix, /ticker-monitor, /daily-dashboard.
# Do NOT add prose to the body of this file — all content lives in the YAML block above the closing ---.

ticker: TICKER
company: "Company Name"
cik: "0000000000"        # SEC CIK; null for foreign-listed non-filers
exchange: NASDAQ         # NASDAQ / NYSE / TSX / TSE / TWSE / Euronext / etc.
sector: "Sector Name"

management:
  - role: CEO
    name: "—"
    ownership_pct: null
    notes: "—"
  - role: CFO
    name: "—"
    ownership_pct: null
    notes: "—"

earnings: []
# Append new entries after each earnings event. Most recent first.
# - quarter: Q1_FY2027
#   date: "YYYY-MM-DD"
#   revenue_b: 0.0
#   eps_nongaap: 0.00
#   beat: true            # true / false / null (if miss)
#   guidance_next_b: null # next quarter guidance; null if not provided
#   notes: "Key metrics from earnings call, max 20 words"

filings: []
# Append new entries as filings are confirmed.
# - type: 10-Q           # 10-K / 10-Q / 8-K / DEF 14A / etc.
#   period: "Q1_FY2027"
#   date: "YYYY-MM-DD"
#   url: ""

moat:
  type: "—"              # e.g. Platform/Ecosystem / Sole-source / IP/Patent / Cost / Network
  pricing_power: "—"     # high / medium / low
  competition_intensity: "—"   # low / medium / high
  made_in_usa: null      # true / false / partial
  notes: "—"

tech_exposure: []
# Link this ticker to technology races in Technology Preferences.md.
# exposure: primary / partial / indirect / none
# - technology: "NAND Flash"
#   exposure: primary
#   notes: "~100% revenue from NAND; enterprise + client SSD"
# - technology: "Proof-of-Stake"
#   exposure: partial
#   notes: "Ethereum staking revenue stream; not primary business"

demand_chain:
  customer_funding_type: null  # "fcf-hyperscaler" | "debt-neocloud" | "pre-ipo-ecosystem" | "mixed" | "diversified"
  top_customer_pct: null       # % of revenue from largest single customer (integer, e.g. 35)
  top_3_customers_pct: null    # % of revenue from top 3 customers combined
  circular_exposure: null      # "none" | "minor" | "significant"
  notes: "—"                   # brief description of primary customer ecosystem

metrics:
  score: null            # Composite score from /score-ticker (0–10)
  score_label: "—"       # Unrivaled / Strong / Average / Reassess
  last_scored: null      # "YYYY-MM-DD"
  valuation_fpe: null    # Forward P/E
  analyst_pt: null       # Analyst consensus price target
  analyst_upside_pct: null

last_updated: "YYYY-MM-DD"
next_earnings: null      # "YYYY-MM-DD" — predicted date of next earnings release; updated by /ticker-monitor
---

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

profile:
  currency: USD          # reporting currency of financial_history / balance_sheet (USD / EUR / SEK / JPY / ...)
  fiscal_year_end: null  # "MM-DD", e.g. "12-31"; null if unknown
  dividend: null         # "none" | "paying" | "suspended"; null if unknown

management:
  - role: CEO
    name: "—"
    ownership_pct: null
    notes: "—"
  - role: CFO
    name: "—"
    ownership_pct: null
    notes: "—"

financial_history: []
# Annual full-year figures, most recent first. ~5-6 fiscal years + one forward
# estimate row. Powers the ticker-page visual summary (revenue trajectory bars,
# EBIT margin line, KPI tiles). Units are millions of profile.currency.
# SEC filers: backfilled by scripts/financials_backfill_fetch.py (EDGAR XBRL);
# foreign non-filers: from annual reports via web research.
# Appended once per year at the annual report by /ticker-monitor; the estimate
# row is replaced (only exception to append-only) when guidance changes.
# - fy: FY2026
#   end_date: "YYYY-MM-DD"   # fiscal year end covered by this row
#   revenue_m: 0.0
#   ebit_m: null             # operating income; null if not disclosed
#   ebit_margin_pct: null    # derived: ebit_m / revenue_m * 100, 1 decimal
#   fcf_m: null              # operating cash flow minus capex; null if unavailable
#   estimate: false          # true for the forward row (guidance or consensus)
#   source: "10-K"           # 10-K / 20-F / annual report / guidance / consensus

balance_sheet:
  as_of: null            # "YYYY-MM-DD" — balance sheet date
  cash_m: null           # cash + equivalents (+ short-term investments if reported together)
  debt_m: null           # total borrowings; 0.0 if debt-free, null if unknown
  net_cash_m: null       # cash_m - debt_m; negative = net debt

segments: []
# Business segment revenue mix, largest first. From the 10-K/annual report
# segment note. Percentages are of latest full-year revenue (~ is fine).
# Replaced wholesale when the company re-segments (exception to append-only).
# - name: "Segment Name"
#   revenue_pct: 42
#   description: "max 12 words on what's in this segment"

business_units: []
# Named subsidiaries / operating units worth tracking individually — mainly for
# holdings and conglomerates. Omit (leave []) for single-business companies.
# - name: "Subsidiary Name"
#   tag: null              # "crown_jewel" for the standout asset; null otherwise
#   description: "max 25 words: what it does + why it matters"

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

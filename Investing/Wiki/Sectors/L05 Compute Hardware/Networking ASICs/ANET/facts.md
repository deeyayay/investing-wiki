---
# Layer 1 — Facts KB (machine-readable)
# YAML frontmatter only. Obsidian renders this as a Properties panel.
# Written by: /add-ticker (initial), /ticker-monitor (earnings + filings updates).
# Read by: /score-ticker, /screen-stocks, /build-customer-matrix, /ticker-monitor, /daily-dashboard.
# Do NOT add prose to the body of this file — all content lives in the YAML block above the closing ---.

ticker: ANET
company: "Arista Networks"
cik: "0001313925"
exchange: NYSE
sector: "Cloud Infrastructure"

management:
  - role: CEO
    name: "Jayshree Ullal"
    ownership_pct: 2.33
    notes: "Founder-era executive; joined 2008; scaled ANET from startup to S&P 500; 29% rev growth FY2025 at 48% non-GAAP op margin; accelerated $10B rev target 2yr early"
  - role: CFO
    name: "Chantelle Breithaupt"
    ownership_pct: null
    notes: "Oversaw Q4 2025 — first quarter ANET crossed $1B net income. Appointed CFO after prior tenure."
  - role: "Co-founder / Chief Architect"
    name: "Andreas Bechtolsheim"
    ownership_pct: null
    notes: "Drives hardware/silicon roadmap. Founder of ANET."

earnings: []
# No structured earnings data yet — migrate from ANET.md narrative: FY2025 29% rev growth, 48% non-GAAP op margin, $1B net income Q4 2025
# - quarter: Q4_FY2025
#   date: "2026-02-18"
#   revenue_b: null
#   eps_nongaap: null
#   beat: null
#   guidance_next_b: null
#   notes: "First quarter with $1B net income; accelerated $10B revenue target 2yr ahead of schedule"

filings: []

moat:
  type: "Platform/Ecosystem"
  pricing_power: "high"
  competition_intensity: "medium"
  made_in_usa: true
  notes: "EOS (Extensible Operating System) software ecosystem lock-in — customers build entire network automation stack around Arista APIs. 400G/800G switching leadership. Deep hyperscaler relationships (Meta, MSFT, GOOGL). InfiniBand (NVDA Quantum-X) is the primary competitive alternative for AI backend clusters."

tech_exposure:
  - technology: "Ethernet switching (AI networking)"
    exposure: primary
    notes: "Dominant high-speed Ethernet switching for hyperscaler AI clusters; 400G/800G/1.6T roadmap"
  - technology: "Co-Packaged Optics (CPO)"
    exposure: partial
    notes: "CPO adoption in switch ASICs is a future adjacency; ANET benefits as Ethernet wins AI backend networking"

demand_chain:
  customer_funding_type: "fcf-hyperscaler"
  top_customer_pct: 15
  top_3_customers_pct: null
  circular_exposure: "none"
  notes: "Primary customers: Meta (~15% revenue), Microsoft, Google — all large-cap FCF-funded hyperscalers. No debt-funded neocloud material exposure."

metrics:
  score: 8.0
  score_label: "Unrivaled"
  last_scored: "2026-06-17"
  valuation_fpe: null
  analyst_pt: null
  analyst_upside_pct: null

last_updated: "2026-06-17"
next_earnings: "2026-08-03"
---

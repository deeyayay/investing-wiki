---
ticker: INTC
company: "Intel Corporation"
cik: "0000050863"
exchange: NASDAQ
sector: "Semiconductors"

management:
  - role: CEO
    name: "Lip-Bu Tan"
    ownership_pct: null
    notes: "Appointed March 2025; former CEO/Executive Chairman Cadence Design Systems"
  - role: CFO
    name: "David Zinsner"
    ownership_pct: null
    notes: "CFO since January 2022; ex-Micron; leading foundry financial restructuring"

earnings:
  - quarter: Q1_FY2026
    date: "2026-04-23"
    revenue_b: 13.6
    eps_nongaap: 0.29
    beat: true
    guidance_next_b: 14.3
    notes: "Revenue +7% YoY beat guidance ($11.7-12.7B); Non-GAAP GM 41.0%; IFS rev $5.4B +20% QoQ"
  - quarter: Q4_FY2025
    date: "2026-01-22"
    revenue_b: 13.7
    eps_nongaap: null
    beat: null
    guidance_next_b: 12.2
    notes: "Revenue -4% YoY; Non-GAAP gross margin 37.9%; guided Q1 2026 at $11.7-12.7B"
  - quarter: FY2025
    date: "2026-01-22"
    revenue_b: 52.9
    eps_nongaap: null
    beat: null
    guidance_next_b: null
    notes: "FY2025 flat vs FY2024 $53.1B; GAAP gross margin 34.8%; Non-GAAP 36.7%"

filings:
  - type: 10-Q
    period: "Q1_FY2026"
    date: "2026-04-24"
    url: "https://www.sec.gov/Archives/edgar/data/0000050863/000005086326000079/intc-20260328.htm"
  - type: 8-K
    period: "Q1_FY2026"
    date: "2026-04-23"
    url: "https://www.sec.gov/Archives/edgar/data/0000050863/000005086326000077/intc-20260423.htm"
  - type: 8-K
    period: "Q4_FY2025"
    date: "2026-01-22"
    url: "https://www.sec.gov/Archives/edgar/data/0000050863/000005086326000009/intc-20260122.htm"

moat:
  type: "IP/Patent + Platform"
  pricing_power: "medium"
  competition_intensity: "high"
  made_in_usa: true
  notes: "x86 ISA lock-in, EMIB packaging IP, 25yr silicon photonics R&D, CHIPS Act US fab"

tech_exposure:
  - technology: "Advanced Packaging (EMIB / EMIB-T / Foveros)"
    exposure: primary
    notes: "EMIB-T at 8x reticle today; >12x roadmap by 2028; ~90% yield; enables CPO at scale"
  - technology: "Co-Packaged Optics (CPO)"
    exposure: primary
    notes: "Only IDM with in-house silicon photonics + EMIB + JEDEC-certified fiber attach published"
  - technology: "Intel Foundry Services (18A process)"
    exposure: primary
    notes: ">$15B lifetime commitments signed; NVIDIA $5B + SoftBank $2B strategic investment"
  - technology: "x86 CPU (Client + Datacenter)"
    exposure: primary
    notes: "Core Ultra (client) + Xeon (server); x86 inference workload persistence thesis"

metrics:
  score: 6.5
  score_label: "Strong"
  last_scored: "2026-06-07"
  valuation_fpe: 73.0
  analyst_pt: 83.00
  analyst_upside_pct: null

last_updated: "2026-06-07"
---

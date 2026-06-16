---
# Layer 1 — Facts KB (machine-readable)
ticker: MPWR
company: "Monolithic Power Systems, Inc."
cik: "0001280452"
exchange: NASDAQ
sector: "Electronic Components"

management:
  - role: CEO
    name: "Michael Hsing"
    ownership_pct: null
    notes: "Founder-led (co-founded MPS in 1997). Engineer-CEO; proprietary BCD process and analog design culture are his signature."
  - role: CFO
    name: "Rob Dean (interim)"
    ownership_pct: null
    notes: "Interim CFO as of mid-2026 (9-yr Corporate Controller); succeeds Bernie Blegen, who announced retirement Feb 2026 after the FY2025 10-K. Refresh via /ticker-monitor --deep MPWR."

earnings: []
# High-growth fabless analog/power; data-center segment now the largest growth driver. Net-cash balance sheet.

filings: []

moat:
  type: "Proprietary BCD process + analog design IP + design-win lock-in"
  pricing_power: high
  competition_intensity: medium
  made_in_usa: false
  notes: "Fabless analog/power-management IC designer (US HQ, foundry-based manufacturing). Moat is a proprietary BCD (Bipolar-CMOS-DMOS) process co-developed with foundry partners plus deep analog design IP that is hard to second-source once designed into a board. A disproportionate AI/data-center beneficiary: every GPU compute node needs dense, high-efficiency multi-phase power delivery, and MPS's vertical power modules are designed into NVIDIA Blackwell / Vera Rubin board power. Concentration risk (NVIDIA-linked demand) and rich valuation are the offsets."

tech_exposure:
  - technology: "Power-management ICs & vertical power modules for AI servers"
    exposure: primary
    notes: "Maps to the AI Buildout Stack Power Infrastructure rail → 'Power Management ICs' box (Power Semiconductors group). Vertical power delivery + 800V-architecture content scales with every accelerator node; the AI data-center segment is MPS's fastest-growing end market."

metrics:
  score: null
  score_label: "—"
  last_scored: null
  valuation_fpe: null
  analyst_pt: null
  analyst_upside_pct: null

last_updated: "2026-06-15"
next_earnings: null
---

# Healthcare & Drug Discovery Stack — AI in Biology

*Last updated: 2026-06-27 — created as a dedicated domain stack for the dashboard's Supply Chain domain switcher.*

This file is the **authoritative taxonomy** for the **Healthcare & Drug Discovery** domain on the dashboard. It models AI-driven drug discovery and healthcare as a layered stack — from **Therapeutic Applications** (top — the drugs and clinical tools) down to **Compute & Data Infrastructure** (bedrock — the sequencing and GPU compute that power them).

It renders through the same `renderL0()` engine via the dashboard's domain switcher (`STACKS["healthcare"]` in `Investing/Output/Dashboard/index.html`). Like the Robotics stack and unlike AI Buildout, it has **no cross-cutting rails**.

> **First-cut scaffold.** This domain is the least-mapped of the three. Most boxes are **coverage gaps** (`"gap": true`, rendered hatched/"unmapped") awaiting `/map-sector "Healthcare & Drug Discovery"` and ticker onboarding. The relocated **AI Drug Discovery** vertical (formerly an L01 box on the AI Buildout stack) anchors the top layer here. Seed tickers: **QTRX, ABCL, RXRX** (already in the wiki under `L01 Application / AI Drug Discovery`).

---

## The 6 Layers (first cut)

| # | Layer | What it is | Coverage |
|---|-------|------------|----------|
| L01 | **Therapeutic Applications** | AI-discovered drugs · clinical decision support | RXRX, ABCL wired; diagnostics AI is a gap |
| L02 | **Molecular Design & Simulation** | Generative chemistry · protein structure | ABCL (biologics) wired; gen-chemistry is a gap |
| L03 | **Clinical Trial AI** | Trial design · patient matching · real-world evidence | gap — awaiting `/map-sector` |
| L04 | **Lab Automation & Instruments** | Biomarker detection · wet-lab robotics | QTRX wired; lab robotics is a gap |
| L05 | **Genomics & Sequencing** | Sequencing · multi-omics data | gap (ILMN candidate) |
| L06 | **Compute & Data Infrastructure** | GPU compute · biomedical data platforms | gap (NVDA chip) |

---

## Machine-readable definition

The `daily-dashboard` skill copies the JSON block below verbatim into the `STACKS["healthcare"].stack` assignment in `index.html`. Keep the two in sync. As `/map-sector` fills a layer, remove `"gap": true` and wire the box to its new `(slug, tier)`.

```json
{
  "generated":"2026-06-27",
  "intro":"AI-driven <strong>drug discovery & healthcare</strong> as a layered stack — from therapeutic applications at the top down to the genomics and compute that power them. This is a <strong>first-cut scaffold</strong>: many layers are still coverage gaps (hatched) awaiting <code>/map-sector</code> and ticker onboarding. Click a <strong>box</strong> or a <strong>ticker</strong> to drill in.",
  "layers":[
    {"num":"01","name":"Therapeutic Applications","hue":200,"tag":"AI-discovered drugs · clinical decision support","boxes":[
      {"label":"AI-Native Drug Discovery Platforms","slug":"healthcare","tier":"Drug Discovery Platforms","chips":["RXRX","ABCL"],"fn":"End-to-end AI platforms for target identification, molecular design, and candidate generation."},
      {"label":"Clinical Decision Support & Diagnostic AI","gap":true,"chips":[]}
    ]},
    {"num":"02","name":"Molecular Design & Simulation","hue":255,"tag":"generative chemistry · protein structure","boxes":[
      {"label":"Generative Chemistry & Protein Structure","gap":true,"chips":[]},
      {"label":"Antibody & Biologics Discovery","slug":"healthcare","tier":"Biologics Discovery","chips":["ABCL"],"fn":"AI-driven antibody discovery platforms."}
    ]},
    {"num":"03","name":"Clinical Trial AI","hue":288,"tag":"trial design · patient matching · real-world evidence","boxes":[
      {"label":"Trial Design & Patient Recruitment AI","gap":true,"chips":[]},
      {"label":"Real-World Evidence & Data","gap":true,"chips":[]}
    ]},
    {"num":"04","name":"Lab Automation & Instruments","hue":150,"tag":"biomarker detection · wet-lab robotics","boxes":[
      {"label":"Ultra-Sensitive Detection & Biomarkers","slug":"healthcare","tier":"Biomarker Detection","chips":["QTRX"],"fn":"Quanterix Simoa — ultrasensitive digital protein detection for biomarkers."},
      {"label":"Lab Automation & Robotics","gap":true,"chips":[]}
    ]},
    {"num":"05","name":"Genomics & Sequencing","hue":92,"tag":"sequencing · multi-omics data","boxes":[
      {"label":"Sequencing Platforms","gap":true,"chips":["ILMN"]},
      {"label":"Multi-Omics & Spatial Biology","gap":true,"chips":[]}
    ]},
    {"num":"06","name":"Compute & Data Infrastructure","hue":42,"tag":"GPU compute · biomedical data platforms","boxes":[
      {"label":"AI Compute for Biology","gap":true,"chips":["NVDA"]},
      {"label":"Biomedical Data Platforms","gap":true,"chips":[]}
    ]}
  ],
  "connectors":[
    {"label":"designed by"},
    {"label":"validated through"},
    {"label":"measured by"},
    {"label":"informed by"},
    {"label":"computed on"}
  ],
  "rails":[]
}
```

---

## Build-out queue (out of scope for the initial scaffold)

1. `/map-sector "Healthcare & Drug Discovery"` — define the real value chain and fill the gap boxes.
2. `/scout-tickers "Healthcare & Drug Discovery" --tier "Clinical Trial AI"` (and other gap tiers) — find investable pure-plays.
3. `/add-ticker` for high-conviction hits (e.g. ILMN for sequencing, plus any clinical-AI / lab-automation names surfaced).

Seed tickers already in the wiki: **QTRX, ABCL** (RXRX is a candidate in `Monitor Registry.yaml`). Verify homes before wiring.

---

## Maintenance

- Keep this JSON block and `STACKS["healthcare"].stack` in `index.html` in sync — `/daily-dashboard --refresh-data` regenerates the dashboard from the three stack files.
- This is a scaffold — expect the layer set and labels to change as `/map-sector` formalizes the taxonomy. Treat the 6 layers above as provisional, not canonical-from-a-graphic (unlike AI Buildout and Robotics).

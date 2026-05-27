# Daily Dashboard — Ecosystem Map Viewer

Deploys the ecosystem map via `gh-pages` to GitHub Pages. The HTML and embedded `DATA` object live in `Investing/Output/Dashboard/index.html` as the source of truth.

**Dashboard URL:** `https://deeyayay.github.io/investing-wiki`
*GitHub Pages serves the `gh-pages` branch — every push auto-deploys within ~1 minute.*

**Flags:**
- *(none)* — deploy existing `index.html` to gh-pages as-is
- `--refresh-data` — re-read source files, update the `DATA` block in `index.html`, then deploy
- `--no-push` — write changes locally only, skip deployment

---

## Default path (no flags)

Run the deploy steps in Phase 3. No file reads needed.

---

## `--refresh-data` path

### Phase 1 — Read source files (parallel, up to 12 reads)

Run all reads in parallel.

**Dimension Map** (`Investing/Wiki/Reference/Dimension Map.md`):
- Extract: `name`, `dimension` (D1–D5), `folder` slug, `status`
- Skip sectors where `status === "planned"`
- Folder slug overrides: Compute Infrastructure → `AI Infrastructure`, Energy & Power → `Clean Energy`, Materials & Mining → `Metals & Mining`, Space & Communications → `Space & Comms`, Fintech & Commerce AI → `Fintech & E-Commerce`

**Supply chain maps** — for each active sector read `Investing/Wiki/Sectors/[folder]/_Supply Chain Map.md`:
- From the `## Value Chain` table extract only: `tier` (col[0]), `chokepoint` (col[4])
- Normalize: "Yes" → "Y"; skip header/separator rows

**Ecosystem Interrelationships** (`Investing/Wiki/Reference/Ecosystem Interrelationships.md`):
- From `## Dependency Graph` extract: `from`, `from_tier`, `to`, `to_tier`, `flow`, `product`, `chokepoint`
- Keep only rows where `chokepoint === "Y"` (after normalizing "Yes" → "Y")
- Deduplicate by `(from, to)` sector pair — keep first occurrence

### Phase 2 — Update DATA in index.html

Read `Investing/Output/Dashboard/index.html`. Locate the line starting with `const DATA = {` and replace the entire `DATA` object (through the matching closing `};`) with the newly assembled object:

```javascript
const DATA = {
  generated: "YYYY-MM-DD",
  sectors: [
    { slug: "semiconductors", name: "Semiconductors", dimension: "D1",
      tiers: [
        { tier: "Silicon Wafer Production", chokepoint: "Y" },
        // ...
      ]
    },
    // one entry per active sector, D1→D5 order
  ],
  edges: [
    { from: "Materials & Mining", from_tier: "Silicon Refining",
      to: "Semiconductors", to_tier: "Wafer Production",
      flow: "Material", product: "Polysilicon → silicon wafer", chokepoint: "Y" },
    // ~12 Y-chokepoint edges
  ]
};
```

Slug format: lowercase, spaces and `&` → `-`, strip non-alphanumeric. E.g. `"Photonics & Optical"` → `"photonics-optical"`.

Write the updated file back to `Investing/Output/Dashboard/index.html` and copy to `Investing/Output/Dashboard/[DATE].html`.

---

## Phase 3 — Deploy to gh-pages

```bash
git fetch origin gh-pages
git checkout gh-pages
git show [CURRENT_BRANCH]:Investing/Output/Dashboard/index.html > index.html
git add index.html
git commit -m "Deploy ecosystem map [DATE]"
git push -u origin gh-pages
git checkout [CURRENT_BRANCH]
```

If `--no-push` is set, stop before these steps.

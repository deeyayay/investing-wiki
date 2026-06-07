---
description: Parse the Tweets.md staging dump (or any pasted signal) into individual signal notes, create/update Social Mentions in signals.md (Layer 3) for each ticker, and update the Sentiment Index. Usage: /ingest-sentiment [--source article|musing] [--author "@handle"]
allowed-tools: Read, Write, Edit, Glob, mcp__mcp-obsidian__obsidian_get_file_contents, mcp__mcp-obsidian__obsidian_append_content, mcp__mcp-obsidian__obsidian_patch_content
---

# Ingest Sentiment

Parse raw signals from the staging inbox into the structured social mentions database. Writes to Layer 3 (signals.md) only — never reads or modifies facts.md or analysis.md.

**Staging file:** `Investing/Raw/Inbox/Tweets.md`
**Signal folder:** `Investing/Raw/Sentiment/`
**Sentiment Index:** `Investing/Wiki/Reference/Sentiment Index.md`
**Registry:** `Investing/Wiki/Reference/Monitor Registry.yaml`

**Input:** `$ARGUMENTS` — optional flags:
- `--source article|musing` — override source type (default: `tweet`)
- `--author "@handle"` — author for all signals in this batch

---

## Step 1 — Read staging content

Read `Investing/Raw/Inbox/Tweets.md`.

If the file is empty or contains only whitespace, print:
```
Tweets.md is empty — nothing to ingest. Paste content there and run again.
```
Then stop.

---

## Step 2 — Split into individual signals

Split the raw content into individual signal blocks. Primary split boundary: a URL line matching `https://x.com/` or `https://twitter.com/`. Each block of text above a URL = one signal. The URL belongs to the signal above it.

If no URLs are present (articles or musings), treat the entire content as one signal.

For each signal block, extract:
- **Raw text** — full pasted content including embedded URL
- **URL** — the trailing URL line if present, else empty
- **Tickers** — all `$TICKER` patterns; also include clearly-referenced public tickers written without `$`; deduplicate, sort alphabetically
- **Sectors** — infer which sector(s) the signal touches using sector names from Monitor Registry.yaml
- **Is sector-level** — flag true if the signal makes a broad claim about a sector (TAM, macro dynamics, sector thesis) rather than being purely ticker-specific

---

## Step 3 — Batch review

Present the full batch in a single review table:

```
─────────────────────────────────────────
Batch preview — [M] signals
─────────────────────────────────────────
 #  | Tickers        | Sectors              | Sector-level?
----|----------------|----------------------|--------------
 1  | PENG, MRVL     | Photonics & Optical  | no
 2  | SIVE, LITE     | Photonics & Optical  | yes
─────────────────────────────────────────
```

Then ask:
> "Review the table. Reply with corrections: `[#] add TICKER`, `[#] remove TICKER`, `[#] sector Sector Name`, or `[#] skip`. Type **ok** to accept all and file."

Wait for reply. Apply corrections. If a signal is marked `skip`, drop it.

---

## Step 4 — Write signal notes

For each signal (not skipped), generate:
- **date** — today's date `YYYY-MM-DD`
- **slug** — `[date]-[first-ticker-or-topic]-[first-3-words]`, lowercase, hyphens, max 60 chars
- **filepath** — `Investing/Raw/Sentiment/[slug].md`

Write the file:
```markdown
---
date: [date]
source: tweet
tickers: [TICKER1, TICKER2]
sectors: [Sector Name]
author: ""
url: "[url]"
tags: []
---

[full raw text]
```

Print `✓ [slug].md` for each file saved.

---

## Step 5 — Update ticker signals.md files (Layer 3 only)

Read `Investing/Wiki/Reference/Monitor Registry.yaml`. Build the ticker → path map from the `tickers:` key.

For each ticker across all filed signals:

**A) Ticker exists in Monitor Registry.yaml:**
1. Read `[path]/signals.md`
2. Check for `## Social Mentions` section
3. If section **does not exist**: insert before `## Research Log`:
   ```markdown
   ## Social Mentions

   | Date | Signal | Source |
   |------|--------|--------|
   | [date] | [[slug]] | tweet |
   ```
4. If section **exists**: append a new row to the table — never rewrite existing rows

Do NOT read or touch facts.md or analysis.md.

**B) Ticker NOT in Monitor Registry.yaml (stub):**
1. Infer the most likely sector from the signal context. Use the folder name exactly as it appears in `Investing/Wiki/Sectors/`.
2. Check if `Investing/Wiki/Sectors/[sector]/[TICKER]/signals.md` already exists
3. If **does not exist**: create the ticker folder and write a minimal signals.md:
   ```markdown
   # [TICKER] — Signals
   *Social mentions only — not yet in Monitor Registry. Run `/add-ticker [TICKER]` to onboard fully.*

   ---

   ## Social Mentions

   | Date | Signal | Source |
   |------|--------|--------|
   | [date] | [[slug]] | tweet |

   ---

   ## Research Log
   ```
4. If **exists**: append a row to the Social Mentions table

Do NOT register stub tickers in Monitor Registry.yaml.

---

## Step 6 — Update sector pages

For each signal flagged as sector-level, for each sector it touches:

1. Check if `Investing/Wiki/Sectors/[Sector Name]/Sector Sentiment.md` exists
2. If **does not exist**: create it with a Signals table:
   ```markdown
   # [Sector Name] — Social Mentions

   Sector-level signals and commentary from external sources.

   ---

   ## Signals

   | Date | Signal | Source | Summary |
   |------|--------|--------|---------|
   | [date] | [[slug]] | tweet | [one-sentence summary of the sector-level claim] |
   ```
3. If **exists**: append a row to the Signals table

---

## Step 7 — Update Sentiment Index

Read `Investing/Wiki/Reference/Sentiment Index.md`.

**Ticker Summary table:**
- New ticker: add row with Mentions = 1, Last Signal = date, Wiki = `[[TICKER]]`, Status = `monitored` or `stub`
- Existing ticker: increment Mentions, update Last Signal if newer

Columns: `Ticker | Wiki | Status | Mentions | Last Signal`

**Recent Signals feed** — prepend one line per signal:
```
[date] · [source] · [[slug]] · [ticker1], [ticker2], ...
```
Keep max 30 entries.

Rewrite the Sentiment Index with updated table and feed using Edit.

---

## Step 8 — Archive processed content

Ask: "Clear Tweets.md now that signals are filed? (yes / no)"

If yes: overwrite `Investing/Raw/Inbox/Tweets.md` with an empty file. Print `✓ Tweets.md cleared.`
If no: leave unchanged.

---

## Step 9 — Summary

```
─────────────────────────────────────────
Ingest complete
─────────────────────────────────────────
Signals filed:        [N]
Signals skipped:      [N]
Tickers tagged:       [list]
  - Monitored:        [list — signals.md updated]
  - Stubs created:    [list — new signals.md created]
Sector pages updated: [list or "none"]
Sentiment Index:      updated
─────────────────────────────────────────
```

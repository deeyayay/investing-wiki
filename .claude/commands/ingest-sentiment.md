---
description: Parse the Tweets.md staging dump (or any pasted signal) into individual signal notes, create/update Social Mentions sections on ticker and sector wiki pages, and update the Sentiment Index. Usage: /ingest-sentiment [--source article|musing] [--author "@handle"]
allowed-tools: Read, Write, Edit, Glob, mcp__mcp-obsidian__obsidian_get_file_contents, mcp__mcp-obsidian__obsidian_append_content, mcp__mcp-obsidian__obsidian_patch_content
---

# Ingest Sentiment

Parse raw signals from the staging inbox into the structured social mentions database.

**Staging file:** `Investing/Raw/Inbox/Tweets.md`
**Signal folder:** `Investing/Raw/Sentiment/`
**Sentiment Index:** `Investing/Wiki/Reference/Sentiment Index.md`
**Monitor Registry:** `Investing/Wiki/Reference/Monitor Registry.md`

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

Split the raw content into individual signal blocks. The primary split boundary is a URL line matching `https://x.com/` or `https://twitter.com/`. Each block of text above a URL (down to the previous URL) = one signal. The URL belongs to the signal above it.

If no URLs are present (e.g. articles or musings pasted without links), treat the entire content as one signal.

For each signal block, extract:
- **Raw text** — full pasted content including embedded URL
- **URL** — the trailing `https://x.com/...` line if present, else empty
- **Tickers** — all `$TICKER` patterns; deduplicate; sort alphabetically. Also include clearly-referenced public tickers written without `$` if you are confident they refer to a traded stock.
- **Sectors** — infer which sector(s) the signal touches based on content. Use the existing sector names from the Monitor Registry: `Photonics & Optical`, `Semiconductors`, `AI Infrastructure`, `Cybersecurity`, `Fintech & E-Commerce`, `Clean Energy`, `Space & Comms`. A signal can touch multiple sectors. If none apply, leave empty.
- **Is sector-level** — flag true if the signal makes a broad claim about a sector (e.g. TAM size, macro dynamics, sector thesis) rather than being purely ticker-specific.

---

## Step 3 — Auto-assign and present batch for review

Internally process all signals. For each signal, note:
- Extracted tickers
- Inferred sectors
- Whether it's sector-level (true/false)

Present the full batch in a single review table:

```
─────────────────────────────────────────
Batch preview — [M] signals
─────────────────────────────────────────
 #  | Tickers                                   | Sectors              | Sector-level?
----|-------------------------------------------|----------------------|--------------
 1  | PENG, MRVL, SMCI                          | Photonics & Optical, Semiconductors | no
 2  | BOT                                       | —                    | no
 3  | SIVE, LITE, AAOI, COHR, POET, FN, IQE, LPK| Photonics & Optical | yes
...
─────────────────────────────────────────
```

Then ask in a single message:
> "Review the table. Reply with corrections in the format `[#] add TICKER`, `[#] remove TICKER`, `[#] sector Sector Name`, or `[#] skip`. Type **ok** to accept all and file."

Wait for user reply. Apply any corrections. If a signal is marked `skip`, drop it. Then proceed.

---

## Step 4 — Write signal notes

For each signal (not skipped), generate:
- **date** — today's date `YYYY-MM-DD`
- **slug** — `[date]-[first-ticker-or-topic]-[first-3-words]`, lowercase, hyphens, max 60 chars
- **filename** — `[slug].md`
- **filepath** — `Investing/Raw/Sentiment/[filename]`

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

## Step 5 — Update ticker wiki pages

Read the Monitor Registry to build the full ticker → file path map.

For each ticker across all filed signals:

**A) Ticker exists in Monitor Registry:**
1. Read the wiki page
2. Check for `## Social Mentions` section
3. If section **does not exist**: insert before `## Research Log` (or append to end of file if missing):
   ```markdown
   ## Social Mentions

   | Date | Signal | Source |
   |------|--------|--------|
   | [date] | [[slug]] | tweet |
   ```
4. If section **already exists**: append a new row to the table only — never rewrite existing rows.

**B) Ticker NOT in Monitor Registry (stub):**
1. Infer the most likely sector from the signal context. Use the folder name exactly as it appears in `Investing/Wiki/Sectors/` (e.g. `Photonics & Optical`).
2. Check if a file already exists at `Investing/Wiki/Sectors/[sector]/[TICKER].md`
3. If file **does not exist**: create it:
   ```markdown
   # [TICKER]
   *Social mentions only — not yet in Monitor Registry. Run `/add-ticker [TICKER]` to onboard fully.*

   ---

   ## Social Mentions

   | Date | Signal | Source |
   |------|--------|--------|
   | [date] | [[slug]] | tweet |
   ```
4. If file **already exists** (previously created stub): append a row to the Social Mentions table.

Do NOT register stub tickers in the Monitor Registry.

---

## Step 6 — Update sector pages

For each signal flagged as sector-level, for each sector it touches:

1. Read `Investing/Wiki/Sectors/[Sector Name]/_Sector Framework.md`
2. Check for a `## Social Mentions` section
3. If section **does not exist**: append to end of file:
   ```markdown
   ---

   ## Social Mentions

   *Sector-level signals and commentary. Maintained by `/ingest-sentiment`.*

   | Date | Signal | Source | Summary |
   |------|--------|--------|---------|
   | [date] | [[slug]] | tweet | [one-sentence summary of the sector-level claim] |
   ```
4. If section **already exists**: append a new row to the table only — never rewrite existing rows.

---

## Step 7 — Update Sentiment Index

Read `Investing/Wiki/Reference/Sentiment Index.md`.

**Ticker Summary table** — for each ticker across the batch:
- New ticker: add row with Mentions = 1, Last Signal = date, Wiki = `[[TICKER]]` if in Monitor Registry else `[[TICKER]]` linking to stub, Status = `monitored` or `stub`
- Existing ticker: increment Mentions, update Last Signal if newer

Columns: `Ticker | Wiki | Status | Mentions | Last Signal`

**Recent Signals feed** — prepend one line per signal:
```
[date] · [source] · [[slug]] · [ticker1], [ticker2], ...
```
Keep max 30 entries.

Rewrite the Sentiment Index with updated table and feed using the Edit tool.

---

## Step 8 — Archive processed content

Ask: "Clear Tweets.md now that signals are filed? (yes / no)"

If yes: overwrite `Investing/Raw/Inbox/Tweets.md` with an empty file. Print `✓ Tweets.md cleared.`
If no: leave unchanged. Print `Tweets.md left as-is.`

---

## Step 9 — Summary

```
─────────────────────────────────────────
Ingest complete
─────────────────────────────────────────
Signals filed:        [N]
Signals skipped:      [N]
Tickers tagged:       [list]
  - Monitored:        [list — existing wiki pages updated]
  - Stubs created:    [list — new bare pages created]
Sector pages updated: [list or "none"]
Sentiment Index:      updated
─────────────────────────────────────────
```

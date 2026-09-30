---
description: Stop watching a ticker — remove it from Watchlist.md so the daily brief no longer scans it. Non-destructive: the registry entry, the ticker's page and all its history stay. The inverse of /track. Usage: /untrack TICKER [--no-push]
allowed-tools: Bash(python3 scripts/check_registry.py:*), Bash(git add:*), Bash(git commit:*), Bash(git push:*), Read, Edit
---

# Untrack — take a ticker off the watchlist

`/brief` scans every ticker named in a `Watchlist.md` table. Removing a ticker's
rows from that file is what stops the scan, and it is the *only* thing this skill
removes. Everything the KB learned about the name stays: untracking is about
what gets scanned daily, not about forgetting.

This is the inverse of `/track`, which is why the registry entry and page are
deliberately left alone: `/track TICKER` later finds the name already registered
and offers to add just the Watchlist row back, so changing your mind costs one
command.

## Step 1 — Find it

Read `Investing/Wiki/Reference/Watchlist.md`. List every table row whose first
cell is `$1`, across **all** sections (a name can appear in more than one, for
example High Conviction and Core Holdings).

- **No rows** → say so and stop. Also read `Monitor Registry.yaml`: if `$1` is
  registered, add that it is not on the watchlist, so the default daily pass
  already skips it (only `--all` scans the full registry). Do not edit anything.
- **A row in Core Holdings** → that section is owner-maintained and lists
  positions the owner actually holds. **Stop and ask** before removing it, naming
  the ticker and its tier. Proceed only on a clear yes. Removing a holding changes
  which names the brief prioritises, and nothing else in the repo knows it is held.

## Step 2 — Remove the rows

Edit `Watchlist.md`:

1. Delete every row for `$1`. Change nothing else in the file — no other tickers,
   no headings, no prose.
2. If the row was in **Active Coverage** and the italic line above that table
   carries a count (`… 18 names.`), decrease it by one. The other sections carry
   no counts.
3. Set `*Last updated:*` at the top to today's date.

Do **not** touch `Monitor Registry.yaml`, the ticker's page, `Topics.yaml`, or
the "Not yet covered" section.

## Step 3 — Leave a trace

The KB is append-only, so record the decision where the name's history lives.
Find the ticker's page from its registry `path:`:

- `layout: three-layer` → `signals.md` in that folder
- `layout: legacy` → the page itself
- `layout: unpaged`, or no page on disk → skip this step

Append **one** line to its `## Research Log`, in the same style that log already
uses (a `- **YYYY-MM-DD** — …` bullet, or a table row matching its columns):

`Untracked via /untrack — removed from Watchlist.md; no longer scanned by /brief. Page and history kept.`

If the page has no `## Research Log` section, skip the step. Do not add sections.

## Step 4 — Verify, summarise, publish

```
python3 scripts/check_registry.py
```

Must report **0 errors**. The registry was not edited, so any new error means
something else is wrong; say so rather than committing over it.

```
✅ TICKER untracked
   Removed from: High Conviction, Core Holdings   (rows deleted: N)
   Kept: registry entry, page, history
   Undo: /track TICKER
```

Commit as `Untrack TICKER` and push unless `--no-push`. The dashboard reads
`Watchlist.md` live, so the name disappears from its Watchlist tab on the next
load, with no redeploy.

## Rules

- Never delete the registry entry, the ticker's page, or any of its history.
- Never edit any ticker other than `$1`.
- Never remove a Core Holdings row without an explicit yes in this conversation.
- No searches, no research. This skill only edits two files and commits.

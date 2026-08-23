---
description: Add a ticker to the watchlist with the minimum ceremony that makes it visible to the daily brief — a registry entry, a one-file page, and a Watchlist row. No three-layer scaffolding, no research pass. Use it on a lead from the brief's discovered list, or any name worth watching before it is worth studying. Usage: /track TICKER [--sector "Sector"] [--tier core|rocket|compounder] [--note "why"] [--no-push]
allowed-tools: Bash(curl -s*), Bash(python3 scripts/check_registry.py:*), Bash(python3 scripts/repair_registry.py:*), Bash(mkdir *), Bash(git add:*), Bash(git commit:*), Bash(git push:*), Read, Edit, Write
---

# Track — put a ticker on the watchlist

The cheap front door. A name reaches the daily brief the moment it is in the
registry and named on the Watchlist; everything else — three-layer folders,
thesis, scoring — is earned later by names that prove worth it.

The KB's problem has never been too few pages. 56 ticker pages already sit on
disk that no registry entry claims, so they are invisible to every skill. This
skill exists so watching a name costs a row, not a research project.

## Step 1 — Check what already exists

Read `Investing/Wiki/Reference/Monitor Registry.yaml`.

- **Already registered** → say so, print its `path` and `layout`, and stop.
  If it is missing from Watchlist.md, offer to add just the row.
- **Listed under `candidates:`** → good, this is the promotion path. Remove it
  from `candidates:` as part of Step 3.
- **Not present** → continue.

Then check disk, because an unregistered page very likely already exists:

```
python3 scripts/check_registry.py
```

Its warnings list every page the registry does not claim. If `$1` is among
them, **register the existing page — do not create a second one.**

## Step 2 — Resolve identity

Company name, exchange and CIK from SEC:

```
curl -s -H "User-Agent: $SEC_USER_AGENT" \
  "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=$1&type=&count=1&output=atom"
```

Not an SEC filer (foreign listing) → `cik: null` and carry on. That is a normal
state, not a failure. Do not research the business here; that is `/dig`.

Sector: use `--sector` if given. Otherwise infer from the 12-layer stack in
`AI Buildout Stack.md` and **say which you chose and why** — a wrong sector is
cheap to fix now and annoying later.

## Step 3 — Register

Sector folders are layer-prefixed on disk (`L05 Compute Hardware`); `sector:`
is that name with the prefix stripped. Append under `tickers:`:

```yaml
  TICKER:
    company: "Legal Company Name"
    cik: "0001234567"
    exchange: NASDAQ
    sector: "Compute Hardware"
    path: "Investing/Wiki/Sectors/L05 Compute Hardware/[Tier]/TICKER.md"
    layout: legacy
    score: null
    next_earnings: null
    notes: "why this is worth watching"
```

`layout` must match what `path` points at — `legacy` for the single file this
skill creates, `three-layer` only if you registered an existing folder. Update
`last_updated`.

## Step 4 — Create the page (skip if one already exists on disk)

One file, `[TICKER].md`, in the sector's tier folder:

```markdown
# TICKER — Company Name
*Tracked YYYY-MM-DD via /track. Not yet researched.*

**Why tracked:** [--note, or the headline that surfaced it]

## One-Line Thesis
_None yet — run `/dig TICKER` to establish one._

## News & Alpha Log

| Date | Item | Source | So what |
|------|------|--------|---------|

## Social Mentions

| Date | Handle | Class | Claim | Status |
|------|--------|-------|-------|--------|
```

The One-Line Thesis heading is deliberately present but empty: `/brief` reads
it to decide whether a ticker can be triaged for drift, and an honest "none
yet" is what makes the gap visible in the Watchlist's coverage count.

## Step 5 — Add to Watchlist.md

Without this the ticker is registered but **not scanned daily** — Watchlist.md
is the scope input for `/brief`.

With `--tier`, add to Core Holdings with that tier. Otherwise append to
**Active Coverage**:

`| TICKER | Company Name | Sector | — | _No thesis yet — /dig TICKER_ |`

## Step 6 — Verify, summarise, publish

```
python3 scripts/check_registry.py
```

Must report **0 errors**. A new warning naming `$1` means `path` and disk
disagree — fix it before committing.

```
✅ TICKER — Company Name tracked
   Sector: X (inferred|given) | CIK: Y | layout: legacy
   Watchlist: Active Coverage | now scanned by /brief
   Next: /dig TICKER to establish a thesis
```

Commit as `Track TICKER` and push unless `--no-push`.

## Rules

- Never create a page for a ticker that already has one — register it instead.
- No research pass, no web search beyond the SEC identity lookup. A name that
  deserves research deserves `/dig`.
- Never invent a thesis or a score to fill a field. Empty is accurate.

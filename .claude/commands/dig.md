---
description: On-demand deep dive on one ticker, for when the daily brief flags something a headline cannot settle. Pulls SEC filings, reads the actual documents, re-tests the thesis leg by leg, and writes the verdict to analysis.md. This is the expensive skill — use it on the handful of names that matter, not on a schedule. Usage: /dig TICKER [--filings-only] [--score] [--no-push]
allowed-tools: Bash(curl -s*), Bash(python3 scripts/check_registry.py:*), Bash(git add:*), Bash(git commit:*), Bash(git push:*), Read, Edit, Write, WebSearch, WebFetch
---

# Dig — deep dive on one ticker

`/brief` triages headlines and deliberately never searches. When it flags
something a headline cannot settle, this is where that goes. One ticker at a
time, primary sources first.

## Step 1 — Locate the ticker

Read `Investing/Wiki/Reference/Monitor Registry.yaml` and find `$1`. Use its
`layout` field:

| `layout` | Then |
|---|---|
| `three-layer` | `path` is a folder — read `analysis.md`, and `facts.md` for the CIK |
| `legacy` | `path` is a single `.md` — read it; offer to migrate at the end |
| `unpaged` | Registered with nothing on disk — run `/track $1` first, then come back |

Not in the registry at all → say so and suggest `/track $1`. Do not silently
create pages.

## Step 2 — Filings first (primary sources)

The CIK is in facts.md. `cik: null` means a foreign listing that does not file
with the SEC — skip to Step 3 and say so rather than reporting nothing found.

```
curl -s -H "User-Agent: $SEC_USER_AGENT" \
  "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[CIK]&type=&dateb=&owner=include&count=20&output=atom"
```

`SEC_USER_AGENT` must contain a contact email or SEC answers 403. If it is
unset, the request will fail — say so plainly rather than retrying.

Read the atom feed for filings since the date in analysis.md's
`**Last validated:**`. For anything material, **fetch and read the actual
document** from its `filing-href` — that is the entire point of this skill.
Priority order:

- **8-K** — read the item numbers. 1.01 material agreement · 2.02 results ·
  2.03 debt · 5.02 officer change · 7.01 Reg FD · 8.01 other
- **10-Q / 10-K** — go to MD&A and risk-factor *changes*, not the whole filing
- **Form 4** — cluster buying by multiple insiders is the signal; a single
  scheduled 10b5-1 sale is not

Full-text search across all filings, when you need to test a specific claim:

```
curl -s -H "User-Agent: $SEC_USER_AGENT" \
  'https://efts.sec.gov/LATEST/search-index?q=%22SEARCH+PHRASE%22&forms=8-K'
```

Stop here if `--filings-only`.

## Step 3 — Targeted research

Now search — but with a specific question, never "news about $1". Good
questions look like: *did the customer concentration change?* · *is the
capacity expansion funded?* · *did a competitor win the socket?*

Prefer, in order: the company's own filings and IR releases → a transcript →
reporting that cites one of those. A headline restating another headline adds
nothing and costs tokens.

## Step 4 — Re-test the thesis leg by leg

Take the One-Line Thesis and Investment Thesis from analysis.md and break them
into their claims. Test each against what Steps 2–3 actually found:

| Verdict | Meaning |
|---|---|
| `CONFIRMED` | A primary source supports it |
| `INTACT` | Nothing contradicts it, no fresh confirmation either |
| `WEAKENED` | Real evidence against, thesis survives |
| `BROKEN` | A load-bearing claim is false |

Say which source settled each one. "No evidence either way" is a legitimate
and useful verdict — record it as `INTACT`, do not manufacture a conclusion.

`BROKEN` is the verdict headlines are not allowed to reach and this skill is.
If you reach it, say so directly and lead the summary with it.

## Step 5 — Write

**facts.md** — new filings, earnings figures, management changes. Facts only,
no interpretation.

**analysis.md** —
- Conviction Log: `| date | event ≤15 words | ↑/↓/→ | why, 1–2 sentences |`
- Drift status + `**Last validated:**` — this skill *may* set `Broken`
- Thesis verdict table from Step 4, under a `### Deep Pass — YYYY-MM-DD` heading

**signals.md** — one Research Log line:
`- **YYYY-MM-DD** — 🔬 DIG | [n] filings read, [m] claims tested, verdict: [X]`

Append-only. Never rewrite an existing Conviction Log row.

## Step 6 — Score (only with --score)

Score on the 6-criterion rubric using what this run established, write the
Scoring Summary to analysis.md, and update `score:` in Monitor Registry.yaml.
Re-run `python3 scripts/check_registry.py` afterwards.

## Step 7 — Summary + publish

```
🔬 $1 — deep pass YYYY-MM-DD
Filings read: N | Claims tested: M
Verdict: CONFIRMED x | INTACT x | WEAKENED x | BROKEN x
[the one thing that matters, in a sentence]
Thesis action: none | drift updated | escalate
```

Commit as `Dig $1 YYYY-MM-DD` and push unless `--no-push`.

## Cost

This skill reads real documents and searches — it is the expensive one, by
design. Run it on the handful of names the brief actually flags. If you find
yourself running it across a sector, that is `--all` on `/brief` instead.

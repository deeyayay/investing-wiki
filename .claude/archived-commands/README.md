# Archived skills

These 13 skills are **unloaded** — they live outside `.claude/commands/`, so Claude Code does not
register them and they cost nothing at session start. They are kept, not deleted.

They were archived on 2026-08-23 when the skill surface collapsed to three:

| Now | Replaces |
|---|---|
| `/brief` | `watchlist-refresh`, `ingest-sentiment`, the `--news-only` half of `ticker-monitor` |
| `/dig` | `ticker-monitor --deep`, `score-ticker` (via `--score`), `stock-research-all` |
| `/track` | `add-ticker` (the lightweight path), `scout-tickers` / `screen-stocks` candidate promotion |

## Why

Eight of the thirteen existed to *build* KB structure — `map-sector`,
`build-customer-matrix`, `scout-tickers`, `screen-stocks`, `detect-shifts`,
`ingest-ecosystem`, `score-ticker`, `stock-research-all` — against a stated goal of
tracking news and sentiment. ~2,500 lines of prompt for a job three skills do.

The structure they built is still there and still read; what stopped is building more of it.

## Restoring one

```bash
git mv .claude/archived-commands/NAME.md .claude/commands/
```

Then check it against the current conventions before trusting it. All of these predate:

- the registry's `layout:` field (`three-layer` | `legacy` | `unpaged`), so any of them that
  writes a registry entry will write one that `scripts/check_registry.py` flags
- layer-prefixed sector folders (`L05 Compute Hardware`), so hardcoded paths in them are stale
- `Topics.yaml` and the discovery funnel
- the multi-provider fetcher and its exit-status contract

`daily-dashboard` is the most likely to be wanted back — the HTML dashboard is still a
reasonable occasional deep-dive view, it just is not a daily habit.

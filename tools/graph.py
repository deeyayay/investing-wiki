#!/usr/bin/env python3
"""
graph.py — directed relational graph over sentiment signal notes.

Each signal note may carry a `relationships` YAML field that encodes
explicit directed edges between tickers. Undirected co-mention edges
are always derived from the `tickers` list as a fallback layer.

Edge direction convention:
    from → to  means  "from creates demand for / depends on to"

    customer   : from buys from to  (META → AMD = Meta buys AMD EPYC)
    design_win : from integrates to's component  (NVDA → INTC = DGX uses Xeon)
    investor   : from has equity stake in to
    supplier   : from sells to to  (explicit supply direction)
    partner    : bilateral strategic relationship  (encode one direction)
    competitor : from competes directly with to

Usage:
    python tools/graph.py                    # summary
    python tools/graph.py --query NVDA       # all edges for a ticker
    python tools/graph.py --export           # write tools/graph.json
    python tools/graph.py --export --out /path/to/graph.json
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")


REPO_ROOT = Path(__file__).parent.parent
SIGNAL_DIR = REPO_ROOT / "Investing" / "Raw" / "Sentiment"
DEFAULT_EXPORT = REPO_ROOT / "tools" / "graph.json"


# ── Parsing ───────────────────────────────────────────────────────────────────

def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    try:
        end = text.index("---", 3)
    except ValueError:
        return {}
    return yaml.safe_load(text[3:end]) or {}


def load_signals(signal_dir: Path = SIGNAL_DIR) -> list[dict]:
    signals = []
    for path in sorted(signal_dir.glob("*.md")):
        if path.name.startswith("."):
            continue
        fm = parse_frontmatter(path)
        if not fm:
            continue
        signals.append({
            "slug":          path.stem,
            "date":          str(fm.get("date", "")),
            "tickers":       _as_list(fm.get("tickers")),
            "sectors":       _as_list(fm.get("sectors")),
            "relationships": _as_list(fm.get("relationships")),
            "source":        fm.get("source", "tweet"),
            "author":        fm.get("author", ""),
        })
    return signals


def _as_list(val) -> list:
    if val is None:
        return []
    if isinstance(val, list):
        return val
    return [val]


# ── Graph construction ────────────────────────────────────────────────────────

def build_graph(signals: list[dict]) -> tuple[dict, list[dict]]:
    """
    Returns:
        nodes : {ticker: {mentions, dates, slugs, sectors}}
        edges : list of edge dicts, each with a `directed` bool
    """
    nodes: dict[str, dict] = defaultdict(lambda: {
        "mentions": 0, "dates": [], "slugs": [], "sectors": set()
    })
    edges: list[dict] = []
    seen_cooccur: set[tuple] = set()

    for sig in signals:
        date  = sig["date"]
        slug  = sig["slug"]
        tickers = sig["tickers"]

        # Register nodes
        for t in tickers:
            nodes[t]["mentions"] += 1
            nodes[t]["dates"].append(date)
            nodes[t]["slugs"].append(slug)
            for s in sig["sectors"]:
                nodes[t]["sectors"].add(s)

        # Explicit directed edges from `relationships` field
        for rel in sig["relationships"]:
            if not isinstance(rel, dict):
                continue
            src = rel.get("from", "").upper()
            tgt = rel.get("to",   "").upper()
            if not src or not tgt:
                continue
            edges.append({
                "from":     src,
                "to":       tgt,
                "type":     rel.get("type", "related"),
                "note":     rel.get("note", ""),
                "date":     date,
                "slug":     slug,
                "directed": True,
            })
            # Ensure both endpoints are registered as nodes
            for t in (src, tgt):
                if t not in nodes:
                    nodes[t] = {"mentions": 0, "dates": [], "slugs": [], "sectors": set()}

        # Undirected co-mention edges (one per unique pair per signal)
        for i, a in enumerate(tickers):
            for b in tickers[i + 1:]:
                key = (min(a, b), max(a, b), slug)
                if key in seen_cooccur:
                    continue
                seen_cooccur.add(key)
                edges.append({
                    "from":     a,
                    "to":       b,
                    "type":     "co-mention",
                    "note":     "",
                    "date":     date,
                    "slug":     slug,
                    "directed": False,
                })

    # Serialise sets
    for t in nodes:
        nodes[t]["sectors"] = sorted(nodes[t]["sectors"])

    return dict(nodes), edges


# ── Query ─────────────────────────────────────────────────────────────────────

def query_ticker(ticker: str, nodes: dict, edges: list[dict]) -> None:
    ticker = ticker.upper()
    if ticker not in nodes:
        print(f"\n  {ticker} not found in graph.\n")
        return

    outgoing  = [e for e in edges if e["directed"] and e["from"] == ticker]
    incoming  = [e for e in edges if e["directed"] and e["to"]   == ticker]
    cooccur   = [e for e in edges if not e["directed"] and ticker in (e["from"], e["to"])]

    n = nodes[ticker]
    print(f"\n{'─'*64}")
    print(f"  {ticker}  ·  {n['mentions']} mention(s)  ·  {', '.join(n['sectors']) or '—'}")
    print(f"{'─'*64}")

    if outgoing:
        print("\n  Outgoing — creates demand for / depends on:")
        for e in sorted(outgoing, key=lambda x: x["date"], reverse=True):
            note = f"  ← {e['note']}" if e["note"] else ""
            print(f"    → {e['to']:<8}  [{e['type']}]  {e['date']}{note}")
            print(f"               {e['slug']}")

    if incoming:
        print("\n  Incoming — depended upon by:")
        for e in sorted(incoming, key=lambda x: x["date"], reverse=True):
            note = f"  ← {e['note']}" if e["note"] else ""
            print(f"    ← {e['from']:<8}  [{e['type']}]  {e['date']}{note}")
            print(f"               {e['slug']}")

    if cooccur:
        others = sorted({
            e["to"] if e["from"] == ticker else e["from"]
            for e in cooccur
        })
        print(f"\n  Co-mentioned with ({len(others)}): {', '.join(others)}")

    if not outgoing and not incoming and not cooccur:
        print("\n  No edges recorded yet.")

    print()


# ── Export ────────────────────────────────────────────────────────────────────

def export_json(nodes: dict, edges: list[dict], out_path: Path = DEFAULT_EXPORT) -> None:
    """
    Writes a D3-compatible JSON file:
        nodes : [{id, mentions, sectors}]
        links : [{source, target, type, weight, dates, slugs, notes}]  — directed only
        co_occurrences : [{source, target, date, slug}]
    """
    # Aggregate directed edges: merge multiple signals for the same (src, tgt, type) triple
    agg: dict[tuple, dict] = defaultdict(lambda: {
        "weight": 0, "dates": [], "slugs": [], "notes": []
    })
    for e in edges:
        if not e["directed"]:
            continue
        key = (e["from"], e["to"], e["type"])
        agg[key]["weight"] += 1
        agg[key]["dates"].append(e["date"])
        agg[key]["slugs"].append(e["slug"])
        if e["note"]:
            agg[key]["notes"].append(e["note"])

    graph = {
        "nodes": [
            {"id": t, "mentions": d["mentions"], "sectors": d["sectors"]}
            for t, d in sorted(nodes.items())
        ],
        "links": [
            {
                "source": k[0],
                "target": k[1],
                "type":   k[2],
                "weight": v["weight"],
                "dates":  sorted(set(v["dates"])),
                "slugs":  v["slugs"],
                "notes":  v["notes"],
            }
            for k, v in sorted(agg.items())
        ],
        "co_occurrences": [
            {"source": e["from"], "target": e["to"], "date": e["date"], "slug": e["slug"]}
            for e in edges if not e["directed"]
        ],
    }

    out_path.write_text(json.dumps(graph, indent=2))
    print(
        f"✓ {out_path.relative_to(REPO_ROOT)}  "
        f"({len(graph['nodes'])} nodes · "
        f"{len(graph['links'])} directed edges · "
        f"{len(graph['co_occurrences'])} co-mentions)"
    )


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    args = sys.argv[1:]
    signals      = load_signals()
    nodes, edges = build_graph(signals)

    if "--query" in args:
        idx    = args.index("--query")
        ticker = args[idx + 1] if idx + 1 < len(args) else ""
        if not ticker:
            sys.exit("Usage: --query TICKER")
        query_ticker(ticker, nodes, edges)

    elif "--export" in args:
        out = DEFAULT_EXPORT
        if "--out" in args:
            idx = args.index("--out")
            out = Path(args[idx + 1])
        export_json(nodes, edges, out)

    else:
        directed  = [e for e in edges if e["directed"]]
        cooccur   = [e for e in edges if not e["directed"]]

        print(f"\nSignals loaded:    {len(signals)}")
        print(f"Unique tickers:    {len(nodes)}")
        print(f"Directed edges:    {len(directed)}")
        print(f"Co-mention edges:  {len(cooccur)}")

        if directed:
            print("\nDirected edges:")
            for e in sorted(directed, key=lambda x: x["date"], reverse=True):
                note = f"  ({e['note']})" if e["note"] else ""
                print(f"  {e['from']:>8} → {e['to']:<8}  [{e['type']}]{note}")

        print("\nTop tickers by mention:")
        for t, d in sorted(nodes.items(), key=lambda x: -x[1]["mentions"])[:15]:
            print(f"  {t:<8}  {d['mentions']} mention(s)  {', '.join(d['sectors']) or '—'}")
        print()


if __name__ == "__main__":
    main()

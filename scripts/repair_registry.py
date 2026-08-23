#!/usr/bin/env python3
"""One-shot repair for Investing/Wiki/Reference/Monitor Registry.yaml.

Sector folders were renamed to layer-prefixed names without updating the
registry, so 73 of 77 `path:` values pointed at folders that no longer exist.
This rewrites `path:` (and the `sector:` derived from it) to match disk, and
stamps each ticker with an explicit `layout:` so the integrity check can tell a
three-layer folder from an unmigrated single-file page.

Conventions settled here:
  * sector folders on disk keep the "Lxx " layer prefix
  * `sector:` is that folder name with the prefix stripped (human-readable)
  * `layout: three-layer` -> `path:` is a folder holding facts/analysis/signals
  * `layout: legacy`      -> `path:` is the single .md page, pre-migration

Usage: python3 scripts/repair_registry.py [--dry-run]
"""
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(REPO_ROOT, "Investing", "Wiki", "Reference", "Monitor Registry.yaml")
SECTORS_DIR = os.path.join(REPO_ROOT, "Investing", "Wiki", "Sectors")
LAYER_PREFIX_RE = re.compile(r"^L\d\d ")
LAYER_FILES = ("facts.md", "analysis.md", "signals.md")


def index_disk():
    """ticker -> (relative path, layout). Three-layer folders win over legacy files."""
    found = {}
    for root, dirs, files in os.walk(SECTORS_DIR):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for d in list(dirs):
            folder = os.path.join(root, d)
            if any(os.path.isfile(os.path.join(folder, f)) for f in LAYER_FILES):
                found[d] = (os.path.relpath(folder, REPO_ROOT), "three-layer")
        for f in files:
            if not f.endswith(".md") or f.startswith("_") or f in LAYER_FILES:
                continue
            ticker = f[:-3]
            if ticker == "Sector Sentiment" or ticker in found:
                continue
            found[ticker] = (os.path.relpath(os.path.join(root, f), REPO_ROOT), "legacy")
    return found


def sector_of(rel_path):
    """Top-level sector folder for a path, with the Lxx layer prefix stripped."""
    parts = rel_path.split(os.sep)
    return LAYER_PREFIX_RE.sub("", parts[3]) if len(parts) > 3 else None


def main():
    dry_run = "--dry-run" in sys.argv
    disk = index_disk()

    with open(REGISTRY, encoding="utf-8") as f:
        lines = f.read().split("\n")

    key_re = re.compile(r'^  (?:"([^"]+)"|([A-Za-z0-9.\-]+)):\s*(?:#.*)?$')
    field_re = re.compile(r'^    ([a-z_]+):\s*(.*?)\s*(?:#.*)?$')

    out, current, in_tickers = [], None, False
    repaired, unresolved, already_ok = [], [], []

    for line in lines:
        if line.startswith("tickers:"):
            in_tickers = True
            out.append(line)
            continue
        if line.startswith("candidates:"):
            in_tickers = False
        if not in_tickers:
            out.append(line)
            continue

        m = key_re.match(line)
        if m:
            current = m.group(1) or m.group(2)
            out.append(line)
            continue

        m = field_re.match(line)
        if m and current and m.group(1) in ("path", "sector", "layout"):
            key = m.group(1)
            if key == "layout":
                continue  # regenerated alongside path
            if current not in disk:
                if key == "path":
                    unresolved.append((current, m.group(2).strip().strip('"')))
                    out.append(line)
                    out.append("    layout: unpaged")
                else:
                    out.append(line)
                continue
            rel, layout = disk[current]
            if key == "sector":
                out.append('    sector: "%s"' % sector_of(rel))
                continue
            old = m.group(2).strip().strip('"')
            if old == rel:
                already_ok.append(current)
            else:
                repaired.append((current, old, rel))
            out.append('    path: "%s"' % rel)
            out.append("    layout: %s" % layout)
            continue

        out.append(line)

    text = "\n".join(out)
    text = re.sub(r'^last_updated: ".*"$', 'last_updated: "2026-08-23"', text, flags=re.M)

    if not dry_run:
        with open(REGISTRY, "w", encoding="utf-8") as f:
            f.write(text)

    print("repaired: %d   already correct: %d   unresolved: %d"
          % (len(repaired), len(already_ok), len(unresolved)))
    for t, old, new in repaired:
        print("  %-10s %s  ->  %s" % (t, old, new))
    for t, old in unresolved:
        print("  UNPAGED %-10s registered but no page on disk (path left as %s)" % (t, old))
    return 0


if __name__ == "__main__":
    sys.exit(main())

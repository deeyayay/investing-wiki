#!/usr/bin/env python3
"""Integrity check for Investing/Wiki/Reference/Monitor Registry.yaml.

Every skill resolves ticker folders through the registry, so a stale `path:`
silently breaks the whole toolchain. Run this after any sector-folder rename.

Checks:
  1. every `path:` exists on disk
  2. `layout:` matches what is actually there
       three-layer -> folder holding facts/analysis/signals
       legacy      -> single .md page, not yet migrated
       unpaged     -> registered but nothing on disk (reported, not an error)
  3. `sector:` matches the top-level sector folder, Lxx prefix stripped
  4. ticker pages on disk that no ticker in the registry claims

Exit 0 when clean, 1 on any error. Warnings (unpaged, orphans) do not fail
unless --strict is passed.

Usage: python3 scripts/check_registry.py [--strict]
"""
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(REPO_ROOT, "Investing", "Wiki", "Reference", "Monitor Registry.yaml")
SECTORS_DIR = os.path.join(REPO_ROOT, "Investing", "Wiki", "Sectors")
LAYER_PREFIX_RE = re.compile(r"^L\d\d ")
LAYER_FILES = ("facts.md", "analysis.md", "signals.md")


def parse_registry():
    key_re = re.compile(r'^  (?:"([^"]+)"|([A-Za-z0-9.\-]+)):\s*(?:#.*)?$')
    field_re = re.compile(r'^    ([a-z_]+):\s*(.*?)\s*(?:#.*)?$')
    entries, current, in_tickers = {}, None, False
    with open(REGISTRY, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("tickers:"):
                in_tickers = True
                continue
            if line.startswith("candidates:"):
                break
            if not in_tickers:
                continue
            m = key_re.match(line)
            if m:
                current = m.group(1) or m.group(2)
                entries[current] = {}
                continue
            m = field_re.match(line)
            if m and current:
                entries[current][m.group(1)] = m.group(2).strip().strip('"')
    return {k: v for k, v in entries.items() if v.get("company")}


def disk_tickers():
    found = set()
    for root, dirs, files in os.walk(SECTORS_DIR):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for d in dirs:
            if any(os.path.isfile(os.path.join(root, d, f)) for f in LAYER_FILES):
                found.add(d)
        for f in files:
            if f.endswith(".md") and not f.startswith("_") and f not in LAYER_FILES \
                    and f[:-3] != "Sector Sentiment":
                found.add(f[:-3])
    return found


def main():
    strict = "--strict" in sys.argv
    entries = parse_registry()
    errors, warnings = [], []

    for ticker, e in sorted(entries.items()):
        rel = e.get("path")
        layout = e.get("layout")
        if not rel:
            errors.append("%s: no path" % ticker)
            continue
        abs_path = os.path.join(REPO_ROOT, rel)
        if layout == "unpaged":
            warnings.append("%s: registered but no page on disk" % ticker)
            continue
        if not os.path.exists(abs_path):
            errors.append("%s: path does not exist -> %s" % (ticker, rel))
            continue
        is_folder = os.path.isdir(abs_path) and any(
            os.path.isfile(os.path.join(abs_path, f)) for f in LAYER_FILES)
        actual = "three-layer" if is_folder else ("legacy" if abs_path.endswith(".md") else None)
        if actual is None:
            errors.append("%s: path is neither a three-layer folder nor a .md page -> %s"
                          % (ticker, rel))
        elif layout != actual:
            errors.append("%s: layout says %s, disk says %s" % (ticker, layout, actual))
        parts = rel.split(os.sep)
        expected_sector = LAYER_PREFIX_RE.sub("", parts[3]) if len(parts) > 3 else None
        if expected_sector and e.get("sector") != expected_sector:
            errors.append('%s: sector "%s" but folder says "%s"'
                          % (ticker, e.get("sector"), expected_sector))

    orphans = disk_tickers() - set(entries)
    for t in sorted(orphans):
        warnings.append("%s: page on disk, not in registry" % t)

    for w in warnings:
        print("WARN  " + w)
    for err in errors:
        print("ERROR " + err)
    print("\n%d tickers checked — %d errors, %d warnings"
          % (len(entries), len(errors), len(warnings)))
    return 1 if errors or (strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())

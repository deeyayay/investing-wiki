#!/usr/bin/env python3
"""Annual financials backfill fetcher — the zero-token half of the facts.md
financial_history / balance_sheet blocks (ticker-page visual summary data).

Pulls from the SEC EDGAR XBRL companyfacts API (SEC filers only):
  1. Resolves ticker → CIK via the SEC company_tickers.json index (or --cik).
  2. Extracts ~6 fiscal years of annual revenue, operating income (EBIT),
     and free cash flow (operating cash flow − capex) from 10-K/20-F facts.
  3. Extracts the latest balance-sheet cash and debt.
  4. Prints a ready-to-paste YAML snippet matching _facts-template.md
     (financial_history + balance_sheet), or raw JSON with --json.

What it does NOT cover (Claude research territory): the forward estimate row
(guidance/consensus), segments, business_units, and foreign non-filers
(cik: null) — those come from annual reports via web search. Stdlib only.

Usage:
  python3 scripts/financials_backfill_fetch.py --ticker CRWD [--cik 0001535527]
      [--years 6] [--json]
"""

import argparse
import json
import re
import sys
import urllib.request
from datetime import date

USER_AGENT = "investing-wiki financials-backfill (alexd7@gmail.com)"
ANNUAL_FORMS = {"10-K", "10-K/A", "20-F", "20-F/A", "40-F", "40-F/A"}
# 52/53-week fiscal years and transition periods put annual spans in 330-420 days.
MIN_ANNUAL_DAYS, MAX_ANNUAL_DAYS = 330, 420

# us-gaap concept tags in preference order; first tag with annual data wins.
REVENUE_TAGS = [
    "RevenueFromContractWithCustomerExcludingAssessedTax",
    "Revenues",
    "SalesRevenueNet",
    "RevenueFromContractWithCustomerIncludingAssessedTax",
    "SalesRevenueGoodsNet",
]
EBIT_TAGS = ["OperatingIncomeLoss"]
OCF_TAGS = [
    "NetCashProvidedByUsedInOperatingActivities",
    "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations",
]
CAPEX_TAGS = [
    "PaymentsToAcquirePropertyPlantAndEquipment",
    "PaymentsToAcquireProductiveAssets",
]
CASH_TAGS = [
    "CashAndCashEquivalentsAtCarryingValue",
    "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents",
]
DEBT_TAGS = ["LongTermDebt", "DebtLongtermAndShorttermCombinedAmount"]
DEBT_PART_TAGS = ["LongTermDebtNoncurrent", "LongTermDebtCurrent"]


def fetch_json(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.load(resp)


def resolve_cik(ticker):
    index = fetch_json("https://www.sec.gov/files/company_tickers.json")
    for row in index.values():
        if row["ticker"].upper() == ticker.upper():
            return f"{row['cik_str']:010d}", row["title"]
    return None, None


def parse_iso(s):
    return date(*[int(p) for p in s.split("-")])


def pick_unit(units):
    """Prefer USD; otherwise take the single-currency unit that's present
    (20-F filers report in EUR/JPY/etc.). Skip per-share and ratio units."""
    if "USD" in units:
        return "USD"
    for name in units:
        if re.fullmatch(r"[A-Z]{3}", name):
            return name
    return None


def annual_series(gaap, tags):
    """{end_date: value} of full-fiscal-year facts from annual filings, for the
    first tag that yields data. Latest-filed value wins per end date."""
    for tag in tags:
        units = gaap.get(tag, {}).get("units", {})
        unit = pick_unit(units)
        if not unit:
            continue
        best = {}  # end -> (filed, value)
        for fact in units[unit]:
            if fact.get("form") not in ANNUAL_FORMS or not fact.get("start"):
                continue
            span = (parse_iso(fact["end"]) - parse_iso(fact["start"])).days
            if not (MIN_ANNUAL_DAYS <= span <= MAX_ANNUAL_DAYS):
                continue
            filed = fact.get("filed", "")
            if fact["end"] not in best or filed > best[fact["end"]][0]:
                best[fact["end"]] = (filed, fact["val"])
        if best:
            return {end: v for end, (_, v) in best.items()}, unit
    return {}, None


def latest_instant(gaap, tags):
    """(end_date, value) of the most recent point-in-time fact across tags.
    Latest end date wins; latest filed breaks ties (restatements)."""
    best = None  # (end, filed, value)
    for tag in tags:
        units = gaap.get(tag, {}).get("units", {})
        unit = pick_unit(units)
        if not unit:
            continue
        for fact in units[unit]:
            if fact.get("start"):  # instant facts only
                continue
            key = (fact["end"], fact.get("filed", ""))
            if best is None or key > best[:2]:
                best = (fact["end"], fact.get("filed", ""), fact["val"])
    return (best[0], best[2]) if best else (None, None)


def millions(val):
    return None if val is None else round(val / 1e6, 1)


def build_history(gaap, years):
    revenue, currency = annual_series(gaap, REVENUE_TAGS)
    ebit, _ = annual_series(gaap, EBIT_TAGS)
    ocf, _ = annual_series(gaap, OCF_TAGS)
    capex, _ = annual_series(gaap, CAPEX_TAGS)

    rows = []
    for end in sorted(revenue, reverse=True)[:years]:
        rev_m = millions(revenue[end])
        ebit_m = millions(ebit.get(end))
        fcf_m = None
        if end in ocf:
            fcf_m = millions(ocf[end] - capex.get(end, 0))
        rows.append({
            "fy": f"FY{parse_iso(end).year}",
            "end_date": end,
            "revenue_m": rev_m,
            "ebit_m": ebit_m,
            "ebit_margin_pct": round(ebit_m / rev_m * 100, 1)
            if ebit_m is not None and rev_m else None,
            "fcf_m": fcf_m,
            "estimate": False,
            "source": "10-K",
        })
    return rows, currency


def build_balance_sheet(gaap):
    cash_date, cash = latest_instant(gaap, CASH_TAGS)
    debt_date, debt = latest_instant(gaap, DEBT_TAGS)
    if debt is None:
        nc_date, noncurrent = latest_instant(gaap, DEBT_PART_TAGS[:1])
        c_date, current = latest_instant(gaap, DEBT_PART_TAGS[1:])
        if noncurrent is not None and nc_date == cash_date:
            debt = noncurrent + (current if c_date == nc_date and current else 0)
    elif debt_date != cash_date:
        debt = None  # stale debt figure vs. cash date — leave for research
    cash_m, debt_m = millions(cash), millions(debt)
    return {
        "as_of": cash_date,
        "cash_m": cash_m,
        "debt_m": debt_m,
        "net_cash_m": round(cash_m - debt_m, 1)
        if cash_m is not None and debt_m is not None else None,
    }


def yaml_scalar(v):
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, str) and not re.fullmatch(r"FY\d{4}", v):
        return f'"{v}"'
    return str(v)


def print_yaml(history, balance_sheet, currency):
    print(f"# paste into facts.md — values in millions of {currency}")
    print(f"# profile.currency should be: {currency}")
    print("# add the forward estimate row (estimate: true) from guidance/consensus research")
    print("financial_history:")
    for row in history:
        prefix = "  - "
        for key, val in row.items():
            print(f"{prefix}{key}: {yaml_scalar(val)}")
            prefix = "    "
    print("\nbalance_sheet:")
    for key, val in balance_sheet.items():
        print(f"  {key}: {yaml_scalar(val)}")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--ticker", required=True, help="ticker symbol, e.g. CRWD")
    ap.add_argument("--cik", help="10-digit CIK; skips the ticker-index lookup")
    ap.add_argument("--years", type=int, default=6, help="fiscal years to include (default 6)")
    ap.add_argument("--json", action="store_true", help="raw JSON instead of YAML snippet")
    args = ap.parse_args(argv)

    if args.cik:
        cik, title = args.cik.zfill(10), None
    else:
        cik, title = resolve_cik(args.ticker)
        if not cik:
            print(f"ERROR: {args.ticker} not found in the SEC ticker index — "
                  f"likely a foreign non-filer. Backfill from annual reports "
                  f"via web research instead.", file=sys.stderr)
            return 1

    facts = fetch_json(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json")
    gaap = facts.get("facts", {}).get("us-gaap", {})
    if not gaap:
        print(f"ERROR: no us-gaap facts for CIK {cik} ({facts.get('entityName')}). "
              f"IFRS-only filer — backfill via web research.", file=sys.stderr)
        return 1

    history, currency = build_history(gaap, args.years)
    if not history:
        print(f"ERROR: no annual revenue facts found for CIK {cik} "
              f"({facts.get('entityName')}).", file=sys.stderr)
        return 1
    balance_sheet = build_balance_sheet(gaap)

    if args.json:
        json.dump({
            "ticker": args.ticker.upper(),
            "cik": cik,
            "entity": facts.get("entityName") or title,
            "currency": currency,
            "financial_history": history,
            "balance_sheet": balance_sheet,
        }, sys.stdout, indent=1)
        print()
    else:
        print_yaml(history, balance_sheet, currency)
    return 0


if __name__ == "__main__":
    sys.exit(main())

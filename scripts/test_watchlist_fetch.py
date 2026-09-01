#!/usr/bin/env python3
"""Guard tests for watchlist_refresh_fetch.py — no network, no model tokens.

The failure these cover is the one that hid for seven weeks: every fetch broke,
the script wrote a well-formed digest with zero headlines and exited 0, so
nothing anywhere said the pipeline was dead. Providers are injected here so the
guards are tested deterministically instead of by poking at live hosts.

Usage: python3 scripts/test_watchlist_fetch.py
"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import watchlist_refresh_fetch as w  # noqa: E402

GOOD_DIGEST = {"tickers": [{"ticker": "NVDA", "headlines": [{"t": "old news"}]}]}

RSS_TWO_ITEMS = """<rss><channel>
<item><title>Humanoid robot maker (NASDAQ: FIGR) ships units</title>
<source>Test Wire</source><pubDate>%s</pubDate></item>
<item><title>HBM4 capacity sold out through next year</title>
<source>Test Wire</source><pubDate>%s</pubDate></item>
</channel></rss>""" % (((__import__("email.utils", fromlist=["x"])
                         .format_datetime(__import__("datetime")
                                          .datetime.now(__import__("datetime").timezone.utc))),) * 2)


def item(title, kind="news", url=None):
    return {"t": title, "src": "Test", "d": "2026-08-23", "kind": kind, "url": url}


class GuardTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.digest = os.path.join(self.tmp, "digest.json")
        self._saved = dict(w.PROVIDERS)
        # Keep each test's seen-cache isolated from the real one.
        self._state = w.STATE_PATH
        w.STATE_PATH = os.path.join(self.tmp, "state.json")

    def tearDown(self):
        w.PROVIDERS.clear()
        w.PROVIDERS.update(self._saved)
        w.STATE_PATH = self._state

    def write_good_digest(self):
        with open(self.digest, "w") as f:
            json.dump(GOOD_DIGEST, f)

    def run_fetch(self, provider):
        w.PROVIDERS.clear()
        w.PROVIDERS["test"] = provider
        return w.main(["--tickers", "NVDA,CRDO", "--providers", "test",
                       "--no-topics", "--output", self.digest])

    def digest_tickers(self):
        with open(self.digest) as f:
            return json.load(f)["tickers"]

    def test_every_fetch_failing_exits_nonzero(self):
        def boom(entry, hours):
            raise OSError("tunnel refused")
        self.assertEqual(self.run_fetch(boom), 1)

    def test_every_fetch_failing_preserves_existing_digest(self):
        self.write_good_digest()

        def boom(entry, hours):
            raise OSError("tunnel refused")
        self.run_fetch(boom)
        self.assertEqual(self.digest_tickers(), GOOD_DIGEST["tickers"],
                         "a failed run overwrote a good digest")

    def test_silent_provider_returning_nothing_is_caught(self):
        """A provider answering 200 with zero items is the dangerous failure —
        no exception, no error entry, just a silently empty digest."""
        self.write_good_digest()
        self.assertEqual(self.run_fetch(lambda entry, hours: []), 1)
        self.assertEqual(self.digest_tickers(), GOOD_DIGEST["tickers"])

    def test_healthy_run_writes_and_exits_zero(self):
        rc = self.run_fetch(lambda entry, hours: [item("real headline about " + entry["ticker"])])
        self.assertEqual(rc, 0)
        self.assertTrue(self.digest_tickers())

    def test_quiet_day_with_no_prior_digest_still_writes(self):
        """Nothing new and nothing to lose is a normal outcome, not a failure."""
        self.assertEqual(self.run_fetch(lambda entry, hours: [item("x")]), 0)
        # second run: same items, all now in the seen cache -> no new content
        rc = self.run_fetch(lambda entry, hours: [item("x")])
        self.assertEqual(rc, 0)

    def test_one_provider_dead_other_alive_still_writes_but_warns(self):
        """Degrade, don't die — the reason there is more than one provider."""
        w.PROVIDERS.clear()
        w.PROVIDERS["alive"] = lambda entry, hours: [item("live " + entry["ticker"])]

        def boom(entry, hours):
            raise OSError("blocked")
        w.PROVIDERS["dead"] = boom
        rc = w.main(["--tickers", "NVDA", "--providers", "alive,dead",
                     "--no-topics", "--output", self.digest])
        self.assertEqual(rc, 1, "a dead provider must be reported in the exit status")
        self.assertTrue(self.digest_tickers(), "live provider's items must still be written")

    def test_filings_are_ranked_above_news(self):
        def mixed(entry, hours):
            return [item("a headline"), item("8-K", kind="filing", url="u1")]
        self.run_fetch(mixed)
        first = self.digest_tickers()[0]["headlines"][0]
        self.assertEqual(first["kind"], "filing")

    def test_distinct_filings_sharing_a_title_are_not_deduped(self):
        """Every 8-K is titled '8-K'. Keying on text alone would hide all but one."""
        def two_8ks(entry, hours):
            return [item("8-K", kind="filing", url="accession-1"),
                    item("8-K", kind="filing", url="accession-2")]
        self.run_fetch(two_8ks)
        self.assertEqual(len(self.digest_tickers()[0]["headlines"]), 2)

    def test_topic_pass_records_hits_and_gaps(self):
        """Topics run off the same RSS host, so fetch_url is stubbed to stay offline."""
        saved = w.fetch_url
        w.fetch_url = lambda url, **kw: RSS_TWO_ITEMS
        try:
            w.PROVIDERS.clear()
            w.PROVIDERS["test"] = lambda entry, hours: []
            w.main(["--tickers", "NVDA", "--providers", "test", "--output", self.digest])
        finally:
            w.fetch_url = saved
        with open(self.digest) as f:
            topics = json.load(f)["topics"]
        self.assertTrue(topics, "topic pass produced nothing")
        self.assertTrue(any(t["gaps"] for t in topics),
                        "gaps must survive into the digest — they are the onboarding queue")

    def test_discovery_only_accepts_exchange_tagged_tickers(self):
        """Bare capitalised words (AI, CEO, US) must not become candidates."""
        items = [{"t": "AI startup CEO says US demand is strong"},
                 {"t": "Figure AI rival (NASDAQ: FIGR) raises a round"},
                 {"t": "Another story about (NYSE: XYZ) and NVDA"}]
        found = {d["ticker"] for d in w.discover_tickers(items, known={"NVDA"})}
        self.assertEqual(found, {"FIGR", "XYZ"})

    def test_discovery_skips_already_tracked_tickers(self):
        items = [{"t": "Report on (NASDAQ: NVDA) supply"}]
        self.assertEqual(w.discover_tickers(items, known={"NVDA"}), [])

    def test_topic_query_keeps_inner_quotes(self):
        """A query like '\"HBM\" OR \"HBM4\"' loses its phrase grouping if both
        quote characters get stripped — which silently widens every search."""
        topics = w.parse_topics(w.TOPICS)
        hbm = next(t for t in topics if t["id"] == "hbm-supply")
        self.assertIn('"HBM"', hbm["query"])

    def test_every_topic_ticker_is_registered(self):
        """A topic naming an unregistered ticker cannot be resolved to a folder."""
        known = {e["ticker"] for e in w.parse_registry(w.REGISTRY)}
        for topic in w.parse_topics(w.TOPICS):
            for t in topic["tickers"]:
                self.assertIn(t, known,
                              "topic %s lists unregistered ticker %s (use gaps:)"
                              % (topic["id"], t))

    def test_drift_index_covers_quiet_tickers(self):
        """A drift flag that only shows up when a ticker had news is useless for
        scanning, so drift must be emitted for every scanned ticker."""
        saved = w.extract_thesis
        w.extract_thesis = lambda folder: ("a thesis", "Drifting — made up for the test")
        try:
            # NVDA gets an item, CRDO stays quiet; both must appear in drift_index.
            self.run_fetch(lambda entry, hours:
                           [item("headline")] if entry["ticker"] == "NVDA" else [])
        finally:
            w.extract_thesis = saved
        with open(self.digest) as f:
            digest = json.load(f)
        self.assertEqual(sorted(digest["drift_index"]), ["CRDO", "NVDA"])
        self.assertEqual([t["ticker"] for t in digest["tickers"]], ["NVDA"])

    def test_edgar_window_has_a_floor_below_the_news_window(self):
        """EDGAR's cutoff is date-granular, so the default 36h news window can
        cover barely one calendar day and silently drop filings."""
        seen = {}
        saved = w.fetch_url
        w.fetch_url = lambda url, **kw: (seen.setdefault('url', url), '<feed></feed>')[1]
        try:
            w.parse_edgar_atom = lambda xml, hours: seen.setdefault('hours', hours) and []
            w.provider_edgar({'ticker': 'NVDA', 'cik': '0001045810'}, 36)
        finally:
            w.fetch_url = saved
        self.assertGreaterEqual(seen.get('hours', 0), 96,
                                'filings must look back further than headlines')

    # ---- impact scoring -------------------------------------------------
    # Real headlines from the feed. The false positives below all shipped in a
    # first draft, so they stay as regression guards.
    def test_impact_ranks_structural_news_above_noise(self):
        cases = [
            ("Amazon's stock slips as the FTC alleges billions in hidden ad fees", "regulatory"),
            ("AeroVironment Pockets $51M Army Contract", "deal"),
            ("Nvidia Stock Up 1.5% as $20 Billion Buyback Represents 0.4% of Market Cap", "capital"),
            ("Palo Alto Networks Q4 earnings face a higher bar", "earnings"),
            ("Arista Networks initiated with a Buy at Deutsche Bank", "analyst"),
        ]
        for title, tag in cases:
            sc, got = w.score_impact({"t": title, "kind": "news"})
            self.assertEqual(got, tag, title)
            self.assertGreaterEqual(sc, 40, title)

    def test_impact_sinks_formulaic_filler(self):
        for title, tag in [
            ("Royal London Asset Management Ltd. Purchases 62,892 Shares of SoFi", "ownership"),
            ("Rational Advisors Inc. Decreases Stake in Advanced Micro Devices", "ownership"),
            ("AMD Options Spot-On: On August 31st, 354.77K Contracts Were Traded", "options"),
            ("Amazon.com Inc Stock (AMZN) Moved Down by 3.06% on Aug 31", "pricemove"),
            ("Japan, South Korea Stocks Open Lower and Extend Losses; Kospi drops", "roundup"),
        ]:
            sc, got = w.score_impact({"t": title, "kind": "news"})
            self.assertEqual(got, tag, title)
            self.assertEqual(w.impact_tier(sc), "low", title)

    def test_impact_does_not_promote_clickbait_or_13f_as_deals(self):
        """'to buy' and a bare 'acquires' matched 'A $31 Billion Reason to Buy'
        and 'Acquires Shares of 5,871', ranking both as major deals."""
        for title in ["A $31 Billion Reason to Buy Sandisk Stock Now",
                      "CEO Lip-Bu Tan Just Gave 12 Million Reasons to Buy Intel Stock",
                      "Analysts Expect Nvidia Stock to Soar 47%, But You Shouldn't Rush to Buy"]:
            sc, tag = w.score_impact({"t": title, "kind": "news"})
            self.assertNotEqual(tag, "deal", title)
        sc, tag = w.score_impact(
            {"t": "Old North State Trust LLC Acquires Shares of 5,871 AMD", "kind": "news"})
        self.assertEqual(tag, "ownership")

    def test_analyst_price_target_is_not_company_guidance(self):
        """'Raises Target Price' is an analyst action; putting 'target' in the
        guidance pattern ranked broker notes alongside a real guidance change."""
        sc, tag = w.score_impact(
            {"t": "Scotiabank Maintains Palo Alto Networks With Buy Rating, Raises Target Price to $250",
             "kind": "news"})
        self.assertEqual(tag, "analyst")
        sc2, tag2 = w.score_impact(
            {"t": "Arista Networks Is Still a Buy After a Third Guidance Hike?", "kind": "news"})
        self.assertEqual(tag2, "guidance")
        self.assertGreater(sc2, sc)

    def test_price_recap_is_not_a_product_launch(self):
        """'Key Drivers Unveiled' made a percent-move recap look like a launch."""
        sc, tag = w.score_impact(
            {"t": "SanDisk Stock (SNDK) Moved Up by 3.37% on Aug 31: Key Drivers Unveiled",
             "kind": "news"})
        self.assertEqual(w.impact_tier(sc), "low")

    def test_material_filings_outrank_headlines(self):
        f, _ = w.score_impact({"t": "8-K — Current report (items 1.01, 2.03)", "kind": "filing"})
        best_news = max(sc for sc, _ in
                        (w.score_impact({"t": t, "kind": "news"}) for t in
                         ["FTC sues Amazon", "Company awarded a contract", "raises full-year guidance"]))
        self.assertGreater(f, best_news)

    def test_routine_paperwork_does_not_rank_as_a_filing(self):
        """Form 4s, 144s and N-PX reports arrive constantly. Ranking them as
        "a filing" put proxy-voting records above real news and let three of
        them consume a ticker's entire per-ticker allowance."""
        for title in ["N-PX — Annual Report of proxy voting record",
                      "144 — Report of proposed sale of securities",
                      "4 — Statement of changes in beneficial ownership of securities"]:
            sc, _ = w.score_impact({"t": title, "kind": "filing"})
            self.assertEqual(w.impact_tier(sc), "low", title)
        material, _ = w.score_impact({"t": "8-K — Current report", "kind": "filing"})
        routine, _ = w.score_impact({"t": "4 — Statement of changes", "kind": "filing"})
        self.assertGreater(material, routine)

    def test_routine_filings_do_not_crowd_out_news(self):
        """Three Form 4s used to take three of a ticker's five slots purely for
        being filings, pushing real headlines out of the digest entirely."""
        def mixed(entry, hours):
            return ([item("4 — Statement of changes in beneficial ownership",
                          kind="filing", url="f%d" % i) for i in range(3)]
                    + [item("Company awarded a $500M supply contract"),
                       item("FTC opens an antitrust investigation"),
                       item("raises full-year guidance")])
        self.run_fetch(mixed)
        kept = [h["t"] for h in self.digest_tickers()[0]["headlines"]]
        self.assertNotIn("4 — Statement of changes in beneficial ownership", kept[:3],
                         "routine filings displaced real news: %r" % kept)

    def test_unknown_provider_name_is_rejected(self):
        with self.assertRaises(SystemExit):
            w.main(["--tickers", "NVDA", "--providers", "nope", "--no-topics",
                    "--output", self.digest])


if __name__ == "__main__":
    unittest.main(verbosity=2)

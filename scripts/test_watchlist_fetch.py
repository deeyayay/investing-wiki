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
                       "--output", self.digest])

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
                     "--output", self.digest])
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

    def test_unknown_provider_name_is_rejected(self):
        with self.assertRaises(SystemExit):
            w.main(["--tickers", "NVDA", "--providers", "nope", "--output", self.digest])


if __name__ == "__main__":
    unittest.main(verbosity=2)

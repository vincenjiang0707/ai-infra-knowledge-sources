# [Issue #4227] Nightly build/test failure - 2026-09-18

source: https://github.com/kvcache-ai/Mooncake/issues/4227
state: open | updated: 2026-09-19T12:16:00Z
labels: nightly-failure

## 正文

## Nightly Failure Report

**Run**: https://github.com/kvcache-ai/Mooncake/actions/runs/35245246893
**Branch**: refs/heads/main
**Timestamp**: 2026-09-18T16:11:37.550Z

Please investigate the failed jobs in the workflow run linked above.

## 评论 (1)

### he-yufeng · 2026-09-19

Triage of the three red lanes, all on `3e626f20` (which contains `c57745c3`, the #4150 link fix):

- **nightly-test** fails at `Run CTest unit tests`: `FilereadWorkerPoolTest.AcceptsTypedTrailingWhitespaceAndCaches` again. That is #4213, and the fix is #4210 (still open). Expected until that lands.
- **nightly-coverage** fails at `Run Go store binding sanitizer integration tests`, but not at linking: no `undefined reference` anywhere in the log. The Go binary links and starts, then the master dies with `Failed to start HTTP metadata server on 0.0.0.0:8080` ("master exited before becoming ready"). That is a port-bind/startup flake, a different root cause from the link issue. So the #4150 fix holds — the link step is past it now, which also closes the loop on #4202.
- **build-wheels (cuda13, 3.11)** shows no failing step of its own; it reads as a cascade of the two above through `nightly-gate`.

The new signal worth tracking is the 8080 bind failure. If it recurs on the next nightly, the Go sanitizer job probably needs a unique port per run (or a retry when the port is taken); happy to look if it shows up again.

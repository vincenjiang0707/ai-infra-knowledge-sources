# [Issue #4080] [CI] HighPerformanceTcpLaneDistributionTest.InterleavedPeersUseEveryConfiguredLane/1 is flaky on main

source: https://github.com/kvcache-ai/Mooncake/issues/4080
state: open | updated: 2026-09-14T04:04:51Z
labels: 

## 正文

`HighPerformanceTcpLaneDistributionTest.InterleavedPeersUseEveryConfiguredLane/1` (`GetParam() = true`, sliced read) fails intermittently in `tent-ci (cuda-off)` on main.

Recent main `Build & Test (Linux)` runs show the same test alternating pass/fail with no related change in between:

- 2026-09-13T07 run 34746572253: FAILED (`1 FAILED TEST`, CTest `WriteAndSlicedRead/HighPerformanceTcpLaneDistributionTest.InterleavedPeersUseEveryConfiguredLane/1, where GetParam() = true (9 ms)`)
- the runs immediately before and after it on main: pass

The test (mooncake-transfer-engine/tent/tests/hp_tcp_transport_test.cpp:812) sets up two loopback peers on `127.0.0.1`/`127.0.0.2` with `connections_per_peer = 4` and asserts every configured lane gets used for a 4 MiB sliced read. On a shared CI runner, that assertion is timing- and scheduling-sensitive: whether all four connections per peer actually get exercised before completion depends on transfer interleaving the test does not control.

Not a code regression I can see — main's lane code didn't change between the passing and failing runs. Likely candidates: make the assertion tolerate under-utilized lanes on contended runners, bound the check to "at least N of M lanes", or serialize the sliced-read case so utilization is deterministic. Filing so the flake has a home instead of a nightly-style failure everyone re-runs past.


## 评论 (1)

### github-actions[bot] · 2026-09-13

Thanks for opening this issue, @he-yufeng!

| Field | Value |
|-------|-------|
| **Issue** | #4080 |
| **GitHub user ID** | `40085740` |
| **Reporter** | @he-yufeng |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

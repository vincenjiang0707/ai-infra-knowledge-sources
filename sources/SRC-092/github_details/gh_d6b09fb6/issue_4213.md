# [Issue #4213] [CI] FilereadWorkerPoolTest.AcceptsTypedTrailingWhitespaceAndCaches is flaky on the 1s teardown window

source: https://github.com/kvcache-ai/Mooncake/issues/4213
state: open | updated: 2026-09-23T05:52:12Z
labels: 

## 正文

`FilereadWorkerPoolTest.AcceptsTypedTrailingWhitespaceAndCaches` (`mooncake-store/tests/fileread_worker_pool_test.cpp`) fails intermittently in the `CTest unit tests` job on threads-teardown timing.

Data points (two consecutive failures on the same PR, different heads, with nothing related changed in between):

- PR #3806 run [35269949955](https://github.com/kvcache-ai/Mooncake/actions/runs/35269949955) (job 104379602787): `[  FAILED  ] FilereadWorkerPoolTest.AcceptsTypedTrailingWhitespaceAndCaches (1000 ms)` — `fileread_worker_pool_test.cpp:76`, `WaitForProcessThreadCount(baseline)` returned false.
- Same PR, next head, run [35272724353](https://github.com/kvcache-ai/Mooncake/actions/runs/35272724353) (job 105376045858): identical failure at the same line.
- Main's `Build & Test (Linux)` from the same day passes the test (run 35241301803), so this is load-sensitive, not deterministic.

Mechanism: `WaitForProcessThreadCount` polls for exactly **1 second** (1 ms sleep loop) for the destroyed pool's two worker threads to exit. The failing run's total test time is exactly 1000 ms, i.e. the deadline expired before teardown completed on a loaded runner. The test was restructured recently by #4166, so the 1 s margin is new-ish and unproven under CI load.

This is the same timing-margin flake family as #4136, with an even tighter window. Suggest either widening the wait to a generous bound (e.g. 10 s; the test only cares that teardown *eventually* returns to baseline) or making the pool teardown deterministic (join before the assertion instead of racing a fixed window).


## 评论 (4)

### github-actions[bot] · 2026-09-18

Thanks for opening this issue, @he-yufeng!

| Field | Value |
|-------|-------|
| **Issue** | #4213 |
| **GitHub user ID** | `40085740` |
| **Reporter** | @he-yufeng |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### ykwd · 2026-09-18

Thanks for reporting this. It is addressed in this pr: https://github.com/kvcache-ai/Mooncake/pull/4210

### ToLiveAndLove · 2026-09-20

Another data point on an unrelated PR (#4221, TENT-only change): the same case failed in run [35496873470](https://github.com/kvcache-ai/Mooncake/actions/runs/35496873470/job/106041379037) with `ProcessThreadCount()` = 6 vs expected `baseline + 2` = 4 at `fileread_worker_pool_test.cpp:74`, then the teardown wait at line 76 timed out. It reproduced identically across three heads of that PR while all `tent-ci`/build/format checks stayed green, consistent with the etcd/glog background-thread root cause already noted in #4210 and #4226.

### quantz8a · 2026-09-23

Closing as fixed by #4210 on `main` (same flake class: assert pool worker count instead of process-wide `/proc` thread count). Our follow-up #4226 is closed as redundant.

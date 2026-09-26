# [Issue #4136] [CI] MasterServiceSSDSnapshotTest.EvictObject is flaky around a 4s margin

source: https://github.com/kvcache-ai/Mooncake/issues/4136
state: open | updated: 2026-09-21T02:11:43Z
labels: 

## 正文

`MasterServiceSSDSnapshotTest.EvictObject` (`mooncake-store/tests/master_service_ssd_test_for_snapshot.cpp`) fails intermittently in the `CTest unit tests` job, passing and failing with no related change in between.

Data points so far:

- 2026-09-15T02:14, PR run [34918209366](https://github.com/kvcache-ai/Mooncake/actions/runs/34918209366) (job 104220406540): `[  FAILED  ] MasterServiceSSDSnapshotTest.EvictObject (4012 ms)` — the only failure out of 200 tests.
- A main `Build & Test (Linux)` run earlier this week failed the same test at ~4011 ms (observed while triaging another PR's red).
- The same binary passes locally on a quiet machine, consistently, at ~4027 ms per run.

The signature is a test that lives right at a ~4 s margin: every observed failure sits at 4011-4012 ms, every pass just under or over the same line depending on runner load. On a shared CI runner, whatever the test waits on (eviction completing under concurrent load) crosses the boundary; on a quiet box it does not. Not a code regression — the SSD snapshot code did not change between the passing and failing runs.

Likely candidates: raise the test's own timeout/margin so runner jitter stops deciding the outcome, poll for the evicted state instead of sleeping a fixed interval, or mark it with the retry label the suite already uses for timing-sensitive cases. Filing so the flake has a home instead of a failure everyone re-runs past.


## 评论 (3)

### github-actions[bot] · 2026-09-15

Thanks for opening this issue, @he-yufeng!

| Field | Value |
|-------|-------|
| **Issue** | #4136 |
| **GitHub user ID** | `40085740` |
| **Reporter** | @he-yufeng |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### he-yufeng · 2026-09-15

One more data point, same 4s-margin signature in the sibling scenario binary: `MasterServiceEvictScenarioTest.OpLogDurabilityGatesTenantQuotaReclamation` failed at 4001 ms on a PR merged snapshot (run 35027196459, job 104576973209) with `PutStart(after-durable) failed: TENANT_QUOTA_EXCEEDED`, then passed on rerun with no code change. Same day, `EvictObject` itself flaked at 4011 ms (run 34980652857) and 4012 ms (run 34979380422) on two unrelated branches. Three hits in one day across both binaries suggests the wait margin itself is the common factor, not any one scenario.


### Icedcoco · 2026-09-21

Thanks for reporting this and for the detailed failure data.

The MasterServiceSSDSnapshotTest.EvictObject flake has been addressed by #4156 . The fix prevents the restored MasterService eviction worker from modifying metadata before snapshot comparison.

Please keep an eye on CI runs and let us know if this test, or any related eviction scenario, still fails. If it does, please share the new failure logs so we can investigate separately.

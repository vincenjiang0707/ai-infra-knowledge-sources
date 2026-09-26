# [Issue #5315] [good-first-issue] tests: synchronize health-monitor fallback and recovery

source: https://github.com/LMCache/LMCache/issues/5315
state: open | updated: 2026-09-24T05:22:31Z
labels: good first issue, help wanted, Testing, onboarding-2026

## 正文

Parent tracker: #5313 · Onboarding: #3372

## Problem

`tests/v1/test_health_monitor_fallback_recovery.py::TestRemoteBackendHealthCheckFallbackRecovery::test_full_cycle_with_monitor_thread` uses three 0.2-second sleeps to move through healthy, fallback, and recovery states. The assertions can run before the background monitor applies a transition.

This is a focused CPU-only task using the existing controllable connector and mocks. No live backend or GPU is required.

## Verified CI evidence

PR #5157, September 17: [Python 3.11 failed](https://github.com/LMCache/LMCache/actions/runs/35200658425/job/105135526521) with:

```text
assert mock_local_cpu_backend.use_hot is True
AssertionError: assert False is True
```

The captured log shows the ping failure at `09:09:33.733`, but `Enabled hot_cache for LocalCPUBackend` and `Applied LOCAL_CPU fallback` only at `09:09:33.999`, after the test had already entered cleanup. The action eventually happened; the assertion ran too early.

[Python 3.12 in the same workflow passed this test](https://github.com/LMCache/LMCache/actions/runs/35200658425/job/105135526498). Both checkout logs report tested merge commit `51742dad874ccb60c3009b63b7deb43ea90870a8` (PR head `f0ccdbe26098d65436195eab5f389ca582638b0e`). This is a same-source matrix comparison, **not** a claimed same-Python rerun. The PR changes device-transfer code, not this health-monitor test.

## Starting points and scope

- [The failing full-cycle test](https://github.com/LMCache/LMCache/blob/21571dae80c64ab4d141be571744494995270160/tests/v1/test_health_monitor_fallback_recovery.py#L254).
- [Existing controllable connector and event-loop fixture](https://github.com/LMCache/LMCache/blob/21571dae80c64ab4d141be571744494995270160/tests/v1/test_health_monitor_fallback_recovery.py#L1).
- [HealthMonitor fallback/recovery implementation](https://github.com/LMCache/LMCache/blob/21571dae80c64ab4d141be571744494995270160/lmcache/v1/health_monitor/base.py).

Use observable completion conditions or events with finite deadlines for each phase. Wait for fallback/recovery effects before changing the connector into the next phase. Keep the actual background monitor running in this test.

`monitor.is_healthy()` alone is insufficient: it intentionally stays true while local-CPU fallback is active. Preserve checks for hot-cache and backend-bypass transitions; include the phase and last observed state in timeout failures. Always stop/join the monitor during cleanup.

## Run and validate

Use the shared Linux CPU setup in the parent tracker; run from the repository root:

```bash
python -m pytest -q tests/v1/test_health_monitor_fallback_recovery.py
for i in $(seq 1 50); do
  python -m pytest -q tests/v1/test_health_monitor_fallback_recovery.py::TestRemoteBackendHealthCheckFallbackRecovery::test_full_cycle_with_monitor_thread || exit 1
done
```

- [ ] Observe healthy → local-CPU fallback → recovery in order through the running monitor.
- [ ] A controlled delayed ping/transition exercises the old race and the new wait handles it.
- [ ] A transition that never occurs fails within a finite deadline.
- [ ] Retain behavior checks and leave no monitor thread running after teardown.
- [ ] Run the file and 50 focused repetitions, preferably on Python 3.11 and 3.12; report versions/results.
- [ ] No blanket retry or larger fixed sleep as the fix.

## How to claim

Comment `/claim` or “I'd like to work on this” below before starting so a maintainer can coordinate assignment. Follow #3372, target `dev`, sign off every commit, and run `pre-commit run --all-files` before sending the PR.


## 评论 (2)

### akshat-lakhera · 2026-09-23

/claim

I'd like to work on this! I'll replace the fixed `0.2` second sleeps in `test_full_cycle_with_monitor_thread` with event-based waits/polling with finite deadlines to ensure the background monitor transitions properly before assertions are run. I'll make sure to test it with 50 repetitions locally to prove the race condition is fixed without using blanket retries.


### maobaolong · 2026-09-23

@akshat-lakhera Thank you!

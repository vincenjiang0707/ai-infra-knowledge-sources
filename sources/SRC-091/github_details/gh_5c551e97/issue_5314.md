# [Issue #5314] [good-first-issue] tests: wait for health-monitor exit instead of sleeping

source: https://github.com/LMCache/LMCache/issues/5314
state: open | updated: 2026-09-24T05:37:38Z
labels: good first issue, help wanted, Testing, onboarding-2026

## 正文

Parent tracker: #5313 · Onboarding: #3372

## Problem

`tests/v1/test_health_monitor.py::TestIrrecoverableException::test_run_loop_stops_on_irrecoverable_exception` sleeps for 0.2 seconds after starting a worker, then asserts it has exited. A fixed sleep does not establish that the exception path and its logging have finished.

This is a focused CPU-only test synchronization task. Python threading basics are sufficient; no GPU is needed.

## Verified CI evidence

- PR #4769, September 22: [Python 3.10 attempt 1 failed](https://github.com/LMCache/LMCache/actions/runs/35748069108/job/106815522162) at `assert not thread.is_alive()`; [attempt 2 passed](https://github.com/LMCache/LMCache/actions/runs/35748069108/job/106876629094).
- Both checkout logs report **the same tested merge commit** `59028c36bdea5b0d4f484c26d94c8f662c2c3f53` (PR head `e0b4b9fcc2c98eed9d8cfdfe2a6980e3ba4b8d38`). The second workflow overall was cancelled because another matrix job was cancelled; the cited Python 3.10 job succeeded.
- PR #5271 independently hit the same assertion: [Python 3.11 attempt 1 failed](https://github.com/LMCache/LMCache/actions/runs/35552348541/job/106189327379), then [attempt 2 passed](https://github.com/LMCache/LMCache/actions/runs/35552348541/job/106192617425), both at tested merge commit `cf6b1c8450e79d8dbac54ea9bb6776df64ba8342`.

The #5271 failure log records the exception at `02:06:53.292` and the worker stopping at `02:06:53.541`, about 249 ms later. The test's 200 ms assumption is shorter than the observed shutdown path. This does not imply production must guarantee a 200 ms shutdown.

## Starting points and scope

- [The test and neighboring irrecoverable-exception cases](https://github.com/LMCache/LMCache/blob/21571dae80c64ab4d141be571744494995270160/tests/v1/test_health_monitor.py#L280).
- [PeriodicThread implementation](https://github.com/LMCache/LMCache/blob/21571dae80c64ab4d141be571744494995270160/lmcache/v1/periodic_thread.py).

Replace the fixed sleep with a bounded wait for thread completion, for example joining the returned thread with a deadline. Retain the exit/unhealthy assertions and ensure cleanup runs on failure. Review adjacent tests only where they repeat the same exit assumption.

Do **not** call `monitor.stop()` before verifying that the irrecoverable exception stopped the worker: that would mask broken exception-driven termination. Keep production behavior unchanged unless investigation demonstrates a separate defect.

## Run and validate

Use the shared Linux CPU setup in the parent tracker; run from the repository root:

```bash
python -m pytest -q tests/v1/test_health_monitor.py
for i in $(seq 1 50); do
  python -m pytest -q tests/v1/test_health_monitor.py::TestIrrecoverableException::test_run_loop_stops_on_irrecoverable_exception || exit 1
done
```

- [ ] Add a controlled slow/scheduled exception path that exposes the old timing assumption without relying on runner luck.
- [ ] Verify exit is caused by the exception and retain health-state checks.
- [ ] A worker that never exits must fail within a finite deadline with useful diagnostics.
- [ ] Run the file and 50 focused repetitions; exercise Python 3.10 and 3.11 when available and report actual versions/results.
- [ ] No blanket retry, assertion removal, or longer fixed sleep as the fix.

## How to claim

Comment `/claim` or “I'd like to work on this” below before starting so a maintainer can coordinate assignment. Follow #3372, target `dev`, sign off every commit, and run `pre-commit run --all-files` before sending the PR.


## 评论 (4)

### harbinresearcher · 2026-09-23

/claim

### maobaolong · 2026-09-24

@harbinresearcher Thanks for claim this, you can submit a PR.

### maobaolong · 2026-09-24

@harbinresearcher Would you like to submit a PR recently?

### Zhou-Kan · 2026-09-24

Can I work on this one ? @maobaolong 

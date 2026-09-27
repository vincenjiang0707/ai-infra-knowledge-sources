# [Issue #5316] [good-first-issue] tests: bound and diagnose RESP connector waits

source: https://github.com/LMCache/LMCache/issues/5316
state: open | updated: 2026-09-23T03:41:58Z
labels: good first issue, help wanted, Testing, onboarding-2026

## 正文

Parent tracker: #5313 · Onboarding: #3372

## Problem and bounded newcomer scope

RESP connector tests submit coroutines to an event-loop thread and call `future.result()` without timeouts. If an operation stops making progress, the test can wait until GitHub cancels the entire job.

Add bounded waits and useful failure diagnostics **inside the RESP tests**, plus a deterministic stalled-operation regression test. This is a CPU-only task for someone comfortable with Python futures. It does not require redesigning the production executor.

## Verified CI evidence and its limit

PR #4948, September 16, run `35072883302`:

- [Python 3.13 attempt 1](https://github.com/LMCache/LMCache/actions/runs/35072883302/job/104718427337) last reported `test_remote_storage_plugin_no_matching_url_raises_error PASSED [82%]` at `08:29:58`; the next output is cancellation at `14:17:23`, about 5 hours 47 minutes without test progress.
- [Python 3.13 attempt 2](https://github.com/LMCache/LMCache/actions/runs/35072883302/job/104841298240) passes `test_resp_connector_basic_operations` immediately after that preceding test and completes successfully (`5867 passed`).
- Both checkout logs report the same tested merge commit `7a44663e28ae51da86076fd5ef0068247e7e8c88` (PR head `d0d44956f14d5a5b9e6cdfc1de4bb3c0762a651e`). Both used vLLM 0.29.0 and torch 2.13.0.

The hang is intermittent. **Its exact stack is unknown:** attempt 1 has no traceback or stack dump proving a particular RESP operation was responsible. The RESP boundary is a lead based on test order, not a proven root cause or a Python 3.13 compatibility verdict.

## Starting points

- [RESP tests and unbounded waits](https://github.com/LMCache/LMCache/blob/21571dae80c64ab4d141be571744494995270160/tests/v1/storage_backend/test_resp_connector.py#L105).
- [Event-loop test helpers](https://github.com/LMCache/LMCache/blob/21571dae80c64ab4d141be571744494995270160/tests/v1/utils.py#L180).
- [RESP implementation](https://github.com/LMCache/LMCache/blob/21571dae80c64ab4d141be571744494995270160/lmcache/v1/storage_backend/connector/redis_connector.py).
- #4489 already tracks executor shutdown defects. Coordinate there if diagnostics implicate that path; do not duplicate its implementation task.

## Suggested implementation

Introduce a small test-local waiting helper with a reasonable deadline and an operation label such as `exists`, `put`, or `get`. Use it consistently for synchronous waits in this file. On timeout, report the operation and loop/thread liveness; cancel the submitted future as appropriate and preserve cleanup. Diagnostics must not themselves wait forever on the possibly stuck loop.

Use a deliberately non-completing mock operation to prove prompt failure. Retain successful operations and exception propagation. Avoid globally rewriting shared fixtures or suppressing lifecycle warnings in this small task; coordinate any necessary shared lifecycle fix separately.

## Run and validate

Use the shared Linux CPU setup in the parent tracker. The fixture uses `MockRESPClient`; no Redis server is needed. Run from the repository root:

```bash
python -m pytest -q tests/v1/storage_backend/test_resp_connector.py -o faulthandler_timeout=60
for i in $(seq 1 20); do
  python -m pytest -q tests/v1/storage_backend/test_resp_connector.py::test_resp_connector_basic_operations -o faulthandler_timeout=60 || exit 1
done
```

`faulthandler_timeout` prints a stack dump; it is **not** the bounded failure mechanism the task must add. Exercise Python 3.13 and at least one other supported version when available. For the historical environment, install vLLM 0.29.0 in a fresh venv instead of 0.30.0.

- [ ] No unbounded synchronous future waits remain in this RESP test file.
- [ ] A deliberately stalled operation produces a bounded, actionable failure; diagnostics/cleanup do not leave the process stuck.
- [ ] Successful operations and data-integrity assertions pass; genuine operation errors remain visible.
- [ ] Run the full file and 20 basic-operation repetitions; report versions/results.
- [ ] Describe the result as test hardening/diagnostics. Do not claim the historical production hang is fixed without reproduction and evidence.

## How to claim

Comment `/claim` or “I'd like to work on this” below before starting so a maintainer can coordinate assignment. Follow #3372, target `dev`, sign off every commit, and run `pre-commit run --all-files` before sending the PR.


## 评论 (2)

### Alanxtl · 2026-09-23

/claim

### maobaolong · 2026-09-23

@Alanxtl Thank you!

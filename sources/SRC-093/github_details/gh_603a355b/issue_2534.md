# [Issue #2534] Add progressDeadlineSeconds support to StormService rollout progress

source: https://github.com/vllm-project/aibrix/issues/2534
state: closed | updated: 2026-09-01T09:02:01Z
labels: help wanted, area/disaggregated

## 正文

## 🚀 Feature Description and Motivation

StormService rollouts for LLM inference workloads can get stuck for common serving-system reasons, including long model weight downloads, image pull or startup delays, engine bootstrap failures, CUDA graph compilation stalls, P/D role coordination issues, or one role becoming ready while another remains blocked.

RayClusterFleet already exposes `spec.progressDeadlineSeconds` to detect rollout progress stalls. StormService has a `Progressing` condition, but it currently acts as a generic “not ready yet” signal. There is no API-level deadline for deciding that rollout progress has stalled.

As a result, a StormService can remain progressing indefinitely without a clear timeout condition for users or automation.

## Use Case

In production model serving, rollout stalls often require operator action, such as checking model artifacts, image availability, runtime logs, or role coordination.

This feature would give users and automation a clear signal when a StormService rollout is stuck instead of leaving it indefinitely Progressing.

## Proposed Solution

Add `spec.progressDeadlineSeconds` to `StormServiceSpec`.

Suggested semantics:

- Default: `600`
- If unset, preserve default rollout timeout behavior.
- If rollout progress does not happen within this deadline, update the StormService `Progressing` condition to indicate failure, for example:
  - `type: Progressing`
  - `status: False`
  - `reason: ProgressDeadlineExceeded`
- The controller should continue reconciling after timeout.
- Paused StormServices should not be considered timed out while paused.

Expected work:

- Add `progressDeadlineSeconds` to `StormServiceSpec`.
- Regenerate CRDs / deepcopy / client code as needed.
- Update StormService progress condition logic.
- Add unit tests.
- Add integration test cases under `test/integration/controller/stormservice_test.go`.

Required integration test cases:

- Default deadline is applied when `progressDeadlineSeconds` is unset.
- Rollout progress refreshes the progress timestamp / condition.
- A stuck rollout transitions `Progressing` to failed after the deadline.
- Paused StormService does not time out while paused.
- After progress resumes, the timeout condition should recover according to the chosen condition semantics.

## 评论 (1)

### googs1025 · 2026-08-09

We can determine whether need this first, and then work on this feature later.  cc @Jeffwan 

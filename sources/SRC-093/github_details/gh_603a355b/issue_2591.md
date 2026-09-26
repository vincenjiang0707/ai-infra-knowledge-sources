# [Issue #2591] KPA/APA should not scale down on unknown metrics and should reject invalid subTargetSelector targets

source: https://github.com/vllm-project/aibrix/issues/2591
state: closed | updated: 2026-08-23T00:34:38Z
labels: help wanted

## 正文

### Bug description

While smoke-testing PodAutoscaler KPA / APA strategies on minikube, I found two related validation / error-handling issues:

1. Unknown metric names are accepted and then treated as metric value `0`, causing KPA / APA to scale down.
2. `subTargetSelector.roleName` is accepted for a Deployment target under KPA, even though role-level sub-targeting appears to be intended only for StormService.

### What worked

Using a fake vLLM-style Prometheus endpoint and the current central metric registry key `num_requests_running`, both KPA and APA worked:

- KPA + POD metric scaled a Deployment from `2` to `4`.
- APA + POD metric scaled a Deployment up to the configured `maxReplicas: 6`.
- KPA / APA did not create HPA resources; they directly patched the target workload's `spec.replicas`.

### Issues found

#### 1. Unknown metric name is treated as zero and causes scale-down

Example PodAutoscaler:

```yaml
spec:
  scalingStrategy: APA
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: custom-pa-target
  minReplicas: 1
  maxReplicas: 6
  metricsSources:
  - metricSourceType: pod
    protocolType: http
    port: "8000"
    path: /metrics
    targetMetric: running_requests
    targetValue: "1"
```

Observed controller log:

```text
Failed to fetch metric running_requests from pod ...: metric running_requests not found in central registry. Returning zero value.
```

Observed behavior:

- The PodAutoscaler is accepted by admission.
- The controller records metric values as `[0, 0, ...]`.
- KPA / APA computes a scale-down recommendation.
- The workload scales down to `minReplicas=1`.
- PodAutoscaler still reports `ValidSpec=True` and `Ready=True`.

This is dangerous because a typo, stale example, or registry mismatch can silently scale down a live workload. Metric collection/config errors should not be converted into a healthy metric value of `0`.

Expected behavior:

- Unknown `targetMetric` should be rejected during admission if the set of supported central registry metrics is known to the controller/webhook.
- If the metric cannot be validated at admission time, metric fetch failures should make scaling invalid for that reconciliation.
- PodAutoscaler should report something like `FailedComputeScale` / `AbleToScale=False`, and should not apply a scale-down based on synthetic zero values.

#### 2. Existing test/example metric key may not match the current registry

I noticed existing integration coverage uses `running_requests`, while the current central registry key is `num_requests_running`.

With `targetMetric: running_requests`:

- KPA / APA accepts the PodAutoscaler.
- Controller logs `metric running_requests not found in central registry`.
- The metric is treated as `0`.

With `targetMetric: num_requests_running`:

- KPA / APA successfully fetch metrics from a vLLM-style endpoint.
- Scaling behaves as expected.

This suggests test fixtures/examples should be updated to use current metric keys, and regression tests should cover the unknown-metric behavior.

#### 3. KPA accepts `subTargetSelector.roleName` for a Deployment target

Example:

```yaml
spec:
  scalingStrategy: KPA
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: custom-pa-target
  subTargetSelector:
    roleName: prefill
  minReplicas: 1
  maxReplicas: 6
  metricsSources:
  - metricSourceType: pod
    protocolType: http
    port: "8000"
    path: /metrics
    targetMetric: num_requests_running
    targetValue: "1"
```

Observed behavior:

- Server-side dry-run accepts it.
- Live creation accepts it.
- PodAutoscaler status reports `ValidSpec=True` and `Ready=True`.
- No clear invalid-spec signal is surfaced.

Based on the controller code and behavior, `subTargetSelector.roleName` appears intended for StormService role-level autoscaling, not generic Deployment scaling. This should be rejected by admission and/or controller fallback validation unless Deployment sub-targeting is intentionally supported.

### Expected validation / test coverage

Please consider adding:

- Webhook / controller validation for unknown or unsupported `targetMetric` names when possible.
- Regression tests ensuring metric fetch/config errors do not produce synthetic `0` values that trigger scale-down.
- Test fixture/example cleanup from `running_requests` to `num_requests_running`, or a compatibility alias if `running_requests` is still intended to be supported.
- Admission/controller tests rejecting `subTargetSelector.roleName` when `scaleTargetRef.kind` is not `StormService`.

### Environment

- AIBrix version: upstream `main`, commit `136197c8db5ab353052234749a53d0534b3590de`
- Deployment environment: minikube
- Controller image: `aibrix/controller-manager:nightly`
- CRDs and controller deployed from `config/crd` and `config/default`


## 评论 (1)

### wieghx · 2026-08-20

I'll work on this: reject unknown targetMetric / invalid subTargetSelector at admission, and stop treating missing metrics as 0 for KPA/APA scale-down.

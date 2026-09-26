# [Issue #2590] PodAutoscaler HPA strategy accepts invalid replica bounds and inconsistent targetValue formats

source: https://github.com/vllm-project/aibrix/issues/2590
state: closed | updated: 2026-08-24T14:58:14Z
labels: help wanted

## 正文

### Bug description

While smoke-testing the upstream `main` PodAutoscaler controller and CRDs on minikube, I found several HPA strategy validation gaps where invalid PodAutoscaler specs are accepted and later produce misleading status or unsafe HPA specs.

The normal HPA strategy flow works:

- HPA strategy creates an HPA successfully: PodAutoscaler -> HPA.
- Updating `minReplicas` / `maxReplicas` on the PodAutoscaler syncs to the HPA successfully. I verified `2/6`.
- Deleting the PodAutoscaler deletes the HPA through ownerReference / garbage collection.
- When two PodAutoscalers point to the same Deployment, the second one is marked `MultiPodAutoscalerConflict=False` and does not create a second HPA.
- After deleting the first PodAutoscaler, the second one can take over and create its own HPA.
- The existing PodAutoscaler integration subsets pass:
  - `./test/integration/webhook`
  - `./test/integration/controller`

However, the following invalid specs are still accepted or produce unsafe behavior.

### Issues found

1. `resource` metric `targetValue: 100m` is accepted by the webhook, but the controller fails to parse it.

Controller log:

```text
strconv.ParseFloat: parsing "100m": invalid syntax
```

Observed behavior:

- The PodAutoscaler is accepted.
- HPA is not created.
- PodAutoscaler status still reports `Ready=True` and `ValidSpec=True`.

This suggests the webhook and controller disagree on the accepted `targetValue` format. The webhook accepts Kubernetes quantity-style values such as `100m`, while the HPA generation path expects a plain float/percentage-like value.

2. `minReplicas: -1` is accepted by admission.

Observed behavior:

- The PodAutoscaler is accepted.
- The PodAutoscaler can still report `Ready=True`.
- An HPA is generated with `minReplicas: 1`.

This should be rejected by CRD schema and/or validating webhook.

3. `maxReplicas: 0` is accepted by admission and produces a dangerous HPA spec.

Observed generated HPA:

```yaml
spec:
  minReplicas: 1
  maxReplicas: 2147483647
```

This is high risk because an invalid PodAutoscaler with `maxReplicas: 0` becomes an HPA with a very large upper bound.

### Correctly rejected cases

The following negative cases were correctly rejected during server-side dry-run:

- `minReplicas > maxReplicas`
- empty `scaleTargetRef.name`
- HPA strategy with `subTargetSelector.roleName`
- empty `metricsSources`
- invalid `scalingStrategy`

### Expected behavior

- Reject negative `minReplicas`.
- Reject non-positive `maxReplicas`.
- Align webhook/controller semantics for `metricsSources[*].targetValue`.
- If `targetValue: 100m` is supported, HPA generation should handle it consistently.
- If only plain numeric values are supported for HPA/resource metrics, admission should reject quantity-style values.
- PodAutoscaler should not report `Ready=True` / `ValidSpec=True` when the controller cannot generate the HPA from the accepted spec.

### Environment

- AIBrix version: upstream `main`, commit `136197c8db5ab353052234749a53d0534b3590de`
- Deployment environment: minikube
- Controller image: `aibrix/controller-manager:nightly`
- CRDs and controller deployed from `config/crd` and `config/default`


## 评论 (1)

### lettycat · 2026-08-20

I'd like to work on this. 👍

  I verified on the latest `main` that PR #2529 (merged after this issue was filed) has already fixed part of this: the webhook now
  validates `targetValue` with `strconv.ParseFloat` (so quantity-style values like `100m` are rejected), and rejects negative
  `minReplicas` / non-positive `maxReplicas`.

  The remaining gap is on the controller side: `validateMetricsSources` only checks `TargetValue != ""`, so when the validating webhook
  is bypassed (e.g., `failurePolicy=ignore` with the webhook unavailable), an unparseable `targetValue` reaches `makeHPAWithBounds`,
  which fails — but the PodAutoscaler status still reports `ValidSpec=True` / `Ready=True` and no HPA is ever created.

  I plan to submit a PR that:
  - adds `targetValue` parse/positivity validation to the controller's `validateSpec` (mirroring the webhook semantics),
  - updates the status (`ValidSpec=False` / `Ready=False`) when HPA generation fails, so the status never reports Ready for an HPA that
  cannot be generated,
  - adds unit tests covering the webhook-bypassed path.

  /cc @googs1025


# [Issue #5310] [Bug][Prometheus] `rayClusterConditionProvisioned` is missing from `Describe()`

source: https://github.com/ray-project/kuberay/issues/5310
state: closed | updated: 2026-09-22T21:48:35Z
labels: bug, good-first-issue

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### KubeRay Component

ray-operator

### Description

`RayClusterMetricsManager` emits `rayClusterConditionProvisioned` in `Collect()`, but its Desc is not included in `Describe()`:

https://github.com/ray-project/kuberay/blob/f72fa09812e0412305ee536bc2d28a6a3fe6037d/ray-operator/controllers/ray/metrics/ray_cluster_metrics.go#L23-L30

https://github.com/ray-project/kuberay/blob/f72fa09812e0412305ee536bc2d28a6a3fe6037d/ray-operator/controllers/ray/metrics/ray_cluster_metrics.go#L66-L71

This is inconsistent with the prometheus.Collector contract, which requires Describe() to return the descriptors of metrics collected by the Collector.

> The descriptor of each sent metric is one of those returned by Describe

https://github.com/prometheus/client_golang/blob/d2f148ba5de4e4e1d072740ced923f869f46f4a1/prometheus/collector.go#L52-L53

We should add `r.rayClusterConditionProvisioned` to `Describe()` so that all metrics emitted by Collect() are properly described

### Use case

_No response_

### Related issues

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (1)

### Efutrrionpy · 2026-09-17

I’d like to work on this.

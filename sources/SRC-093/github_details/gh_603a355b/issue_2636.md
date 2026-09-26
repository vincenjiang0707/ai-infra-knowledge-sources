# [Issue #2636] Document PodAutoscaler support for Kubernetes external metrics adapters

source: https://github.com/vllm-project/aibrix/issues/2636
state: closed | updated: 2026-09-03T08:14:46Z
labels: help wanted, area/autoscaling, kind/feature

## 正文

## Background

AIBrix PodAutoscaler already supports consuming metrics from the Kubernetes `external.metrics.k8s.io` API. This makes it possible to scale workloads using metrics provided by external metrics adapters, such as Prometheus Adapter, a custom adapter, or other adapters that implement the Kubernetes external metrics API.

Currently, this capability is mainly covered by the e2e test:

- `test/e2e/external_metrics_autoscaler_test.go`

There are also basic sample manifests under:

- `samples/autoscaling/external-metrics-apa.yaml`
- `samples/autoscaling/external-metrics-kpa.yaml`

However, users may not know from the documentation that PodAutoscaler can integrate with existing external metrics adapters.

## Proposal

Add user-facing documentation and sample coverage for using PodAutoscaler with Kubernetes external metrics adapters.

The documentation should explain:

- PodAutoscaler can consume metrics from `external.metrics.k8s.io`.
- Users can use Prometheus Adapter, a custom external metrics adapter, or another compatible adapter.
- For this mode, the `metricsSources` entry should use:
  - `metricSourceType: external`
  - `targetMetric: <external metric name>`
  - `targetValue: <threshold>`
- The external metrics adapter must be installed and expose the requested metric through the Kubernetes external metrics API.
- This mode does not require setting `endpoint`, `path`, or `protocolType` in the PodAutoscaler metric source.

## Expected Changes

- Add or update documentation for PodAutoscaler external metrics support.
- Add a clearer sample under `samples/autoscaling/`, for example:
  - a Prometheus Adapter based example, or
  - a generic external metrics adapter example.
- Reference the sample from the autoscaler documentation.
- Clarify that the existing e2e fake adapter is for test validation only, while users can bring their own adapter implementation.

## Example

```yaml
apiVersion: autoscaling.aibrix.ai/v1alpha1
kind: PodAutoscaler
metadata:
  name: external-metrics-example
spec:
  scalingStrategy: APA
  minReplicas: 1
  maxReplicas: 8
  metricsSources:
    - metricSourceType: external
      targetMetric: aibrix_queue_depth
      targetValue: "40"
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: example-workload
```

## Acceptance Criteria

- Users can understand that PodAutoscaler supports Kubernetes external metrics adapters.
- Users can find at least one sample manifest showing how to configure `metricsSources` for external metrics.
- Documentation explains how this integrates with Prometheus Adapter, custom adapters, or other compatible adapters.
- Documentation distinguishes user-facing adapter integration from the e2e-only fake adapter.

## 评论 (1)

### DsThakurRawat · 2026-08-31

this gap is real, checked it against `main`. the plumbing and the samples are both there:

```
test/e2e/external_metrics_autoscaler_test.go
samples/autoscaling/external-metrics-apa.yaml
samples/autoscaling/external-metrics-kpa.yaml
```

but `grep -rl "external.metrics.k8s.io" docs/` comes back empty, and
`docs/source/features/autoscaling/` only has `autoscaling.rst`,
`metric-based-autoscaling.rst` and `optimizer-based-autoscaling.rst`. so someone reading the
docs has no way to discover the capability exists, and the two sample manifests are effectively
unreferenced.

happy to write this up. the shape i would go for, unless you would rather it live somewhere else:

a section in `metric-based-autoscaling.rst` rather than a new page, since external metrics is a
metric source for the same autoscalers rather than a separate autoscaling mode. it would cover
what has to be running on the cluster (an adapter serving `external.metrics.k8s.io`, with
Prometheus Adapter as the worked example), the fields on the PodAutoscaler that select an
external metric, and a pointer to both sample manifests so the APA and KPA variants are
discoverable. the e2e test is the most reliable description of the working configuration, so i
would derive the example from it rather than write one from scratch.

one thing i cannot check from the outside: whether external metrics is considered stable enough
to document as a supported path, or whether it is deliberately undocumented for now. if it is
the latter, say so and i will leave it.


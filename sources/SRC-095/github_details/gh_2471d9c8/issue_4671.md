# [Issue #4671] [operator] BuildAutoscalerContainer does not declare containerPort for autoscaler metrics (44217)

source: https://github.com/ray-project/kuberay/issues/4671
state: open | updated: 2026-09-22T16:59:17Z
labels: stale

## 正文

## Bug

When `enableInTreeAutoscaling: true`, the KubeRay operator injects an autoscaler sidecar into the head pod via `BuildAutoscalerContainer()`. The autoscaler process starts a Prometheus metrics server on port 44217 (`AUTOSCALER_METRIC_PORT`), exposing metrics like `autoscaler_active_nodes`.

However, `BuildAutoscalerContainer()` does not declare any `containerPort` entries on the sidecar container. The official PodMonitor YAML (`config/prometheus/podMonitor.yaml`) scrapes `port: as-metrics` from head pods, which requires a named container port to be discoverable by Prometheus.

Since no container declares `containerPort: 44217` with `name: as-metrics`, Prometheus silently fails to scrape autoscaler metrics.

## Root cause

`BuildAutoscalerContainer()` in `controllers/ray/common/pod.go` creates the sidecar with `Env`, `Command`, `Args`, and `Resources` — but no `Ports` field.

The sample YAML `ray-cluster.embed-grafana.yaml` works around this by manually declaring the port on the head container, but that sample does not use `enableInTreeAutoscaling`. Users who enable autoscaling via the operator flag don't get this port.

## How to reproduce

1. Create a RayCluster with `enableInTreeAutoscaling: true`
2. Deploy the PodMonitor from `config/prometheus/podMonitor.yaml`
3. Check Prometheus targets — the `as-metrics` endpoint is not discovered
4. `autoscaler_active_nodes` metric is missing

## Fix

Add the port declaration to `BuildAutoscalerContainer`:

```go
Ports: []corev1.ContainerPort{
    {
        ContainerPort: 44217,
        Name:          "as-metrics",
    },
},
```

## 评论 (1)

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

# [Issue #4697] [Feature] [observability] Add latency metrics (p95, p99) for Ray HTTP clients

source: https://github.com/ray-project/kuberay/issues/4697
state: open | updated: 2026-09-23T04:42:27Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

Add latency metrics (p95, p99) to `RayDashboardClient` and `RayHttpProxyClient` for improved observability, as proposed by @andrewsykim in this [thread](https://github.com/ray-project/kuberay/pull/4680#pullrequestreview-4091293710).

### Use case

Make it easier to debug timeout issues in both Kubernetes proxy mode and direct (non-proxy) mode.

### Related issues

Add default timeout for Kubernetes proxy mode: https://github.com/ray-project/kuberay/issues/4679.

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (1)

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

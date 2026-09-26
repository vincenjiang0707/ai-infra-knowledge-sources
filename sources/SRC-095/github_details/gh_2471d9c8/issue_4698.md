# [Issue #4698] [Chore] [RayService] Version skew between Kubernetes and Istio

source: https://github.com/ray-project/kuberay/issues/4698
state: open | updated: 2026-09-23T04:42:29Z
labels: stale

## 正文

The current CI setup for incremental upgrades relies on Istio v1.28.3, while Kubernetes 1.29 is listed as "Tested, but not supported (see [here](https://istio.io/latest/docs/releases/supported-releases/#support-status-of-istio-releases))."  Additionally, all Istio versions that support Kubernetes 1.29 have reached end of life.

#### Proposed Fix

Bump up the KinD cluster Kubernetes version within the supported range (v1.30 – v1.34) that is compatible with Istio v1.28.3.

#### Related Issues

https://github.com/ray-project/kuberay/issues/4606

## 评论 (2)

### troy0820 · 2026-04-21

Would v1.35.0 Kubernetes version be to out of support for istio? There is currently a PR I have to bump the ci to use kind v1.35.0 Kubernetes. In the issue linked, I believe we wanted to go to where k8s versions were supported as well. 

https://github.com/ray-project/kuberay/pull/4630

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

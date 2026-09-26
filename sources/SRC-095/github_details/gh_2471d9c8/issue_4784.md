# [Issue #4784] [RayService] Suspend toggle are silently dropped during rollback

source: https://github.com/ray-project/kuberay/issues/4784
state: open | updated: 2026-09-23T04:42:52Z
labels: discussion, stale

## 正文

### Problem Statement

During the incremental upgrade **rollback** phase, any change to `spec.rayClusterSpec.suspend` is not propagated to the active RayCluster. This breaks integrations that drive `suspend` externally (e.g., Kueue admitting / preempting the workload):

- the surviving cluster keeps running when it should be suspended,
- or stays suspended when it should be admitted back.

### Why it happens

`shouldUpdateCluster` short-circuits for the active cluster whenever `UpgradeInProgress` is true.

## 评论 (1)

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

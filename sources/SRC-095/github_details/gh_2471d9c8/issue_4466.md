# [Issue #4466] [Refactor] [history server] Rename cluster session key of events

source: https://github.com/ray-project/kuberay/issues/4466
state: open | updated: 2026-09-22T16:58:18Z
labels: stale

## 正文

For now, we use the cluster session key as the identifier to isolate different sessions within the same Ray cluster. However, the "clusterName" key name of events should be renamed to "clusterSessionKey" [1] for better readability and maintainability.

### Related PR
https://github.com/ray-project/kuberay/pull/4464

### References
[1] https://github.com/Future-Outlier/kuberay/blob/0843e1a50486e12323d09af1a07c012b9fe59422/historyserver/pkg/eventserver/eventserver.go#L153

## 评论 (2)

### Future-Outlier · 2026-01-31

thank you! given that this is not urgent, we can do this in the beta

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

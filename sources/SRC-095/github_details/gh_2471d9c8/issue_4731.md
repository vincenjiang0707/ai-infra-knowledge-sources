# [Issue #4731] Fix gosec G704 SSRF false positives in apiserver/pkg/http/client.go

source: https://github.com/ray-project/kuberay/issues/4731
state: open | updated: 2026-09-23T04:42:39Z
labels: stale

## 正文

#4703 updated golangci-lint to a new version which started URLs constructed in apiserver/pkg/http/client.go

These URls are constructed from internal config and are false positives but we should try and remove the suprssions anyways



## 评论 (1)

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

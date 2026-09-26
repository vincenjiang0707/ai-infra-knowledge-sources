# [Issue #3993] [Refactor] Refactor utils package in ray-operator

source: https://github.com/ray-project/kuberay/issues/3993
state: open | updated: 2026-09-22T16:56:39Z
labels: stale

## 正文

Currently, the utils package contains many unnecessary components that are mixed together, making it messy and overly large. This also causes other packages to become bloated when they depend on utils.

This issue is intended to track the refactoring of the utils package.

#3983
#3991 
#3992 
#4009 
#4010
#3979

## 评论 (1)

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

# [Issue #4627] [Feature] generate SMD schemas for all kuberay types

source: https://github.com/ray-project/kuberay/issues/4627
state: open | updated: 2026-09-22T16:59:00Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

In trying to update deprecated APIs, we found we can't easily replace `NewSimpleClientset` with `NewClientset` because it requires a complete Structured Merge Diff (SMD) schema to exist. See [this comment](https://github.com/ray-project/kuberay/pull/4605#pullrequestreview-3976652285) and the Kubernetes [structured-merge-diff](https://github.com/kubernetes-sigs/structured-merge-diff) repository for more details.

### Use case

We would like to re-enable the SA1019 staticcheck linter rule and remove the `// TODO:` comment about `NewSimpleClientset` in the linter rules, but doing so requires creating an SMD schema for kuberay objects, which would be a pervasive, but beneficial, change.

### Related issues

_No response_

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (1)

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

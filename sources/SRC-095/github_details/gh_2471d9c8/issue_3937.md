# [Issue #3937] [Flaky] "Test Autoscaler E2E Part 1 (nightly operator)" is flaky

source: https://github.com/ray-project/kuberay/issues/3937
state: open | updated: 2026-09-22T16:56:16Z
labels: bug, ci, autoscaler, flaky, 1.5.0, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

ci

### What happened + What you expected to happen

https://buildkite.com/ray-project/ray-ecosystem-ci-kuberay-ci/builds/10311#01989a3c-2f12-410e-9b0d-9b56d0a86c65

### Reproduction script

https://buildkite.com/ray-project/ray-ecosystem-ci-kuberay-ci/builds/10311#01989a3c-2f12-410e-9b0d-9b56d0a86c65

### Anything else

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (3)

### kevin85421 · 2025-08-11

cc @rueian Autoscaler E2E tests are flaky. Please take a look. Thanks!

### rueian · 2025-08-17

Note: this looks like a shutdown issue with grpc in Ray

<img width="1168" height="486" alt="Image" src="https://github.com/user-attachments/assets/1f190c4d-deea-4f30-b4d8-32e093aed3d8" />

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

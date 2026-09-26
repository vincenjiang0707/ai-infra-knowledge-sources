# [Issue #4197] [Feature] Support custom ray-job-submitter container spec for Sidecar mode

source: https://github.com/ray-project/kuberay/issues/4197
state: open | updated: 2026-09-22T16:57:22Z
labels: enhancement, 1.6.0, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

I've been trying out the new Rayjob sidecar submission mode. However, my jobs rely on a script located on a `volumeMount` and it does not appear that there is a straightforward way to patch this into the `ray-job-submitter` container. It would be helpful to have the ability to specify a custom spec for the ray-job-submitter container in the same way that it's possible to do so for the `ray-head` container.

### Use case

_No response_

### Related issues

_No response_

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (2)

### dalaoqi · 2025-11-18

@Future-Outlier  I'd like to help with this.

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

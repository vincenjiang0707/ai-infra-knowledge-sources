# [Issue #4115] [Feature] Add authentication support to the Ray Dashboard

source: https://github.com/ray-project/kuberay/issues/4115
state: open | updated: 2026-09-22T16:57:10Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

Currently the ray dashboard is available outside of the cluster without authentication. 
I would like to propose a configuration type that would enable authentication on the ray dashboard allowing cluster admins secure access to the ray dashboard


### Use case

Using oauth or oidc from the cluster to secure the dashboard would give cluster admins greater control over access to the platform. This could be tied together with already existing issues to provide an easy was for admins to secure their platform, see related issues linked below. 

### Related issues

https://github.com/ray-project/kuberay/issues/3974
https://github.com/ray-project/kuberay/issues/3987

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (1)

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

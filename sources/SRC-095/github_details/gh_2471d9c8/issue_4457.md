# [Issue #4457] [Feature] [Dashboard] Support viewing resources from multiple namespaces

source: https://github.com/ray-project/kuberay/issues/4457
state: open | updated: 2026-09-22T16:58:16Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

Currently the kuberay dashboard can only display resources from the same namespace as the dashboard. However, users may have multiple k8s namespaces in addition to the NS which dashboard belongs to.


### Use case

Multi tenant  k8s. For example, RL use one namespace, ray data (offline batching) using another. Kuberay Dashboard should be able to display resources from all NS

### Related issues

_No response_

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (4)

### dentiny · 2026-05-01

I also met the issue in production today.

> Currently the kuberay dashboard can only display resources from the same namespace as the dashboard

I'm not sure if the statement is correct and accurate, it reads to me namespace is hard-coded to `default`: https://github.com/ray-project/kuberay/blob/6f1ee4863cf3d8e988032b52a31609ba0d0cc268/dashboard/src/components/NamespaceProvider.tsx#L10

### dentiny · 2026-05-01

Hi @harryge00 I'm wondering if you're working on the issue? Maybe we could collaborate on this?

### dentiny · 2026-05-01

Just as a supplement, for my production use case, (1) we have multiple namespaces in k8s cluster; (2) each team has its own namespace and that's how to do access control.

To me, this issue could be split into two tasks, all dashboard frontend change:
- Assign one or more default namespace to list, say, via environment variable
  + The reason is: it's not a good user experience if the default namespace `default` is not accessible and returns error 
- UI-wise, provide checkbox to (de)select namespace to list

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

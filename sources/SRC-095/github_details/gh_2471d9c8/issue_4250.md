# [Issue #4250] [Epic][Feature] KubeRay Cache Pod Pool 

source: https://github.com/ray-project/kuberay/issues/4250
state: open | updated: 2026-09-22T16:57:31Z
labels: enhancement, 1.6.0, 1.7.0, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

KubeRay Pod Pool Virtual Kubelet is an optional and standalone component of the KubeRay Ecosystem. It provides warmed-up pod pools by registering itself as a virtual kubelet to a Kubernetes cluster. When KubeRay requests pods from the virtual kubelet, the actual pods are taken from one of the pod pools specified by the users and effectively skip:
1. resource scheduling time
2. image pulling time
3. volume preparation time
because those pods are already active and waiting in pools.

### Use case

1. Improve the elasticity and efficiency of job-based operations, such as efficient analysis of Ray data.

2. Improve the efficiency of autoscaling in cluster-based operations to meet peak business load demands. For example, elastic scaling of inference and agent scaling.

### Related issues

_No response_

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (2)

### KunWuLuan · 2025-12-18

Hi, do you have any design doc about this feature?

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

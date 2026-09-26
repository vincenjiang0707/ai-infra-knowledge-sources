# [Issue #2052] [Feature] Support extended kube-scheduler as batch scheduler

source: https://github.com/ray-project/kuberay/issues/2052
state: closed | updated: 2026-09-23T06:29:54Z
labels: enhancement, P2, rayjob

## 正文

### Search before asking

- [X] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

[Extended kube scheduler](https://github.com/kubernetes-sigs/scheduler-plugins/blob/master/config/crd/bases/scheduling.x-k8s.io_podgroups.yaml) support coscheduling.

Can we support creating podgroups.scheduling.x-k8s.io in batch scheduler?

### Use case

_No response_

### Related issues

_No response_

### Are you willing to submit a PR?

- [X] Yes I am willing to submit a PR!

## 评论 (2)

### kevin85421 · 2025-03-19

@KunWuLuan KubeRay has already supported Volcano, YuniKorn, and Kueue. Which scheduling behaviors that these schedulers can't support and the extended kube scheduler can support?

### KunWuLuan · 2026-09-23

The core of this request — extended kube-scheduler (scheduler-plugins) support with PodGroup integration — landed in #3612 (tracked by #3611, released in v1.4.0). For integration with workloads.scheduling.k8s.io (including Kueue), tracking continues in #4344. Closing this issue.

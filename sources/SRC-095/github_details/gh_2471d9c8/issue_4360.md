# [Issue #4360] [Feature] When we use different pod priorities in different worker-groups and open volcano batch scheduler, Want to create a different podgroup for each worker-group

source: https://github.com/ray-project/kuberay/issues/4360
state: open | updated: 2026-09-22T16:57:50Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

current  situation：Turn on autoscaler and turn on volcano gang scheduling
For example, I declare that worker-1 in raycluster uses best-effort priority, worker-2 uses guaranteed priority, and specify the label of ray.io/priority-class-name = guaranteed. The pod expanded through hpa by worker-1 will also be designated as guaranteed priority

### Use case

In the data processing scenario, we expect head role use high-priority resources, worker role use low-priority resources, which can be preempt at any time, but the raycluster will remain running continuously, and worker pod will be scaled through autoscaler

### Related issues

_No response_

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (2)

### Future-Outlier · 2026-01-10

Hi, @dushulin 
feel free to submit a PR, thank you!

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

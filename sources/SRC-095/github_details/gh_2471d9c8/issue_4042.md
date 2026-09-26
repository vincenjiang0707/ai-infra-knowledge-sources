# [Issue #4042] [Feature] ObservedGeneration is missing in RayJobStatus

source: https://github.com/ray-project/kuberay/issues/4042
state: open | updated: 2026-09-22T16:56:52Z
labels: observability, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

ray-operator

### What happened + What you expected to happen

The `ObservedGeneration` is missing in RayJobStatus. After searching it, there is `ObservedGeneration` in the RayJobStatus but no where for updating it.

https://github.com/ray-project/kuberay/blob/d59cbd8901c498b17bac728be54189214fea3f30/ray-operator/apis/ray/v1/rayjob_types.go#L250-L253

### Reproduction script

Create a RayJob and check the RayJobStatus.

### Anything else

_No response_

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (5)

### Future-Outlier · 2025-09-04

Hi, @fscnick 
Based on the comment below, I think we can wait for users need this.

https://github.com/ray-project/kuberay/blob/d59cbd8901c498b17bac728be54189214fea3f30/ray-operator/controllers/ray/utils/consistency.go#L9-L33


### Future-Outlier · 2025-09-04

If we plan to support this, we should identify user use cases. For example, posting a question in the Ray Slack channel to gather feedback could be a good approach.

### fscnick · 2025-09-04

Yep, there is no user report yet. I think it could be waited.

However, there are existed in RayCluster and RayService but missing in RayJob.

https://github.com/ray-project/kuberay/blob/d59cbd8901c498b17bac728be54189214fea3f30/ray-operator/controllers/ray/raycluster_controller.go#L1162

https://github.com/ray-project/kuberay/blob/d59cbd8901c498b17bac728be54189214fea3f30/ray-operator/controllers/ray/rayservice_controller.go#L229



### Future-Outlier · 2025-09-13

we can refer statefulset source code.

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

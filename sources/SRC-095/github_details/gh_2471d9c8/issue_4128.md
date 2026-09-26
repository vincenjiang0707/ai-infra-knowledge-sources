# [Issue #4128] [Feature] ray-service

source: https://github.com/ray-project/kuberay/issues/4128
state: open | updated: 2026-09-22T16:57:12Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

I tested deploying RayServe and RayCluster to Kubernetes using Helm Chart and found some inconvenience.

How are new Served applications supposed to be deployed? I tried deploying:
https://raw.githubusercontent.com/ray-project/kuberay/master/ray-operator/config/samples/ray-service.stable-diffusion.yaml
and noticed that kind: RayService is used, unlike kind: RayCluster, which is specified in the helm-charts in this repo.

I think it makes sense to create a new helm-chart for RayServe here:
https://github.com/ray-project/kuberay/tree/master/helm-chart

How are new Served applications supposed to be added to an already deployed cluster?

What do you think? I think many would find it convenient to have a declarative Helm solution for GitOps. I might work on that.

### Use case

_No response_

### Related issues

_No response_

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (4)

### Future-Outlier · 2025-10-18

Hi, @AlexAseyev 
do you want to contribute?

### Future-Outlier · 2025-10-18

Hi, @AlexAseyev 
> How are new Served applications supposed to be added to an already deployed cluster?

you can try this.
https://docs.ray.io/en/latest/serve/getting_started.html

### colldata79 · 2026-02-01

Is this stil an issue or do we believe it is resolved ?


### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

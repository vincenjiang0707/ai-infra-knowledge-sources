# [Issue #4113] Update Ray's version to support label-based scheduling + autoscaler

source: https://github.com/ray-project/kuberay/issues/4113
state: open | updated: 2026-09-22T16:57:06Z
labels: 1.5.0, stale

## 正文

After this commit is released in Ray’s official image, we should update all Ray images in our examples and default configurations to use it.
https://github.com/ray-project/ray/pull/56532

Discussion link: https://github.com/ray-project/kuberay/pull/4106#pullrequestreview-3302029243
release ref: https://github.com/ray-project/ray/releases


## 评论 (6)

### Future-Outlier · 2025-10-06

We should also update the doc on how to use `ray start` params with `{Head|Worker}GroupSpec.Labels`.


### ryanaoleary · 2025-10-06

https://github.com/ray-project/ray/pull/56532 reads the `--labels` field from the `rayStartParams`, with https://github.com/ray-project/kuberay/pull/4106 we'll need to instead check the top level `Labels` field, which will require another change to Ray. I can try to get that in in the next release of Ray after we've added the new `.Labels` structured field.

### Future-Outlier · 2025-10-06

> [ray-project/ray#56532](https://github.com/ray-project/ray/pull/56532) reads the `--labels` field from the `rayStartParams`, with [#4106](https://github.com/ray-project/kuberay/pull/4106) we'll need to instead check the top level `Labels` field, which will require another change to Ray. I can try to get that in in the next release of Ray after we've added the new `.Labels` structured field.

Thank you Ryan, really appreciate this

### Future-Outlier · 2025-10-07

Hi, @ryanaoleary 
I also need you create a PR about "[Core][Autoscaler] Add resources to KubeRay autoscaling config" in ray.
now we only support `labels` in ray.

### ryanaoleary · 2025-10-07

> Hi, [@ryanaoleary](https://github.com/ryanaoleary) I also need you create a PR about "[Core][Autoscaler] Add resources to KubeRay autoscaling config" in ray. now we only support `labels` in ray.

@Future-Outlier I implemented support for both the new top level fields in https://github.com/ray-project/ray/pull/57260, adding them to the KubeRay autoscaling config if found. There was already support for parsing the resources ([here](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/kuberay/autoscaling_config.py#L224)) and labels ([here](https://github.com/ray-project/ray/blob/83c8ca4058bd67f6ca6b1f64fffbc1e4596ebbe3/python/ray/autoscaler/_private/kuberay/autoscaling_config.py#L303)) from the `rayStartParams` or k8s container, but now we first check the new `resources` and `labels` fields respectively since they are the most explicit.

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

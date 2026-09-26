# [Issue #5160] Inconsistent RayCluster name in ray-job.use-existing-raycluster.yaml

source: https://github.com/ray-project/kuberay/issues/5160
state: closed | updated: 2026-09-22T22:01:16Z
labels: 

## 正文

## Description

The `ray-job.use-existing-raycluster.yaml` sample selects an existing RayCluster using:
```
clusterSelector: 
    ray.io/cluster: ray-cluster-kuberay
```

However, the `ray-cluster.sample.yaml` creates a RayCluster named:

```
metadata:
  name: raycluster-kuberay
```
Because these names do not match, applying the two samples as written does not allow the RayJob to attach to the sample RayCluster.

## Suggested fix
Align the clusterSelector value in `ray-job.use-existing-raycluster.yaml` with the RayCluster name used by `ray-cluster.sample.yaml`.

## 评论 (3)

### zhuangzhewei09 · 2026-08-18

@AndySung320 hi can you assign the issue to me? I`m interested to take a PR   cc @machichima 

### machichima · 2026-08-18

@AndySung320 do you want to work on this? If not we can assign it to @chacha923 

### AndySung320 · 2026-08-18

Hi @machichima, feel free to assign to @chacha923 ~

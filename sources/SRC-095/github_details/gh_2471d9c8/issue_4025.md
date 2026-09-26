# [Issue #4025] [Feature] Enable GCS Fault Tolerance for Kuberay-Operator Lifecycled Ray Cluster

source: https://github.com/ray-project/kuberay/issues/4025
state: open | updated: 2026-09-22T16:56:41Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

When you create a RayJob and pass a RayClusterSpec, Kuberay lifecycles the RayCluster for that job. If you were to enable GCS FT for this Job's RayCluster, it would be effectively useless. If the GCS fails, the Job is marked as failed and the cluster torn down. If you set a `backoffLimit` it will retry, but Kuberay creates a new RayCluster for the Job instead of retrying the failed cluster. This circumvents the usefulness of GCS Fault Tolerance. 

This feature could be a flag or an env var that could enable Kuberay to retry the failed cluster instead of spinning up new ones. This would make GCS FT useful for lifecycled Ray Clusters. It could be an env var, something like `retryFailedCluster: true`.

### Use case

I want to submit RayJobs and have Kuberay Operator lifecycle a RayCluster for each Job. If GCS fails, I don't want to lose the state of my RayCluster - so I would like to enable GCS Fault Tolerance and Kuberay to retry the failed cluster instead of creating new ones. 

### Related issues

_No response_

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (4)

### rueian · 2025-09-01

Hi @kryanbeane, I’m not sure what benefit we’d get from retrying a failed job on the old cluster, but I think this can be achieved by specifying clusterSelector to target a GCS FT-enabled cluster. We want to avoid CRD changes whenever possible.

### kryanbeane · 2025-09-02

hey @rueian & @Future-Outlier, thanks for looking at this

The key here is that if your cluster (and so the Job too) failed because of the GCS, without GCS FT and retrying the same Cluster, you lose all Actor & Task state in the ray cluster, and by using a new RayCluster to retry, you lose all of the state in the GCS. For me, I prefer to have Kuberay lifecycle the RayCluster for me so I don't need to worry about spinning up and tearing down RayClusters, but if GCS fails during job execution I lose all that's in it. 

The idea here would be to not change the CRD, but have an env var that changes the use case of `backoffLimit` so if for example the env var called `retryFailedCluster` was set to true, and the already existing field `backoffLimit` was set to 3, then instead of Kuberay retrying 3 times with new RayClusters, it could retry the failed RayCluster which would retain Actor / Task state from the GCS. Wdyt?

### andrewsykim · 2025-09-02

What's the use-case for needing GCS FT for RayJob though? Is there a use-case that benefits from retrying against an existing state? 

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

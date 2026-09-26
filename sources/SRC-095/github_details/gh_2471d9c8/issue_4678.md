# [Issue #4678] [Bug] RayCluster with GCS fault tolerance can become un-deletable

source: https://github.com/ray-project/kuberay/issues/4678
state: open | updated: 2026-09-23T04:42:21Z
labels: bug, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

ray-operator

### What happened + What you expected to happen

1. Create a RayCluster with GCS fault tolerance enabled as well as some invalid fields, like a head pod name that is not RFC 1035 compliant or similar. 
    - I observed this with an empty `spec.gcsFaultToleranceOptions.redisPassword.valueFrom.secretKeyRef.name`
3. The cluster should be broken, the head cannot be created
4. Delete the cluster
5. The cluster will get the `ray.io/gcs-ft-redis-cleanup-finalizer` finalizer but never delete
6. The operator is attempting to create a redis cleanup job that will never be accepted forever.
 
The only way to recover this is to edit the raycluster to fix the invalid field, and then it can be deleted.

Expected behavior:
- Maybe tighter validation of the redispassword field, for the specific failure. 
- Minimal user generated fields are used to clean up redis to limit potential errors.
- Maybe RayClusters that have never become ready do not need a clean up job.

### Reproduction script

.

### Anything else

_No response_

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (4)

### Future-Outlier · 2026-04-11

cc @fscnick to take a look

### fscnick · 2026-04-18

After a short survey, the RayCluster still gets deleted after the cleanup job has been timeout. However, it takes a bit of long time.

The reason might be the cleanup job shares some settings of the head pod.
https://github.com/ray-project/kuberay/blob/b916d9eef669e2f194a099c922726aaad2b6372c/ray-operator/controllers/ray/raycluster_controller.go#L1439-L1443

If the head pod has the issue of getting up, so does the cleanup job likely. This makes the deletion blocked until the cleanup job timeout.

The possible solution as following:
1. Build up the validation to fail the RayCluster earlier.
2. Find a state during the starting up of the RayCluster. If the RayCluster failed before this state, the `command` has not been executed. The redis would not contain the data yet. The cleanup job isn't needed.

Currently, I am looking for the solution 2. For solution 1, because there are many wrong settings to make the RayCluster failed, it might be inappropriate to build up the validation for each possibility. Discussion is welcome if there are some different opinion.

cc @Future-Outlier 

### yaroslava-serdiuk · 2026-04-24

/cc

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

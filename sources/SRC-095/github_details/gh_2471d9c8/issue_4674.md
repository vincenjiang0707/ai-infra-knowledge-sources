# [Issue #4674] [operator] RayClusterProvisioned stays False and RayJob stuck in Initializing when enableInTreeAutoscaling: true with initial replicas: 0

source: https://github.com/ray-project/kuberay/issues/4674
state: open | updated: 2026-09-23T04:42:17Z
labels: stale

## 正文

## Bug

When a RayJob uses `enableInTreeAutoscaling: true` with `workerGroupSpecs[0].replicas: 0` and `minReplicas: 1`, the `RayClusterProvisioned` condition never transitions to `True` and `State` never becomes `Ready`. This causes the RayJob `jobDeploymentStatus` to stay `Initializing` indefinitely, even though workers are actively processing data.

## Root cause

Two checks in `calculateStatus` (`raycluster_controller.go`) are too strict for autoscaling clusters:

**1. `State = Ready` requires exact pod count match (line ~1593):**
```go
if reconcileErr == nil && len(runtimePods.Items) == int(newInstance.Status.DesiredWorkerReplicas)+1 {
```
With autoscaling, `DesiredWorkerReplicas` is a moving target because the autoscaler continuously patches `spec.replicas`. The pod count rarely matches the desired count at the moment the check runs. Additionally, `reconcilePods` returns an error when deleting unhealthy pods (workers with terminated containers under `RestartPolicy: Never`), which blocks this check via `reconcileErr != nil`.

**2. `RayClusterProvisioned` uses `CheckAllPodsRunning` on all pods (line ~1623):**
```go
if utils.CheckAllPodsRunning(ctx, runtimePods) {
```
During autoscaling, `runtimePods` includes pods in transition (Pending from scale-up, Terminating from scale-down). `CheckAllPodsRunning` fails if ANY pod is not Running/Ready. Since the autoscaler frequently adjusts the pod set, there are almost always pods in transition during initial provisioning.

**3. The RayJob controller gates `Initializing → Running` on `State == Ready` (line ~217):**
```go
if rayClusterInstance.Status.State != rayv1.Ready {
    break // stays in Initializing
}
```

## How to reproduce

1. Create a RayJob with:
   - `enableInTreeAutoscaling: true`
   - `workerGroupSpecs[0].replicas: 0`, `minReplicas: 1`, `maxReplicas: 20`
   - `submissionMode: SidecarMode`
2. Observe that `jobDeploymentStatus` stays `Initializing` even though workers are actively processing

```
$ kubectl get rayjob <name> -o jsonpath='{.status}'
jobDeploymentStatus: Initializing
RayClusterProvisioned: False
  reason: RayClusterPodsProvisioning
desiredWorkerReplicas: 1
availableWorkerReplicas: 1
HeadPodReady: True
```

## Proposed fix

1. Filter out terminating pods (DeletionTimestamp != nil) from `runtimePods` before the State and RayClusterProvisioned checks
2. When autoscaling is enabled, use `ReadyWorkerReplicas >= MinWorkerReplicas` instead of requiring all pods to match — the cluster is operational once the head and minimum workers are running, regardless of ongoing autoscaler adjustments

## 评论 (1)

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

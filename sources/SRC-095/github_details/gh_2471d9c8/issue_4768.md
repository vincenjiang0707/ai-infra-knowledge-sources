# [Issue #4768] [KubeRay][Autoscaler] Cluster-level idle termination via Ray Autoscaler

source: https://github.com/ray-project/kuberay/issues/4768
state: open | updated: 2026-09-23T04:42:47Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.

Related to https://github.com/ray-project/kuberay/issues/2998

## Summary

Ray Autoscaler today scales **worker** pods to zero based on per-node-type `idleTimeoutSeconds`, but the **head pod, head Service, and the RayCluster CR itself** persist even when no Ray jobs, actors, or placement groups exist on the cluster. For users who back the head with reserved capacity this leftover cost is non-trivial. 

PR #4400 tried (KubeRay polls Ray Dashboard's `/api/component_activities`) and was closed because we don't want the operator to open new HTTP connections to RayClusters. So i pursues Ray Autoscaler, but there are **three plausible ways** to wire it up. Each has a different blast radius, RBAC profile, and feature surface.

The three options share a common detection way and differ in **how the autoscaler signals "the cluster is idle" and who performs the termination**:

| | Option A, autoscaler patches `spec.suspend=true` | Option B, autoscaler reports a status condition, operator acts | Option C, autoscaler deletes the RayCluster CR directly |
|---|---|---|---|
| Who terminates | Autoscaler (via spec patch) | Operator (after observing condition) | Autoscaler (via DELETE) |
| New RBAC | None | `rayclusters/status: [patch]` | `rayclusters: [delete]` |
| Where the policy lives | In autoscaler | Operator reconcile branch | In autoscaler |


## ### CRD changes

```yaml
spec:
  enableInTreeAutoscaling: true
  autoscalerOptions:
    idleTerminationSeconds: 1800
      ...
```

## Option A, autoscaler patches `spec.suspend=true` directly

### How it works

When the predicate fires for `idleTerminationSeconds`, `KubeRayNodeProvider` issues:

```json
{"op": "replace", "path": "/spec/suspend", "value": true}
```

KubeRay's existing `RayClusterSuspending` → `RayClusterSuspended` lifecycle takes over: head and worker pods deleted, Services cleaned up, condition flipped to `Suspended`. The CR remains in the cluster with `spec.suspend=true`.

https://github.com/ray-project/kuberay/blob/262d0f458af7fc9e820307fa72371acdd8df704a/ray-operator/controllers/ray/raycluster_controller.go#L628-L644

The autoscaler dies with the head pod (it's a sidecar). That's fine, the work is already done; suspension is a one-shot.


## Option B, autoscaler reports, operator acts

### How it works

When the predicate fires, `KubeRayNodeProvider` patches `RayCluster.status.conditions` or add a annotations like ["ray.io/idle-ttl-expired"] == "true":

```json
  {                                                                                                                                                                                     
    "type": "RayClusterIdleTimeout", 
    "status": "True",
    "reason": "ClusterIdlePastTTL",
    "message": "Cluster idle for 1823s exceeds idleTerminationSeconds=1800s",
    "lastTransitionTime": "2026-04-25T10:30:00Z"                                                                                                                                        
  }
```

The autoscaler is the sole timer source-of-truth: it only flips the condition to True when every alive node has status == `IDLE` AND min(`idle_duration_ms` across alive nodes) / 1000 > `idleTerminationSeconds`. The operator acts on True immediately.                                 
  
Operator side                                                                                                                                                                         
```
  if cond := meta.FindStatusCondition(rc.Status.Conditions, "IdleTTLExpired"); 
     cond != nil && cond.Status == metav1.ConditionTrue {
      r.recorder.Eventf(rc, corev1.EventTypeNormal, "IdleTTLExpired", cond.Message)  
      return ctrl.Result{}, r.Delete(ctx, rc)
  }                                                                                                                                                                                     
 ```

## Option C, autoscaler deletes the RayCluster CR directly

When the predicate fires, the autoscaler issues to delete the RayCluster CR:

```
DELETE /apis/ray.io/v1/namespaces/<ns>/rayclusters/<name> 
``` 

-----
I prefer option B, cause it keeps the autoscaler in the observer role, which has concrete benefits the other options lose:

### Use case

_No response_

### Related issues

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (6)

### 400Ping · 2026-04-26

Looks nice, are you planning to work on this?

### win5923 · 2026-04-26

I don’t have the bandwidth to work on this right now, feel free to take it if you’d like.

### 400Ping · 2026-04-26

Ok sure.

### roulbac · 2026-05-05

I'd love this feature, and option B makes sense. 

Curious, when "IdleTTLExpired" is set to True, is there a mechanism to prevent the head node from admitting new jobs/tasks? Thinking just in case the cluster hadn't been cleaned up by the operator yet and someone tries to run stuff on it after it was marked for expiry.

### 400Ping · 2026-05-05

I already have a draft on my local desktop, will push here soon.

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

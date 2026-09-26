# [Issue #2670] [RFC]: Add pending replica guard to PodAutoscaler KPA/APA to prevent cascading scale-up

source: https://github.com/vllm-project/aibrix/issues/2670
state: closed | updated: 2026-09-16T00:01:55Z
labels: area/autoscaling

## 正文

## Summary

AIBrix PodAutoscaler should add a pending replica guard for KPA/APA strategies to prevent repeated scale-up while previously requested replicas are still pending and have not started reporting metrics.

For LLM workloads, pod startup can take minutes due to image pull, GPU scheduling, model loading, and readiness checks. During this period, newly created pods usually do not emit serving metrics. If the autoscaler computes desired replicas only from the currently ready pods, it can repeatedly scale up every reconciliation cycle before the previous scale-up has taken effect.

## Motivation

Current KPA/APA autoscaling can enter a cascading scale-up pattern:

```text
t0: ready=2, current=2, pending=0
    rawDesired=4
    set replicas=4

t1: ready=2, current=4, pending=2
    new pods are not Ready and have no metrics yet
    ready-pod metrics are still high
    rawDesired=8
    set replicas=8

t2: ready=2, current=8, pending=6
    metrics are still high on the same ready pods
    rawDesired=16
    set replicas=16
```

This can cause replica leakage: replicas keep accumulating because the autoscaler repeatedly reacts to the same capacity deficit while earlier scale-up replicas are still pending. For LLM inference, this is especially risky because startup latency is high and pending pods may not contribute any capacity for several minutes.

Kubernetes HPA handles similar scenarios through conservative treatment of not-yet-ready pods and missing metrics. For scale up, pods without metrics are treated conservatively; for scale down, missing metrics suppress aggressive downscale. AIBrix KPA/APA are implemented in the PodAutoscaler controller, so we can apply a simpler and more conservative guard in our own pipeline.

## Proposed Change

For KPA/APA strategies, compute the raw desired replicas as today, then apply a pending replica guard before writing the final desired replica count.

Proposed first version:

```text
rawDesired = existing KPA/APA recommendation based on ready pod metrics

pendingReplicas = max(currentReplicas - readyReplicas, 0)

if pendingReplicas > 0:
  if rawDesired > currentReplicas:
      desired = currentReplicas
      reason = "scale-up suppressed: pending replicas have no metrics yet"
  if rawDesired < currentReplicas:
      desired = currentReplicas
      reason = "scale-down suppressed: pending replicas not ready"
else:
  desired = rawDesired
```

In other words, while a PodAutoscaler has pending replicas, KPA/APA should hold the target at the current replica count and wait for the pending replicas to become ready before making another scaling decision.

This should be implemented as an autoscaling pipeline guard rather than inside each individual algorithm, so future algorithms can reuse the same behavior.

Potential implementation shape:

- Add internal replica state to the KPA/APA compute request, such as `ReadyReplicas` and `PendingReplicas`, or a small `ReplicaState` struct.
- Count ready pods in the PodAutoscaler reconcile path using the target selector and Ready condition.
- Derive pending replicas from the scale target replica count and ready replicas.
- After selecting the best raw recommendation across metric sources, apply the pending replica guard once.
- Update status/reason so users can see when scaling was held due to pending replicas.
- Keep HPA strategy unchanged because Kubernetes HPA already owns its own not-ready/missing-metrics logic.

No new PodAutoscaler CRD fields are proposed for the first version. This should be a default safety behavior for LLM autoscaling rather than a user-facing tuning option.

## Alternatives Considered

1. **HPA-style conservative recomputation**

   More closely mimic Kubernetes HPA by treating missing/pending pods as 0% utilization for scale-up and 100% utilization for scale-down, then recomputing the desired replica count.

   This is more nuanced, but also more complex. For LLM workloads, pending pods often provide zero serving capacity for minutes, so a strict hold is simpler and safer as a first version.

2. **Expose a timeout or user-configurable pending policy**

   A timeout could avoid a broken pending pod blocking future scale-up indefinitely. However, choosing a correct timeout is difficult for LLM workloads because model startup times vary widely. Kubernetes HPA keeps this type of behavior mostly as controller-level logic rather than per-HPA API fields.

   The first version should avoid new CRD fields or annotations. If real deployments show that stale pending pods commonly block scaling, we can later add an internal default timeout or an annotation.

3. **Use current replicas as algorithm input directly**

   Passing `currentReplicas` instead of ready replicas into the algorithm reduces repeated scale-up, but mixes metric semantics with replica accounting and may still produce confusing behavior. A post-algorithm guard keeps the existing algorithm behavior intact and makes the safety policy explicit.

## Expected Behavior

With the guard:

```text
t0: ready=2, current=2, pending=0
    rawDesired=4
    set replicas=4

t1: ready=2, current=4, pending=2
    rawDesired=8
    pendingReplicas > 0
    hold replicas=4

t2: ready=2, current=4, pending=2
    rawDesired=8
    pendingReplicas > 0
    hold replicas=4

t3: ready=4, current=4, pending=0
    recompute using updated metrics
    scale again only if capacity is still insufficient
```

This prevents repeated scaling on the same unresolved capacity deficit and reduces the chance of runaway replica growth for slow-starting LLM pods.


## 评论 (7)

### czczycz · 2026-09-05

Using pending pods alone cannot reliably distinguish pods created by an autoscaling action from pods pending for unrelated reasons, such as a rolling update, pod eviction, scheduling failures, or other workload changes.

The guard therefore needs a way to determine whether the pending state is actually attributable to a recent autoscaling decision. Pending pods not caused by autoscaling should not activate this guard; otherwise, unrelated transient workload conditions could incorrectly block further scaling.

### googs1025 · 2026-09-05

> Using pending pods alone cannot reliably distinguish pods created by an autoscaling action from pods pending for unrelated reasons, such as a rolling update, pod eviction, scheduling failures, or other workload changes.
> 
> The guard therefore needs a way to determine whether the pending state is actually attributable to a recent autoscaling decision. Pending pods not caused by autoscaling should not activate this guard; otherwise, unrelated transient workload conditions could incorrectly block further scaling.

Thanks for the feedback. I updated the implementation to avoid treating pending pods as a hard autoscaling blocker.

  The new logic follows the conservative idea for missing/unready metrics:

  - For scale-up, pending replicas are treated as having no metrics contribution, which dampens the computed desired replicas and avoids over-scaling while newly created pods are not ready yet.
  - For scale-down, pending replicas are treated as being at the target utilization, which avoids over-aggressive scale-down while those pods are still coming up.
  - The guard only applies to KPA/APA when there are pending replicas and the conservative recomputation changes the recommendation. HPA behavior remains delegated to Kubernetes.

  This means the controller no longer needs to determine whether a pending pod was caused by autoscaling, rollout, scheduling delay, or another external factor. Instead, it handles incomplete pod metrics conservatively, similar to HPA, so unrelated pending pods do not fully suppress scaling decisions.


### googs1025 · 2026-09-05

 I intentionally avoided attribution-based logic here because reliably determining why a pod is pending would require correlating autoscaler decisions with workload rollout, eviction, scheduling, and controller timing. That adds statefulness and edge cases to the autoscaler path, while still being hard to make fully reliable. The conservative recomputation gives us the safety property we need without depending on fragile pending-pod attribution.

### czczycz · 2026-09-05

> I intentionally avoided attribution-based logic here because reliably determining why a pod is pending would require correlating autoscaler decisions with workload rollout, eviction, scheduling, and controller timing. That adds statefulness and edge cases to the autoscaler path, while still being hard to make fully reliable. The conservative recomputation gives us the safety property we need without depending on fragile pending-pod attribution.

`pendingReplicas = currentReplicas - readyReplicas` assumes that every non-Ready Pod has no metric contribution. This is not always true.
For example, before a Pod becomes Ready, it may already report non-zero CPU usage during model loading/initialization, and it may already expose gpu_cache_usage_perc through the metrics endpoint. The current collector also attempts to fetch metrics from all selected Pods, not only Ready ones.
As a result, a non-Ready Pod’s value may already be included in the aggregated metric, while the pending-replica adjustment treats the same Pod as a zero/missing-metric replica. This can discount its contribution twice and under-estimate the desired replica count.

### googs1025 · 2026-09-05

 I agree this is a trade-off. In some practical cases, I expect the impact of pending or not Ready Pods to be limited because the condition is usually transient and the conservative recomputation only dampens recommendations instead of fully blocking scaling.

  The current implementation intentionally uses readiness as a conservative proxy instead of adding more state, attribution logic, or tighter coupling between metric collection and replica adjustment. I agree it is not perfectly equivalent to metric availability, and a non-Ready Pod that already exposes metrics could be discounted more than necessary.

  That said, I think this is acceptable for now as a conservative first version. If there are concrete production scenarios where non-Ready Pods commonly expose meaningful autoscaling metrics for a long time and this causes under-scaling, we can discuss refining the adjustment to use actual metric sample coverage instead.


### czczycz · 2026-09-05

> I agree this is a trade-off. In some practical cases, I expect the impact of pending or not Ready Pods to be limited because the condition is usually transient and the conservative recomputation only dampens recommendations instead of fully blocking scaling.
> 
> The current implementation intentionally uses readiness as a conservative proxy instead of adding more state, attribution logic, or tighter coupling between metric collection and replica adjustment. I agree it is not perfectly equivalent to metric availability, and a non-Ready Pod that already exposes metrics could be discounted more than necessary.
> 
> That said, I think this is acceptable for now as a conservative first version. If there are concrete production scenarios where non-Ready Pods commonly expose meaningful autoscaling metrics for a long time and this causes under-scaling, we can discuss refining the adjustment to use actual metric sample coverage instead.

I agree with you, your PR won't make things worse; in most cases, it actually has a positive effect. It's fine as the first version, but we need to think about possible directions for future improvements.

In my experience, scaling up a LLM's inference service pod(from pending to ready) sometimes takes 10-20 minutes, especially in cases where the TP size is relatively large.

### googs1025 · 2026-09-05

 @czczycz  😄 Thanks for the detailed feedback and discussion.

  There are still many autoscaler-related areas in AIBrix that could benefit from more review and design input. For example, #2613 is another ongoing autoscaling topic. If you are interested, please take a look at the latest proposal/design there as well. Any suggestions or feedback would be very valuable.


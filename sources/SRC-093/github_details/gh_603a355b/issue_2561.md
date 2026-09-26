# [Issue #2561] Discussion: Cache-aware rescheduling for recreated StormService/RoleSet pods

source: https://github.com/vllm-project/aibrix/issues/2561
state: closed | updated: 2026-09-15T14:48:02Z
labels: area/disaggregated

## 正文

## Proposal

I would like to propose adding an opt-in cache-aware rescheduling policy for AIBrix `StormService` / `RoleSet` workloads.

The goal is to help recreated pods land back on nodes where their previous replicas already ran, so they can reuse node-local model weights, image layers, compilation caches, local NVMe data, or other runtime cache artifacts.

This issue is intended to start discussion with maintainers. It is not a finalized API proposal.

## Background

AIBrix already has `InPlaceIfPossible` support for `RoleSet` role updates. That path is valuable when a pod can be updated without deleting and recreating the pod.

However, in-place update is not always possible. For example, changes to non-image pod fields, init container images, scheduling fields, volumes, or other immutable pod properties may require pod recreation. In those cases, the replacement pod is normally scheduled by Kubernetes without awareness of where the previous pod ran.

For LLM workloads, that can be expensive. If a replacement pod lands on a different node, it may need to re-download large model weights or rebuild local runtime caches, even though the old node already had useful cached state.

## Business Value

Cache-aware rescheduling would help AIBrix users:

- reduce rollout time when pods must be recreated
- reuse node-local model weights and runtime caches
- reduce repeated model downloads from remote storage
- improve GPU utilization by shortening post-recreate startup time
- improve recovery time after pod eviction or failure
- make `InPlaceIfPossible` fallback behavior less costly

This is especially useful for large model serving where model artifacts may be tens or hundreds of GB and node-local cache reuse can save minutes per pod.

## Relationship to Existing `InPlaceUpdate`

This proposal is complementary to existing in-place update support:

- `InPlaceUpdate`: avoid deleting the pod when the update is safe.
- cache-aware rescheduling: when the pod must be deleted and recreated, steer the new pod back to the historical node.

In other words, this feature improves the fallback path when true in-place update is not possible.

## Proposed MVP

Start with a small opt-in policy for `RoleSet` pods managed by `StormService`.

Possible role-level annotation:

```yaml
apiVersion: orchestration.aibrix.ai/v1alpha1
kind: StormService
metadata:
  name: qwen
spec:
  template:
    spec:
      roles:
      - name: decode
        annotations:
          orchestration.aibrix.ai/inplace-scheduling: "Preferred"
        updateStrategy:
          type: InPlaceIfPossible
        template:
          spec:
            containers:
            - name: engine
              image: registry.example.com/vllm:v2
```

The MVP could support:

- `Preferred`: inject preferred node affinity toward the historical node
- optional `Required`: inject required node affinity for strict same-node replacement
- Stateful role replica index granularity first
- in-memory node binding store in the controller
- only record bindings from Running and Ready pods

## Execution Model

The controller would:

1. During reconciliation, list pods for a `RoleSet` role.
2. For each Running and Ready pod, record its historical node binding.
3. When the controller creates a replacement pod for the same role replica slot, look up the historical node.
4. If a binding exists and the feature is enabled, inject node affinity into the new pod before creation.

For `Preferred` mode:

```yaml
affinity:
  nodeAffinity:
    preferredDuringSchedulingIgnoredDuringExecution:
    - weight: 100
      preference:
        matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - node-a
```

For `Required` mode:

```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - node-a
```

## Possible Binding Key

For the first version, AIBrix can use the existing role replica index information:

```text
{rolesetUID}/{roleName}/{roleReplicaIndex}
```

This works well for the current stateful role path where each role replica has a stable slot index.

Future versions could support broader binding granularities, such as role/component-level binding, if AIBrix introduces richer multi-pod instance/component abstractions.

## MVP Boundaries

To keep the first version focused, I suggest not including:

- persistent binding storage
- component-level binding
- automatic degradation from `Required` to `Preferred`
- complex conflict resolution with user-authored required node affinity
- cross-RoleSet or cross-StormService binding reuse
- scheduler plugin integration

The controller can keep bindings in memory. If the controller restarts, cache-aware scheduling simply loses history and falls back to normal scheduling. That seems acceptable for an MVP.

## Interaction With Existing Scheduling Features

AIBrix already has topology policy support. Cache-aware rescheduling should not overwrite user-authored scheduling constraints.

Open behavior to define:

- If the pod already has required node affinity, should the controller skip injection or merge only preferred affinity?
- If topology policy is required and conflicts with historical node affinity, which policy should win?
- Should `Preferred` be the only supported MVP mode to avoid unschedulable pods?

## Risks

- `Required` mode can leave pods Pending if the historical node is unavailable.
- In-memory bindings are lost on controller restart.
- Historical nodes may no longer be suitable if hardware labels, taints, or local cache contents changed.
- Incorrect affinity merging could conflict with user-specified scheduling constraints.

These risks can be reduced by making the feature opt-in and using `Preferred` as the recommended/default mode.

## Open Questions

- Should the first version support only `Preferred` mode?
- Should this be configured via role annotation or a typed field under `RoleSpec`?
- Should bindings be persisted in status or kept in memory only?
- Should the first version apply only to StatefulRoleSyncer paths?
- How should this interact with existing topology policy and user-defined node affinity?


## 评论 (4)

### googs1025 · 2026-08-21

cc @Jeffwan @varungup90 

### varungup90 · 2026-08-22

Thanks for writing this up. I agree with the direction.

`InPlaceIfPossible` already covers the cheap path. When we have to recreate, the replacement pod is scheduled with no memory of the old node, and that is expensive for LLM workloads. An opt-in historical-node preference on stateful RoleSet slots is a reasonable complement, not a replacement for in-place update.

A few suggestions for the MVP:

1. **Preferred only.** I would not ship `Required` in v1. Hard hostname pins are easy to deadlock on GPU nodes, and we already default `TopologyPolicy` to `Preferred` for the same reason.
2. **Watch the surge path.** In `StatefulRoleSyncer.Rollout`, if `maxUnavailable` is exhausted we create the replacement while the old pod is still running. The old replica still holds the GPU, so preferred affinity to that node usually will not win, and required affinity can wait forever because the old pod is not deleted until the new one is ready. This feature helps most after eviction, failure, or recreate-with-`maxUnavailable`. Call that out, and skip injection when it would deadlock a surge.
3. **Do not keep bindings only in memory.** History disappearing on controller restart / leader failover is the wrong tradeoff for a recovery feature. The node is already on `pod.Spec.NodeName` while the pod exists, including `Terminating`. Read that first, and persist `{role, replicaIndex} → node` on RoleSet status (or a controller annotation) for the gap after the pod is gone.
4. **Be explicit about which cache actually survives.** Image layers are already scored by kube-scheduler `ImageLocality`. `emptyDir` compilation / HuggingFace caches die with the pod. The real win is `hostPath`, local PV, and other node-durable artifacts. We should say that so users do not enable this, land back on the old node, and still wait on a cold `emptyDir`.
5. **Typed field, not `inplace-scheduling`.** The name is misleading (this is historical-node preference, not in-place update), and `TopologyPolicy` is already typed. I would put this on `RoleUpdateStrategy` or a small `RoleSpec` field, default `Preferred`. Skip injection if the template already has required `nodeAffinity`; merge preferred terms only. `TopologyPolicy` injects pod affinity and this would inject node affinity, so they do not overwrite, but `Required` hostname topology plus a pin to a *different* historical node can still conflict.

Stateful slot index is the right v1 key. Stateless has no identity, and `podGroupSize > 1` / PodSet can be a follow-up.

Happy to review a small `Preferred`-only prototype on that path.

### Jeffwan · 2026-08-22

Do you like to make a change in scheduler plugin to consume `orchestration.aibrix.ai/inplace-scheduling: "Preferred"`? 

### googs1025 · 2026-08-22

> Do you like to make a change in scheduler plugin to consume `orchestration.aibrix.ai/inplace-scheduling: "Preferred"`? 

Thanks for asking. I do **not** intend to change the scheduler plugin.

  The idea is controller-side only: AIBrix records the historical node for a stateful RoleSet replica slot, and when the controller has to create a replacement Pod, it injects native Kubernetes `nodeAffinity` into that new Pod before creation. The kube-scheduler then consumes the normal Pod affinity fields; no scheduler-plugin-specific API is required.

> Typed field, not inplace-scheduling. The name is misleading (this is historical-node preference, not in-place update), and TopologyPolicy is already typed. I would put this on RoleUpdateStrategy or a small RoleSpec field, default Preferred. Skip injection if the template already has required nodeAffinity; merge preferred terms only. TopologyPolicy injects pod affinity and this would inject node affinity, so they do not overwrite, but Required hostname topology plus a pin to a different historical node can still conflict.

  Also, I agree the name `inplace-scheduling` is misleading. This is not part of the successful in-place update path. A clearer name may be something like `replacementSchedulingPolicy.historicalNode`.

  The intended flow is:

  ```mermaid
  flowchart TD
      A[RoleSet reconcile] --> B[List role Pods]
      B --> C[Refresh historical bindings from pod.spec.nodeName]
      C --> D{Role update needed?}
      D -- no --> Z[Done]
      D -- yes --> E{Can update in place?}

      E -- yes --> F[Patch existing Pod in place]
      F --> G[No new Pod created]
      G --> H[No scheduler involved]
      H --> Z

      E -- no --> I[Fallback to recreate]
      I --> J{Replacement Pod will be created?}
      J -- no --> K[Delete old Pod / wait for budget]
      K --> Z

      J -- yes --> L{Historical node binding exists?}
      L -- no --> M[Create Pod normally]
      L -- yes --> N{Old same-slot Pod still active?}

      N -- yes --> O[Skip historical-node injection for surge path]
      N -- no --> P[Inject preferred nodeAffinity to historical node]

      O --> Q[Create replacement Pod]
      P --> Q
      M --> Q
      Q --> R[kube-scheduler schedules using native nodeAffinity]
```


  So the relationship with InPlaceIfPossible is:

  - If in-place update succeeds, no replacement Pod is created and this policy is unused.
  - If in-place update is not possible and AIBrix falls back to recreation, the policy may apply to the replacement Pod.
  - The policy does not change maxUnavailable / maxSurge; it only affects placement when a replacement Pod is created.
  - For strongest cache reuse, users should prefer delete-before-create rollout, for example maxSurge: 0 and maxUnavailable > 0.
  - For surge-first rollout, for example maxUnavailable: 0 and maxSurge > 0, the old Pod may still occupy the historical GPU node, so the controller should skip injection or treat it
    as best-effort only.

 I would keep this as Preferred only. Required hostname pinning can easily deadlock on GPU nodes, especially when the old Pod is still running or the historical node is unavailable.



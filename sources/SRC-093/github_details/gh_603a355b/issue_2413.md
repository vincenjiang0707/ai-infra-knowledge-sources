# [Issue #2413] [Feature] Support drain-aware RoleSet rollout and scale-in

source: https://github.com/vllm-project/aibrix/issues/2413
state: open | updated: 2026-09-01T09:21:20Z
labels: area/gateway, area/disaggregated

## 正文

## Background

Currently, RoleSet deletes pods directly during rollout or scale-in.

For LLM serving workloads, this can interrupt in-flight requests, especially when:

- streaming decode requests are still producing tokens;
- decode pods in P/D disaggregation still have active streams;
- SGLang async prefill still has unfinished prefill requests;
- the gateway may continue routing new requests to a pod that is about to be deleted.

This can cause long-tail request failures, broken streams, and inconsistent prefill/decode state.

## Goal

RoleSet should support a simple time-based drain window before deleting pods:

1. The RoleSet controller selects a pod to delete.
2. Instead of deleting it immediately, the controller marks the pod as draining.
3. The gateway/router observes the draining state and stops routing new requests to the pod.
4. The controller waits for the configured `drain.timeoutSeconds`.
5. After the wait window expires, the controller deletes the pod.

This should work for both direct `RoleSet` users and the more common `StormService` users.

## API Design

Add an optional `Drain` field to `RoleSpec`.

Because `StormService` reuses `RoleSetSpec` through `spec.template.spec`, this field can be configured in both:

- `RoleSet.spec.roles[].drain`
- `StormService.spec.template.spec.roles[].drain`

### Go struct

```go
type RoleSpec struct {
    Name string `json:"name,omitempty"`

    // Replicas is the number of desired replicas.
    // +optional
    Replicas *int32 `json:"replicas,omitempty"`

    // Drain configures a time-based drain window before deleting pods
    // during rollout or scale-in.
    //
    // When unset, or when TimeoutSeconds is nil/0, RoleSet keeps the
    // current behavior and deletes pods immediately.
    //
    // When TimeoutSeconds > 0, RoleSet marks the selected pod as draining,
    // waits for the configured timeout, and then deletes the pod.
    //
    // +optional
    Drain *RoleDrainSpec `json:"drain,omitempty"`

    // ... existing fields ...
}
```

```go
// RoleDrainSpec configures drain-aware deletion for pods belonging to a role.
type RoleDrainSpec struct {
    // TimeoutSeconds is the time-based drain window before deleting a pod.
    //
    // If unset or 0, drain-aware deletion is disabled.
    // If greater than 0, the RoleSet controller marks the pod as draining,
    // waits this duration, and then deletes the pod.
    //
    // +optional
    // +kubebuilder:validation:Minimum=0
    TimeoutSeconds *int32 `json:"timeoutSeconds,omitempty"`
}
```

## StormService Example

```yaml
apiVersion: orchestration.aibrix.ai/v1alpha1
kind: StormService
metadata:
  name: llama-pd
spec:
  replicas: 1
  selector:
    matchLabels:
      app: llama-pd
  template:
    metadata:
      labels:
        app: llama-pd
    spec:
      roles:
      - name: prefill
        replicas: 2
        drain:
          timeoutSeconds: 30
        template:
          spec:
            containers:
            - name: engine
              image: example/prefill:latest
      - name: decode
        replicas: 4
        drain:
          timeoutSeconds: 120
        template:
          spec:
            containers:
            - name: engine
              image: example/decode:latest
```

## RoleSet Example

```yaml
apiVersion: orchestration.aibrix.ai/v1alpha1
kind: RoleSet
metadata:
  name: llama-pd-rs
spec:
  roles:
  - name: decode
    replicas: 4
    drain:
      timeoutSeconds: 120
    template:
      spec:
        containers:
        - name: engine
          image: example/decode:latest
```

## Field Semantics

- If `drain` is unset, existing behavior is preserved and pods are deleted without waiting.
- If `drain.timeoutSeconds` is unset or `0`, existing behavior is preserved.
- If `drain.timeoutSeconds > 0`, drain-aware deletion is enabled.
- Before deleting a pod, the controller marks it as draining and waits for the configured timeout.
- After the timeout expires, the controller deletes the pod to avoid blocking rollout or scale-in forever.

## Draining Annotations

When a pod is selected for deletion, the RoleSet controller patches the pod with:

```yaml
aibrix.ai/draining: "true"
aibrix.ai/drain-start-time: "<RFC3339 timestamp>"
aibrix.ai/drain-reason: "scale-in" # or "rollout"
aibrix.ai/drain-target-action: "delete" # future values may include "sleep"
```

These annotations are used to:

- let the gateway/router identify draining pods;
- let the controller recover drain state after restart;
- help users debug why a pod has not been deleted yet;
- let future lifecycle controllers distinguish the post-drain target action without adding action fields to the `drain` API.

## Drain Target Action

The first version only uses drain-aware deletion, so `aibrix.ai/drain-target-action` should be set to `delete`.

The annotation intentionally keeps the CRD API small: `drain` describes the pre-action drain window, while the controller-owned annotation describes what happens after draining. This leaves room for a future sleep/warm-standby controller to reuse the same draining protocol by setting:

```yaml
aibrix.ai/drain-reason: "sleep"
aibrix.ai/drain-target-action: "sleep"
```

The gateway should treat all `aibrix.ai/draining=true` pods as unavailable for new requests, regardless of the target action.

## Gateway Behavior

The gateway/router should filter out pods with:

```yaml
aibrix.ai/draining: "true"
```

Pods with this annotation should not receive new requests.

The first version does not require the gateway to report active request counts or write back drain completion state.

## Implementation Scope

Drain-aware deletion must cover both deletion layers:

1. RoleSet controller / role syncers
   - For `podGroupSize <= 1`, RoleSet deletes Pods directly during scale-in and rollout.
   - These direct Pod deletions must patch drain annotations and wait for `drain.timeoutSeconds` before deleting the Pod.

2. PodSet path
   - For `podGroupSize > 1`, RoleSet deletes PodSet objects during scale-in and rollout.
   - PodSet controller owns the actual Pods and deletes them during finalization, recreate, unhealthy replacement, and scale-down.
   - The drain config from `RoleSpec` must be propagated to the generated PodSet, and PodSet controller must apply the same drain-before-delete behavior before deleting member Pods.

The user-facing API should remain `RoleSpec.drain`; PodSet can carry this as controller-owned internal state, such as a spec field or annotation, so direct users do not need to configure PodSet drain separately.

## Controller Behavior

When the RoleSet controller is about to delete a pod:

1. If the role does not configure `drain.timeoutSeconds`, delete the pod using the existing behavior.
2. If the pod does not have `aibrix.ai/draining=true`:
   - patch the draining annotations with `aibrix.ai/drain-target-action=delete`;
   - set `aibrix.ai/drain-start-time`;
   - do not delete the pod in the current reconcile;
   - requeue after the drain timeout.
3. If the pod is already draining:
   - read `aibrix.ai/drain-start-time`;
   - if the timeout has not expired, keep waiting;
   - if the timeout has expired, delete the pod.
4. If the annotation is missing or malformed, the controller should record an event and conservatively restart the drain flow or keep waiting.

## Non-goals

The first version does not implement:

- controller calls to sidecar or engine drain endpoints;
- controller calls to vLLM sleep/wake endpoints;
- controller polling of active streams or active prefill requests;
- gateway write-back of drain completion state;
- shared active request counters across gateway replicas;
- a `PodDrain` CRD;
- early deletion based on actual request completion.

The first version only provides a time-based drain window to reduce the chance of interrupting long-running requests during rollout or scale-in.

## Rollout / Scale-in Impact

Enabling this feature increases rollout and scale-in duration.

The additional duration is roughly:

```text
extra duration ~= number of drain batches * drain.timeoutSeconds
```

For example, if a decode role has 10 pods, `maxUnavailable=1`, and `drain.timeoutSeconds=60`:

```text
extra duration ~= 10 * 60s = 600s
```

Therefore, this feature should be disabled by default and enabled explicitly per role.

## Acceptance Criteria

- If `drain.timeoutSeconds` is not configured, RoleSet behavior remains unchanged.
- StormService users can enable this through `spec.template.spec.roles[].drain.timeoutSeconds`.
- RoleSet users can enable this through `spec.roles[].drain.timeoutSeconds`.
- During scale-in, pods selected for removal are marked as draining before deletion.
- During rollout, old pods are marked as draining before deletion.
- The gateway does not route new requests to draining pods.
- The controller can recover drain state from pod annotations after restart.
- Pods are deleted after the drain timeout expires.
- The controller emits clear events/logs for drain state transitions.


## 评论 (3)

### googs1025 · 2026-07-05

@Jeffwan I updated the proposal to keep `drain` as the generic pre-action drain window and use annotations to distinguish the post-drain target action:

```yaml
aibrix.ai/draining: "true"
aibrix.ai/drain-start-time: "..."
aibrix.ai/drain-reason: "scale-in|rollout|sleep"
aibrix.ai/drain-target-action: "delete|sleep"
```

For the first version, RoleSet would only set `drain-target-action=delete`. The `sleep` value is meant as a future extension point for the warm-standby / sleep-mode work, without adding an `action` field to the `drain` API.

Could you take a look and share whether this API boundary makes sense?

### googs1025 · 2026-07-15

cc @varungup90 @Jeffwan 

### googs1025 · 2026-08-12

cc @varungup90 /PTAL 

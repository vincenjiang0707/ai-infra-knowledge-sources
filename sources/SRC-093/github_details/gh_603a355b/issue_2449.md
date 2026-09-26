# [Issue #2449] Make StormService deployment mode explicit

source: https://github.com/vllm-project/aibrix/issues/2449
state: closed | updated: 2026-09-20T14:03:43Z
labels: help wanted, area/disaggregated

## 正文

## Problem

StormService currently has two deployment modes, but the mode is implicit:

- `spec.replicas > 1` means replica mode.
- `spec.replicas == 1` means pooled mode.

This makes the API hard to understand and easy to misuse because `spec.replicas` is doing two jobs at once:

1. It is the desired number of RoleSets.
2. It is also used as the deployment mode selector.

The ambiguity is especially visible when `spec.replicas == 1`. A user may intend either:

- pooled mode: one RoleSet with independently scalable roles, or
- replica mode with a single service replica.

The autoscaling path already exposes this ambiguity. `PodAutoscaler` uses the annotation `autoscaling.aibrix.ai/storm-service-mode` to decide whether role-level scaling should update `StormService.spec.replicas` or `StormService.spec.template.spec.roles[].replicas`. The code comment also notes that it is hard to know whether `replicas=1` means pool mode or replica mode.

## Why this matters

For users, the current API is too implicit:

- There is no obvious field showing whether a StormService is in pooled mode or replica mode.
- `replicas: 1` is overloaded and cannot distinguish pooled mode from single-replica replica mode.
- Autoscaling requires a separate annotation to recover the missing mode signal.
- Documentation explains the convention, but the resource itself does not encode the intent.

This can lead to surprising scaling behavior, especially for users who start with one replica and later add autoscaling or role-level scaling.

## Current examples

Replica mode:

```yaml
spec:
  replicas: 3
  updateStrategy:
    type: RollingUpdate
  template:
    spec:
      roles:
        - name: prefill
          replicas: 1
        - name: decode
          replicas: 1
```

Pooled mode:

```yaml
spec:
  replicas: 1
  updateStrategy:
    type: InPlaceUpdate
  template:
    spec:
      roles:
        - name: prefill
          replicas: 4
        - name: decode
          replicas: 8
```

Both are valid, but the mode is inferred rather than declared.

## Recommended implementation

Add an explicit deployment mode field to `StormServiceSpec`, for example:

```go
type StormServiceMode string

const (
    StormServiceReplicaMode StormServiceMode = "Replica"
    StormServicePooledMode  StormServiceMode = "Pooled"
)

type StormServiceSpec struct {
    Mode StormServiceMode `json:"mode,omitempty"`
    Replicas *int32 `json:"replicas,omitempty"`
    // ...
}
```

Suggested semantics:

- `mode: Replica`
  - `spec.replicas` means number of RoleSets.
  - `replicas: 1` is valid and means one replica-mode RoleSet.
  - Autoscaling the whole StormService updates `spec.replicas`.

- `mode: Pooled`
  - `spec.replicas` should be `1` or omitted/defaulted to `1`.
  - Each role is scaled through `spec.template.spec.roles[].replicas`.
  - Role-level autoscaling updates the selected role replicas.

## Backward compatibility

To avoid breaking existing users:

1. Keep `mode` optional initially.
2. If `mode` is omitted, preserve the current behavior:
   - `replicas > 1` => replica mode
   - `replicas == 1` or omitted => pooled mode
3. Add defaulting and status reporting so users can see the resolved mode.
4. Update documentation and samples to set `spec.mode` explicitly.
5. Eventually consider warning on omitted mode once the field is broadly adopted.

## Webhook validation

The webhook can make invalid combinations explicit:

- `mode: Pooled` with `spec.replicas > 1` should be rejected or normalized, depending on compatibility preference.
- `mode: Replica` should allow `spec.replicas >= 1`.
- Role-level autoscaling should require `mode: Pooled`, unless the intended behavior is clearly documented for replica mode.

## Autoscaler changes

After `spec.mode` exists, `PodAutoscaler` should read `StormService.spec.mode` instead of relying on:

```yaml
metadata:
  annotations:
    autoscaling.aibrix.ai/storm-service-mode: "pool"
```

The annotation can be kept temporarily as a compatibility fallback, but `spec.mode` should become the source of truth.

## Status and observability

Consider adding the resolved mode to status:

```yaml
status:
  mode: Pooled
```

This would make `kubectl get stormservice -o yaml` self-explanatory and help users/debuggers understand how the controller interpreted the resource.

## Tests

Suggested test coverage:

- API defaulting/resolution when `mode` is omitted.
- Validation for `mode: Pooled` with `replicas > 1`.
- `mode: Replica` with `replicas: 1` remains valid.
- Autoscaler updates `spec.replicas` for replica mode.
- Autoscaler updates `spec.template.spec.roles[].replicas` for pooled mode.
- Existing manifests without `mode` continue to behave as before.


## 评论 (6)

### V-3604 · 2026-07-14

I'll take this.

Plan (keeping the field optional and backward compatible):
- Add `Mode` (`Replica`/`Pooled`) to `StormServiceSpec`, default it in the mutating webhook from `replicas` when unset, reject `Pooled` with `replicas > 1`, and put the resolved mode in status.
- Regenerate the CRDs/applyconfiguration and update the autoscaling samples and design doc.

Autoscaler switch to `spec.mode` (annotation kept as fallback) I'd do as a follow-up so the first PR stays small. Mode is advisory here, so it won't change the controller's update-path selection.

One open point: nothing derives mode from `replicas` today, so I'll take the rule in the issue as the canonical one unless you'd rather key off `updateStrategy.type`.

### FAUST-BENCHOU · 2026-07-31

Any updates on this issue? Can I give it a try since it seems like there's been no update for a long time?

### googs1025 · 2026-08-25

Follow-ups after #2450:

- Decide how `spec.mode` should interact with `spec.updateStrategy.type`. Today the StormService controller still uses `updateStrategy.type` to choose the update path; either the controller should consume `spec.mode` / `ResolvedMode()`, or validation should prevent conflicting combinations.
- Move PodAutoscaler mode detection from `autoscaling.aibrix.ai/storm-service-mode` to `StormService.spec.mode`, with the annotation kept as a compatibility fallback during migration.
- Cover `/scale` subresource enforcement for `mode: Pooled` so `spec.replicas` cannot be scaled above 1 through `kubectl scale`, HPA, or external autoscalers.
- Keep docs/API comments explicit that `spec.mode` is advisory until controller/autoscaler logic is migrated.

### rishabhsinha17 · 2026-08-26

Taking the first two follow-ups from the last comment: making the StormService controller consume `spec.mode` / `ResolvedMode()` with validation for conflicting `spec.mode` vs `updateStrategy.type` combinations, and moving PodAutoscaler mode detection from the `autoscaling.aibrix.ai/storm-service-mode` annotation to `spec.mode` with the annotation kept as a compatibility fallback. Will reference this issue in the PR.

### roshpr · 2026-09-03

I'll take the leftover `/scale` subresource enforcement for `mode: Pooled` so `spec.replicas` cannot be scaled above 1 through `kubectl scale`, HPA, or external autoscalers.

#2450 and #2617 already covered the API field, controller path, and PodAutoscaler. This follow-up will add webhook/validation plus tests for the scale subresource, and I'll open the PR against this issue.

### googs1025 · 2026-09-20

all work complete
/close

# [Issue #2613] Proposal: PD-aware autoscaling for StormService roles

source: https://github.com/vllm-project/aibrix/issues/2613
state: open | updated: 2026-09-23T15:04:57Z
labels: area/autoscaling, kind/feature, area/disaggregated

## 正文

# Proposal: PD-aware autoscaling for StormService roles

## Summary

This issue proposes extending `PodAutoscaler` to support PD-aware autoscaling for
disaggregated inference workloads running on `StormService`.

Today, `PodAutoscaler` can scale either:

- a whole workload through `scaleTargetRef`, or
- one StormService role through `subTargetSelector.roleName`.

This works for single-target autoscaling, but it is not enough for
prefill/decode disaggregated serving. In PD disaggregation, prefill and decode
are separate serving pools with different pressure signals and scaling needs.
A single autoscaling decision often needs to adjust both roles together
while keeping a workload-specific prefill/decode ratio.

The goal is to support this without introducing a new CRD.

## Problem

PD-disaggregated inference has at least two independently scalable roles:

- `prefill`: usually sensitive to queue depth, prompt tokens, and TTFT.
- `decode`: usually sensitive to KV usage, decode backlog, and token latency.

With the current API, users need one `PodAutoscaler` per role:

```yaml
spec:
  scaleTargetRef:
    apiVersion: orchestration.aibrix.ai/v1alpha1
    kind: StormService
    name: llama
  subTargetSelector:
    roleName: prefill
  minReplicas: 1
  maxReplicas: 12
  metricsSources:
    - metricSourceType: pod
      targetMetric: prefill_queue_tokens
      targetValue: "10000"
```

This creates several problems:

- Each role is scaled independently, so the autoscalers do not know the desired
  relationship between prefill and decode capacity.
- It is difficult to express workload-specific ratio choices such as:
  - when prefill is under pressure, `prefill:decode = 2:1` is preferred;
  - when decode is under pressure, `prefill:decode = 1:2` is preferred.
- The current single-target status does not show why a PD profile was selected
  or how each role contributed to the final decision.
- StormService has both `spec.replicas` and role-level replicas, so the scaling
  target must be explicit to avoid confusing RoleSet-level scaling with
  role-pool scaling.

## Business Context

This proposal is important for current PD-disaggregated serving scenarios because `prefill` and `decode` are not two fully independent capacity pools. They are separate roles with different pressure signals, but the end-to-end service quality depends on keeping them balanced for the active traffic pattern.

If users configure one `PodAutoscaler` for `prefill` and another one for `decode`, each autoscaler can only react to its own metrics. The two autoscalers do not know the desired workload-specific relationship between the pools, such as `prefill:decode = 2:1` for long-prompt traffic or `prefill:decode = 1:2` for long-output or high-concurrency generation traffic. This can scale one side while simply moving the bottleneck to the other side.

For example, when `prefill` pressure is high, increasing only prefill replicas may improve prompt ingestion but still leave decode capacity or KV pressure as the next limiter. Conversely, when decode is under pressure, scaling only decode without preserving enough prefill capacity can hurt TTFT or leave the service shape mismatched with the workload.

A single multi-target `PodAutoscaler` lets the service owner treat a StormService PD deployment as one logical serving system while still scaling individual role pools. It can select a benchmark-derived profile based on the role that is currently under pressure, then apply coordinated desired replicas to both `prefill` and `decode`.

This is mainly useful for StormService-based PD deployments where operators already know several tested P/D shapes for their workload. It is less useful for ordinary single-pool model serving, where a single-target `PodAutoscaler` remains simpler and sufficient.

## Motivation

The desired prefill/decode shape is workload dependent. Long-prompt workloads
usually put more pressure on prefill, while long-output or high-concurrency
generation workloads usually put more pressure on decode. The right ratio also
depends on model size, tensor parallelism, KV cache capacity, latency SLOs, and
the observed input/output length distribution.

In practice, teams often benchmark several candidate shapes and keep the ones
that work well for their service. For example:

```text
When prefill pressure is high:
  prefill:decode = 2:1

When decode pressure is high:
  prefill:decode = 1:2
```

The autoscaling API should make this operational knowledge easy to express. It
should not require users to encode a dynamic ratio formula inside the CRD.

This proposal uses `profiles[]` for that reason: each profile is a tested
scaling shape, and `triggerTarget` describes which target's pressure should
activate that shape.

## Goals

- Keep using the existing `PodAutoscaler` CRD.
- Support one `PodAutoscaler` managing multiple StormService role targets.
- Allow each role target to keep its own metric source, min replicas, and max
  replicas.
- Allow users to define simple, tested scaling profiles for different role
  pressure scenarios.
- Keep the API generic enough to avoid PD-specific field names.
- Keep the status compatible with existing `PodAutoscalerStatus` fields.

## Non-goals

- Do not introduce a new autoscaling CRD.
- Do not add a generic resource budget field in the first version.
- Do not expose a user-written dynamic ratio formula.
- Do not make `StormService.spec.replicas > 1` part of role-pool autoscaling
  semantics.
- Do not expose low-level scheduler or hardware-specific details in the API.

## Proposed API

Add multi-target support to `PodAutoscalerSpec`:

```yaml
apiVersion: autoscaling.aibrix.ai/v1alpha1
kind: PodAutoscaler
metadata:
  name: llama-pd
spec:
  scaleTargetRef:
    apiVersion: orchestration.aibrix.ai/v1alpha1
    kind: StormService
    name: llama

  scalingStrategy: APA

  targets:
    - name: prefill
      subTargetSelector:
        roleName: prefill
      minReplicas: 4
      maxReplicas: 24
      metricsSources:
        - metricSourceType: pod
          protocolType: http
          port: "8000"
          path: /metrics
          targetMetric: prefill_queue_tokens
          targetValue: "10000"

    - name: decode
      subTargetSelector:
        roleName: decode
      minReplicas: 4
      maxReplicas: 48
      metricsSources:
        - metricSourceType: pod
          protocolType: http
          port: "8000"
          path: /metrics
          targetMetric: decode_kv_usage
          targetValue: "80"

  profiles:
    - name: prefill-heavy
      triggerTarget: prefill
      weights:
        prefill: 2
        decode: 1

    - name: decode-heavy
      triggerTarget: decode
      weights:
        prefill: 1
        decode: 2
```

### Field semantics

`targets[]` generalizes the existing single-target fields:

- `targets[].name` is the logical target name used by profiles and status.
- `targets[].subTargetSelector.roleName` selects the StormService role.
- `targets[].minReplicas` and `targets[].maxReplicas` bound that role.
- `targets[].metricsSources` define how pressure is observed for that role.

`profiles[]` defines simple scaling shapes:

- `profiles[].triggerTarget` references `targets[].name`.
- `profiles[].weights` maps target names to relative scaling weights.
- Weights are ratios, not absolute replica counts.

The concrete total desired replica count is still computed by the autoscaling
strategy. A profile only describes how that total should be shaped across
targets after a trigger target is selected.

For example:

```yaml
profiles:
  - name: prefill-heavy
    triggerTarget: prefill
    weights:
      prefill: 2
      decode: 1
```

This means: when the `prefill` target is the pressure trigger, shape the target
replicas toward `prefill:decode = 2:1`, while still respecting each target's
`minReplicas` and `maxReplicas`.

### Example decision flow

Start with a `StormService` that runs prefill and decode as role pools:

```yaml
apiVersion: orchestration.aibrix.ai/v1alpha1
kind: StormService
metadata:
  name: llama
spec:
  replicas: 1
  template:
    spec:
      roles:
        - name: prefill
          replicas: 4
        - name: decode
          replicas: 4
```

Because `spec.replicas` is `1`, each role's `replicas` represents the global
pool size:

```text
prefill pool = 4
decode pool  = 4
total        = 8
```

Then configure one `PodAutoscaler` for both roles:

```yaml
apiVersion: autoscaling.aibrix.ai/v1alpha1
kind: PodAutoscaler
metadata:
  name: llama-pd
spec:
  scaleTargetRef:
    apiVersion: orchestration.aibrix.ai/v1alpha1
    kind: StormService
    name: llama
  scalingStrategy: APA
  targets:
    - name: prefill
      subTargetSelector:
        roleName: prefill
      minReplicas: 4
      maxReplicas: 24
      metricsSources:
        - metricSourceType: pod
          targetMetric: prefill_queue_tokens
          targetValue: "10000"
    - name: decode
      subTargetSelector:
        roleName: decode
      minReplicas: 4
      maxReplicas: 48
      metricsSources:
        - metricSourceType: pod
          targetMetric: decode_kv_usage
          targetValue: "80"
  profiles:
    - name: prefill-heavy
      triggerTarget: prefill
      weights:
        prefill: 2
        decode: 1
    - name: decode-heavy
      triggerTarget: decode
      weights:
        prefill: 1
        decode: 2
```

#### Case 1: prefill target triggers scale up

If the prefill metric crosses its target first, the controller selects:

```yaml
activeProfile: prefill-heavy
triggerTarget: prefill
```

The selected shape is:

```text
prefill:decode = 2:1
```

If the scale-up algorithm decides the desired total size should be `12`, the
weighted split becomes:

```text
prefill = 8
decode  = 4
```

This shows that a profile is not an absolute replica assignment. It is a target
shape. The concrete `desiredReplicas` are still computed on each reconciliation
and must respect each target's bounds.

The status could look like:

```yaml
status:
  desiredScale: 12
  actualScale: 8
  activeProfile: prefill-heavy
  triggerTarget: prefill
  targets:
    - name: prefill
      currentReplicas: 4
      desiredReplicas: 8
      reason: MetricAboveTarget
    - name: decode
      currentReplicas: 4
      desiredReplicas: 4
      reason: ProfileRatio
  conditions:
    - type: ProfileSelected
      status: "True"
      reason: TriggerTargetMetricAboveTarget
      message: selected profile prefill-heavy because target prefill triggered scale up
```

In this example, `currentReplicas` still reflects the observed pool size before
the new target has fully taken effect. `desiredReplicas` is the computed target.
After the scale operation converges, prefill's `currentReplicas` should move
from `4` to `8`.

#### Case 2: decode target triggers scale up

If the decode metric crosses its target first, the controller selects:

```yaml
activeProfile: decode-heavy
triggerTarget: decode
```

The selected shape is:

```text
prefill:decode = 1:2
```

If the scale-up algorithm decides the desired total size should be `12`, the
weighted split becomes:

```text
prefill = 4
decode  = 8
```

The status could look like:

```yaml
status:
  desiredScale: 12
  actualScale: 8
  activeProfile: decode-heavy
  triggerTarget: decode
  targets:
    - name: prefill
      currentReplicas: 4
      desiredReplicas: 4
      reason: ProfileRatio
    - name: decode
      currentReplicas: 4
      desiredReplicas: 8
      reason: MetricAboveTarget
  conditions:
    - type: ProfileSelected
      status: "True"
      reason: TriggerTargetMetricAboveTarget
      message: selected profile decode-heavy because target decode triggered scale up
```

## StormService scaling semantics

For role-pool autoscaling, the target StormService should use one RoleSet:

```yaml
apiVersion: orchestration.aibrix.ai/v1alpha1
kind: StormService
metadata:
  name: llama
spec:
  replicas: 1
  template:
    spec:
      roles:
        - name: prefill
          replicas: 4
        - name: decode
          replicas: 4
```

In this mode, role replicas represent global pool size:

```text
prefill pool = spec.template.spec.roles[prefill].replicas
decode pool  = spec.template.spec.roles[decode].replicas
```

This proposal should not interpret `StormService.spec.replicas > 1` as
role-pool autoscaling, because then a desired role replica count becomes
ambiguous: it could mean either per-RoleSet replicas or global replicas.

## Status

Existing `PodAutoscalerStatus` fields should remain compatible:

```yaml
status:
  desiredScale: 12
  actualScale: 8
  lastScaleTime: ...
  conditions: ...
  scalingHistory: ...
  scheduledBounds: ...
```

In multi-target mode:

- `status.desiredScale` is the sum of `status.targets[].desiredReplicas`.
- `status.actualScale` is the sum of `status.targets[].currentReplicas`.
- existing conditions and scaling history remain available.

Add multi-target details:

```yaml
status:
  desiredScale: 12
  actualScale: 8

  activeProfile: prefill-heavy
  triggerTarget: prefill

  targets:
    - name: prefill
      roleName: prefill
      currentReplicas: 4
      desiredReplicas: 8
      reason: MetricAboveTarget

    - name: decode
      roleName: decode
      currentReplicas: 4
      desiredReplicas: 4
      reason: ProfileRatio

  conditions:
    - type: ProfileSelected
      status: "True"
      reason: TriggerTargetMetricAboveTarget
      message: selected profile prefill-heavy because target prefill triggered scale up

    - type: ScaleApplied
      status: "True"
      reason: StormServiceUpdated
      message: updated prefill and decode role replicas
```

This should allow users to answer:

- which profile is active;
- which target triggered that profile;
- what the desired and current replicas are for each role;
- whether the scale operation was applied successfully.

## Validation

When `spec.targets` is set:

- `scaleTargetRef.kind` must be `StormService`.
- the target StormService must have `spec.replicas == 1`.
- `targets[].name` must be unique.
- each target must set `subTargetSelector.roleName`.
- each selected role must exist in the StormService template.
- top-level `subTargetSelector`, `minReplicas`, `maxReplicas`, and
  `metricsSources` should not be used together with `targets[]`.
- `profiles[].name` must be unique.
- `profiles[].triggerTarget` must reference one of `targets[].name`.
- `profiles[].weights` keys must reference `targets[].name`.
- `profiles[].weights` values must be positive integers.

Note: the current `PodAutoscalerSpec.maxReplicas` field is required in the Go
API. Supporting this multi-target shape would require making the top-level
`maxReplicas` optional when `targets[]` is set, or adding equivalent conditional
validation in the CRD schema.

## Backward compatibility

Existing single-target `PodAutoscaler` resources should continue to work without
changes:

```yaml
spec:
  scaleTargetRef: ...
  subTargetSelector:
    roleName: decode
  minReplicas: 1
  maxReplicas: 96
  metricsSources: ...
```

The new behavior is only enabled when `spec.targets[]` is configured.

## Open questions

- How should the controller select `triggerTarget` when a target has multiple
  metrics?
- If multiple targets trigger at the same time, should the controller select the
  target with the strongest scale-up signal?
- If no target clearly triggers, should the controller keep the current profile
  and current replicas?
- Should `profiles[]` be required when `targets[]` is configured, or should
  targets be allowed to scale independently without profiles?
- Should each target be allowed to override `scalingStrategy`, or should the
  first version keep one top-level `spec.scalingStrategy`?
- How should existing `schedules[]` interact with `targets[]`? The first version
  may keep schedules only for single-target autoscaling.
- Should profiles be applied only to scale-up decisions, or also to scale-down
  decisions?

## Related reading

The following links are non-normative background references. They specifically
motivate why the desired prefill/decode ratio is workload dependent and why a
benchmark-derived profile is useful.

- [pd分离最佳配比实验方法](https://gogongxt.com/posts/1f902e41.html):
  describes a benchmark-driven method for measuring prefill and decode capacity
  separately, then deriving suitable P/D ratios from observed RPS, TTFT, TPOT,
  and KV cache limits.
- [AWS: Disaggregated prefill and decode on SageMaker HyperPod](https://aws.amazon.com/blogs/machine-learning/disaggregated-prefill-and-decode-for-llm-inference-on-sagemaker-hyperpod/):
  gives practical ratio guidance: start around 1:1 for balanced workloads and
  move toward 2:1 or 3:1 when prefill pressure dominates.



## 评论 (4)

### googs1025 · 2026-08-26

This is just an exploratory proposal, and it will be discussed later.

### googs1025 · 2026-09-01

After more discussion, I think we should tighten the API semantics before implementing this. The current `weights` wording can be misleading because users may expect a soft ratio, while the controller can easily produce confusing intermediate states such as `9P:4D` after rounding or per-target clamping.

My current preference is to model `profiles[]` as strict scalable shapes instead of weights:

```yaml
spec:
  targets:
    - name: prefill
      subTargetSelector:
        roleName: prefill
      minReplicas: 3
      maxReplicas: 30
      metricsSources:
        - metricSourceType: pod
          protocolType: http
          port: "8000"
          path: /metrics
          targetMetric: prefill_queue_tokens
          targetValue: "10000"

    - name: decode
      subTargetSelector:
        roleName: decode
      minReplicas: 1
      maxReplicas: 20
      metricsSources:
        - metricSourceType: pod
          protocolType: http
          port: "8000"
          path: /metrics
          targetMetric: decode_kv_usage
          targetValue: "80"

  profiles:
    - name: steady
      default: true
      shape:
        prefill: 3
        decode: 1

    - name: prefill-heavy
      triggerTarget: prefill
      shape:
        prefill: 4
        decode: 1

    - name: decode-heavy
      triggerTarget: decode
      shape:
        prefill: 1
        decode: 2
```

The key semantic difference is:

```text
profiles[].shape is not a final replica count and not a soft weight.
It is one scalable service unit.

For every reconcile, the controller selects exactly one activeProfile.
The final desired replicas must be an integer multiple of that profile's shape.
```

So the planner should use:

```text
desiredReplicas[target] = desiredUnits * activeProfile.shape[target]
```

This means min/max should be converted to unit-level bounds, not applied as per-target replica clamps:

```text
profileMinUnits = max(ceil(target.minReplicas / profile.shape[target]))
profileMaxUnits = min(floor(target.maxReplicas / profile.shape[target]))
desiredUnits    = clamp(rawUnits, profileMinUnits, profileMaxUnits)
desired[target] = desiredUnits * profile.shape[target]
```

If `profileMinUnits > profileMaxUnits`, the profile is invalid because its shape cannot satisfy the target min/max bounds while preserving strict shape.

### Default profile and initial ownership

I think multi-target mode should require exactly one `default: true` profile.

This answers the question of what happens when a StormService already has an initial role ratio, while the PodAutoscaler has its own default profile:

```text
Once the PodAutoscaler is created and owns these StormService roles,
the autoscaling policy comes from the PodAutoscaler spec.

The original StormService role replicas are only the current observed capacity.
They are not the long-term scaling policy anymore.
```

First reconcile should work like this:

```text
1. If a target already has scale-up pressure, select that target's trigger profile.
2. Otherwise select the default profile.
3. Use current StormService role replicas only to infer currentUnits, so the controller
   does not reduce capacity immediately on takeover.
```

For example, if StormService starts as `3P:1D` and the default profile is also `3P:1D`:

```text
currentUnits = max(ceil(3/3), ceil(1/1)) = 1
desired = 3P:1D
```

If StormService starts as `3P:1D` but the default profile is `2P:1D`:

```text
currentUnits = max(ceil(3/2), ceil(1/1)) = 2
desired = 4P:2D
```

So the PodAutoscaler default wins, but it normalizes using enough units to cover the current capacity. To avoid surprising rollout right after creation, we should recommend that `default.shape` matches the StormService's initial steady-state pool shape.

### Scale-up flow

For scale up:

```text
1. Compute pressure for each target: pressure = observedMetric / targetValue.
2. Compute rawDesiredReplicas per target.
3. Select the target with the highest scale-up pressure as triggerTarget.
4. Select the profile whose triggerTarget matches.
5. Compute rawUnits from the trigger target.
6. Clamp rawUnits using the selected profile's unit bounds.
7. Patch all StormService role replicas together.
```

Formula:

```text
rawUnits = ceil(rawDesiredReplicas[triggerTarget] / profile.shape[triggerTarget])
desiredUnits = clamp(rawUnits, profileMinUnits, profileMaxUnits)
desiredReplicas[target] = desiredUnits * profile.shape[target]
```

Example:

```text
rawDesiredReplicas[prefill] = 10
selected profile = prefill-heavy, shape = 4P:1D

rawUnits = ceil(10 / 4) = 3
desired = 12P:3D
```

For decode pressure:

```text
rawDesiredReplicas[decode] = 5
selected profile = decode-heavy, shape = 1P:2D

rawUnits = ceil(5 / 2) = 3
desired = 3P:6D
```

### Scale-down flow

Scale down should be conservative. A single low-pressure target should not shrink the whole PD service shape:

```text
Scale down only when all targets are scale-down eligible.
```

Suggested target eligibility:

```text
- all critical metrics are below scaleDownThresholdRatio * targetValue
- the low-pressure state lasts for scaleDownStabilizationWindow
- the target is not inside scale-up cooldown or panic window
```

During scale down, keep the current `activeProfile` and reduce units:

```text
currentUnits = max(ceil(currentReplicas[target] / activeProfile.shape[target]))
rawUnits = ceil(currentUnits / maxScaleDownRate)
desiredUnits = clamp(rawUnits, activeProfile.minUnits, activeProfile.maxUnits)
desiredReplicas[target] = desiredUnits * activeProfile.shape[target]
```

Only after the active profile has reached its minimum units, and all targets remain low, should the controller switch back to the default profile.

### Metric progression example

Assume:

```text
targets:
  prefill min=3 max=30 targetValue(prefill_queue_tokens)=10000
  decode  min=1 max=20 targetValue(decode_kv_usage)=80

profiles:
  steady default: 3P:1D
  prefill-heavy:  4P:1D
  decode-heavy:   1P:2D

scaleUpTolerance = 0.1
scaleDownThresholdRatio = 0.5
scaleDownStabilizationWindow = 5m
maxScaleDownRate = 2
```

| Time | Prefill pressure | Decode pressure | Decision | Active profile | Desired units | Desired replicas |
| --- | ---: | ---: | --- | --- | ---: | --- |
| t0 | 0.60 | 0.50 | no trigger, first reconcile uses default | steady | 1 | 3P:1D |
| t1 | 1.20 | 0.56 | prefill crosses 1.1 | prefill-heavy | ceil(5 / 4)=2 | 8P:2D |
| t2 | 2.50 | 0.75 | prefill pressure increases | prefill-heavy | ceil(12 / 4)=3 | 12P:3D |
| t3 | 0.90 | 1.19 | decode becomes the highest-pressure target | decode-heavy | ceil(5 / 2)=3 | 3P:6D |
| t4 | 0.80 | 1.63 | decode pressure increases | decode-heavy | ceil(10 / 2)=5 | 5P:10D |
| t5 | 0.30 | 0.90 | prefill is low, but decode is not low | decode-heavy | 5 | 5P:10D |
| t6 | 0.30 | 0.38 | all targets are low for 5m, scale down | decode-heavy | ceil(5 / 2)=3 | 3P:6D |
| t7 | 0.25 | 0.35 | still low and decode-heavy is at minUnits | steady | 1 | 3P:1D |

The important tradeoff is visible at `t3`: switching from `prefill-heavy` to `decode-heavy` may reduce prefill from 12 to 3. With strict shape, this is expected and intentional. The alternative is preserving extra non-trigger replicas, but then the API starts producing mixed shapes such as `12P:6D`, which is harder to explain.

Because of this, scale down and profile switches must be coordinated with workload drain:

```text
- PodAutoscaler computes desired shape and role replica counts.
- RoleSet/PodSet controllers should perform drain-aware deletion.
- Decode needs special care for active generation / KV state.
- Prefill should also avoid deleting pods with in-flight prefill work.
```

### Suggested implementation scope

I would split this into phases:

```text
Phase 1: API and validation
- add targets[] / profiles[]
- use shape instead of weights
- require exactly one default profile in multi-target mode
- validate shape keys and profile unit bounds
- keep legacy single-target mode compatible

Phase 2: planner algorithm
- compute per-target pressure and rawDesiredReplicas
- select triggerTarget by highest pressure
- select activeProfile
- use strict shape and unit-level clamp
- support default initialization and low-pressure return to default

Phase 3: controller integration
- patch multiple StormService role replicas together
- add multi-target status: activeProfile, triggerTarget, desiredUnits, per-target status
- add ownership/conflict detection for role targets

Phase 4: drain-aware scale down
- RoleSet controller should respect drain state
- PodSet controller should respect drain state
- PodAutoscaler should not directly decide which pod is safe to delete

Phase 5: tests and docs
- validation tests
- table-driven planner tests
- first reconcile/default profile tests
- scale-up profile selection tests
- all-targets-low scale-down tests
- strict shape tests to ensure no 9P:4D-like result
```

Overall, I think the cleaner v1 direction is:

```text
PodAutoscaler multi-target mode + targets[] + profiles[].shape + required default profile + strict unit-level planning.
```


### czczycz · 2026-09-07

I think the scale-up planner still needs an explicit rule for the case where multiple targets are simultaneously scale-up eligible. Selecting the target with the highest normalized pressure determines one active profile, but it does not necessarily satisfy the other overloaded target's raw replica requirement.
For example:
```
prefill-heavy shape = 4P:1D
decode-heavy  shape = 1P:2D

rawDesiredReplicas[prefill] = 12
rawDesiredReplicas[decode]  = 10
```
If decode has slightly higher pressure, the controller selects `decode-heavy`:
```
desiredUnits = ceil(10 / 2) = 5
desired       = 5P:10D
```
This satisfies decode, but prefill is still below its computed requirement of 12 replicas. Conversely, selecting prefill-heavy gives 12P:3D, which leaves decode below its requirement of 10.
One conservative option would be: after selecting the active profile, compute units against every scale-up-eligible target:
```
desiredUnits =
  max(ceil(rawDesiredReplicas[target] / activeProfile.shape[target]))
```
However, in order to reduce multiple pressures, resources may be wasted for a period of time, and the upper limit of some targets may also be broken.
The fundamental reason is that we can only choose one profile. In this case, we may have to spend a lot of effort to determine which shape is both effective and resource-efficient.

### bolubo · 2026-09-23

On the example from @czczycz and the open question about two targets triggering at once: under the updated `shape` semantics, neither trigger profile can cover that demand. `decode-heavy` (1P:2D) gives 5P:10D from the decode trigger, and even at its unit maximum of 10 (from prefill max 30 and decode max 20) it is 10P:20D, with prefill 2 short of `rawDesiredReplicas[prefill] = 12` and decode 10 over. `prefill-heavy` (4P:1D) needs 10 units to serve decode and caps at 7, 28P:7D. The only plan in the example that meets both is `steady` at its maximum, 10 units = 30P:10D, which is 18 replicas above what prefill needs.

The missing piece is not the max over targets; it is which target absorbs the miss and how that is reported. The max-units variant either breaks decode's max (12P:24D) or, after the unit clamp, leaves the same 2-replica prefill shortfall and adds 10 decode replicas beyond its requirement. One thing I would keep for a follow-up is switch stability: near-crossing pressures flip `activeProfile` between `prefill-heavy` (12P:3D at 3 units) and `decode-heavy` (5P:10D at 5 units) and reshape both roles, while the stabilization window applies to scale-down only. For the first version the choice is whether the planner stays on the trigger profile and reports the miss, or may pick a profile that meets every eligible target when one exists (`steady` at 10 units here). I would default to the first, with the miss visible as a condition or a per-target deficit next to `activeProfile`/`triggerTarget`. Which would you prefer for the first version?

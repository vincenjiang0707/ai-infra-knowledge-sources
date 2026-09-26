# [Issue #2620] Document StormService Volcano gang scheduling with minMember and minTaskMember

source: https://github.com/vllm-project/aibrix/issues/2620
state: closed | updated: 2026-09-06T22:38:16Z
labels: kind/documentation, help wanted

## 正文

## Summary

AIBrix already supports Volcano PodGroup gang scheduling through `StormService.spec.template.spec.schedulingStrategy.volcanoSchedulingStrategy`, but the current usage is not obvious from examples or documentation.

We should add documentation and examples showing how to configure gang scheduling from the StormService entry point.

## Motivation

StormService is the main user-facing entry for AIBrix orchestration. Users who want PD-disaggregated serving need to understand how to configure:

- group-level gang scheduling with `minMember`
- role-level pod minimums with Volcano `minTaskMember`
- the difference between RoleSet-level scheduling and per-role/PodSet scheduling

Without examples, users may assume AIBrix has no role-aware gang support, or may configure `RoleSet` directly instead of using `StormService`.

## Proposed Scope

Add StormService examples for:

### 1. Group-level gang scheduling

```yaml
apiVersion: orchestration.aibrix.ai/v1alpha1
kind: StormService
metadata:
  name: sglang-pd
spec:
  replicas: 1
  selector:
    matchLabels:
      app: sglang-pd
  template:
    metadata:
      labels:
        app: sglang-pd
    spec:
      schedulingStrategy:
        volcanoSchedulingStrategy:
          minMember: 6
          queue: default
      roles:
        - name: prefill
          replicas: 4
          template:
            spec:
              schedulerName: volcano
              containers:
                - name: prefill
                  image: example/sglang:latest
        - name: decode
          replicas: 6
          template:
            spec:
              schedulerName: volcano
              containers:
                - name: decode
                  image: example/sglang:latest
```

### 2. Role-level pod minimums with `minTaskMember`

```yaml
apiVersion: orchestration.aibrix.ai/v1alpha1
kind: StormService
metadata:
  name: sglang-pd
spec:
  replicas: 1
  selector:
    matchLabels:
      app: sglang-pd
  template:
    metadata:
      labels:
        app: sglang-pd
    spec:
      schedulingStrategy:
        volcanoSchedulingStrategy:
          minMember: 6
          minTaskMember:
            prefill: 4
            decode: 2
          queue: default
      roles:
        - name: prefill
          replicas: 4
          template:
            spec:
              schedulerName: volcano
              containers:
                - name: prefill
                  image: example/sglang:latest
        - name: decode
          replicas: 6
          template:
            spec:
              schedulerName: volcano
              containers:
                - name: decode
                  image: example/sglang:latest
```

## Notes

`minTaskMember` expresses minimum pod counts per Volcano task. It is useful for simple role-level pod minimums, but it is not the same as Volcano `subGroupPolicy`.

For multi-pod replicas, users must manually translate role replica counts into pod counts. For example, if each prefill replica has 2 pods and the desired minimum is 2 prefill replicas, then `minTaskMember.prefill` should be `4`.

## Non-goals

- Do not add a new API.
- Do not upgrade `volcano.sh/apis`.
- Do not change controller behavior.

## Acceptance Criteria

- Add documentation for StormService Volcano gang scheduling.
- Include examples for `minMember` and `minTaskMember`.
- Explain the limitation of `minTaskMember` versus `subGroupPolicy`.
- Clarify that users currently need to set `schedulerName: volcano` in pod templates.


## 评论 (1)

### yaojiejia · 2026-08-26

would love to take on this!

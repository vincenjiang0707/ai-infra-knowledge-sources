# [Issue #2619] Improve StormService Volcano gang usability with validation and schedulerName injection

source: https://github.com/vllm-project/aibrix/issues/2619
state: closed | updated: 2026-08-31T05:07:04Z
labels: help wanted, area/disaggregated, area/scheduling

## 正文

## Summary

Improve the usability and correctness of Volcano gang scheduling in StormService by adding validation for invalid gang configurations and automatically injecting `pod.spec.schedulerName` when Volcano gang scheduling is configured.

## Motivation

Today users configure Volcano gang scheduling through:

```yaml
spec:
  template:
    spec:
      schedulingStrategy:
        volcanoSchedulingStrategy:
          minMember: 6
          minTaskMember:
            prefill: 4
            decode: 2
```

However, there are two usability gaps:

1. Invalid configurations can be accepted, such as zero or negative `minTaskMember` values.
2. Users must manually set `schedulerName: volcano` in every role pod template, which is easy to forget.

This makes StormService gang scheduling harder to use and easier to misconfigure.

## Proposed Scope

### 1. Add validation for Volcano gang fields

Validate `StormService.spec.template.spec.schedulingStrategy.volcanoSchedulingStrategy` and the corresponding RoleSet fields.

Suggested validation rules:

- `minMember` must be greater than 0 when Volcano gang scheduling is configured.
- Every `minTaskMember` value must be greater than 0.
- Every `minTaskMember` key should match an existing role name.
- `RoleSet.spec.schedulingStrategy` and `RoleSpec.schedulingStrategy` should not be set at the same time, since the controller assumes they are mutually exclusive.
- If both `minMember` and `minTaskMember` are set, document or validate that `minMember` should not be smaller than the sum of `minTaskMember` values.

### 2. Automatically inject `schedulerName: volcano`

When a StormService/RoleSet uses:

```yaml
schedulingStrategy:
  volcanoSchedulingStrategy: {}
```

the controller should inject:

```yaml
spec:
  schedulerName: volcano
```

into generated Pods if the user did not explicitly set `schedulerName`.

Rules:

- Do not override a user-provided `schedulerName`.
- Apply to pods participating in the Volcano PodGroup.
- Keep existing behavior for Godel and scheduler-plugins unchanged unless explicitly handled in a follow-up issue.

## Example

User input:

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
      roles:
        - name: prefill
          replicas: 4
          template:
            spec:
              containers:
                - name: prefill
                  image: example/sglang:latest
        - name: decode
          replicas: 6
          template:
            spec:
              containers:
                - name: decode
                  image: example/sglang:latest
```

Generated pods should use:

```yaml
spec:
  schedulerName: volcano
```

unless the user already set a scheduler name.

## Non-goals

- Do not introduce a new scheduler-agnostic gang API.
- Do not implement Volcano `subGroupPolicy`.
- Do not change `minTaskMember` semantics.
- Do not upgrade `volcano.sh/apis`.

## Acceptance Criteria

- Invalid `minTaskMember` values are rejected.
- Unknown `minTaskMember` role names are rejected.
- Mixed RoleSet-level and Role-level scheduling strategies are rejected or clearly handled.
- Generated pods get `schedulerName: volcano` when Volcano gang scheduling is configured and `schedulerName` is empty.
- Existing user-provided `schedulerName` is preserved.
- Add unit tests for validation and schedulerName injection.


## 评论 (2)

### googs1025 · 2026-08-27

Proposed Scope 1 still open 

### yaojiejia · 2026-08-27

> Proposed Scope 1 still open

feel free to take a look https://github.com/vllm-project/aibrix/pull/2629

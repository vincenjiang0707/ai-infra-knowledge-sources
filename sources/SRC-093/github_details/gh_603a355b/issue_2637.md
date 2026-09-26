# [Issue #2637] Add missing integration/e2e test coverage for controllers and routing paths

source: https://github.com/vllm-project/aibrix/issues/2637
state: closed | updated: 2026-09-16T17:49:16Z
labels: good first issue, help wanted, area/gateway, kind/feature, area/testing, area/runtime, area/kv-cache, area/orchestration

## 正文

## Add missing integration/e2e test coverage

We should add focused integration/e2e tests for several controller and routing paths that are currently under-covered.

This issue can be used as a tracking issue. Please pick one unchecked item, comment before starting, and add yourself next to the task.

### Related

- Related RFC: #1430
- Related PR: #1491

### Test candidates

- [x] Add ModelRouter integration tests — assignee: @SarnadAbhilash 
  - Verify Deployment/ModelAdapter/RayClusterFleet informer events create `HTTPRoute`
  - Verify cross-namespace `ReferenceGrant` creation
  - Verify route/reference grant cleanup after workload deletion
  - Verify custom model router paths are appended correctly

- [x] Add KVCache controller integration tests — assignee: @weichenxu923 
  - Verify default backend behavior
  - Verify unsupported backend returns expected reconcile error
  - Verify owned Service/Deployment/StatefulSet resources are created with correct owner references
  - Verify Pod label events trigger reconciliation for the matching KVCache

- [x] Add RayClusterFleet integration tests — assignee: @yigitcan-ozturk 
  - Cover basic Fleet -> RayClusterReplicaSet reconciliation
  - Cover empty selector / SelectingAll behavior
  - Cover scale up/down status aggregation
  - Cover paused or rolling update behavior

- [x] Add ModelAdapter controller integration tests — assignee: @
  - Replace or complement the currently disabled controller-level Ginkgo suite
  - Verify Service/EndpointSlice lifecycle
  - Verify pod readiness/backoff affects status correctly
  - Verify retry annotations are set and cleared correctly

- [x] Add controller registration integration tests — assignee: @askarshabdanov1-collab
  - Verify `features.InitControllers("*")` + `SetupWithManager` starts successfully
  - Verify optional KubeRay CRD absence does not fail startup
  - Verify KubeRay controllers are registered when CRDs exist
  - Verify `NoKindMatchError` is skipped but other errors fail fast

- [ ] Add ModelRouter/Gateway e2e test — assignee: @
  - Deploy a model workload with routing metadata
  - Wait for `HTTPRoute` to be created/accepted
  - Send an OpenAI-compatible request through the gateway
  - Delete workload and verify route cleanup

### Suggested priority

1. ModelRouter integration tests
2. KVCache controller integration tests
3. RayClusterFleet integration tests
4. ModelAdapter controller integration tests
5. Controller registration integration tests
6. ModelRouter/Gateway e2e test

### Notes

Prefer integration tests first where possible because they are faster and more stable than full kind e2e tests. Add e2e only when the behavior depends on real Kubernetes/Gateway runtime behavior.

## 评论 (10)

### askarshabdanov1-collab · 2026-08-31

I'd like to take the **controller registration integration tests** item. I'll cover wildcard initialization/setup, KubeRay CRD absence/presence, and NoKindMatchError versus other setup errors.

### SarnadAbhilash · 2026-08-31

I'll take the **ModelRouter integration tests** item:

- Deployment/ModelAdapter/RayClusterFleet informer events create `HTTPRoute`
- Cross-namespace `ReferenceGrant` creation
- Route/reference grant cleanup after workload deletion
- Custom model router paths are appended correctly

Starting on this now.

### SarnadAbhilash · 2026-08-31

I'll take the **KVCache controller integration tests** item:

- Default backend behavior
- Unsupported backend returns the expected reconcile error
- Owned Service/Deployment/StatefulSet resources are created with correct owner references
- Pod label events trigger reconciliation for the matching KVCache

Starting on this now.

### SarnadAbhilash · 2026-08-31

I'll take the **RayClusterFleet integration tests** item:

- Basic Fleet -> RayClusterReplicaSet reconciliation
- Empty selector / SelectingAll behavior
- Scale up/down status aggregation
- Paused or rolling update behavior

Starting on this now.

### googs1025 · 2026-08-31

@SarnadAbhilash 
Please just take one task and leave the rest to others; this is very helpful for everyone to participate. 😄 
If you want, you can participate in other issues.

### SarnadAbhilash · 2026-08-31

Sorry about that, @googs1025 — I got ahead of myself. I'll stick to one item (the ModelRouter tests in #2640) and close #2641 and #2642 so the KVCache and RayClusterFleet tasks are free for others. Thanks for the reminder.

### weichenxu923 · 2026-09-01

I would like to work on the **KVCache controller** integration tests

- Verify default backend behavior
- Verify unsupported backend returns expected reconcile error
- Verify owned Service/Deployment/StatefulSet resources are created with correct owner references
- Verify Pod label events trigger reconciliation for the matching KVCache

### yigitcan-ozturk · 2026-09-02

I'd like to take the RayClusterFleet integration tests item. I'll keep the scope to the Fleet -> RayClusterReplicaSet reconciliation path, empty-selector/SelectingAll behavior, scale up/down status aggregation, and paused/rolling-update behavior, with focused integration coverage only.

### SarnadAbhilash · 2026-09-04

I'll take **only** the **ModelAdapter controller integration tests** item (one task):

- Replace or complement the currently disabled controller-level Ginkgo suite
- Verify Service/EndpointSlice lifecycle
- Verify pod readiness/backoff affects status correctly
- Verify retry annotations are set and cleared correctly

Leaving RayClusterFleet, Gateway e2e, and the other checkboxes for others.

### Zyh-one · 2026-09-04

Hi, I'd like to take Add ModelRouter/Gateway e2e test.
I plan to cover the flow described here: deploy a model workload with routing metadata, wait for the HTTPRoute to be accepted, send an OpenAI-compatible request through the gateway, and verify route cleanup after workload deletion.
Please assign this task to me if it's available. Thanks!

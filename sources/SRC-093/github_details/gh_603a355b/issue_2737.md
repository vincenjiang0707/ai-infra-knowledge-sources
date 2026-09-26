# [Issue #2737] [Testing] Expand integration and E2E coverage for core controller and gateway workflows

source: https://github.com/vllm-project/aibrix/issues/2737
state: closed | updated: 2026-09-20T04:29:59Z
labels: area/gateway, priority/important-longterm, triage/needs-information, kind/feature, area/testing, area/website, area/runtime, area/cicd, area/orchestration

## 正文

## Summary

Expand AIBrix integration and end-to-end test coverage for several core workflows that currently have partial coverage or are only exercised at a lower test layer:

- ModelClaim controller state transitions
- ModelRouter routing-resource lifecycle
- Metrics-driven gateway routing and fallback behavior
- PodSet lifecycle and draining
- RayClusterFleet and RayClusterReplicaSet lifecycle

This is a tracking issue. The checklist may be completed through multiple focused PRs, but all work remains tracked here.

## Motivation

Current test coverage is strong around ModelAdapter, StormService, RoleSet, PD disaggregation, and basic gateway routing. The areas below still lack either deterministic integration coverage or real-cluster validation.

The goal is to verify complete workflows across Kubernetes resources, controllers, Gateway API resources, routing state, and real requests—not simply add more isolated happy-path tests.

## Scope

### 1. ModelClaim controller integration coverage

Add an envtest-based integration suite under:

- `test/integration/controller/modelclaim_test.go`

Cover the following controller behavior:

- [ ] A newly created ModelClaim progresses through the expected initial status transitions.
- [ ] A ModelClaim with no matching warm pods reports `NoMatchingPods`.
- [ ] Reconciliation recovers when a matching pod becomes available.
- [ ] Invalid engine configuration produces the expected failed phase and condition.
- [ ] Runtime activation failure produces an observable condition/event and is retried according to controller policy.
- [ ] Runtime state is reflected as Activating, Active, Sleeping, and Failed.
- [ ] Deleting or losing an assigned pod causes the ModelClaim status to converge to the correct state.
- [ ] Reconciliation remains idempotent when the same ModelClaim is processed repeatedly.
- [ ] Multiple ModelClaims do not incorrectly overwrite each other's assignments or status.

Use a deterministic fake runtime endpoint instead of depending on an external inference engine.

### 2. ModelRouter end-to-end coverage

Add a live-cluster E2E package under:

- `test/e2e/controller/modelrouter/`

Validate the complete routing-resource lifecycle:

- [ ] Creating a supported model workload causes the expected HTTPRoute to be created.
- [ ] A workload outside `aibrix-system` causes the required ReferenceGrant to be created.
- [ ] The generated route points to the expected backend and model path.
- [ ] A request sent through the gateway reaches the expected model backend.
- [ ] Updating the workload or configured model paths updates the HTTPRoute.
- [ ] Deleting one workload preserves shared routing resources while another workload still requires them.
- [ ] Deleting the last workload removes the HTTPRoute and ReferenceGrant.
- [ ] Controller restart does not create duplicate routes or lose existing routing configuration.

At minimum, exercise Deployment and ModelAdapter discovery. RayClusterFleet may be covered when the Ray E2E fixture is available.

### 3. Metrics-driven gateway routing and fallback coverage

Extend:

- `test/e2e/gateway/routing/`

Add representative E2E coverage for routing strategies that currently rely mainly on unit tests:

- [ ] Verify least-request routing prefers the less-loaded ready replica.
- [ ] Verify one metrics-driven strategy, such as least-latency or least-busy-time, selects the expected replica.
- [ ] Verify missing or stale metrics trigger the documented fallback behavior.
- [ ] Verify a replica becoming unready is immediately excluded from routing candidates.
- [ ] Verify session affinity continues routing a session to the selected replica.
- [ ] Verify session affinity falls back safely when the selected replica disappears.
- [ ] Verify updating a ConfigProfile changes routing behavior without restarting the gateway.
- [ ] Verify a zero-weight strategy does not participate in routing.
- [ ] Verify temporary Redis/state-sync unavailability does not permanently break routing and that routing recovers after the dependency returns.

The tests do not need to cover every routing algorithm. Prefer a small set of deterministic scenarios that validate the shared metrics, state synchronization, candidate filtering, and fallback paths.

### 4. PodSet end-to-end coverage

Add a live-cluster E2E package under:

- `test/e2e/controller/podset/`

Cover:

- [ ] PodSet creation produces the expected pods and status.
- [ ] Scaling up creates the correct number of pods.
- [ ] Scaling down marks selected pods as draining before deletion.
- [ ] Restoring replicas before the drain timeout cancels the pending scale-down.
- [ ] Pods are deleted after the configured drain timeout.
- [ ] Pod failure or manual deletion is reconciled without producing duplicate pods.
- [ ] Deleting the PodSet cleans up owned resources.

Tests must observe controller state and Kubernetes resources rather than relying on fixed sleeps.

### 5. RayClusterFleet and RayClusterReplicaSet end-to-end coverage

Add a live-cluster E2E package under:

- `test/e2e/controller/raycluster/`

Cover the complete ownership chain:

```text
RayClusterFleet
  -> RayClusterReplicaSet
    -> RayCluster
```

Required scenarios:

- [x] Creating a RayClusterFleet creates an owned RayClusterReplicaSet.
- [x] The RayClusterReplicaSet creates the expected RayCluster resources.
- [ ] Scaling the Fleet propagates through the ownership chain.
- [ ] Replica and readiness status is aggregated back to the Fleet.
- [ ] A paused Fleet does not create or update child resources until resumed.
- [ ] Scale-down ordering is respected.
- [ ] Controller restart preserves the ownership chain and converges to the desired state.
- [ ] Deleting the Fleet cleans up owned ReplicaSets and RayClusters.

Use the existing KubeRay CRDs and test fixtures already loaded by the integration environment.

## Shared test requirements

All new tests must:

- [ ] Use isolated, uniquely named resources or namespaces.
- [ ] Use bounded contexts and explicit timeouts.
- [ ] Use polling/watch-based assertions rather than arbitrary sleeps.
- [ ] Clean up resources after success.
- [ ] Support preserving resources and diagnostics when an E2E test fails.
- [ ] Produce useful failure output, including relevant status conditions, events, and controller logs.
- [ ] Avoid requiring GPU hardware or downloading production model weights.
- [ ] Be deterministic when packages execute serially against the shared E2E cluster.
- [ ] Document any new E2E environment variables in `test/README.md`.

## CI integration

- [ ] ModelClaim tests run as part of `make test-integration-controller`.
- [ ] New controller E2E packages run under the `controller` and `all` suites.
- [ ] Gateway routing additions run under the `gateway` and `all` suites.
- [ ] Required CRDs, fixtures, and mock services are installed by the existing E2E runner.
- [ ] Required tests are not silently skipped in the CI job intended to cover them.
- [ ] Expensive or dependency-specific scenarios have a documented dedicated CI target when they cannot run in the default installation job.

## Suggested implementation order

1. ModelClaim integration tests
2. ModelRouter E2E
3. PodSet E2E
4. RayClusterFleet/ReplicaSet E2E
5. Metrics-driven gateway routing and fallback E2E
6. CI wiring and documentation review

Each section should be delivered as a focused PR and checked off in this issue.

## Validation

Relevant checks include:

```bash
make test-integration-controller
```

```bash
go test -p 1 ./test/e2e/controller/modelrouter/... -v -count=1
go test -p 1 ./test/e2e/controller/podset/... -v -count=1
go test -p 1 ./test/e2e/controller/raycluster/... -v -count=1
go test -p 1 ./test/e2e/gateway/routing/... -v -count=1
```

The complete cluster validation should also pass through:

```bash
KIND_E2E=true INSTALL_AIBRIX=true make test-e2e
```

## Non-goals

- Exhaustive E2E coverage for every gateway routing algorithm
- Performance, soak, or large-scale load testing
- Tests requiring GPU nodes or production-sized model artifacts
- Unrelated controller or gateway refactoring
- Changing public API behavior solely to simplify tests

If a test exposes a product defect, the fix may be submitted separately and linked from this issue.

## Definition of done

This issue is complete when:

- [ ] All five scope sections have landed.
- [ ] The tests run in an appropriate CI job rather than existing only as opt-in local tests.
- [ ] No required scenario is permanently skipped.
- [ ] New test configuration is documented.
- [ ] Integration and E2E jobs pass consistently without fixed-delay synchronization.


## 评论 (2)

### github-actions[bot] · 2026-09-16

<!-- aibrix-bot-needs-info -->
Please complete these required sections: `Proposed Change`.

### github-actions[bot] · 2026-09-16

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.


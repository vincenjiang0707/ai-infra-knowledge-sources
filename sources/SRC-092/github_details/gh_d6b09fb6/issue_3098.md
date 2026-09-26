# [Issue #3098] [RFC][Store] Scenario DSL and deterministic concurrency runner for MasterService tests

source: https://github.com/kvcache-ai/Mooncake/issues/3098
state: open | updated: 2026-09-22T15:19:00Z
labels: 

## 正文

## Summary

> [!IMPORTANT]
> This RFC and PR #3100 are an experimental prototype. The PR is provided primarily as a concrete, runnable artifact for design and code review; it is not a commitment to merge this implementation or to adopt the current DSL, checkpoint API, scheduler, file organization, or migration boundary as the final design. Any part of the approach may change substantially—or the proposal may be rejected—based on review feedback.

Introduce a typed, embedded C++ scenario DSL for `MasterService` tests and a deterministic concurrency runner based on test-only semantic checkpoints.

The goal is to move business-behavior coverage away from implementation-coupled fixtures while keeping stress, backend, protocol-compatibility, and low-level fault-injection tests as focused tests.

## Motivation

The existing `MasterService` test suites have accumulated several problems:

- large monolithic files make reviews expensive;
- setup, client UUID management, tenant policy files, and lifecycle cleanup are repeated;
- many tests describe implementation steps instead of business scenarios;
- concurrency tests rely on timing, sleeps, or mutex contention and are difficult to reproduce in CI;
- failures do not preserve the observed schedule or a reusable event trace.

A scenario DSL provides a stable vocabulary for public `MasterService` behavior. Semantic checkpoints provide deterministic control at the small number of concurrency boundaries where ordering is part of the contract.

## Goals

- Express `MasterService` business scenarios through its public C++ interfaces.
- Make success the default and require expected failures to be explicit.
- Support tenant, object, replica, quota, segment, copy/move, upsert, task, drain, lease, eviction, and offload scenarios.
- Distinguish order-independent `Parallel(...)` execution from explicit `Interleave(...)` choreography.
- Reproduce stale-writer and policy-deletion races without sleeps or scheduler luck.
- Capture a versioned JSON schedule and event trace on failure and replay it strictly.
- Compile all checkpoint infrastructure out of non-unit-test builds.
- Split the former monolithic suites by behavior area.

## Non-goals

- Random schedule exploration or state-space enumeration.
- A linearizability checker.
- Instruction-level race reproduction between semantic checkpoints.
- RPC or cross-process schedule replay in the first version.
- Replacing stress tests, allocator/backend tests, serialization compatibility tests, or performance tests with the DSL.
- Proving strict same-client/same-key ABA safety without an operation generation in the API.

## Proposed DSL

The embedded DSL declares service configuration, tenants, memory nodes, actors, actions, and assertions:

```cpp
MasterScenario("stale writer is rejected")
    .Given(MemoryNode("memory"))
    .When(PutStart("key", 1_KB).By("old-writer"))
    .Interleave({
        RunUntil("new-writer",
                 UpsertStart("key", 1_KB),
                 MasterTestCheckpoint::UPSERT_AFTER_PREEMPT),
        Start("old-writer",
              PutEnd("key").ExpectError(ErrorCode::ILLEGAL_CLIENT)),
        Resume("new-writer"),
        Join("new-writer"),
        Join("old-writer"),
    })
    .When(UpsertEnd("key").By("new-writer"))
    .Then(Object("key").IsReadable());
```

Normal actions require success. Failures must be declared with `ExpectError(...)`. Actors map to stable client UUIDs. The runner owns policy files, service lifetime, checkpoint sink, and actor threads through RAII.

The current vocabulary covers:

- put/upsert/copy/move/add-replica/remove flows;
- batch operations and replica clearing;
- tenants and quota snapshots;
- segment allocation, unmount, graceful drain, and client IP lookup;
- tasks, task payload assertions, and worker simulation;
- lease, soft-pin, hard-pin, grouped eviction, and offload behavior;
- synchronous and eventual object/job assertions.

## Deterministic concurrency

Under `BUILD_UNIT_TESTS`, `mooncake_store` exports `MOONCAKE_ENABLE_TEST_CHECKPOINTS`. Production builds contain no hook fields, branches, or checkpoint symbols.

The initial semantic checkpoints are:

- `UPSERT_AFTER_PREEMPT`: old processing metadata has been removed, but the new upsert has not returned;
- `ADD_REPLICA_AFTER_TENANT_VALIDATION`: tenant validation has completed while the policy mutex is still held, before publishing the replica.

`Reach(...)` is synchronous and may block. The runner arms only declared checkpoints, records operation begin/end and checkpoint arrival/release events, and cancels and wakes every actor on timeout or mismatch.

Checkpoint comments document held locks and valid choreography so tests do not accidentally wait while preserving an impossible lock dependency.

## Capture and replay

Every run records scenario/test identity, actor, operation, tenant/key/client, checkpoint occurrence, arrival/release order, and operation result.

A failure writes a versioned JSON artifact to `TEST_UNDECLARED_OUTPUTS_DIR`, or to a temporary fallback directory. It can be replayed with:

```bash
MOONCAKE_SCENARIO_REPLAY=/path/to/failure.schedule.json \
  ./master_scenario_test --gtest_filter='MasterScenarioTest.StaleWriter'
```

Replay strictly validates scenario, choreography, actor, checkpoint, occurrence, and release order. A changed scenario fails at the first mismatch instead of falling back to free scheduling.

## Test organization

The large `master_service_test.cpp` and `master_service_tenant_quota_test.cpp` files are replaced by scenario files grouped by behavior. The current migration contains 122 DSL business scenarios.

Focused suites remain for behavior that the DSL should not abstract:

- uncontrolled contention and stress workloads;
- Cachelib, offset allocator, NoF, and performance coverage;
- `WrappedMasterService` RPC boundary and metric behavior;
- legacy serialized payload compatibility;
- connector reload and quota coordination requiring private fault injection.

This boundary prevents the scenario DSL from becoming a second white-box `MasterService` API.

## Safety and production impact

- The checkpoint API and storage are guarded by `MOONCAKE_ENABLE_TEST_CHECKPOINTS`.
- The definition is public only for unit-test targets so the runner can implement the sink.
- Non-test builds are checked for checkpoint symbols.
- Checkpoint sinks are installed before actor startup and are not replaced during a schedule.
- All waits have bounded timeouts and cancellation wakes and joins all actors.

## Alternatives considered

### Continue using direct fixtures

This preserves flexibility but retains implementation coupling, repeated setup, and timing-dependent concurrency tests.

### Mock internal stores and mutexes

This makes specific interleavings possible but couples scenarios to private implementation and makes refactoring expensive.

### Randomized scheduling only

Useful as future stress coverage, but it does not provide a stable minimal reproduction and is difficult to review.

### RPC-first DSL

Closer to end-to-end behavior, but substantially increases runtime and does not solve in-process semantic scheduling. RPC and cross-process replay can be added later.

## Validation plan

- Build the scenario and legacy-compatible test targets with high parallelism.
- Run the complete `master_service_test`, `master_scenario_test`, and tenant quota suite.
- Repeat stale-writer deterministic schedules 100 times.
- Repeat new eviction and drain asynchronous scenarios.
- Inject a temporary failure, verify artifact capture, replay it after removing the failure, and verify mismatch behavior.
- Build with `BUILD_UNIT_TESTS=OFF` and confirm no checkpoint symbols are present.
- Run touched-file formatting, spelling, conflict, and whitespace checks.

## Rollout

Start with the two semantic checkpoints above and add new checkpoints only for concrete concurrency defects. Keep focused tests when their purpose is stress, backend integration, performance, compatibility, or private fault injection. Review future DSL additions against this boundary.

## 评论 (2)

### github-actions[bot] · 2026-07-24

Thanks for opening this issue, @Aionw!

| Field | Value |
|-------|-------|
| **Issue** | #3098 |
| **GitHub user ID** | `41376987` |
| **Reporter** | @Aionw |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### rishabhsinha17 · 2026-09-22

@ykwd Could we add a codeowner line for the MasterService scenario tests, with me as one of the contacts? I wrote the four migration PRs that moved those suites onto @Aionw's DSL (#3656, #3702, #3847, #3927), and the last two extended the DSL vocabulary itself. The tree changes every week now. #3805 and #4135 both touched `dsl/scenario.*` in the past ten days, and I want to keep reviewing such changes for consistency, as I did on #4127 before it merged. Something like the Store HA line from #3524, covering `mooncake-store/tests/master_service/` and the `*_scenario_test.cpp` suites, would be enough. If that works, I can send the PR with whatever contact list you prefer. Thanks.


# [Issue #2188] [Usage]: Mooncake HA: Primary-side OpLog writing not wired — by design or pending work?

source: https://github.com/kvcache-ai/Mooncake/issues/2188
state: closed | updated: 2026-09-22T03:15:28Z
labels: stale, auto-closed

## 正文

### Describe your usage question


With `enable_ha` enabled, the Leader Election and Standby OpLog replay pipeline are both implemented, but mutation RPCs (`PutEnd`, `Remove`, etc.) in `WrappedMasterService` delegate directly to `master_service_` without calling `OpLogManager::Append()` / `AppendAndPersist()`.

Specifically:

- `OpLogManager` is only instantiated in its own implementation and test files — `MasterService` / `WrappedMasterService` have no `oplog_manager_` member
- The only production usage of `enable_ha_` is in `ResolveSnapshotSequenceId()` (a read-only snapshot boundary query)
- Standby-side components (`HotStandbyService`, `OpLogApplier`, `OpLogReplicator`) are implemented but receive no entries since Primary never writes OpLog

This means after failover, a promoted Standby has empty or stale metadata and cannot serve traffic.

Is this intentional (e.g., currently validating election flow only), or is the integration still pending? If the latter, are there any plans or in-progress PRs for this?

### Before submitting a new issue...

- [ ] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)

## 评论 (4)

### 00fish0 · 2026-05-22

Thanks for the detailed analysis — your reading of the code is correct.

At the moment, enable_ha only provides high availability of the service itself. Metadata is not yet replicated or persisted through the OpLog pipeline, so although Leader Election and the Standby replay path are in place, the Primary never writes OpLog entries. As you noted, this means a promoted Standby starts with empty/stale metadata after a failover.

This is expected for the current state rather than a bug: the election flow landed first, and wiring the mutation RPCs (PutEnd, Remove, etc.) in WrappedMasterService into OpLogManager::Append() / AppendAndPersist() is still pending work. We're actively developing this integration to deliver true metadata high availability. We'll update this issue as that work progresses.

### silas-scitix · 2026-06-15

Thanks @00fish0 for confirming the current state. We've been validating Mooncake HA empirically on a multi-node cluster (real etcd + real workers, per-rank clients) and independently arrived at the same root cause — the Primary mutation path not writing OpLog — so it's great to hear the integration is actively in progress.

We read through the in-flight PR #2331, and it looks like a solid implementation of the producer side. One **design question about recovery** that we think matters a lot in practice, and that we're well-positioned to validate empirically:

**Reconnect timing vs. replica validity on promotion.** The key value of metadata HA is that on a *master* failover the workers stay alive and their KV data never moves — so ideally a promoted standby keeps serving the existing cache with no re-warm. In #2331, promotion appears to decide replica validity in one shot, based on which segments are connected *at promotion time*:

```cpp
// HandlePromotion(): built once, not refreshed as workers reconnect later
if (!segment_manager_.HasSegmentByEndpoint(seg.transport_endpoint))
    invalid_replica_endpoints_.insert(endpoint);
```

In a real failover, workers detect leadership loss and reconnect over a window of seconds, while promotion itself is fast. So at the moment `invalid_replica_endpoints_` is computed, many still-alive workers may not have reconnected yet — and their replicas would be treated as invalid (filtered, and in some paths persisted as stale-cleanup REMOVE) even though the data is intact on those workers. Since the set is only built at promotion and not refreshed on later re-mounts, those entries seem like they'd stay lost.

Two questions:
1. Is replica validity intended to be re-evaluated as workers re-mount *after* promotion (a reconnect grace window / lazy rebind), rather than fixed at promotion time? If not, would a grace window or rebind-on-remount be in scope?
2. After failover, is a retained replica's RDMA memory handle expected to be re-usable directly, or re-registered on worker reconnect? (The standby keepalive allocator appears to hold a placeholder buffer, so we weren't sure how the live handle is re-established on the new Primary.)

We're not asserting these are bugs — they're our reading of the code, and exactly the kind of thing that's hard to see without a real failover. We have a multi-node setup and would be happy to **empirically validate the end-to-end property** (write keys → kill the leader → confirm keys are still *gettable* on the promoted master, across different worker-reconnect timings) and report numbers here or on #2331. The existing HA unit tests drive the OpLog directly, which is great for the components but doesn't exercise this reconnect-timing path through the real MasterService — so this could be a useful complement. Happy to help however is most useful.


### github-actions[bot] · 2026-09-14

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.

### github-actions[bot] · 2026-09-22

Closing due to 3 months of inactivity. If this is still relevant, please comment and we can reopen.

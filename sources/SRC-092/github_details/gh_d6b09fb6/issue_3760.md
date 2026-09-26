# [Issue #3760] [Bug] HA standby promotion discards the whole index on one validation failure: "overlapping memory descriptors" -> keys 300 to 0 (v0.3.13)

source: https://github.com/kvcache-ai/Mooncake/issues/3760
state: open | updated: 2026-09-14T08:08:51Z
labels: 

## 正文

### Bug Report

On v0.3.13, promoting an HA standby that **has** the state loses the entire metadata index. The standby had applied every OpLog entry for the data in question, promotion itself succeeded, and then the restore validator rejected the whole `PromotionContext` on a single inconsistency check. The master came up serving with zero keys.

Reproduced **3/3** in one session, at `applied_seq_id` 1920, 2223 and 2526.

### Environment

- `docker.io/kvcacheai/mooncake:0.3.13`, master only (the store clients are the same image)
- Kubernetes, 2 master pods (1 primary + 1 standby), 3 store pods, RDMA
- 3 memory segments x 200 GiB, `replica_num=1`
- Master flags: `-enable_ha=true -ha_backend_type=etcd -ha_backend_connstring=<3-member etcd> -enable_oplog=true -allocation_strategy=free_ratio_first -enable_multi_tenants=true -eviction_high_watermark_ratio=0.90`; `enable_snapshot` and `enable_snapshot_restore` both off
- `-oplog_poll_interval_ms` and `-oplog_batch_max_entries` left at defaults

Note this release already contains #3354 and #3527 — in fact the error string below only exists because of #3354, which is direct evidence that fix is in the running binary.

### Repro

1. Bring up primary + standby with the flags above, wait for the standby to reach `WATCHING`.
2. Let the standby soak under traffic. In our case it had been up **nine minutes before the data was written**, so it watched all 300 puts as they happened.
3. Write 300 x 4 MiB objects. Confirm `master_key_count 300` on the primary and, on the standby, `ha_oplog_applied_sequence_id 1920`, `ha_oplog_applied_entries_total 1953`, `ha_oplog_standby_lag 0`.
4. Delete the primary pod so the standby is promoted.

### What happens

```
I hot_standby_service.cpp:560]        Promoting Standby to Primary. Applied seq_id: 1920, lag: 0 entries
I hot_standby_service.cpp:588]        Standby promoted to Primary successfully. All remaining OpLog entries have been synced.
E master_service.cpp:3198]            RestoreFromStandbySnapshot: overlapping memory descriptors
E master_service_supervisor.cpp:401]  Standby restore failed: INVALID_PARAMS
```

`master_key_count` goes **300 -> 0** and stays 0. All three store clients reattach and the full capacity comes back, so the buffers are simply unreachable and will be overwritten. Reads afterwards miss everything; a re-seed + verify returns 300/300, so the cluster is otherwise healthy.

### Two separate problems

**1. The validator is all-or-nothing, and the failure is unobservable.**

`master_service_supervisor.cpp` calls `RestoreFromStandby` and, on failure, only logs:

```cpp
if (!restore_result) {
    LOG(ERROR) << "Standby restore failed: " << toString(restore_result.error());
}
```

Execution continues and the new primary serves an empty index. `MasterService::RestoreFromStandbySnapshot` (`master_service.cpp:2990`) has roughly ten `return tl::make_unexpected(...)` branches — unknown endpoint, invalid descriptor, capacity overflow, duplicate object, overlapping ranges — and **any one of them discards every object in the context**, including the ones that validated cleanly.

For a KV cache this trade seems backwards: dropping the offending replica (or the offending segment's replicas) and restoring the rest would preserve almost all of the index, and prefix reuse degrades gracefully. Losing 100% of it to protect against one bad descriptor does not.

There is also **no metric** for this. `ha_oplog_standby_lag` read `0` throughout, which is honest — it means "not behind on the stream I am watching" and says nothing about whether the context will pass validation. Those two `E` lines are the only evidence that anything went wrong, so an operator watching dashboards sees a clean failover and a mysteriously cold cache. A counter such as `ha_standby_restore_failures_total` (ideally labelled by `ErrorCode`), plus the number of objects accepted vs rejected, would make this visible.

**2. Why is the overlap check firing at all?**

The check at `master_service.cpp:3193-3202` sorts the `(buffer_address_, size_)` pairs per segment and rejects if any two intervals overlap. `memory_ranges` is populated at `master_service.cpp:3139`, gated on `desc.status != REMOVED && desc.status != FAILED`.

Our hypothesis — offered as a hypothesis, we have not instrumented it — is that the standby's replayed view legitimately contains two live-looking replicas over the same address: the primary freed a buffer and reallocated it, and the standby's OpLog state at the promotion instant still carries the old replica in a non-`REMOVED`/`FAILED` status. Under a vLLM KV workload with eviction running (`eviction_high_watermark_ratio=0.90`), address reuse is constant, so this would be expected rather than exceptional.

If that is right, the invariant the check assumes does not hold on a live cache, and the check — not the state — is the bug. If it is wrong, we would appreciate knowing what is supposed to guarantee non-overlap, and we are happy to run instrumented builds to dump the offending pair.

### What we would like

1. Make the restore tolerant: skip the objects that fail validation and restore the rest, instead of returning `INVALID_PARAMS` for the whole context.
2. Log the offending descriptors (segment, addresses, sizes, both statuses) so this is diagnosable without a custom build.
3. Add a metric for standby restore failure and for objects accepted/rejected.
4. Clarify whether overlapping ranges are expected under eviction and address reuse.

### Notes

`ha_oplog_standby_lag = 0` is not a readiness signal for promotion. If a "this context will survive validation" signal is feasible, it would be far more useful than lag, since it is the thing that actually determines whether the cache survives a failover.


## 评论 (3)

### github-actions[bot] · 2026-08-28

Thanks for opening this issue, @gongwei-130!

| Field | Value |
|-------|-------|
| **Issue** | #3760 |
| **GitHub user ID** | `56567052` |
| **Reporter** | @gongwei-130 |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### he-yufeng · 2026-08-31

I am taking this one unless you are already on it, since it sits in the store code I have been working in.

On the mechanism: the all-or-nothing shape is exactly as you mapped it. Every one of the ~10 early returns in `RestoreFromStandbySnapshot` discards the entire context, and the overlap check at the end has no notion of which descriptor is at fault. I am restructuring it in three phases: cheap per-entry validation (each failure skips that entry with its key and reason logged, plus a `mooncake_ha_standby_restore_rejected_objects_total{reason}` counter), keep-latest overlap resolution, then construction for the survivors only. Segment-level structural corruption (empty name/endpoint, zero capacity) stays fail-fast, since that is a malformed context rather than one bad object.

On the winner semantics for an overlap: under eviction a freed buffer is reallocated, so the stale replica and the fresh replica coexist in the replayed state, and OpLog order is the freshness order. The later replay wins; the stale entry is dropped with both descriptors (segment, both address ranges, both keys) logged. That is the shape that preserves the most data while never serving the wrong bytes for a key. If maintainers would rather drop both sides of an overlap, that is a two-line change; I have flagged it in the PR for the call.

Tests cover: one invalid descriptor skips only that object, the overlap case keeps the later replay and drops the earlier one, and rejected counts land in the final log. Building now; PR follows with DCO.


### Icedcoco · 2026-09-14

Thanks for the detailed report. The all-or-nothing restore behavior is a real recovery problem, and #3806 is exploring how to isolate an invalid descriptor instead of discarding unrelated metadata.

However, an overlap itself is not expected during normal operation. Address reuse after eviction should not leave both the old and new descriptors live in the standby state: the old metadata update must become durable before the address can be reused, and ordered OpLog replay should remove or replace the old descriptor before installing the new one. Therefore, we should not treat overlaps as a normal consequence of eviction.

We also cannot safely resolve an overlap by keeping the entry encountered later. `StandbyMetadataStore::Snapshot()` exports objects from unordered maps, and the promotion context does not currently preserve enough per-descriptor ordering or allocation-generation information to determine which descriptor owns the bytes. Serving either descriptor could return another key's data.

To identify where the stale descriptor entered or remained in the OpLog state, could you provide the following from one reproduction?

1. The complete primary and standby logs from before the 300 puts until promotion, including `BatchEvict`, `PUT_END`, `REMOVE`, OpLog persistence/retry, segment mount/unmount, and client reconnect messages.
2. Whether memory usage actually crossed `eviction_high_watermark_ratio` during that reproduction, together with the relevant eviction counters.
3. Whether any store pod, segment, or RDMA endpoint restarted or re-registered before promotion.
4. If possible, the conflicting descriptor pair: tenant/key, `ReplicaID`, status, segment endpoint, address, and size, plus the OpLog entries for both keys.

The current v0.3.13 error only reports that an overlap exists, so an instrumented build may be necessary to obtain item 4. We can provide a small diagnostic patch if needed.

One additional clarification: periodic snapshots are not a reliable fallback for this case. They may be older than the affected writes, and normal snapshot restoration removes metadata that has expired by restore time. This report also has `enable_snapshot` and `enable_snapshot_restore` disabled, so the state rejected during promotion is the standby's in-memory state produced by OpLog replay, rather than a restored periodic snapshot.

For #3806, partial restore can reduce the blast radius, but it should be treated as recovery hardening rather than the root-cause fix. Any discarded conflict also needs a durable canonical `PUT_END` or `REMOVE` before serving; otherwise a later standby can replay the stale descriptor again after the address has been reused.

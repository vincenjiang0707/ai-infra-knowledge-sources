# [Issue #3819] [RFC]: [Store] Persist and Recover DFS Allocator Metadata

source: https://github.com/kvcache-ai/Mooncake/issues/3819
state: open | updated: 2026-09-23T09:54:51Z
labels: RFC

## 正文

### Changes proposed

Related: PR #2683: DFS replica support

## Summary

DFS replicas use Master-allocated ranges in shared shard files. `DfsGlobalAllocator` currently keeps allocation state only in memory, so a Master restart can reuse an extent that is still referenced by restored metadata.

This RFC persists allocator state using one checkpoint and one WAL per shard:

```text
dfs_shard_<index>.data  # object bytes
dfs_shard_<index>.meta  # allocator checkpoint
dfs_shard_<index>.wal   # allocator WAL
```

Recovery restores the allocator in sealed mode, reconciles it with a standalone Master snapshot, quarantines unreferenced extents, and only then resumes service.

This RFC covers single-Master restart recovery. HA, OpLog recovery, Standby promotion, data-file durability, write-attempt identity, and batch WAL coalescing remain out of scope.

## Core invariants

1. The allocator is authoritative for physical ownership and safe reuse.
2. The Master snapshot is authoritative for object visibility.
3. An allocation must be durable before its descriptor is exposed.
4. A release must be durable before its extent becomes reusable.
5. Recovery may delay reuse, but must never shorten a safety window to reclaim capacity.
6. Corrupt or structurally inconsistent metadata fails closed.

## Persistent allocation identity

Each allocation receives a persistent `allocation_id` stored in:

- the allocator checkpoint and WAL;
- the corresponding DFS replica metadata in the Master snapshot.

Reconciliation compares this identity in addition to key, shard, path, offset, and size. This prevents an ABA case where an old snapshot accidentally matches a later allocation that reused the same extent.

The `allocation_id` identifies physical DFS extent ownership. It is not a write-attempt token, and clients are not required to return it through `PutEnd` or `PutRevoke`.

When included in an RPC-visible DFS descriptor, `allocation_id` must use a forward- and backward-compatible wire representation, such as a versioned `struct_pack::compatible` field. Existing RPC method signatures must not be changed by this RFC.

## Checkpoint and WAL

The checkpoint contains:

- format version, generation, base WAL sequence, and checksum;
- serialized allocator state;
- active allocations and their allocation IDs;
- pending frees and their lifecycle state.

The WAL contains checksummed, sequential records:

- `ALLOC`: persistent allocation identity and complete reservation information;
- `RELEASE`: allocations that may be retired.

Allocation ordering:

```text
reserve -> append ALLOC -> fsync -> expose descriptor
```

Release ordering:

```text
defer/quarantine -> append RELEASE -> fsync -> reuse extent
```

A torn terminal frame is discarded. Interior corruption, sequence gaps, invalid transitions, or ambiguous persistence failures poison the shard and fail closed.

Checkpoint replacement uses file `fsync`, atomic rename, and parent-directory `fsync`.

## PUT-path performance

`fsync` remains on the critical path because exposing a non-durable allocation would reintroduce restart overlap.

This RFC preserves the existing per-key `PutStart` allocation flow. Each DFS allocation appends and synchronizes its own `ALLOC` record before returning its descriptor. `BatchPutStart` continues to process allocation results per key and does not introduce a new Master-side batch allocation path.

Grouping multiple `ALLOC` records by shard and performing one `fsync` per touched shard is a potential follow-up optimization. It should be designed separately so that batching does not require passing DFS-specific preallocated descriptors through the generic single-key replica allocation APIs.

A follow-up proposal should define:

- batch preparation and commit ownership;
- rollback of partially prepared allocations;
- per-key error semantics;
- interaction with Memory and NoF replica allocation;
- behavior across multiple shards;
- checkpoint and concurrent allocation locking;
- representative POSIX and HF3FS performance measurements.

Removing the durability wait entirely requires a different protocol, such as allocation from pre-durable reservations, and is also left for future work.

Production enablement requires representative measurements for PUT p99 latency, checkpoint pauses, WAL growth, and recovery time.

## Recovery framework

Recovery follows a reusable state machine:

```text
recover persistent state
  -> enter sealed mode
  -> restore reference state
  -> validate and build reconciliation plan
  -> apply reconciliation and quarantine rules
  -> open recovery barrier
  -> resume service
```

Reconciliation is applied transactionally: a snapshot candidate is fully validated before it changes allocator or object state.

DFS provides the first reconciliation strategy. Future recovery mechanisms may reuse the same barrier and validation framework.

## Snapshot reconciliation

A DFS replica is retained only when its key, path, shard, offset, sizes, and `allocation_id` match an active allocator record.

Recovery handles mismatches as follows:

- prune descriptors whose mismatch can be explained by snapshot staleness;
- remove objects left without a valid replica;
- quarantine active allocator records absent from the snapshot;
- fail closed on invalid extent metadata, conflicting ownership, overlap, or other structural inconsistencies.

This ensures recovery never exposes a descriptor whose current physical ownership cannot be proven.

## Quarantine

Recovery distinguishes two cases:

### 1. Active allocator-only orphan

The descriptor may still be held by a pre-crash writer. Its quarantine covers:

```text
max(deferred_free_duration, read_lease, put_start_release_timeout)
```

### 2. Recovered pending-free extent

The extent was already logically released before the crash. It requires only the remaining deferred-free and read protection.

Persisted lifecycle information may be used to recover the remaining grace period when a restart-safe deadline is available. Otherwise, recovery starts a fresh conservative interval from `barrier_open`.

With the current defaults, the active-orphan bound is 600 seconds because `put_start_release_timeout` is the maximum.

## RPC compatibility and non-goals

This RFC does not introduce `put_attempt_id` and does not change the existing `PutStart`, `PutEnd`, `PutRevoke`, Upsert, or batch RPC method signatures.

A delayed `PutEnd` or `PutRevoke` from an older write attempt may still race with a newer write attempt for the same client and key. This behavior is not specific to DFS and already applies across storage backends.

Write-attempt identity should be addressed separately with a backend-independent design. That work must define:

- consistent semantics for Memory, NoF, DISK, LOCAL_DISK, and DFS replicas;
- rolling-upgrade behavior between old and new clients and Masters;
- versioned or backward-compatible RPC messages;
- handling of clients that do not support write-attempt tokens;
- retry, timeout, revoke, and batch-operation semantics.

Deferring write-attempt identity does not weaken the restart-safety property provided by `allocation_id`. The two identities solve different problems:

- `allocation_id` proves current ownership of a persistent DFS extent;
- a future write-attempt identity would distinguish successive write transactions for the same client and key.

The following are also out of scope:

- changing the existing `BatchPutStart` execution model;
- grouping WAL records across keys;
- cross-key or cross-shard transaction atomicity;
- pre-durable allocation reservations;
- HA, OpLog recovery, and Standby promotion;
- durability of object data stored in the DFS shard files.

## Configuration

- `MOONCAKE_DFS_METADATA_CHECKPOINT_INTERVAL_SECONDS` (default: `300`) controls periodic checkpoint creation.
- `MOONCAKE_DFS_METADATA_WAL_COMPACTION_THRESHOLD_BYTES` (default: `67108864`) is the WAL size threshold that triggers checkpoint/compaction maintenance.

The WAL compaction threshold is deliberately named a threshold rather than a maximum. An appended frame may temporarily grow the WAL beyond this value before compaction completes, so operators must not interpret it as a hard WAL size limit.

## 评论 (8)

### github-actions[bot] · 2026-09-01

Thanks for opening this issue, @fcczzz!

| Field | Value |
|-------|-------|
| **Issue** | #3819 |
| **GitHub user ID** | `93508110` |
| **Reporter** | @fcczzz |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### Yong-ee · 2026-09-17

I think this RFC is very well designed and addresses exactly the problem I am concerned about. After going through the design, I have a few questions and one suggestion.

### Questions

**1. Allocation latency and PUT performance**

The RFC requires a new DFS allocation to be appended to the WAL and `fsync`'d before the allocation descriptor is returned.

Since this is on the critical path of DFS PUT, could this have a significant impact on PUT latency, especially under high-concurrency workloads? If multiple allocations share the same WAL, could the append + `fsync` also become a serialization bottleneck?

Would it be possible to consider group commit or batching multiple `ALLOC` records into a single `fsync`, while still preserving the required durability guarantee?

**2. Snapshot contains a descriptor, but the allocator does not**

Could recovery result in a state where the Master snapshot contains a DFS descriptor, but the recovered allocator does not contain the corresponding allocation?

The RFC proposes pruning such a DFS replica because its physical ownership cannot be proven. Could you clarify what scenarios can lead to this state, and whether pruning is always safe?

**3. Allocation is durable, but `PutEnd` does not complete**

Suppose an allocation has already been persisted to the WAL and the allocation descriptor has been returned, but the subsequent `WriteAt` or `PutEnd` fails, or the Master crashes before `PutEnd` completes.

In this case, the allocator would contain the allocation, while the Master snapshot would not contain the corresponding key. My understanding is that this allocation would be treated as an allocator-only orphan, given a fresh defer interval, and eventually released.

Could you clarify the expected lifecycle of such orphan allocations, and how the defer interval is chosen to avoid prematurely releasing an allocation when the snapshot may simply be lagging behind the allocator state?

### Suggestion: Abstract the recovery/reconciliation framework

One additional suggestion is to consider making the recovery flow an abstract/reusable framework rather than tying it too closely to the current DFS recovery algorithm.

For example, the overall flow could be modeled as:

```text
Recover persistent state
        ↓
Enter sealed/recovery mode
        ↓
Restore external/reference state
        ↓
Reconcile recovered state
        ↓
Apply recovery-specific rules
        ↓
Open the recovery barrier
        ↓
Resume normal operation
```

The current DFS implementation could then provide one concrete reconciliation strategy, while other recovery mechanisms could implement their own algorithms on top of the same framework.

This could make the recovery barrier, state validation, quarantine/orphan handling, and transition back to serving state reusable for future recovery mechanisms such as OpLog recovery, HA, or Standby promotion.

I think this would make the design more extensible while keeping the current DFS-specific recovery logic isolated.


### fcczzz · 2026-09-17

Thanks @Yong-ee — good pushback.

**1. Allocation latency / group commit.**
Agreed. A simpler first step is batch commit: `BatchPutStart` already has N keys, but today effectively pays one WAL append + `fsync` per allocation. We can reserve the batch, append the existing per-allocation frames grouped by shard, and `fsync` once per touched shard. No WAL format change, no locks held across `fsync`, and no cross-shard atomicity is required because results are already per key. General group commit can remain a follow-up.

**2. Snapshot has a descriptor the allocator doesn't.**
This can happen from snapshot staleness, not necessarily a lost `ALLOC`: the key may have been released after the snapshot and the extent reused. I’d distinguish:
* prune mismatches explainable by staleness: no owner / different owner / key mismatch;
* fail closed on structural inconsistencies that staleness cannot explain, such as invalid extent metadata or conflicting ownership of the same `(shard, offset)`.

The allocator remains authoritative for physical ownership; the snapshot is only for visibility.

**3. Durable allocation, but no completed `PutEnd`.**
That is an orphan. Its extent should only become reusable after `RELEASE` is durable, and the quarantine must cover all pre-crash holders:
`free_at = barrier_open + max(deferred_free_duration, read_lease, put_start_release_timeout)`
With current defaults, that is 600s. Starting from `barrier_open` avoids deducting recovery time.

**Recovery framework.**
Agreed on the sequence:
`recover sealed -> restore snapshot -> reconcile -> quarantine orphans -> open barrier`
I’ll make the sealed/barrier state machine, validation hook, fail-closed cases, and orphan quarantine explicit, with the DFS rules as the first strategy.


### Yong-ee · 2026-09-18

Thanks for the detailed explanations. That clarifies the design and the recovery semantics quite a lot. I generally agree with the direction, and I have a few follow-up thoughts:

### 1. Allocation latency / I/O on the PUT path

If possible, I would prefer to avoid performing disk I/O directly on the PUT path, because even a single `fsync` can introduce non-negligible and potentially variable latency.

In the inference framework, the PUT path is part of the critical path for inference, so additional storage latency can propagate directly to end-to-end inference latency. From that perspective, I am still a little concerned that even one `fsync` per touched shard could have a noticeable impact on the latency tail.

That said, I don't have a better solution for this yet. It may require rethinking how extent allocation and metadata persistence are decoupled, or potentially adjusting the allocation strategy so that allocation can be persisted without blocking the PUT critical path.

The proposed batch commit seems like a good first step, though, since it can significantly reduce the number of `fsync`s without changing the WAL format.

### 2. Snapshot vs. allocator authority

I agree with this rule, and I think it should be explicitly stated as one of the core invariants of the recovery design:

> **The allocator remains authoritative for physical ownership; the snapshot is only for visibility.**

This separation makes the recovery semantics much clearer and helps avoid treating a stale snapshot as authoritative for extent reuse.

I also agree that the recovery logic should distinguish between inconsistencies that can be explained by snapshot staleness and structural inconsistencies that should cause recovery to fail closed.

### 3. Orphan quarantine duration

Regarding the proposed 600-second quarantine period: could this be too long in practice?

During the quarantine period, the extent cannot be released and reused by other objects. If there are many orphan allocations, or if the system is under high memory/cache pressure, holding these extents for up to 600 seconds could temporarily reduce the available DFS capacity.

Could this potentially cause hot data to be evicted earlier because the allocator has less reusable space available?

It would be useful to understand how the 600-second value was derived and whether the quarantine duration could be adaptive based on the actual `read_lease`, `put_start_release_timeout`, and recovery state, rather than relying on a relatively large fixed upper bound.


### fcczzz · 2026-09-20

Thanks @Yong-ee  — I agree. I’ll tighten the RFC around these points:

1. **PUT latency:** Batch commit is only the first optimization; `fsync` remains on the critical path because an allocation must be durable before its descriptor is exposed. Removing that wait would require a different protocol, such as allocating from pre-durable reservations.

2. **Recovery authority:** The allocator is authoritative for physical ownership and reuse, while the snapshot is authoritative for object visibility. Reconciliation also needs a persistent allocation generation to prevent ABA cases. Separately, a Put attempt ID should protect `PutEnd`/`PutRevoke` from delayed requests.

3. **Quarantine:** The current 600s comes from:
   `max(deferred_free_duration, read_lease, put_start_release_timeout)`

   This is a conservative lifecycle bound, not true write fencing. Phase 2 therefore needs an explicit assumption that pre-crash clients stop writing within that bound. Arbitrarily delayed writers would require data-plane fencing.

4. **Adaptive duration:** We can recover the remaining grace period from persisted lifecycle information and distinguish active orphans from already pending-free extents. Capacity pressure must not shorten the safety window: quarantined bytes reduce allocatable capacity and may cause PUT rejection, but should not trigger eviction of valid hot objects.

I’ll incorporate these points into the RFC before finalizing the implementation.

### wp-bc · 2026-09-21

This RFC provides a clear recovery model for the shard allocator. We are developing an immutable bucket allocator for DFS replicas, which makes a different tradeoff between durability and performance. I would like to briefly introduce our design and discuss how recovery responsibilities should be divided between the allocator and the Master.

## Bucket Persistence Model

Each fixed-size, append-only bucket has two files:

```text
bucket_<id>.data
bucket_<id>.meta
```

The metadata contains:

- bucket capacity, alignment, and append offset;
- key, offset, object size, reserved size, and generation;
- entry state: `PENDING`, `COMMITTED`, or `TOMBSTONE`;
- an eviction marker and checksum.

The write flow is:

```text
allocate space in the active bucket
    -> create a PENDING entry
    -> return the DFS descriptor
    -> client writes the object data
    -> PutEnd
    -> mark the entry as COMMITTED
```

The active bucket keeps its metadata in memory. When it becomes full, it is sealed, and its complete metadata snapshot is written and fsynced.

Changes to a sealed bucket, such as transitions to `COMMITTED` or `TOMBSTONE`, mark its metadata as dirty. A maintenance task later rewrites and fsyncs the metadata. This avoids performing DFS metadata I/O while the Master holds an object metadata shard lock.

## Performance and Durability Tradeoff

We deliberately do not append a WAL record and call `fsync` for every allocation before returning its descriptor.If the Master crashes or restarts before the active bucket is sealed, that bucket has no persistent metadata and cannot be safely reconstructed. Recovery therefore deletes the active bucket, which may result in the loss of recently written objects stored in it.

This is an intentional tradeoff. We treat an unexpected Master restart as an exceptional event, while PUT is continuously exercised on the inference critical path. Under high concurrency, appending to the WAL and calling `fsync` for every allocation may introduce serialization, variable storage latency, and worse PUT tail latency, potentially affecting inference performance.

Because these DFS objects are cache data and can usually be recomputed, our current design prefers bounded data loss during an exceptional restart over adding synchronous metadata I/O to every normal PUT.The loss is limited to the current unsealed active bucket. Previously sealed buckets remain recoverable from their metadata.If stronger durability is required in the future, possible options include sealing the active bucket during a planned shutdown, using smaller buckets, pre-persisting bucket reservations, or using batched/group metadata commits. We would prefer not to require one `fsync` per allocation on the inference critical path.

## Restart Recovery

At startup, the allocator scans the bucket files and validates the metadata version, checksum, layout, data-file existence, and entry ranges.

The main recovery rules are:

- `COMMITTED` entry → recover;
- `PENDING`/`TOMBSTONE` entry → do not recover;
- invalid metadata → discard the bucket;
- data without metadata → discard it as an unsealed bucket;
- bucket being evicted → complete the interrupted deletion.

Duplicate keys are resolved deterministically using the following tuple:

```text
(generation, bucket_id, entry_offset)
```

Recovered buckets remain sealed, and new writes use a new bucket.

## Core Difference from This RFC

Our current bucket allocator recovers valid `COMMITTED` entries from `bucket_<id>.meta` during startup and returns the corresponding `(key, descriptor)` pairs to the Master. The Master then reconstructs minimal `ObjectMetadata` containing only a DFS replica, making the objects queryable again.Therefore, bucket metadata serves as both the source of truth for physical space ownership and the source of truth for DFS object visibility.

In contrast, this RFC separates these responsibilities: allocator metadata only proves physical space ownership, while the Master snapshot restores objects and their visibility. During restart, the two states are validated against each other, and only DFS replicas that exist on both sides and whose descriptors match exactly are retained.

Our approach does not depend on a Master snapshot and does not require synchronous persistence of allocator metadata for every allocation, thereby reducing metadata I/O on the PUT path. The tradeoff is that it can only reconstruct minimal DFS-only objects and cannot fully restore the original UUID, other replica types, pinning state, lifecycle information, or tenant and accounting information that may be added in the future.

## Question

For the bucket allocator, which model do you think is preferable?

### A. Bucket-Driven Recovery

Use committed bucket entries to reconstruct minimal DFS-only Master objects. This supports recovery without a Master snapshot, but creates a second source of truth for object visibility.

### B. Snapshot Reconciliation

The bucket allocator restores physical state in sealed mode, while the Master snapshot restores visibility. Both sides are reconciled according to this RFC before the recovery barrier is opened.

### C. Two Explicit Modes

When a valid snapshot exists, use snapshot reconciliation. When no snapshot exists, optionally allow best-effort DFS-only recovery from bucket metadata.

Our current view is that the allocator should always be responsible for physical layout, safe reuse, and descriptor validation. The main question is whether a committed bucket entry alone should be allowed to reconstruct a visible Master object.

We would greatly appreciate your opinion on this responsibility boundary and on whether accepting the loss of the active bucket to avoid an `fsync` for every allocation is a reasonable tradeoff.

### fcczzz · 2026-09-22

Thanks @wp-bc for explaining the design. I think accepting the loss of the active bucket is a reasonable tradeoff for recomputable cache data, especially if it avoids synchronous metadata I/O on the PUT path.

For DFS-only cache recovery, I lean toward A. Our local SSD path already provides a similar model: the storage backend scans its metadata and reports objects to the Master, which can create missing objects or attach replicas to existing ones. Requiring a Master snapshot would also exclude objects whose bucket metadata is durable but which were written after the latest snapshot.

The authority split in this RFC reflects the current shard allocator design: it persists allocation ownership, but relies on the Master snapshot for object visibility. It does not have to be a requirement for every allocator. The shard allocator could also support independent recovery if it persisted enough object lifecycle information.

I would suggest reusing the existing Master object-registration machinery where practical, while keeping bucket-specific persistence and validation in the backend.

One point I would like to clarify is the recovery boundary for sealed buckets. Since `COMMITTED` and `TOMBSTONE` updates are persisted asynchronously:
- Can a completed object in a sealed bucket also be lost if its persisted state is still `PENDING`?
- After deletion or a same-key update, how do we prevent an older persisted `COMMITTED` entry from becoming visible again?

Accepting cache loss is reasonable, but we should explicitly define whether stale-value recovery or deletion rollback is acceptable. With those semantics clarified, I do not think a Master snapshot needs to be a prerequisite for bucket-driven recovery.

### wp-bc · 2026-09-23

> Thanks [@wp-bc](https://github.com/wp-bc) for explaining the design. I think accepting the loss of the active bucket is a reasonable tradeoff for recomputable cache data, especially if it avoids synchronous metadata I/O on the PUT path.
> 
> For DFS-only cache recovery, I lean toward A. Our local SSD path already provides a similar model: the storage backend scans its metadata and reports objects to the Master, which can create missing objects or attach replicas to existing ones. Requiring a Master snapshot would also exclude objects whose bucket metadata is durable but which were written after the latest snapshot.
> 
> The authority split in this RFC reflects the current shard allocator design: it persists allocation ownership, but relies on the Master snapshot for object visibility. It does not have to be a requirement for every allocator. The shard allocator could also support independent recovery if it persisted enough object lifecycle information.
> 
> I would suggest reusing the existing Master object-registration machinery where practical, while keeping bucket-specific persistence and validation in the backend.
> 
> One point I would like to clarify is the recovery boundary for sealed buckets. Since `COMMITTED` and `TOMBSTONE` updates are persisted asynchronously:
> 
> * Can a completed object in a sealed bucket also be lost if its persisted state is still `PENDING`?
> * After deletion or a same-key update, how do we prevent an older persisted `COMMITTED` entry from becoming visible again?
> 
> Accepting cache loss is reasonable, but we should explicitly define whether stale-value recovery or deletion rollback is acceptable. With those semantics clarified, I do not think a Master snapshot needs to be a prerequisite for bucket-driven recovery.

Thanks, this is consistent with our thinking. We also prefer option A for bucket recovery, and reusing the existing Master object-registration path makes sense. The bucket backend can recover and validate its entries, and the Master can then reconstruct object metadata from the reported `(key, descriptor)` records, similar to the local SSD path.

To clarify the current implementation: metadata for the active bucket is kept only in memory. When the bucket is sealed, a complete metadata snapshot is written and fsynced. Later changes to `COMMITTED` or `TOMBSTONE` states in a sealed bucket only mark its metadata as dirty, and a maintenance thread or the clean shutdown path flushes it afterward.

During recovery, we validate each bucket metadata file and restore only `COMMITTED` entries. `PENDING` and `TOMBSTONE` entries are not restored, and a data file without valid metadata is discarded. If the same key exists in multiple buckets, the entry with the greatest `(generation, bucket_id, offset)` is selected.

Regarding your first question: yes, a completed object may still be lost if its persisted state is still `PENDING`, even if it belongs to a sealed bucket. If the Master crashes before the dirty metadata is flushed, the result is a cache miss. We consider this acceptable for the same reason that we accept losing the active bucket: an unexpected restart may lose recently written cache data, but normal PUTs do not require synchronous metadata I/O.

For the second question, the current implementation first changes the key's state to `TOMBSTONE` and marks the bucket metadata as dirty. A background thread later rewrites the metadata according to that dirty flag. This does leave a real gap: if the `TOMBSTONE` has not been flushed before a crash, the old value may become visible again during recovery.

One idea for addressing this is to add a small global invalidation WAL only for deletion operations. A same-key update also falls into this category because it deletes the old entry. Before acknowledging a deletion or replacement, we would persist the old entry's `bucket_id`, offset, and generation. During recovery, these records would be replayed after loading the bucket metadata. A WAL record would remain until the corresponding invalidation is durable in the bucket metadata, and would then be removed through periodic or size-triggered compaction.

This keeps the normal PUT path unchanged. Only deletion and same-key update would require an additional `fsync`. The intended rule is that losing a recently written cache value is acceptable, but restoring a deleted or superseded value is not.

`Remove` and same-key update are relatively uncommon in our workload, so we can address this gap in a follow-up if needed. This is only our initial idea, and we would be interested in your opinion.

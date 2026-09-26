# [Issue #4230] [RFC]: Multi-disk SSD offload for the bucket storage backend

source: https://github.com/kvcache-ai/Mooncake/issues/4230
state: open | updated: 2026-09-19T02:20:48Z
labels: 

## 正文

## Motivation

We run SSD offload in production. It gives us a much larger cache tier than DRAM
alone and measurably lifts our KVCache hit rate. Our serving hosts, however,
have several SSDs each, and today offload can only use one of them: the other
drives sit idle while the single configured disk caps both our offload capacity
and our offload bandwidth. Adding capacity means buying a bigger drive rather
than using the ones already in the box.

## Current behavior

`BucketStorageBackend` assumes a single offload root throughout:
`MOONCAKE_OFFLOAD_FILE_STORAGE_PATH` is one directory, `total_size_` is one
counter, there is one FIFO/LRU eviction order over `buckets_`, and every path is
built from the one root. There is no supported way to point one real client at
more than one disk. The workarounds are all unsatisfying:

- **One real client per disk.** Multiplies RPC servers, memory pools and master
  registrations per host, and splits the DRAM segment N ways.
- **LVM/RAID-0 across the SSDs.** Loses per-disk failure isolation — one drive
  failing takes down the whole offload tier instead of a fraction of it — and
  puts a striping layer under an I/O path that already does large sequential
  bucket writes.
- **A union/overlay filesystem.** Adds a filesystem layer with its own
  accounting, which defeats the physical-usage cap that Kubernetes `emptyDir`
  deployments depend on.

## Proposal

Let `MOONCAKE_OFFLOAD_FILE_STORAGE_PATH` accept a comma-separated list of roots
and make `BucketStorageBackend` per-disk end to end. A single path stays a list
of length one, so existing deployments are unaffected.

```bash
export MOONCAKE_OFFLOAD_FILE_STORAGE_PATH=/nvme0/mooncake,/nvme1/mooncake
export MOONCAKE_OFFLOAD_BUCKET_MAX_TOTAL_SIZE_LIST=214748364800,429496729600
```

### Configuration surface

- `MOONCAKE_OFFLOAD_FILE_STORAGE_PATH` takes a comma list. Whitespace around
  entries is trimmed, empty entries dropped. Each root is validated on its own
  (a `stat` of the raw list string is always `ENOENT`). Roots may not nest
  inside one another — overlapping roots would double-count physical usage.
- `MOONCAKE_OFFLOAD_BUCKET_MAX_TOTAL_SIZE_LIST` is a new optional per-disk quota
  list, positionally aligned with the path list. Empty broadcasts the existing
  scalar `MOONCAKE_OFFLOAD_BUCKET_MAX_TOTAL_SIZE` to every disk; a shorter list
  reuses its last entry. Entries must be `> 0`.
- When no quota is configured and an eviction policy is enabled, each disk
  defaults to 90% of *its own* physical capacity — the existing behavior, now
  applied per disk.

### Placement and accounting

- **Round-robin placement.** A new `rr_cursor_` picks the first disk to try;
  a disk qualifies if its whole quota could hold the incoming bucket (and,
  with eviction disabled, if it already has the room). `NO_AVAILABLE_DISK` when
  none qualifies.
- **`DiskState` per root**, holding `max_total_size`, `total_size`,
  `pending_write_size`, `pending_eviction_size`, its own FIFO and LRU eviction
  indices, and its own physical-usage scan cache.
- **Selection, write reservation and eviction happen in one critical section**,
  so a concurrent writer cannot pick a disk on stale free-space numbers. The
  chosen disk travels in `PendingEviction::disk_index` and every
  restore/commit/release step credits that same disk.
- **`MOONCAKE_OFFLOAD_BUCKET_MAX_PHYSICAL_BYTES` becomes a per-disk cap**, since
  the `du`-equivalent scan now runs per root.
- **Watermark eviction runs per disk**, one disk at a time, rather than off a
  single global watermark.

### Recovery

`BucketMetadata` gains a `disk_index`, used to route path construction. It is
**not** serialized: `Init()` scans every root and re-derives the index from the
disk whose subtree the `.meta` file was found under. Existing offloaded data
therefore stays readable with no migration step, and a single-disk deployment
that later adds a second path keeps all its data.

## Design decisions worth comment

1. **Round-robin rather than most-free-wins.** Free-space-greedy selection
   drains onto whichever disk is emptiest until the disks equalize, then
   degenerates into alternating anyway — but in the meantime it concentrates
   write bandwidth on one drive, which is exactly what this feature exists to
   avoid. Round-robin keeps every drive in the write path from the first bucket.
   Capacity skew is handled by per-disk quotas instead, not by placement.
2. **Per-disk quotas rather than one global quota.** A write reserved on one
   disk but counted against a global counter makes *other* disks evict to make
   room for bytes they will never receive. Per-disk accounting is what makes the
   eviction decision local and correct.
3. **Positional quota list, and it fails as a unit.** Because entries are matched
   to paths by position, one unparsable entry cannot simply be skipped: that
   shifts every later disk onto its neighbour's quota. The whole list is dropped
   with an error log and the scalar quota is used instead. Entries must be `> 0`,
   deliberately stricter than the scalar (where `<= 0` means "derive a default"),
   because a `0` in a position-aligned list is far more likely a typo than an
   intent to unlimit exactly one disk.
4. **`disk_index` is derived, not persisted.** Persisting it would make the
   on-disk format depend on the *order* of the path list, so reordering the
   configuration would silently mis-route reads. Deriving it from the location
   of the `.meta` file makes the disk the single source of truth.

## Non-goals

- **Only `bucket_storage_backend`.** `file_per_key_storage_backend` and
  `offset_allocator_storage_backend` use `storage_filepath` as a single
  directory and would treat a comma list as one path name. They must stay on one
  path; this is documented.
- **No rebalancing.** Buckets are never moved between disks after placement.
  Adding a disk to the list makes it receive new writes only; removing a disk
  makes its buckets unreachable.
- **No cross-disk striping of a single bucket.** A bucket lives entirely on one
  disk, which keeps the read path and the failure domain unchanged.
- **No global cap across disks or across ranks.** Each disk is bounded on its
  own; a machine-wide sum would need master-side aggregation, which is out of
  scope here (and already noted as out of scope for `MAX_PHYSICAL_BYTES`).

## Compatibility

Backward compatible. A single path behaves exactly as today, existing on-disk
data is readable with no migration, and the new environment variable is optional.
No public API or wire format changes; `BucketMetadata`'s serialized form is
unchanged.

## Testing

17 new `MultiDisk*` cases in `mooncake-store/tests/storage_backend_test.cpp`
cover read-back across disks, recovery from every disk on `Init()`, round-robin
evenness (including under eviction pressure), per-disk quota enforcement,
rejecting a bucket larger than any single disk, unparsable / short /
non-positive quota lists, overlapping-root rejection, and `storage_filepath`
overriding the derived path cache.

## Implementation status

Implemented and tested locally, split into three reviewable commits (config
parsing / backend conversion / docs); roughly 1050 lines of non-test change.
Happy to adjust the design before opening the PR.


## 评论 (1)

### github-actions[bot] · 2026-09-19

Thanks for opening this issue, @DeyunYang!

| Field | Value |
|-------|-------|
| **Issue** | #4230 |
| **GitHub user ID** | `75969023` |
| **Reporter** | @DeyunYang |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

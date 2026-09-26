# [Issue #2560] [Performance]: BatchEvict full-metadata scan dominates eviction-cycle time at 1M objects (and holds snapshot_mutex_ for that duration)

source: https://github.com/kvcache-ai/Mooncake/issues/2560
state: open | updated: 2026-09-25T03:14:23Z
labels: stale

## 正文

### Describe the issue

While reading `MasterService::BatchEvict` (`mooncake-store/src/master_service.cpp`), I wrote a small gtest benchmark that drives the real `BatchEvict` path with benchmark-only timing, to see where its time goes at large metadata scale. Filing the measurements to confirm whether this is worth addressing before proposing anything.

The candidate-selection path traverses all `kNumShards` × tenants × metadata each cycle, builds transient `candidates` vectors of `lease_timeout`, and runs `std::nth_element` to find the threshold — all under `snapshot_mutex_` held as a shared lock for the duration of the scan.

**All numbers are from a synthetic, single-tenant, all-expired, all-no-pin workload** (every object evictable: one completed memory replica, refcnt 0). The first pass reaches the eviction target, so the second pass is not exercised. Real workloads with soft-pinned / unexpired / multi-tenant objects will differ — I'm reporting the structural cost, not a production latency claim.

## Measurements

Commit `ef0312f8`, 128-core host, single-threaded `BatchEvict`, `evict_ratio_target=0.5`, `evict_ratio_lowerbound=0.25`.

### 1. End-to-end runtime is linear in object count

Bare (non-instrumented) `BatchEvict`:

| objects | runtime |
|---------|---------|
| 10k | ~8.7 ms |
| 100k | ~109 ms |
| 1M | ~0.95–1.0 s (median; n=5 range 930 ms–1.2 s, shared instance) |

### 2. The time is in scanning, not sorting or evicting

Per-phase breakdown at 1M (instrumented; ratios are the point, absolute total is higher due to instrumentation overhead):

| phase | share of cycle |
|-------|----------------|
| metadata scan / traversal | ~73–75% |
| └ candidate vector collection | ~28–31% |
| `std::nth_element` (all calls) | ~0.1% |
| actual eviction (`try_evict_group_or_object`) | <0.5% |

To be clear, I checked whether `nth_element` was the cost — it is not (~0.1%). The dominant cost is the full-metadata traversal to collect candidates.

### 3. The scan holds `snapshot_mutex_`, blocking unique-lock waiters

A probe thread issues a single `unique_lock<shared_mutex>` on `snapshot_mutex_` shortly after a cycle begins and records the wait. 30 trials at 1M:

| unique-lock wait | value |
|------------------|-------|
| p50 | ~1.00 s |
| p95 | ~1.21 s |
| max | ~1.36 s |

Wait p50 ≈ (cycle time − probe start delay), i.e. the waiter is blocked for essentially the whole scan. Because the shared lock is held once for the whole scan rather than re-acquired, the waiter did not measurably change `BatchEvict`'s own runtime in this probe.

## Question

Is the full-metadata scan in candidate selection considered acceptable at this scale, or would a candidate-selection structure that avoids repeated full scans (e.g. a lease-timeout-ordered auxiliary structure / per-shard expiration structure, in a similar spirit to the bounded-scan concerns raised for master-side promotion in #2509) be of interest?

I'm aware #1998 introduces radix-tree-based eviction for RadixAttention prefix-chain correctness. This report is meant to be complementary and narrower: the scan cost above exists independently of prefix semantics — it is purely about how candidates are found by `lease_timeout`. The two seem orthogonal and could land independently, but happy to be corrected if #1998 already subsumes this.

If reducing the scan / lock-hold time is of interest, I'm happy to put up a small PR — wanted to confirm the direction first.

## Reproduction

The benchmark drives the real path (`MountSegment` → `PutStart` → `PutEnd(..., ReplicaType::MEMORY)` → `BatchEvict`) with test-only timing through the existing friend-test pattern; it changes no production behavior. Happy to share the patch.

## Environment

- Building `main` near commit `ef0312f8`, store + transfer engine, TCP transport, RelWithDebInfo.
- Synthetic benchmark, single-threaded `BatchEvict`; not a production runtime failure.


## 评论 (10)

### github-actions[bot] · 2026-06-22

Thanks for opening this issue, @jacklin78911-collab!

| Field | Value |
|-------|-------|
| **Issue** | #2560 |
| **GitHub user ID** | `251732545` |
| **Reporter** | @jacklin78911-collab |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### ykwd · 2026-06-23

We have also noticed this issue, and previously conducted in-depth testing and optimization, e.g., https://github.com/kvcache-ai/Mooncake/pull/2405 https://github.com/kvcache-ai/Mooncake/pull/2508 However, these two optimizations were not aimed at reducing the overall time of evict. Instead, they focused on optimizing the issue where holding the write lock during evict would block exist and get operations, both of which are latency-critical. If you have any further optimization ideas for the evict operation, we would be very happy to hear them and take a look together.

### jacklin78911-collab · 2026-06-23

Thanks @ykwd, and thanks for pointing me to #2405 / #2508 — I read through them.

If I understand correctly, those PRs mainly reduce contention between eviction and latency-critical lookup/get paths: #2405 groups `BatchExistKey` by metadata shard and moves evicted-replica destruction out of the shard write lock, while #2508 extends the shard-grouped approach to `BatchGetReplicaList`.

That seems complementary to what I measured here rather than overlapping with it:

* The work moved out of the shard write lock in #2405 corresponds to the actual-eviction/destruction part of the cycle. In my breakdown that part is very small at 1M objects (`actual eviction` <0.5%, and `nth_element` ~0.1%). To the best of my reading, the baseline I measured already includes the deferred-replica destruction path from #2405, so that <0.5% is measured after that optimization — the scan cost below is what remains on top of it.
* The dominant part in this benchmark is the full metadata traversal / candidate collection (~73–75% of the cycle). That still determines the total eviction-cycle time and the duration for which `snapshot_mutex_` is held in shared mode.
* So my reading is that #2405 / #2508 reduce eviction's interference with latency-critical lookup/get paths, while the remaining issue here is reducing the total candidate-selection scan time itself, and therefore the outer `snapshot_mutex_` hold duration.

For possible directions, I agree this should be measured rather than assumed. One idea would be to maintain a per-shard lease-timeout-oriented candidate structure, such as a small expiration heap or coarse time-bucketed structure, updated on insert/erase and revalidated at eviction time for lease / pin / replica state. The goal would be to reduce the number of metadata entries scanned per eviction cycle, not to change the eviction policy semantics.

The tradeoff is extra maintenance cost on Put/erase/lease-update paths and correctness around soft-pin / expired lease / group-object cases, so I would not assume it is a win without a benchmark.

If this direction sounds reasonable, I can try to put together a small benchmark + PoC on top of current main and compare it against the current full-scan path before proposing any production change. Also happy to start by sharing the benchmark-only patch from this issue if that would be more useful.


### yokinoshitayoki · 2026-06-23

@jacklin78911-collab Thanks for the detailed breakdown. I agree this looks complementary to #2405 / #2508.

My understanding is that #2405 and #2508 mainly reduce eviction's interference with latency-critical lookup/get paths by reducing metadata shard lock contention. This issue is pointing at a different layer: the total cost of eviction candidate selection is still O(total metadata objects), and the outer `snapshot_mutex_` shared lock is held for that whole eviction cycle.

A benchmark-only patch sounds good to me. Would you mind share the benchmark-only patch here, or open it as a small benchmark PR?

For the optimization direction, a per-shard lease-timeout-oriented candidate structure, such as a heap or coarse time buckets, sounds worth exploring. But I think we should be more careful because maintaining it would add cost to put/erase/lease-refresh paths, and lookup/get may refresh leases on latency-critical paths. Group objects, soft pins, hard pins, and replica state revalidation also need to be handled carefully.

### jacklin78911-collab · 2026-06-23

Thanks @yokinoshitayoki — that makes sense, and thanks for spelling out the tricky parts.

I agree the lease-refresh path is probably the main reason this should not be treated as a straightforward heap/indexing change. If lookup/get can refresh leases on latency-critical paths, then a strictly ordered per-shard heap keyed by `lease_timeout` could shift O(log N) maintenance cost onto exactly the paths #2405 / #2508 were trying to protect.

My current thinking is to keep the next step limited to measurement first. I can clean up the benchmark-only patch into a small PR against current main, without changing production eviction behavior, so the full-scan cost and the `snapshot_mutex_` wait can be reproduced and reviewed in context.

For the optimization direction, I would treat the index as a hint rather than a source of truth. A coarse time-bucketed or lazy/approximate candidate structure may be safer than an exact heap, with eviction still revalidating the real `lease_timeout`, soft pin, hard pin, group-object state, and replica state before removing anything. The key question is whether the scan-time reduction outweighs the extra maintenance cost on put/erase/lease-refresh paths, so I would want to measure that before proposing any production change.

I'll start with the benchmark-only PR first and link it back to this issue.


### ykwd · 2026-06-24

> One idea would be to maintain a per-shard lease-timeout-oriented candidate structure, such as a small expiration heap or coarse time-bucketed structure, updated on insert/erase and revalidated at eviction time for lease / pin / replica state.

Note that the lease or access time is also updated at each Get operation. And get operation only holds read lock, during which we cannot update the shard-scope data structure

### jacklin78911-collab · 2026-06-24

Good point — I agree this is the core difficulty.

If `Get` refreshes the lease/access time while only holding a read/shared lock, then a precisely maintained per-shard heap or ordered index would be problematic: updating that structure on every `Get` would either require extra synchronization on the read path, or effectively move maintenance cost and contention onto the latency-critical path that #2405 / #2508 tried to protect.

So I think an exact index is probably not the right starting point. If we explore this direction, I would treat the candidate structure only as a hint, not as the source of truth.

In that model, `Get` would not synchronously update the auxiliary structure. The eviction path would use the structure to find likely candidates, but before evicting anything it would still revalidate the real object state: current lease/access time, soft pin, hard pin, group-object state, and replica state. If a candidate was refreshed by a recent `Get`, eviction would simply skip it.

The tradeoff is that the hint structure can become stale. That means eviction may spend time checking stale candidates, so the design would need a cleanup / fallback policy — for example, falling back to the current full scan if too many popped candidates are invalid, or periodically rebuilding/coarsening the structure. This is also why I think this should be evaluated with a benchmark before proposing any production change.

So my current view is:

* a strictly maintained heap is likely too expensive for the `Get` path;
* a lazy / approximate candidate structure may still be worth testing;
* correctness should still come from eviction-time revalidation, not from the auxiliary structure itself.

Does this “hint + revalidation + fallback” direction sound compatible with the read-lock constraint you mentioned?


### jacklin78911-collab · 2026-06-25

Update: I re-measured on current `main` (commit `ae250848`, including the #2286 parallel Phase-1 rewrite), since my earlier single-threaded scan breakdown is now stale.

Setup: AutoDL host, 12-core / RTX 4090, TCP transport, RelWithDebInfo. Synthetic workload: single tenant, all objects expired, no pin, one completed memory replica each, `evict_ratio_target=0.5`, `evict_ratio_lowerbound=0.25`. The following numbers come from local-only instrumentation inside `BatchEvict` and are not part of PR #2584.

### Per-phase breakdown at 1M objects

Median of 31 runs:

```text
total BatchEvict time        ~1.50 s
phase1 parallel scan         ~35 ms   (~2.3%)
phase2 serial work           ~1.24 s  (~82.2%)
snapshot_mutex_ hold time    ~1.50 s  (approximately the whole cycle)
per-shard lock max           ~2–3 ms
```

So two things changed relative to my original report:

1. #2286's Phase-1 parallelization is effective. The candidate scan that I previously measured as dominant in the older single-threaded version is now only about 2.3% of the cycle on current `main`. So my earlier “scan dominates” framing is outdated for the current implementation.

2. The remaining dominant cost is now the serial Phase 2: candidate re-lookup / revalidation / eviction work for about 500k evicted objects, which accounts for about 82% of the cycle in this workload.

The part that did not change is the outer lock-hold behavior:

* `snapshot_mutex_` is still held in shared mode for essentially the entire `BatchEvict` cycle.
* In the 1M-object run, that means the shared lock is held for about 1.5s.
* Per-shard metadata locks do not look like the bottleneck in this version: max hold time is only about 2–3ms, consistent with #2286's design where different scanning threads lock disjoint shards.

### Unique-lock waiter probe

I also reran the single-waiter probe on current `main`. A single `unique_lock` waiter on `snapshot_mutex_` arrives shortly after a `BatchEvict` cycle begins.

30 trials at 1M objects:

```text
batch_evict_total_p50   ~1.44 s
unique_lock_wait_p50    ~1.44 s
unique_lock_wait_p95    ~1.49 s
unique_lock_wait_max    ~1.54 s
```

So the waiter blocks for almost the full `BatchEvict` cycle. This suggests that paths needing the `snapshot_mutex_` unique lock, such as snapshot / graceful unmount style management paths, can still be delayed by the whole eviction cycle even after the Phase-1 parallelization.

My current reading is:

* Phase-1 scan time is no longer the main issue on current `main`.
* Per-shard metadata lock contention does not appear to be the main issue in this benchmark.
* The remaining issue is the combination of serial Phase-2 work and the fact that `snapshot_mutex_` is held across the whole cycle, so unique-lock management paths can still wait for about the full eviction duration.

I can share the local instrumentation patch or raw per-trial CSV if that would be useful.


### jacklin78911-collab · 2026-06-26

@yokinoshitayoki Just to summarize the updated measurement: after #2286, Phase-1 scan time and per-shard lock contention no longer look like the main issue in this benchmark. The remaining cost appears to be the serial Phase 2 plus `snapshot_mutex_` being held across the whole cycle, which makes a unique-lock waiter block for nearly the full eviction duration.

Happy to look into Phase 2 specifically — for example, whether some of the re-lookup / revalidation / eviction work can be parallelized, or whether the `snapshot_mutex_` scope can be narrowed safely.


### github-actions[bot] · 2026-09-25

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.

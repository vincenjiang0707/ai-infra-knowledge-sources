# [Issue #4207] [RFC]: Export process and allocator memory metrics, and complete the jemalloc build option

source: https://github.com/kvcache-ai/Mooncake/issues/4207
state: closed | updated: 2026-09-19T02:54:06Z
labels: 

## 正文

## Summary

Mooncake exports no process memory metrics today. There is no `mooncake_process_rss_bytes`,
nothing sourced from `/proc/self/status`, and no allocator visibility of any kind. When a
master's RSS climbs, the only available tools are a code audit and a heap profiler attached
after the fact.

This RFC proposes adding a process/allocator metric surface to both the master and the
client, and finishing the `STORE_USE_JEMALLOC` option introduced in #902 so that the
allocator it selects can actually be observed.

**`STORE_USE_JEMALLOC` stays OFF by default.** This is not a proposal to change the default.

## Motivation

Two threads converge here.

**#3452** (mooncake-master OOM under a long-context PD-separation workload) was closed as
fixed on main, but the discussion is instructive: diagnosing it took a structure-level audit
of the `MasterService` metadata lifecycle because no metric could distinguish "the allocator
is holding freed pages" from "Mooncake is leaking". The closing analysis names the mechanism
explicitly — temporary allocations that glibc/jemalloc arenas retained after the workload
stopped. In that thread, @ykwd suggested:

> for workloads with too much metadata, it may also be worth trying jemalloc to improve
> memory allocation behavior and potentially reduce RSS retention / fragmentation

That suggestion is hard to act on today: a release binary is stripped, `STORE_USE_JEMALLOC`
emits no runtime evidence that it took effect, and even with jemalloc linked there is no
series showing whether pages are being purged.

**#1436** proposed defaulting jemalloc ON. It got an LGTM and stalled on a single concern —
jemalloc is not packaged on every distribution — then was auto-closed for inactivity. That
concern is specific to flipping the default and does not apply to this RFC.

Independently, we hit the same class of problem in production and traced it to the bottom.
The measurements are in **Production evidence** below; they are what the metric surface
proposed here was built to make visible.

## Production evidence

Master-side and client-side, all metadata-churn driven.

### The restart tax, measured with syscall tracepoints

On a production leader holding ~264M keys, two things were happening. Every client restart
stepped master RSS up by roughly 15 GB and it never came back down, five times in a single
day. Underneath that, RSS also grew steadily through normal serving, with no restart
involved. Neither is fixed by an HA failover. The figure below is the one traced restart,
measured end to end.

We attached `sys_enter_mmap` / `mprotect` / `munmap` / `brk` / `madvise` tracepoints filtered
to the master pid across one controlled client restart, sampling `VmRSS` and master metrics
every 15s. Overhead was negligible.

| Phase | key_count | newly committed (mprotect) | madvise / munmap | VmRSS |
|---|---|---|---|---|
| erase, 4 min | 264,474,025 -> 222,467,218 (**-42.0M**) | 4 MB | **0 / 0** | +41.7 MB (flat) |
| refill, 3 min | 224,010,477 -> 263,744,892 (**+39.7M**) | **14,888 MB over 2,654,157 calls** | 58 MB / 0 | **+15.1 GiB** |
| whole window, 10 min | net -0.8M (back to start) | **15,701 MB = 15.33 GiB** | 58 MB madvise | 276.15 -> **291.39 GiB (+15.23 GiB, permanent)** |

Three readings:

1. **Nothing was returned.** Freeing ~42M objects produced 0 `madvise` and 0 `munmap` calls;
   RSS moved 42 MB in four minutes.
2. **Nothing was reused.** The refill did not touch the free lists just created — it asked the
   kernel for 14.9 GiB of fresh memory. Reuse was measured at 0, not "low". Grouping the new
   commits by 64 MB alignment: `heaps=253 total=15.33 GiB min=1.3MB p50=62.5MB p90=64.0MB
   max=64.0MB` — 253 brand-new 64 MB heaps filled one by one (253 x 64 MB ~ 16.2 GiB).
3. **That accounts for all of it.** `mprotect` total 15.33 GiB matches the 15.23 GiB RSS rise
   almost byte for byte, so there is no other consumer hiding in the number.

The mechanism is glibc's: it returns free memory only from the top of a heap, and the erased
metadata sat in the middle.

### After switching the master and client to jemalloc

Same deployment, `MALLOC_CONF=background_thread:true`, allocator linked in (verified via
`/proc/<pid>/maps`, not `LD_PRELOAD`):

| | glibc | jemalloc |
|---|---|---|
| key_count | 264.5M | 267.9M |
| VmRSS | 276.1 GiB | **152.7 GiB** |
| **RSS per key** | ~1.19 KiB | **~612 B** |
| anonymous mappings | 4177 mappings / 4085 64 MB heaps | **391 mappings** |
| trough under sustained churn | steps upward, 58.8 -> 66.3 -> 73.4 GiB, never converging | steps down, then flat |

24h continuous sampling (2-min interval, 718 samples, zero gaps, `restarts` 0 throughout, a
single incarnation):

```
start   RSS 155.09 GiB   keys 268.01M
end     RSS 152.71 GiB   keys 267.91M
net -2.38 GiB (-1.5%)    peak 155.43 (2nd h)   trough 152.39 (21st h)
```

Over the same window the resident set turned over completely — evictions +268M, puts +272M,
`allocated_bytes` swinging between 3.0 and 4.6 TB across a dozen fill/evict cycles — while
`key_count` stayed within 267.90-268.01M. So the RSS decline is not "keys went away". The
per-2h troughs descend monotonically and then flatten (154.92 -> ... -> 152.39 -> 152.53 ->
152.69), the exact inverse of the glibc staircase.

A second deployment with sustained rather than restart-driven churn (483M evictions against a
41M resident key count, ~12x turnover) showed the same allocator behavior at ~750 B/key under
glibc.

The client was verified the same way, and that result is why this proposal links the allocator
into `mooncake_client` rather than the master alone. The client under test had SSD offload
enabled, which puts it in the same position as the master: every offloaded object carries a
metadata entry in the client's own maps — `object_bucket_map_`, plus the LRU index and the
pending-key sets beside it — so an offload workload allocates and frees small records at the
rate objects move, and glibc holds the freed pages exactly as it does on the master. On a
client serving a 900 GB segment, resident memory under glibc grew past 1000 GB and was still
climbing when the run was cut. With jemalloc linked, the same workload settles at around
930 GB and stops growing.

### Why this argues for the metrics, not just for jemalloc

Every number above came from syscall tracing and `/proc` scraping done by hand, after the
fact, on a live leader. None of it was visible in Mooncake's own metrics, and the two
hypotheses that mattered — "decay never ran" versus "decay ran but fragmentation pins the
pages" — produce identical curves under cgroup-level RSS. The series proposed here
(`dirty_purge_runs_total` and `dirty_madvises_total` for the first, `resident/allocated` and
`active/allocated` plus the per-size-class breakdown for the second) separate them directly,
and `mooncake_process_rss_peak_bytes` catches the `VmHWM` that OOM decisions actually use and
that a 15s scrape otherwise misses.

## Design

### Metric surface

A single `AllocatorMetric` class, held by both `MasterMetricManager` and `ClientMetric`, so
master and client expose the same series and a scrape can be compared across the two.

**Process series**, from `/proc/self/status`, exported regardless of which allocator is
linked: `mooncake_process_rss_bytes`, `..._rss_peak_bytes`, `..._rss_anon_bytes`,
`..._rss_file_bytes`, `..._rss_shmem_bytes`, `..._vsize_bytes`, `..._swap_bytes`.

These are the ground truth the allocator series are read against. `mooncake_jemalloc_resident_bytes`
is jemalloc's own upper estimate over the extents it maps and can exceed the kernel's resident
size, so the two are compared for divergence rather than subtracted.

**Allocator series**, from `mallctl`: `mooncake_jemalloc_enabled` plus allocated / active /
metadata / resident / retained / mapped / dirty / muzzy bytes, arena and background-thread
counts, the `opt.dirty_decay_ms` and `opt.muzzy_decay_ms` knobs, and cumulative purge counters
(`dirty_purge_runs_total`, `dirty_madvises_total`, …). Dirty and muzzy are kept apart rather
than summed, because jemalloc 5 decays them on separate paths and exposes no combined counter.

**Per-size-class occupancy**: `mooncake_jemalloc_bin_regs`, `..._bin_slabs`, `..._bin_used_bytes`,
labelled by size class. A slab returns to the OS only once every region in it is free, so a
size class sitting at low occupancy is holding `slab_bytes` while using `used_bytes` — this is
the series that localizes fragmentation to a specific allocation size.

### Keeping libmooncake_store allocator-free

`libmooncake_store` is also consumed by the Python extension, which must not have an allocator
forced on its host process. So:

- jemalloc is linked into the `mooncake_master` and `mooncake_client` executables only.
- The `STORE_USE_JEMALLOC` compile definition is scoped to those two targets.
- `AllocatorMetric` names no jemalloc type. It calls a `JemallocStatsCollector` function
  pointer installed at startup by a binary that does link the allocator
  (`SetJemallocStatsCollector`). With no collector installed, `mooncake_jemalloc_enabled`
  reports 0 and the process series still work — which is the correct answer for a process
  running the system allocator, the Python extension included.

This also means the metric half of this change is useful with `STORE_USE_JEMALLOC=OFF`, i.e.
in the default build, and on distributions where jemalloc is unavailable.

### Startup evidence

`LogAllocatorStatus()` logs the jemalloc version, `background_thread` state, live background
thread count, and both decay knobs at startup. Release binaries are linked with `-s`, so this
line is the only evidence that jemalloc actually replaced the system allocator; `mallctl`
resolves only when jemalloc is linked and glibc exposes no equivalent knob. It compiles to an
empty function when `STORE_USE_JEMALLOC` is off.

### Failure behavior

Collection fails as a whole rather than partially. A build without `--enable-stats` still
answers the epoch write, so a partial snapshot would be indistinguishable on a dashboard from
a healthy one that happens to read zero. On failure `mooncake_jemalloc_enabled` reports 0.

### Scrape rate limiting

Advancing the jemalloc epoch takes a lock shared with allocating threads, so `Refresh()`
reuses already-published values for samples closer together than a minimum interval, rather
than letting an unauthenticated `/metrics` endpoint drive that rate.

### Build variable reset

`#902`'s `${JEMALLOC_STATIC_LIBRARIES}` is kept as is. Its `MASTER_EXTRA_*` indirection is
kept too, renamed `ALLOCATOR_*` because the client now uses it, and extended with the
compile definition and library directory.

That indirection is load-bearing rather than stylistic: `pkg_check_modules` writes its
`JEMALLOC_*` results into the CMake cache, so referencing those names directly on the
targets leaves a build directory reconfigured back to `STORE_USE_JEMALLOC=OFF` still
linking the allocator while the compile definition is gone — the binary runs on jemalloc
while reporting `mooncake_jemalloc_enabled 0`. The plain `ALLOCATOR_*` variables are
cleared on every configure, which the cached names cannot be.

## Compatibility

- `STORE_USE_JEMALLOC` remains OFF by default; no existing build changes behavior.
- No on-disk format, RPC, or public API change.
- New metric series are additive.
- One shared change: `hybrid_metric.h` gains a `basic_hybrid_gauge` alongside the existing
  `basic_hybrid_counter`, via a delegating constructor, so that the per-size-class series can
  declare `# TYPE gauge` instead of telling Prometheus a value that can fall is monotonic.

## Size

1118 added lines, 246 of them tests and 34 CMake. Filed as an RFC per `CONTRIBUTING.md`'s 500-LOC
threshold. Proposed as a single PR with two commits (link, then metrics): splitting it would
leave the metrics commit shipping a collector hook with no in-tree caller.

## Testing

`allocator_metric_test` covers: process series present without a collector; jemalloc series
zero and `enabled=0` without a collector; full series with a collector installed; a failing
collector leaving `enabled=0` rather than publishing zeros; cumulative counters tracking
jemalloc's own totals rather than a sum of deltas; and per-bin series with size-class labels.


## 评论 (2)

### github-actions[bot] · 2026-09-18

Thanks for opening this issue, @erlangx!

| Field | Value |
|-------|-------|
| **Issue** | #4207 |
| **GitHub user ID** | `75969023` |
| **Reporter** | @erlangx |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### DeyunYang · 2026-09-19

Implemented in #4208 

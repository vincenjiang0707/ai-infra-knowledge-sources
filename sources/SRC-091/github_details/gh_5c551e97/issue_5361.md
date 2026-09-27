# [Issue #5361] [MP][ROCm][Bug] L1 pinned via hipHostRegister stays movable: compaction triggers KFD queue eviction, MP server freezes 30–79 s

source: https://github.com/LMCache/LMCache/issues/5361
state: open | updated: 2026-09-26T10:48:19Z
labels: 

## 正文

## Summary

On ROCm, `LazyMemoryAllocator` pins L1 via `cudaHostRegister` (→ `hipHostRegister`), which becomes a KFD **userptr** mapping. The pages stay **movable**, so `VmPin` stays at 0 and the kernel is still free to migrate them. With a large L1 on a host with little free memory, direct compaction keeps migrating L1 pages. Every migration fires the MMU notifier. KFD then evicts **all user queues of the MP server process on every visible GPU** and revalidates the userptr BOs while holding the process's `mmap_lock`.

While that lasts, every page fault in the server blocks, the ZMQ I/O thread included. The whole MP server freezes for **30–79 s**. All connected vLLM workers log `LMCache server is unhealthy — entering degraded mode` in the same millisecond, and with `kv_load_failure_policy=fail` the in-flight requests fail.

## Environment

- 8× AMD Instinct MI350X, ROCm/HIP 7.2.53211, amdgpu 6.16.13, Linux 6.8.0 (Ubuntu), 2.3 TB RAM
- LMCache 0.5.4, MP server (`lmcache server … --l1-size-gb 1200 --l1-init-size-gb 64 --supported-transfer-mode lmcache_driven`), one server shared by two vLLM TP4 instances
- L1 = 1200 GB via `LazyMemoryAllocator` (64 MB `PIN_CHUNK_SIZE`, ~19k registrations); host page cache ~850 GB, `MemFree` ~20 GB
- THP `enabled=madvise`, `defrag=madvise`, `vm.compaction_proactiveness=20` (distro defaults)

## Evidence

1. Server log: single transfers suddenly take tens of seconds (normally ~0.05 s), identical on all TP ranks:
   ```
   Retrieved 256 tokens in 58.194 seconds
   Stored 8192 tokens in 72.317 seconds
   ```
2. `/sys/class/kfd/kfd/proc/<server-pid>/stats_*/evicted_ms` (readable without root): **922 s** of queue eviction in 8 h for the MP server, versus ~20 s for the vLLM workers.
3. A 2 s sampler of `/proc/vmstat` + `evicted_ms` shows the correlation directly:
   | time (UTC) | compact_stall Δ | pgmigrate_success Δ | evicted_ms afterwards |
   |---|---|---|---|
   | 19:53:53 | 267 | 38,930 | +47 s |
   | 19:54:49–51 | 1,078 | 211,587 | +28 s |

   `compact_daemon_wake` stayed at 0, so the migrations came from **direct** compaction, not from kcompactd.
4. Kernel stack of a server thread during the freeze:
   ```
   ZMQbg/IO/0 state=D
     lock_mm_and_find_vma
     do_user_addr_fault
     exc_page_fault
     _copy_to_iter
     skb_copy_datagram_iter
   ```

## Fix we run in production

`mlock()` each chunk right before `cudaHostRegister` in `LazyMemoryAllocator._pin_memory_chunk`, and set `vm.compact_unevictable_allowed=0` so that compaction skips mlocked pages. `mlock` alone is not enough, because the default `=1` still lets compaction migrate them.

```python
# lazy_memory_allocator.py, _pin_memory_chunk, before current_device_spec.pin_memory(ptr, size, 2)
if _libc.mlock(ctypes.c_void_p(ptr), ctypes.c_size_t(size)) != 0:
    logger.warning("mlock failed for chunk at ptr=%#x size=%d: errno %d", ptr, size, ctypes.get_errno())
```

The container also needs `--ulimit memlock=-1:-1` (or `CAP_IPC_LOCK`). Server start takes ~2.5 min longer because the initial 64 GB get faulted in. We additionally set `vm.compaction_proactiveness=0` and THP `defrag=defer`.

Result over 33 h of production: `VmLck` = full 1.2 TB, KFD eviction **2.4 s** total (was 922 s per 8 h), longest transfer 1.2 s (was 72 s), 0 `unhealthy` events, 0 failed requests. The kernel still did 4.2 M migrations and 2.3 k compaction stalls in that time; they just no longer touch L1.

## Suggestions

- ROCm: optionally `mlock` pinned L1 chunks (e.g. a config flag, default on for ROCm) and log a warning when `vm.compact_unevictable_allowed != 0`, or allocate L1 with `hipHostMalloc` (driver-owned GTT, not movable) instead of registering user memory.
- Document the `memlock` ulimit / sysctl requirement for large L1 on ROCm.
- It would also help if the heartbeat logged individual ping failures. #4670 makes the same point: our 40–79 s windows were only visible as enter/leave transitions.

Happy to open a PR for the `mlock` option if that direction is acceptable.


## 评论 (1)

### neevmodh · 2026-09-26

This is an exceptional writeup — a 33-hour production before/after comparison (`VmLck` full pin, KFD eviction dropping from 922s to 2.4s over 8h, longest transfer 72s → 1.2s) is about as convincing a case for a fix as an issue can make.

I don't have ROCm/AMD GPU hardware to reproduce or validate a fix against, so I won't guess at the `mlock`/`hipHostMalloc` implementation blind on a memory-pinning path this sensitive — getting it subtly wrong on hardware I can't test against would be worse than not touching it. You mentioned being happy to open a PR for the `mlock` option yourself, which given you already have the production environment to validate against, seems like the right path here rather than me attempting a parallel implementation. If it'd help, I'm glad to review the PR from the non-ROCm-specific side (config plumbing, the warning log for `vm.compact_unevictable_allowed`, docs for the `memlock` ulimit requirement) once it's up.


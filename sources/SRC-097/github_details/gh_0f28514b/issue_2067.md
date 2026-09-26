# [Issue #2067] releaseXferReq use-after-free (SegFault) + nixlBasicDesc match key excludes metaInfo

source: https://github.com/ai-dynamo/nixl/issues/2067
state: closed | updated: 2026-09-11T14:59:38Z
labels: 

## 正文

## Summary

Two related defects in the NIXL core that together can cause use-after-free (SIGSEGV) and EBADF errors under concurrent FILE backend transfers. Discovered while debugging production EBADF errors (`aio_error failed: Unknown error -9`) in a GLM-5.2 deployment using the POSIX backend for KV cache offloading.

---

## Defect A: `releaseXferReq` use-after-free → SIGSEGV

### Location

`src/core/nixl_agent.cpp:1319-1345` (`nixlAgent::releaseXferReq`)
`src/plugins/posix/posix_backend.cpp:341-345` (`nixlPosixEngine::releaseReqH`)

### Description

When `releaseXferReq` is called on a transfer with `status == NIXL_IN_PROG`:

1. It calls `checkXfer` (poll) — if still IN_PROG:
2. It calls `releaseReqH` (cancel in-flight IO) — for the POSIX backend, this is simply `delete handle` (`posix_backend.cpp:343`)
3. It then `delete req_hndl` (line 1343)

But in-flight IO callbacks (`ioDoneClb`) hold a pointer to `req_hndl`. After `delete req_hndl`, when a cancelled IO completes, its callback accesses the deleted `req_hndl` → **use-after-free → SIGSEGV**.

```cpp
// nixl_agent.cpp:1319
nixl_status_t
nixlAgent::releaseXferReq(nixlXferReqH *req_hndl) const {
    NIXL_SHARED_LOCK_GUARD(data->lock);
    if(req_hndl->status == NIXL_IN_PROG) {
        req_hndl->status = req_hndl->engine->checkXfer(req_hndl->backendHandle);
        if(req_hndl->status == NIXL_IN_PROG) {
            req_hndl->status = req_hndl->engine->releaseReqH(req_hndl->backendHandle);
            // ... error handling ...
            req_hndl->backendHandle = nullptr;
        }
    }
    delete req_hndl;   // ← callbacks for cancelled in-flight IO may still fire after this
    return NIXL_SUCCESS;
}
```

```cpp
// posix_backend.cpp:341
nixl_status_t
nixlPosixEngine::releaseReqH(nixlBackendReqH *handle) const {
    NIXL_ASSERT(handle != nullptr);
    delete handle;   // ← cancels IO but callbacks may still be pending
    return NIXL_SUCCESS;
}
```

### Reproduction

1. Start a POSIX backend transfer with multiple pages
2. While some pages' AIO is still in flight, call `releaseXferReq`
3. `releaseReqH` → `delete handle` → `delete req_hndl`
4. Residual in-flight IO completes → callback accesses freed `req_hndl` → SegFault

### Stack trace (from production)

```
Fatal Python error: Segmentation fault
Thread 0x7f... (most recent call first):
  File ".../nixl/_api.py", line 96 in release
  File ".../nixl_registry.py", line ... in storage
  File ".../hybrid_cache.py", line ... in _page_backup
  File ".../hybrid_cache.py", line ... in backup_thread_func
```

### Suggested fix direction

`releaseReqH` should not `delete handle` while IO may still be in flight. Options:
- Wait for in-flight IO to complete (or be fully cancelled) before deleting
- Use a reference count / shared_ptr so callbacks can safely check if `req_hndl` is still alive
- Mark `req_hndl` as "released" and have callbacks check the flag before accessing

### Impact

This is a latent defect: any fd failure that triggers the error path can lead to `releaseXferReq` being called while IO is in flight. In our production, it caused a SegFault that cascaded to NCCL heartbeat timeout (4.5 min) → all ranks exit → container stop.

---

## Defect B: `nixlBasicDesc` match key excludes metaInfo

### Location

`src/api/cpp/nixl_descriptors.h:84-88` (`operator<`)
`src/infra/nixl_descriptors.cpp:55-58` (`operator==`)
`src/infra/nixl_descriptors.cpp:481-492` (`nixlSecDescList::getIndex`)

### Description

`nixlBasicDesc` compares by `(devId, addr, len)` only. **metaInfo (e.g. file path) is NOT part of the match key.** This means two descriptors with the same `(devId, addr, len)` but different file paths are considered equal.

For FILE_SEG registrations, `addr` is always 0 and `len` is the page size. If `devId` collides (e.g. a caller using per-batch `i+1`), two registrations of the same page produce equal descriptors. `nixlSecDescList::getIndex` (lower_bound) then matches the **first** one in the sorted list — which may belong to a different, in-flight transfer.

When `remDescList` (deregister) uses `getIndex` to find the descriptor to remove, it may remove the wrong one, closing the wrong fd and causing EBADF on the in-flight AIO.

### Code

```cpp
// nixl_descriptors.h:84
bool operator<(const nixlBasicDesc &desc) const noexcept {
    if (devId != desc.devId) return (devId < desc.devId);
    if (addr != desc.addr) return (addr < desc.addr);
    return (len < desc.len);
}

// nixl_descriptors.cpp:55
bool operator==(const nixlBasicDesc &lhs, const nixlBasicDesc &rhs) {
    return ((lhs.addr  == rhs.addr ) &&
            (lhs.len   == rhs.len  ) &&
            (lhs.devId == rhs.devId));
}
```

### Impact

This is the root cause of the EBADF errors observed in production. The sglang-side workaround (global devId counter, PR sgl-project/sglang#34362) prevents devId collision, but the underlying NIXL design issue remains: if any two registrations produce equal `nixlBasicDesc` (by the current match key), deregister can match the wrong one.

### Suggested fix direction

For FILE_SEG, include metaInfo (file path) in the match key, or require devId to be globally unique at the NIXL API level (documented + enforced).

---

## Context

These defects were discovered while debugging EBADF errors (`aio_error failed: Unknown error -9`) in a production GLM-5.2 deployment using the NIXL POSIX backend for KV cache offloading. The complete fix chain:

1. **nixl PR #2066**: posix_aio_io_queue failure-path leak fix (prevents io slot leak + infinite retry)
2. **sglang PR #34362**: nixl_registry devId global uniqueness (prevents deregister misdelete → EBADF trigger source)
3. **This issue**: releaseXferReq UAF (latent, triggered when EBADF error path leads to release while IO in flight) + nixlBasicDesc match key design

Defects A and B are reported as issues (not PRs) because the correct fix involves API design decisions that should be discussed with maintainers.

## Environment

- NIXL: main branch (54a015f)
- Backend: POSIX (Linux AIO)
- Platform: AMD MI350X, 8-GPU, ROCm 7.14
- Workload: GLM-5.2 KV cache offloading via sglang HiCacheNixl


## 评论 (8)

### iyastreb · 2026-08-11

As of now NIXL does not really support cancellation of in-flight requests.
It's not just a question of request lifetime, but also about request invalidation, to prevent late writes/reads from the remote process.

### lluki · 2026-08-26

use after free bug is described here: https://github.com/ai-dynamo/nixl/issues/1955

### lluki · 2026-08-26

Defect B should have been fixed by this PR: https://github.com/ai-dynamo/nixl/pull/1790 

Can you provide the exact NIXL version you are running?

### lluki · 2026-08-26

I'm currently looking at `Defect A` and how it is triggered in SGLang. Where your stack trace is coming from, we do poll to completion, hence, there *should* be no outstanding requests and the handle should be safe to be removed. There is however currently a bug in AIO that immediately returns error codes, leaving pending IOs alive. I think #2085 will fix it and i expect it to be merged soon.

But yes, the releaseXferReqH *also* has a bug with outstanding requests. We will implement some defensive coding there (ref counting on the handle will probably be it).

Another case where I can see the handle being freed without polling to completion is if the inner while (in [sglang, hicache_nixl.py](https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/mem_cache/storage/nixl/hicache_nixl.py#L253-L271)) loop throws a python exception. Then the stack unwinding enters the finally and releases the handle.





### rishabhsinha17 · 2026-08-27

@lluki defect A: #2077 has implemented the flag-flavor deferred free you asked for in its review (Aug 13) since Aug 14. `releaseReqH()` under `io_queue_lock_` frees the request only when every submitted I/O is confirmed, otherwise parks it on an engine-side `released_reqs_` list that `reapReleasedReqs()` sweeps after each `checkXfer()` poll, and the engine destructor drains leftovers, so the free never runs inside a completion callback (posix_backend.cpp:353,377 on that branch). It also covers the agent-side half (a negative `releaseReqH()` status wedges `getXferStatus()`, which only polls while status is `NIXL_IN_PROG`) and adds release-active and release-teardown regression tests that the sanitizer job exercises. State: 20/20 checks green including nixl-ci-test-sanitizers on the run @iyastreb authorized at 58761cb (Aug 24), now CONFLICTING since #1942 merged; I did not push the resolution over the green run, but it already exists on #2161's branch (stacked on #2077): the release gate moves from `allConfirmed()` to `isComplete()`, which also counts cancel completions, so a parked request is not freed while #1942's cancellations are outstanding. #2162 takes the same released_-flag approach with the free inside `ioDone()`/`cancelDone()` rather than a post-poll reap. I can refresh #2077 onto main with the `isComplete()` gate today, or port the tests and the agent-side fix onto #2162, whichever converges faster for you.


### lluki · 2026-08-27

@rishabhsinha17  Sorry, i missed the update on your PR. I'll get back to you.

### hekhong-png · 2026-08-29

Thanks for the detailed response @lluki. Here's the info you asked for:

**NIXL version:** main branch at commit `54a015f` (Aug 10, 2026) — post-v1.3.2, pre-v1.4.0. I verified the production `posix_aio_io_queue.cpp` is byte-identical to that commit.

**Defect B (match key excludes metaInfo):** #1790 is included in our build (confirmed `PathModeDevIdRegistry` is present in `posix_backend.cpp` at `54a015f`). #1790 rejects duplicate path-mode devIds at registration time, which prevents the silent corruption. However, the SGLang caller (`nixl_registry.py`) was still passing per-batch `devId = i+1`, so two concurrent `storage()` calls for the same page would collide and the second registration would fail with `NIXL_ERR_INVALID_PARAM`. Our SGLang-side PR (sgl-project/sglang#34362) fixes the root cause by allocating globally unique devIds from a monotonic counter, so both batches succeed without relying on the NIXL-level rejection. The two fixes are complementary — #1790 guards at the NIXL level, our PR prevents the collision at the caller level.

**Defect A (releaseXferReq UAF):** This is indeed a duplicate of #1955. In our production stack trace, the UAF was triggered exactly as you described — the SGLang `hicache_nixl.py` transfer loop (`while state != "DONE"`) throws a Python exception, and the `finally: release_xfer_handle` runs while AIO is still in flight. Our nixl PR #2066 addresses the io slot leak that pollutes the error path, but the complete fix (proper cancellation + deferred release) is in your #2085. We will defer to #2085 for the definitive fix and are happy to close #2066 as a duplicate once #2085 lands, or rebase #2066 onto #2085 if a smaller incremental fix is preferred.

Regarding the SGLang-side exception path you identified: that is a real issue — `release_xfer_handle` in the `finally` block can run while IO is in flight. We can address that on the SGLang side by polling to completion before releasing, but that is a workaround for the NIXL-level issue that #2085/#2077 properly fix.

### lluki · 2026-09-11

I'm closing this as the remaining issue is #1955 

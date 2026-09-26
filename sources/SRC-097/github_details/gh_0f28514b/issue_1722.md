# [Issue #1722] libfabric backend: releaseReqH() does not delete backend request handle — memory leak

source: https://github.com/ai-dynamo/nixl/issues/1722
state: closed | updated: 2026-06-12T08:16:59Z
labels: 

## 正文

## Summary

`nixlLibfabricEngine::releaseReqH()` does not `delete` the `nixlLibfabricBackendH` object allocated in `prepXfer()`, causing a memory leak on every transfer request lifecycle.

## Environment

- NIXL main branch (latest commit as of 2026-06-03)
- libfabric backend with EFA provider
- Multi-GPU benchmark (8x GPU, 1024 requests/iteration)

## Root Cause

In `src/plugins/libfabric/libfabric_backend.cpp`, `releaseReqH()` simply returns without freeing the handle:

```cpp
nixl_status_t
nixlLibfabricEngine::releaseReqH(nixlBackendReqH *handle) const {
    if (!handle) {
        return NIXL_SUCCESS;
    }
    // Let NIXL framework handle the deletion   <-- INCORRECT: framework does NOT delete
    NIXL_DEBUG << "releaseReqH completed successfully";
    return NIXL_SUCCESS;
}
```

The comment "Let NIXL framework handle the deletion" is **incorrect**. The framework's `~nixlXferReqH()` only calls `engine->releaseReqH(backendHandle)` — it **never** calls `delete backendHandle`. This is confirmed by:

1. `src/core/transfer_request.h` — destructor only calls `releaseReqH`, no `delete`
2. `docs/BackendGuide.md` line 93: _"releaseReqH(): Releases a transfer request handle... **freeing resources**"_
3. Every other backend (UCX, Mooncake, HiXL, HF3FS, OBJ, CUDA GDS) performs `delete handle` inside `releaseReqH()`

## Impact

- Every `postXfer()` call allocates a `new nixlLibfabricBackendH()` (in `prepXfer`)
- The handle is never freed → **unbounded memory growth** proportional to transfer count
- In production disaggregated inference: thousands of transfers/second → rapid OOM

## Proposed Fix

```cpp
nixl_status_t
nixlLibfabricEngine::releaseReqH(nixlBackendReqH *handle) const {
    if (!handle) {
        return NIXL_SUCCESS;
    }

    nixlLibfabricBackendH *lf_handle = static_cast<nixlLibfabricBackendH *>(handle);
    delete lf_handle;

    NIXL_DEBUG << "releaseReqH completed successfully";
    return NIXL_SUCCESS;
}
```

## Additional Related Issues Found

During the same code audit, we also identified several other resource management issues in the libfabric backend:

1. **Control request leak in `postXfer()`** — a `ControlRequestPool` request is allocated unconditionally at the start of `postXfer()` but only released (via send completion callback) when `hasNotif == true`. Without notification, the request permanently leaks from the 256-entry pool.

2. **`received_remote_writes_` unbounded growth** — the `unordered_set<uint32_t>` tracking received XFER_IDs is never cleared, growing indefinitely and causing false positives after XFER_ID wraparound (20-bit counter).

3. **CQ error path does not release failed requests** — when `fi_cq_read` returns error, `fi_cq_readerr` is called for logging but the errored request (identifiable via `err_entry.op_context`) is never returned to the pool.

Happy to submit PRs for any/all of these.

## References

- UCX backend correctly deletes: `src/plugins/ucx/ucx_backend.cpp` (releaseReqH → `delete intHandle`)
- Mooncake backend correctly deletes: `src/plugins/mooncake/mooncake_backend.cpp` (releaseReqH → `delete priv`)
- BackendGuide documentation: `docs/BackendGuide.md` line 93

## 评论 (2)

### amitrad-aws · 2026-06-09

Thanks a lot for calling this out.
We have created a PR to address these issues, https://github.com/ai-dynamo/nixl/pull/1747.
Will close once we merge it

### ztxdcyy · 2026-06-12

> Thanks a lot for calling this out. We have created a PR to address these issues, [#1747](https://github.com/ai-dynamo/nixl/pull/1747). Will close once we merge it

Thank you for the quick response and the PR! Really appreciate it. Looking forward to continued collaboration — I'll keep actively reporting any issues I encounter while working with NIXL and libfabric.

# [Issue #1758] [BUG]: deregisterMem ignores backend failures and reports false success

source: https://github.com/ai-dynamo/nixl/issues/1758
state: closed | updated: 2026-06-12T07:19:59Z
labels: 

## 正文

### Summary

`nixlLocalSection::remDescList()` currently calls `backend->deregisterMem(...)` but ignores its return value. As a result, `nixlAgent::deregisterMem()` may return `NIXL_SUCCESS` even when a backend failed to deregister one or more metadata objects.

This can leave NIXL and the backend in an inconsistent state, and the caller has no way to know that deregistration was only partially completed.

### Current behavior

In `src/infra/nixl_memory_section.cpp`, `remDescList()` does:

```cpp
for (size_t idx : indices) {
    backend->deregisterMem(target[idx].metadataP);
}

target.remDescs(std::move(indices));
return NIXL_SUCCESS;

```
The return value from `backend->deregisterMem(...)` is ignored.

Therefore:

1. Backend deregistration may fail.
2. NIXL still removes the descriptors from its internal base list.
3. `remDescList()` returns `NIXL_SUCCESS`.
4. `nixlAgent::deregisterMem()` may also return `NIXL_SUCCESS`.
5. The caller believes deregistration succeeded even though backend resources may still be registered.

### Expected behavior
`deregisterMem()` should not silently ignore backend deregistration failures.

At minimum:

- if any `backend->deregisterMem(...)` call fails, the failure should be propagated back to `nixlAgent::deregisterMem()`;

- descriptors whose backend deregistration succeeded should be removed from NIXL's internal descriptor list;

- descriptors whose backend deregistration failed should remain registered internally so their metadata is not lost.


## 评论 (2)

### flpanbin · 2026-06-11

I submitted a PR https://github.com/ai-dynamo/nixl/pull/1759  try to fix this. 

### rakhmets · 2026-06-11

In the current approach using error statuses instead of exceptions, resource allocation methods should report an error and return the corresponding status in case of failure. And the appropriate methods for freeing resources should return void and report failures by issuing a warning message in case of failure.

Since `deregisterMem` returns `nixl_status_t` at the moment, then it is expected that it will always return `NIXL_SUCCESS`.

At the moment, there is not much benefit from saving unsuccessful attempts at deregistration in internal structures, since there are no mechanisms for their further processing.

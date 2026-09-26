# [Issue #2032] [gds_mt] Preserve cuFile registered base and descriptor offset for interior GPU pointers in gds_mt

source: https://github.com/ai-dynamo/nixl/issues/2032
state: open | updated: 2026-08-10T07:56:58Z
labels: 

## 正文

## Problem

The current `gds_mt` backend appears to pass the transfer descriptor pointer directly to `cuFileRead` / `cuFileWrite` as the buffer base, with a buffer offset of `0`.

Current shape:

```cpp
cuFileRead(req->fh, req->addr, req->size, req->file_offset, 0);
cuFileWrite(req->fh, req->addr, req->size, req->file_offset, 0);
```

This works when the transfer descriptor pointer is identical to the pointer registered with cuFileBufRegister. However, some KV cache layouts can produce transfer descriptors that point inside a larger registered allocation.

For example:
```cpp
cuFileBufRegister(registered_base, registered_size, flags);
descriptor_addr = registered_base + descriptor_offset;
```

In this case, the transfer descriptor is still inside registered memory, but the pointer passed to the cuFile API differs from the registered base pointer.

### [Why this matters]

For layouts such as layer-separated KV cache storage, the buffer registered with cuFile can be a larger contiguous allocation, while individual transfer descriptors can refer to interior regions.

In that case, `gds_mt` should preserve:
```cpp
devPtr_base   = registered_base;
devPtr_offset = descriptor_addr - registered_base;
```
and call cuFile APIs using the registered base plus descriptor-relative offset.

This follows the [GDS Best Practices Guide](https://docs.nvidia.com/gpudirect-storage/best-practices-guide/index.html) recommendation for accessing subranges of a parent-registered GPU buffer: use the registered buffer base as devPtr_base and specify the sub-buffer location through devPtr_offset.

### [Current behavior]

`gds_mt` currently stores a single pointer in the transfer request:
```cpp
struct GdsMtTransferRequestH {
    GdsMtTransferRequestH (void *a,
                           size_t s,
                           size_t offset,
                           CUfileHandle_t handle,
                           CUfileOpcode_t operation)
        : addr{a},
          size{s},
          file_offset{offset},
          fh{handle},
          op{operation} {}

    void *addr;
    size_t size;
    size_t file_offset;
    CUfileHandle_t fh;
    CUfileOpcode_t op;
};
```
and submits I/O using:
```cpp
nbytes = cuFileRead (req->fh, req->addr, req->size, req->file_offset, 0);
nbytes = cuFileWrite (req->fh, req->addr, req->size, req->file_offset, 0);
```
This does not distinguish between:
- the pointer originally registered with `cuFileBufRegister`
- the descriptor pointer used for this specific transfer

### [Proposed direction]
Store the registered memory base and descriptor-relative offset separately in the gds_mt transfer request.

Conceptually:
```cpp
struct GdsMtTransferRequestH {
    void *dev_ptr_base;
    size_t dev_ptr_offset;
    size_t size;
    size_t file_offset;
    CUfileHandle_t fh;
    CUfileOpcode_t op;
};
```
```cpp
cuFileRead(
    req->fh,
    req->dev_ptr_base,
    req->size,
    req->file_offset,
    req->dev_ptr_offset
);
```
and similarly for `cuFileWrite`.

### [Expected benefit]
This would make gds_mt handle interior GPU pointers consistently with cuFile registered-buffer semantics and avoid unintended fallback behavior when transfer descriptors refer to subranges of a registered allocation.

### [Validation plan]

I can follow up with a PR that adds unit coverage for registered-range resolution:

- descriptor exactly equal to registered base: offset is `0`
- descriptor inside registered range: offset is computed correctly
- descriptor outside registered range: request is rejected
- descriptor range partially exceeds registered range: request is rejected

If useful, I can also add benchmark data in a follow-up comment showing TTFT/QPS and peak bandwidth differences for a layer-separated KV cache workload.

## 评论 (3)

### Chije · 2026-08-05

```markdown
Progress update for #2032:

- Added GTest coverage for registered-base and descriptor-offset resolution.
- Added rejection tests for descriptors before the registered base and beyond
  the registered allocation.
- Added regression coverage for a descriptor equal to the registered base.
- All four GDS_MT offset unit tests passed as part of `nixl:unit`.
- Added a GDS_MT integration test using a full GPU allocation and an
  interior-pointer write/read flow.
- Focused validation passed: 6/6 tests.

Passed tests:

- `nixl:posix_plugin_test`
- `nixl:unit`
- `sanitizer:nixl:gtest`
- `nixl:telemetry_benchmark`
- `nixl:tracing_nsys`
- `gds_mt_integration:nixl:gds_mt_interior_pointer_integration`

The two GDS path-mode smoke tests were excluded because their runtime-directory
registration issue is unrelated to this interior-pointer fix and is not changed
in this PR.

`TELEMETRY_DOCA` was disabled because the available DOCA telemetry exporter
library was ABI-incompatible with the required symbols. CUDA/GDS_MT validation
was executed with GDS enabled.

Detailed build and test commands will be included in the PR.

### yanok · 2026-08-06

Sounds like the right thing to do. But do you have an actual PR to share? Also note that #1856 will unify request preparation across GDS and GDS_MT, which will likely clash with your changes.

### Chije · 2026-08-10

I have opened an implementation PR for this issue:

https://github.com/ai-dynamo/nixl/pull/2062

PR #2062 implements the registered-base and descriptor-offset handling
described in this issue. It also adds:

- unit coverage for interior offsets and the exact registered base
- rejection tests for descriptors outside the registered allocation
- a GDS_MT integration test that performs an interior-pointer write/read
  round trip and verifies the surrounding GPU memory

Focused validation passed locally with 6/6 tests passing on a CUDA/GDS-enabled
host.

I understand that #1856 will consolidate GDS and GDS_MT request preparation
and that this PR is likely to conflict with that refactoring. PR #2062 is
intentionally based on the current pre-consolidation GDS_MT layout. If #1856
lands first, I will rebase and port this fix to the shared `cuda_gds`
request-preparation layer, ensuring that the registered base and descriptor
offset are calculated and applied exactly once.

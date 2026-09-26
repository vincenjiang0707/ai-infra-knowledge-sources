# [Issue #24] [Feature]: Add tracing records for memory alloc/free

source: https://github.com/ROCm/rocprofiler-sdk/issues/24
state: closed | updated: 2025-01-15T18:53:42Z
labels: Under Investigation, Feature Request

## 正文

### Suggestion Description

In Score-P, we usually provide memory allocated on the CPU and GPU as process-level metrics (across a variety of accelerator paradigms). We are able to create finer-grained metrics as desired, for e.g. pinned vs. managed vs. stream-local async allocations.

The problem: in order to know what memory has been allocated, and of what type, we potentially need to intercept all HIP allocation functions and have per-function handling of their semantics (what type of buffer/handle is returned, is "size" an array size or an actual size in bytes, what kind of memory has been allocated). Contrast this with e.g. kernel launch and memory copy, where the semantics of the various API calls are digested by rocprofiler and handed back in the associated event records.

My suggested solution: allow a `MEMORY_ALLOCATION` record kind, operations `ALLOC`, `FREE`,  and potentially `REALLOC`, and something like:
```
enum ROCPROFILER_ALLOCATION_KIND {
    ROCPROFILER_ALLOC_NONE,
    ROCPROFILER_ALLOC_HOST_PINNED,
    ROCPROFILER_ALLOC_UNIFIED,
    ROCPROFILER_ALLOC_DEVICE,
    ... // any other kinds that are worth separating out
    ROCPROFILER_ALLOC_GENERIC, // covers the case where `hipFree` is used as a wildcard
    ROCPROFILER_ALLOC_LAST
};

typedef struct alloc_free_record {
    void* address;
    size_t bytes; // undefined for operation FREE
    ROCPROFILER_ALLOCATION_KIND kind;
} alloc_free_record_t;
```
to be delivered by the callback and buffer tracing systems. This then allows us to register for allocation and free notifications with memory kinds that are meaningful and correct and data that we can feed into our internal `SCOREP_AllocMetric` structures (designed for malloc/free/new/delete) directly.

### Operating System

_No response_

### GPU

_No response_

### ROCm Component

_No response_

## 评论 (2)

### jrmadsen · 2025-01-15

This work was completed in https://github.com/ROCm/rocprofiler-sdk/commit/79006bb8969f4b75ec5083e26b75f88771d829b5

### jrmadsen · 2025-01-15

Let me know if you have any feedback/problems

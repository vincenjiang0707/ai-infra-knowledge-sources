# [Issue #1916] [RFE]: Add ncclNotifyTag API for user-defined profiler metadata injection

source: https://github.com/NVIDIA/nccl/issues/1916
state: closed | updated: 2026-08-10T03:19:57Z
labels: enhancement

## 正文

### Please provide the below details to ensure we understand your needs

# Feature Request: User Metadata Tagging API for NCCL Profiler

## Summary

Add `ncclNotifyTag(uint64_t tag, ncclComm_t comm, cudaStream_t stream)` to inject user-defined metadata into profiler event stream, enabling phase-aware profiling and debug instrumentation with <0.001% overhead.

## Motivation

Modern ML training frameworks divide iterations into distinct phases (forward pass, backward pass, optimizer step), each with different communication patterns and performance characteristics. Understanding per-phase performance is critical for optimization, but current NCCL profiler API provides no mechanism for applications to annotate these semantic boundaries.

### The Phase Attribution Problem

NCCL profilers typically use asynchronous event processing: NCCL operations generate events that are queued and processed by a background thread. This creates a timing gap between when operations occur and when they're attributed to training phases.

**Problem**: When the training framework switches phases (e.g., backward -> optimizer), events still in the queue from the previous phase get misattributed to the new phase. This is especially severe for short phases.

**Optimizer phase challenge**: The optimizer step is particularly problematic because:
1. **Very short duration** (10-200ms, vs 1000ms+ for forward/backward)
2. **Communication-intensive** (AllReduce gradients across all ranks)
3. **Most latency-sensitive** (directly impacts training throughput)

With typical profiler queue lag (~100ms of events), optimizer metrics can be 50-90% corrupted with backward-phase operations, making accurate optimizer analysis nearly impossible.

**Current workarounds** have severe limitations:
- **Synchronous queue flush**: 10%+ training slowdown (unacceptable)
- **External correlation (NVTX)**: Cannot correlate with queued events
- **Post-hoc attribution**: Requires complex timestamp correlation, error-prone

### What We Need

A lightweight mechanism for applications to inject phase markers directly into the profiler event stream, ensuring correct attribution with negligible overhead.

## Proposed API

```c
ncclResult_t ncclNotifyTag(
    uint64_t tag,           // User-defined metadata (arbitrary uint64)
    ncclComm_t comm,        // Communicator (may be NCCL_COMM_NULL)
    cudaStream_t stream     // CUDA stream (may be 0)
);
```

Profiler plugin extension:
```c
typedef enum {
    ncclProfilerEvent_NcclOp = 0,
    ncclProfilerEvent_ProxyOp = 1,
    ncclProfilerEvent_ProxyStep = 2,
    ncclProfilerEvent_UserTag = 3,     // NEW
} ncclProfilerEvent_t;

typedef struct {
    uint64_t tag;           // User-provided metadata
    uint64_t timestamp_ns;  // Timestamp when recorded
    int rank;               // Rank that generated tag
    ncclComm_t comm;        // Communicator (may be NULL)
} ncclProfilerUserTagInfo_v1_t;
```

## Use Cases

### 1. Phase Tracking

```c
#define PHASE_FORWARD   0x1
#define PHASE_BACKWARD  0x2
#define PHASE_OPTIMIZER 0x3

for (int step = 0; step < num_steps; step++) {
    ncclNotifyTag(PHASE_FORWARD, comm, stream);
    forward_pass();

    ncclNotifyTag(PHASE_BACKWARD, comm, stream);
    backward_pass();

    ncclNotifyTag(PHASE_OPTIMIZER, comm, stream);
    optimizer_step();
}
```

Profiler receives tags in event stream and correlates with NCCL operations.

### 2. Debug Source Location Tracking

```c
ncclAllReduce(data, count, ncclFloat, ncclSum, comm, stream);
ncclNotifyTag(__LINE__, comm, stream);  // Mark: before sync
cudaStreamSynchronize(stream);
ncclNotifyTag(__LINE__, comm, stream);  // Mark: after sync
```

Correlate profiler events with source code without NCCL recompilation.

### 3. Custom Markers

Applications can define their own metadata schemes: checkpoint boundaries, microbatch markers, data loading phases, etc.

## Performance

**Per-call overhead**: ~13ns (parameter validation + timestamp + SPSC push)

**Training impact** (3 tags per iteration for phase tracking):
```
Tags per iteration:  3
Overhead:            3 * 13ns = 39ns
Typical iteration:   2600ms
Slowdown:            39ns / 2600ms = 0.0000015%
```

**Verdict**: Negligible (<0.001% even with heavy instrumentation)

## API Naming

**Proposed**: `ncclNotifyTag`
- Follows Linux kernel blktrace precedent (`blk_trace_note_message`)
- Short, consistent with NCCL style
- Clear intent

**Alternatives**: `ncclProfilerMarkTag`, `ncclProfilerMetadata`

Feedback welcome on preferred name.

## Implementation

I'm happy to implement this feature if the community finds it valuable. Seeking feedback on:

1. **API design**: Is `ncclNotifyTag` acceptable? Any concerns with proposed signature?
2. **Profiler versioning**: Should this be V5 API or extend V4?
3. **Stream association**: Should tags be stream-ordered or global?
4. **Alternative approaches**: Is there a better way to solve phase attribution?

## Benefits

- Solves phase attribution problem with minimal overhead
- Framework integration: PyTorch/JAX can annotate semantics
- Debug flexibility: Correlate traces with source code
- Backward compatible: Profilers ignore unknown events safely
- Extensible: Applications define custom metadata schemes

## References

- Linux blktrace: https://github.com/torvalds/linux/blob/master/include/uapi/linux/blktrace_api.h
- NCCL Profiler Plugin: https://github.com/NVIDIA/nccl/tree/master/ext-profiler

## Background

The phase attribution problem was discovered through detailed analysis of profiler event queue behavior in production ML training workloads. Key findings:
- Event queue lag: ~100ms (8000 events) between generation and processing
- Optimizer phase corruption: 50-90% for short phases (10-50ms duration)
- Impact: Makes optimizer performance analysis unreliable

This proposal solves the problem by allowing applications to inject phase markers into the event stream at the exact moment of phase transition, eliminating queue-induced misattribution.

## 评论 (6)

### gcongiu · 2025-12-12

@dmitry-monakhov, first of all thank you for your RFE! A few questions:

> When the training framework switches phases (e.g., backward -> optimizer), events still in the queue from the previous phase get misattributed to the new phase

1. What do you mean with "events still in the queue"? NCCL emits events to the profiler plugin as they happen, it does not queue them.

2. Do you mean that it is difficult for the framework to reliably assign NCCL operations to phases because of their host asynchronous nature?

3. Is that why you also have a stream argument in the `ncclNotifyTag` API? What is the intended usage of the stream?

# Feedback

> Is ncclNotifyTag acceptable? Any concerns with proposed signature?

Why not have a string tag instead of an integer? A string can capture a wider range of user attributes, not only phase identifiers and line numbers

> Should this be V5 API or extend V4?

For the user facing API we don't need versioning. We may need NCCL profiler plugin API updates to support the feature to propagate the user attribute to the profiler plugin.

```C
typedef struct {
  uint64_t type;
  void* parentObj;
  int rank;
  const char* userInfo;
  ...
} ncclProfilerEventDescr_v7_t;
```
Currently we are at v5 and we have some new feature for v6 in NCCL v2.29. So, this would be part of v7.

> Should tags be stream-ordered or global?

NCCL events are stream ordered. Since tags will be attached to NCCL events they will also be stream ordered. However, I would leave the stream in the signature because it can be useful to instrument kernels that use the NCCL device API.

> Is there a better way to solve phase attribution?

In NCCL v2.27 (if I am not mistaken) we introduced a name attribute for the communicator. Users can create communicators and give them meaningful names. The communicator name is propagated to the profiler plugin so that users can easily attribute collectives to a DP, TP, PP communicators, for example. We did not consider the training phase however. I would say this proposal bridges that gap.


### dmitry-monakhov · 2026-01-10

```bash
> [@dmitry-monakhov](https://github.com/dmitry-monakhov), first of all thank you for your RFE! A few questions:
> 
@gcongiu, thank you for the detailed feedback and questions!
> > When the training framework switches phases (e.g., backward -> optimizer), events still in the queue from the previous phase get misattributed to the new phase
> 
> 1. What do you mean with "events still in the queue"? NCCL emits events to the profiler plugin as they happen, it does not queue them.
```

You're absolutely right - NCCL calls profiler callbacks synchronously. The queue I referred to is **internal to the profiler plugin**, not NCCL itself. Apologies for the confusion in the original description.

High-performance profiler plugins typically use internal queues to minimize callback latency:

```
NCCL callback (hot path, ~10ns):
  -> Push event to internal SPSC queue
  -> Return immediately

Profiler daemon thread (background):
  -> Poll queue, batch events
  -> Export telemetry (file I/O, network, aggregation)
```

> 2. Do you mean that it is difficult for the framework to reliably assign NCCL operations to phases because of their host asynchronous nature?

Yes, but the specific problem is the **profiler-internal queue lag**, not NCCL's async nature per se. The framework knows exactly when phases change (it controls the training loop). The issue is:

```
T=0:    Framework sets phase=OPTIMIZER
        Queue contains 8000 events from BACKWARD phase

T=10ms: Profiler daemon processes queued events
        Reads current phase = OPTIMIZER
        Misattributes BACKWARD events to OPTIMIZER
```

The tag solves this by entering the queue at the exact phase boundary:

```
T=0:    Framework calls ncclNotifyTag(OPTIMIZER)
        Tag enters queue AFTER backward events, BEFORE optimizer events

T=10ms: Daemon processes queue
        Sees: [backward events...] [TAG:OPTIMIZER] [optimizer events...]
        Correctly attributes events based on tag position
```

This eliminates queue-induced misattribution entirely.

> 3. Is that why you also have a stream argument in the `ncclNotifyTag` API? What is the intended usage of the stream?

For the phase tracking use case, `stream=0` (global) is typical since phase changes apply to all streams. However, I agree with your point about keeping it for NCCL device API instrumentation and future flexibility.

> 
```bash
> # Feedback
> > Is ncclNotifyTag acceptable? Any concerns with proposed signature?
> 
> Why not have a string tag instead of an integer? A string can capture a wider range of user attributes, not only phase identifiers and line numbers
```

Excellent point. The original uint64_t proposal was admittedly influenced by my Linux kernel background where strings are bad habits :)

After looking at NVTX, I think we can have both: **registered string handles** (like `nvtxDomainRegisterStringA`).

**NVTX-style approach**:
```c
// Register strings once at init (amortized cost)
ncclStringHandle_t phase_fwd = ncclRegisterString(comm, "forward");
ncclStringHandle_t phase_bwd = ncclRegisterString(comm, "backward");

// Hot path uses handles (cheap - just uint64_t internally)
ncclNotifyTag(phase_fwd, comm, stream);
```

**Benefits**:
- Human-readable strings in profiler output
- Minimal hot-path overhead (handle is just uint64_t)
- Follows established NVTX pattern
- Handle can encode both raw integers AND registered strings

**Overhead comparison**:

| Approach | No-Tool | With-Tool |
|----------|---------|-----------|
| uint64_t | ~2ns | ~10-15ns |
| const char* raw | ~5ns + strlen | ~50-200ns |
| Registered handle | ~2ns | ~15-25ns |

For phase tracking (3 tags/iteration), all approaches have negligible impact. But registered handles give string flexibility without raw string overhead.

**Proposed encoding** (backward compatible):
```c
typedef uint64_t ncclStringHandle_t;
// Upper bits indicate type:
// 0x0... = raw integer (original proposal)
// 0x8... = registered string handle
```

This way profilers can support both use cases, and the API remains simple.

```bash
> > Should this be V5 API or extend V4?
> 
> For the user facing API we don't need versioning. We may need NCCL profiler plugin API updates to support the feature to propagate the user attribute to the profiler plugin.
> 
> typedef struct {
>   uint64_t type;
>   void* parentObj;
>   int rank;
>   const char* userInfo;
>   ...
> } ncclProfilerEventDescr_v7_t;
> Currently we are at v5 and we have some new feature for v6 in NCCL v2.29. So, this would be part of v7.
Understood. The v7 path works for us. Should I prepare a more detailed proposal for the profiler plugin API changes, or wait for v6 to land first?

> > Should tags be stream-ordered or global?
> 
> NCCL events are stream ordered. Since tags will be attached to NCCL events they will also be stream ordered. However, I would leave the stream in the signature because it can be useful to instrument kernels that use the NCCL device API.
> 
> > Is there a better way to solve phase attribution?
> 
> In NCCL v2.27 (if I am not mistaken) we introduced a name attribute for the communicator. Users can create communicators and give them meaningful names. The communicator name is propagated to the profiler plugin so that users can easily attribute collectives to a DP, TP, PP communicators, for example. We did not consider the training phase however. I would say this proposal bridges that gap.
```

Exactly - communicator naming answers "which communication group?" while phase tagging answers "which training phase?". Together they provide full semantic context:

- "AllReduce on DP communicator during backward phase"
- "AllGather on TP communicator during forward phase"

This enables per-phase, per-communicator analysis that neither feature provides alone.


### gcongiu · 2026-02-06

@dmitry-monakhov do you have a proof of concept for this feature that you can share in a PR? It would be easier to understand the feature by looking at some code.

### dmonakhov · 2026-03-10

@gcongiu PR is available here https://github.com/NVIDIA/nccl/pull/2045

### yfguo · 2026-07-21

Three commits landed on `dev` branch should address this RFE.
https://github.com/NVIDIA/nccl/commit/69e7c2c0c06f7744d7bde0c24e566a2b2ec84b99
https://github.com/NVIDIA/nccl/commit/0dab26429c5a0ef15339fe0285809721b67302bf
https://github.com/NVIDIA/nccl/commit/deb1f27a074afb3eb65106419168814655624563

### xiaofanl-nvidia · 2026-08-10

This will be released as part of 2.31 shortly. Closing. 

@dmonakhov please let us know if you see any issues when using this feature! Thank you for your RFE, which motivated us to add the collConfig feature. 

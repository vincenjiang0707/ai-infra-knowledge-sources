# [Issue #2416] [RFE]:Pluggable external device-memory allocator: hand all non-registration buffer classes to a framework-supplied allocator (e.g. PyTorch's caching allocator)

source: https://github.com/NVIDIA/nccl/issues/2416
state: open | updated: 2026-09-21T03:49:45Z
labels: enhancement

## 正文

## Background

In typical large-model training setups, the framework (PyTorch) and NCCL coexist in the same process but manage GPU memory through two completely independent paths:

- PyTorch's **caching allocator** grabs device memory eagerly and keeps it in a reserved pool. Freed tensors are returned to the pool, not to the driver. As a result `nvidia-smi` shows most of the GPU as occupied even when the *live* tensor footprint is small — the pool holds a large amount of physically-backed but logically-idle memory, especially between training steps.
- NCCL manages its own memory (channel buffers, P2P/IPC staging buffers, NVLS symmetric windows, proxy buffers, scratch/workspace) through its internal allocator, which since 2.19 defaults to `cuMem*`-based VMM allocations (`NCCL_CUMEM_ENABLE`), with a `cudaMalloc` fallback when VMM is unavailable.

Because these two allocators never share memory, the total footprint is roughly `max(framework need) + NCCL need + fragmentation`, not the true peak of either.

## Problem

The static partitioning of GPU memory between the framework pool and NCCL is a lose-lose trade-off, and it bites in both directions:

1. **Static headroom reservation wastes memory.** If you pre-reserve enough free memory for NCCL (e.g. by capping `PYTORCH_CUDA_ALLOC_CONF` / `gpu_memory_utilization` so the framework pool can't grow into it), that memory sits idle during compute-heavy phases. With modern 3D/4D parallelism the number of communicators per rank is large; community measurements put NCCL's footprint at 10–20 GB per GPU in large-scale training, which is a lot of permanently-carved-out capacity.
2. **Not reserving headroom causes hard failures.** If you let the framework pool grow freely, NCCL's internal allocations fail when it actually needs memory — `cuda failure 2 'out of memory'` from `include/alloc.h`, often in the middle of communicator init or the first large collective, long after the framework has committed its memory layout. This is a common and confusing failure mode in the wild (e.g. pytorch/pytorch#152302: NCCL OOM right after a PyTorch upgrade).
3. **The temporal structure is in NCCL's favor.** A large fraction of NCCL's memory (channel buffers, staging buffers) is only needed while collectives are in flight. Between training steps — during optimizer phases, host-side orchestration, checkpointing — the framework's pool is often holding tens of GB of *reserved-but-unused* memory while NCCL holds memory it isn't actively using either. Neither side can borrow from the other, so peak capacity is dictated by the sum of two non-overlapping lifetimes.
4. **NCCL memory is invisible to the framework.** Because NCCL allocates behind the framework's back, framework-level tooling — OOM diagnostics with full allocation stacks, `torch.cuda.memory` snapshots, memory profiling, expandable-segments defragmentation — sees a black hole. Users hit an OOM and cannot tell from framework telemetry that NCCL is the actual owner of the missing memory.

In short: **the memory exists on the device at almost every instant, but it is locked behind the wrong allocator.**

## Existing workarounds and why they fall short

- **`NCCL_CUMEM_ENABLE=0`**: makes NCCL fall back to plain `cudaMalloc`, which still bypasses the framework pool, so it doesn't solve sharing; it also historically trades away the memory benefits of VMM (this is why vLLM flips it off, not on, as a workaround).
- **PyTorch-side `MemPool` wrapping `ncclMemAlloc`** (`CUDAPluggableAllocator`, `backend.mem_allocator`): solves the *registration* problem (tensors allocated via `ncclMemAlloc` so they can be `ncclCommRegister`'d for NVLS/symmetric memory), but it moves framework tensors *into* NCCL's allocator — the opposite direction of what we need, and it constrains those allocations to VMM granularity rules.
- **External plugins that hook NCCL internals** (e.g. AMem): offload NCCL buffers to CPU pinned memory and restore them on demand. This works but requires patching NCCL's allocation/free/map call sites from the outside, is fragile across NCCL upgrades, and pays offload/restore latency; it exists precisely because NCCL exposes no supported interface for this.
- **Destroying and recreating communicators** to reclaim NCCL memory (used by some RL training frameworks that alternate training/inference phases): seconds of overhead per transition and loses connection warmup.

None of these lets NCCL memory live in the same accounting and physical-memory universe as the framework's.

## Proposal: pluggable external allocator for non-registration buffer classes

We'd like NCCL to support an **external device-memory allocator hook**, configured once at communicator initialization (and overridable per-communicator), and to route its *non-registration* allocation classes through it when set:

```c
typedef struct {
  void* ctx;
  // Called for every eligible allocation when set. Must return NULL on
  // failure; NCCL then applies the configured failure policy (below).
  void* (*alloc)(void* ctx, size_t size, int device, cudaStream_t stream);
  void  (*free)(void* ctx, void* ptr, size_t size, int device, cudaStream_t stream);
  // Optional: allow NCCL to round the request to a granularity the
  // allocator is comfortable with (e.g. PyTorch's 512B/2MB size classes).
  size_t (*roundSize)(void* ctx, size_t size);
} ncclExternalAllocator_t;

// In ncclConfig_t:
ncclExternalAllocator_t externalAlloc;            // 0-filled = current behavior
int externalAllocPolicy;                          // enum, see below
```

**Scope: all non-registration buffer classes.** This covers channel/staging buffers, proxy buffers, scratch/workspace, and any allocation that is consumed internally by NCCL kernels without being exported to peers as a P2P/IPC or NVLS/symmetric window. Explicitly **out of scope** for the hook: user-supplied buffers and registration arenas (`ncclCommRegister` / NVLS windows), which must keep the `ncclMemAlloc` VMM semantics (shared handles, recommended granularity, alignment). This keeps the hook simple: eligible memory is *only ever accessed by the local rank's own kernels*, so it does not need to satisfy any VMM/IPC/export invariant — ordinary `cudaMalloc`-equivalent memory is sufficient. The eligibility split should follow the code structure that already exists (e.g. `ncclCuMemAlloc` vs `ncclCudaMalloc` call sites), not introduce a new classification.

**Failure policy** (`externalAllocPolicy`), chosen by the integrator:

1. **External-only (default recommendation):** if the external allocator fails, NCCL fails, exactly as if its own allocator had failed. This maximizes framework visibility — the OOM surfaces inside the framework's own allocator, with full stacks and stats — and makes capacity planning a single-allocator problem.
2. **External-first with internal fallback:** NCCL falls back to its internal allocator when the external one returns NULL. This maximizes robustness (e.g. during early bootstrap before the framework pool is warm) at the cost of partially re-introducing the invisible-memory problem; useful as a transition mode.

Note this subsumes the narrower "fallback" ask: with an external allocator in place, *framework-idle pool memory is naturally what NCCL draws from*, and the framework's own OOM path governs what happens when the device is truly full. Fallback is a policy choice, not the mechanism.

**Framework-side integration.** PyTorch registers an allocator wrapping `c10::cuda::CUDACachingAllocator::raw_alloc` / `raw_delete`. Consequences:

- **Time-sharing instead of partitioning:** NCCL's non-registration footprint is allocated from (and returned to) the framework pool, so the device capacity is governed by the *peak concurrent* usage of the two workloads rather than the sum. Between-step idle pool memory genuinely becomes available to NCCL.
- **Full visibility:** NCCL allocations appear in memory snapshots and OOM reports with their size/stream; debugging "who took my memory" stops requiring `NCCL_DEBUG=INFO` forensics.
- **Defragmentation cooperation:** with PyTorch's expandable segments (VMM-backed) the pool can hand NCCL properly aligned, large physical mappings; NCCL freeing back to the pool lets expandable segments release/defrag around it.

**Safety constraints.**

- **Thread-safety / re-entrancy:** the external allocator may be invoked from NCCL's proxy threads and bootstrap threads; the contract must state which threads call it and that it must not call back into NCCL.
- **Stream ordering:** allocate/free should be treated as stream-ordered where the caller supplies a stream, or NCCL must insert the necessary synchronization before reuse.
- **Performance parity:** eligible buffers must not take extra syncs on the allocation path; if NCCL's internal path is async/stream-ordered, the hook should be too.
- **Attribution/telemetry:** extend `NCCL_DEBUG_SUBSYS=ALLOC` (or a new subsys) to report bytes routed through the external allocator vs. internal, so users can verify the hook is firing and reason about capacity.
- **Cleanup contract:** NCCL frees every external allocation before communicator destruction returns; a leaked external allocation is treated as an NCCL bug (assert in debug builds).

## Open questions for discussion

1. **Eligibility boundary precision.** Is "never exported to peers" the right line? Some buffers are locally accessed today but could be promoted to registered/NVLS paths by future features — should the eligibility be per-allocator-class opt-in (a bitmask in the config) rather than a hardcoded split?
2. **Asymmetric sourcing across ranks.** With external-only policy, rank 0's pool may serve NCCL while rank 3's pool is full. For eligible (non-exported) buffers this is safe per-rank, but does NCCL want a uniform accounting mode anyway (e.g. all ranks fall back together) to keep capacity reasoning simple at fleet level?
3. **Granularity.** PyTorch rounds to 512 B / 2 MB classes; NCCL often wants larger, alignment-friendly chunks. The `roundSize` callback lets the allocator advertise comfort — is a two-way negotiation (NCCL asks preferred granularity per allocation) worth it, or is a static round-up enough?
4. **Relationship to `ncclMemAlloc` / symmetric memory roadmap.** If NCCL later allows user buffer registration on framework-allocated VMM memory (per the ongoing PyTorch work on making expandable segments interoperate with VMM allocators), should the same hook eventually grow a "VMM-capable external allocator" mode, so one interface covers both classes? Or should registration memory stay permanently on `ncclMemAlloc` semantics?

## Why this is worth doing upstream

- It removes a whole class of OOM failures (NCCL-vs-framework memory contention) that currently require per-framework hacks to avoid.
- It recovers memory that is physically present but stranded: with 10–20 GB of NCCL footprint per GPU at scale, time-sharing the framework pool and NCCL buffers is a meaningful effective-capacity win, especially for frameworks that alternate phases (RLHF-style train/inference colocation, elastic training with variable degree).
- It makes NCCL's memory a first-class citizen of framework observability (snapshots, OOM stacks, profiling) instead of a black hole.
- It replaces fragile external hooking projects with a supported interface, and is strictly additive: with the hook unset, behavior is bit-for-bit today's.

## 评论 (4)

### alpha-baby · 2026-09-17

We have a requirement. Could the NCCL team evaluate whether it can be supported? @xiaofanl-nvidia 

### 0z5a · 2026-09-19

@zjjott I'd be interested in helping with a scoped part of this RFE.

Instead of trying to make every NCCL device allocation externally pluggable at once, I'd like to start by classifying the internal allocation sites by lifetime and requirements — especially whether they require registration, IPC/export, symmetric addressing, or transport-specific ownership.

### xiaofanl-nvidia · 2026-09-21

Hi @zjjott @alpha-baby Thanks for raising the RFE. We'll discuss the painpoints and ideas. 

FWIW I think the RFE has merits but we will have to cross check everything (current problem statement, design assumptions, framework dependencies and roadmap alignment etc) with internal experts and framework teams, and get back to you. 

Do you have any functional prototype with e2e value demonstrations that can be shared with us? 

### zjjott · 2026-09-21

@xiaofanl-nvidia OK, that works. I'll need some time to build a functional prototype that demonstrates the framework's behavior and NCCL memory footprint when running with long sequences across multiple GPUs. I will share it once ready.

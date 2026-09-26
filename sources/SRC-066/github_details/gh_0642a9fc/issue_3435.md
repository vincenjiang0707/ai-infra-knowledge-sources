# [Issue #3435] tcgen05.alloc/dealloc.cta_group::2: deterministic unspecified launch failure when one CTA deallocs before the peer's alloc completes (sm_103a)

source: https://github.com/NVIDIA/cutlass/issues/3435
state: open | updated: 2026-09-05T02:19:45Z
labels: inactive-30d

## 正文

## Summary

On sm_103a (B300), if one CTA of a cluster pair executes `tcgen05.dealloc.cta_group::2`
before the peer CTA's `tcgen05.alloc.cta_group::2` has completed, the kernel fails with
`unspecified launch failure`. This is **deterministic**: baseline **25/25** failures, while
inserting a `barrier.cluster` anywhere between `alloc` and `dealloc` gives **0/25** in all
three placements tested. Reproduced identically on **8/8 physical GPUs** (96/96 vs 0/96).

`cute::TMEM::Allocator2Sm` documents no cross-CTA timing/ordering precondition, and I could
not find one in the parts of the PTX ISA I was able to consult (see "Open question" below).
All documented preconditions for both `allocate()` and `free()` are satisfied by the
reproducer.

I am filing this as a **standalone, reproducible defect report**. I am *not* claiming it
explains any other issue — see "Relation to a separate production hang" at the end.

## Environment

| Item | Value |
| --- | --- |
| GPU | NVIDIA B300 SXM6 (sm_103) |
| Toolkit | CUDA 13.0, V13.0.88 |
| Compile | `nvcc -gencode arch=compute_103a,code=sm_103a` |
| CUTLASS | `147f5673d0c1c3dcf66f78d677fd647e4a020219` |

## Reproducer

Self-contained; emits the PTX directly so it does not depend on CUTLASS headers.

```cuda
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cuda_runtime.h>

__device__ __forceinline__ uint32_t smem_u32(void* p) {
  uint32_t r;
  asm volatile("{ .reg .u64 u; cvta.to.shared.u64 u, %1; cvt.u32.u64 %0, u; }"
               : "=r"(r) : "l"(p));
  return r;
}
__device__ __forceinline__ uint32_t ctarank() {
  uint32_t r; asm volatile("mov.u32 %0, %%cluster_ctarank;" : "=r"(r)); return r;
}
__device__ __forceinline__ void cluster_sync() {
  asm volatile("barrier.cluster.arrive.aligned;" ::: "memory");
  asm volatile("barrier.cluster.wait.aligned;"   ::: "memory");
}

// delay_cta: which CTA of the pair is delayed (0 = leader, 1 = follower, 2 = neither)
// mode: 0 = baseline
//       1 = barrier.cluster before alloc
//       2 = barrier.cluster after alloc (before relinquish)
//       6 = barrier.cluster immediately before dealloc
extern "C" __global__ void __cluster_dims__(2, 1, 1)
repro(uint32_t* out, uint32_t delay_cta, uint32_t spin, uint32_t mode) {
  __shared__ uint32_t tmem_addr;
  uint32_t rank = ctarank();
  uint32_t warp = threadIdx.x >> 5;
  if (threadIdx.x == 0) tmem_addr = 0;
  __syncthreads();

  if (rank == delay_cta) { for (uint32_t i = 0; i < spin; i++) __nanosleep(1000); }

  if (mode == 1) cluster_sync();

  if (warp == 0) {
    uint32_t dst = smem_u32(&tmem_addr);
    asm volatile("tcgen05.alloc.cta_group::2.sync.aligned.shared::cta.b32 [%0], %1;"
                 :: "r"(dst), "r"(512) : "memory");
  }
  __syncthreads();

  if (mode == 2) cluster_sync();

  if (warp == 0) {
    asm volatile("tcgen05.relinquish_alloc_permit.cta_group::2.sync.aligned;" ::: "memory");
  }
  __syncthreads();
  if (threadIdx.x == 0) out[rank] = tmem_addr;
  __syncthreads();

  if (mode == 6) cluster_sync();

  if (warp == 0) {
    asm volatile("tcgen05.dealloc.cta_group::2.sync.aligned.b32 %0, %1;"
                 :: "r"(tmem_addr), "r"(512) : "memory");
  }
}

int main(int argc, char** argv) {
  uint32_t dc = (argc > 1) ? atoi(argv[1]) : 1;      // delay follower by default
  uint32_t sp = (argc > 2) ? atoi(argv[2]) : 5000;
  uint32_t md = (argc > 3) ? atoi(argv[3]) : 0;

  uint32_t* d; cudaMalloc(&d, 4096);
  cudaLaunchConfig_t cfg = {};
  cfg.gridDim = dim3(2, 1, 1);
  cfg.blockDim = dim3(128, 1, 1);
  cudaLaunchAttribute a[1];
  a[0].id = cudaLaunchAttributeClusterDimension;
  a[0].val.clusterDim.x = 2; a[0].val.clusterDim.y = 1; a[0].val.clusterDim.z = 1;
  cfg.attrs = a; cfg.numAttrs = 1;

  if (cudaLaunchKernelEx(&cfg, repro, d, dc, sp, md) != cudaSuccess) {
    printf("launch failed\n"); return 2;
  }
  cudaError_t e = cudaDeviceSynchronize();
  printf("delay_cta=%u spin=%u mode=%u => %s\n", dc, sp, md, cudaGetErrorString(e));
  return (e == cudaSuccess) ? 0 : 1;
}
```

Build and run:

```bash
nvcc -gencode arch=compute_103a,code=sm_103a -o repro repro.cu
./repro 1 5000 0    # follower delayed, baseline    -> unspecified launch failure
./repro 0 5000 0    # leader   delayed, baseline    -> no error
./repro 1 5000 6    # follower delayed, barrier     -> no error
```

## Precondition audit

`Allocator2Sm::allocate()` (`include/cute/arch/tmem_allocator_sm100.hpp`):

| Documented `@pre` | Reproducer |
| --- | --- |
| Must be issued by a single fully active warp of the CTA | warp 0, all 32 lanes active |
| Must never be issued by more than one warp at the same time | only warp 0 issues |
| For repeated allocations, the same warp must be used | only one allocation |
| The 2 warps from participating CTAs have the same logical warp ID | warp 0 in both CTAs |

Plus the body text: *"Both CTAs must provide the exact same `dst_ptr` for correctness."* —
both CTAs take `cvta.to.shared` of the same static `__shared__` variable, so the CTA-local
offset is identical.

`Allocator2Sm::free()` (`tcgen05.dealloc`) documents three `@pre`: single fully active warp,
never more than one warp at a time, and the 2 warps from participating CTAs have the same
logical warp ID. All satisfied.

Notably, `free()` documents **no** requirement that the peer CTA's allocation must have
completed first — while its `@pre` referring to "the 2 warps from participating CTAs" does
imply `dealloc` is itself a CTA-pair collective.

## Results

### Asymmetry: only a late *follower* breaks

| Delayed CTA | Delay position | Result |
| --- | --- | --- |
| leader (rank 0) | before `alloc` | no error (tested up to `spin=50000`) |
| **follower (rank 1)** | **before `alloc`** | **`unspecified launch failure`** |
| follower (rank 1) | *after* `alloc` | no error |

The threshold is very low: `spin=0` passes, `spin=10` (~10 µs) fails 100%.

### Randomized ablation (N=25 per arm, run order shuffled, 100 runs total)

| Variant | Failures |
| --- | --- |
| baseline | **25/25 (100%)** |
| `barrier.cluster` before `alloc` | 0/25 |
| `barrier.cluster` after `alloc` | 0/25 |
| `barrier.cluster` immediately before `dealloc` | 0/25 |

Additional checks (3 runs each): removing `relinquish_alloc_permit` still fails 3/3, so
`relinquish` is not involved; removing `dealloc` removes the launch failure.

So the trigger is specifically **one CTA's `dealloc` running before the peer's `alloc`
completes**, and a cluster barrier anywhere between the two removes it.

### Cross-GPU control: not a single bad GPU or SM pair

Same host, 8× B300, all idle. Per GPU: baseline ×12 and the "barrier before `dealloc`"
variant ×12, run order shuffled.

| GPU | baseline failures | mitigated failures |
| --- | --- | --- |
| 0–7 (each) | **12/12** | 0/12 |

Total **96/96 vs 0/96** across 8 distinct physical GPUs.

Caveat: this is still one host and one architecture (sm_103a / B300); I have not tested
sm_100a or a second machine.

### Where it fails

Progress markers written to `cudaHostAllocMapped` memory survive the context teardown, so
they can be read from the host afterwards:

| Stage | CTA0 | CTA1 |
| --- | --- | --- |
| entered kernel / delay done / before `alloc` | reached | reached |
| **`alloc` returned** | reached | **not reached** |
| `relinquish` / `dealloc` / end | reached | not reached |

The failure therefore occurs **inside CTA1's `tcgen05.alloc.cta_group::2`**.

### Every instrument I have suppresses it

| Instrument | Result |
| --- | --- |
| none | **10/10 failures** |
| `cuda-gdb` attach | does not reproduce |
| `CUDA_ENABLE_COREDUMP_ON_EXCEPTION=1` | does not reproduce |

This is consistent with a timing-sensitive condition, but it also means I cannot localize
the faulting PC myself. `compute-sanitizer` is not available in the container image I am
using.

## Questions

1. Is there an **undocumented cross-CTA ordering requirement** for
   `tcgen05.alloc.cta_group::2` / `tcgen05.dealloc.cta_group::2` — e.g. that the pair must
   not have one CTA proceed to `dealloc` while the peer is still inside `alloc`? If so, it
   would be worth stating in the PTX ISA and in the `Allocator2Sm` `@pre` list.
2. If there is no such requirement, this looks like a defect. Since every instrument
   available to me suppresses it, help localizing it would be very welcome.
3. Can the operand-level semantics of the `SYNCS.ARRIVE.TRANS64` suffixes
   (`.A1T0` / `.A0TR` / `.A0TX` / `.RED`) be confirmed? I derived a mapping by differential
   compilation (appendix) and would like authoritative confirmation.

## Open question I could not resolve

The precondition audit above is against the **CUTLASS docstrings**. I was not able to
retrieve the PTX ISA text for the `tcgen05.alloc` / `dealloc` /
`relinquish_alloc_permit` section itself, so if the ISA states a participation or ordering
constraint that the CUTLASS docstrings do not reflect, this report should be reframed as a
documentation gap rather than a defect. The reproduction facts are unaffected either way.

Separately, there appears to be an internal inconsistency worth checking: the
`allocate()` docstring begins *"Performs a non-blocking allocation of TMEM."*, while a
separate analysis I ran cited the PTX ISA describing `tcgen05.alloc` as a blocking
instruction. I cannot tell which is authoritative.

## Appendix: PTX → SASS mapping obtained by differential compilation

Feeding PTX with publicly defined semantics through the same `ptxas` and reading back the
generated SASS:

| PTX | Generated SASS |
| --- | --- |
| `mbarrier.arrive` | `SYNCS.ARRIVE.TRANS64.A1T0 RZ,[bar],RZ` |
| `mbarrier.arrive.expect_tx` | `SYNCS.ARRIVE.TRANS64 RZ,[bar],R0` |
| `mbarrier.expect_tx` | `SYNCS.ARRIVE.TRANS64.RED.A0TR RZ,[bar],R0` |
| `mbarrier.complete_tx` | `SYNCS.ARRIVE.TRANS64.RED.A0TX RZ,[bar],R0` |
| `mbarrier.try_wait.parity` | `SYNCS.PHASECHK.TRANS64.TRYWAIT P,[bar],R0` |

Reading `tcgen05.alloc.cta_group::2`'s lowering with that mapping — it splits into
leader/follower paths on `cta_id & 1`:

```text
CTA0 (leader)   UTCATOMSWS.2CTA.FIND_AND_SET.ALIGN      allocate (spin + NANOSLEEP)
                SYNCS.ARRIVE.TRANS64.RED [peer], 4      expect_tx(4) + arrive on peer's barrier
                STAS [peer_smem], addr                  async store of the TMEM address

CTA1 (follower) SYNCS.PHASECHK.TRANS64.TRYWAIT [own+8]  wait on its own barrier
                LDS [tmem_addr]                         read the address
                SYNCS.ARRIVE.TRANS64.RED.A1T0 [peer]    plain ack
```

This was cross-checked instruction by instruction against the shipped cubin (17 offsets
plus instruction counts), not only against a rebuild.

## Relation to a separate production hang: not established

I also track an intermittent **hang** (roughly once every few hours) in a production
inference workload that exercises the same `tcgen05` / `Allocator2Sm` path
(vllm-project/vllm#51035). **I am not claiming the two share a root cause**, because:

- this reproducer produces a **device fault**, whereas production **hangs** — different
  manifestations;
- in this reproducer the follower's `alloc` eventually **does** complete; in the production
  capture it **never** completed;
- adding production-like structure to the reproducer (keeping the post-`alloc` cluster
  barrier, adding TMEM contention, many clusters) did **not** reproduce the production
  shape — delay stages 0/1/2, 128/256/512 columns, and 74 and 148 clusters all passed
  cleanly;
- a paired CUDA-graph A/B (fixed kernel, grid, block, SMEM and input addresses; only
  capture/replay varied; 30 runs per arm) showed 0 faults and 0 hangs in both arms.

Please treat this report as an independent defect. The production hang is tracked
separately.


## 评论 (1)

### github-actions[bot] · 2026-09-05

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

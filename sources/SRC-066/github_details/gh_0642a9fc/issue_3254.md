# [Issue #3254] [BUG] Wrong TV Layout C in MMA Atom

source: https://github.com/NVIDIA/cutlass/issues/3254
state: open | updated: 2026-09-19T04:16:21Z
labels: bug, ? - Needs Triage, inactive-30d, inactive-90d, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

**Describe the bug**
When N equals 8, the SM90 WGMMA Atom has an incorrect TV Layout C.

**Steps/Code to reproduce bug**
```
import cutlass
import cutlass.cute as cute
import cutlass.utils.hopper_helpers as sm90_utils

@cute.jit
def make_mma(N: cutlass.Constexpr):
    tiled_mma = sm90_utils.make_trivial_tiled_mma(
        cutlass.Float16,
        cutlass.Float16,
        cute.nvgpu.OperandMajorMode.K,
        cute.nvgpu.OperandMajorMode.K,
        cutlass.Float32,
        (1, 1, 1),
        tiler_mn=(64, N),
    )
    print(tiled_mma)

if __name__ == '__main__':
    make_mma(8)
    make_mma(16)
    make_mma(32)
    make_mma(64)

```

**Expected behavior**
Wrong Result:
```
Tiled MMA
  Thr Layout VMNK: (128,1,1,1):(1,0,0,0)
  Permutation MNK: (_,_,_)
MMA Atom
  ThrID:           128:1
  Shape MNK:       (64,8,16)
  TV Layout A:     (128,(64,16)):(0,(1,64))
  TV Layout B:     (128,(8,16)):(0,(1,8))
  TV Layout C:     ((4,8,4),(2,2)):((128,1,16),(64,8))
```
Right Result:
```
Tiled MMA
  Thr Layout VMNK: (128,1,1,1):(1,0,0,0)
  Permutation MNK: (_,_,_)
MMA Atom
  ThrID:           128:1
  Shape MNK:       (64,8,16)
  TV Layout A:     (128,(64,16)):(0,(1,64))
  TV Layout B:     (128,(8,16)):(0,(1,8))
  TV Layout C:     ((4,8,4),(2,2,1)):((128,1,16),(64,8,512))
```
Reference Code: https://github.com/NVIDIA/cutlass/blob/982cb9e718bcd4d7ac546b1795702a08326dfe4b/include/cute/atom/mma_traits_sm90_gmma.hpp#L432-L435

**Environment details (please complete the following information):**
 - nvidia-cutlass-dsl            4.5.1
 - nvidia-cutlass-dsl-libs-base  4.5.1
 - nvidia-cutlass-dsl-libs-cu13  4.5.1

**Additional context**
None.


## 评论 (7)

### shubaoyu2 · 2026-05-21

I think it should be an implementation choice, can you explain more why it's a bug and in which case it will cause an e2e kernel error?

### zhils · 2026-05-21

I believe this is indeed a bug rather than an implementation choice. Here's why:

**Reference in C++ CuTe** ([mma_traits_sm90_gmma.hpp#L432-L435](https://github.com/NVIDIA/cutlass/blob/main/include/cute/atom/mma_traits_sm90_gmma.hpp#L432-L435)):

```cpp
template<int N>
using CLayout_64xN = Layout<
    Shape <Shape <  _4, _8, _4>, Shape <_2, _2, Int<N/8>>>,
    Stride<Stride<_128, _1,_16>, Stride<_64, _8,   _512>>>;

using CLayout_64x8   = CLayout_64xN<  8>;   // Shape: ((4,8,4),(2,2,1))
using CLayout_64x16  = CLayout_64xN< 16>;   // Shape: ((4,8,4),(2,2,2))
```

The C++ implementation intentionally uses `Int<N/8>` rather than conditionally dropping the dimension — even when N=8 and `N/8=1`. This is not an oversight: the trailing `Int<1>` dimension (and its corresponding stride `_512`) is part of the accumulator layout's structural invariant across all N values. Removing it when `N/8 == 1` creates an inconsistency between the TV Layout and the underlying register allocation.

**Practical impact:** When `tv_layout_C` is `((4,8,4),(2,2))` instead of `((4,8,4),(2,2,1))`, layout algebra operations like `composition` and `make_fragment_C` may produce incorrect results because the layout rank doesn't match what the MMA atom internally expects.

The fix should be targeted at the MLIR `MmaAtomSM90Type` construction path that canonicalizes away the size-1 dimension when `N/8 == 1`.

I'd like to work on a fix for this. Could you assign this issue to me?

### shubaoyu2 · 2026-05-21

1. cutedsl doesn't guarantee to be identical with cute cpp.
2. can you give a **practical** minimal reproducible example to demonstrate?

I don't consider it a bug because what you said is still an implementation choice. we could consider to be align with cute cpp in next release, but it's not a must

### ccecka · 2026-05-21

This is not a bug and the ranks of the T-mode and V-mode have no semantic meaning in either C++ or CuTeDSL.

### HydraQYH · 2026-05-22

@shubaoyu2 @ccecka Dropping the dimension will cause an error:
```
[Error] MLIRError: Verification failed:
error: "cute.gemm("("/data00/qiyuhang/cutlass/examples/python/CuTeDSL/cute/hopper/kernel/dense_gemm/dense_gemm_persistent.py":886:20): 'cute.gemm' op invalid layout of A/B/D. A: (1,2):(0,512), B: (1,1):(0,0), D:((2,2),2,1):((1,2),4,0)
 note: "cute.gemm("("/data00/qiyuhang/cutlass/examples/python/CuTeDSL/cute/hopper/kernel/dense_gemm/dense_gemm_persistent.py":886:20): see current operation: "cute.gemm"(%720, %arg27, %726, %730, %arg27) <{operandSegmentSizes = array<i32: 1, 1, 1, 1, 1>}> : (!cute.tiled_mma<!cute_nvgpu.sm90.mma<64x8x16, ab_major = (k, k), elem_type = (f16, f16, f32), frag_kind = ss>, atom_layout_MNK = <"(1,1,1):(0,0,0)">>, !cute.memref<f32, rmem, align<32>, "((2,2),2,1):((1,2),4,0)">, !cute_nvgpu.smem_desc_view<!cute_nvgpu.smem_desc, "(1,2):(0,512)">, !cute_nvgpu.smem_desc_view<!cute_nvgpu.smem_desc, "(1,1):(0,0)">, !cute.memref<f32, rmem, align<32>, "((2,2),2,1):((1,2),4,0)">) -> ()
```

### github-actions[bot] · 2026-06-21

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-09-19

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

# [Issue #2787] [QST] Where is the actual MMA (a * b + c) implemented for SM70 SIMT convolution kernels?

source: https://github.com/NVIDIA/cutlass/issues/2787
state: closed | updated: 2026-09-20T16:49:33Z
labels: question, ? - Needs Triage, inactive-30d, inactive-90d

## 正文

Hi, I’m using CUTLASS on an SM70 GPU to implement 2D convolutions via the implicit GEMM path, and I’m trying to understand precisely **where** the multiply–accumulate at the elemental level (`a * b + c`) is implemented in the source code for my configuration.

My setup:

* Architecture: **SM70**
* Convolution: `conv2d_fprop` using the implicit GEMM kernel
  (`cutlass::conv::kernel::ImplicitGemmConvolution` from
  `include/cutlass/conv/kernel/implicit_gemm_convolution.h`)
* Kernel name observed in Nsight Systems: something like
  `cutlass_sm70_simt_sfprop_optimized_128x128_8x2_nhwc_align1`
  (so it’s a **SIMT** conv kernel, not TensorOp-based)

From the documentation and code I understand:

* The high-level conv kernel is `ImplicitGemmConvolution`, which uses a threadblock-level MMA (e.g. `ImplicitGemmPipelined` / `ImplicitGemmMultistage`) that in turn calls a warp-level MMA such as `gemm::warp::MmaSimt` in `include/cutlass/gemm/warp/mma_simt.h`.
* At the lowest level, `include/cutlass/arch/mma.h` defines `cutlass::arch::Mma` and provides a specialization for `GemmShape<1,1,1>, 1` where you can clearly see `d[0] = a[0] * b[0] + c[0];`.
* For SM70, `include/cutlass/arch/mma_sm70.h` adds architecture-specific specializations of `arch::Mma` for TensorCore shapes. However, there is no obvious `a * b + c` in plain C++ there; it seems to be implemented through WMMA / `mma.sync` intrinsics.

My questions are:

1. **For a SIMT convolution kernel on SM70** like `cutlass_sm70_simt_sfprop_optimized_128x128_8x2_nhwc_align1`, which **concrete `Mma` implementation** is actually instantiated and used?

   * Is the elemental `a * b + c` coming from a SIMT path in `gemm::warp::MmaSimt` / `gemm::thread::Mma` (with FFMA instructions), completely bypassing `arch::Mma`?
   * Or is there still an `arch::Mma<...>` specialization involved even for the SIMT kernels?

2. In other words, if I want to **instrument or modify the point where each element of the A and B tiles is multiplied and accumulated into C** (for research on masking / fault tolerance), what is the recommended spot in the codebase for an SM70 SIMT conv kernel?

   * `arch/mma.h` (the `GemmShape<1,1,1>, 1` specialization) seems more like a reference / fallback.
   * `arch/mma_sm70.h` appears to target TensorOps rather than SIMT.
   * Should I instead focus on the SIMT micro-kernels under `include/cutlass/gemm/warp/mma_simt.h` (or related thread-level MMA code) for this architecture and kernel type?

3. Finally, is there a canonical “call chain” for the SIMT implicit GEMM conv kernels (e.g. `ImplicitGemmConvolution → ImplicitGemmPipelined/Multistage → gemm::warp::MmaSimt → [thread-level MMA]`) that you recommend following if we want to understand or alter the per-element MMA behavior?

Any clarification or pointers to the relevant specializations/files for the SM70 SIMT path would be very helpful. Thanks a lot for maintaining CUTLASS and for any guidance you can provide!



## 评论 (2)

### github-actions[bot] · 2025-12-20

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-03-20

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

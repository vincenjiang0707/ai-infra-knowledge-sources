# [Issue #211] Query on performance-modeling of MoE Grouped GEMM

source: https://github.com/deepseek-ai/DeepGEMM/issues/211
state: closed | updated: 2025-10-09T08:17:43Z
labels: 

## 正文

### Background

Grouped GEMMs are unlike a _vanilla_ GEMM (a single _GEMM problem_ in a grouped GEMM could be considered a _vanilla_ GEMM).

If `M` is the value of M-dimension of a GEMM problem (`A` is sized `[M, K]`, and `B` is sized `[M, N]`), and `B_M` is the block-level tile size's M dimension, then for a single GEMM problem, M-occupancy is computed like this:

Actual number of tiles used = `(M + B_M - 1) / B_M`
Tiles needed to fit `M` = `M / float(B_M)`
M-occupancy = `Tiles needed to fit M`/`Actual number of tiles used`

For a single GEMM, if `M` is large, we typically choose `B_M` such that M-occupancy is 1, or close to 1, if `M` is not a multiple of `B_M`.

For a Grouped GEMM, specifically the one used in MoEs, the `M` dimension of each expert may vary a lot if load-balancing is not used to route tokens to experts.

As an example, we may end up with `M` dimension per expert in an MoE layer like,
```
// 32 experts
  {4, 1026, 1799, 166, 694, 753, 0, 16, 0, 240, 1119, 19, 6, 0, 46, 659, 10, 0, 112, 808, 181, 0, 28, 22, 90, 0, 176, 0, 37, 5, 10, 22},
```

If we choose the same tiling scheme for all GEMM problems of a grouped GEMM, then with values as divergent as the ones above, we would have low M-occupancy if we choose `B_M` such as `256`, `128`, which would result in a significant proportion of compute being wasteful.

However, choosing a smaller `B_M` would result in lower arithmetic intensity, which may slow down compute.

### Question

In your experience, if we use the same tiling scheme to compute all the GEMM problems in a grouped GEMM for MoE (without load-balancing), is the traditional roofline model still helpful in determining what the ideal latency should be? Or do you account for low `M occupancy` somehow, and adjust the roofline accordingly?

Thank you!







## 评论 (1)

### sanchitintel · 2025-10-09

Will choose a more appropriate place to ask this question. Thanks!

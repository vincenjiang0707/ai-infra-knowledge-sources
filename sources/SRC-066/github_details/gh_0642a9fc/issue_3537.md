# [Issue #3537] Blockwise-scaled split-K GEMM applies slice-0 scale factors to every K slice

source: https://github.com/NVIDIA/cutlass/issues/3537
state: open | updated: 2026-09-12T02:54:13Z
labels: CUTLASS C++

## 正文

### Description

Blockwise-scaled GEMM applies the wrong scale factors for every split-K slice beyond the first: the scale lookup uses the CTA-local K-tile index and is never offset by the slice's position in the global K range.

The multistage mainloop indexes the scale tensors by `k_iter_idx`, the loop counter local to this threadblock:

```cpp
// include/cutlass/gemm/threadblock/mma_multistage_blockwise.h:243-250
int ldA = int(scale_A.layout().stride(0));
int k_block_idx = k_iter_idx;
if (k_block_idx >= ldA) {
  k_block_idx = ldA - 1;                       // clamps OOB reads only
}
float scale_factor = scale_A.at({block_m_idx, k_block_idx}) *
                     scale_B.at({block_n_idx, k_block_idx});
```

and the kernel passes only the M/N tile offsets down to the MMA:

```cpp
// include/cutlass/gemm/kernel/gemm_universal_blockwise.h:268-273
mma(gemm_k_iterations, accumulators, iterator_A, iterator_B, accumulators,
    params.scale_A, params.scale_B, threadblock_tile_offset.m(),
    threadblock_tile_offset.n());
```

There is no `threadblock_tile_offset.k()` contribution anywhere, so slice `s` (which multiplies A/B blocks from global K range `[s * tiles_per_slice, (s+1) * tiles_per_slice)`) scales all of its partial products with the scale factors of K-blocks `[0, ...)`. The clamp at line 245 turns out-of-range lookups into silent reuse of the last scale block instead of a diagnostic.

The wrapper accepts this configuration when `kSplitKSerial` is true (`device/gemm_blockwise.h:367-369` rejects `split_k_slices > 1` only for the non-serial path), so the mis-scaled result is returned as success.

### Suggested fix

Offset the scale index by the slice's global K-tile base (`threadblock_tile_offset.k() * gemm_k_size / ThreadblockShape::kK`, or equivalent) before indexing `scale_A`/`scale_B`, keeping the existing clamp as a bounds guard.


## 评论 (1)

### amacharla15 · 2026-09-12

Opened #3615 with a reproduction and a fix. With split_k_slices=2 on SM89 the observed value was 1280 against an expected 10880, matching slice 1 re-applying K-blocks 0 and 1. The existing SM89 blockwise test uses K=128 with a single scale block and no split-K, so it can't catch this  ; the PR adds coverage.

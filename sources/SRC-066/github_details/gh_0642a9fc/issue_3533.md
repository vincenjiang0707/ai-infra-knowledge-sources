# [Issue #3533] Sparse split-K kernels offset the E operand without the kElementsPerElementE division

source: https://github.com/NVIDIA/cutlass/issues/3533
state: open | updated: 2026-09-13T04:19:00Z
labels: CUTLASS C++

## 正文

### Description

`SparseGemmSplitKParallel`-style serial split-K in `include/cutlass/gemm/kernel/sparse_gemm.h` offsets the E (metadata) operand by the wrong amount for slices beyond the first:

```cpp
// sparse_gemm.h:237
cutlass::MatrixCoord tb_offset_E{
  threadblock_tile_offset.m() * Mma::Shape::kM,
  threadblock_tile_offset.k() * params.gemm_k_size / kSparse,   // missing / kElementsPerElementE
};
```

The E iterator's extent is expressed in packed element-E columns and divides twice (`sparse_gemm.h:269`, `problem_size_k / kSparse / kElementsPerElementE`), and the sibling kernel `gemm_sparse_universal.h:622` divides twice as well when offsetting:

```cpp
cutlass::MatrixCoord tb_offset_E{
  threadblock_tile_offset.m() * Mma::Shape::kM,
  offset_k / kSparse / kElementsPerElementE,
};
```

With the missing division, every K-slice `>= 1` of a split-K sparse GEMM starts its metadata reads far past the end of the packed E tensor; all accesses are predicated off and the slice runs on zero-filled (invalid) metadata.

Concrete numbers: fp16 (`kElementsPerElementE == 2`), K=128, `split_k_slices = 2`: slice 1 has an E extent of 4 columns while its offset column is 32. Zero valid accesses.

The same formula is duplicated in two more copies of this kernel body:
- `sparse_gemm_with_absmax.h:322`
- `sparse_gemm_with_visitor.h:153`

Reachability note: nothing in-tree exercises it (`device::SparseGemm` with `split_k_slices > 1`; example 15 uses one slice), so this is latent, but the wrapper accepts split-K (`device/sparse_gemm.h` passes `args.batch_count` through).

### Suggested fix

Divide by `kElementsPerElementE` in the offset at all three sites, matching `gemm_sparse_universal.h`:

```cpp
threadblock_tile_offset.k() * params.gemm_k_size / kSparse / kElementsPerElementE,
```


## 评论 (1)

### XFDG · 2026-09-13

Hi, I've submitted a fix in https://github.com/NVIDIA/cutlass/pull/3625.

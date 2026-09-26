# [Issue #3539] EllGemm ColumnMajor-output workspace sizing uses the unswapped problem shape and undersizes split-K semaphores

source: https://github.com/NVIDIA/cutlass/issues/3539
state: open | updated: 2026-09-13T04:11:50Z
labels: CUTLASS C++

## 正文

### Description

`device::EllGemm` computes its split-K semaphore workspace size from an unswapped problem shape, while `initialize()` builds the launch grid from the swapped one, so for rectangular problems on ColumnMajor outputs the workspace is sized for a different grid than the one that runs.

```cpp
// include/cutlass/gemm/device/ell_gemm.h:747-753  (get_workspace_size)
cutlass::gemm::GemmCoord tiled_shape = threadblock_swizzle.get_tiled_shape(
  args.problem_size,                       // (m, n, k)
  {ThreadblockShape::kM, args.ell_blocksize, ThreadblockShape::kK},
  args.split_k_slices);
...
bytes += sizeof(int) * size_t(tiled_shape.m()) * size_t(tiled_shape.n());

// include/cutlass/gemm/device/ell_gemm.h:768-773  (initialize)
cutlass::gemm::GemmCoord grid_shape = threadblock_swizzle.get_tiled_shape(
  {args.problem_size.n(), args.problem_size.m(), args.problem_size.k()},   // transposed
  {ThreadblockShape::kM, args.ell_blocksize, ThreadblockShape::kK},
  args.split_k_slices);
```

The transpose is intentional at the launch site (the kernel consumes the swapped convention), but the sizing call must match it. Arithmetic example with `ThreadblockShape = 128x128x32`, `split_k_slices = 4`, `m = 264`, `n = 136`: sizing yields `tiled_shape.m() * n() = 15 * 2 = 30` semaphores (120 bytes after the ell-block N scaling), while the launched grid is built from `(136, 264)` and needs `18` tiles along one axis instead of `15`, i.e. more semaphore slots than were allocated and zeroed. The reverse aspect ratio over-allocates harmlessly; the bad direction gives an undersized, partially uninitialized semaphore buffer feeding split-K accumulation.

The RowMajor-output specialization does not swap and is consistent.

### Suggested fix

Pass the same swapped problem shape to `get_tiled_shape` inside `get_workspace_size`:

```cpp
threadblock_swizzle.get_tiled_shape(
  {args.problem_size.n(), args.problem_size.m(), args.problem_size.k()}, ...)
```


## 评论 (2)

### VaggelisGian · 2026-08-25

Correction to the numeric example: the second tile extent in `get_tiled_shape` is `ell_blocksize` (32), not `ThreadblockShape::kN`. With `m = 264, n = 136, split_k_slices = 4`, executed against the real swizzle class: sizing path gives `tiled_shape.m() * n() = 3 * 5 = 15` semaphores (60 bytes) while `initialize()`'s swapped grid needs `2 * 9 = 18` (72 bytes). The undersizing conclusion stands; the earlier 15/18-tile figures were mislabeled.

### XFDG · 2026-09-13

Hi, I've submitted a fix in https://github.com/NVIDIA/cutlass/pull/3624.

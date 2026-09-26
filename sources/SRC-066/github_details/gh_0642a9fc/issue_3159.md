# [Issue #3159] [CuTeDSL] make_tiled_mma SIGABRTs on hierarchical rank-3 atom_layout_mnk

source: https://github.com/NVIDIA/cutlass/issues/3159
state: open | updated: 2026-09-08T17:14:02Z
labels: inactive-30d, inactive-90d

## 正文

## Summary
`cute.make_tiled_mma` passes its Python-side rank check but crashes with SIGABRT inside the MLIR backend when given a rank-3 `atom_layout_mnk` whose M or N mode has a nested (hierarchical) shape. The equivalent layout works correctly in C++ CuTe.

## Environment
- `nvidia-cutlass-dsl` (pip, latest)
- GPU: NVIDIA RTX 5080 (SM 120 / Blackwell)
- CUDA 13.1, Python 3.12, Linux

## Minimal Repro
```python
import cutlass
import cutlass.cute as cute
from cutlass.cute import nvgpu

@cute.jit
def test():
    mma_op = cute.make_mma_atom(nvgpu.MmaUniversalOp(cutlass.Float32))

    # Flat rank-3 layout — works fine
    flat = cute.make_layout((16, 8, 1), stride=(1, 16, 0))
    tiled_mma_flat = cute.make_tiled_mma(mma_op, flat)
    cute.printf("flat ok, size = {}", cute.size(tiled_mma_flat))

    # Hierarchical rank-3 layout — crashes with SIGABRT
    hier = cute.make_layout(((8, 2), (4, 2), 1),
                             stride=((1, 32), (8, 64), 0))
    tiled_mma_hier = cute.make_tiled_mma(mma_op, hier)
    cute.printf("hier ok, size = {}", cute.size(tiled_mma_hier))

test()
```

## Expected
Both `make_tiled_mma` calls should succeed. This layout is the canonical way to express warp-structured thread tiling in CuTe C++ (e.g., warptiling SGEMM where `((NTM, NWM), (NTN, NWN))` encodes `NWM*NWN` warps each owning an `NTM*NTN = 32` thread subtile).

## Actual
```
python repro.py
# Aborted (core dumped), exit=134
```
No Python exception — the process dies inside MLIR type construction. Neither stderr nor any Python try/except catches it.

## Additional context
- `cute.make_layout(((8,2),(4,2)), stride=((1,32),(8,64)))` (rank-2 hierarchical) constructs fine outside `make_tiled_mma`, so the layout itself is valid.
- `make_tiled_copy_tv` accepts similar hierarchical shapes without crashing.
- C++ CuTe accepts the exact same shape/stride via \`make_layout(make_shape(make_shape(_8,_2), make_shape(_4,_2), _1), make_stride(...))\` and `make_tiled_mma` produces a working warp-structured MMA.
- `permutation_mnk` is not a workaround — it reshuffles atom value positions but cannot express warp groupings in the thread mapping (tested).

The DSL-side check at `cutlass/cute/atom.py:544` only validates `rank(atom_layout_mnk) != 3`, so hierarchical layouts pass through to MLIR which then asserts.

## 评论 (4)

### github-actions[bot] · 2026-05-10

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### thakkarV · 2026-05-11

@ccecka CC

### github-actions[bot] · 2026-06-10

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-09-08

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

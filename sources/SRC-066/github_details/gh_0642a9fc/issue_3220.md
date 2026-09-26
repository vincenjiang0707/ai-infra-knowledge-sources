# [Issue #3220] [QST] what exactly is MmaUniversalOp

source: https://github.com/NVIDIA/cutlass/issues/3220
state: closed | updated: 2026-09-24T09:29:08Z
labels: question, ? - Needs Triage, inactive-30d, inactive-90d

## 正文

its a bit unclear from the documentation of what exactly is the mmauniversalop, does it use tensor cores or the cuda cores itself?

```
mma_op = cute.nvgpu.MmaUniversalOp(cutlass.Float32)
    mma_atoms_layout = cute.make_layout((mma_m, mma_n, 1), stride=(mma_n, 1, 0))
    tiled_mma = cute.make_tiled_mma(
        mma_op,
        atom_layout_mnk=mma_atoms_layout,
    )
```

## 评论 (3)

### Austeritz-L · 2026-05-27

I think `MmaUniversalOp` does **not** use Tensor Cores.

My understanding is that, in CuTe DSL, `MmaUniversalOp` represents a generic scalar FMA MMA operation. It lowers to ordinary per-thread floating-point multiply-add work on the CUDA core / scalar FP pipeline, rather than warp-level Tensor Core MMA instructions.

For example, this code:

```python
mma_atom = cute.make_mma_atom(cute.nvgpu.MmaUniversalOp(cutlass.Float32))
cute.gemm(mma_atom, tCrC, tCrA, tCrB, tCrC)
```

can be understood as something similar to:

```python
for k in range(cute.size(tCrA)):
    tCrC[0] += tCrA[k] * tCrB[k]
```

That is, it performs regular scalar FMA accumulation.

If you want to use Tensor Cores on Ampere, you may want to use warp-level MMA ops, such as:

```python
cute.nvgpu.warp.MmaF16BF16Op(
    cutlass.Float16,
    cutlass.Float32,
    (16, 8, 8),
)
```

I also put a small example here for reference:

https://github.com/Austeritz-L/CuTeDSL-Tutorial/blob/main/Gemm/navie_sgemm.py

### github-actions[bot] · 2026-06-26

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-09-24

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

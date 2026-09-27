# [Issue #3281] [BUG] CuTeDSL 4.5.2: MmaFP8Op.make_fragment_A segfaults on SM120 (Blackwell)

source: https://github.com/NVIDIA/cutlass/issues/3281
state: open | updated: 2026-09-26T03:16:52Z
labels: bug, ? - Needs Triage, inactive-30d, inactive-90d, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

**Describe the bug**
`MmaFP8Op` segfaults during `cute.compile` on SM120 (Blackwell RTX 5090) when calling `make_fragment_A/B/C`. The same code works on Hopper (SM90) with `MmaFP8Op`, and on Blackwell with `MmaMXF8Op`.
Root cause: `MmaFP8Op._make_trait()` creates `MmaAtomSM89Type` (Ada SM89 MMA atom), which is incompatible with SM120's MLIR lowering passes — the fragment generator accesses SM89-specific fields that don't exist on the SM120 pipeline, causing a null pointer dereference in the C++ MLIR dialect library.
**Steps/Code to reproduce bug**
```python
import torch
import cutlass
import cutlass.cute as cute
import cutlass.torch as cutlass_torch
from cutlass.cute.runtime import from_dlpack
class TestKernel:
    MNK = (16, 8, 16)
    @cute.jit
    def __call__(self, a, b, c):
        op = cute.nvgpu.warp.MmaFP8Op(
            cutlass.Float8E4M3FN, cutlass.Float32, self.MNK)
        tmm = cute.make_tiled_mma(
            op, cute.make_layout((2, 2, 1)),
            permutation_mnk=(32, 16, 128))
        thr = tmm.get_slice(0)
        fA = tmm.make_fragment_A(thr.partition_A(a)[None, None, None, 0])
# Create tensors
a_ref = cutlass_torch.matrix(1, 128, 128, 'k', cutlass.Float32)
a_t, _ = cutlass_torch.cute_tensor_like(a_ref, cutlass.Float8E4M3FN, True, 16)
b_ref = cutlass_torch.matrix(1, 128, 128, 'k', cutlass.Float32)
b_t, _ = cutlass_torch.cute_tensor_like(b_ref, cutlass.Float8E4M3FN, True, 16)
c_ref = cutlass_torch.matrix(1, 128, 128, 'n', cutlass.Float32)
c_t, _ = cutlass_torch.cute_tensor_like(c_ref, cutlass.Float32, True, 16)
cute.compile(TestKernel(), a_t, b_t, c_t)   # ← SEGFAULT here
```

**Expected behavior**
Successful compilation. The same workflow works when replacing MmaFP8Op with MmaMXF8Op (block-scaled variant):
op = cute.nvgpu.warp.MmaMXF8Op(
    cutlass.Float8E4M3FN, cutlass.Float32, cutlass.Float8E8M0FNU)
**Environment details**
- GPU: NVIDIA GeForce RTX 5090 (SM120, Blackwell)
- nvidia-cutlass-dsl[cu13]: 4.5.2 (installed via pip)
- Python: 3.12
- PyTorch: 2.7.0
- CUDA: 12.8
- OS: Linux (x86_64, bare-metal)
**Additional context**
MLIR type mismatch identified:
MMA Op	MLIR Atom Type
MmaFP8Op	MmaAtomSM89Type (Ada)
MmaMXF8Op	MmaAtomSM120BlockScaledType (BL)
SM120 has native non-block-scaled FP8 MMA via tcgen05 instructions (MmaAtomSM100UMMAType in the dialect), but CuTeDSL 4.5.2 only exposes it at the warpgroup level — there is no warp-level wrapper. A new MmaFP8UMMAOp (or extending MmaFP8Op to select the correct MLIR atom type based on architecture) would resolve this.
Workaround: use MmaMXF8Op with fill(127) Ue8M0 scale factors to compute raw FP8×FP8 matmul, and apply true FP32 scale factors as a host-side post-process.

## 评论 (3)

### brandon-yujie-sun · 2026-05-29

@shubaoyu2 

### github-actions[bot] · 2026-06-28

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-09-26

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

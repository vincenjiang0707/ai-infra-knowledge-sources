# [Issue #3689] [BUG] mma_atom_call for mma.sync is eliminated if C is RZ

source: https://github.com/NVIDIA/cutlass/issues/3689
state: open | updated: 2026-09-27T09:38:56Z
labels: bug, ? - Needs Triage, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

**Describe the bug**
mma_atom_call for mma.sync is eliminated if C is zeroed independently, instead of reusing the fragment for D.

**Steps/Code to reproduce bug**

Remove the line ~`rD.store(rC.load())`~ `rD = rC` and the generated PTX will contain no code, i.e. the kernel is completely eliminated. Insert  ~`rD.store(rC.load())`~ `rD = rC`  then the result passes.~

Edit: The first version did not use `rC` in `mma_atom_call`, but the problem remains even if it is fixed, thanks to @yunweili3.
```
import torch
import cutlass
import cutlass.cute as cute
from cutlass.cute.runtime import from_dlpack

WARP_SIZE = 32
A_VALUES_PER_LANE = 8
B_VALUES_PER_LANE = 4
C_VALUES_PER_LANE = 4

@cute.kernel
def mma_sync_kernel(
    gA: cute.Tensor,
    gB: cute.Tensor,
    gC: cute.Tensor,
    mma_atom: cute.MmaAtom,
):
    lane, _, _ = cute.arch.thread_idx()
    rA = cute.make_rmem_tensor((A_VALUES_PER_LANE,), cutlass.BFloat16)
    rB = cute.make_rmem_tensor((B_VALUES_PER_LANE,), cutlass.BFloat16)
    rC = cute.make_rmem_tensor((C_VALUES_PER_LANE,), cutlass.Float32)
    rD = cute.make_rmem_tensor((C_VALUES_PER_LANE,), cutlass.Float32)
    cute.autovec_copy(gA[lane, None], rA)
    cute.autovec_copy(gB[lane, None], rB)
    rC.fill(0.0)

    # IMPORTANT :The current warp-MMA lowering incorrectly eliminates that separate-D/C form.
    rD = rC

    cute.mma_atom_call(mma_atom, rD, rA, rB, rC)
    cute.autovec_copy(rD, gC[lane, None])


@cute.jit
def run_mma_sync(gA: cute.Tensor, gB: cute.Tensor, gC: cute.Tensor):
    op = cute.nvgpu.warp.MmaF16BF16Op(
        cutlass.BFloat16,
        cutlass.Float32,
        (16, 8, 16),
    )
    mma_atom = cute.make_mma_atom(op)

    mma_sync_kernel(gA, gB, gC, mma_atom).launch(
        grid=(1, 1, 1),
        block=(WARP_SIZE, 1, 1),
    )


def main() -> None:
    if not torch.cuda.is_available():
        raise RuntimeError("An NVIDIA GPU with mma.sync support is required")

    # These shapes describe native [lane, lane_value] fragments, not ordinary
    # [M, K], [K, N], and [M, N] matrix layouts.
    a = torch.ones((WARP_SIZE, A_VALUES_PER_LANE), device="cuda", dtype=torch.bfloat16)
    b = torch.ones((WARP_SIZE, B_VALUES_PER_LANE), device="cuda", dtype=torch.bfloat16)
    c = torch.empty((WARP_SIZE, C_VALUES_PER_LANE), device="cuda", dtype=torch.float32)

    run_mma_sync(
        from_dlpack(a, assumed_align=16),
        from_dlpack(b, assumed_align=16),
        from_dlpack(c, assumed_align=16),
    )

    # With A=1, B=1, and K=16, all 128 values in the native C fragment are 16.
    torch.testing.assert_close(c, torch.full_like(c, 16.0), rtol=0.0, atol=0.0)
    print("PASS: one BF16 m16n8k16 mma.sync, every native C-fragment value is 16")
    print(c)


if __name__ == "__main__":
    main()
```

**Expected behavior**
The inserted ~`rD.store(rC.load())`~ `rD = rC` is redundant and should not affect the result.

**Environment details (please complete the following information):**
 - Environment location: Bare-metal
 - CuTeDSL version: 4.8.0, cu13
 - Torch version: 2.14.0

**Additional context**
Add any other context about the problem here.


## 评论 (2)

### yunweili3 · 2026-09-27

Reproduced on a B200 (DSL 4.8.0). With a separate register `C`, the MMA lowering writes the result into `C` and never writes `D`, so the store of `D` is dropped and the kernel is eliminated. This also affects `cute.gemm` and the universal FMA atom, not just `mma.sync`.

Note that removing `rD.store(rC.load())` as written leaves `mma_atom_call(atom, rD, rA, rB, rD)`, which reads uninitialized `rD`. The failing form is `mma_atom_call(atom, rD, rA, rB, rC)`.

Workaround in #3690 (copies `C` into `D` and accumulates in place; no PTX overhead). The lowering itself still needs a fix.


### melonedo · 2026-09-27

Reopen with fixed reproduction code

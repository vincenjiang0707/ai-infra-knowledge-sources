# [Issue #3234] [BUG] CuTe DSL StMatrix16x8x8bOp (b8) ICE: nvvm.stmatrix m16n8 lowering passes wrong register count to LLVM intrinsic

source: https://github.com/NVIDIA/cutlass/issues/3234
state: open | updated: 2026-09-24T14:37:44Z
labels: bug, ? - Needs Triage, inactive-30d, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

## Describe the bug

`StMatrix16x8x8bOp` (the b8 `stmatrix.m16n8` warp copy op) triggers an ICE during MLIR→LLVM IR translation. The `nvvm.stmatrix` lowering with `store_shape<m16n8>` emits a single `.x1` LLVM intrinsic call and forwards **all** register operands as arguments, instead of passing the correct number of registers per the `.x1` signature.

```
Incorrect number of arguments passed to called function!
  call void @llvm.nvvm.stmatrix.sync.aligned.m16n8.x1.trans.b8.p3(
      ptr addrspace(3) %14, i32 %19, i32 %20, i32 %21, ... i32 %34)
```

`stmatrix.m16n8.x1.b8` stores a 16×8 matrix of 8-bit elements (128 bytes, 4 bytes/thread = 1 i32), so the intrinsic expects `(ptr, i32)` — 2 arguments total. The DSL passes 17 (ptr + 16 × i32).

All `num_matrices` values (1, 2, 4) are affected — the lowering always emits `.x1` and never splits by `num_matrices`.

The corresponding **load** ops (`LdMatrix16x16x8bOp`, `LdMatrix16x8x8bOp`, `LdMatrix8x16x8bOp`) all work correctly for b8.

## Steps/Code to reproduce bug

```python
import cutlass
import cutlass.cute as cute
import cutlass.cute.nvgpu.warp as warp
import cutlass.utils as utils


class Repro:
    @cute.jit
    def __call__(self, dst: cute.Tensor):
        @cute.struct
        class SM:
            buf: cute.struct.Align[
                cute.struct.MemRange[cutlass.Float8E4M3FN, 16 * 8], 128]

        self.kernel(dst, SM).launch(
            grid=(1, 1, 1), block=(32, 1, 1), smem=SM.size_in_bytes())

    @cute.kernel
    def kernel(self, dst, SM: cutlass.Constexpr):
        alloc = utils.SmemAllocator()
        storage = alloc.allocate(SM)
        tid = cute.arch.thread_idx()[0]
        smem = storage.buf.get_tensor(
            cute.make_layout((16, 8), stride=(8, 1)))

        atom = cute.make_copy_atom(
            warp.StMatrix16x8x8bOp(transpose=True, num_matrices=1),
            cutlass.Float8E4M3FN)

        # Trivial TV: 1 warp group × 1 value rep = just the raw atom on 32 threads
        identity = cute.make_layout((1, 1), stride=(0, 0))
        tiled = cute.make_tiled_copy_tv(atom, identity, identity)
        tc = tiled.get_slice(tid)

        # Workaround https://github.com/NVIDIA/cutlass/issues/2902 —
        # partition_D drops SMEM alignment; reconstruct with assumed_align.
        part = tc.partition_D(smem)
        aligned = cute.make_tensor(
            cute.make_ptr(part.element_type, part.iterator.toint(),
                          cute.AddressSpace.smem, assumed_align=16),
            part.layout)

        reg = cute.make_fragment_like(aligned)
        cute.copy(tiled, reg, aligned)  # ← ICE here


import torch
from cutlass.torch import from_dlpack

dst = torch.zeros(16, 8, device="cuda", dtype=torch.float8_e4m3fn)
dst_cute = from_dlpack(dst.view(torch.int8).detach(), assumed_align=16)
dst_cute.element_type = cutlass.Float8E4M3FN

cute.compile(Repro(), dst_cute)
```

## Expected behavior

The kernel compiles and runs successfully, emitting valid `stmatrix.sync.aligned.m16n8.x1.trans.b8` PTX instructions.

## Environment details

- **Environment location:** Bare-metal
- **GPU:** SM120
- **nvidia-cutlass-dsl:** 4.5.0
- **torch:** 2.8.0+cu128
- **CUDA toolkit:** 12.8
- **Python:** 3.13

## Additional context

- All three `num_matrices` values (1, 2, 4) accepted by `StMatrix16x8x8bOp` produce the same ICE. The generated MLIR always shows a single `nvvm.stmatrix` op with `store_shape<m16n8>` and all registers bundled into one call.
- The b8 **load** counterparts (`LdMatrix16x16x8bOp`, `LdMatrix16x8x8bOp`, `LdMatrix8x16x8bOp`) all compile and execute correctly — the bug is specific to the **store** lowering path.
- The `assumed_align=16` workaround for the SMEM pointer is needed due to #2902 (`partition_S`/`partition_D` dropping alignment for b8 stride-1 layouts). This is a separate issue and is not the cause of the ICE.


## 评论 (4)

### github-actions[bot] · 2026-06-14

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-09-12

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

### 0z5a · 2026-09-24

Hi @16bit-ykiko ,I would like take this.

I'll first reproduce the `StMatrix16x8x8bOp` failure on current main / the latest CuTe DSL stack on SM120, then isolate where the register-count mismatch is introduced.

The investigation will cover:

* `num_matrices = 1 / 2 / 4`;
* CuTe/NVVM IR -> LLVM IR -> PTX to identify the first incorrect representation;
* the expected `.x1/.x2/.x4` register grouping and intrinsic signatures;
* bit-exact register -> shared-memory validation once the lowering compiles;
* SM120 hardware coverage on RTX 5090.

If the CuTe IR is already correct and the issue is in the downstream NVVM/LLVM lowering, I'll reduce it to the smallest reproducer and keep any CUTLASS-side change limited to what belongs in this repository rather than working around the compiler issue at a higher level.


### 0z5a · 2026-09-24

Draft #3667 adds early validation for incomplete atom thread groups. On RTX 5090 with CuTeDSL 4.8, b8 x1/x2/x4 readback is bit exact across 1/2/4 warps and 1/3 CTAs, with clean memcheck and racecheck results.


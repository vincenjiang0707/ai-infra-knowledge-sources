# [Issue #3420] [BUG] NVVM compiler crash (no diagnostics) on sm_100f  `tcgen05.ld` `.x64` + `warpgroup_reg_dealloc` (`setmaxnreg`)

source: https://github.com/NVIDIA/cutlass/issues/3420
state: closed | updated: 2026-09-01T07:07:22Z
labels: bug, ? - Needs Triage, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

`cute.compile` of a small, valid CuTe DSL kernel fails in the NVVM backend that is statically linked into the `nvidia-cutlass-dsl` 4.6.1 wheel, with no actionable diagnostics:

```
cutlass.base_dsl.compiler.CompilerDiagnosticError: error: NVVM backend compilation failed
  error: libNVVM failed while compiling generated device IR.
  note: target architecture: sm_100a
  note: backend log:
        NVVM backend compilation failed
  suggestion: check that CUDA_TOOLKIT_PATH is set correctly and that the CUDA toolkit supports
              target architecture sm_100a; rerun with IR dump flags if backend context is needed
```

The failure needs exactly three ingredients in one kernel; removing any one of them makes it compile:

1. `tcgen05.ld.sync.aligned.32x32b.x64` whose result is actually consumed (stored to gmem);
2. `cute.arch.warpgroup_reg_dealloc(40)` (PTX `setmaxnreg.dec`) executed by the warps that do **not** participate in the TMEM load;
3. a 384-thread CTA.

Bisection results (each row = one change relative to the failing config):

| change | result |
| --- | --- |
| none (`.x64`, dealloc(40) on non-loading warps, 384 threads) | **crash** |
| `.x32` load instead of `.x64` (same code, 32-column tile) | compiles |
| drop the `warpgroup_reg_dealloc` | compiles |
| `warpgroup_reg_alloc(168/216)` on the loading warps instead of dealloc on the others | compiles |
| add `warpgroup_reg_alloc` on loading warps *in addition to* the dealloc | still crashes (alloc is irrelevant either way) |
| 256 or 128 threads instead of 384 | compiles |
| dead `.x64` load (result not stored) | compiles |
| same file on nvidia-cutlass-dsl **4.4.2** | compiles |

# Steps/Code to reproduce bug

Self-contained repro below (also attached). Compile-only — the kernel is never launched. Requires an sm_100 GPU visible to the process and PyTorch (only used to allocate the 128×64 output tensor).

```
python repro_nvvm_tcgen05_ld_x64.py --width 64   # -> CompilerDiagnosticError: NVVM backend compilation failed
python repro_nvvm_tcgen05_ld_x64.py --width 32   # -> COMPILE_OK width=32
```

`--width` sets the accumulator/output tile width, which is the only difference between the two runs: 64 columns makes `cutlass.utils.blackwell_helpers.get_tmem_load_op` select `Ld32x32bOp` with repetition ×64, 32 columns selects ×32.

```python
"""NVVM backend crash in nvidia-cutlass-dsl 4.6.1: `tcgen05.ld ... .x64`
+ `setmaxnreg` (warpgroup register deallocation) on sm_100a.

Usage (compile only, the kernel is never launched; needs an sm_100 GPU):
    python repro_nvvm_tcgen05_ld_x64.py --width 64   # crash
    python repro_nvvm_tcgen05_ld_x64.py --width 32   # compiles OK
"""

import argparse

import torch

import cutlass
import cutlass.cute as cute
import cutlass.utils as utils
import cutlass.utils.blackwell_helpers as sm100_utils
from cutlass.cute.nvgpu import tcgen05
from cutlass.cute.runtime import from_dlpack
from cutlass.utils import LayoutEnum

M = 128  # 4 warps x 32 TMEM datapaths
NUM_THREADS = 384  # 12 warps: warps 0-3 issue the load, warps 4-11 idle

# 4.6 moved OperandMajorMode to cute.nvgpu; keep the file runnable on 4.4.x
# too so the regression can be demonstrated with the same script.
_MAJOR_MODE_K = getattr(cute.nvgpu, "OperandMajorMode", None) or tcgen05.OperandMajorMode
_MAJOR_MODE_K = _MAJOR_MODE_K.K


@cute.kernel
def kernel(
    mC: cute.Tensor,
    tiled_mma: cute.TiledMma,
    epi_tile: cute.Tile,
    num_tmem_cols: cutlass.Constexpr[int],
):
    warp_idx = cute.arch.make_warp_uniform(cute.arch.warp_idx())
    tidx, _, _ = cute.arch.thread_idx()

    @cute.struct
    class SharedStorage:
        tmem_holding_buf: cutlass.Int32

    smem = utils.SmemAllocator()
    storage = smem.allocate(SharedStorage)

    if warp_idx == 0:
        cute.arch.alloc_tmem(
            num_tmem_cols, storage.tmem_holding_buf, is_two_cta=False
        )
    cute.arch.barrier(barrier_id=0, number_of_threads=NUM_THREADS)
    tmem_ptr = cute.arch.retrieve_tmem_ptr(
        cutlass.Float32,
        alignment=16,
        ptr_to_buffer_holding_addr=storage.tmem_holding_buf,
    )

    # Required for the crash: reduce the register budget of the warps that
    # do not participate in the TMEM load (PTX `setmaxnreg.dec`).
    if warp_idx >= 4:
        cute.arch.warpgroup_reg_dealloc(40)

    if warp_idx < 4:
        # TMEM accumulator tensor, (M, N) fp32.
        acc_shape = tiled_mma.partition_shape_C(mC.shape)
        tAcc = cute.make_tensor(
            tmem_ptr, tiled_mma.make_fragment_C(acc_shape).layout
        )

        # Epilogue-style TMEM->register tiled copy. For epi_tile width 64
        # this selects tcgen05.ld 32x32b x64; for width 32, the x32 variant.
        copy_atom_t2r = sm100_utils.get_tmem_load_op(
            (M, mC.shape[1], 64),
            LayoutEnum.ROW_MAJOR,
            cutlass.BFloat16,
            cutlass.Float32,
            epi_tile,
            False,
        )
        tAcc_epi = cute.flat_divide(tAcc[((None, None), 0, 0)], epi_tile)
        tiled_copy_t2r = tcgen05.make_tmem_copy(
            copy_atom_t2r, tAcc_epi[(None, None, 0, 0)]
        )
        thr_copy_t2r = tiled_copy_t2r.get_slice(tidx)
        tTR_tAcc = thr_copy_t2r.partition_S(tAcc_epi)

        gC_epi = cute.flat_divide(mC, epi_tile)
        tTR_gC = thr_copy_t2r.partition_D(gC_epi)
        tTR_rAcc = cute.make_rmem_tensor(
            tTR_gC[(None, None, None, 0, 0)].shape, cutlass.Float32
        )

        # The failing TMEM load (+ a gmem store so the result is not dead).
        cute.copy(
            tiled_copy_t2r, tTR_tAcc[(None, None, None, 0, 0)], tTR_rAcc
        )
        tTR_gC[(None, None, None, 0, 0)].store(
            tTR_rAcc.load().to(cutlass.BFloat16)
        )


@cute.jit
def launcher(mC: cute.Tensor):
    n = mC.shape[1]
    tiled_mma = sm100_utils.make_trivial_tiled_mma(
        cutlass.BFloat16,
        _MAJOR_MODE_K,
        _MAJOR_MODE_K,
        cutlass.Float32,
        tcgen05.CtaGroup.ONE,
        (M, n),
    )
    epi_tile = (cute.make_layout(M), cute.make_layout(n))

    acc_shape = tiled_mma.partition_shape_C((M, n))
    num_tmem_cols = utils.get_num_tmem_alloc_cols(
        tiled_mma.make_fragment_C(acc_shape)
    )

    kernel(mC, tiled_mma, epi_tile, num_tmem_cols).launch(
        grid=(1, 1, 1),
        block=(NUM_THREADS, 1, 1),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--width",
        type=int,
        choices=(32, 64),
        default=64,
        help="TMEM load width: 64 -> tcgen05.ld .x64 (crash), 32 -> .x32 (OK)",
    )
    args = parser.parse_args()

    c = torch.zeros(M, args.width, dtype=torch.bfloat16, device="cuda")
    cute.compile(launcher, from_dlpack(c, assumed_align=16))
    print(f"COMPILE_OK width={args.width}")


if __name__ == "__main__":
    main()
```

Observed output at `--width 64`:

```
cutlass.base_dsl.compiler.CompilerDiagnosticError: error: NVVM backend compilation failed
  error: libNVVM failed while compiling generated device IR.
  note: target architecture: sm_100a
  note: backend log:
        NVVM backend compilation failed
  suggestion: check that CUDA_TOOLKIT_PATH is set correctly and that the CUDA toolkit supports
              target architecture sm_100a; rerun with IR dump flags if backend context is needed
```

Observed output at `--width 32`:

```
COMPILE_OK width=32
```

The dumped module IR (`CUTE_DSL_KEEP=ir`) for the failing case contains exactly one `tmem_load<f32, 32 DP, 32 bit, x64>` copy, one `setmaxregister decrease 40`, and `reqntid = 384`.

# Expected behavior

The `--width 64` variant should compile (it does on nvidia-cutlass-dsl 4.4.2, same machine, same driver), or at minimum the backend should emit a real diagnostic instead of an empty "NVVM backend compilation failed" log.

# Environment details

- nvidia-cutlass-dsl: **4.6.1** (fails); 4.4.2 compiles the identical file
- Python 3.12.9, PyTorch 2.12.0a0 nightly (only used to allocate the output tensor)
- GPU: NVIDIA GB200 (sm_100a, compute capability 10.0), aarch64 host
- CUDA driver: 580.82.07
- The same failure signature has also been observed on GB300 (sm_103a) with 4.6.1
- 4.6.0 fails identically; 4.4.2 is the last known-good version we tested

# Additional context

Things we ruled out while triaging (on the original production kernel, same failure signature):

- `--opt-level 0/2/3`: fails at every opt level
- `CUDA_TOOLKIT_PATH` / `CUDA_HOME`: no effect; the failing NVVM backend appears to be statically linked into the wheel's compiler library, so a newer local toolkit is not picked up
- libNVVM never emits an actual error log


## 评论 (1)

### brandon-yujie-sun · 2026-08-27

@thakkarV hi Vijay, this is fixed now in both 4.6.3 and 4.7.1

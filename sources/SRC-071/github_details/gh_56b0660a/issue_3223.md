# [Issue #3223] [BUG] T.gemm silently downgrades WGMMA to mma.sync for FP8 operands on SM90

source: https://github.com/tile-ai/tilelang/issues/3223
state: open | updated: 2026-09-14T14:19:54Z
labels: bug

## 正文

### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) that this hasn't already been reported. (comment there if it has.)

### What version of TileLang are you using?

0.1.14

### System information

3.12.3 linux
tilelang 0.1.14
torch 2.11.0+cu130
cuda 13.0
gpu NVIDIA H800 SM 9.0
nvcc release 13.0, V13.0.88
installed via pip (wheel)

### Problem description

### Describe the issue

On Hopper, `T.gemm` silently drops from WGMMA to Ampere-class `mma.sync` when an
FP8 operand is not K-major. There is no warning, no log, and no note in the
generated code — the only way to notice is to dump the CUDA source and count
instructions.

### Background

The FP8 form of `wgmma.mma_async` has no `imm-trans-a` / `imm-trans-b` operands,
unlike the bf16/fp16 form, so both operands must be K-major. The toolchain
enforces this:

```
wgmma.mma_async.sync.aligned.m64n8k16.f32.bf16.bf16 {...}, %a, %b, p, 1, 1, 0, 1;  // compiles
wgmma.mma_async.sync.aligned.m64n8k32.f32.e4m3.e4m3 {...}, %a, %b, p, 1, 1, 0, 1;
// ptxas: error : Arguments mismatch for instruction 'wgmma.mma_async with FP8 types'
```

`CheckWgmma()` in `src/cuda/op/gemm.cc` models this correctly:

```cpp
if (op.a_->dtype.is_float8() && op.b_->dtype.is_float8())
  return (!op.transA_) && op.transB_ && op.k_ % 32 == 0;
```

but when it returns false, `GetGemmInst()` just falls through:

```cpp
if (AllowTcgen5Mma(op, target)) return kCudaTCGEN05;
if (AllowWgmma(op, block_size, target)) return kCudaWGMMA;
...
return kCudaMMA;   // no diagnostic
```

### Impact

Measured on an idle H800 with an FP8 sparse MLA forward kernel
(S=8192, H=128, topk=2048, DQK=576, DV=512):

| PV operand | time | throughput | instruction mix |
| --- | --- | --- | --- |
| row-major (silently `mma.sync`) | 25.79 ms | 181 TFLOP/s | 4 wgmma + 4 mma_sync + 2 ldmatrix |
| K-major (WGMMA) | 14.24 ms | 328 TFLOP/s | 6 wgmma, no mma_sync |

1.81x, entirely invisible to the user. The natural way to write the PV product
of an attention kernel — `T.gemm(P_shared, V_shared, acc)` — is exactly the case
that hits this path.

This is not hypothetical: SGLang's production TileLang DSA kernel
(`sparse_mla_fwd_decode_partial_fp8` in `tilelang_kernel.py`) has four PV gemms
that all land on the fallback path.

### Suggested fix

Emit a `LOG(WARNING)` in `GetGemmInst()` when `AllowWgmma()` returns false on a
Hopper target for a dtype that carries layout constraints (FP8 / INT8 / TF32),
naming the failing condition and how to fix it, e.g.

```
WGMMA disabled for this gemm: FP8 requires (!trans_A && trans_B) on SM90
(got trans_A=0, trans_B=0); falling back to mma.sync. Store B as K-major to
enable WGMMA.
```

This matches the direction already taken elsewhere: `T.tcgen05_gemm` documents
that "compilation fails instead of silently falling back if the requested ISA
path is unavailable", and #2117 moved FP6 vector-type rejection earlier for the
same reason.


**Clarifying GitHub markdown formatting requirements**

### Reproducible example code

```python
import tilelang
from tilelang import language as T


@tilelang.jit(out_idx=[2])
def gemm_fp8(M, N, K, trans_B, threads=128):
    b_shape = (N, K) if trans_B else (K, N)

    @T.prim_func
    def main(
        A: T.Tensor((M, K), T.float8_e4m3),
        B: T.Tensor(b_shape, T.float8_e4m3),
        C: T.Tensor((M, N), T.float32),
    ):
        with T.Kernel(1, threads=threads):
            A_s = T.alloc_shared((M, K), T.float8_e4m3)
            B_s = T.alloc_shared(b_shape, T.float8_e4m3)
            acc = T.alloc_fragment((M, N), T.float32)

            T.clear(acc)
            T.copy(A, A_s)
            T.copy(B, B_s)
            T.gemm(A_s, B_s, acc, transpose_B=trans_B)
            T.copy(acc, C)

    return main


for trans_B in (True, False):
    src = gemm_fp8(64, 64, 64, trans_B).get_kernel_source()

    print(
        f"transpose_B={trans_B!s:<5} "
        f"wgmma={src.count('tl::wgmma')} "
        f"mma_sync={src.count('tl::mma_sync')} "
        f"ldmatrix={src.count('ptx_ldmatrix')}"
    )

# Output:
# transpose_B=True  wgmma=1 mma_sync=0 ldmatrix=0
# transpose_B=False wgmma=0 mma_sync=2 ldmatrix=1
```


### Traceback

```pytb
N/A -- the kernel compiles and produces correct results; the issue is a silent
performance downgrade, not a crash.
```

### Expected behavior

When `T.gemm` cannot use WGMMA on a Hopper target because of an operand layout
constraint that is specific to the dtype (FP8 / INT8 / TF32 all require
`!trans_A && trans_B`), the compiler should say so.

A one-line warning naming the failing condition would be enough, e.g.

    WGMMA disabled for this gemm: FP8 requires (!trans_A && trans_B) on SM90
    (got trans_A=0, trans_B=0); falling back to mma.sync. Store B as K-major to
    enable WGMMA.

Right now the only way to discover the downgrade is to call
`get_kernel_source()` and count instructions, which is not something a user
would think to do -- the kernel works, it is just ~1.8x slower than it should be
in a full attention kernel.

Raising an error would also be defensible (`T.tcgen05_gemm` already documents
that it "fails instead of silently falling back"), but a warning keeps existing
code working.

### Additional context

Found while adding an FP8 sparse MLA forward example for DeepSeek V3.2. In that
kernel the PV product contracts over the top-k tile dimension while V is stored
`[block_I, dim]`, so the natural `T.gemm(P_shared, V_shared, acc)` hits this
path: 25.79 ms instead of 14.24 ms at S=8192, H=128, topk=2048 on an idle H800.

The constraint itself comes from the instruction, not from TileLang -- the FP8
form of `wgmma.mma_async` has no `imm-trans-a` / `imm-trans-b` operands, and
ptxas rejects them:

    wgmma.mma_async.sync.aligned.m64n8k32.f32.e4m3.e4m3 {...}, %a, %b, p, 1, 1, 0, 1;
    // ptxas: error : Arguments mismatch for instruction 'wgmma.mma_async with FP8 types'

So the fix is purely about reporting, not about capability.

## 评论 (1)

### xuebozhang525-alt · 2026-09-14

Added the example side in #3224 , which uses a K-major V in shared memory to keep both GEMMs on WGMMA. The diagnostic itself is still open.

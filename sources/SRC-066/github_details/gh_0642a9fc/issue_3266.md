# [Issue #3266] [CuTeDSL] `nvvm.load.ext` rejects `BFloat16`: "Unsupported FP type for ExtLoadOp"

source: https://github.com/NVIDIA/cutlass/issues/3266
state: open | updated: 2026-09-21T18:17:32Z
labels: bug, ? - Needs Triage, inactive-30d, inactive-90d, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

**Describe the bug**

`cute.arch.load(ptr, BFloat16)` fails MLIR verification on both
`nvidia-cutlass-dsl == 4.4.2` and the latest `4.5.1`. The Python wrapper
`cute.arch.load` accepts the call (it accepts any `Numeric` type with no
per-dtype guard), but the underlying `nvvm.load.ext` op rejects `bf16` at
verification time with:

```
DSLRuntimeError: ICE IR Verification Failed
  Caused exception: Verification failed:
error: 'nvvm.load.ext' op Unsupported FP type for ExtLoadOp
  see current operation: %14 = "nvvm.load.ext"(%13) : (!llvm.ptr<1>) -> bf16
```

This is surprising because BF16 is a first-class type elsewhere in the
CuTe DSL surface, it is used in `cvt_i8_bf16`, in atomic-reduce dtype literals
(`"bf16"`, `"bf16x2"`), in MMA atom dtypes, and fully wired into
`nvvm_wrappers.py`, yet a scalar load through `nvvm.load.ext`
rejects it.

Workaround in user code is to read the BF16 as `Uint16`, left-shift by 16
(BF16 is bit-identical to the top 16 bits of an FP32), then bitcast to
`Float32` via `cutlass._mlir.dialects.llvm.bitcast`.

**Steps/Code to reproduce bug**

```python
import cutlass
import cutlass.cute as cute
from cutlass import BFloat16, Float32
from cutlass.cute.runtime import make_fake_tensor

@cute.kernel
def k(bias: cute.Tensor, out: cute.Tensor):
    tidx, _, _ = cute.arch.thread_idx()
    val_bf16 = cute.arch.load(bias.iterator + tidx, BFloat16)
    val_f32 = Float32(val_bf16)
    cute.arch.store(out.iterator + tidx, val_f32)

@cute.jit
def entry(bias: cute.Tensor, out: cute.Tensor):
    k(bias, out).launch(grid=(1, 1, 1), block=(32, 1, 1))

bias = make_fake_tensor(BFloat16, (32,), stride=(1,), assumed_align=2)
out = make_fake_tensor(Float32, (32,), stride=(1,), assumed_align=4)

cute.compile(entry, bias, out)  # fails at MLIR verification
```

**Expected behavior**

`cute.arch.load(ptr, BFloat16)` should compile and produce a scalar
`BFloat16` value, equivalent to a PTX `ld.b16` plus an interpretation as
BF16. If the underlying `nvvm.load.ext` cannot be extended to support
BF16 directly, the Python wrapper should silently lower BF16 loads
through `Uint16` + bitcast so callers do not need to know about the
limitation.

**Environment details (please complete the following information):**

 - Environment location: Docker (`flashmoe-cute-compile:latest`, derived
   from `nvidia/cuda:12.8.1` base image; no GPU required for the
   compile-time verification step)
 - `nvidia-cutlass-dsl` versions tested: **4.4.2** and **4.5.1** (both
   fail identically)
 - Target GPU arch: sm_100a (Blackwell).

**Additional context**

Two suggested fixes; **(2) is strictly safer** since it does not touch
the NVVM dialect verifier:

1. Add `bf16` to the list of supported FP types in `nvvm.load.ext`'s
   verifier, alongside `f16` / `f32` / `f64`. The PTX instruction
   `ld.b16` is dtype-agnostic at the hardware level; the rejection is
   purely a verifier-side restriction.
2. In the Python wrapper `cute.arch.load`, transparently lower BF16
   loads through `load(ptr, Uint16)` + bitcast to BF16. No NVVM dialect
   change needed; matches what users have to write by hand today.

We verified the op is **not** in upstream LLVM/MLIR. Neither
`nvvm.load.ext` nor `ExtLoadOp`/`LoadExtOp` appear in
`mlir/include/mlir/Dialect/LLVMIR/NVVMOps.td` or
`mlir/lib/Dialect/LLVMIR/IR/NVVMDialect.cpp` on `llvm/llvm-project` main
(checked 2026-05-23). The op and its `"Unsupported FP type for ExtLoadOp"`
verifier live in CUTLASS's bundled NVVM-dialect extension, so fix
option (1) is local to the CUTLASS DSL repo.

Other things we tried before filing:

- `assumed_align=4` on the `make_fake_tensor` call: same failure
  (alignment isn't the issue — the verifier rejects the BF16 dtype itself).
- The hand-rolled workaround (`Uint16` load + `<< 16` + `llvm.bitcast`
  to `Float32`) compiles cleanly on both 4.4.2 and 4.5.1 and produces
  the expected numerical result.

No existing CuTe DSL issue specifically requests BF16 support in
`nvvm.load.ext`. Closest neighbors (e.g. #2779 — bf16→fp8 single-element
conversion FEA) are unrelated to the load path.


## 评论 (2)

### github-actions[bot] · 2026-06-23

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-09-21

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

# [Issue #3687] [BUG] CuTe DSL: `a % b` gives different results for dynamic and constant operands when the signs differ

source: https://github.com/NVIDIA/cutlass/issues/3687
state: open | updated: 2026-09-27T00:38:12Z
labels: CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

**Describe the bug**

For signed integers and floats, `//` and `%` on dynamic values don't agree on a rounding direction, so `(a // b) * b + a % b != a` when `a` and `b` have opposite signs. The same expression on Python constants gives a different `%` result than it does at runtime.

In `python/CuTeDSL/_mlir_helpers/arith.py`, `__floordiv__` floors: `arith.floordivsi` for signed integers ([L672](https://github.com/NVIDIA/cutlass/blob/0b55a2f691d69981583568fd9eb69687b1f0de8a/python/CuTeDSL/_mlir_helpers/arith.py#L672)) and `math.floor(divf)` for floats ([L670](https://github.com/NVIDIA/cutlass/blob/0b55a2f691d69981583568fd9eb69687b1f0de8a/python/CuTeDSL/_mlir_helpers/arith.py#L670)). `__mod__` uses `arith.remsi` ([L689](https://github.com/NVIDIA/cutlass/blob/0b55a2f691d69981583568fd9eb69687b1f0de8a/python/CuTeDSL/_mlir_helpers/arith.py#L689)) and `arith.remf` ([L687](https://github.com/NVIDIA/cutlass/blob/0b55a2f691d69981583568fd9eb69687b1f0de8a/python/CuTeDSL/_mlir_helpers/arith.py#L687)), whose result takes the sign of the dividend. When both operands are Python constants, `Numeric` folds them with Python's own operators, which floor for both.

A wrap-around index shows it: `(i - 1) % n` with `i = 0` and `n = 4` gives -1 when `i` and `n` are kernel arguments and 3 when they're constants.

**Steps/Code to reproduce bug**

```python
import torch
import cutlass
import cutlass.cute as cute
from cutlass.cute.runtime import from_dlpack


@cute.kernel
def kernel(out_i: cute.Tensor, out_f: cute.Tensor, a: cutlass.Int32, b: cutlass.Int32,
           x: cutlass.Float32, y: cutlass.Float32):
    out_i[0] = a // b
    out_i[1] = a % b
    out_i[2] = cutlass.Int32(-7) // cutlass.Int32(2)
    out_i[3] = cutlass.Int32(-7) % cutlass.Int32(2)
    out_f[0] = x // y
    out_f[1] = x % y
    out_f[2] = cutlass.Float32(-7.0) // cutlass.Float32(2.0)
    out_f[3] = cutlass.Float32(-7.0) % cutlass.Float32(2.0)


@cute.jit
def run(out_i: cute.Tensor, out_f: cute.Tensor, a: cutlass.Int32, b: cutlass.Int32,
        x: cutlass.Float32, y: cutlass.Float32):
    kernel(out_i, out_f, a, b, x, y).launch(grid=(1, 1, 1), block=(1, 1, 1))


oi = torch.zeros(4, dtype=torch.int32, device="cuda")
of = torch.zeros(4, dtype=torch.float32, device="cuda")
run(from_dlpack(oi), from_dlpack(of), -7, 2, -7.0, 2.0)
torch.cuda.synchronize()
print("Int32   dynamic : -7 // 2 =", oi[0].item(), "  -7 % 2 =", oi[1].item())
print("Int32   constant: -7 // 2 =", oi[2].item(), "  -7 % 2 =", oi[3].item())
print("Float32 dynamic : -7.0 // 2.0 =", of[0].item(), "  -7.0 % 2.0 =", of[1].item())
print("Float32 constant: -7.0 // 2.0 =", of[2].item(), "  -7.0 % 2.0 =", of[3].item())
```

Output with nvidia-cutlass-dsl 4.8.0:

```text
Int32   dynamic : -7 // 2 = -4   -7 % 2 = -1
Int32   constant: -7 // 2 = -4   -7 % 2 = 1
Float32 dynamic : -7.0 // 2.0 = -4.0   -7.0 % 2.0 = -1.0
Float32 constant: -7.0 // 2.0 = -4.0   -7.0 % 2.0 = 1.0
```

The dynamic lines give `-4 * 2 + -1 = -9`, not `-7`.

**Expected behavior**

The dynamic and constant results should match, and `//` and `%` should agree with each other. `%` on dynamic values should take the sign of the divisor, as it already does for constants and as `//` implies: `1` and `1.0` above. `_WatchedM._binop_ir` in `pyir_core.py` already does this for `remsi` and `remf` ([L2727-L2747](https://github.com/NVIDIA/cutlass/blob/0b55a2f691d69981583568fd9eb69687b1f0de8a/python/CuTeDSL/cutlass/base_dsl/pyir_core.py#L2727-L2747)), with the comment `# Python % takes the DIVISOR's sign; arith.remsi the dividend's.` `ArithValue.__mod__` doesn't.

I have a local change that applies the same correction in `ArithValue.__mod__`. With it the script above prints `1` and `1.0` on all four lines. I also wrote a test in `test/python/CuTeDSL` that runs `//` and `%` on the GPU for Int32, Int64 and Float32 across all sign combinations and checks the results against Python. It fails on 4.8.0 and passes with the change. The rest of `test/python/CuTeDSL` gives the same results with and without it. The correction adds a few compares and a select to every signed `%`, so if `remsi` was kept here on purpose for cost, that would be good to know.

**Environment details (please complete the following information):**
 - Environment location: Bare-metal, Ubuntu 24.04.4, RTX 5090 (driver 610.43.02), nvidia-cutlass-dsl[cu13] 4.8.0, Python 3.12.13, torch 2.14.0

**Additional context**

Unsigned `%` (`remui`) isn't affected: for the `Uint32` pairs I tried, including values above 2**31, dynamic and constant results matched.


## 评论 (1)

### yunweili3 · 2026-09-27

Fix in #3688: `ArithValue.__mod__` now applies the same divisor-sign correction as `_WatchedM._binop_ir`, so dynamic `%` matches `//` and the constant-folded results for signed ints and floats (unsigned `%` is unchanged). Verified on a B200 with DSL 4.8.0: the reproducer above prints `1` / `1.0` on all four lines, and a new GPU test covering Int32/Int64/Float32 (scalars and TensorSSA) across all sign combinations fails before and passes after.


# [Issue #3001] [BUG][Fuzzer][ice-on-valid-code] Constant int32 `1 << 31` aborts compile in const-fold instead of wrapping to INT32_MIN

source: https://github.com/tile-ai/tilelang/issues/3001
state: closed | updated: 2026-08-25T05:43:57Z
labels: 

## 正文

### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) and no similar issue was found.

### What version of TileLang are you using?

0.1.13

### System information

Linux, NVIDIA L40S (sm_89), CUDA 13.0, PyTorch 2.13.0. The defect is in constant folding (host-side, `target="cuda"`) and is architecture-independent — it aborts before any device code is generated.

### Problem description

A left shift by a compile-time-constant amount whose folded result lands in the top bit of a signed integer aborts compilation with an internal `IntImm` range assert, instead of producing the wrapped constant. `(T.int32(1) << T.int32(31))` — a compile-time-constant `0x80000000` / `INT32_MIN` — crashes the compiler:

```
Check failed: value < 1LL << (dtype.bits() - 1) (2147483648 vs. 2147483648)
  : Literal value 2147483648 exceeds maximum of int32
```

The same operation is well-defined and works on every non-folding path:

| form | `1 << 31`, `int32` | result |
|---|---|---|
| **constant amount** `T.int32(1) << T.int32(31)` | **compile abort** (range check) | — |
| runtime amount `T.int32(1) << S[i]` (`S[i]==31`) | compiles | `-2147483648` (`0x80000000`) ✓ |
| constant amount, `uint32` | compiles | `2147483648` ✓ |
| constant amount `1 << 30`, `int32` | compiles | `1073741824` ✓ |

The controls agree with NumPy and PyTorch, both of which return `-2147483648` for `int32(1) << 31` (they wrap, they don't reject). Note the `uint32` row compiles because `uint32` is *not* an index type, so its shift is never const-folded (a `shift_left` intrinsic is emitted); only signed `int32` both folds *and* overflows the constructor. So only the *constant-folded signed `int32`* path crashes; the value is computable and its wrapped result is well-defined.

This is not a regression — the folding logic predates the vendored TVM fork (see Provenance).

### Reproducible example code

```python
import tilelang, tilelang.language as T
import torch

N = 256

def build(shift):
    @T.prim_func
    def p(A: T.Tensor((N,), "int32"), C: T.Tensor((N,), "int32")):
        with T.Kernel(1, threads=N) as _:
            i = T.get_thread_binding()
            C[i] = A[i] + (T.int32(1) << T.int32(shift))   # shift amount is a compile-time constant
    return tilelang.compile(p, out_idx=[1], target="cuda")

a = torch.zeros(N, dtype=torch.int32, device="cuda")

# control: shift = 30 -> folds to 1073741824, fits int32 -> compiles
k = build(30); print("shift=30:", int(k(a).cpu()[0]))   # -> 1073741824

# bug: shift = 31 -> const-fold builds IntImm(int32, 1<<31 = 2147483648) -> range check aborts compile
k = build(31); print("shift=31:", int(k(a).cpu()[0]))   # want INT32_MIN = -2147483648; instead: compile aborts
```

### Traceback

```
File "repro.py", line 9, in p
    C[i] = A[i] + (T.int32(1) << T.int32(shift))
File ".../tvm/python/tvm/tirx/expr.py", line 128, in __lshift__
    return _ffi_api.left_shift(self, other, None)
File "<unknown>", line 0, in tvm::left_shift(tvm::PrimExpr, tvm::PrimExpr, tvm::Span)
File ".../3rdparty/tvm/src/ir/expr.cc", line 73, in tvm::IntImm::IntImm(tvm::DataType, int64_t, tvm::Span)
ValueError: Check failed: value < 1LL << (dtype.bits() - 1) (2147483648 vs. 2147483648) : Literal value 2147483648 exceeds maximum of int32
```

### Expected behavior

Compile and produce the wrapped constant — `int32(1) << 31 == -2147483648` (`0x80000000`), matching TileLang's own runtime-shift path, its `uint32` path, and NumPy/PyTorch. The wrapped low `bits` of the fold are the well-defined result.

### Additional context

**Root cause.** `left_shift`'s constant-folding path builds the result `IntImm` directly from the raw wide product, without narrowing it to the result dtype first. When both operands are constants, [`op.cc:792`](https://github.com/tile-ai/tvm/blob/8df8ebd61659505dd7005f4820b030e983e2c005/src/tirx/op/op.cc#L792) does `return IntImm(rtype, (pa->value << pb->value), span)`. For `rtype=int32`, `1LL << 31 == 2147483648`, which is outside the signed-int32 range, so the `IntImm` constructor's range check [`expr.cc:73`](https://github.com/tile-ai/tvm/blob/8df8ebd61659505dd7005f4820b030e983e2c005/src/ir/expr.cc#L73) (`TVM_FFI_CHECK_LT(value, 1LL << (dtype.bits() - 1), ValueError)`) fires. The preceding `pb->value < rtype.bits()` guard (shift `31 < 32`) passes, so the shift amount itself is legal; it is the folded *value* that overflows the dtype at construction. Note that this range branch is gated on `dtype.bits() < 64`, so a 64-bit result dtype takes a different path (see §17).

<details><summary>Why the sibling fold paths don't crash</summary>

The arith constant-fold helper [`GetFoldResultInt64Repr` (`const_fold.h:81`)](https://github.com/tile-ai/tvm/blob/8df8ebd61659505dd7005f4820b030e983e2c005/src/arith/const_fold.h#L81) already narrows a fold result to the dtype before constructing the `IntImm` — it masks the low `bits` (`x &= (1LL << dtype.bits()) - 1`) and sign-extends for signed types (`x = (x ^ m) - m`). That helper is what `Add`/`Mul`/etc. route their folds through. `left_shift` in `op.cc` bypasses it and hands the raw `int64_t` product straight to `IntImm`, so it is the one integer fold that does not narrow.

- `uint32`: the fold is never entered — the fold body is gated on `arith::IsIndexType`, which is `type.is_int()` (signed only) `&& bits ∈ {32,64}`, so `uint32` takes the non-fold path and a `shift_left` intrinsic is emitted; the device computes `2147483648`. (Even if it did fold, the unsigned `IntImm` range `[0, 2^32)` would accept the value.)
- `int8`/`int16`: also never fold — `IsIndexType` requires bits 32 or 64, so these emit a `shift_left` intrinsic (verified in §17).
- runtime shift amount: `pa && pb` is false, so the fold is skipped entirely and a `shift_left` intrinsic is emitted; the device computes the wrapped value.
</details>

**Suggested fix.** Narrow the fold result to the result dtype before building the `IntImm` — e.g. route the `left_shift` constant fold through the same `GetFoldResultInt64Repr` masking/sign-extension that the other integer folds use, so `int32(1) << 31` yields `IntImm(int32, -2147483648)`. (Not built end-to-end; the mask helper already exists in the same tree.)

**Provenance.** The fold lives in the vendored TVM fork (`3rdparty/tvm`, submodule `tile-ai/tvm` at `8df8ebd6`). The `left_shift` fold predates the fork (the file carries apache/tvm history back to 2020), so this is inherited-upstream, not a TileLang regression.

**Dedup.** I searched the open and closed tracker and found no existing report of the left-shift fold overflow. It shares its general root with #2982 (`FloatImm`/`IntImm` range-check on an un-narrowed value in the same `expr.cc`) — same mechanism, different sink (`FloatImm` in `T.fill` there, the `left_shift` `IntImm` fold here). These are distinct sinks in different operators and are not a merge; the shared root is recorded in §17.

**Reach.** The trigger is a compile-time-constant left shift into the sign bit of **signed `int32`** — `T.int32(1) << 31`. The fold only runs for *index* dtypes (`arith::IsIndexType` = signed int of exactly 32 or 64 bits, [`const_fold.h:81`](https://github.com/tile-ai/tvm/blob/8df8ebd61659505dd7005f4820b030e983e2c005/src/arith/const_fold.h#L81)), and the `expr.cc:73` signed range check only fires for `bits < 64`; so of the index dtypes only `int32` both folds *and* overflows the constructor. `int8`/`int16` do **not** fold at all (non-index width → a `shift_left` intrinsic is emitted, verified in §17), and `int64` folds but skips the range check (`bits==64`), so the boundary is exactly `int32`. Building `INT32_MIN`, a top-bit mask, or `0x80000000` as a literal is ordinary integer code, and the shift amount `31` is exactly on the boundary of the op's own accepted range (`< bits`).

**Shipped-example run (0.1.13, L40S).** The only shipped `examples/` kernels that route a constant `<<` through this exact fold are the dequant-GEMM FP4 converters (`example_dequant_gemm_fp4_hopper.py`, `example_dequant_gemm_bf16_mxfp4_hopper.py`), which build FP16/BF16 bit patterns with `s << tirx.const(5, uint16)`, `... << tirx.const(10, uint16)`, `m << tirx.const(9, uint16)`. I ran `example_dequant_gemm_fp4_hopper.py::test_fp4_fp16_convert_close()` verbatim on 0.1.13 — it **compiles and passes** (`Pass`). It **dodges the bug** for two independent reasons: (1) the dtype is `uint16`, which is not an index type, so the fold is never entered (a `shift_left` intrinsic is emitted); and (2) even the largest shift (`1 << 15`) is in range. All other `<<` uses in `examples/` are Python-level `int`/torch shifts (folded by Python/PyTorch, not TVM) or C++ string literals inside inline-PTX asm — none reach the TVM `int32` fold. This is why CI is green. Any kernel that writes a constant `T.int32(1) << 31` in signed `int32` context trips it at compile.

**Impact.** The trigger is narrow: the shift amount and operand must both be compile-time constants of signed `int32`, and the folded result must land exactly on the sign bit (`1 << 31`) — a runtime shift amount, an unsigned dtype, a non-index-width signed dtype (`int8`/`int16`, which do not fold at all), a 64-bit dtype, or any smaller shift all avoid it. When it fires it is a loud compile-time abort, deterministic on the source, so it cannot silently corrupt a result or slip into a running workload — it blocks that one kernel from building and produces nothing wrong. Fixing it closes a boundary case (the top-bit constant-shift fold) so a legal idiom like a literal `INT_MIN`/top-bit mask compiles instead of being refused, matching the runtime-shift and `uint32` paths.

<details><summary>§17 Generalization record</summary>

**Found first.** `int32` constant `T.int32(1) << T.int32(31)` — folds to `IntImm(int32, 2147483648)`, aborts compile at the `expr.cc:73` range check.

**Two-level root.**
- **SOURCE-level (fragile implementation):** `left_shift`'s constant-fold arm in `3rdparty/tvm/src/tirx/op/op.cc:792` — `return IntImm(rtype, (pa->value << pb->value), span)` — builds the result `IntImm` from the *raw* wide `int64_t` product without narrowing to `rtype`. It bypasses `arith::GetFoldResultInt64Repr` (`const_fold.h:81`), the mask-and-sign-extend helper that the arith `TryConstFold` folds (`Add`/`Sub`/`Mul`/`Div`/`Mod`) all route through. The same *bypass* pattern (`IntImm(rtype, raw)` inline, no `GetFoldResultInt64Repr`) appears in the sibling ops in the same file: `right_shift` (`op.cc:771`), `bitwise_and` (`:805`), `bitwise_or` (`:817`), `bitwise_xor` (`:829`), and the C++ unary `neg` (`:524`, `IntImm(dtype, -pa->value)`).
- **OPERATOR-level (what could correlate):** any const-foldable integer op whose folded value can land outside the *signed 32-bit* range while its wrapped result is well-defined. The only such op reachable at the fold gate is a top-bit `<<`; the bitwise ops can raise no bit their (already-valid) operands don't already have, so from valid `int32` `IntImm`s they cannot produce an out-of-range value; `right_shift` shrinks; and the C++ `neg` overflow point (`-INT32_MIN`) is not reachable from the Python frontend (see below).

**Fold gate (why only `int32`).** The fold body is wrapped in `TVM_INDEX_CONST_PROPAGATION`, which runs the fold *only* when both operands satisfy `arith::IsIndexType` = `type.is_int()` (signed, `kInt` — `data_type.h:210`) `&& bits ∈ {32, 64}`. So the fold is entered *only* for signed `int32`/`int64`. Combined with the `expr.cc:73` range check being gated on `bits < 64`, the crash window is exactly signed `int32`.

**Four-axis cells tested (observed on 0.1.13, L40S, each in a fresh process):**

| axis | cell tested | input → observed result | same root? |
|---|---|---|---|
| — (finding) | `int32` `1 << 31` | **compile abort**, `expr.cc:73` `(2147483648 vs. 2147483648)` | — |
| related-type | `int64` `1 << 63` | **folds, compiles** → `IntImm(int64, -9223372036854775808)` (INT64_MIN) | distinct — same fold arm, but range check skipped (`bits==64`); no overflow |
| related-type | `uint32` `1 << 31` | **not folded** → `T.shift_left(...)` Call; kernel compiles, yields `2147483648` | distinct — `uint32` is not an index type (`is_int()` false), fold never entered |
| related-type | `int8` `1 << 7` | **not folded** → `T.shift_left(int8(1), int8(7))` Call | distinct — non-index width (bits≠32/64), fold never entered |
| related-type | `int16` `1 << 15` | **not folded** → `T.shift_left(int16(1), int16(15))` Call | distinct — same as int8 |
| related-operator | `neg(INT32_MIN)` via Python `-x` | **folds, compiles** → `IntImm(int32, -2147483648)` (correct wrap) | distinct — Python `__neg__` is `x * const(-1)` → routes through `Mul` `TryConstFold` → `GetFoldResultInt64Repr` narrows. The un-narrowed C++ `neg` at `op.cc:524` is not reached from the frontend |
| related-operator | `bitwise_or` `0x40000000 \| 0x1` (`int32`) | **folds, compiles** → `IntImm(int32, 1073741825)` | distinct — OR/XOR/AND of valid `int32` `IntImm`s can never set a bit above what an operand already holds, so cannot reach out-of-range |
| related-source | `right_shift` `(1<<30) >> 1` (`int32`) | **folds, compiles** → `IntImm(int32, 536870912)` | distinct — shares the same inline-`IntImm` bypass at `op.cc:771`, but right-shift shrinks the value so it can never overflow |

**Boundary verdict — kept specific.** The crash is narrow to signed `int32` top-bit `<<`. The *source* fragility (raw-`IntImm` fold without `GetFoldResultInt64Repr`) is shared across `right_shift` + the three bitwise ops + C++ `neg`, but none of those sinks can be driven out of range from valid frontend inputs: right-shift/bitwise cannot grow a value past its operands, and frontend `neg` narrows via `Mul`. So the fix (route the `<<` fold through `GetFoldResultInt64Repr`, ideally applied uniformly to all five inline-`IntImm` sites for consistency) is the right shape, but only the `<<` site is currently a live crash. Title/Problem kept specific to the `int32 1<<31` crash.

**Distinct-adjacent, not filed.** The `int8`/`int16` "not folded → intrinsic emitted" behavior is a *non-fold* (correct on device), not a bug — the shift is left as a runtime `shift_left`, so `int8`/`int16` never crash (they never fold; the crash window is `int32` only). The C++ `neg` un-narrowed sink (`op.cc:524`) is latent but frontend-unreachable. No new bug was found while sweeping.

**Shared general root with #2982.** #2982 is the `FloatImm` range-check-on-un-narrowed-value defect (`T.fill(f32, -3.4028235e38)` rejected though it rounds onto `float32::lowest()`), same `expr.cc` at the same tvm pin `8df8ebd6`, different sink (the `FloatImm` branch, reached via `T.fill`). This left-shift `IntImm` fold is the same general mechanism at a different sink. **Do not merge** — they are separate operators/sinks; the shared root is recorded here for tracking, not as a duplicate.

</details>

## 评论 (1)

### KellyFrog · 2026-08-25

Hi!

Writing `1 << 31` is not recommended in C++ either and this issue is irrelevant to tilelang's main focus.

The issue is therefore closed.

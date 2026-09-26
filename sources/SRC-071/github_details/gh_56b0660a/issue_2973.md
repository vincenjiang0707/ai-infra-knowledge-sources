# [Issue #2973] [BUG][Fuzzer][wrong-code] CuTeDSL codegen emits Python floor `//` for integer truncdiv (DivNode), giving wrong results for negative operands

source: https://github.com/tile-ai/tilelang/issues/2973
state: open | updated: 2026-08-27T14:41:17Z
labels: 

## 正文


### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the Issue Tracker that this hasn't already been reported.

### What version of TileLang are you using?

0.1.13 (reproduced on 0.1.13 with nvidia-cutlass-dsl 4.3.1).

### System information

NVIDIA L40S (`sm_89`), CUDA 12.8, Python 3.13, tilelang 0.1.13, nvidia-cutlass-dsl 4.3.1. The defect is in the target-independent CuTeDSL codegen `DivNode` emit, so it is not specific to one GPU.

### Problem description

On the **CuTeDSL backend**, TIR's `DivNode` (the truncating integer division used by `T.truncdiv` and the `/` operator on integers) is emitted as Python floor-division `//`. Python `//` rounds toward negative infinity; TIR `truncdiv` (and CUDA C `/`) round toward zero. For negative operands the two differ silently.

Worse, the CuTeDSL `%` operator (emitted for `truncmod`) rounds **toward zero** (C semantics), so `//` and `%` use *inconsistent* conventions and the identity `a == (a // b) * b + (a % b)` is broken.

Measured operator semantics on `cutlass.Int32` (isolated, `a = -7, b = 3`):

| operator (emitted) | result | convention |
|---|---|---|
| `//` (DivNode / truncdiv) | -3 | Python **floor** |
| `%`  (ModNode / truncmod) | -1 | C **truncate** |

`(-7 // 3) * 3 + (-7 % 3) = -3*3 + -1 = -10 != -7`. Any code that relies on `q*b + r == a` (index math, tiling, un-flattening) silently corrupts.

### Reproducible example code

```python
import torch, tilelang, tilelang.language as T

@T.prim_func
def tdiv(A: T.Tensor((8,), "int32"), C: T.Tensor((8,), "int32")):
    with T.Kernel(1, threads=8) as bx:
        i = T.get_thread_binding()
        C[i] = T.truncdiv(A[i], 3)

k = tilelang.compile(tdiv, target="cutedsl", out_idx=-1)
a = torch.tensor([-7,-5,-1,2,5,7,3,4], dtype=torch.int32, device="cuda")
print(k(a).tolist())                                   # [-3,-2,-1,0,1,2,1,1]  (floor -- WRONG)
print(torch.div(a,3,rounding_mode="trunc").tolist())   # [-2,-1, 0,0,1,2,1,1]  (trunc -- CORRECT)
```

Emitted CuTeDSL source: `C.iterator[tid] = A.iterator[tid] // 3`.

Expected vs actual:

| a | `truncdiv(a,3)` expected | CuTeDSL emit `a // 3` |
|---|---|---|
| -7 | -2 | **-3** |
| -5 | -1 | **-2** |
| -1 |  0 | **-1** |

### Traceback

No traceback — the kernel compiles and runs to completion; the result is silently wrong and deterministic.

### Expected behavior

`T.truncdiv(a, b)` (TIR `DivNode`) should round toward zero: `truncdiv(-7, 3) == -2`, not `-3`. The same `DivNode` on the CUDA backend already does this — its inherited `CodeGenC::VisitExpr_(DivNode)` prints C `/`, which truncates — so a correct target already exists; only CuTeDSL diverges. This also matches `torch.div(..., rounding_mode="trunc")`. The result should stay consistent with the `%` operator the backend emits, so that `(a // b) * b + (a % b) == a` holds.

### Additional context

**Root cause.** [`src/cuda/codegen/codegen_cutedsl.cc#L667-L670`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/cuda/codegen/codegen_cutedsl.cc#L667-L670):

```cpp
if (op->dtype.is_int() || op->dtype.is_uint()) {
    PrintBinaryExpr_("//", op->dtype, op->a, op->b, os);   // Python floor, but DivNode means truncdiv
```

(Identical hazard in the base class [`src/cuda/codegen/codegen_py.cc#L271-L276`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/cuda/codegen/codegen_py.cc#L271-L276) — note the base class emits `/` for the float branch but `//` for the int branch.)

TIR's `Div`/`DivNode` is **truncating** division; `FloorDiv` is a separate node. Emitting `//` for `DivNode` is a semantic mismatch. The CUDA backend emits C `/` here, which truncates correctly. Because CuTeDSL `%` already truncates, `//`-for-DivNode disagrees with it and breaks the div/mod identity.

TVM's own IR contract fixes the expected result — `DivNode` is truncating, not flooring — and the CuTeDSL emit contradicts it in two independent places:

<details>
<summary>TVM defines DivNode as truncating (doc + constant folder), distinct from FloorDiv</summary>

- **Type doc**, [`tvm/include/tvm/tirx/op.h#L336-L347`](https://github.com/apache/tvm/blob/8df8ebd61659505dd7005f4820b030e983e2c005/include/tvm/tirx/op.h#L336-L347): `truncdiv` is documented as `compute trunc(a / b)` / "the default integer division behavior in C"; `div` (the `/` operator) "directly corresponds to truncdiv" for integers. TVM deliberately keeps `truncdiv`/`floordiv` as *separate* nodes and emits a compile error for a bare `/` to force the caller to disambiguate — so `DivNode` and `FloorDiv` are not interchangeable by design.
- **Constant folder**, `tvm/src/arith/const_fold.h`: the two nodes fold with *different* algorithms — [`Div`](https://github.com/apache/tvm/blob/8df8ebd61659505dd7005f4820b030e983e2c005/src/arith/const_fold.h#L218-L232) does `pa->value / pb->value` with the comment `// NOTE: this will assumes trunc div.`, while [`FloorDiv`](https://github.com/apache/tvm/blob/8df8ebd61659505dd7005f4820b030e983e2c005/src/arith/const_fold.h#L274-L280) does `arith::floordiv(...)`. So at compile time TVM folds `truncdiv(-7,3)` to **-2**.

The consequence: a `DivNode` with **constant** operands folds to the truncating value (-2), but the **same node with runtime operands** is emitted as `//` and yields the flooring value (-3). One kernel gives two different answers for the same expression depending only on whether the operand is a literal — a self-contradiction that pins -2 as the intended result.

</details>

**Suggested fix.** Emit a truncating form for `DivNode` on integers instead of `//`. Options: emit an explicit truncation (`cutlass` integer division intrinsic if one exists), or `int(a / b)`-style trunc, or a corrected `//` with the standard sign fix-up. Because CuTeDSL `%` already truncates, the fix must make `//`-for-DivNode agree with it so `q*b + r == a` holds. Note the `floordiv`/`ceildiv` lowerings (see "Same root, wider scope" below) currently *assume* `//` truncates and add a floor fix-up — whichever convention `//` is fixed to, those fix-ups must be reconciled with it so all of truncdiv/floordiv/ceildiv agree.

**Provenance.** The int arm of `DivNode` emitting `//` is present in `codegen_cutedsl.cc:667-670` and the base `codegen_py.cc:273-274` (0.1.13); reproduced at runtime on 0.1.13 this session (`[-3,-2,-1,…]` vs torch trunc `[-2,-1,0,…]`); origin not bisected below 0.1.13.

**Dedup.** This is not a report that `//`/`>>` floors — that is intended. In #995 (closed) a maintainer set the project's contract explicitly: the `/` operator lowers to floor division ("`>>` represents floor division, consistent with Python's `//`"), and **users who want truncation are told to call `T.truncdiv`**. This report is that the escape hatch itself is broken *on the CuTeDSL backend*: `T.truncdiv` builds a TIR `DivNode` (documented truncating), and CuTeDSL emits `//` for it, so the one op the maintainer pointed users to still floors. It is distinct from the CuTeDSL fast-math #2597 and slow-math #2565 families (floating-point math intrinsics, not integer rounding).

**Same root, wider scope.** The `//`-convention inconsistency is not confined to `truncdiv` — I enumerated every op whose correctness depends on the backend's division-rounding convention. `floordiv` and `ceildiv` are corrupted too, in the *opposite* direction: their lowerings assume `//` truncates and add a `+ ((a % b) >> 31)` fix-up to reach floor, but since `//` already floors, they over-correct.

<details>
<summary>Full rounding-scope on 0.1.13 (int32, operand -7)</summary>

| op | expected | CuTeDSL | emitted |
|---|---|---|---|
| `T.truncdiv(-7,3)` | -2 | **-3** | `a // 3` |
| `T.floordiv(-7,3)` | -3 | **-4** | `(a // 3) + Int32((a % 3) >> 31)` |
| `T.ceildiv(-7,3)`  | -2 | **-3** | `((a + 2) // 3) + Int32(((a+2) % 3) >> 31)` |
| `T.truncmod(-7,3)` | -1 | -1 (correct) | `a % 3` |
| `T.floormod(-7,3)` |  2 |  2 (correct) | `a % 3` |
| `a >> 1` (a=-8) | -4 | -4 (correct) | `a >> 1` |

So `truncdiv` floors when it should truncate, while `floordiv`/`ceildiv` double-floor. `truncmod`/`floormod` (both emit `%`, truncating) and arithmetic `>>` are correct. All reproduced this session on 0.1.13.

</details>

**Reach.** `T.truncdiv` is a documented frontend op and is the exact op the maintainer directs truncation-needing users to (#995), so the trigger is a supported, recommended call — not an exotic one. The failing condition is any integer division with a possibly-negative operand (index math, tiling, un-flattening on the CuTeDSL backend); the div/mod identity break additionally reaches code that assumes `q*b + r == a`. Non-negative operands are unaffected. The `floordiv`/`ceildiv` faces above share this one root.

**Impact.** The trigger is narrow in one ingredient only — it needs a negative operand — but integer division is pervasive in index and tiling math, so a possibly-negative operand is not rare. When it fires there is no error: the kernel compiles and runs, and the result is deterministically off by one. Worse, because `%` and `//` round under inconsistent conventions the div/mod identity `q*b+r==a` breaks, so any downstream index math built on the pair (un-flattening, tiling) corrupts silently rather than failing loudly.



## 评论 (2)

### Hughshine · 2026-08-15

**Follow-up — the same `//`-semantics inconsistency corrupts `floordiv` and `ceildiv` too, in the opposite direction.**

I checked the full set of ops whose correctness depends on the backend's integer-division rounding convention. The root here — the CuTeDSL backend is internally inconsistent about whether `//` truncates or floors — has a second face: the `FloorDiv`/`ceildiv` lowerings *assume `//` truncates* and add a correction to reach floor, but since `//` already floors, they over-correct.

Measured on 0.1.13 (L40S sm_89), int32, operand `-7`:

| op | expected | CuTeDSL | emitted expression |
|---|---|---|---|
| `T.truncdiv(-7,3)` | -2 | **-3** (this issue) | `a // 3` |
| `T.floordiv(-7,3)` | -3 | **-4** | `(a // 3) + Int32((a % 3) >> 31)` |
| `T.ceildiv(-7,3)`  | -2 | **-3** | `((a + 2) // 3) + Int32(((a+2) % 3) >> 31)` |
| `T.truncmod(-7,3)` | -1 | -1 (correct) | `a % 3` |
| `T.floormod(-7,3)` |  2 |  2 (correct) | `a % 3` |
| `a >> 1` (a=-8) | -4 | -4 (correct) | `a >> 1` |

The `floordiv`/`ceildiv` emit adds `+ ((a % b) >> 31)` (i.e. `-1` when the remainder is negative) — the standard fix-up to turn C's *truncating* `/` into a floor. But CuTeDSL's `//` is Python floor already, so `-7 // 3` is `-3` and the fix-up subtracts another 1 → `-4`. So `truncdiv` floors when it should truncate (this issue), while `floordiv`/`ceildiv` double-floor. A single consistent convention for `//` fixes all three: if `//` is defined as floor, `DivNode` must not use it *and* the `FloorDiv`/`ceildiv` fix-up must be dropped; if `//` were truncating, the reverse. `truncmod`/`floormod` (both emit `%`, which truncates) and arithmetic `>>` are correct and unaffected.

All reproduced this session on 0.1.13.


### SuperGoodGame · 2026-08-27

Reproduced on a source build of HEAD (`a2e02cc`, `0.1.13+cuda.gita2e02cc5`) — H200 sm_90, CUDA 12.8, torch 2.11, nvidia-cutlass-dsl 4.7.1.

The blast radius is wider than the report: all three division ops are wrong, both mod ops are fine.

| op | got | expected |
|---|---|---|
| `truncdiv(-7, 3)` | -3 | -2 |
| `floordiv(-7, 3)` | **-4** | -3 |
| `ceildiv(-7, 3)` | **-3** | -2 |
| `truncmod(-7, 3)` | -1 | -1 |
| `floormod(-7, 3)` | 2 | 2 |

`q*b + r == a` breaks for 3 of my 8 test inputs.

The emitted CuTeDSL makes the mechanism explicit (tensor accesses simplified for readability):

```python
truncdiv(a, 3)  ->  a // 3
floordiv(a, 3)  ->  (a // 3) + cutlass.Int32(((a % 3) >> 31))
```

The floordiv lowering is the standard truncdiv→floordiv correction, and it is only correct if `//` truncates. Because `//` already floors, the correction double-applies: for `a = -7`, `//` gives -3 and the term adds -1, hence -4.

So I think there is only one bug — `VisitExpr_(DivNode)` emitting `//` — and floordiv/ceildiv are downstream victims of it. Fixing `DivNode` alone should make all three correct with no change to the FloorDiv/CeilDiv fix-ups, since those were already written against TIR's truncating-`Div` contract. That is the opposite of the concern raised above about having to reconcile the fix-ups — the direction works in our favour.

Before I write it, one question on the form you'd prefer, since it decides which files get touched.

**Option 1** — add a `truncdiv` helper to `tilelang/contrib/cutedsl/math.py` (next to `divf`) and emit `tl.truncdiv(a, b)` from `VisitExpr_(DivNode)`:

```python
def truncdiv(x, y):
    return (x - (x % y)) // y
```

Exact, because the backend's `%` already truncates, so `x - r` is exactly divisible by `y` and the following `//` cannot round in either direction. Correct for negative divisors and for unsigned types, and there is no shift width to get right.

**Option 2** — inline the same arithmetic in the codegen, no new runtime symbol.

I'd lean to option 1. The scalar path of `PrintBinaryExpr_` has no SSA temporary, so inlining would duplicate the whole `x` subexpression; the vector path does temp its operands, so it would be fine there. The cost of option 1 is the mirror image: `//` sits in the infix fast path of `PrintVecBinaryOp_`, so a function-style name makes vectorized integer division unpack per lane. `truncdiv` as written also accepts `TensorSSA`, so it could later be added to the vectorized `.store()` path if that matters.

Scope question: `codegen_py.cc:274` has the same int-branch hazard in the base class. Same PR, or separate?

Happy to take this — could you assign it to me? Tests I'd add: all five ops on negative operands against `torch.div(..., rounding_mode=...)`, the `q*b + r == a` identity, and the CUDA backend as a cross-target reference.


# [Issue #3024] [BUG][Fuzzer][wrong-code] `T.clamp` silently drops `NaN` and returns the `min` bound instead of propagating `NaN`

source: https://github.com/tile-ai/tilelang/issues/3024
state: closed | updated: 2026-09-24T05:44:23Z
labels: 

## 正文


### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) that this hasn't already been reported. (comment there if it has.)
- [x] I have tried the latest version of TileLang.

### What version of TileLang are you using?

0.1.13

### System information

NVIDIA L40S (sm_89), CUDA 13.0, PyTorch 2.13.0, Python 3.13. The behavior is architecture-independent — the wrong value comes from the CUDA `fminf`/`fmaxf` NaN semantics, which are identical on every NVIDIA target; only sm_89 was run.

### Problem description

`T.clamp(x, lo, hi)` on a `NaN` input silently returns `lo` (the lower bound) instead of `NaN`. The reference semantics `T.clamp` should match are **`torch.clamp` and `numpy.clip`, both of which propagate `NaN`** (verified this session) — these are the frameworks a TileLang kernel is written against and differentially tested against. The kernel compiles and runs to completion with no error, so the wrong value is silent.

Clamping is used in the shipped fp8-quantization examples (`T.clamp(y / y_s, fp8_min, fp8_max)` in `examples/cast/example_group_per_split_token_cast_to_fp8.py:48`, `example_per_token_cast_to_fp8.py:35`, and the DeepSeek act-quant examples), where a `NaN` in the input would be quantized to `fp8_min` rather than surfacing.

`T.clamp` lowers to `min(max(x, lo), hi)`; the emitted CUDA is `min(max(A[i], -1.0f), 1.0f)`. `NaN` fed to CUDA `max`/`min` (`fmaxf`/`fminf`) returns the non-`NaN` operand, so `max(NaN, -1.0f)` gives `-1.0f` and the `NaN` is gone before the outer `min` runs.

The same `NaN`-suppression is visible in `T.max`/`T.min` on their own (not just via `T.clamp`) — see the neighbor note below.

Not a regression: `clamp` has been `min(max(...))` since it was added.

### Reproducible example code

```python
import tilelang, tilelang.language as T, torch

N = 4

@T.prim_func
def main(A: T.Tensor((N,), "float32"), C: T.Tensor((N,), "float32")):
    with T.Kernel(1, threads=N) as bx:
        i = T.get_thread_binding()
        C[i] = T.clamp(A[i], T.float32(-1.0), T.float32(1.0))

kernel = tilelang.compile(main, out_idx=[1])

a   = torch.tensor([float('nan'), 2.0, 0.5, -5.0], dtype=torch.float32, device="cuda")
got = kernel(a).cpu()
ref = torch.clamp(a.cpu(), -1.0, 1.0)                 # trusted oracle
print("T.clamp :", got.tolist())                      # -> [-1.0, 1.0, 0.5, -1.0]  NaN -> -1.0 (min bound)
print("torch   :", ref.tolist())                      # -> [nan, 1.0, 0.5, -1.0]   NaN preserved
print("NaN preserved:", torch.isnan(got[0]).item())   # -> False  (should be True)

# control: with no NaN present, T.clamp matches torch exactly
b = torch.tensor([2.0, 0.5, -5.0, 0.0], dtype=torch.float32, device="cuda")
print("finite ctrl OK:", torch.equal(kernel(b).cpu(), torch.clamp(b.cpu(), -1.0, 1.0)))  # -> True
```

### Traceback

No traceback — the kernel compiles and runs to completion; the result is silently wrong and deterministic.

### Expected behavior

`T.clamp(NaN, lo, hi)` returns `NaN`.

The reference semantics that matter most here are **`torch.clamp` and `numpy.clip`** — both propagate `NaN` (a `NaN` input yields a `NaN` output; verified this session on 0.1.13's PyTorch and NumPy). These are the libraries TileLang kernels are written against and validated against, so `T.clamp` diverging from them on `NaN` is the core defect. The finite-input control already matches `torch` exactly, so only a `NaN` operand disagrees.

This also aligns with the newer IEEE-754 direction: 754**-2019** `minimum`/`maximum` propagate `NaN` (whereas the older 754**-2008** `minNum`/`maxNum` — which is what CUDA's `fmaxf`/`fminf` follow — suppress it). So "propagate" is not a single universal rule for min/max, but it is what both dominant array libraries do and what the current IEEE revision moved to; the concrete ask is that `T.clamp` match `torch`/`numpy`. Whether that is achieved by making `T.clamp` `NaN`-transparent or by exposing an opt-in is the maintainers' call.

### Additional context

**Root cause.** `T.clamp` composes clamping out of `T.max`/`T.min`, whose CUDA lowering does not preserve `NaN`. `clamp` is defined as `T.min(T.max(dst, min_val), max_val)` at [`customize.py#L55-L56`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/language/customize.py#L55); on CUDA `T.max`/`T.min` on floats emit `max`/`min`, i.e. `fmaxf`/`fminf`, which return the non-`NaN` argument. So `T.clamp(NaN, lo, hi)` computes `min(max(NaN, lo), hi) = min(lo, hi) = lo`.

<details>
<summary>Emitted CUDA + the T.max/T.min neighbor (both run on 0.1.13, L40S)</summary>

Emitted device expression for the repro:

```c++
C[((int)threadIdx.x)] = min(max(A[((int)threadIdx.x)], -0x1p+0f), 0x1p+0f);   // min(max(A[i], -1.0f), 1.0f)
```

The building blocks drop `NaN` on their own, so this is not specific to `clamp`:

```
T.max(nan, 0.0) -> 0.0    (torch.maximum -> nan)
T.min(nan, 0.0) -> 0.0    (torch.minimum -> nan)
```

A fix targeting `clamp`'s composition (e.g. an explicit `dst != dst` re-injection of `NaN`, or a `NaN`-propagating min/max) closes `T.clamp`; the `T.max`/`T.min` primitives keep the CUDA `fmaxf`/`fminf` behavior unless they are separately changed.
</details>

**Suggested fix.** One direction is to make `clamp` `NaN`-transparent — carry the input `NaN` through, or build it from a `NaN`-propagating min/max — so `T.clamp(NaN, …)` returns `NaN` like `torch.clamp`. Whether `T.max`/`T.min` themselves should also propagate `NaN` (vs keep the `fmaxf`/`fminf` reduction semantics used by softmax-style `m_i = T.max(m_i, …)` accumulators) is a separate call for the maintainers. Not built/verified.

**Provenance.** `clamp` was introduced in [#192](https://github.com/tile-ai/tilelang/pull/192) ("[Language] Support clamp in language", merged 2025-03-12) with the `min(max(...))` body it still has; the `NaN`-dropping behavior has been present since then. Not a regression.

**Dedup.** I searched the open and closed tracker for `clamp` / `NaN` / `min max`. Distinct from [#2882](https://github.com/tile-ai/tilelang/issues/2882) (`T.max`/`T.min` on two compile-time float **constants** fold order-dependently on `NaN` via the host `const_fold.h` path); that report treats the **runtime** `max(...)` lowering as the well-defined reference — this issue is that the runtime lowering itself drops `NaN` versus `torch.clamp`/`numpy.clip` (and IEEE-754-2019). No existing report covers `T.clamp`.

**Reach.** `T.clamp` is documented and appears in shipped examples. On 0.1.13 the cited sites are present and verbatim: `T.clamp(y_local[i,j] / y_s_local[i], fp8_min, fp8_max)` at `examples/cast/example_per_token_cast_to_fp8.py:35` and `example_group_per_split_token_cast_to_fp8.py:48`, and `T.clamp(x_local[i,j] / s_local[i], fp8_min/fp8_max)` at `examples/deepseek_v32/inference/kernel.py:72` and `examples/deepseek_v4/act_quant.py:78,156`. The underlying `T.max`/`T.min` appear in ~100 example sites (softmax `m_i = T.max(...)`, `T.max(x, 0)` ReLU).

I **ran** `example_per_token_cast_to_fp8.py`'s shipped kernel verbatim on 0.1.13 (L40S). Two results: (1) with the example's shipped input (`torch.randn`, all finite) the correctness check passes exactly — the shipped example **dodges** this bug because no `NaN` ever reaches the clamp, and no test in the tree injects one. (2) Injecting a single `NaN` into one input row of the same kernel makes that row diverge from the torch reference: torch propagates `NaN` across the whole 128-element group (row0 fp8 = `[nan, nan, …]`) while TileLang emits finite fp8 values (`[-448.0, -60.0, -384.0, …]`). So the bug is reachable through the shipped kernel; the shipped test just never exercises `NaN`. (This particular divergence is compounded by `T.reduce_absmax` also dropping the `NaN` by default — see the generalization table.) The trigger requires a `NaN` reaching the clamp; finite inputs clamp correctly (control passes). CI is green because no test asserts `NaN` propagation through `T.clamp`.

**Generalization.** Root, two levels: (a) SOURCE-level — `clamp` at `tilelang/language/customize.py#L55-L56` composes out of `T.max`/`T.min` (`tilelang/language/tir/ir.py:184-193` → TIR `min`/`max`), which lower to the CUDA NaN-dropping intrinsics (`fmaxf`/`fminf` for fp32, `__hmax`/`__hmin` for fp16/bf16 — never the `_nan` variants). (b) OPERATOR-level — every op built on scalar `T.max`/`T.min` inherits the drop: `T.clamp`, elementwise `T.max`/`T.min` themselves, and (by default) the `reduce_max`/`reduce_min`/`reduce_absmax` family. 4-axis sweep, all cells RUN on 0.1.13 (L40S):

| axis | cell tested (input → observed) | same-root? |
|---|---|---|
| related-operator | `T.max(nan,0.0)→0.0`, `T.min(nan,0.0)→0.0` (torch: `nan`); but `T.max(nan,nan)→nan` (`fmaxf` returns the other operand, so `NaN` survives only when BOTH are `NaN`) | same root (elementwise; the clamp building blocks) |
| related-operator | `T.reduce_absmax` fp32, default: `[…,nan,…]→3.0` (torch amax(abs)=`nan`) | same root, **distinct face** — reduce family has a `nan_propagate=True` opt-in (`reduce_op.py`, GH-#2697) that clamp lacks; but it **defaults to dropping** and is fp16/bf16-only |
| related-type | `T.clamp` fp16: `clamp(nan,-1,1)→-1.0` (device emits `__hmax`/`__hmin`, not `__hmax_nan`) | same root |
| related-type | `T.clamp` bf16: `clamp(nan,-1,1)→-1.0` (device emits `cutlass::bfloat16 __hmax/__hmin`) | same root |
| related-type | `T.clamp` int32/int (no `NaN` representation) | N/A — does not apply (integers have no `NaN`) |
| similar-logic | reduce family got a per-call `nan_propagate` escape hatch; elementwise `T.max`/`T.min`/`T.clamp` have NO such kwarg (`git grep nan_propagate` hits only `reduce_op.py`) | same root, asymmetric coverage — the fix already exists for reductions but not for the elementwise/clamp composition |

Framing kept **specific to `T.clamp`** (title/Problem unchanged): the elementwise `T.max`/`T.min` NaN-drop is arguably intended (softmax `m_i = T.max(...)` accumulators rely on `fmaxf` reduction semantics), and the reduce family already has an opt-in, so the crisp defect is that `T.clamp` — which per `torch.clamp`/IEEE should be `NaN`-transparent — has no way to preserve `NaN`. The reduce-default NaN-drop (`reduce_absmax` etc.) is a **distinct, adjacent** behavior with an existing opt-in and test coverage; not filed here.

**Impact.** Silent-wrong, deterministic, bounded to the clamped value: a `NaN` at the input becomes the `min` bound (`lo`) with no error, so a `NaN` that a workload relies on to detect (or propagate through a quantization step) is silently replaced by a finite in-range value every run. Fixing it aligns `T.clamp` with the `torch.clamp`/`numpy.clip` `NaN` semantics kernels are validated against (and the IEEE-754-2019 direction) and removes a silent frontend/runtime disagreement.

## 评论 (1)

### yurekami · 2026-09-02

Confirmed on `main`, and there are two constraints in the way of the obvious fix that seem worth recording before anyone writes one.

## Reproduction without a GPU

`tilelang.engine.lower(f, target=...)` defaults to `enable_device_compile=False`, so the emitted CUDA can be read without nvcc or a device. For `T.clamp(A[i], 0.0, 1.0)` on `float32`:

```cuda
__2.x = max(v_.x, v__1.x);
__1.x = min(__2.x, v__2.x);
```

`fmaxf`/`fminf` return the non-NaN operand, so the NaN is discarded at the `max` and the result is `min_val`.

Worth noting that `testing/python/language/test_tilelang_language_clamp.py` already uses `torch.clamp` as its reference oracle. The existing cases just never feed a NaN, so the two semantics have not been compared on this input.

## The rewrite that looks right is wrong

Lowering to nested ordered comparisons, `x < lo ? lo : (x > hi ? hi : x)`, propagates NaN but changes the degenerate range. `torch.clamp` applies `min` first, so for `lo > hi` the upper bound wins: `clamp(-5, lo=5, hi=1)` is `1`. The nested form returns `5`. The current `min(max(...))` gets this case right, so a fix has to preserve it.

## `x != x` does not survive the simplifier

The natural guard, `Select(dst != dst, dst, clamped)`, disappears before codegen. The arithmetic simplifier folds it:

```
x != x   -> T.bool(False)
x - x    -> T.float32(0.0)
x * 0.0  -> T.float32(0.0)
```

which is the same NaN-unsafe folding reported in #2638. Only the opaque `T.isnan` intrinsic survives to codegen, where it lowers to `A != A`.

Two smaller edges in that direction: `T.isnan` rejects `bfloat16` outright (`Data type bfloat16 not supported for isnan op`), so that test has to widen to `float32`; and `T.min`/`T.max` promote a narrow `dst` against `float` bounds, so a `Select` whose other branch is the unpromoted `dst` fails TVM's `false_value.dtype() == true_value.dtype()` check on `float16`.

## What passes

`isnan(x) ? x : min(max(x, lo), hi)`, which is the form `torch.clamp` itself uses, applied only when `dst` is `FLOAT` or `BFLOAT` so integer clamps keep the plain `min`/`max` lowering. Against `torch.clamp` over 4007 inputs (including NaN, both infinities, signed zeros, subnormals) crossed with five bound-sets including `lo > hi` and `lo == hi`, the current lowering disagrees on all five bound-sets and this one on none.

## The open question

In the emitted source the `min`/`max` form produces two-wide lane writes and the guarded form does not, so this may cost vectorization on `T.Parallel` clamps. `T.clamp` is on the hot path of the shipped fp8 quantization examples (`examples/cast/example_per_token_cast_to_fp8.py` and the DeepSeek act-quant examples), which is exactly where that would matter. I have no GPU here and cannot benchmark it, so I would rather not guess whether the correctness fix is worth the instruction count, or whether it should be gated behind a flag or applied only where NaN is reachable.

I have the change and its tests ready and will open a PR if the unconditional fix is the direction you want. If you would rather keep the fast path and document the NaN behavior instead, that is a smaller change and I am happy to do that one.

(Investigated with Claude Code; all output above was produced locally.)


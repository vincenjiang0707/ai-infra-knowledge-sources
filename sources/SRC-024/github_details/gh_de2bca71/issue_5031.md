# [Issue #5031] [RFC]: Replace the hardcoded `atol=100` in the MoE op_tests with a derived tolerance

source: https://github.com/ROCm/aiter/issues/5031
state: open | updated: 2026-09-08T15:54:15Z
labels: 

## 正文

### Motivation.

**In short:** six `checkAllclose` calls in the MoE op_tests share one hardcoded
`atol=100` across six quantization algorithms. The right `(rtol, atol)` depends
on dtype, reduction depth and data magnitude, the way Composable Kernel already
does. A single constant cannot sit in the right place for all of them.

**Status: the attached patch is a prototype and should not land as written.**
I ran it on an MI300X before asking anyone to review it, and it flips the int8
path from pass to fail. Working the logged numbers through afterwards shows
the first-pass diagnosis — "the quantization term must scale with reduction
depth" — is too coarse to act on. `√K` overshoots, `K` is useless, and a
corrected int8 bound at this depth lands *looser* than the shipped `atol=100`.
The argument for *deriving* the tolerance from the tensor still stands; this
particular formula should not ship.

Size, if you want to look at the diff: **48 added and 6 removed lines across the
two existing op_tests**, plus 271 lines in two new files. The helper is
dependency-free and its unit tests run on CPU in a few seconds with no GPU, no
ROCm and no JIT build (`python op_tests/test_tolerance.py`, 8 assertions).

---

`op_tests/test_moe.py` and `op_tests/test_moe_tkw1.py` compare the fused MoE
kernels against a torch reference through six `checkAllclose` calls, and all
six pass the same hardcoded absolute tolerance:

| File | Line | Call |
|---|---|---|
| `test_moe.py` | 199 | `checkAllclose(ref2, out_b, rtol=0.01, atol=100, msg=msg)` |
| `test_moe.py` | 314 | `checkAllclose(ref2, out_b2, atol=100, msg=msg)` |
| `test_moe.py` | 317 | `checkAllclose(ref2, out_b, rtol=0.01, atol=100, msg=msg)` |
| `test_moe_tkw1.py` | 194 | `checkAllclose(ref2, out_b, rtol=0.01, atol=100, msg=msg)` |
| `test_moe_tkw1.py` | 299 | `checkAllclose(ref2, out_b2, atol=100, msg=msg)` |
| `test_moe_tkw1.py` | 302 | `checkAllclose(ref2, out_b, rtol=0.01, atol=100, msg=msg)` |

Those call sites are reached under all six entries of `quant_algo`, which span
unquantized bf16 through int4 weights with fp8 activations:

```python
quant_algo = [
    "No", "int8quant", "fp8quant",
    "int8smoothquant", "fp8smoothquant", "wint4afp8smoothquant",
]
```

The absolute tolerance those pipelines warrant is not one number. It depends on
the weakest precision in the pipeline and on the magnitude of the data, and
both vary across the cases the same constant is applied to.

Composable Kernel already derives this from mantissa bits, accumulator
precision, reduction length and the magnitude of the reference
(`get_relative_threshold` / `get_absolute_threshold`):

```
rtol = max(u(compute), u(output), u(acc) * K)
atol = same, placed in the floored binary exponent band of max|ref|
```

with `u(t) = 2**-mant * 0.5`. I extended that to integer quantization
containers (`0.5/127` for symmetric int8, `0.5/7` for the int4 path) and
applied it at the six call sites. **That extension is the defect the GPU run
found.** CK's `u(compute)` is one rounding of a float compute dtype. Treating
an int8 *scale* as the same thing under-counts the error we actually measured.
The gap is not closed by multiplying that term by `√K` or `K` either; the
working is under *Hardware measurement*.

For reference only, here is what that one-rounding model prints at the
magnitudes these two tests actually produce (measured on MI300X: max `|ref|`
between 1928 and 6304, so the `2**10` and `2**12` exponent bands). These are
**not** the warranted tolerances; they are the numbers the prototype used,
and the int8 row is the one the hardware run falsified.

| quant | one-rounding rtol | atol @ \|ref\|=1928 | atol @ \|ref\|=6304 |
|---|---|---|---|
| `No` | 0.003906 | 8 | 32 |
| `int8quant` | 0.003937 | 8 | 32 |
| `fp8quant` | 0.0625 | 64 | 256 |
| `int8smoothquant` | 0.003937 | 8 | 32 |
| `fp8smoothquant` | 0.0625 | 64 | 256 |
| `wint4afp8smoothquant` | 0.07143 | 73.14 | 292.6 |

A note on magnitude, because it is easy to talk past each other here. These
1928–6304 figures are from the op_tests' `randn` init, not from a real forward
pass. In that synthetic band `atol=100` is 1.6–5% of the output range, not a
no-op. On a typical decoder-block down_proj the output is much smaller, and
the same constant is a much larger fraction of the data. Either way the problem
is that it is one constant for every dtype and every magnitude.

#### This has cost people time already

* **#600** (`test_moe_tkw1.py`) prints `[checkAllclose atol=100 rtol=0.01
  failed!]` on four consecutive configurations, with values around 1824–2008
  and deltas of 103, 118, 184, 108. bf16 has an 8-bit significand, so one ULP
  at 1824 is 8. The 103 delta cleared `atol=100` by a hair; 184 is 1.8× over.
  Anything up to 100 in that tensor is reported as a pass.
* **#2421** (open) asks whether "~3.5% of elements exceeding 0.03 atol, with max
  ~0.09" is expected for fp8 fused MoE on gfx950. There is no mechanical way to
  answer that today.
* **#4788** used a *different* comparison (`checkAllclose(rtol=atol=0.05)`),
  not `atol=100`. Its reporter found that bound too tight for fp8, flagging
  ~24% of elements on kernels they had independently established were correct.
  That is still the same disease — a hardcoded constant in the wrong place —
  but it is not evidence about this particular `atol=100`.

### Proposed Change.

Add `aiter/utility/tolerance.py`, a small dependency-free helper that returns
`(rtol, atol)` from the error model, and call it at the six sites. Prototyped in
the patch attached below. **Do not land that patch.** What I want from this RFC
is agreement on the shape of the helper — in particular that it reads magnitude
off the reference tensor rather than predicting it from weight statistics —
not a merge of the prototype, and not a decision between `√K` and `K`.

```python
def derive_tolerance(
    compute_dtype,            # dtype the math runs in -- the weakest link,
                              # not the bf16 output
    output_dtype,
    acc_dtype=torch.float32,  # MFMA accumulates in fp32
    num_accumulations=1,      # reduction length K
    max_value=1.0,            # magnitude of the largest reference value
    compute_dtype_max=None,   # integer amplitude, see below
    safety_factor=1.0,
): ...

def tolerance_for(reference, compute_dtype, ...): ...
```

CK's float rule is `rtol = max(u(compute), u(output), u(acc) * K)`, with `atol`
scaled into the floored binary exponent band of `max_value`, and with the
output-cast term taking a full ULP rather than half so that a hardware bf16
rounding that lands on the adjacent code to the software one is not counted as
an error. An integer *output* is still compared bit-exactly.

The prototype then treats an integer *compute* dtype as a quantization
container whose error is `0.5 / dtypeMax` (127 or 7), appearing once in the
`max(...)`. That one-rounding term is what the GPU run falsified. Two other
composition choices in the prototype are also suspect:

* The call sites pass `num_accumulations=model_dim + inter_dim` (3840 on the
  measured shape). Two sequential GEMMs plus SiLU is not one reduction of
  length K1+K2. Stage-1 error is multiplied by W2. And even as written, K only
  scales `u_acc`, which is inert next to `u_compute`.
* `a8w8` / `wint4afp8` pipelines have activation quantization as well as
  weight quantization. The prototype models only the weight container.

What the prototype already gets right, and is worth keeping regardless of how
the int8 term is rewritten: `tolerance_for` sizes `atol` from
`reference.abs().max()` on the actual tensor. A depth-aware rule that tracked
weight scale would miss the RMSNorm `γ` that actually moves the GEMM operating
point; whatever that scale did on the way is already in the reference. That is
an argument for a tensor-derived helper over any lookup table or closed-form
predictor of magnitude.

The matching weakness: a single scalar `atol` keyed to the global max is loose
for the bulk of a heavy-tailed tensor. On measured decoder weights,
`abs_max / std` runs 3.2–13.7× above the Gaussian expectation, so most elements
sit far below the max the bound is sized for. That is the same dilution
#5032 is fixing in the tuner, and it suggests the coherent next step is a
per-row (or p99-keyed) tolerance rather than a better global constant.

At the call sites this currently reads:

```python
# Two reductions compose: stage1 over model_dim, stage2 over inter_dim.
rtol, atol = tolerance_for(
    ref2, compute_dtype=quant_dtype,
    num_accumulations=model_dim + inter_dim,
    compute_dtype_max=quant_amplitude,
)
checkAllclose(ref2, out_b, rtol=rtol, atol=atol, msg=msg)
```

### Feedback Period.

Two weeks. The remaining design question is a measured or condition-aware
int8 term, not a closed form in `K`.

### CC List.

_Owners of `op_tests/test_moe.py`, `op_tests/test_moe_tkw1.py`, and the fused
MoE kernels._

### Any Other Things.

#### Reproducer

`atol100_tolerance.py` — CPU-only, torch is the only dependency, no AITER import
and no GPU. The derivation is inlined so it does not depend on the patch. It
prints the one-rounding table above. Treat that table as a description of the
prototype, not as the bound we should ship.

`int8_k_scaling_check.py` — also CPU-only, no torch. Replays the logged int8
failure through the formula (reproduces `rtol=0.003937007874015748` exactly)
and through `√K` / `K` multipliers. The table under *Hardware measurement*
is this script's output.

#### Hardware measurement, and the defect it found

I ran the patched op_tests on an MI300X (gfx942) against `536118a`, stock versus
patched on the same machine with identical shapes and identical kernels, so the
only difference between the two runs is the patch. Shapes: `--token 32
--hidden_dim 2048 --inter_dim 1792 --expert 32 --topk 5`, bf16 output.

| test | stock | patched | verdict |
|---|---|---|---|
| `g1u1_fp8quant` | `atol=100 rtol=0.01` → `passed~` | `atol=64 rtol=0.0625` → `passed~` | unchanged |
| `g1u1_int8quant` | `atol=100 rtol=0.01` → `passed~` | `atol=8 rtol=0.003937` → `failed!` | **pass → fail** |

```
[checkAllclose atol=8.0 rtol=0.003937007874015748 failed!]
    a: tensor([ 460.0000, -211.0000, -121.5000,  251.0000,  704.0000, ...])
    b: tensor([ 448.0000, -198.0000, -132.0000,  238.0000,  672.0000, ...])
    delta: tensor([12.0000, 13.0000, 10.5000, 13.0000, 32.0000, ...])
-->max abs delta:72.0, delta details: 46.9% (30721 of 65536) elements
```

**This is a defect in the derivation above, not a kernel bug.** The formula
reproduces the logged `rtol=0.003937007874015748` exactly, so the reading is
right. Those `rtol` values decode as exactly *one* quantization rounding:
`0.003937 = 1/(2·127)` for symmetric int8, `0.0625 = 2⁻⁴` for fp8 e4m3.

A detail that is easy to get backwards: **`rtol` and `atol` are bound by
different terms.** `rtol` is set by `u_compute` (the int8 container). `atol`
is set by the bf16 output-cast (`u_output * 2 = 0.0078125`), not by
quantization. The call site passes `num_accumulations = model_dim + inter_dim
= 3840`, not 2048, but that K only scales the fp32 accumulator term, which at
this depth is 17× *smaller* than `u_compute` (`u_acc * K = 0.000229`). The K
factor is inert either way; the quantization charge does not move with depth.

fp8 survives only because its unit roundoff is large enough to absorb the
error; int8's is not, and it fails on 46.9% of elements rather than a handful.
On the printed elements the observed median relative error is 6.16% against a
charged `rtol` of 0.394% — short by 15.6×. Observed max abs delta is 72, which
stock `atol=100` still accepts.

The standing first-pass recommendation was "the quantization term must scale
with reduction depth." Working the same numbers shows that is too coarse to
act on:

| model | what it does at this shape | vs stock 100 | vs observed 72 |
|---|---|---|---|
| one rounding (the prototype) | rtol 0.003937, atol 8 | 12× tighter | fails |
| multiply the quant term by `√K` (K=3840, √K≈62) | atol ≈ 250 | looser | passes, overshoots the observed 15.6× gap by ~4× |
| multiply the quant term by `K` | atol 15481 | accepts anything | useless |

In a random-sign dot product the signal *and* the rounding error both grow as
`√K`, so relative error is roughly K-invariant and the depth factor largely
cancels. The 15.6× gap is therefore not raw reduction depth — it comes from
cancellation (the condition number of the sum) compounded across the two GEMM
stages and the SiLU between them. That is data-dependent. No pure function of
`K` closes it.

Two things fall out before any redesign:

* A physically-corrected int8 bound at this depth lands *looser* than the
  shipped `atol=100`. "`atol=100` is too loose" holds for the bf16 and fp8
  paths (one-rounding still says 8–32 and 64–256 at these magnitudes) but
  **not for int8 here**.
* A redesign needs a measured safety factor or a condition-aware term, not
  another closed form in `K`.

The fp8 row of the A/B is still useful as a measurement of what the prototype
*does*, not as a claim that 64/0.0625 is the right bound: the same patch moves
fp8's `atol` from 100 down to 64 while moving its `rtol` from 0.01 up to 0.0625,
and the verdict stays `passed~`.

The bf16 no-quant path could not be measured. `test_moe.py` aborts there with a
GPU memory access fault loading `fmoe_b16.co`, on a clean `536118a` tree with
the patch reverted, so it is independent of anything proposed here. It resembles
the fault reported in #456; happy to open that separately if useful. Until that
path runs, the "kernel that adds 99.0 would pass on unquantized bf16" statement
is a property of the one-rounding formula at these magnitudes, not a measured
kernel error.

#### An earlier offline estimate, now superseded

Before running on hardware I estimated blast radius by re-deciding 353 recorded
`checkAllclose` comparisons offline, and reported no pass→fail flips. That
estimate did not cover the int8 path at this shape, and the hardware run above
supersedes it. Recording it here because the reasoning is still worth knowing:
only 14 of the 353 could be re-decided at all. `checkAllclose` sees output
tensors only, so the compute dtype a derived tolerance needs is not recoverable
from its arguments — which is why the proposed helper takes `compute_dtype`
explicitly. The remaining 339 comparisons (336 from `test_gemm_a8w8.py`, plus
three `a8w8 asm vs a16w8 asm` comparisons in `test_moe.py`) carry no `quant=`
tag and so have no derived verdict.

#### Relationship to the other two issues

These six comparisons currently cannot fail a build at all, because
`checkAllclose` only logs; that is filed separately as #5030. Calibrating the
tolerance and making failures fail are complementary — neither is much use
without the other. The int8 result above is a concrete argument for landing
#5030 first and keeping it default-off: once a wrong verdict can actually
redden CI, a mis-derived tolerance stops being a cosmetic problem, so the
tolerance has to be right before the gate is armed.

A global `atol` keyed to `max|ref|` is also loose on the bulk of a heavy-tailed
tensor, which is the same weakness #5032 is fixing in the tuner with per-row
scoring. If this helper is rewritten, per-row (or p99-keyed) tolerance is the
coherent next step rather than a better single scalar.

#### Patch

Against `536118a`. Inlined below rather than attached — I cannot fork this
repository from my account, so if maintainers would rather review this as a
pull request, say so and I will arrange a branch.

```
 aiter/utility/tolerance.py | 166 +++++++++++++++++++++++++++++++++++++
 op_tests/test_moe.py       |  27 +++++-
 op_tests/test_moe_tkw1.py  |  27 +++++-
 op_tests/test_tolerance.py | 105 ++++++++++++++++++++++
```

<details>
<summary>Full patch (<code>derived-tolerance-moe.patch</code>, 448 lines) — <code>git am</code> applies it on <code>536118a</code></summary>

```diff
From 2ced4f195f5e36c571ceb814c2d78ee86825f40e Mon Sep 17 00:00:00 2001
From: KHassanQazi <281752142+KHassanQazi@users.noreply.github.com>
Date: Tue, 18 Aug 2026 18:18:58 -0400
Subject: [PATCH] op_tests/moe: derive the comparison tolerance instead of
 atol=100

The six checkAllclose calls in test_moe.py and test_moe_tkw1.py share one
hardcoded atol=100 across six quantization algorithms, from unquantized
bf16 through int4 weights with fp8 activations. The correct absolute
tolerance for those paths spans 9x at a fixed magnitude, and scales with
the magnitude of the data on top of that, so no single constant fits. At
the magnitudes these tests actually produce (max |ref| measured between
1928 and 6304 on MI300X), 100 runs from 3.1x to 12.5x too loose on the
bf16 and int8 paths; on the fp8 and int4 paths it is too loose at the
bottom of that range and too tight at the top.

Add aiter/utility/tolerance.py, which derives (rtol, atol) from mantissa
bits, accumulator precision, reduction length and the magnitude of the
reference, following Composable Kernel's get_relative_threshold /
get_absolute_threshold. CK already handles fp8 and bf16 directly; what
this adds is the integer quantization containers, whose error comes from
the amplitude the values were scaled into rather than from a mantissa
width. Use it at the six call sites.

Co-authored-by: Cursor <cursoragent@cursor.com>
Signed-off-by: KHassanQazi <281752142+KHassanQazi@users.noreply.github.com>
---
 aiter/utility/tolerance.py | 166 +++++++++++++++++++++++++++++++++++++
 op_tests/test_moe.py       |  27 +++++-
 op_tests/test_moe_tkw1.py  |  27 +++++-
 op_tests/test_tolerance.py | 105 +++++++++++++++++++++++
 4 files changed, 319 insertions(+), 6 deletions(-)
 create mode 100644 aiter/utility/tolerance.py
 create mode 100644 op_tests/test_tolerance.py

diff --git a/aiter/utility/tolerance.py b/aiter/utility/tolerance.py
new file mode 100644
index 0000000..7040065
--- /dev/null
+++ b/aiter/utility/tolerance.py
@@ -0,0 +1,166 @@
+# SPDX-License-Identifier: MIT
+# Copyright (C) 2024-2026, Advanced Micro Devices, Inc. All rights reserved.
+"""Derive checkAllclose tolerances from the dtype error model.
+
+The tolerance for comparing a kernel against a higher-precision reference is
+determined by three things, none of which are constants across a test file:
+
+  * the precision the math is actually carried out in (the *weakest* link in a
+    quantized pipeline, not the output dtype),
+  * the accumulator precision and the reduction length ``K``,
+  * the magnitude of the values being compared.
+
+This mirrors Composable Kernel's ``get_relative_threshold`` /
+``get_absolute_threshold``, which is the existing mantissa-derived tolerance in
+the ROCm stack, and extends it to the FP8/FP4 and integer-quantized formats
+AITER uses.
+
+Typical use in an op_test::
+
+    from aiter.utility.tolerance import tolerance_for
+
+    rtol, atol = tolerance_for(ref, compute_dtype=quant_dtype, num_accumulations=K)
+    checkAllclose(ref, out, rtol=rtol, atol=atol, msg=msg)
+"""
+
+import math
+
+import torch
+
+__all__ = [
+    "derive_tolerance",
+    "tolerance_for",
+    "unit_roundoff",
+]
+
+# Explicit stored mantissa bits, excluding the implicit leading 1. The unit
+# roundoff of a float format is u = 2**-mant * 0.5 -- half a ULP at magnitude 1.
+_MANTISSA_BITS = {
+    torch.float64: 52,
+    torch.float32: 23,
+    torch.float16: 10,
+    torch.bfloat16: 7,
+    torch.float8_e4m3fn: 3,
+    torch.float8_e4m3fnuz: 3,
+    torch.float8_e5m2: 2,
+    torch.float8_e5m2fnuz: 2,
+}
+
+for _name, _bits in (("float4_e2m1fn_x2", 1), ("float8_e8m0fnu", 0)):
+    _dtype = getattr(torch, _name, None)
+    if _dtype is not None:
+        _MANTISSA_BITS[_dtype] = _bits
+
+
+def unit_roundoff(dtype, dtype_max=None):
+    """Largest relative representation error of ``dtype``.
+
+    Float formats: ``2**-mant * 0.5``.
+
+    Integer formats are only a quantization *container*; their error depends on
+    the scale, so pass ``dtype_max`` -- the integer amplitude the values were
+    scaled into (127 for symmetric int8, 7 for the int4 path). The step is then
+    ``1/dtype_max`` of full scale and the rounding error is half of that.
+    Without ``dtype_max`` an integer dtype is treated as exact, which is the
+    right answer for index and counter tensors.
+    """
+    if dtype in _MANTISSA_BITS:
+        return math.ldexp(0.5, -_MANTISSA_BITS[dtype])
+    if not dtype.is_floating_point:
+        return 0.0 if dtype_max is None else 0.5 / float(dtype_max)
+    raise ValueError(f"No error model for dtype {dtype!r}")
+
+
+def derive_tolerance(
+    compute_dtype,
+    output_dtype,
+    acc_dtype=torch.float32,
+    num_accumulations=1,
+    max_value=1.0,
+    compute_dtype_max=None,
+    safety_factor=1.0,
+):
+    """Return ``(rtol, atol)`` for one comparison.
+
+    Args:
+        compute_dtype: dtype the math is carried out in. For a quantized
+            pipeline this is the quantized dtype, not the bf16 output -- the
+            weakest link sets the error.
+        output_dtype: dtype the result is stored as.
+        acc_dtype: accumulator dtype. MFMA GEMM accumulates in fp32.
+        num_accumulations: reduction length ``K``. Scales the accumulator term
+            only; with an fp32 accumulator the quantization term dominates for
+            any realistic ``K``.
+        max_value: magnitude of the largest reference value, used to place
+            ``atol`` in the right binary exponent band.
+        compute_dtype_max: integer amplitude, when ``compute_dtype`` is an
+            integer quantization container. See :func:`unit_roundoff`.
+        safety_factor: multiplier >= 1 for datapaths that are not
+            round-to-nearest deterministic, e.g. stochastic rounding or an
+            autotuner that reorders the reduction.
+
+    Returns:
+        ``(rtol, atol)``, both non-negative. An exact (integer) pipeline
+        returns ``(0.0, 0.0)``.
+    """
+    if num_accumulations < 1:
+        raise ValueError("num_accumulations must be >= 1")
+    if safety_factor < 1.0:
+        raise ValueError("safety_factor must be >= 1; it may only loosen")
+
+    u_compute = unit_roundoff(compute_dtype, compute_dtype_max)
+    u_output = unit_roundoff(output_dtype)
+    u_acc = unit_roundoff(acc_dtype)
+
+    # An integer output holds no rounding error no matter what the pipeline
+    # did on the way, so the comparison is bit-exact.
+    if u_output == 0.0:
+        return 0.0, 0.0
+
+    rtol = safety_factor * max(u_compute, u_output, u_acc * num_accumulations)
+
+    if max_value == 0.0 or not math.isfinite(max_value):
+        expo = 0
+    else:
+        expo = math.floor(math.log2(abs(max_value)))
+    scale = math.ldexp(1.0, expo)
+
+    # The output-cast term uses a full ULP rather than half: hardware and
+    # software rounding of the same fp32 value to bf16 can legitimately land on
+    # adjacent codes at a tie.
+    atol = (
+        safety_factor
+        * scale
+        * max(
+            u_compute,
+            u_output * 2.0,
+            u_acc * num_accumulations,
+        )
+    )
+    return rtol, atol
+
+
+def tolerance_for(
+    reference,
+    compute_dtype,
+    acc_dtype=torch.float32,
+    num_accumulations=1,
+    compute_dtype_max=None,
+    safety_factor=1.0,
+):
+    """:func:`derive_tolerance` with ``output_dtype`` and ``max_value`` read off
+    the reference tensor."""
+    finite = torch.isfinite(reference)
+    if finite.any():
+        max_value = float(reference[finite].abs().max().item())
+    else:
+        max_value = 1.0
+    return derive_tolerance(
+        compute_dtype=compute_dtype,
+        output_dtype=reference.dtype,
+        acc_dtype=acc_dtype,
+        num_accumulations=num_accumulations,
+        max_value=max_value,
+        compute_dtype_max=compute_dtype_max,
+        safety_factor=safety_factor,
+    )
diff --git a/op_tests/test_moe.py b/op_tests/test_moe.py
index 0dec927..3a4544d 100644
--- a/op_tests/test_moe.py
+++ b/op_tests/test_moe.py
@@ -11,6 +11,7 @@ from aiter.fused_moe_bf16_asm import asm_moe
 from aiter.int4_utils import *
 from aiter.ops.shuffle import shuffle_weight
 from aiter.test_common import checkAllclose, perftest
+from aiter.utility.tolerance import tolerance_for
 
 BLOCK_SIZE_M = 32
 
@@ -196,9 +197,20 @@ def test_fmoe(
             )
 
         msg = f"[perf] {token=}, quant={quantstr}, {model_dim=}, {inter_dim=}, {E=}, {topk=}, dtype: {dtype}, torch_avg: {avg_c:<8.2f} us, asm_avg: {avg_b:>8.2f} us, uplift: {avg_c/avg_b-1:.1%}"
-        checkAllclose(ref2, out_b, rtol=0.01, atol=100, msg=msg)
+        # Two reductions compose: stage1 over model_dim, stage2 over inter_dim.
+        rtol, atol = tolerance_for(
+            ref2, compute_dtype=dtype, num_accumulations=model_dim + inter_dim
+        )
+        checkAllclose(ref2, out_b, rtol=rtol, atol=atol, msg=msg)
     else:
         dtypeMax = 7 if use_int4 else None
+        # Integer containers carry no precision of their own; the amplitude the
+        # values are scaled into is what sets the quantization step.
+        quant_amplitude = (
+            dtypeMax
+            if dtypeMax is not None
+            else (127 if quant_dtype == dtypes.i8 else None)
+        )
         w1, fc1_scale = pertoken_quant(w1, quant_dtype=quant_dtype, dtypeMax=dtypeMax)
         w2, fc2_scale = pertoken_quant(w2, quant_dtype=quant_dtype, dtypeMax=dtypeMax)
 
@@ -279,6 +291,15 @@ def test_fmoe(
             f"[BW  ] {token=}, quant={quantstr}, {model_dim=}, {inter_dim=}, {E=}, {shared_E=}, {topk=}, dtype: {dtype}, asm_bandwidth: {bw:>8.2f}TB/s"
         )
 
+        # The quantized weights are the weakest link in both the a8w8 and the
+        # a16w8 pipeline, so they set the tolerance in both.
+        rtol, atol = tolerance_for(
+            ref2,
+            compute_dtype=quant_dtype,
+            num_accumulations=model_dim + inter_dim,
+            compute_dtype_max=quant_amplitude,
+        )
+
         if (
             use_smooth
             and (
@@ -311,10 +332,10 @@ def test_fmoe(
                 activation=activation,
             )
             msg = f"[perf] a8w8 asm: {avg_b:>8.2f} vs a16w8 asm: {avg_b2:>8.2f} ......"
-            checkAllclose(ref2, out_b2, atol=100, msg=msg)
+            checkAllclose(ref2, out_b2, rtol=rtol, atol=atol, msg=msg)
 
         msg = f"[perf] {use_g1u1=} {token=}, quant={quantstr}, {model_dim=}, {inter_dim=}, {E=}, {shared_E=}, {topk=}, dtype: {dtype}, torch_avg: {avg_c:<8.2f} us, asm_avg: {avg_b:>8.2f} us ...... uplift: {avg_c/avg_b-1:.1%}"
-        checkAllclose(ref2, out_b, rtol=0.01, atol=100, msg=msg)
+        checkAllclose(ref2, out_b, rtol=rtol, atol=atol, msg=msg)
 
 
 parser = argparse.ArgumentParser(
diff --git a/op_tests/test_moe_tkw1.py b/op_tests/test_moe_tkw1.py
index 185d538..5281e60 100644
--- a/op_tests/test_moe_tkw1.py
+++ b/op_tests/test_moe_tkw1.py
@@ -14,6 +14,7 @@ from aiter.fused_moe_bf16_asm import (
 from aiter.int4_utils import *
 from aiter.ops.shuffle import shuffle_weight
 from aiter.test_common import checkAllclose, perftest
+from aiter.utility.tolerance import tolerance_for
 
 BLOCK_SIZE_M = 32
 
@@ -191,9 +192,20 @@ def test_fmoe(
             out_b, avg_b = asm_moe_test(input, w1b, w2b, topk_weights, topk_ids)
 
         msg = f"[perf] {token=}, quant={quantstr}, {model_dim=}, {inter_dim=}, {E=}, {topk=}, dtype: {dtype}, torch_avg: {avg_c:<8.2f} us, asm_avg: {avg_b:.2f} us, uplift: {avg_c/avg_b-1:.1%}"
-        checkAllclose(ref2, out_b, rtol=0.01, atol=100, msg=msg)
+        # Two reductions compose: stage1 over model_dim, stage2 over inter_dim.
+        rtol, atol = tolerance_for(
+            ref2, compute_dtype=dtype, num_accumulations=model_dim + inter_dim
+        )
+        checkAllclose(ref2, out_b, rtol=rtol, atol=atol, msg=msg)
     else:
         dtypeMax = 7 if use_int4 else None
+        # Integer containers carry no precision of their own; the amplitude the
+        # values are scaled into is what sets the quantization step.
+        quant_amplitude = (
+            dtypeMax
+            if dtypeMax is not None
+            else (127 if quant_dtype == dtypes.i8 else None)
+        )
         w1, fc1_scale = pertoken_quant(w1, quant_dtype=quant_dtype, dtypeMax=dtypeMax)
         w2, fc2_scale = pertoken_quant(w2, quant_dtype=quant_dtype, dtypeMax=dtypeMax)
 
@@ -274,6 +286,15 @@ def test_fmoe(
             f"[BW  ] {token=}, quant={quantstr}, {model_dim=}, {inter_dim=}, {E=}, {shared_E=}, {topk=}, dtype: {dtype}, asm_bandwidth: {bw:.2f}TB/s"
         )
 
+        # The quantized weights are the weakest link in both the a8w8 and the
+        # a16w8 pipeline, so they set the tolerance in both.
+        rtol, atol = tolerance_for(
+            ref2,
+            compute_dtype=quant_dtype,
+            num_accumulations=model_dim + inter_dim,
+            compute_dtype_max=quant_amplitude,
+        )
+
         if (
             use_smooth
             and (inter_dim % 512 == 0 or inter_dim % 320 == 0)
@@ -296,10 +317,10 @@ def test_fmoe(
                 activation=activation,
             )
             msg = f"[perf] a8w8 asm: {avg_b:.2f} vs a16w8 asm: {avg_b2:.2f} ......"
-            checkAllclose(ref2, out_b2, atol=100, msg=msg)
+            checkAllclose(ref2, out_b2, rtol=rtol, atol=atol, msg=msg)
 
         msg = f"[perf] {use_g1u1=} {token=}, quant={quantstr}, {model_dim=}, {inter_dim=}, {E=}, {shared_E=}, {topk=}, dtype: {dtype}, torch_avg: {avg_c:<8.2f} us, asm_avg: {avg_b:.2f} us ...... uplift: {avg_c/avg_b-1:.1%}"
-        checkAllclose(ref2, out_b, rtol=0.01, atol=100, msg=msg)
+        checkAllclose(ref2, out_b, rtol=rtol, atol=atol, msg=msg)
 
 
 parser = argparse.ArgumentParser(
diff --git a/op_tests/test_tolerance.py b/op_tests/test_tolerance.py
new file mode 100644
index 0000000..df768c4
--- /dev/null
+++ b/op_tests/test_tolerance.py
@@ -0,0 +1,105 @@
+# SPDX-License-Identifier: MIT
+# Copyright (C) 2024-2026, Advanced Micro Devices, Inc. All rights reserved.
+"""Unit tests for the derived-tolerance helper. CPU-only."""
+
+import torch
+
+from aiter.utility.tolerance import derive_tolerance, tolerance_for, unit_roundoff
+
+
+def test_unit_roundoff_float_formats():
+    assert unit_roundoff(torch.float32) == 2**-24
+    assert unit_roundoff(torch.float16) == 2**-11
+    assert unit_roundoff(torch.bfloat16) == 2**-8
+    assert unit_roundoff(torch.float8_e4m3fnuz) == 2**-4
+    assert unit_roundoff(torch.float8_e5m2) == 2**-3
+
+
+def test_unit_roundoff_integer_needs_amplitude():
+    # An index tensor is exact.
+    assert unit_roundoff(torch.int32) == 0.0
+    # A quantization container's error comes from the amplitude it is scaled to.
+    assert unit_roundoff(torch.int8, 127) == 0.5 / 127
+    assert unit_roundoff(torch.int8, 7) == 0.5 / 7
+
+
+def test_atol_tracks_the_binary_exponent_of_the_data():
+    # bf16 output, bf16 compute: the full-ULP output-cast term dominates, so
+    # atol is 2**-7 of the exponent band the data sits in.
+    for magnitude, expected in ((1.0, 2**-7), (2048.0, 16.0), (4096.0, 32.0)):
+        _, atol = derive_tolerance(
+            torch.bfloat16,
+            torch.bfloat16,
+            num_accumulations=8192,
+            max_value=magnitude,
+        )
+        assert atol == expected, f"{magnitude}: got {atol}, want {expected}"
+
+
+def test_quantized_compute_dominates_the_bf16_output_cast():
+    # fp8 e4m3 has 3 mantissa bits: u = 2**-4 = 0.0625, far above bf16's
+    # 2**-8, so the quantization error sets the tolerance.
+    rtol, atol = derive_tolerance(
+        torch.float8_e4m3fnuz,
+        torch.bfloat16,
+        num_accumulations=8192,
+        max_value=4096.0,
+    )
+    assert rtol == 2**-4
+    assert atol == 256.0
+
+
+def test_derived_atol_spans_an_order_of_magnitude_across_quant_algos():
+    # The six quant algorithms in test_moe.py, at one fixed magnitude.
+    cases = [
+        (torch.bfloat16, None),
+        (torch.int8, 127),
+        (torch.float8_e4m3fnuz, None),
+        (torch.int8, 7),
+    ]
+    atols = [
+        derive_tolerance(
+            dt,
+            torch.bfloat16,
+            num_accumulations=8192,
+            max_value=2048.0,
+            compute_dtype_max=amp,
+        )[1]
+        for dt, amp in cases
+    ]
+    assert max(atols) / min(atols) > 8, atols
+
+
+def test_exact_pipeline_is_bit_exact():
+    assert derive_tolerance(torch.int32, torch.int32) == (0.0, 0.0)
+
+
+def test_safety_factor_only_loosens():
+    base = derive_tolerance(torch.bfloat16, torch.bfloat16, max_value=1024.0)
+    loose = derive_tolerance(
+        torch.bfloat16, torch.bfloat16, max_value=1024.0, safety_factor=2.0
+    )
+    assert loose == (base[0] * 2, base[1] * 2)
+    for bad in (0.5, 0.0):
+        try:
+            derive_tolerance(torch.bfloat16, torch.bfloat16, safety_factor=bad)
+        except ValueError:
+            continue
+        raise AssertionError(f"safety_factor={bad} should have been rejected")
+
+
+def test_tolerance_for_reads_the_reference():
+    ref = torch.zeros(4, 4, dtype=torch.bfloat16)
+    ref[0, 0] = 4096.0
+    ref[0, 1] = float("inf")  # ignored when sizing the magnitude
+    rtol, atol = tolerance_for(ref, compute_dtype=torch.float8_e4m3fnuz)
+    assert rtol == 2**-4
+    assert atol == 256.0
+
+
+if __name__ == "__main__":
+    for name, fn in sorted(globals().items()):
+        if name.startswith("test_") and callable(fn):
+            fn()
+            print(f"ok  {name}")
+    print("all tolerance tests passed")
-- 
2.54.0.windows.1
```

</details>


## 评论 (1)

### KHassanQazi · 2026-08-27

Hardware results, now folded into the issue body above.

I ran the patched op_tests on an MI300X (gfx942) against `536118a`, stock versus
patched on the same machine with identical shapes and kernels. `g1u1_fp8quant`
keeps its verdict (`atol` 100→64, `rtol` 0.01→0.0625, still passes).
**`g1u1_int8quant` flips pass→fail** (`atol` 100→8, `rtol` 0.01→0.003937), on
46.9% of elements.

The cause is a defect in my derivation, not a kernel bug: the derived `rtol` is
exactly one quantization rounding (`1/(2·127)` for int8, `2⁻⁴` for fp8 e4m3),
but the error accumulates across a K=2048 reduction, so the bound under-counts
whenever the inputs are quantized. The quantization term needs to scale with
reduction depth.

**The patch should not land as written.** Flagging it here rather than letting
someone find it in review. Full numbers, the failing output and the earlier
offline estimate this supersedes are in the body under *Hardware measurement*.


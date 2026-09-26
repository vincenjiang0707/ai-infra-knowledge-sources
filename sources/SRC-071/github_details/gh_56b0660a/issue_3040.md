# [Issue #3040] [BUG][Fuzzer][ice-on-valid-code] A width-changing `T.view` of a fragment aborts with an internal layout-inference `ICHECK` instead of a clear diagnostic

source: https://github.com/tile-ai/tilelang/issues/3040
state: closed | updated: 2026-08-25T07:46:32Z
labels: 

## 正文


### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) that this hasn't already been reported. (comment there if it has.)

### What version of TileLang are you using?

0.1.13

### System information

Linux; NVIDIA L40S (sm_89); CUDA 12.8; PyTorch 2.8.0; tilelang 0.1.13.

### Problem description

Reusing one buffer at a different element width is a documented, shipped pattern — `T.view(buf, shape, dtype)` reinterprets the same storage so a kernel can, e.g., read a bf16 input buffer back as an fp32 accumulator without paying for a second allocation (`examples/dsa_sparse_finetune/sparse_mla_bwd.py:167` does exactly this on a shared buffer). `T.view`'s only stated precondition is that the total bit count is preserved.

When the same width-changing view is taken on a **fragment** (`T.alloc_fragment`), compilation aborts with an internal `ICHECK`:

```
InternalError: Check failed: (analyzer_->CanProveEqual(abs(source->scale), 1)) is false
```

The view is in-contract: `256 * 32 == 512 * 16 == 8192` bits, so it passes `T.view`'s own `bits_product` assertion. The failure is fragment-specific and count-change-specific:

| target | view | result |
|---|---|---|
| `alloc_shared` fp32(256) → fp16(512) | count changes | **compiles, correct** (TESTED, L40S) |
| `alloc_fragment` fp32(256) → int32(256) | same count, dtype change | **compiles, correct** (TESTED, L40S) |
| `alloc_fragment` fp32(256) → fp16(512) | count changes | **aborts** (TESTED, L40S) |

The shared-buffer row is the byte-identical operation on contiguous storage and it compiles and returns the correct bit-reinterpretation. On a fragment, however, the same view is not well-defined: a fragment is a thread-distributed register layout, and (as the layout-axis sweep in Additional context shows) width-changing it produces a **non-injective** map on a real MMA layout — two logical elements collide on one physical register slot. So the right outcome is a clear front-end rejection of a width-changing `T.view` on a fragment, not the internal `ICHECK` it currently aborts with (nor a silent miscompile). The shared path's computability does not carry over to the distributed register layout.

The pattern is Hopper-independent (a fragment layout-inference step, no arch gate around it); not re-run on other arches.

### Reproducible example code

```python
import tilelang as tl, tilelang.language as T, torch

def build(scope):                       # scope: T.alloc_fragment or T.alloc_shared
    @T.prim_func
    def main(A: T.Tensor((256,), "float32"), B: T.Tensor((512,), "float16")):
        with T.Kernel(1, threads=32) as _:
            buf = scope((256,), "float32")
            T.copy(A, buf)
            v = T.view(buf, (512,), dtype="float16")   # 256*32 == 512*16 bits: passes bits_product
            T.copy(v, B)
    return main

def check(scope):
    k = tl.compile(build(scope), out_idx=-1)
    A = torch.randn(256, device="cuda", dtype=torch.float32)
    B = k(A)
    ok = torch.equal(B.view(torch.int16), A.view(torch.float16).view(torch.int16))
    return "PASS" if ok else "FAIL"

print("shared  :", check(T.alloc_shared))     # -> PASS
print("fragment:", check(T.alloc_fragment))   # -> aborts: CanProveEqual(abs(source->scale), 1) is false
```

### Traceback

```
tilelang.transform.LayoutInference()(mod)
  ...
  tvm::tl::ParallelOpNode::InferLayout(...)
  tvm::tl::ParallelOpNode::ValidateCandidateAgainstFragments(...)   # src/op/parallel.cc
  tvm::tl::ProveFragmentContains(...)                               # src/layout/utils.cc
  tvm::tl::FragmentNode::Inverse() -> LayoutNode::InverseWithLevel()
  tvm::arith::InverseAffineIterMap(...)
  InverseAffineIterMapTransformer::Visit_(const IterSumExpr&)       # src/arith/iter_affine_map.cc:2568
tvm.error.InternalError: Check failed: (analyzer_->CanProveEqual(abs(source->scale), 1)) is false:
```

### Expected behavior

A clear front-end error that names `T.view` and the fragment scope, rather than an internal `ICHECK` deep in layout inference.

The preferable outcome is a **clean rejection**, not a compile. A width-changing view is well-defined on a shared/global buffer because storage there is a plain contiguous byte layout, but a fragment is a *thread-distributed* register layout, and splitting/merging an element across a width change has no well-defined mapping under a non-trivial fragment layout. The layout-axis sweep below makes this concrete: on an **MMA-laid-out** fragment (a `T.gemm` accumulator), the width-changed view produces a **non-injective** loop layout — two distinct logical elements map to the *same* physical register slot (`logical [0,0,0] and [0,1,0] both map to physical [0,0]`). That is not a limitation the compiler could compute around; the operation genuinely has no correct answer on that layout. So the shared path being byte-computable does **not** imply the fragment path should compile — the earlier framing of "make the fragment path compile like shared" is withdrawn in favor of a clean front-end rejection of a width-changing `T.view` on a fragment. (`T.view`'s docstring states the only requirement is bit-count preservation, which this input meets syntactically — so the rejection should be an explicit, documented scope restriction, not the bit-count assert.)

### Additional context

**Root cause.** A width-changing `T.view` of a fragment makes the SIMT loop's index map carry a non-unit element stride, and layout inference's affine-map inverter aborts because it only accepts unit strides. This is a two-pass interaction, not a single faulty check.

- *Pass 1 — the `T.view` front-end op* (`tilelang/language/customize.py`) rebuilds a fresh `Tensor` over the source's `.data` and validates only that the total bit count is preserved. It records nothing about the width change: to everything downstream the view is simply a differently-shaped, differently-typed buffer aliasing the same storage. There is no place in a `T.view` for the element-count reindexing (256 fp32 lanes ↔ 512 fp16 lanes) to be captured.
- *Pass 2 — `LayoutInference`* (`src/transform/layout_inference.cc`, run as `tilelang.transform.LayoutInference()`) then has to assign a fragment (register) layout to the viewed buffer and prove the SIMT copy-out loop is consistent with it. `ParallelOpNode::ValidateCandidateAgainstFragments` calls `ProveFragmentContains`, which inverts the fragment layout via `large_frag->Inverse()`. Because the width-changed view makes the loop→fragment index map carry a **non-unit element stride**, the affine-map inverter's single-component back-propagation — which asserts the source scale is `±1` — fails.

Neither pass is independently wrong: `T.view` has no mechanism to carry the reindexing, and layout inference has no notion that this fragment is a width-changed alias whose access map is non-unit-stride. The abort is the collision of the two. A shared/global buffer never enters fragment layout inference / this inversion step, which is why the byte-identical view compiles there.

<details><summary>where it happens</summary>

- Pass 1: `T.view` builds a new `Tensor` over the source's `.data` guarded only by a bit-count assert — [`tilelang/language/customize.py#L77-L90`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/language/customize.py#L77-L90).
- Pass 2 (`LayoutInference`): the SIMT copy-out candidate is validated against the fragment layout in [`src/op/parallel.cc#L650`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/op/parallel.cc#L650) (`ParallelOpNode::ValidateCandidateAgainstFragments`), which calls `ProveFragmentContains` — [`src/layout/utils.cc#L464`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/layout/utils.cc#L464) — which inverts the fragment layout at [`src/layout/utils.cc#L506`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/layout/utils.cc#L506) (`large_frag->Inverse()`).
- The affine-map inverter's single-component (`args.size()==1`) path asserts unit scale — [`3rdparty/tvm` `iter_affine_map.cc#L2568`](https://github.com/tile-ai/tvm/blob/8df8ebd61659505dd7005f4820b030e983e2c005/src/arith/iter_affine_map.cc#L2568): `TVM_FFI_ICHECK(analyzer_->CanProveEqual(abs(source->scale), 1));`. The width-changed view makes that scale non-unit, so the `ICHECK` aborts.

</details>

**Suggested fix.** Reject a width-changing `T.view` of a fragment up front, at the pass boundary, with a front-end diagnostic that names `T.view` and the fragment scope — not the internal `iter_affine_map.cc#L2568` `ICHECK`. The layout-axis sweep below shows the operation is not merely hard to lower but *ill-defined* on a non-trivial fragment layout (an MMA-laid-out accumulator gives a **non-injective** map — two logical elements collide on one physical register slot), so "teach the inverter to handle the non-unit stride" is not a viable direction for the layout that matters: there is no correct mapping to compute. The clean rejection is the appropriate outcome; the bit-count assert (which this input passes) is not the place to enforce it, so the check should be an explicit fragment-scope restriction on width-changing views.

**Provenance.** Present since `T.view` first shipped in [#212](https://github.com/tile-ai/tilelang/pull/212) (merged 2025-03-14); not a regression. No review-bot flag found on that PR.

**Dedup.** I searched the open and closed tracker and found no existing report of this defect. [#2609](https://github.com/tile-ai/tilelang/issues/2609) is the nearest neighbor but is a different bug: a cross-dtype view of a **shared** buffer carrying a swizzle that silently reads the wrong slots (`LayoutNode::Reshape` rescale) — a silent wrong-value on shared memory, whereas this is a hard compile abort specific to a **fragment** view via iter-map inversion.

**Impact.** The trigger is narrow: a width-changing (element count-changing) `T.view` whose target is a fragment rather than a shared/global buffer. When it fires it is a compile-time abort surfaced as an internal `ICHECK`, so it is loud and caught immediately at build time — nothing is miscompiled and no wrong value can reach a running kernel. Fixing it either lets this documented, byte-computable reinterpretation compile on the fragment path (as the shared path already does) or replaces the internal assert with a clear front-end diagnostic; the concrete gain is closing that fragment-vs-shared compile disagreement, not unblocking a workload that ships today.

**Reach.** This is a confirmed two-pass interaction (front-end `T.view` × `LayoutInference` fragment inversion), not a single bad check; the honest boundary was mapped with cells run in isolation on L40S / sm_89 / 0.1.13.

*Root, two levels.* (a) **Source-level:** the fragile implementation is the affine-map inverter's single-component path in `3rdparty/tvm` `src/arith/iter_affine_map.cc:2568` — `TVM_FFI_ICHECK(analyzer_->CanProveEqual(abs(source->scale), 1))` — reached only through the fragment layout inversion in `src/layout/utils.cc` (`ProveFragmentContains` → `large_frag->Inverse()`), which in turn is reached only when a **fragment** (register) buffer carrying a **non-unit element stride** must have its layout inferred. `T.view` (`tilelang/language/customize.py:77-90`) is upstream fragile in a different way: it rebuilds a fresh `T.Tensor(shape, dtype, src.data)` guarded *only* by a bit-count assert and carries no record of the width change. The abort is the collision. (b) **Operator-level:** any op that (i) produces an element-count-changing alias over the same storage and (ii) feeds a fragment into SIMT layout inference. `T.view(dtype=...)` is the only front-end op that changes element count on a fragment; `T.reshape` (the byte-identical sibling in the same file, same rebuild + same guard) cannot change dtype so cannot produce the non-unit stride.

*4-axis sweep (all cells RUN on L40S / sm_89 / 0.1.13, one kernel per fresh process):*

| axis | cell tested | result | same-root? |
|---|---|---|---|
| baseline | `alloc_shared` fp32(256)→fp16(512), copy-out | **compiles, bit-exact PASS** | — (distinct scope, no failure) |
| baseline | `alloc_fragment` fp32(256)→int32(256) same-count | **compiles, PASS** | — (no count change → no non-unit stride) |
| baseline | `alloc_fragment` fp32(256)→fp16(512) | **aborts** `iter_affine_map.cc:2568` | yes |
| baseline | `alloc_fragment` fp16(512)→fp32(256) | **aborts** `iter_affine_map.cc:2568` | yes (symmetric in count direction) |
| related-type | `alloc_fragment` int32(256)→int16(512) | **aborts**, same ICHECK | yes |
| related-type | `alloc_fragment` int32(256)→int8(1024) (4:1) | **aborts**, same ICHECK | yes |
| related-type | `alloc_fragment` fp32(256)→bfloat16(512) | **aborts**, same ICHECK | yes |
| related-type | `alloc_fragment` fp16(512)→float8_e4m3(1024) | **aborts**, same ICHECK | yes |
| related-type | `alloc_fragment` int16(512)→int8(1024) | **aborts**, same ICHECK | yes |
| related-type | `alloc_fragment` 2-D fp32(16×16)→fp16(16×32) | **aborts**, same ICHECK | yes (rank/shape irrelevant) |
| related-operator | fragment fp32→fp16 view, then **`T.Parallel` compute** on the view (no copy-out) | **aborts**, same ICHECK | yes (not copy-out-specific — any SIMT use of the viewed fragment) |
| similar-logic | `T.reshape` fragment fp32(16×16)→fp32(256) (same-count rank change, same rebuild code) | **compiles OK** | related but does not fire (reshape can't change element width → no non-unit stride) |
| related-source | `alloc_shared` fp32→fp16 view + `T.Parallel` compute on view | **compiles OK** | shared scope never enters fragment inversion, even under a compute loop |
| **related-layout** | fragment carrying an **MMA layout** (a `T.gemm` fp32 accumulator) fp32→fp16 view + copy-out | **aborts — DIFFERENT site**: `Loop layout is not injective … logical [0,0,0] and [0,1,0] both map to physical [0,0]` (not the `scale==1` assert) | same class, **second face** — proves the op is *ill-defined* (non-injective) on a real distributed layout, not just un-invertible by the default-layout path |
| **related-layout** | fragment with an explicit `T.annotate_layout(T.Fragment(...))` + width view | aborts (LayoutInference) | same class — a non-trivial fragment layout has no well-defined width-split |

*What the sweep pins down.* The trigger is exactly **{fragment scope} × {element-count-changing view} × {any SIMT/`T.Parallel` use}**; remove any one and it compiles. It is **dtype-family-independent** (fp16/bf16/fp8, int8/16/32 all abort), **direction-independent** (widen or narrow), **rank-independent** (1-D and 2-D both abort), and **not tied to copy-out** (an in-place compute loop on the view aborts the same way).

The **layout axis** is what settles the disposition. The default-layout fragment aborts at the `CanProveEqual(abs(source->scale), 1)` inverter assert; an **MMA-laid-out** fragment (a `T.gemm` accumulator) aborts at a *different* site — `Loop layout is not injective`, reporting two distinct logical elements mapping to one physical register slot. These are two faces of one class (fragment × width-view unsupported), but the second face is the important one: it shows the width-changing view is **ill-defined**, not merely un-invertible, on a genuine thread-distributed layout — there is no correct physical mapping to compute. This is why the disposition is a **clean rejection**, not "make the fragment path compile like shared": the shared path's byte-computability does not transfer to a distributed register layout. `T.reshape` (the byte-identical sibling) cannot change element width, so it cannot reach this. **No separately-fileable neighbor was found** — every failing cell is the same class (default-layout and MMA-layout are two faces of it), every passing cell lacks the fragment-width-view ingredient. Kept a single, specific defect with a same-class reach across dtypes/ranks/consumers/layouts.

*Example run (verified this session, not inherited).* The width-changing `T.view` idiom ships in `examples/dsa_sparse_finetune/sparse_mla_bwd.py:167` — `acc_dkv_shared = T.view(KV_shared, shape=[BS // split_store, D], dtype=accum_dtype)` — a bf16(16-bit)→fp32(32-bit) count-changing view on the **`T.alloc_shared`** buffer `KV_shared` (declared line 151). I ran the shipped example verbatim on 0.1.13 (`test_sparse_mla_bwd(...)`, its `__main__` default config). The kernel that contains this view (`bwd`, a `@tilelang.jit` function) **compiles successfully** (`TileLang completes to compile kernel bwd`); the example then fails only at *runtime* on shared-memory allocation (`Failed to set the allowed dynamic shared memory size to 221040` — ~216 KB, over the L40S per-block limit), a hardware-config limit unrelated to this bug and unrelated to the view. So the shipped example exercises cell 1's shared-scope path, which compiles, and **dodges the fragment-specific abort precisely because the view is on a shared buffer, not a fragment**. This is the same conclusion the draft asserted, now confirmed by running it. Searching the v0.1.13 tree, **no shipped example or test takes a width-changing view of a fragment**, so CI stays green. The trigger uses documented API (`T.view`'s `dtype` parameter and its bit-count-only precondition).

## 评论 (3)

### haoyang9804 · 2026-08-20

I can reproduce it on macos M3. Simply updating to master can solve this issue.

### haoyang9804 · 2026-08-20

the root cause is fragmetn is not continuous. Cutting a fp32 into two fp16s does not work and v0.1.13 assertion fails it.

### KellyFrog · 2026-08-25

Hi!

The issued code can run corrently on current `main`, the issue is therefore closed.


# [Issue #3039] [BUG][Fuzzer][ice-on-valid-code] Reading a `T.Pipelined` producer shared buffer after the loop crashes the compiler instead of compiling

source: https://github.com/tile-ai/tilelang/issues/3039
state: closed | updated: 2026-09-06T14:28:52Z
labels: 

## 正文


### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) and no similar issue was found.

### What version of TileLang are you using?

0.1.13

### System information

TileLang 0.1.13 / PyTorch 2.8.0 / CUDA 12.8; NVIDIA L40S (sm_89). The crash is in a target-independent host pass (`LayoutInference`), so it is not hardware-specific.

### Problem description

A shared buffer that is written inside a `T.Pipelined(..., num_stages>=2)` loop and then read *after* the loop crashes compilation with an internal assert, while the identical kernel with `num_stages=1` compiles and runs:

```
InternalError: Check failed: (az->CanProveEqual(input_shape_product * rescale_num, shape_product * rescale_den)) is false:
InputShape() = (3, 64, 32) shape = (64, 32), rescale_num = 16, rescale_den = 16
```

The `(3, 64, 32)` is the buffer after pipeline multi-versioning has prepended the `num_stages=3` version dimension; `(64, 32)` is the buffer's original shape as seen at the post-loop read. Same trigger with `num_stages=1` (no versioning) compiles and runs correctly, so the crash is specific to the multi-versioning path — not the read itself. Not a regression — see Provenance.

### Reproducible example code

```python
import tilelang
import tilelang.language as T
import torch

M, K, BK = 64, 128, 32

def build(num_stages):
    @tilelang.jit(out_idx=[1])
    def kern():
        @T.prim_func
        def main(A: T.Tensor((M, K), "float16"), Out: T.Tensor((M, BK), "float16")):
            with T.Kernel(1, threads=128) as bx:
                As = T.alloc_shared((M, BK), "float16")   # producer, written each stage
                Bs = T.alloc_shared((BK, M), "float16")
                Cf = T.alloc_fragment((M, M), "float32")
                T.clear(Cf)
                for k in T.Pipelined(K // BK, num_stages=num_stages):
                    T.copy(A[0:M, k * BK:(k + 1) * BK], As)
                    for i, j in T.Parallel(BK, M):
                        Bs[i, j] = T.float16(1.0)
                    T.gemm(As, Bs, Cf)
                T.copy(As, Out)                            # read As AFTER the pipelined loop
        return main
    return kern()

# CONTROL: same kernel, same post-loop read, num_stages=1 (no multi-versioning) -> compiles + runs
f = build(num_stages=1)
a = torch.randn(M, K, device="cuda", dtype=torch.float16)
o = f(a)
print("num_stages=1 :", "COMPILED+RAN, out", tuple(o.shape))   # -> COMPILED+RAN, out (64, 32)

# TRIGGER: num_stages>=2 multi-versions As; the post-loop read then crashes the compiler
f = build(num_stages=3)                                        # -> InternalError (see Traceback)
print("num_stages=3 : COMPILED (unexpected)")
```

### Traceback

```
  File "tilelang/cuda/pipeline.py", line 117, in CUDAPassPipelineBodyPrologue
    mod = tilelang.transform.LayoutInference()(mod)
  ...
  in tvm::tl::LayoutInferencer::Substitute(tvm::tirx::PrimFunc)
  in tvm::tl::BufferUseDefCollector::Run()
  in tvm::tl::BufferUseDefCollector::RunInferStep(...)
  in tvm::tl::BufferUseDefCollector::RunInferStep(...)::{lambda(Buffer, Layout)#1}::operator()(...)
  File "/project/src/layout/layout.cc", line 871, in tvm::tl::LayoutNode::Reshape(...)
tvm.error.InternalError: Check failed: (az->CanProveEqual(input_shape_product * rescale_num, shape_product * rescale_den)) is false: InputShape() = (3, 64, 32) shape = (64, 32), rescale_num = 16, rescale_den = 16
```

### Expected behavior

Compilation completes instead of tripping an internal assert. The two consistent outcomes both seem reasonable: either the post-loop read is honored (reading the buffer's last-written version), or, if reading a pipeline-versioned producer after the loop is not intended to be supported, a clean diagnostic at the frontend that names the buffer and the pattern. An internal `CanProveEqual` assert deep in layout inference is neither.

### Additional context

**Root cause.** Two passes disagree about a shared buffer that is both a `T.gemm` operand *and* read after the pipelined loop. The multi-version buffer rewriter (run by the software-pipeline stack) rewrites the buffer's allocation to carry a leading `num_stages` version dimension, so its declared shape becomes `[3, 64, 32]`. `LayoutInference` independently infers an MMA-operand layout for that buffer over its original `[64, 32]` shape (from the `T.gemm` use), then — because the versioned allocation and the operand use are the same underlying storage — propagates the `[64, 32]` layout onto the `[3, 64, 32]` alias via `LayoutNode::Reshape`. That reshape assumes the two shapes differ only by element width (an alias-reinterpret rescale) and fails the storage-product invariant: `prod([3,64,32])*16 != prod([64,32])*16`. The trigger is narrow and specific: adjacent-cell probes (see Reach) show it needs the read-after buffer to carry an inferred MMA-operand layout — a versioned shared buffer that is *not* a gemm operand, or the gemm accumulator fragment, is read after the loop without crashing.

<details><summary>Where it happens (0.1.13)</summary>

- The version dimension is prepended in [`RewriteAllocBuffer`, `multi_version_buffer_rewriter.cc:494`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/cuda/transform/multi_version_buffer_rewriter.cc#L494) — [`shape.insert(begin, num_versions)`, :503](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/cuda/transform/multi_version_buffer_rewriter.cc#L503) → `[64,32]` becomes `[3,64,32]`.
- The rewriter's own [BufferLoad guard, `:769`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/cuda/transform/multi_version_buffer_rewriter.cc#L769) (`ICHECK(version_index.defined()) << "Versioned buffer load escaped pipeline stage context"`) shows the escaped-use case was anticipated, but a post-loop read reaching layout inference is not caught there.
- The crash surfaces in the alias-propagation path of layout inference, which reshapes the inferred layout onto a same-data sibling assuming the two shapes differ only by element width: [`layout_inference.cc:184`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/layout_inference.cc#L184).
- The assert is the storage-product check in [`LayoutNode::Reshape`, `layout.cc:871`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/layout/layout.cc#L871): `prod([3,64,32])*16 != prod([64,32])*16`.

</details>

**Suggested fix.** The multi-version rewriter should detect a use of a versioned buffer outside the pipeline stage context (the case its `:769` guard already describes) and either keep that use on an un-versioned view or reject it at the frontend with a clear message; alternatively the layout-inference alias propagation at `:184` should account for a prepended version dimension rather than treating the shape difference as an element-width rescale. This touches either the pipeline rewriter or layout inference, so it is not a one-line change (not verified end-to-end).

**Provenance.** The version-dimension prepend is part of the multi-version buffer rewriter, present since it shipped (`multi_version_buffer_rewriter.cc`, created in [#2166](https://github.com/tile-ai/tilelang/pull/2166), merged 2026-05-12; software-pipeline transforms later refactored in [#2245](https://github.com/tile-ai/tilelang/pull/2245)). The equivalent versioning existed inline in the pipeline pass before that split. The crash is the interaction of this versioning with layout-inference alias propagation; I did not pin a single introducing PR for the interaction.

**Dedup.** I searched the open and closed tracker and found no existing report of this exact crash. The closest relative is [#2309](https://github.com/tile-ai/tilelang/issues/2309) (open, "LayoutInference crash for sibling `T.Pipelined` loops sharing `alloc_shared` buffers with different `num_stages`") — a **distinct bug that shares this one's underlying theme**: both are a `T.Pipelined` × shared-buffer interaction where the buffer's *actual multi-versioned storage layout* disagrees with the shape a later use assumes, and `LayoutInference` cannot reconcile the two. They differ in the triggering structure: #2309 needs **two sibling pipelined loops** that request **different `num_stages`** for the *same* `alloc_shared` (the conflict is between the two loops' version counts), whereas this bug needs a **single** pipelined loop whose versioned MMA-operand buffer is **read after the loop** (the conflict is between the versioned allocation `[num_stages,…]` and the operand's original `[…]` shape at the post-loop read). Same family — the multi-version rewriter's prepended version dimension not being accounted for downstream — but a different trigger and a different reconciliation site, so they warrant separate reports (and likely a shared fix in how versioned aliases carry their layout). Two further, more distant relatives: [#2528](https://github.com/tile-ai/tilelang/issues/2528) also involves the multi-version rewriter but is a distinct defect — a runtime `CUDA error: misaligned address` from missing 128B padding on a 1-D TMA copy, not a compile-time layout-inference assert; and [#2609](https://github.com/tile-ai/tilelang/issues/2609) is also a `LayoutNode::Reshape` failure but for a cross-element-width swizzled `T.view`, with no pipeline versioning involved.

**Impact.** The trigger is narrow: a shared `T.gemm`-operand buffer read after a `num_stages>=2` pipelined loop, a pattern the shipped examples happen to dodge by reading the fragment accumulator instead. `examples/gemm/example_gemm.py` was **run verbatim on 0.1.13** and compiles+runs+passes (`All check passed.`, latency 0.033 ms): it uses `num_stages=3` but copies the fragment accumulator `C_local` — not a shared operand — after the loop, so it never hits the versioned-alias reshape. When the bug fires the failure is a compile-time internal assert in `LayoutInference` — loud and deterministic, caught the moment the kernel is built; it corrupts no data and cannot reach a running workload silently. Fixing it either lets a legal "fill a shared operand tile across the loop, reuse its final contents after" kernel compile or replaces the deep `CanProveEqual` assert with a clear frontend diagnostic naming the buffer and pattern.

**Reach.** The root is a two-pass interaction — the **multi-version buffer rewriter** (`src/cuda/transform/multi_version_buffer_rewriter.cc`, driven by the software-pipeline stack) prepends the version dimension, and **`LayoutInference`** (`src/transform/layout_inference.cc`, run from `tilelang/cuda/pipeline.py:117`) reshapes an MMA-operand layout onto that versioned alias. Neither pass is wrong in isolation; the assert fires only where they compose. I ran six isolated cells on 0.1.13 (fresh cache each, one kernel per process) to map the boundary:

- `num_stages=1` (control) — **COMPILED+RAN**, `out (64,32)`. No versioning, no crash.
- `num_stages=2`, gemm-operand `As` read after loop — **CRASH**, `InputShape() = (2,64,32)`. Same assert, version dim = `num_stages`. **Same root** as the `num_stages=3` trigger.
- `num_stages=3`, gemm-operand `As` read after loop — **CRASH**, `InputShape() = (3,64,32)`. The headline trigger.
- `num_stages=3`, read the *fragment accumulator* after loop (the canonical GEMM pattern, `examples/gemm/example_gemm.py` copies `C_local` not the shared operand) — **COMPILED+RAN**, `out (64,64)`. **Distinct path**: fragment read-after does not hit the versioned-alias reshape. This is why shipped examples and CI stay green.
- `num_stages=3`, read-after buffer written in-loop but **not** a gemm operand (gemm uses a separate shared pair) — **COMPILED+RAN**, `out (64,32)`. **Distinct**: without an inferred MMA-operand layout there is nothing to reshape onto the versioned alias.
- `num_stages=3`, gemm-operand `As` written by `T.Parallel` instead of `T.copy`, read after loop — **CRASH**, `InputShape() = (3,64,32)`. **Same root**: the discriminator is *being an MMA operand read after the loop*, not how the buffer is written.

So the necessary ingredients are all three of: `num_stages>=2` (versioning), the read-after buffer is a `T.gemm` operand (so `LayoutInference` gives it an MMA layout), and it is read after the loop (so the versioned allocation and the operand use alias the same storage). `T.Pipelined` with `num_stages>=2` is itself ubiquitous (grep at this SHA: **130** example files use `T.Pipelined`, **1105** `num_stages` sites under `examples/`); the rarer combination is reusing an MMA-operand shared tile after the pipelined loop, which nothing in the `T.Pipelined` docstring disclaims.

**Generalization (root + 4-axis sweep, all cells run on 0.1.13).** *Two-level root.*
- **SOURCE-level root.** The fragile code is the alias-reinterpret branch of layout inference: [`layout_inference.cc:184`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/layout_inference.cc#L184) calls `LayoutNode::Reshape(sib->shape, ..., old_bits, new_bits)` for any two buffers sharing storage, assuming they differ only by element **width**. When one alias is the pipeline-versioned allocation (`[num_stages, ...]`) the shape differs by a prepended *count* dimension, not a width, and the storage-product ICHECK at [`layout.cc:871`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/layout/layout.cc#L871) fails. The version dimension itself is prepended upstream by `RewriteAllocBuffer` in the multi-version buffer rewriter (`multi_version_buffer_rewriter.cc:494/503`). Neither pass is wrong alone; the assert fires only where they compose.
- **OPERATOR-level root.** Being an **MMA operand read after the pipelined loop.** The `T.gemm` use gives the shared buffer an MMA-operand layout that must be reshaped onto the versioned alias; the *read* is what makes the versioned allocation and the operand use the same storage. Related ops correlate only if they too impose a layout on a versioned shared buffer that is then read post-loop.

**4-axis sweep** (each cell run in a fresh `/tmp/gen_23_*` dir, fresh cache, one kernel/process):

| axis | cell tested | result | same-root? |
|---|---|---|---|
| baseline | `num_stages=1`, LHS operand read-after (control) | COMPILED+RAN, out (64,32) | n/a (no versioning) |
| baseline | `num_stages=2/3`, LHS operand `As` read-after | CRASH `InputShape()=(2,64,32)` / `(3,64,32)`, rescale 16/16 | headline |
| similar-logic | operand read-after via `T.Parallel` elementwise (not `T.copy`) | CRASH `(3,64,32)`, rescale 16 | **same-root** — read *op* is irrelevant |
| similar-logic | operand written by `T.Parallel` instead of `T.copy`, read-after | CRASH `(3,64,32)` | **same-root** — write *op* is irrelevant |
| related-source | fragment accumulator read-after (the `example_gemm.py` path) | COMPILED+RAN, out (64,64) | distinct — fragment has no versioned-alias reshape |
| related-source | versioned shared buffer read-after that is **not** a gemm operand | COMPILED+RAN, out (64,32) | distinct — no MMA layout to reshape |
| related-operator | read the **RHS** gemm operand `Bs` after loop (vs LHS) | COMPILED+RAN, out (32,64) | distinct — RHS operand layout reshapes cleanly onto the versioned alias; only LHS crashes |
| related-type | **bf16** LHS operand read-after | CRASH `(3,64,32)`, rescale 16/16 | **same-root** — dtype-independent within 16-bit |
| related-type | **fp8 (e4m3)** LHS operand read-after | CRASH `(3,64,32)`, rescale **8/8** | **same-root** — width-independent; storage-bits change but the product mismatch (prepended count dim) is unchanged |

**Findings.** The root is dtype/width-independent (fp16, bf16, fp8 all crash identically; the `rescale` numbers track element-storage-bits but the failure is the prepended count dimension, not any width mismatch) and read-op/write-op-independent (`T.copy` and `T.Parallel` both crash). The discriminator is exactly *being an LHS MMA operand read after the loop*: fragment-accumulator reads, non-operand shared reads, and **RHS-operand** reads all compile. The RHS-vs-LHS asymmetry (draft's previously-unpinned note) is now confirmed by direct test — only the LHS operand crashes; the RHS operand's inferred layout reshapes onto the versioned alias without tripping the product check. This is a **narrow, specific** boundary, not a class, so the title and Problem are **kept specific**. No new distinct-adjacent bug and no separately-fileable neighbor were found: every crashing neighbor is the same root, every non-crashing neighbor is a genuinely distinct (correct) path.

**Example-run result (PART 1).** `examples/gemm/example_gemm.py` (v0.1.13) run verbatim: **COMPILED+RAN, `All check passed.`**, latency 0.033 ms. It uses `num_stages=3` but copies the fragment accumulator `C_local` after the loop (source confirmed) — so the shipped example does **not** exercise this bug; it dodges it exactly as the Reach section claims. This is honest evidence that the pattern is off the CI path, which is why the crash went unreported, not evidence that the trigger is common.

## 评论 (1)

### KellyFrog · 2026-08-27

Hi!

This is a known phenomenon and we treat it more like a feature than a bug. In practice, a pipelined buffer is usually not used outside pipelines.

Enhancements on this issue is welcomed, but it is not our top priority.

Best reguards.

# [Issue #3033] [BUG][Fuzzer][ice-on-invalid-code] `T.finalize_reducer` on a reducer never reduced in a `T.Parallel` loop aborts with an internal `bad_optional_access` in `LayoutInference`

source: https://github.com/tile-ai/tilelang/issues/3033
state: closed | updated: 2026-08-25T07:29:38Z
labels: 

## 正文


## Required prerequisites

- [x] Make sure you've read the [documentation](https://tilelang.com). Your issue may be addressed there.
- [x] Search the [issue tracker](https://github.com/tile-ai/tilelang/issues) to verify that this hasn't already been reported. No related report was found.
- [x] I have provided a minimal, reproducible example.

## What version of TileLang are you using?

0.1.13 (tag `v0.1.13`)

## System information

- GPU: NVIDIA L40S (sm_89)
- CUDA: 13.0 (nvcc V13.0.88)
- PyTorch: 2.13.0+cu130
- OS: Linux x86_64

## Problem description

A kernel that allocates a reducer with `T.alloc_reducer`, initializes it (`T.clear`/`T.fill`), and then calls `T.finalize_reducer` **without an enclosing `T.Parallel` reduction loop over that reducer** aborts compilation with a raw C++ optional null-dereference in the `LayoutInference` pass:

```
tvm.error.InternalError: bad_optional_access while inferring layout for op 9 (tl.FinalizeReducerOp) at level Strict
```

It surfaces both in a degenerate form (fill + finalize, no reduction at all) and in the realistic form where the reduction into the reducer is performed with `T.reduce` (a fragment reduce op) instead of an explicit `T.Parallel` accumulate loop. The op index (`op 9` / `op 3`) is the only variable part; the `std::optional` access failure gives the user no indication of what is wrong or where in their source.

## Reproducible example code

```python
import tilelang
import tilelang.language as T

N = 16

@T.prim_func
def reduce_kernel(
    A: T.Buffer((N,), 'float32'),
    Out: T.Buffer((1,), 'float32'),
):
    with T.Kernel(1, threads=32) as (_,):
        a = T.alloc_fragment((N,), 'float32')
        r = T.alloc_reducer((1,), 'float32', op='sum')
        T.copy(A, a)
        T.clear(r)
        # reduce into the reducer via T.reduce (a fragment reduce), not a T.Parallel += loop
        T.reduce(a, r, reduce_type='sum', dim=0, clear=False)
        T.finalize_reducer(r)
        Out[0] = r[0]

tilelang.compile(reduce_kernel, out_idx=[1], target='cuda')
```

<details>
<summary>Minimal trigger (deletion-tested) — <code>T.reduce</code> is not required</summary>

Removing `T.reduce` still crashes with the identical `bad optional access`. The minimal trigger is just: a reducer that is opened by `T.fill`/`T.clear` and closed by `T.finalize_reducer`, with no `T.Parallel` loop reducing it in between.

```python
import tilelang
import tilelang.language as T

N = 16

@T.prim_func
def k(A: T.Buffer((N,), 'float32'), Out: T.Buffer((1,), 'float32')):
    with T.Kernel(1, threads=32) as (_,):
        r = T.alloc_reducer((1,), 'float32', op='sum')
        T.fill(r, 0)
        T.finalize_reducer(r)
        Out[0] = r[0]

tilelang.compile(k, out_idx=[1], target='cuda')   # -> InternalError: bad optional access
```

The intended reducer workflow — `T.alloc_reducer` + `T.clear` + a `T.Parallel` accumulate loop + `T.finalize_reducer` (as in `examples/gemv/example_gemv.py::gemv_alloc_reducer`) — compiles and runs correctly, so the presence of the `T.Parallel` reduction loop is exactly the difference:

```python
@T.prim_func
def ok(A: T.Buffer((128, 64), 'float32'), Out: T.Buffer((128,), 'float32')):
    with T.Kernel(1, threads=128) as (_,):
        a = T.alloc_fragment((128, 64), 'float32')
        r = T.alloc_reducer((128,), 'float32', op='sum', replication='all')
        T.copy(A, a)
        T.clear(r)
        for i, j in T.Parallel(128, 64):
            r[i] += a[i, j]
        T.finalize_reducer(r)
        T.copy(r, Out)
# compiles; result == 64.0 (correct)
```
</details>

## Traceback

<details>
<summary>Full traceback</summary>

```
File ".../tilelang/cuda/pipeline.py", line 117, in CUDAPassPipelineBodyPrologue
    mod = tilelang.transform.LayoutInference()(mod)
File ".../tvm/ir/transform.py", line 171, in __call__
    return _ffi_transform_api.RunPass(self, mod)
  ...
  in tvm::tl::LayoutInferencer::Substitute(tvm::tirx::PrimFunc)
  in tvm::tl::BufferUseDefCollector::Run()
  in tvm::tl::BufferUseDefCollector::RunInferStep(...)
tvm.error.InternalError: bad_optional_access while inferring layout for op 9 (tl.FinalizeReducerOp) at level Strict
thread_bounds=I.Range(0, 32)
stmt=T.finalize_reducer(T.region(r[0], 2, 1), 0)
```
</details>

## Expected behavior

Either a clear frontend/pass diagnostic (e.g. "`T.finalize_reducer` on a reducer that is never reduced inside an enclosing `T.Parallel` loop"), or — if reducing into a reducer via `T.reduce` is intended to be supported — a valid layout for the reducer so compilation succeeds. In no case should the compiler abort with an internal `bad_optional_access` null-dereference on frontend-accepted input.

## Additional context

**Root cause.** `T.finalize_reducer` dereferences the reducer's layout unconditionally, but that layout is only ever produced by a `T.Parallel` reduction loop, so with no such loop the dereference is on an empty `Optional` and aborts.

<details>
<summary>Mechanism</summary>

The reducer's `Fragment` layout is assigned only inside the layout annotator's `VisitStmt_(ForNode)`, gated on the loop being a parallel loop:

- [`src/transform/layout_reducer.cc#L189-L191`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/layout_reducer.cc#L189-L191) — `should_annotate` requires `!inside_reducer_range_.empty() && !already_annotated_ && op->kind == ForKind::kParallel`. Only then does it build the `Fragment` and record it at [`layout_reducer.cc#L233`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/layout_reducer.cc#L233) (`new_layout_map_.Set(buffer->data, f)`).

When the reducer range is opened (by `T.fill`/`T.clear`) and closed (by `T.finalize_reducer`) with no `ForKind::kParallel` loop in between, `new_layout_map_` never gets an entry for the reducer, so no layout reaches the layout map. Later:

- [`src/op/finalize_reducer.cc#L115`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/op/finalize_reducer.cc#L115) — `FinalizeReducerOpNode::InferLayout` does `layout_map.Set(reducer, layout_args.layout_map.Get(reducer).value());`. `Get(reducer)` returns an empty `Optional`, and the unconditional `.value()` throws `bad_optional_access`. (Sibling `InferLayout` ops using the same idiom — `ReduceOp` at `reduce.cc:209`, `Scan` at `scan.cc:94` — guard it with a `count()` check first; this call site does not.)
</details>

**Suggested fix.** In `FinalizeReducerOpNode::InferLayout`, check the `Optional` before dereferencing and raise a contextful error (naming the reducer buffer and pointing at the missing `T.Parallel` reduction loop) instead of `.value()`. Equivalently, the layout annotator in `layout_reducer.cc` could detect a reducer range that is opened and finalized without any enclosing `ForKind::kParallel` loop and reject it up front with the same message. This turns an opaque internal crash into an actionable diagnostic.

**Impact.** The reducer allocated but never reduced in a `T.Parallel` loop is an easy shape for a user to write while building up or refactoring a reduction kernel (e.g. temporarily switching from a `T.Parallel` accumulate loop to `T.reduce`, or a not-yet-finished kernel). Instead of a diagnostic that names the missing reduction loop, the compiler aborts with a raw `bad_optional_access` that gives no hint of which primitive or which buffer is at fault, so the failure is hard to localize. It is a compile-time abort, not a silent miscompile, so no wrong results reach silicon.

**Provenance.** The `.value()` dereference in `FinalizeReducerOpNode::InferLayout` and the parallel-loop-gated layout assignment in `ReducerLayoutAnnotator` are both present at the pinned `v0.1.13` SHA; not a recent regression.

**Dedup.** Distinct from the other reducer/LayoutInference reports: `#2408` and `#2623` are silent *wrong-value* bugs on the correct `T.Parallel` reducer path (not a crash); `#2530`/`#2399`/`#2398` are different `LayoutInference` failures ("vars.size() 2 vs 1" keep-dim, "Inconsistent layouts", "no available layout found"); `#2547` is a Hopper warp-specialization pass-ordering regression. None reports `FinalizeReducerOpNode::InferLayout` dereferencing an empty `Optional`.

**Reach.** Root cause is host-side layout inference, independent of GPU architecture (fails before any codegen). Reproduced on L40S (sm_89); expected to reproduce on all targets. Confirmed dtype- and op-independent (sum/max/min, fp32/fp16/int32, `replication=all`/`none` all abort with the identical `bad_optional_access ... (tl.FinalizeReducerOp) at level Strict`; see Generalization).

The shipped example `examples/gemv/example_gemv.py::gemv_alloc_reducer` (v0.1.13) is the *correct* reducer path — it puts the accumulation in a `T.Parallel(block_M, block_N)` loop (`o_reducer[i1_m] += ...`) before `T.finalize_reducer`, so it does **not** exercise this bug; it is the control for it. Ran verbatim on 0.1.13: `gemv_alloc_reducer.compile(M=1024, N=1024, block_M=128, block_N=128)` compiles (~5s) and `profiler.assert_allclose` passes. The bug appears only when that `T.Parallel` accumulate loop is absent (reduction done via `T.reduce`, or no reduction at all).

<details>
<summary>Generalization — two-level root + 4-axis sweep, all cells run in isolation on v0.1.13 / L40S</summary>

**Two-level root.**
- **Source-level root (fragile implementation):** `FinalizeReducerOpNode::InferLayout` at [`src/op/finalize_reducer.cc#L115`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/op/finalize_reducer.cc#L115) does `layout_args.layout_map.Get(reducer).value()` with **no `count()`/`Optional` guard**. The layout it depends on is written only by `ReducerLayoutAnnotator::VisitStmt_(ForNode)` under the `op->kind == ForKind::kParallel` gate ([`layout_reducer.cc#L189-L191`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/layout_reducer.cc#L189-L191), set at [L233](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/layout_reducer.cc#L233)). No parallel loop → no layout entry → the unguarded `.value()` throws `bad_optional_access`.
- **Operator-level root (what correlates):** the `tl.FinalizeReducerOp` op itself. Deletion control (minimal case with `T.finalize_reducer` removed) does **not** hit `bad_optional_access` — it falls through to the free-mode `no available layout found` instead — so the empty-`Optional` dereference is specifically finalize_reducer's, not shared by the reducer's other consumers.

**4-axis sweep** (every cell was compiled; `bad_optional_access` = `... while inferring layout for op N (tl.FinalizeReducerOp) at level Strict`):

| Axis | Cell tested | Result | Same-root? |
|---|---|---|---|
| (main) | `T.reduce` fragment-reduce into reducer, `op='sum'` fp32 | `bad_optional_access` (op 9) | yes |
| (minimal) | `T.fill` + `T.finalize_reducer`, no reduction, `sum` fp32 | `bad_optional_access` (op 3) | yes |
| related-operator | `op='max'` (via `T.reduce`; and minimal) | `bad_optional_access` (op 9 / op 3) | yes |
| related-operator | `op='min'`, minimal | `bad_optional_access` (op 3) | yes — exhausts `ReducerOp = {sum,max,min}` |
| related-type (dtype) | `float16`, minimal | `bad_optional_access` (op 3) | yes |
| related-type (dtype) | `int32`, minimal | `bad_optional_access` (op 3) | yes |
| related-type (replication) | `replication='none'`, shape `(32,)`, minimal | `bad_optional_access` (op 3) | yes — both `ReducerRepType::ALL` and `NONE` annotator branches |
| related-source (sibling `.value()`) | `ReduceOp::InferLayout` `reduce.cc:209` `.Get(dst).value()` | guarded by `if (layout_map.count(dst))` above it — **not** the bug | distinct (correctly guarded) |
| related-source (sibling `.value()`) | `Scan::InferLayout` `scan.cc:94` `.Get(buf).value()` | guarded by `if (layout_map.count(buf))` — **not** the bug | distinct (correctly guarded) |
| similar-logic (control, OK) | `T.Parallel` accumulate loop, `sum` | compiles, result `64.0` (correct) | n/a — the intended path |
| similar-logic (distinct) | `T.serial` accumulate loop instead of `T.Parallel` | `Check failed: (min_reg_num < ...) is false: no available layout found` (`layout_inference.cc:1160`, `InferInFreeMode`) | **distinct root** — separate layout-selection failure, not `bad_optional_access` |

**Findings.** The bug is a single mechanism across all three reducer ops (`sum`/`max`/`min`), both float and int dtypes, and both replication modes — the root is host-side and value/dtype-agnostic, so those neighbors are the *same* bug (kept as one report, not filed separately). The two sibling `InferLayout` ops that use the identical `layout_map.Get(x).value()` idiom (`ReduceOp`, `Scan`) both guard it with a `count()` check first, so `FinalizeReducerOpNode::InferLayout` is the *only* unguarded instance — the boundary is narrow and specific to that one call site. The `T.serial` variant is a **distinct, not-filed** adjacent bug (different pass, different message).

**Example run (PART 1).** The only reducer idiom shipped in examples/tests at v0.1.13 is `examples/gemv/example_gemv.py::gemv_alloc_reducer`, which uses the correct `T.Parallel` accumulate loop and therefore **dodges** this bug by construction — ran verbatim on 0.1.13: it compiles and passes `assert_allclose`. It is the control, not a trigger; no shipped example exercises the missing-loop form. Honest note: this means the buggy shape is one a user reaches while editing/refactoring a reducer kernel, not one demonstrated by an existing example.
</details>

## 评论 (2)

### KellyFrog · 2026-08-25

Fixed by PR #3043 .

### KellyFrog · 2026-08-25

Btw, reducing to a reducer buffer is no longer valid in our new reducer buffer design. The example code above will be rejected directly.

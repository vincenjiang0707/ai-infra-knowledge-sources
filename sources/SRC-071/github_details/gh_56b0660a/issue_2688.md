# [Issue #2688] [BUG][Fuzzer][wrong-code] Vectorized `T.atomic_add` silently downgrades the requested `memory_order` to relaxed

source: https://github.com/tile-ai/tilelang/issues/2688
state: closed | updated: 2026-08-20T05:34:01Z
labels: 

## 正文


### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the Issue Tracker that this hasn't already been reported.

### What version of TileLang are you using?

0.1.12 (reproduced this session on the released `0.1.12` wheel). Source on `main` re-checked at `d36ec37c596ff8e587fc67fcf1e88bcb90cc60d6` (and the offending line is unchanged at current `main` HEAD `c5e53076`).

### System information

NVIDIA L40S (`sm_89`), CUDA 12.8, Python 3.13, tilelang 0.1.12. The defect is in target-independent transform/codegen (the atomic-add vectorizer and its CUDA codegen), so it is not specific to one GPU.

### Problem description

A tile-region `T.atomic_add(Out, Src, memory_order="acq_rel")` on `float16`/`bfloat16` (or `float32`) silently produces a **relaxed** atomic whenever the add auto-vectorizes to `AtomicAddx2`/`AtomicAddx4`, even though the *identical* call lowers scalar-wise — and correctly emits the requested ordering — when it does not vectorize. Whether it vectorizes is decided by whether the per-thread inner-loop extent shares a factor ≥2 with the atomic vector width (`GCD(vector_width, extent) ≥ 2`, i.e. the extent is divisible by 2 for the fp16/bf16 `x2` path or by 2/4 for the fp32 `x4` path) — a tiling detail unrelated to memory ordering. No error or warning is raised at any stage; the kernel compiles and runs, and the requested memory ordering is just gone.

Concretely, the same `T.atomic_add(Out[i], X[i], memory_order="acq_rel")` in a `T.Parallel` loop emits (both verified this session, fp16, `threads=32`):

| per-thread extent | lowering | emitted CUDA | ordering |
|---|---|---|---|
| 3 (`N=96`) — `GCD(2,3)=1`, no vectorize | scalar | `AtomicAdd(&Out[...], Src[...], 4)` | acq_rel (id 4) — **honored** |
| 2 (`N=64`) — `GCD(2,2)=2`, vectorizes | `AtomicAddx2` | `AtomicAddx2(&Out[tid*2], *(uint1*)(Src+tid*2))` | (no arg) → **relaxed** |

So identical public-API input yields different memory ordering depending purely on an invisible vectorization choice driven by the tile shape. This is not a regression — the vectorized atomic path has reconstructed the wide op from two operands since it first shipped.

<details><summary>Emitted atomic lines, both paths (this session, 0.1.12)</summary>

```
extent 3 (no vectorize): AtomicAdd((&(Out[((int)threadIdx.x)])), Src[((int)threadIdx.x)], 4);
   -> honors acq_rel (trailing ", 4)"): True
extent 2 (vectorizes)  : AtomicAddx2((&(Out[(((int)threadIdx.x) * 2)])), *(uint1*)(Src + (((int)threadIdx.x) * 2)));
   -> honors acq_rel (trailing ", 4)"): False   (silently relaxed)
```

</details>

### Reproducible example code

```python
import tilelang, tilelang.language as T

def mk(N, threads):
    @T.prim_func
    def k(X: T.Tensor((N,), "float16"), Out: T.Tensor((N,), "float16")):
        with T.Kernel(1, threads=threads):
            # identical tile-region atomic_add on both paths; only N/threads differ
            T.atomic_add(Out[0:N], X[0:N], memory_order="acq_rel")   # acq_rel == id 4
    return k

def emitted_atomic(N, threads):
    src = tilelang.compile(mk(N, threads), out_idx=-1, target="cuda").get_kernel_source()
    return [l.strip() for l in src.splitlines() if "AtomicAdd" in l][0]

# SCALAR lowering (1 elem/thread): honors acq_rel -> "AtomicAdd(..., 4)"
print(emitted_atomic(130, 130))   # -> AtomicAdd(&Out[...], X[...], 4);   ("...4)" present)

# VECTORIZED lowering (4 elem/thread, SAME call): drops it -> "AtomicAddx2(...)" no order arg
print(emitted_atomic(256, 64))    # -> AtomicAddx2(&Out[...], *(uint1*)(X+...));   (order gone -> relaxed)
```

### Traceback

No traceback — the kernel compiles and runs to completion on both paths; the vectorized path silently emits a weaker (relaxed) atomic than requested, with no error or warning.

### Expected behavior

A vectorized `T.atomic_add` should carry the same requested `memory_order` its scalar sibling does — the wide device helpers already accept and honor a `memory_order` argument (they branch to explicit ordered PTX for a non-relaxed order), so the requested `acq_rel` seems computable on the vectorized path too, not just the scalar one. Grounding: the compiler already emits `AtomicAdd(..., 4)` for the identical tile-region call when it lowers scalar-wise, so honoring the order is the behavior the code already exhibits on one of its two lowerings of the same input.

(One doc note for the maintainers: the `atomic_add` docstring currently says "the tile-region path ignores `memory_order`", but the scalar tile-region lowering demonstrably *does* honor it, so that line reads as stale — the intent appears to be to honor the order, which makes the vectorized drop the defect. Reconciling the docstring either way would remove the ambiguity.)

### Additional context

**Root cause.** The atomic-add vectorizer does not carry the operation's memory-order operand when it rewrites a tile-region atomic add into its wide (x2/x4) form, so the wide atomic is generated without any ordering and silently falls back to relaxed. In detail: the tile-region lowering attaches the requested order as the third operand of the scalar `atomic_add_elem_op` ([`atomic_add.cc#L185-L192`](https://github.com/tile-ai/tilelang/blob/d36ec37c596ff8e587fc67fcf1e88bcb90cc60d6/src/cuda/op/atomic_add.cc#L185-L192), pushing `op.GetMemoryOrder()` — [`atomic_reduce.h#L47-L54`](https://github.com/tile-ai/tilelang/blob/d36ec37c596ff8e587fc67fcf1e88bcb90cc60d6/src/op/atomic_reduce.h#L47-L54)); the vectorizer then reconstructs the wide op from **only** the destination and source and discards that operand ([`vectorize_loop.cc#L629-L664`](https://github.com/tile-ai/tilelang/blob/d36ec37c596ff8e587fc67fcf1e88bcb90cc60d6/src/transform/vectorize_loop.cc#L629-L664) — the return is `Call(op->dtype, GetVectorizedAtomicOp(vector_size), {dst, src})`, two operands only).

<details><summary>Why the dropped operand changes the emitted ordering</summary>

The CUDA codegen for both the scalar and the wide atomics appends the order only when it is present as a third operand:

- scalar [`AtomicAdd` — codegen_cuda.cc#L4597-L4608](https://github.com/tile-ai/tilelang/blob/d36ec37c596ff8e587fc67fcf1e88bcb90cc60d6/src/cuda/codegen/codegen_cuda.cc#L4597-L4608): `AtomicAdd(dst, src)` then `if (op->args.size() > 2) stream << ", " << args[2];`
- wide [`AtomicAddx2`/`AtomicAddx4` — codegen_cuda.cc#L4620-L4643](https://github.com/tile-ai/tilelang/blob/d36ec37c596ff8e587fc67fcf1e88bcb90cc60d6/src/cuda/codegen/codegen_cuda.cc#L4620-L4643): identical `if (op->args.size() > 2)` guard.

After the vectorizer drops the operand, `op->args.size()` is 2, so the guard is false and no order is emitted. The wide device helper then takes its default: [`AtomicAddx2(half_t*, ValType, int memory_order = relaxed)` — atomic.h#L557-L577](https://github.com/tile-ai/tilelang/blob/d36ec37c596ff8e587fc67fcf1e88bcb90cc60d6/src/tl_templates/cuda/atomic.h#L557-L577) branches on the order — relaxed → a plain `atomicAdd`; non-relaxed → explicit ordered PTX (`tl_atomic_add_v2_f16` with fences). So the requested `acq_rel` (id 4) becomes relaxed (id 0), silently. `AtomicAddx4` and the `float32` wide wrappers share the same default-relaxed / branch shape, so `fp32 → AtomicAddx4` is the same mechanism (I exhibited the `fp16 → AtomicAddx2` face; the x4 face is inferred from the identical guard and helper, not separately run).

</details>

**Suggested fix (proposed, not built).** One direction that fits the existing wiring is to carry the memory-order operand through the wide reconstruction — append the original op's third operand (when present) to the `{dst, src}` argument list in the vectorizer — so the wide `AtomicAddx2`/`AtomicAddx4` codegen and device helpers receive the order exactly as the scalar path does. The codegen and device helpers already accept it (the `if (op->args.size() > 2)` guard and the `memory_order` parameter are in place); only the vectorizer's two-operand reconstruction appears to drop it.

**Distinct from #2382/#2574/#2573.** #2382 (closed, fixed by #2414) is the *same* vectorizer function but a different defect — the wide helper bit-reinterprets instead of converting when the source dtype differs from the destination; its fix touched only `atomic.h` and never the operand reconstruction, so the memory-order drop is untouched (`{dst, src}` still stands at `main`). #2574 is an *illegal* memory order on `atomic_load`/`atomic_store` reaching a device assert (a missing frontend legality check; the order is carried, not dropped). #2573 is an `int64` `atomic_max`/`atomic_min` compile failure with no memory-order involvement. I searched the open and closed tracker and found no existing report of the memory-order drop on the vectorized `atomic_add` path.

**Provenance.** Not a regression — the vectorized atomic path has reconstructed the wide op from two operands (`{addr_dst, addr_src}` / `{dst, src}`) since it first shipped: it existed in the pre-refactor `atomicadd_vectorize.cc`, was relocated into `vectorize_loop.cc` (with `MutateAtomicAddExpr_`) by [#1677](https://github.com/tile-ai/tilelang/pull/1677) (`5feb2253`, merged 2026-01-16), and the line was last moved by the #2166 refactor (`431c85f1`, 2026-05-12). The `memory_order` argument for atomics arrived alongside it in [#1676](https://github.com/tile-ai/tilelang/pull/1676) (`b27fb928`, merged 2026-01-16, an ancestor of #1677), so from the moment a non-relaxed order could be requested the vectorized path has never carried it. (Origins verified via `git log`/`git blame` and `gh pr view`; the exact PR that first added the two-operand form pre-refactor is not pinned beyond "no later than #1677".)

**Reach.** Triggering requires a tile-region `T.atomic_add` (a region argument such as `Out[0:N]`, which is what routes to the wide helpers) with a non-relaxed `memory_order` *and* a per-thread inner-loop extent divisible by the dtype's atomic vector width (2 for fp16/bf16, 2-or-4 for fp32), so the add auto-vectorizes. A non-relaxed order is the rare ingredient — `relaxed` is the default, so a program only hits this if it explicitly asks for ordering; the divisible extent is common (the 128-multiple tiles typical of reduction/scatter kernels split to an even per-thread extent), so once a kernel does request ordering on a region it will usually take the dropping path. `grep -rn` over `examples/` and `testing/` this session: the shipped examples that pass `memory_order=` all pass `"relaxed"` (`examples/norm/layernorm.py:127-128`, `examples/flash_attention/example_gqa_bwd_tma_reduce_varlen.py:476`), so the downgrade is a no-op for them. The atomic tests that use a non-relaxed order (`testing/python/language/test_tilelang_language_atomic.py:104`, `memory_order="release"`; and `:46`) index a single element (`B[idx_i, idx_j]`), which routes to the scalar/extern `AtomicAdd` path — the one that honors the order — never the region/vectorized path; and `test_atomic_addx2` calls `T.atomic_addx2` directly, which has no `memory_order` parameter. So no example or test exercises the region + non-relaxed-order + even-count intersection, and the value-comparison tests would not catch an ordering downgrade regardless (they check a sum, which has no cross-thread ordering dependency).


## 评论 (1)

### arcusbuilds · 2026-07-30

I'd like to take this one.

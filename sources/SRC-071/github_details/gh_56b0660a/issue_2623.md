# [Issue #2623] [BUG][Fuzzer][wrong-code] `T.finalize_reducer(reducer, batch>1)` silently reduces only the first `batch` elements

source: https://github.com/tile-ai/tilelang/issues/2623
state: open | updated: 2026-08-22T21:03:39Z
labels: 

## 正文

### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) that this hasn't already been reported. (comment there if it has.)

### What version of TileLang are you using?

0.1.11 (source pinned to tag `v0.1.11`, commit `cd37ed5fc35ae7a60a1277c8eb49028174ac51e6`).

### System information

Reproduced on two GPUs: NVIDIA H100 80GB HBM3 (`sm_90`) and NVIDIA L40S (`sm_89`), Python 3.12/3.13, torch cu13, tilelang 0.1.11. Bit-identical mismatch counts on both — the defect is in the target-independent finalize-reducer lowering, not arch-specific codegen.

```python
import sys, tilelang, torch
print(sys.version, sys.platform)   # 3.13.x linux
print(tilelang.__version__)        # 0.1.11
print(torch.__version__)           # 2.11.x (cu13)
```

### Problem description

`T.finalize_reducer(reducer, batch=B)` with `B > 1` **silently miscomputes**: it correctly reduces only the *first `B`* of the reducer's per-thread output elements and leaves every remaining element as its un-reduced per-thread partial (mostly the cleared value, i.e. `0` for `sum`, the identity clamp for `max`/`min`). `batch=1` on the exact same kernel is correct. The **first `batch` output elements are correctly reduced and the rest are dropped** — so the number of matching elements is `batch` plus any coincidental matches (a dropped row whose leftover partial happens to equal the reduced value); with random exact-int inputs I measured e.g. batch=4 → 6/128 match (rows 0–3 correct + 2 coincidental), batch=8 → 9/128, batch=16 → 17/128, batch=1 → 128/128. The structural defect is unambiguous regardless of the coincidental count: elements `[batch, OutputDim)` are never reduced.

This is a gross value error, not float rounding — the repro uses integer-valued inputs (any reassociation is still exact) and is bit-identical across repeated launches (deterministic, not a race).

<details>
<summary>Trigger boundary (replication="all", threads=256, fp32 integer inputs, row-sum reducer)</summary>

The reducer output has `block_M` elements; with `replication="all"` each thread holds all `block_M`. The batched path processes exactly `batch` of them, so the count of correct rows is exactly `batch`:

| `block_M` (output elems) | `batch` | # correct rows | correct indices |
|---|---|---|---|
| 16 | 1  | 16/16 | all (scalar path) |
| 16 | 2  | 2/16  | `[0, 1]` |
| 16 | 4  | 4/16  | `[0, 1, 2, 3]` |
| 16 | 8  | 8/16  | `[0..7]` |
| 16 | 16 | 16/16 | all (`batch == block_M`, single call covers everything) |
| 128 | 1 | 128/128 | all |
| 128 | 4 | 4/128  | `[0, 1, 2, 3]` (the other 124 are wrong, mostly `0`) |

The defect fires **iff** the batched path is taken (`batch > 1` **and** `reducing_threads > warpSize`, so `MakeBatchAllReduce`/`run_batch` is emitted) **and** `batch < block_M` (the reducer's per-thread output count). It is accidentally correct when `batch == block_M` (the single `run_batch` happens to cover all elements) or `batch == 1` (scalar path). `max`/`min` reproduce identically.

</details>

#### Root cause

The finalize-reducer lowering does not emit the per-element outer loop on its batched path, so only the first `batch` output elements are reduced and the rest are left un-reduced. Concretely, `FinalizeReducerLowerer::Lower` ([`src/backend/common/op/finalize_reducer.h`](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/src/backend/common/op/finalize_reducer.h#L81-L112)) has two paths:

- **Scalar path** (`batch == 1` or `reducing_threads <= warpSize`, [lines 93–111](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/src/backend/common/op/finalize_reducer.h#L93-L111)): builds a `BufferStore` and **wraps it in a `For` loop over every `layout->OutputShape()[i]`** (lines 106–109), so all output elements are reduced. Emits, per element:
  ```cuda
  for (int __finred_0 = 0; __finred_0 < 128; ++__finred_0)
    o_reducer[__finred_0] = tl::AllReduce<SumOp,256,1,0>::run(o_reducer[__finred_0], workspace);
  ```

- **Batched path** (`use_batch`, [lines 81–91](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/src/backend/common/op/finalize_reducer.h#L81-L91)): emits a **single `Evaluate(Call(... run_batch ...))` with NO enclosing loop**:
  ```cuda
  tl::AllReduce<SumOp,256,1,0,SyncThreadsBarrier,4,256>::run_batch(o_reducer, workspace);
  ```
  `run_batch` covers only `batch` elements starting at `o_reducer[0]`. The outer `ceil(OutputDim / batch)` loop that the [`T.reduce` docstring promises](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/tilelang/language/reduce_op.py#L35-L39) ("the compiler emits `ceil(N/batch)` batched AllReduce calls") is simply missing from the finalize-reducer lowering. So elements `[batch, OutputDim)` are never reduced.

The scalar path is immune because it iterates the full `OutputDim`; the batched path drops the iteration entirely.

### Reproducible example code

`replication="all"`, `threads=256`, so `reducing_threads = 256 > warpSize` and the batched path is taken. Integer inputs make any reassociated sum exact — any difference is a real miscompile. Only `BATCH` changes between the correct control (`1`) and the wrong run (`4`).

```python
import torch, tilelang as tl
import tilelang.language as T

def make_kernel(BATCH, block_M=128, block_N=64):
    @T.prim_func
    def kernel(A: T.Tensor((block_M, block_N), "float32"), B: T.Tensor((block_M,), "float32")):
        with T.Kernel(1, threads=256):
            o = T.alloc_reducer(block_M, "float32", op="sum", replication="all")
            T.clear(o)
            A_s = T.alloc_shared((block_M, block_N), "float32"); T.copy(A, A_s)
            A_f = T.alloc_fragment((block_M, block_N), "float32"); T.copy(A_s, A_f)
            for i, j in T.Parallel(block_M, block_N):
                o[i] += A_f[i, j]
            T.finalize_reducer(o, batch=BATCH)     # flip BATCH 1 -> 4
            T.copy(o, B)
    return kernel

FLAGS = {tl.PassConfigKey.TL_DISABLE_WARP_SPECIALIZED: True,
         tl.PassConfigKey.TL_DISABLE_TMA_LOWER: True}

torch.manual_seed(0)
A = torch.randint(-8, 9, (128, 64), dtype=torch.int32).float().cuda()  # exact integers
ref = A.sum(dim=1)

for BATCH in (1, 4):
    B = tl.compile(make_kernel(BATCH), out_idx=-1, pass_configs=FLAGS)(A)
    ndiff = int((B != ref).sum())
    print(f"BATCH={BATCH}: ndiff={ndiff}/128")

# -> BATCH=1: ndiff=0/128    (control: scalar path, correct)
# -> BATCH=4: ndiff=122/128  (batched path: only first 4 rows correct, rest dropped to 0)
```

### Traceback

No traceback — silent, no crash. The kernel compiles and runs cleanly; the output tensor is just wrong for elements `[batch, OutputDim)`.

### Expected behavior

`T.finalize_reducer(reducer, batch=B)` should reduce **all** `OutputDim` per-thread output elements, exactly matching the `batch=1` scalar path, per the [`T.reduce` docstring](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/tilelang/language/reduce_op.py#L35-L39): "the compiler emits `ceil(N/batch)` batched AllReduce calls." Concretely, on the repro above, `BATCH=4` would then give `ndiff=0/128` (identical to `BATCH=1`); currently only the first `batch` elements are reduced and the remaining `OutputDim - batch` are silently left as their un-reduced per-thread partials.

### Additional context

Note: the maintainers' own test `test_finalize_reducer_correctness` ([`testing/python/language/test_tilelang_language_reduce.py`](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/testing/python/language/test_tilelang_language_reduce.py#L260)) only parametrizes `batch == 1` cases (the parametrize filters `c[4] == 1`) and its docstring notes *"batch>1 blocked by fragment layout bug"*; the separate `batch>1` codegen test only asserts the `run_batch` string appears, never that the result is correct. So `batch>1` is a known-unfinished path. That docstring attributes it to a *fragment layout* bug; this report identifies a concrete, independently-reproducible cause on the finalize-reducer lowering — the missing outer loop — which may be the same issue or a distinct one (I have not confirmed the "fragment layout" attribution refers to this loop). Either way, the exact-int oracle here shows the observable failure and its lowering site.

Also note this is a **performance opt-in with narrow reach**: `batch` defaults to `1` everywhere and no in-tree example, library path, or autotuner passes `batch>1` (checked this session) — so this only affects a user who manually enables the documented barrier-reduction knob. It is still a silent wrong result for that user.

**Suggested fix:** Wrap the batched `run_batch` call in the same outer loop the scalar path uses — emit `ceil(OutputDim / batch)` `run_batch` calls, each covering a `batch`-element slice of the reducer, advancing the base pointer by `batch` each iteration (matching the documented "ceil(N/batch) batched AllReduce calls" contract). Alternatively, until the batched finalize-reducer path is correct, fall back to the scalar path for `finalize_reducer` (ignore `batch`), which is already numerically correct.

**Provenance.** Not a regression — the batched finalize-reducer path was born without the loop. It was introduced by [#1976](https://github.com/tile-ai/tilelang/pull/1976) ("Batched AllReduce for better T.reduce performance", commit `6548c05f`): in that commit's `src/op/finalize_reducer.cc`, the `use_batch` branch already `return`s a single `Evaluate(Call(... ::run_batch ...))` with no enclosing loop, while the scalar path directly below it builds the `For` over `layout->OutputDim()`. (#1976's own message says it "emits `ceil(N/batch)` calls to `run_batch`", but the finalize-reducer branch does not — it emits one.) The [#2163](https://github.com/tile-ai/tilelang/pull/2163) refactor ("Share common GPU tile op lowerers", commit `38983368f`) relocated the same branch to `src/backend/common/op/finalize_reducer.h` unchanged. Still present on `main`.

**Dedup.** Searched the tracker (`gh` + `finalize_reducer` / `reducer batch`) this session. Distinct from three nearby reducer issues:
- **#2408** (`alloc_reducer(replication="all")` over-count): a `batch=1` defect (over-counts by `floor(threads/block_N)×`); here `batch=1` is *correct* and only `batch>1` fails.
- **#2542** (`reduce_sum`/`max` non-power-of-two lane drop): independent of `batch`; a lane-count issue in the AllReduce butterfly, not a missing outer loop.
- **#2524** (`reduce_sum`/`max` with `batch>1` workspace-stride vs block-index aliasing): the closest neighbor, but a *different op and file* (`T.reduce` via `reduce.h`, not `T.finalize_reducer` via `finalize_reducer.h`) and a *different mechanism* — #2524 is workspace aliasing and is correct when `reducing_threads == total_threads`, whereas this bug fails *exactly* at `reducing_threads(256) == total(256)` because the cause is a missing outer loop, not workspace aliasing. Fixing #2524 would not fix this.


## 评论 (1)

### jq-wei · 2026-08-22

I opened #3070 with a targeted fix for the current batched `finalize_reducer` lowering. It processes every output chunk and adds
numerical regression tests for multiple operations, dtypes, and batch sizes. The fix was validated on an NVIDIA L40S.

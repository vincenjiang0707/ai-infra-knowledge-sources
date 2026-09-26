# [Issue #3031] [Enhancement] Pipeline planner `LOG(FATAL)`s on a legally reused shared buffer (region-overlap check has no liveness); add liveness or at least a clean diagnostic

source: https://github.com/tile-ai/tilelang/issues/3031
state: closed | updated: 2026-08-25T07:34:14Z
labels: 

## 正文


### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the Issue Tracker that this hasn't already been reported.

### What version of TileLang are you using?

0.1.13 (reproduced this session on the released `0.1.13` wheel; source cited at the `v0.1.13` tag).

### System information

NVIDIA L40S (`sm_89`), CUDA 12.8, Python 3.13, tilelang 0.1.13. The defect is in the target-independent pipeline-planning pass, so it is not specific to one GPU.

### Problem description

A loop body that loads a shared scratch buffer with a global→shared copy and then overwrites that buffer's region again later in the same iteration — the first value fully consumed before the second write — aborts compilation with `LOG(FATAL) "Pipeline planning error: Multiple writes to overlapping buffer regions detected"` as soon as the loop is pipelined (`num_stages >= 1`). The canonical case is reusing one shared scratch buffer for two sequential `T.copy`s, but the second overwriting write need not be a copy (a plain store trips it too). The identical kernel compiles and runs to a correct result with no pipelining (`num_stages = 0`), and the same pattern with two separate buffers (or with disjoint regions) pipelines fine — so the kernel is valid and the buffer reuse is legal. The write-write conflict check (`MayConflict`) is a deliberate over-approximation — it flags any two writes whose regions intersect — but it is purely geometric with no liveness: in this repro the two writes are separated by a `reduce_sum(sh, …)` that reads the *whole* buffer, so the first write's value is provably dead before the second write (straight-line code, no data-dependent control flow). That is a case an over-approximation could resolve, not one that is genuinely undecidable. The concrete ask here is narrower than "make the planner schedule it": an internal `LOG(FATAL)` on a legal kernel is the wrong failure mode regardless — at minimum it should be a clean, actionable diagnostic.

Trigger boundary (all re-run this session): `num_stages = 0` → compiles + exact result; `num_stages = 1` and `num_stages = 2` → the `LOG(FATAL)`.

### Reproducible example code

```python
import tilelang, tilelang.language as T, torch

M, K, block_M, block_K, dtype = 128, 256, 64, 32, "int32"

@tilelang.jit(out_idx=[-1])
def kern():
    @T.prim_func
    def main(A: T.Tensor((M, K), dtype), B: T.Tensor((M, K), dtype), Out: T.Tensor((M,), dtype)):
        with T.Kernel(T.ceildiv(M, block_M), threads=128) as bx:
            sh = T.alloc_shared((block_M, block_K), dtype)     # ONE scratch buffer, reused
            acc = T.alloc_fragment((block_M,), dtype)
            partial = T.alloc_fragment((block_M,), dtype)
            T.clear(acc)
            for k in T.Pipelined(T.ceildiv(K, block_K), num_stages=2):
                T.copy(A[bx * block_M, k * block_K], sh)       # copy #1 into sh
                T.reduce_sum(sh, partial, dim=1)
                for i in T.Parallel(block_M):
                    acc[i] += partial[i]
                T.copy(B[bx * block_M, k * block_K], sh)       # copy #2 into the SAME sh
                T.reduce_sum(sh, partial, dim=1)
                for i in T.Parallel(block_M):
                    acc[i] += partial[i]
            for i in T.Parallel(block_M):
                Out[bx * block_M + i] = acc[i]
    return main

A = torch.randint(-5, 6, (M, K), dtype=torch.int32, device="cuda")
B = torch.randint(-5, 6, (M, K), dtype=torch.int32, device="cuda")
kern()(A, B)      # InternalError: Multiple writes to overlapping buffer regions detected

# CONTROL — identical body, num_stages=0: compiles and matches the int reference exactly.
```

### Traceback

```
InternalError: Pipeline planning error: Multiple writes to overlapping buffer regions
detected. Stage 0 and stage 4 are both writing to buffer 'sh' with overlapping regions.
This is not supported in pipeline planning.
```

### Expected behavior

Reusing a shared scratch buffer for two copies whose lifetimes don't overlap (each is fully read before the next write) is a normal, memory-saving pattern; it compiles and runs correctly without pipelining. Enabling `T.Pipelined` should either schedule it (treating the two writes as sequential, single-buffer uses) or, if the planner genuinely cannot, reject it with an actionable message — not abort with an internal `LOG(FATAL)`. The `num_stages = 0` run is the reference that a correct target exists.

### Additional context

**Root cause.** The write-vs-write scan in `AnalyzeCopyLastUse` treats *any* geometric region overlap between a copy stage's shared destination and a later stage's write to the same buffer as an unschedulable conflict, and aborts with `LOG(FATAL)` instead of serializing the two writes (or multi-buffering). The overlap test `MayConflict` ([`#L73-L98`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/pipeline_planning.cc#L73-L98)) is a pure `arith::IntSet` intersection with **no lifetime awareness**: it does not account for the first write's value being fully read before the second write, so serially-reused single-buffer patterns look identical to a real hazard.

- SOURCE-level root: the write-write `MayConflict` branch [`src/transform/pipeline_planning.cc#L673-L682`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/pipeline_planning.cc#L673-L682) inside `AnalyzeCopyLastUse` ([`#L644`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/pipeline_planning.cc#L644)). It only runs when the producer `pinfo.IsCopyStage()` ([`#L663`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/pipeline_planning.cc#L663)); a stage is a copy stage only when `ClassifyCopyLikeStage` sees a *global-like source into a shared destination* ([`#L627-L632`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/pipeline_planning.cc#L627-L632)).
- OPERATOR-level root: any op that classifies as a copy stage (a `T.copy` global→shared, an equivalent `T.Parallel` load-from-global loop into shared, or an im2col/TMA copy) whose shared destination region is later overwritten — by *any* write (a second copy, or a plain store) — with an overlapping region, inside a `T.Pipelined` loop with `num_stages >= 1`.

**Suggested fix.** Two tiers. The full fix is an enhancement, not a one-line guard change: teaching `AnalyzeCopyLastUse` a *liveness* check — when every consumer of the first write precedes the second write (no live read spans it), treat the buffer as a serially-reused single buffer rather than an overlapping-write conflict. That is new analysis capability the pass does not have today, and in the general case (data-dependent control flow, partial reads) it cannot always decide, so the over-approximation would still fall back to conservative in the undecidable cases. **Independent of that enhancement**, the immediate defect is the failure mode: aborting a legal kernel with an internal `LOG(FATAL)` is wrong regardless of whether liveness is added — it should be a clean, actionable frontend error that names the reused buffer and suggests distinct buffers or a higher `num_stages`. So: floor = don't `LOG(FATAL)` (turn it into a diagnostic); ideal = add the straight-line liveness case so this repro (and the common "load-use-reload same scratch" pattern) schedules.

**Provenance.** This overlapping-write check was **added by [#2444](https://github.com/tile-ai/tilelang/pull/2444) ("[Pipeline] Simplify async copy lowering", 2026-06-24)** — the same file at the parent commit contains no such check (verified locally: the fatal message appears in #2444's diff and not in its parent). So a kernel with this shape may have compiled before #2444; I have **not** build-verified the pre-#2444 behavior, so I grade this a *possible regression introduced at #2444*, not a confirmed one. First shipped in a release at `v0.1.12` (tag dated 2026-07-08, which post-dates #2444) and still live at `v0.1.13`.

**Dedup.** I searched the open and closed Issue Tracker and found no existing report of this pipeline-planning overlapping-write fatal on a serially-reused single buffer; the other pipeline issues concern distinct mechanisms.

**Impact.** When it fires it is a compile-time `LOG(FATAL)` in the target-independent pipeline-planning pass — loud, deterministic, and caught before any code is generated, so it corrupts no output and cannot reach a running workload silently; the cost is that a valid memory-saving kernel refuses to build and the message is an internal fatal rather than an actionable diagnostic. Fixing it either schedules the serial reuse (the `num_stages = 0` result proves a correct target exists) or replaces the fatal with a clean error naming the reused buffer.

**Generalization (root + 4-axis sweep, all cells re-run on 0.1.13 / L40S, one kernel per fresh process).** Two-level root — as in Root cause above: SOURCE = the lifetime-blind write-vs-write `MayConflict` branch in `AnalyzeCopyLastUse`; OPERATOR = a global-like→shared copy stage whose destination is later overwritten with an overlapping region inside a `T.Pipelined` loop.

**Shipped-example check (Part 1).** The draft cites no specific `examples/X`; its only external claim is the #2444 provenance (verified below). To ground the "distinct buffers avoid it" boundary against real code, I ran the canonical `examples/gemm/example_gemm.py` **verbatim** (`num_stages = 3`): it compiles and passes (`All check passed.`, latency ~0.032 ms). It **dodges** the bug precisely because it uses *two distinct* shared buffers (`A_shared`, `B_shared`), each written by exactly one `T.copy` — i.e. the shipped double-buffering idiom never reuses one shared buffer across two copies. No shipped example was found that writes the same shared buffer with two overlapping copies in one pipelined loop, so the trigger is not exercised by the example suite; the "common memory-saving optimization" framing is a plausible user pattern, not a demonstrated example-suite pattern.

<details><summary><b>4-axis sweep (8 cells)</b></summary>

| Axis | Cell tested | Result | Same-root? |
|---|---|---|---|
| related-type (dtype) | reused `sh`, `dtype=float16`, `num_stages=2` | `LOG(FATAL)` "Stage 0 and stage 4 … buffer 'sh'" | yes — check is geometric, dtype-agnostic |
| related-type (region) | two **adjacent** copies into partially-overlapping sub-slices `sh[:,0:32]`/`sh[:,16:48]` | `LOG(FATAL)` "Stage 0 and stage 1" | yes — fires with no consumer between the two writes |
| similar-logic (num_stages) | reused `sh`, `num_stages=1` | `LOG(FATAL)` | yes — boundary is `num_stages >= 1` |
| related-operator (2nd write) | copy #1 global→shared, then a **non-copy** `T.Parallel` store overwrites the same `sh` region | `LOG(FATAL)` "Stage 0 and stage 4" | yes — broadens class: the *second* write need not be a copy |
| related-operator (1st write) | write #1 = `T.Parallel` load-**from-global** into `sh`, write #2 likewise | `LOG(FATAL)` | yes — a parallel load-from-global loop is also classified as a copy stage |
| related-type (region, disjoint) | two copies into **disjoint** halves `sh[:,0:32]` / `sh[:,32:64]` | COMPILES OK | boundary — `MayConflict` sees no overlap; not "same buffer" but "overlapping region" |
| related-operator (non-copy 1st) | both writes **computed** (`sh[i,j]=acc[i]±k`, not derived from global) | COMPILES OK | boundary — neither stage `IsCopyStage`, so the write-write branch is skipped |
| related-type (scope) | two copies into the same **fragment** buffer (dst not shared) | COMPILES OK | boundary — `ClassifyCopyLikeStage` requires a *shared* dst |

</details>

**Class boundary (reframed).** The fatal is triggered by three ingredients together: (1) a *producer* stage that classifies as a global-like→shared copy (`T.copy` **or** an equivalent parallel load-from-global loop into a shared buffer), (2) a later *overlapping* write to that same shared region — the later write can be *any* write, not necessarily a copy, (3) inside a `T.Pipelined` loop with `num_stages >= 1`. Dropping any one avoids it: `num_stages = 0` (reference: compiles + exact result), distinct buffers (shipped-gemm idiom), disjoint sub-regions, a non-shared destination, or a producer that isn't a global→shared copy. This is broader than the title's "two `T.copy`s" — the second write being non-copy and the first write being a parallel-load loop are the same root. Title and Problem updated to the class.

**Related-source not reached.** The im2col/TMA copy path (`Im2ColOpNode`, [`#L635-L640`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/pipeline_planning.cc#L635-L640)) also sets `copy_stage = true` and would route through the same `MayConflict` fatal, but constructing a reused-buffer conv/im2col repro was not attempted this session — noted as the same root, untested. The sibling read-vs-write branch ([`#L654-L660`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/pipeline_planning.cc#L654-L660)) only bumps `last_use_stmt_index` and does not fatal, so it is a distinct, benign path.

**Reach.** Reusing one shared buffer for successive stage loads is a plausible shared-memory-budget optimization, and `T.Pipelined` with `num_stages >= 2` is the standard way to overlap load/compute in a main loop. The three ingredients together (a global→shared producer, a later overlapping write to that buffer, in a pipelined loop) are what trip it; distinct buffers, disjoint regions, or `num_stages = 0` all avoid it. The shipped example suite avoids it by always using distinct buffers, so the impact is on user kernels that hand-reuse one scratch buffer, not on the examples themselves.

## 评论 (1)

### KellyFrog · 2026-08-25

Hi!

`PipelinePlanning` pass rejects overlapping buffer writes for practical reasons: they are hard to analyse and to rerank. This is an intended design, not a bug.

This issue is therefore closed.

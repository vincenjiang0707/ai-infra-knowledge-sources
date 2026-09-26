# [Issue #3037] [BUG][Fuzzer][ice-on-valid-code] 8-bit-operand sparse `T.gemm_sp` with `K > block_K` crashes `ThreadSync` (`Cannot match type int32 vs handle`) instead of compiling

source: https://github.com/tile-ai/tilelang/issues/3037
state: open | updated: 2026-09-08T07:46:51Z
labels: 

## 正文


### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) and [Discussions](https://github.com/tile-ai/tilelang/discussions) that this hasn't already been reported. (+1 or comment there if it has.)

### What version of TileLang are you using?

0.1.13 (latest release)

### System information

TileLang 0.1.13; NVIDIA L40S (sm_89), CUDA 12.8, PyTorch 2.8.0. Reproduced this session on sm_89. The crashing pass (`ThreadSync`) is target-agnostic; the sparse 8-bit-operand path is the sm8x metadata path (`arch="8.0"`).

### Problem description

An 8-bit-operand 2:4 structured-sparse GEMM built with `T.gemm_sp` aborts at compile time with

```
InternalError: Cannot match type int32 vs handle
```

as soon as `K > block_K`, i.e. whenever the standard K-loop iterates more than once. This session both `in_dtype=int8` and `in_dtype=float8_e5m2` (the two 8-bit sparse operand dtypes) crash identically in the same `ThreadSync`/`Summarize`/`BinaryOpMatchTypes` frame; `float16`/`bfloat16` sparse (16-bit metadata layout) compiles. The rest of this report uses `int8` as the running example, but see §17 for the fp8 twin. The identical kernel with `block_K == K` (a single K-block) compiles cleanly (it reaches a runnable kernel; see the note on numeric correctness below). Splitting K into tiles is the ordinary way GEMM pipelines the K dimension (the shipped `examples/gemm_sp/example_gemm_sp.py` runs `K=1024, block_K=64/128` = 16/8 K-iterations by default), so this is a supported, in-contract shape rather than an odd size.

The crash is raised in the `ThreadSync("shared.dyn")` pass, not at codegen; there is no way to reach a kernel.

<details><summary>Trigger boundary (what flips PASS→crash), tested on sm_89</summary>

| in_dtype | metadata | K | block_K | K-iterations | result |
|---|---|---|---|---|---|
| int8 | int32 | 256 | 256 | 1 | compiles to a runnable kernel (no crash) |
| int8 | int32 | 256 | 128 | 2 | `Cannot match type int32 vs handle` (compile abort) |

`float16` sparse GEMM with the same multi-iteration K-loop (`K=256, block_K=128`, verified this session) compiles — the crash is specific to the 8-bit-operand (int8/fp8_e5m2) sparse metadata read path. `fp8_e5m2` with the same multi-K loop crashes identically (see §17).

The boundary that flips is *compile vs compile-crash*: the single-K-block int8 kernel gets through the whole pass pipeline to a launchable kernel, while adding a second K-iteration aborts in `ThreadSync`. (Separately, the numeric result of the single-K-block int8 sparse kernel did not match the dense reference on this sm_89 run — an unrelated int8-sparse-on-sm_89 correctness question, not the ICE reported here; this issue is purely about the multi-K-iteration compile abort.)
</details>

### Reproducible example code

```python
import os, sys, torch, tilelang
import tilelang.language as T
from tilelang.layout import make_cutlass_metadata_layout
from tilelang.cuda.intrinsics.sparse_layout import get_e_factor

# 0.1.13: compress / randint_semi_sparse live in the gemm_sp example, not in
# tilelang.utils.sparse. Point at that dir (adjust to your checkout).
sys.path.insert(0, os.path.join(os.path.dirname(tilelang.__file__),
                                "..", "examples", "gemm_sp"))
from sparse_utils import compress, randint_semi_sparse

# int8 2:4 structured-sparse GEMM (M=N=128, K=256). The ONLY thing that varies
# between the two runs is block_K: 128 -> the K-loop runs twice, 256 -> one
# iteration. Everything else (dtypes, layout, API) is identical.
def build(block_K):
    M, N, K = 128, 128, 256
    block_M, block_N = 128, 128
    in_dtype, e_dtype, accum = "int8", "int32", "int32"
    E_factor = get_e_factor(in_dtype, e_dtype)   # 0.1.13: get_e_factor('int8','int32') == 32

    @T.prim_func
    def main(A_sparse: T.Tensor((M, K // 2), in_dtype),
             E: T.Tensor((M, K // E_factor), e_dtype),
             B: T.Tensor((K, N), in_dtype),
             C: T.Tensor((M, N), accum)):
        with T.Kernel(T.ceildiv(N, block_N), T.ceildiv(M, block_M), threads=128) as (bx, by):
            A_shared = T.alloc_shared((block_M, block_K // 2), in_dtype)
            B_shared = T.alloc_shared((block_K, block_N), in_dtype)
            E_shared = T.alloc_shared((block_M, block_K // E_factor), e_dtype)
            C_frag = T.alloc_fragment((block_M, block_N), accum)
            T.annotate_layout({
                E: make_cutlass_metadata_layout(E, mma_dtype=in_dtype, arch="8.0"),
                E_shared: make_cutlass_metadata_layout(E_shared, mma_dtype=in_dtype, arch="8.0")})
            T.clear(C_frag)
            for k in T.Pipelined(T.ceildiv(K, block_K), num_stages=1):
                T.copy(E[by * block_M, k * block_K // E_factor], E_shared)
                T.copy(A_sparse[by * block_M, k * block_K // 2], A_shared)
                T.copy(B[k * block_K, bx * block_N], B_shared)
                T.gemm_sp(A_shared, E_shared, B_shared, C_frag, transpose_A=False, transpose_E=False)
            T.copy(C_frag, C[by * block_M, bx * block_N])
    return main, (M, N, K)

def run(block_K):
    main, (M, N, K) = build(block_K)
    kernel = tilelang.compile(main, out_idx=[3])           # crashes here for block_K=128
    A = randint_semi_sparse(M, K, -3, 4, dtype=torch.int8, device="cuda")
    B = torch.randint(-3, 4, (K, N), device="cuda", dtype=torch.int8)
    A_sparse, E = compress(A, meta_dtype=torch.int32)
    kernel(A_sparse, E, B)                                 # launches (single-K-block only)
    return "compiled + launched"

# Control: single K-block (block_K == K). Compiles to a runnable kernel (no crash).
print("block_K=256 (1 K-iteration):", run(256))           # -> compiled + launched

# Trigger: same kernel, K split into two block_K=128 tiles (2 K-iterations).
print("block_K=128 (2 K-iterations):", run(128))
# -> InternalError: Cannot match type int32 vs handle  (compile-time abort)
```

### Traceback

```
File ".../tilelang/cuda/pipeline.py", line 236, in CUDAPassPipelineBody
    mod = tilelang.transform.ThreadSync("shared.dyn")(mod)
  ...
  tvm::tl::TileLangThreadSyncPlanner::Summarize(std::vector<...StmtEntry...>, tvm::tirx::ForNode const*)
  tvm::operator<(tvm::PrimExpr, tvm::PrimExpr)
  tvm::less(tvm::PrimExpr, tvm::PrimExpr, tvm::Span)
  .../3rdparty/tvm/src/tirx/op/op.cc:249, in tvm::BinaryOpMatchTypes(PrimExpr&, PrimExpr&, Span)
tvm.error.InternalError: Cannot match type int32 vs handle
```

Immediately before the fatal check the pass logs the offending pair (the `LOG(INFO)` at `op.cc:248`), e.g.

```
tx1 % 64 // 32 * 4096 + tx1 % 16 * 64 + (tx1 % 32 // 16 + tx1 % 4 // 2) % 2 * 16 + 5159 neg_inf
```

— an `int32` index on the left and a `neg_inf` sentinel (`handle` dtype) on the right. (`FindConflict` / `PointerAccessIsDisjoint` are inlined, so the last named frame is `Summarize`.)

### Expected behavior

The kernel should compile (as the `block_K==K` control shows, the single-K-block variant of the identical kernel reaches a runnable kernel without a `ThreadSync` abort); an `int8` sparse GEMM with `K` split across multiple `block_K` tiles is the ordinary pipelined K-loop. The single-K-block variant compiles on the same path, so the multi-K-iteration case should also compile rather than aborting in `ThreadSync`.

### Additional context

**Root cause.** `ThreadSync`'s disjointness test compares an `int32` shared-memory offset against a `±inf` sentinel — the sentinel that `EvalSet` returns when it cannot bound the composed 8-bit sparse metadata index over the K-loop var — and the type-matcher rejects `int32 vs handle`.

<details><summary>Mechanism</summary>

This is a cross-pass interaction between two passes (the int8-vs-fp16 divergence is explained below — each index subterm is individually boundable; the unboundedness comes from `EvalSet`'s loop-var relaxation of the composed int8 index):

1. The **`gemm_sp` lowering** — `ldmatrix_e` in [`mma_sp_macro_generator.py`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/cuda/intrinsics/macro/mma_sp_macro_generator.py#L299) picks a per-dtype thread→(row,col) metadata layout (for `int8`, `metadata_32bit_load_32x1_to_shared_16x2_layout_8bit`) and composes it with the cutlass-interleaved metadata layout from [`make_cutlass_metadata_layout_sm8x`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/layout/gemm_sp.py#L121), whose inner `ColumnMajorInterleaved` contains `bitwise_and` subterms ([`gemm_sp.py:140-141`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/layout/gemm_sp.py#L140)). The result is a shared-memory index built from `%`, `//`, and `&` over the thread var.

2. The **`ThreadSync("shared.dyn")`** barrier-planning pass. When the K-loop iterates more than once, its per-loop handler [relaxes each access's touched `IntSet` over the loop variable](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/thread_storage_sync.cc#L878) via [`arith::EvalSet`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/thread_storage_sync.cc#L887). For the composed `int8` metadata index this relaxation yields an **unbounded** `IntSet`, so `.min()`/`.max()` return the `neg_inf`/`pos_inf` sentinel (a `handle`-typed node). The subsequent disjointness test in [`PointerAccessIsDisjoint`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/thread_storage_sync.cc#L1503) forms [`lhs_max < rhs_min`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/thread_storage_sync.cc#L1548) with one side the `int32` offset and the other the sentinel, which fails [`BinaryOpMatchTypes` — `Cannot match type`](https://github.com/tile-ai/tvm/blob/8df8ebd61659505dd7005f4820b030e983e2c005/src/tirx/op/op.cc#L249) (the preceding [`LOG(INFO)` at `op.cc:248`](https://github.com/tile-ai/tvm/blob/8df8ebd61659505dd7005f4820b030e983e2c005/src/tirx/op/op.cc#L248) is the `... neg_inf` line above).

With a single K-block the loop is one iteration, so the loop-var relaxation at `thread_storage_sync.cc:878` never runs and the sentinel is never formed — which is why `block_K==K` compiles.

The int8-vs-fp16 divergence is confirmed empirically (the `float16` sparse metadata read with the same multi-K K-loop compiles cleanly — see Reach — while `int8` aborts) and both dtypes share the *same* `ColumnMajorInterleaved` layout, so the `bitwise_and` subterm is present for both. Probing the individual subterms this session (via `arith::Analyzer::const_int_bound` over `tx∈[0,128)`, `k∈[0,4)`) shows **each subterm is individually bounded** — `tx & 15` → `[0,15]`, `tx % 16` → `[0,15]`, `tx // 16` → `[0,7]`, and the composed forms `(tx&15)+k*32` (int8 `E_factor`) → `[0,111]` and `(tx%16)+k*16` (fp16) → `[0,63]` are all finite. So the unbounded `IntSet` is **not** produced by `bitwise_and` alone (a common suspicion, refuted here); it arises in `EvalSet`'s *loop-variable relaxation* of the fully-composed int8 metadata index — a different algorithm from `const_int_bound` that gives up (returns the ±inf sentinel) on the int8 index's particular nesting of `%`/`//`/`&` over the relaxed loop var, whereas the shallower fp16 index (`E_factor=16`, `metadata_16bit` thread layout) stays boundable. The precise nesting that defeats `EvalSet` is the int8 `metadata_32bit_load_32x1_to_shared_16x2_layout_8bit`-composed index; a maintainer fixing this need only make the sentinel non-fatal (see Suggested fix), independent of which subterm triggers it.

</details>

**Suggested fix.** Make the touched-set relaxation robust to unbounded/`inf` bounds — an access whose relaxed `EvalSet` bound is `±inf` should be treated as a conflict (conservatively insert a barrier) rather than feeding a `handle`-typed sentinel into the `<` comparison in `PointerAccessIsDisjoint`. A guard for `is_pos_inf`/`is_neg_inf` before building `lhs_max < rhs_min` (returning "not disjoint") would turn the crash into a correctly-synced kernel. Independently, expressing the int8 metadata index so `EvalSet` can bound it would also close the path (not verified end-to-end).

**Provenance.** Reproduced on 0.1.13 (the version tested; the older `T.gemm_sp_v2` spelling was merged into `T.gemm_sp` in the interim). The sparse GEMM backend that carries this int8 metadata path was reworked in [#2048](https://github.com/tile-ai/tilelang/pull/2048) (`[Backend] Refactor gemm_sp`, merged 2026-05-19, first in 0.1.10), but the crash predates it and survives it. Not a functionality regression: the int8 multi-K-iteration configuration has no passing history — see Reach.

**Dedup.** I searched the open and closed tracker and found no existing report of this compile crash. The nearby sparse issues are different defects: silent K-tail drop on non-atom-multiple K (#2605), the `block_N ≡ 8 (mod 16)` sm_90 miscompute (#2603), the metadata-layout non-bijection (#2606), and the missing proxy fence (#2634) — all silent-value/wrong-code, none a `ThreadSync` type-mismatch ICE.

**Impact.** The narrow ingredient is the 8-bit-operand (int8/fp8_e5m2) sparse metadata path combined with a multi-iteration K-loop (`K > block_K`); float16/bfloat16 and single-K-block 8-bit are unaffected. When it fires it is a compile-time `ThreadSync` abort — loud and deterministic (identical error on 3 repeat runs — not a race), caught immediately at `tilelang.compile`, so it blocks that sparse kernel from building but corrupts no data and cannot reach a running workload silently. Fixing it closes this compile-time boundary class (making any 8-bit-operand sparse GEMM with a real pipelined K-loop buildable) rather than changing any numeric result.

**Reach.** The trigger is the ordinary pipelined GEMM K-loop, `K > block_K` — a canonical GEMM idiom, and the shipped `examples/gemm_sp/example_gemm_sp.py` runs [`for k in T.Pipelined(T.ceildiv(K, block_K), ...)`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/examples/gemm_sp/example_gemm_sp.py#L33) with a default `K=1024, block_K=64` (16 K-iterations). The one rare ingredient is an **8-bit operand** (`int8`/`fp8_e5m2`): every 8-bit case in [`testing/python/tilelibrary/test_tilelang_tilelibrary_gemm_sp.py`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/testing/python/tilelibrary/test_tilelang_tilelibrary_gemm_sp.py) uses `K == block_K` (single K-block: `(128,128,64,block_K=64)` int8, `(64,128,128,block_K=128)` int8, `(128,128,64,block_K=64)` fp8_e5m2), the only multi-K rows are `float16`/`bfloat16`, and the shipped example is `matmul_sp_fp16` (fp16-only). So the 8-bit × (`K > block_K`) intersection is exercised nowhere in examples or tests, which is why CI is green.

**Example-run result (this session, 0.1.13, v0.1.13 `examples/gemm_sp/`).** I ran the shipped `example_gemm_sp.py` verbatim. Its default 1024³ config compiles cleanly (no `ThreadSync` abort) but fails at *runtime* on sm_89 with `Failed to set the allowed dynamic shared memory size to 167936` — an sm_89 SMEM-capacity limit, unrelated to this ICE. Re-run on a config that fits sm_89 (`--m 256 --n 256 --k 256 --block_M 128 --block_N 128 --block_K 64 --num_stages 1`, 4 K-iterations, multi-K) it **compiles and passes precision** (`Precision check passed. diff: 0.00158`). So the shipped example **dodges this bug because it is fp16** (16-bit metadata layout, group=32/interweave=4), not because it avoids the multi-K loop — a multi-K fp16 sparse GEMM is exactly what it exercises and it works. The bug requires the 8-bit-operand metadata layout, which no shipped example or test uses together with `K > block_K`.

Adjacent configurations tested this session on sm_89 (0.1.13), each in a fresh process/cache (see §17 for the full 4-axis sweep):

| config | K / block_K | K-iters | result |
|---|---|---|---|
| int8 sparse (trigger) | 256 / 128 | 2 | `Cannot match type int32 vs handle` |
| int8 sparse | 256 / 64 | 4 | `Cannot match type int32 vs handle` (same root) |
| **fp8_e5m2** sparse | 256 / 128 | 2 | `Cannot match type int32 vs handle` (**same root**, same frame) |
| int8 sparse, transpose_E | 256 / 128 | 2 | `Cannot match type int32 vs handle` (same root) |
| int8 sparse (control) | 256 / 256 | 1 | compiles + launches |
| **float16** sparse | 256 / 128 | 2 | **compiles** (16-bit metadata layout, no crash) |
| **dense** int8 `T.gemm` (control) | 256 / 128 | 2 | **compiles** (no sparse metadata → no crash) |
| int8 sparse, repeat-run | 256 / 128 | 2 | identical crash ×3 (deterministic ICE, not a race) |

Same-root vs distinct: all the 8-bit-operand multi-K rows (int8 and fp8_e5m2, block_K = 128 and 64, transpose_E on/off) are the **same** root — any `K > block_K` 8-bit sparse loop aborts identically in the same `Summarize`/`BinaryOpMatchTypes` frame. The non-crashing rows delimit the boundary: single-K-block int8 (no loop-var relaxation), fp16 multi-K (16-bit metadata layout), and dense int8 multi-K (no sparse metadata layout at all) all compile, isolating the defect to *8-bit-operand sparse metadata × multi-iteration K-loop*. (Separately: the single-K-block int8 sparse kernel launches but its result did not match a dense `int8→int32` reference on this sm_89 run — max abs diff 188; an unrelated int8-sparse-on-sm_89 correctness question, deliberately out of scope for this compile-abort issue.)

**Generalization (root levels + 4-axis sweep, all cells RUN this session).**

*Two-level root.*

- **SOURCE-level root** (which implementation is fragile): [`PointerAccessIsDisjoint`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/thread_storage_sync.cc#L1503) forms [`lhs_max < rhs_min`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/thread_storage_sync.cc#L1548) from touched-`IntSet` bounds that the per-loop handler [relaxes over the loop var via `arith::EvalSet`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/thread_storage_sync.cc#L887). When `EvalSet` cannot bound the composed metadata index it returns the `±inf` sentinel (a `handle`-typed node); `<` on `int32` vs `handle` fails [`BinaryOpMatchTypes`](https://github.com/tile-ai/tvm/blob/8df8ebd61659505dd7005f4820b030e983e2c005/src/tirx/op/op.cc#L249). The missing guard (no `is_pos_inf`/`is_neg_inf` check before the `<`) is the true fragile site — it is generic to *any* access whose relaxed `IntSet` is unbounded.
- **OPERATOR-level root** (what correlates): the `T.gemm_sp` **8-bit-operand metadata read** — [`ldmatrix_e`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/cuda/intrinsics/macro/mma_sp_macro_generator.py#L299) selects a `metadata_*_layout_8bit` thread→(row,col) map composed with the 32-bit-metadata `ColumnMajorInterleaved` (`group=16, interweave=2`) that [`make_cutlass_metadata_layout_sm8x`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/layout/gemm_sp.py#L121) *forces* onto 8-bit operands ([the sm8x layout requires 32-bit metadata for `int8`/`uint8`/fp8, 16-bit for fp16/bf16](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/layout/gemm_sp.py#L128-L132)). This 32-bit-metadata interleave is the composed index `EvalSet` gives up on; the 16-bit fp16 interleave (`group=32, interweave=4`) stays boundable.

**4-axis sweep** (each cell run in a fresh process + fresh `TILELANG_CACHE_DIR`, `K=256`, `block_M=block_N=128`, `threads=128`, `num_stages=1`; observed result recorded, not asserted):

| axis | cell tested | result | same-root? |
|---|---|---|---|
| related-type | `fp8_e5m2` a_dtype + int32 meta, block_K=128 (2 K-iters) | `Cannot match type int32 vs handle` — identical `ThreadSync`/`Summarize`/`BinaryOpMatchTypes` frame | **SAME** — bug is the 8-bit family, not int8 alone |
| related-type | `float16` a_dtype + int16 meta, block_K=128 (2 K-iters) | compiles cleanly | distinct — fp16 uses the 16-bit metadata layout that `EvalSet` can bound |
| related-type | `int8` a_dtype + **int16** meta, multi-K | `ValueError: metadata should be 32 bit, got int16` at layout build | unreachable config — sm8x forces 32-bit meta on 8-bit operands |
| related-type | `float16` a_dtype + **int32** meta, multi-K | `ValueError: metadata should be 16 bit, got int32` at layout build | unreachable config — sm8x forces 16-bit meta on fp16 (cannot cross fp16 into the crashing layout) |
| related-type | `uint8` a_dtype + int32 meta, multi-K | `KeyError: uint8` in sparse `GROUP_CONFIG` | unreachable config — uint8 is not a supported sparse operand |
| related-operator | `int8` `gemm_sp` **transpose_E=True**, block_K=128 (2 K-iters) | `Cannot match type int32 vs handle` (same frame) | **SAME** — the other `ldmatrix_e` branch still composes the same metadata index |
| related-operator | dense `int8` `T.gemm`, block_K=128 (2 K-iters) | compiles cleanly | distinct — no sparse metadata layout, so no unbounded index |
| related-source | `int8` sparse, **block_K=64** (4 K-iters) | `Cannot match type int32 vs handle` (same frame) | **SAME** — any `K > block_K` count relaxes over the loop var |

**Example-run (PART 1).** The shipped `examples/gemm_sp/example_gemm_sp.py` is fp16-only (`matmul_sp_fp16`). Run verbatim (v0.1.13 sources), it **compiles and passes precision** on a sm_89-fitting config (`--k 256 --block_K 64`, 4 K-iters, multi-K): `Precision check passed. diff: 0.00158`. Its 1024³ default compiles but hits an unrelated sm_89 SMEM-capacity runtime error (`Failed to set the allowed dynamic shared memory size to 167936`). So the shipped example **dodges this bug because it is fp16, not because it avoids the multi-K loop** — it runs the multi-K loop successfully. Verified there is no shipped example or test that combines an 8-bit operand with `K > block_K`.

**Reframe.** Boundary is wider than the original int8-only framing but still bounded: the bug is the **8-bit-operand sparse family (int8 and fp8_e5m2)** — precisely the set that `make_cutlass_metadata_layout_sm8x` forces onto the 32-bit-metadata ColumnMajorInterleaved. It is *not* reachable for fp16/bf16 (different, boundable layout) nor for uint8 (unsupported operand). Title and Problem updated to "8-bit-operand". No new distinct bug was found while sweeping (the fp16/int16-meta and fp16/int32-meta `ValueError`s and the uint8 `KeyError` are input-validation guards firing correctly, not defects).

## 评论 (1)

### ZenAlexa · 2026-09-08

I checked the reported kernel with TileLang 0.1.14, targeting `sm_89` on Ubuntu 24.04 with Python 3.12.3. Both `int8` and `float8_e5m2` complete lowering through CUDA source generation with `block_K` set to 256, 128, and 64. The unbounded-interval guard from #3050 is included in this release and covers the reported `ThreadSync` comparison. This verification covers the compiler passes and generated source; GPU execution and numerical results remain to be checked.


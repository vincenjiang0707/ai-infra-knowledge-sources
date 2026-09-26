# [Issue #3012] [BUG][Fuzzer][ice-on-valid-code] `T.gemm` on a `T.reshape`d 1D→2D operand aborts ("shape should be at least 2") instead of compiling

source: https://github.com/tile-ai/tilelang/issues/3012
state: closed | updated: 2026-08-24T07:51:24Z
labels: 

## 正文

### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) and [Discussions](https://github.com/tile-ai/tilelang/discussions) that this hasn't already been reported. (+1 or comment there if it has.)

### What version of TileLang are you using?

0.1.13

### System information

TileLang 0.1.13 / CUDA 12.8 / PyTorch 2.8.0, NVIDIA L40S (sm_89). The defect is in the target-independent `LowerTileOp` pass, so it is not arch-gated.

### Problem description

Passing a `T.reshape`d (or `T.view`ed) shared buffer as a `T.gemm` operand aborts compilation with an internal check:

```
tvm.error.InternalError: Check failed: (buffer->shape.size() >= 2) is false:
The dimension of Buffer "As" with shape (1024,) should be at least 2
```

The reshaped operand *is* 2D — e.g. `T.reshape(As, (M, K))` — but the check reports its shape as the original 1D `(1024,)`. `T.reshape` returns a view that shares the source buffer's data var (`return T.Tensor(shape, src.dtype, src.data)`), and the GEMM lowering resolves the operand's access pointer back to the *underlying allocation* keyed by that data var, recovering the pre-reshape 1D buffer rather than the 2D view. The same 1D→2D reshape works fine as a `T.copy` source/target; only the GEMM operand path trips.

Not a regression — see Provenance.

### Reproducible example code

```python
import tilelang
import tilelang.language as T
import torch

# reshape a 1D shared buffer to 2D, then use it as a T.gemm operand -> compile abort
@tilelang.jit(out_idx=[-1])
def make(M, K, N):
    @T.prim_func
    def main(A: T.Tensor((M * K,), "float16"), B: T.Tensor((K, N), "float16"),
             C: T.Tensor((M, N), "float32")):
        with T.Kernel(1, threads=128) as bx:
            As = T.alloc_shared((M * K,), "float16")   # 1D shared
            T.copy(A, As)
            Am = T.reshape(As, (M, K))                 # documented 2D view over As
            Bs = T.alloc_shared((K, N), "float16")
            T.copy(B, Bs)
            Cf = T.alloc_fragment((M, N), "float32")
            T.clear(Cf)
            T.gemm(Am, Bs, Cf)                         # <-- aborts: "As with shape [1024] should be at least 2"
            T.copy(Cf, C)
    return main

M, K, N = 32, 32, 32
a = torch.randn(M * K, device="cuda", dtype=torch.float16)
b = torch.randn(K, N, device="cuda", dtype=torch.float16)
make(M, K, N)(a, b)   # InternalError at compile time
```

<details>
<summary>Two controls that compile and return the correct result (isolate the defect)</summary>

```python
# CONTROL A: allocate the operand directly as 2D (no reshape) -> compiles, correct.
As = T.alloc_shared((M, K), "float16")
T.copy(A2d, As); T.gemm(As, Bs, Cf)            # ORACLE: PASS

# CONTROL B: the SAME 1D->2D reshape used as a T.copy target -> compiles, correct.
Am = T.reshape(As, (M, K))
T.copy(Am, C2d)                                 # ORACLE: PASS
```

Control A shows a 2D shared operand GEMMs correctly; Control B shows the 1D→2D reshape view is otherwise usable. Reshaping either operand (A or B) into GEMM aborts identically (`"Bs" with shape (1024,) should be at least 2`).
</details>

### Traceback

```
tvm.error.InternalError: Check failed: (buffer->shape.size() >= 2) is false:
The dimension of Buffer "As" with shape (1024,) should be at least 2
  File ".../src/transform/lower_tile_op.cc", line 409, in tvm::tl::LowerTileOpPass::CheckAndGetBufferRowSize(...)
  ... in tvm::tl::LowerTileOpPass::VisitExpr_(tvm::tirx::CallNode const*)
```

### Expected behavior

`T.gemm` should compile with a reshaped operand and compute the same result as the equivalent kernel that allocates the operand as 2D directly (Control A above), since `T.reshape` is documented to return "a new buffer view with the specified shape" and the reshaped operand is genuinely 2D. At minimum, if a reshaped operand is not meant to be supported here, a clear frontend error naming `T.gemm`/`T.reshape` would be preferable to an internal `buffer->shape.size() >= 2` abort that reports the wrong (pre-reshape) shape.

### Additional context

**Root cause.** The GEMM operand lowering measures the operand's rank on the *underlying 1D allocation* instead of on the 2D reshaped view it was actually given — so a legitimate 2D view (rank 2) is rejected because its backing buffer is rank 1.

<details><summary>Mechanism (how the view's rank is bypassed)</summary>

`T.reshape`/`T.view` build the 2D operand over the source buffer's existing data var ([`customize.py:60-74`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/language/customize.py#L60-L74), `return T.Tensor(shape, src.dtype, src.data)`). When lowering the operand's `tvm_access_ptr`, the pass looks the buffer up by that data var in `buffer_map_` ([`lower_tile_op.cc:437-438`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/lower_tile_op.cc#L437-L438)), which returns the original 1D `alloc_buffer` (shape `[1024]`), and hands it to `CheckAndGetBufferRowSize`, whose `ICHECK(buffer->shape.size() >= 2)` fails ([`lower_tile_op.cc:408-411`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/transform/lower_tile_op.cc#L408-L411)). It is reached only via the swizzled-`ptx_ldmatrix` access-pointer rewrite, so it is that path — not GEMM lowering in general — that trips.

</details>

**Suggested fix.** In the GEMM operand lowering (`lower_tile_op.cc`), resolve the operand shape/row-size from the reshaped view the GEMM was actually passed (the 2D buffer) rather than from `buffer_map_[data_var]`, so a legitimate view is measured with its own shape. This likely requires threading the view's shape through the access-pointer resolution, not a one-line change.

**Provenance.** Not a regression. Both `src/transform/lower_tile_op.cc` and the `CheckAndGetBufferRowSize` guard (with its `should be at least 2` message) have existed since the initial codebase migration ([#10](https://github.com/tile-ai/tilelang/pull/10), `git log -S`/`--diff-filter=A` both point at that commit), so the check predates any recent change. Still present on `main` (checked `origin/main` @ `27f68b4e` this session): the `CheckAndGetBufferRowSize` helper was refactored away, but the identical `ICHECK(buffer->shape.size() >= 2)` on the operand's underlying (reshape-aliased) allocation now lives in `GetSwizzleShapeInfoChecked` ([`src/layout/gemm_layouts.cc#L405-L407`](https://github.com/tile-ai/tilelang/blob/27f68b4e95f8aa21320a47ebc95e170c2f8aa7c3/src/layout/gemm_layouts.cc#L405-L407), message reworded to "Swizzle layout expects rank >= 2 buffer"). Same guard, same rank-of-underlying-alloc check, same swizzled-`ptx_ldmatrix` path — so the crash is live on `main`, not just the `0.1.13` release.

**Class (operator-level root).** The assert sits on the swizzled-`ptx_ldmatrix` access-pointer rewrite (source detail in the Root-cause `<details>` above), so it affects *any* tile op whose shared-memory operand goes through that permuted-layout rewrite when the operand is a `data`-var-sharing view (`T.reshape`/`T.view`) over a genuinely 1D shared allocation — not just `T.gemm`.

**4-axis generalization (0.1.13, L40S; every cell run this session, one kernel per fresh process).**

| axis | cell tested | result | same-root? |
|---|---|---|---|
| — (baseline) | `T.reshape` 1D→2D **shared** A operand → `T.gemm` | abort `"As" (1024,) should be at least 2` (line 409) | — |
| baseline | `T.reshape` 1D→2D shared **B** operand → `T.gemm` | abort identically `"Bs" (1024,)` | yes |
| similar-logic | `T.view` (sibling, same `return T.Tensor(shape,…,src.data)`) shared A → `T.gemm` | abort identically `"As" (1024,)` (line 409) | yes |
| related-type (scope) | `T.reshape` 1D→2D **fragment** operand → `T.gemm` | **compiles, correct** (err 3.8e-6) — no ldmatrix-over-shared, so `CheckAndGetBufferRowSize` never reached | boundary (distinct path) |
| related-type (rank) | `T.reshape` **3D→2D** shared operand → `T.gemm` (underlying alloc rank ≥ 2) | **compiles**; result correct when 3D storage is laid out row-major identical to the view (err 3.8e-6) | boundary (rank check passes; row-size value is discarded `(void)`, not load-bearing for correctness) |
| related-source | `CheckAndGetBufferRowSize`'s only callers (`:576`,`:680`) both live in the `ptx_ldmatrix` permuted-layout rewrite | source read: confirms the abort is the ldmatrix path, shared by any op emitting `ptx_ldmatrix` over a reshaped shared buffer | yes (shared fragile code) |
| control | directly-allocated 2D shared operand (no view) → `T.gemm` | compiles, correct (err 3.8e-6) | — |
| control | same 1D→2D `T.reshape` view fed to `T.copy` instead of `T.gemm` | compiles, matches reference (this is the shipped test path) | — |

**Class boundary.** The class is *a `data`-var-sharing view (`T.reshape`/`T.view`) over a genuinely 1D **shared** allocation, passed as a `T.gemm` operand* — same root across the reshape/view siblings and both operand positions. The boundary is sharp on two axes the draft previously did not pin: (a) **scope** — a 1D *fragment* reshape into `T.gemm` compiles correctly (it does not route through `ptx_ldmatrix`-over-shared); (b) **rank** — a ≥2D underlying alloc passes the `>= 2` check and computes correctly, so the defect is exclusively the loud abort on a 1D-underlying shared alloc, not a silent miscompile. An earlier candidate "3D→2D reshape gives wrong values" was **refuted**: the wrong result came from a fill that placed data at different offsets than the row-major view implies, not from the reshape/gemm path (verified by re-running with storage laid out identical to the view → correct).

**Distinct-adjacent, not filed.** `T.gemm_sp`/`wgmma_gemm`/`tcgen05_gemm` are sibling GEMM operators in the same pass, but each needs extra operands (sparse metadata) or specific hardware to set up a valid reshaped-shared-operand kernel; not exercised this session. No new bug found while sweeping.

**Dedup.** I searched the open and closed tracker and found no existing report of this defect.

**Reach.** (Example verified by run, 0.1.13.) The trigger is a documented view op (`T.reshape`'s docstring returns "a new buffer view with the specified shape") fed into `T.gemm`. The 1D→2D shared-buffer reshape itself is exercised by the shipped test `test_reshape_smem_1d_2_2d` (`testing/python/language/test_tilelang_language_reshape.py`). I ran that test **verbatim** on 0.1.13 (`git show v0.1.13:...` → `pytest ...::test_reshape_smem_1d_2_2d`): it **passes** (`1 passed`). It dodges this bug because its kernel body feeds the reshaped view to `T.copy` (`T.copy(A_smem_reshaped, B)`), not `T.gemm` — the copy path never resolves the operand back to the underlying alloc through the `ptx_ldmatrix` permuted-layout rewrite. So the shipped 1D→2D-reshape coverage exists but stops short of the GEMM-operand path; no test feeds a reshaped operand into `T.gemm`, and CI is green.

**Impact.** The trigger is narrow: a `T.reshape`/`T.view` view (rather than a directly-allocated 2D buffer) passed specifically as a `T.gemm` operand. When it fires it is a compile-time `InternalError` abort — loud and caught immediately at build, so nothing is silently miscompiled and no wrong values can reach a running workload; the cost is that this valid kernel refuses to build and the abort reports the wrong (pre-reshape) shape, which is misleading to diagnose. Fixing it closes this view-as-GEMM-operand boundary (measure the operand by the view's own shape) and replaces a wrong-shape internal assert with either a compile or a clear frontend error.

## 评论 (1)

### KellyFrog · 2026-08-24

Hi!

This issue can no longer be reproduced and is likely fixed by PR #2836.

The issue is therefore closed.

# [Issue #3120] [Perf] Lower T.any_of / T.all_of via warp vote intrinsics (__any_sync / __all_sync) where safe

source: https://github.com/tile-ai/tilelang/issues/3120
state: open | updated: 2026-09-01T04:31:50Z
labels: enhancement, good first issue

## 正文

## Current behavior

`T.any_of(buffer)` / `T.all_of(buffer)` (`tilelang/language/logical.py`) lower through the `tl.any_of` / `tl.all_of` builtins (`src/op/logical.cc`) to `call_extern` of the device helpers `tl::Any` / `tl::All` (`src/tl_templates/cuda/common.h:846-863`, HIP equivalents at `src/tl_templates/hip/common.h:304-322`):

```cpp
template <typename T> TL_DEVICE bool Any(T *a, int size) {
  for (int i = 0; i < size; i++)
    if (a[i]) return true;
  return false;
}
```

Every thread scans the buffer serially and independently. Two costs:

- **Shared buffers:** all 32 lanes of a warp redundantly read all `size` elements — 32x redundant shared-memory traffic per warp, and the loop is O(size) per thread.
- **Fragments:** each thread reduces only its own local slice, so callers that want a tile-wide / warp-uniform answer still need a manual cross-thread combine (typically a shared-memory round-trip).

## Proposal

Use the warp vote intrinsics that #1858 already wired end-to-end (`tl.any_sync` / `tl.all_sync` → `__any_sync` / `__all_sync` on CUDA at `src/cuda/codegen/codegen_cuda.cc:4492`, `__any` / `__all` on HIP at `src/rocm/codegen/codegen_hip.cc:1589`):

**1. Shared/global buffers — cooperative warp-strided scan + one vote:**

```cpp
template <typename T> TL_DEVICE bool AnyWarp(T *a, int size, uint32_t mask = 0xffffffff) {
  bool local = false;
  for (int i = (threadIdx.x % 32); i < size; i += 32)
    local |= static_cast<bool>(a[i]);
  return __any_sync(mask, local);   // AllWarp: &= + __all_sync
}
```

Per-thread reads drop by the warp size (32x on CUDA, 64x on CDNA wavefronts), and the result is warp-uniform.

**2. Fragments — fold the warp with one vote:** keep the per-thread local scan, then `__any_sync` combines the 32 partials in a single instruction, replacing the shared-memory staging a tile-wide reduction needs today.

## Why this cannot be a blanket replacement

- **Convergence:** `__*_sync` requires every lane in the mask to reach the instruction. The current `tl::Any` is purely thread-local and is legal in divergent control flow (e.g. under `if (tid == 0)`); a vote at such a call site is UB on Volta+. The lowering must either prove the call site warp-uniform or keep the cooperative path opt-in.
- **Fragment semantics change** from "per-thread partial over the local slice" to "warp-uniform" — this must be a new variant, not an in-place swap.
- **Short-circuiting:** `all_of` currently early-exits on the first false; each lane can still break within its own stride, and a chunked ballot-based early exit can recover most of the rest.

## Suggested implementation plan

1. Add `tl::AnyWarp` / `tl::AllWarp` device templates to `src/tl_templates/cuda/common.h` and the HIP equivalents (`__any`/`__all`, wavefront-width stride) to `src/tl_templates/hip/common.h`.
2. First step (conservative): an explicit opt-in, e.g. `T.any_of(buf, scope="warp")`, that selects the cooperative lowering in the `FLowerIntrinsic` hooks in `src/op/logical.cc`, leaving convergence responsibility with the caller.
3. Follow-up: dispatch automatically when the buffer scope is shared and the call site is provably warp-uniform (outside thread-divergent control flow in the tile-op body).
4. Tests alongside the existing `testing/python/language/test_tilelang_language_any_of.py` / `test_tilelang_language_all_of.py`: numerical equivalence vs. the serial path for shared and fragment buffers on CUDA and HIP, plus a documented-constraint test for divergent call sites.


## 评论 (2)

### Dexterai · 2026-09-01

Hi @LeiWang1999 ，I'm new to tilelang and would like to tackle this issue. May I be assigned this?

### LeiWang1999 · 2026-09-01

assigned, thanks for your attention:)

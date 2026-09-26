# [Issue #2979] [BUG][Fuzzer][accepts-invalid] Region ops (`T.fill`/`T.clear`/`T.copy`) accept a sliced region whose `min+extent` exceeds the buffer, silently emitting an out-of-bounds write

source: https://github.com/tile-ai/tilelang/issues/2979
state: open | updated: 2026-09-06T14:34:53Z
labels: 

## 正文


### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the Issue Tracker that this hasn't already been reported.

### What version of TileLang are you using?

0.1.13 (reproduced on 0.1.13; source cited at the `v0.1.13` tag).

### System information

NVIDIA L40S (`sm_89`), CUDA 12.8, Python 3.13, tilelang 0.1.13. The defect is in the target-independent `Fill` op constructor bound check, so it is not specific to one GPU.

### Problem description

A sliced `T.fill` whose start offset plus length runs past the destination buffer — e.g. `T.fill(As[6:12], 7)` into a shape-`8` buffer — is silently accepted and lowered to an out-of-bounds store, even though the op's own contract says such input must be rejected. The `Fill` constructor's static bound check validates `min >= 0` and `extent <= shape` per dimension, but never checks `min + extent <= shape`, so a slice with a nonzero start slips through: `min = 6 >= 0` ✓ and `extent = 6 <= 8` ✓ both pass, while `min + extent = 12 > 8` is out of bounds.

The generated CUDA writes 4 elements past the end of the shared buffer:

<details><summary>Generated store (this session)</summary>

```cpp
// As is alloc_shared((8,), int32); the fill emits, for threadIdx.x in [0,6):
As[(((int)threadIdx.x) + 6)] = 7;      // writes indices 6..11 -> 8,9,10,11 are OOB
```

</details>

The nearest sibling — a pure-extent overflow `T.fill(As[0:12], 7)` (extent `12 > 8`) — **is** cleanly rejected by the very same check (`region[0] = 12 > 8`), which shows the guard exists and is meant to cover this; the min-offset case escapes it only because the start term is omitted.

### Reproducible example code

```python
import tilelang, tilelang.language as T

NBUF = 8

@T.prim_func
def main(B: T.Tensor((NBUF,), "int32")):
    with T.Kernel(1, threads=32):
        As = T.alloc_shared((NBUF,), "int32")
        T.fill(As[6:12], 7)        # min=6, extent=6 -> writes indices 6..11, 4 past shape 8
        T.copy(As, B)

tilelang.compile(main)             # SILENTLY ACCEPTED (compiles); emits As[tid+6]=7

# CONTROL A (rejected as it should be) — pure extent overflow, same buffer:
#   T.fill(As[0:12], 7)  ->  InternalError "region[0] = 12 > 8"
# CONTROL B (correctly accepted) — in-bounds slice:
#   T.fill(As[2:8], 7)   ->  compiles, fills exactly indices 2..7
```

### Traceback

```
No traceback — the kernel compiles and runs to completion; the fill silently
writes 4 elements (indices 8..11) past the end of the 8-element shared buffer.
```

### Expected behavior

An out-of-bounds fill region has no valid target — indices 8..11 are past the end of an 8-element buffer, so there is nothing legal to write there — and the op should reject it, exactly as its docstring promises ("checks that mins >= 0 and extents do not exceed the corresponding destination shape extents … will terminate (via ICHECK) if inputs are … out of bounds") and exactly as the pure-extent-overflow sibling already does. Instead it silently accepts and emits an out-of-bounds shared-memory store.

### Additional context

**Root cause.** The `Fill` operator's static bound check mis-analyzes a sliced fill region: it checks the start and the length independently (`min >= 0`, `extent <= shape`) but never their sum against the shape, so a slice whose start-plus-length exceeds the buffer is treated as in-bounds. The lowering then honors the nonzero start (`region[i]->min + var`) and emits the out-of-range store.

- The incomplete check: [`src/op/fill.cc#L111-L127`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/op/fill.cc#L111-L127) — `ICHECK_GE(min, 0)` and `ICHECK_LE(extent, shape)`, no `min + extent <= shape`.
- The min-offset store the missing check lets through: [`src/op/fill.cc#L164`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/op/fill.cc#L164) (`dst_indices.push_back(region[i]->min + var)`).
- The documented contract it violates: [`src/op/fill.cc#L78-L92`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/op/fill.cc#L78-L92).

**Suggested fix.** In the `Fill` constructor bound check (`src/op/fill.cc#L111-L127`), when both `region[i].min` and `region[i].extent` (and the shape) are statically known, add `ICHECK_LE(min + extent, shape)` alongside the existing checks, so a sliced fill past the end is rejected with the same actionable message the pure-extent case already produces.

**Same root, wider scope — the OOB-region check is per-op and inconsistent.** `Fill` is not the only region op that accepts an out-of-bounds sliced region; the bound check is implemented separately in each op rather than once at the slice/`BufferRegion` layer, so the ops disagree. Verified this session on 0.1.13 (dst slice `[6:12]` into a shape-8 buffer):

| op | check in source | OOB sliced region → | 
|---|---|---|
| `T.fill` | only `extent <= shape` (`fill.cc:122`, no `min` term) | accepted → emits `S[tid+6]=7` (writes 8..11) |
| `T.clear` | same `Fill` op (`fill_op.py:40`) | accepted (same path as fill) |
| `T.copy` | a `min + extent <= shape` expression exists but is **not** a bound guard (see below) | accepted → emits `Bs[tid+6]=Src[tid]`, runs and corrupts `B[7]` |

`fill`/`clear` lack the `min` term entirely. `copy` *appears* to have the right check — `min >= 0 && min + extent <= shape` at [`copy_analysis.cc:374`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/cuda/op/copy_analysis.cc#L374) — but that is `CanProveCopyInBounds`, whose only caller ([`copy_analysis.cc:656`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/cuda/op/copy_analysis.cc#L656)) uses it as an **optimization gate**: `layout_dependent_tma_available = has_layout_map && !is_cutedsl && CanProveCopyInBounds(...)`. When the region is *not* provably in bounds it returns false, which merely disables the TMA 1D fast path and falls back to the ordinary copy — it never rejects. So an OOB copy is not caught at all; it just takes the slow path and emits the out-of-bounds store. In other words no region op rejects an out-of-bounds sliced region — `fill`'s incomplete `extent <= shape` is the *only* actual reject check in the family, and even it misses the `min` term. Because there is no shared bound check, fixing `fill` alone leaves `copy`/`clear` writing out of bounds; a single bound check at the region-construction layer (where every op's slice is formed) would cover all of them. `T.fill` on a `fragment` is rejected here only incidentally — a layout check trips first, not a bound check.

**Provenance.** The `region.min + var` store offset and the extent-only bound check were both introduced by **#1189 (`a03df604`, "[Feature] Enhance fill operation to support various buffer types")** — #1189 added the nonzero-start slice support but wrote the guard as `extent <= shape` without the `min` term, so the sliced-fill OOB has never been caught (never-worked, not a regression). The file was later relocated (not re-introduced) by the `TileOperator`/backend refactors; the check is unchanged through `v0.1.13`. Reproduced at runtime on 0.1.13 this session: `T.fill(As[6:12],7)` into a shape-8 shared buffer silently compiles and emits `As[threadIdx.x + 6] = 7` (writes 8..11), while the pure-extent sibling `As[0:12]` is rejected (`extent 12 > shape 8`) and the in-bounds `As[2:8]` compiles.

**Dedup.** I searched the open and closed Issue Tracker and found no existing report of this bound-check defect; none names the omitted `min + extent` term in the sliced-fill bound check. It is distinct from #2942 (`T.fill` of a row-offset **fragment** sub-region silently fills the *wrong rows* — a non-injective layout-mapping miscompile, disposition compute-correctly), which is a different object (fragment vs shared), symptom (wrong data vs out-of-bounds write), and root (layout mapping vs the missing bound-check term). This one is the constructor bound check accepting an illegal out-of-bounds region.

**Reach.** Sliced `T.fill` (`T.fill(buf[a:b], v)`) is ordinary usage for initializing a sub-region of a tile. The trigger is any slice whose `start + length` exceeds the buffer — an easy off-by-one when a stride/offset is computed. No shipped example or test passes such a slice (they fill in-bounds), so CI stays green.

**Impact.** The trigger is narrow — it needs a statically-out-of-bounds *sliced* fill (nonzero start whose start+length exceeds the shape); a pure-extent overflow is already caught, and in-bounds slices are fine. But when it fires the consequence is severe: instead of a diagnostic it silently emits an out-of-bounds shared-memory store (a memory-safety / soundness gap), deterministic and past the buffer end, corrupting whatever aliases those slots — the kind of error the bound check exists to prevent.


## 评论 (1)

### KellyFrog · 2026-09-06

This will be rejected after PR #3091.

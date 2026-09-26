# [Issue #2942] [BUG][Fuzzer][wrong-code] `T.fill` of a row-offset fragment sub-region silently fills the wrong rows instead of the sliced region

source: https://github.com/tile-ai/tilelang/issues/2942
state: open | updated: 2026-08-26T10:14:52Z
labels: 

## 正文


### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) and [Discussions](https://github.com/tile-ai/tilelang/discussions) that this hasn't already been reported. (+1 or comment there if it has.)

### What version of TileLang are you using?

0.1.13 (latest release)

### System information

TileLang 0.1.13; CUDA 12.8, PyTorch 2.8; NVIDIA L40S (sm_89).

### Problem description

`T.fill(f[off:off+h, :], v)` on a `T.alloc_fragment` sub-region whose row offset `off` is **not** a multiple of the fragment's per-thread row atom silently fills the *wrong rows* — the kernel compiles and runs with no diagnostic. For a `(32, 64)` fragment (128 threads, row atom 8), `T.fill(f[3:11, :], 7.0)` writes rows `[0,1,2,3,4,13,14,15]` instead of `[3..10]`. Offsets that are multiples of the atom (`off=0`, `off=8`) fill the intended rows correctly, so the region is computable and the compiler mishandles only the misaligned offset.

The same misalignment can also abort compilation with `InternalError: Loop layout is not injective: Fragment(... forward_thread: (_i + 5) % 8 * 16 ...)` for some `(off, h)` (e.g. `off=5, h=10`); the silent-wrong-rows face and the ICE face are two manifestations of the same layout mis-map. Not a regression — wrong since the feature was added (see Provenance).

### Reproducible example code

```python
import tilelang, tilelang.language as T, torch

M, N = 32, 64

def build(off, h):
    @tilelang.jit(out_idx=[-1])
    def prog():
        @T.prim_func
        def main(A: T.Tensor((M, N), "float32"), C: T.Tensor((M, N), "float32")):
            with T.Kernel(1, threads=128) as _:
                f = T.alloc_fragment((M, N), "float32")
                T.copy(A, f)
                T.fill(f[off:off + h, :], 7.0)     # fill rows off..off+h of the fragment
                T.copy(f, C)
        return main
    return prog

torch.manual_seed(0)
a = torch.randn(M, N, device="cuda", dtype=torch.float32)

def check(off, h):
    ref = a.clone(); ref[off:off + h, :] = 7.0
    c = build(off, h)()(a); torch.cuda.synchronize()
    rows = [r for r in range(M) if (c[r] == 7.0).all()]
    print(f"off={off}: {'PASS' if torch.allclose(c, ref, atol=1e-4) else 'WRONG'} "
          f" filled rows {rows}  (wanted {list(range(off, off + h))})")

check(0, 8)   # aligned   -> PASS  filled rows [0..7]
check(8, 8)   # aligned   -> PASS  filled rows [8..15]
check(3, 8)   # unaligned -> WRONG filled rows [0,1,2,3,4,13,14,15]
```

Output (deterministic, TileLang 0.1.13, L40S sm_89):

```
off=0: PASS  filled rows [0, 1, 2, 3, 4, 5, 6, 7]      (wanted [0, 1, 2, 3, 4, 5, 6, 7])
off=8: PASS  filled rows [8, 9, 10, 11, 12, 13, 14, 15](wanted [8, 9, 10, 11, 12, 13, 14, 15])
off=3: WRONG filled rows [0, 1, 2, 3, 4, 13, 14, 15]   (wanted [3, 4, 5, 6, 7, 8, 9, 10])
```

### Traceback

No traceback — for the silent face the kernel compiles and runs to completion; the result is silently wrong and deterministic. (For some `(off, h)` the same mis-map instead throws `InternalError: Loop layout is not injective: Fragment(...)` at compile time.)

### Expected behavior

`T.fill(f[off:off+h, :], v)` should fill exactly rows `off..off+h`, matching the atom-aligned offsets `off=0` and `off=8` which already produce the correct rows over the same fragment. `T.fill`'s documented contract is to fill "a buffer or buffer region", and the aligned sibling offsets demonstrate the misaligned region is computable, so the natural expectation is that a misaligned offset fills the same intended rows (rather than silently writing different rows, or aborting with a non-injective-layout error).

### Additional context

**Root cause.** The fill loop applies the region's row offset to the store address but not to the thread→row layout, so the two disagree for any offset that isn't a whole multiple of the fragment's per-thread row atom. The fill loop is built in [`FillNode::MakeSIMTLoop`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/op/fill.cc#L156) with the store index `region[i]->min + var` ([fill.cc:164](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/op/fill.cc#L164)), `var` iterating the region extent `h`. The parallel lowering then derives the loop's fragment layout from the *destination buffer* (unshifted) via [`ComputeLoopLayoutFromBuffer`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/op/parallel.cc#L703) ([called at parallel.cc:487](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/op/parallel.cc#L487)) — so the offset ends up folded into the *thread selector* of a loop whose induction range is only `[0, h)`, instead of selecting the target rows. When `off` is a multiple of the row atom the shift is a whole number of thread groups and the mapping still lands right; otherwise threads land on the wrong physical rows (silent), or the map is non-injective and trips the [injectivity check](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/op/parallel.cc#L536) (the ICE face). Put differently: the forward layout splits a row into a slot component (`row // 8`) and a thread-group component (`row % 8`), but the fill inverts the offset back without that split — it pushes the whole `off` onto the slot selector and drops the `off % 8` part — so the recovered rows are wrong unless `off % 8 == 0`.

<details>
<summary>Generated CUDA for the <code>off=3</code> fill store, and the exact wrong rows it produces</summary>

The store the fill lowers to (0.1.13, this repro):

```cuda
float broadcast_var = 7.0f;
*(float4*)(f + (((((int)threadIdx.x) + 48) >> 7) * 4)) = make_float4(broadcast_var, ...);
```

The fragment layout (read off the surrounding `T.copy`, which lowers to `f[i] = A[i*512 + threadIdx.x*4]`) puts logical row `r` in **register slot `r // 8`**, thread group `(r % 8)` (16 threads per row, 4 columns each). So slot 0 holds rows 0–7, slot 1 holds rows 8–15.

The fill index `((threadIdx.x + 48) >> 7)` (where `48 = off*16 = 3*16`, and `>> 7` is `/128`) evaluates to **0 for threadIdx < 80** and **1 for threadIdx ≥ 80**, i.e. a *thread-dependent slot selector* rather than a per-row predicate:
- threads 0–79 write **slot 0** → rows `threadIdx//16` = rows **0,1,2,3,4**
- threads 80–127 write **slot 1** → rows `8 + threadIdx//16` = rows **13,14,15**

giving the observed `[0,1,2,3,4,13,14,15]`. A correct lowering would instead, per thread, test whether each of its slots maps to a logical row in `[off, off+h)` and write only those — rows 3–10 legitimately span slot 0 (rows 3–7) and slot 1 (rows 8–10). The aligned `off=8` case works precisely because `8*16 = 128` makes the selector the constant `1` (all threads → slot 1 → rows 8–15).
</details>

<details>
<summary>The mis-placement is in the fill's layout, not a dropped barrier (control with no preceding write)</summary>

Filling the offset region of a fragment that has no cross-thread write to synchronize against still lands in the wrong rows, so the cause is the fill loop's own layout, not a missing sync:

```python
@tilelang.jit(out_idx=[-1])
def frag():
    @T.prim_func
    def main(C: T.Tensor((32, 64), "float32")):
        with T.Kernel(1, threads=128) as _:
            f = T.alloc_fragment((32, 64), "float32")
            T.fill(f, 0.0)              # whole fragment, aligned -> correct
            T.fill(f[3:11, :], 7.0)     # offset sub-region
            T.copy(f, C)
    return main
# -> rows filled with 7.0: [0,1,2,3,4,13,14,15]  (wanted [3..10]); 512 sevens, all in wrong rows
```
</details>

**Suggested fix.** Invert the row offset the same way the forward layout builds it — split `region[i]->min` into its slot (`// 8`) and thread-group (`% 8`) components so the fill's layout counts rows from the same origin as the store (`fill.cc:164`), rather than folding the whole offset onto the slot selector. (I haven't built or verified a patch; a non-atom-aligned offset makes the target rows span two atom blocks, so this may be more than a one-line change.) Alternatively, if non-atom-aligned fragment fills aren't meant to be supported, the injectivity check at `parallel.cc:536` should reject them — it currently misses the silent-wrong-rows cases — rather than miscompiling.

**Provenance.** The offset line `region[i]->min + var` in `MakeSIMTLoop` was added in [#2166](https://github.com/tile-ai/tilelang/pull/2166) (merged 2026-05-12), which introduced sliced-region fill without a corresponding shift in the loop-layout derivation; the misalignment has been present since, no later than 0.1.9 (the earliest wheel I ran). No review bot flagged it on that PR.

**Dedup.** I searched the open and closed tracker and found no report of a fragment fill mis-mapping a row offset. [#2698](https://github.com/tile-ai/tilelang/issues/2698) is a distinct bug with a different root cause — a **shared**-buffer nonzero-offset fill whose `__syncthreads()` is dropped by `tl.ThreadSync` (a missing WAW barrier). This report is about a **fragment** fill whose layout partition itself mis-maps the offset, reproducing with no cross-thread hazard to synchronize (see the no-preceding-write control above).

**Reach.** The trigger is documented: `T.fill`'s docstring defines "a buffer or buffer **region**" as valid input, and slicing a fragment sub-region is the natural way to fill part of a tile. Sliced fills appear in `testing/`: `test_tilelang_issue_1008.py` fills `x[0:128]` and `x[a:b]`, and `test_tilelang_transform_plan_update_buffer_allocation_location.py` fills `x[a:b]` — but all of these fill a **global/argument** tensor (no thread-distributed fragment layout), and the static case starts at offset 0; none exercise a fragment sub-region at a non-atom-aligned offset, and the dynamic-region test only checks compilation, not the filled values. Given a fragment target, the boundary is concrete: with a `(32,64)` fragment at 128 threads the row atom is 8, so `off ∈ {0, 8, 16, 24}` fill correctly and every other row offset is wrong; the crashing vs silent face depends on the extent `h`.


## 评论 (1)

### KellyFrog · 2026-08-26

Hi!

Fragment buffer slicing is not supported by tilelang due to practical concerns. 
We are planning to refactor relevant codes so that they will be explicitly rejected.

This issue is therefore closed.

Best reguards.

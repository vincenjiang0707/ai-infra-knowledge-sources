# [Issue #3022] [BUG][Fuzzer][ice-on-valid-code] `T.reduce_*` on a sliced buffer crashes with a Python `AttributeError` — the input contract is undefined for a `BufferRegion`

source: https://github.com/tile-ai/tilelang/issues/3022
state: closed | updated: 2026-08-24T07:47:53Z
labels: 

## 正文


### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) and no similar issue has been filed.

### What version of TileLang are you using?

0.1.13

### System information

L40S (sm_89), CUDA 12.8, Python 3.13, TileLang 0.1.13. The failure is in the Python eager builder (frontend), so it is architecture-independent — it aborts before any codegen.

### Problem description

Passing a **slice** of a buffer to `T.reduce_sum` / `reduce_max` / `reduce_min` / etc. (e.g. `T.reduce_sum(a[0:64], out, dim=0)`) crashes the compiler with an uncaught Python `AttributeError: 'BufferRegion' object has no attribute 'shape'`, instead of either reducing the slice or reporting a clear error. Reducing the **whole** buffer over the same inputs compiles fine.

The reduce docstrings type the input as `tirx.Buffer` ("Input buffer to reduce") and say nothing about slices/regions, so the contract for a sliced input is undefined. But slicing a buffer is a first-class idiom in TileLang, and the sibling scan op `T.cumsum` *does* document and accept exactly this input — its docstring says ["Supports Buffer, BufferRegion, and BufferLoad inputs, allowing operations on buffer slices/regions"](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/language/scan_op.py#L84-L95) and it works on the same slice (see the example below). So a user reasonably expects `T.reduce_*` to accept a slice too; today it neither supports it nor rejects it cleanly.

Not a regression — see Provenance.

### Reproducible example code

```python
import tilelang
import tilelang.language as T


@tilelang.jit(out_idx=[1])              # CONTROL: reduce the whole fragment
def reduce_full(N=128):
    @T.prim_func
    def main(A: T.Tensor((N,), "float32"), B: T.Tensor((1,), "float32")):
        with T.Kernel(1, threads=N):
            a = T.alloc_fragment((N,), "float32")
            o = T.alloc_fragment((1,), "float32")
            T.copy(A, a)
            T.reduce_sum(a, o, dim=0)           # whole Buffer -> OK
            T.copy(o, B)
    return main


@tilelang.jit(out_idx=[1])              # BUG: reduce a slice (a BufferRegion)
def reduce_slice(N=128):
    @T.prim_func
    def main(A: T.Tensor((N,), "float32"), B: T.Tensor((1,), "float32")):
        with T.Kernel(1, threads=N):
            a = T.alloc_fragment((N,), "float32")
            o = T.alloc_fragment((1,), "float32")
            T.copy(A, a)
            T.reduce_sum(a[0:64], o, dim=0)    # slice -> BufferRegion -> crash
            T.copy(o, B)
    return main


for name, fn in [("control (whole buffer)", reduce_full),
                 ("slice   (a[0:64])     ", reduce_slice)]:
    try:
        fn(); print(f"{name}: compiles OK")
    except Exception as e:
        print(f"{name}: {type(e).__name__}: {e}")

# control (whole buffer): compiles OK
# slice   (a[0:64])     : AttributeError: 'BufferRegion' object has no attribute 'shape'
```

### Traceback

```
  File ".../tilelang/language/reduce_op.py", line 232, in reduce_sum
    reduce(buffer, out, "sum", dim, clear, batch=batch)
  File ".../tilelang/language/reduce_op.py", line 51, in reduce
    expected_shapes = [buffer.shape[:dim] + buffer.shape[dim + 1 :], buffer.shape[:dim] + [1] + buffer.shape[dim + 1 :]]
                       ^^^^^^^^^^^^
AttributeError: 'BufferRegion' object has no attribute 'shape'
```

### Expected behavior

`T.reduce_*` most plausibly should **accept a sliced input and reduce it**, matching the sibling `T.cumsum`, which already documents and supports `Buffer`/`BufferRegion`/`BufferLoad` and reduces the same slice correctly on 0.1.13. On that reading this is a valid input the compiler nearly handles already — the *output* side of the same function is already region-aware — so the fix is to route the input shape read through the same region-aware helper `cumsum` uses. If the maintainer instead intends sliced reduce to be out of scope, a clear frontend error naming the unsupported input would still be far better than the current uncaught `AttributeError` from deep inside the builder. The contract direction is the maintainer's to set; either way the present outcome — a raw Python attribute error and a dumped transpiler source — is the defect.

### Additional context

**Root cause.** `reduce()` reads `.shape` directly off its input argument, but a sliced input is a `BufferRegion`, which has no `.shape` — so the shape-validation line raises before the reduction is ever built. Concretely, [`reduce()`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/language/reduce_op.py#L24-L25) is typed `buffer: tirx.Buffer` and computes `expected_shapes` from [`buffer.shape[:dim] + buffer.shape[dim + 1:]`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/language/reduce_op.py#L51); when `buffer` is a `BufferRegion` (a slice like `a[0:64]`), `.shape` does not exist. `reduce_max`/`reduce_min` hit the same wall one step earlier for a negative `dim` via [`_legalize_dim`'s `len(buffer.shape)`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/language/reduce_op.py#L12-L14). The sibling `cumsum` avoids this by taking shapes through the region-aware helper [`retrieve_shape`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/utils/language.py#L233-L251) ([used at `cumsum` line 64](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/language/scan_op.py#L64)), which returns `[r.extent for r in region.region]` for a `BufferRegion`.

**Suggested fix.** The primary suggestion, given the `cumsum` precedent, is to **support the slice**: route the shape read through the same `retrieve_shape` helper `cumsum` uses (and drop the `.shape` access in `_legalize_dim` similarly), so a `BufferRegion` extent list is used for the shape check. If instead sliced reduce is meant to be out of scope, the alternative is an explicit type check at the top of `reduce()` that raises a clear error naming the input. Which direction is right is the maintainer's contract call; both replace the current uncaught `AttributeError`.

**Class tested (this session, 0.1.13, L40S/A10G).** Two-level root: **(a) source-level** — `reduce()` and its helper `_legalize_dim` in `tilelang/language/reduce_op.py` read shape off the *input* argument directly (`buffer.shape` at [L51](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/language/reduce_op.py#L51), `len(buffer.shape)` at [L14](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/language/reduce_op.py#L12-L14)) instead of routing it through the region-aware `retrieve_shape` helper the sibling `cumsum` uses; the *output* argument in the same function IS routed through a region-aware read ([`to_buffer_region(out).buffer` at L47](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/language/reduce_op.py#L47)), so the fragility is input-side only. **(b) operator-level** — the whole `T.reduce_*` family (`sum`/`max`/`min`/`abssum`/`absmax`/`bitand`/`bitor`/`bitxor`), which all funnel through the one `reduce()`/`_legalize_dim` pair.

<details>
<summary>4-axis generalization sweep (each cell run on 0.1.13, observed result recorded — not asserted)</summary>

| axis | cell tested | observed result | same root? |
|---|---|---|---|
| (op family) | `reduce_sum(a[0:64], o, dim=0)` | `AttributeError: 'BufferRegion' object has no attribute 'shape'` @ `reduce_op.py:51` | yes |
| related-operator | `reduce_max` / `reduce_min` / `reduce_abssum` / `reduce_absmax` `(a[0:64], o, dim=0)` | same `AttributeError` @ `reduce_op.py:51` | yes |
| related-operator + related-type | `reduce_bitxor(a[0:64], o, dim=0)`, `int32` | same `AttributeError` @ `reduce_op.py:51` | yes |
| similar-logic | `reduce_max(a[0:64], o, dim=-1)` — negative dim | same `AttributeError`, one step earlier @ `_legalize_dim` (`reduce_op.py:14`, `len(buffer.shape)`) | yes (2nd site) |
| related-source | `reduce_sum(a, o[0:4], dim=0)` — whole input, **sliced output** | clean `ValueError` @ `reduce_op.py:54` (no crash; out routed through `to_buffer_region`) | **no — out-side is region-aware** |
| related-type (dtype control) | `reduce_bitxor(a, o, dim=0)`, `int32` whole buffer | compiles OK | control (dtype not the cause) |
| (input-shape control) | `reduce_sum(a, o, dim=0)` — whole `Buffer` | compiles OK | control |
| related-operator (sibling scan) | `cumsum(a[0:64], o[0:64], dim=0)` — same slice | **compiles OK** (documented to accept `BufferRegion`) | control (sibling handles it) |

The defect is the sliced (`BufferRegion`) *input* reaching a `Buffer`-only shape read: shared across the entire `reduce_*` family and across both the `dim>=0` (`reduce_op.py:51`) and negative-`dim` (`_legalize_dim`, `reduce_op.py:14`) sites, and dtype-independent (int32 slice crashes identically, int32 whole buffer is fine). It is NOT shared by the output argument (region-aware via `to_buffer_region`) — the sliced-output cell gave a clean `ValueError`, isolating the fragility to the input-side read. The region-aware sibling `cumsum` accepts the same slice, confirming the intended-idiom framing.

</details>

**Provenance.** The `expected_shapes = [buffer.shape[...]]` read at `reduce_op.py:51` — the crash on the `dim >= 0` path — was added by [#748 "Add shape checking for reduce options"](https://github.com/tile-ai/tilelang/pull/748) (merged 2025-08-24). The `len(buffer.shape)` read in `_legalize_dim` predates #748, so the negative-`dim` variant of the crash is older; both are region-unaware for the same reason. The file was later moved from `tilelang/language/reduce.py` to `reduce_op.py` and the `cumsum` scan op split out into `scan_op.py`. Not a regression either way — no version accepted a sliced reduce input.

**Related.** Same family, different sites, both closed: [#2550](https://github.com/tile-ai/tilelang/issues/2550) (`T.atomic_addx4` reads `.dtype` off a sliced destination) and [#2631](https://github.com/tile-ai/tilelang/issues/2631) (`increase_descriptor_offset` reads `.shape` off a `BufferLoad`). Those were the eager builder reading a `Buffer`-only attribute off a `BufferRegion`/`BufferLoad`; this is the same shape but in `reduce()`, and it is not fixed.

**Dedup.** I searched the open and closed tracker and found no existing report of the reduce case; the related-family issues (#2550, #2631) are different sites and both already closed.

**Reach.** Triggering requires passing a *slice* (a `BufferRegion`) as the reduce input. I audited the shipped `T.reduce_*` call sites in `examples/` (flash-attn, layernorm, rms_norm, the fp8-cast kernels, the sparse-MLA kernels): every one passes a *whole* fragment buffer (`acc_s`, `A_local`, `y_local`, …), never a slice — so none trip this and CI stays green; there is no test exercising a sliced reduce input. To make the "dodges by whole-buffer input" point concrete I ran the shipped `examples/norm/rms_norm.py` verbatim on 0.1.13 (A10G): it prints `All checks pass.` — its two `T.reduce_sum(A_pow_local, A_powsum, dim=1)` calls take whole buffers, so it compiles and matches the torch reference. Slicing itself is common, and the sibling `T.cumsum` explicitly documents slice input — and I confirmed on 0.1.13 that `T.cumsum(a[0:64], o[0:64], dim=0)` compiles fine while the identical reduce slice crashes — so a user moving between the two ops hits this immediately. The failure is a hard compile-time abort (a raw `AttributeError` from the eager builder) — it corrupts no data and cannot slip into a running workload; it just fails loudly on that kernel build.

## 评论 (1)

### KellyFrog · 2026-08-24

Hi!

After some discussion, we decided that it would be inappropriate for tilelang to accept fragment slicing due to our replication design.

According to current design, if not specified by hand, each appearing fragment should be distributed equially in all threads, sometimes involving replication. Accepting fragment slicing would bring unnecessary complexity to the current layout system.

In your case, it is recommended to use reducer buffer with `T.alloc_reducer` and `T.Parallel` instead.

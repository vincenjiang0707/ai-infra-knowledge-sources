# [Issue #2906] [BUG] `makeBufferWithLayout` segfaults on a symbolic shared-buffer extent instead of hitting its own `ICHECK`

source: https://github.com/tile-ai/tilelang/issues/2906
state: closed | updated: 2026-09-20T00:03:40Z
labels: 

## 正文


**Version:** v0.1.11 (`VERSION` = 0.1.11), commit `607a9144cf375e1176ad487dd5b0e3d87c2cb79a`
**Platform:** Linux, CUDA 13.0, NVIDIA RTX 4000 Ada Generation (sm_89), Python 3.10, torch 2.12.1+cu130
**Still present on `main`:** the two loops below are unchanged as of `af4753045895`
(source inspected; the reproduction itself was run on `607a9144`).

## Summary

`makeBufferWithLayout` in `src/transform/lower_tile_op.cc` dereferences the result of
`.as<IntImmNode>()` without a null check when computing a shared buffer's replication
factor. A symbolic (non-constant) extent therefore crashes the compiler with SIGSEGV.

The loop immediately after it guards the identical condition with an `ICHECK`, so the
crash appears to be an oversight rather than intended behaviour — the diagnostic that was
written for this case can never fire, because the unguarded loop runs first.

## Location

`src/transform/lower_tile_op.cc`, inside `if (IsSharedBuffer(buffer))`:

```cpp
Array<PrimExpr> buffer_shape = buffer->shape;
int buffer_extent = 1;
int layout_extent = 1;
for (size_t i = 0; i < buffer_shape.size(); i++) {
  auto shape = buffer_shape[i].as<IntImmNode>();
  buffer_extent *= shape->value;                     // <-- no null check
}
for (size_t i = 0; i < layout_shape.size(); i++) {
  auto shape = layout_shape[i].as<IntImmNode>();
  ICHECK(shape) << "Layout output shape must be constant integer, but got: "
                << layout_shape[i];                  // <-- guarded
  layout_extent *= shape->value;
}
```

If `buffer_shape[i]` is not an `IntImmNode`, `.as<IntImmNode>()` returns `nullptr` and
`shape->value` dereferences it.

## Reproduction

Run this **from a file**, not `python -c` — TVMScript's `@T.prim_func` parser calls
`inspect.getsourcelines`, which has no source under `-c`, so the parser fails first and the
crash never surfaces.

```python
import tilelang
import tilelang.language as T
from tilelang.layout import Layout

m = T.dynamic("m", "int32")
N = 256

@tilelang.jit(out_idx=[1])
def build():
    @T.prim_func
    def k(A: T.Tensor((m, N), "float16"), B: T.Tensor((m, N), "float16")):
        with T.Kernel(1, threads=128) as bx:
            s = T.alloc_shared([m, N], "float16")
            # element counts match, so the layout.cc:678 product check passes and
            # execution reaches makeBufferWithLayout with a symbolic shape
            T.annotate_layout({s: Layout([m, N], lambda i, j: [i, j])})
            T.copy(A[0:m, :], s)
            T.copy(s, B[0:m, :])
    return k

build()
```

**Actual:** process dies with SIGSEGV (exit `-11`), no diagnostic.

**Expected:** the existing message, i.e.
`Layout output shape must be constant integer, but got: m`

## Notes

A dynamic shared extent *without* an explicit layout annotation compiles fine — that path
never reaches `makeBufferWithLayout`, so the bug only surfaces when a layout annotation
forces the buffer through the remap path.

`T.dynamic("m", "int32")` and `T.symbolic("m")` behave identically here — both segfault with
the same stack. That is expected from `tilelang/language/symbolics.py`, where `symbolic` is a
`@deprecated(..., "v0.1.9")` alias that calls `dynamic(name, dtype)` and returns the same
`tirx.Var`. The reproduction uses `T.dynamic` as the non-deprecated spelling.

## Suggested fix

Guard the first loop the same way as the second, and report which buffer failed:

```cpp
for (size_t i = 0; i < buffer_shape.size(); i++) {
  auto shape = buffer_shape[i].as<IntImmNode>();
  ICHECK(shape) << "Shared buffer '" << buffer->name
                << "' extent must be a constant integer, but got: " << buffer_shape[i];
  buffer_extent *= shape->value;
}
```

Happy to send a PR if that shape looks right.


## 评论 (2)

### sohampanda000 · 2026-08-06

Updated the reproduction to use `T.dynamic("m", "int32")` instead of the deprecated `T.symbolic("m")`, in case the choice of spelling looked relevant.

It is not — both segfault identically, same stack, top frame `tvm::tl::makeBufferWithLayout` via `LowerTileOpPass::VisitStmt_`:

```
T.symbolic("m")          -> rc -11 (SIGSEGV)
T.dynamic("m", "int32")  -> rc -11 (SIGSEGV)
```

Which is what `tilelang/language/symbolics.py` implies — `symbolic` is a `@deprecated(..., "v0.1.9")` alias that calls `dynamic(name, dtype)` and returns the same `tirx.Var`.

Also added a note that the reproduction must be run **from a file**: under `python -c`, TVMScript's `@T.prim_func` parser has no source for `inspect.getsourcelines` and fails before reaching the compiler, which looks like the bug is absent.

### sohampanda000 · 2026-08-06

Narrowing this down further, since the trigger turns out to be tighter than the original report implies.

## The trigger is one cell of a 2x2

Every case below uses `m = T.dynamic("m")` in the global tensors. The only variables are whether the **shared** buffer's extent is a compile-time constant, and whether it carries a layout annotation. Each case that builds is also executed at `m=64` and its output compared against the input, not just compiled:

| shared extent | `annotate_layout` | result |
|---|---|---|
| `(BM, N)` static | yes | builds + runs correctly |
| `(BM, N)` static | no | builds + runs correctly |
| `(m, N)` symbolic | no | **builds + runs correctly** |
| `(m, N)` symbolic | **yes** | **SIGSEGV in `makeBufferWithLayout`** |

So this is not about dynamic shapes in general, and not about layouts in general. It needs **both**: a layout annotation over a shared buffer whose extent is not a compile-time constant.

## A symbolic shared extent on its own is fully supported

Worth stating explicitly, because it bears on what the right fix is. With no layout annotation, `T.alloc_shared((m, N), ...)` lowers to CUDA dynamic shared memory and works:

```cuda
extern "C" __global__ void k_kernel(const half_t* __restrict__ A, half_t* __restrict__ B, int m);
extern __shared__ __align__(1024) half_t s[];
for (int i = 0; i < ((((m - 1) >> 2) * 8) + 8); ++i) {
  if ((((i >> 3) * 4) + (((int)threadIdx.x) >> 5)) < m) { ... }
```

Executed at `m=64`, the output matches the input exactly.

## Which suggests the fix is a rejection, not support

My original "Suggested fix" was an `ICHECK` mirroring the guarded loop below it. That still looks right, but for a more specific reason than the report gives: the problem is not that dynamic shared buffers are unsupported — they demonstrably are supported — it is that a **layout cannot be expressed over a non-constant extent**. `replicate_extent = buffer_extent / layout_extent` needs both as integers, and an index map needs a known extent to be well-defined.

That reading seems consistent with #2719, which added the pigeonhole check a few lines above and scoped itself to "a shared buffer whose layout **has static shapes**". The symbolic case appears to fall outside that scope rather than having been considered and allowed.

If that is right, the fix is to reject the combination with a message naming the buffer and the non-constant extent, rather than to attempt symbolic replication.

## Reproduction note

Run the reproduction **from a file**, not `python -c` — TVMScript's `@T.prim_func` parser calls `inspect.getsourcelines`, which has no source under `-c`, so parsing fails before the compiler is reached and the crash appears to be absent.


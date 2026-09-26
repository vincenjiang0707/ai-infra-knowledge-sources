# [Issue #3564] [BUG] CuTe DSL: _merge_gpu_link_libraries emits link-libraries in Python set order, so the compile pipeline string varies per process

source: https://github.com/NVIDIA/cutlass/issues/3564
state: closed | updated: 2026-09-22T06:38:39Z
labels: CuTe DSL

## 正文

## Describe the bug

`DSL._merge_gpu_link_libraries` collects each `gpu.module`'s `link-libraries` attribute into a Python `set` and joins it unsorted into the `LinkLibraries` compile option (`python/CuTeDSL/cutlass/base_dsl/dsl.py:2127-2134`, `main` @ dc45f97):

```python
sources = set(
    x.value for x in gpu_module.attributes.get("link-libraries", set())
)
link_libraries = (
    link_libraries
    + ("," if link_libraries and len(sources) > 0 else "")
    + ",".join(sources)          # <- set iteration order
)
```

Iteration order of a `set` of strings depends on `PYTHONHASHSEED`, which is randomized per process. Whenever a program links two or more bitcode libraries (one `link-libraries` entry is added per extern bitcode source, `ffi.py:603-611`), the rendered pipeline token `link-libraries='...'` (`StringCompileOption.serialize`, `compiler.py:413-416`) differs from process to process for the same program.

The attribute's writer already establishes a canonical order: `ffi.py:609-611` writes the ArrayAttr **sorted**. The `set()` in `_merge_gpu_link_libraries` then discards that order (and adds no dedup that `ffi.py` has not already done), so the sortedness maintained on the attribute never reaches the compiler invocation.

Order demonstration (pure CPython semantics, no GPU needed):

```console
$ for s in 0 1 2 3; do PYTHONHASHSEED=$s python -c "print(','.join(set(['/opt/libdevice.10.bc','/opt/libuser_ops.bc','/opt/libmath_ext.bc'])))"; done
/opt/libuser_ops.bc,/opt/libdevice.10.bc,/opt/libmath_ext.bc
/opt/libdevice.10.bc,/opt/libmath_ext.bc,/opt/libuser_ops.bc
/opt/libuser_ops.bc,/opt/libmath_ext.bc,/opt/libdevice.10.bc
/opt/libuser_ops.bc,/opt/libmath_ext.bc,/opt/libdevice.10.bc
```

## Why it matters

- The effective compiler invocation is not reproducible across processes for the same source, so byte-identical rebuilds cannot be relied on, and any consumer that records or hashes the effective pipeline string sees spurious per-process variation.
- Link order is semantically load-bearing in the usual first-definition-wins model: if two linked bitcode libraries ever provide the same symbol, which definition wins becomes a per-process choice. I have not identified a shipped pair that conflicts, so with today's inputs the practical effect may be limited to non-reproducible builds; filing accordingly rather than as a correctness bug.
- Process-scoped compile nondeterminism is a failure signature that is costly to debug downstream (for one open example of the class, flashinfer-ai/flashinfer#4704: a CuTe-DSL kernel's tests flip between all-pass and all-fail only across processes). I am not claiming this site explains that report; it is one confirmed instance of the class in the frontend.

## Expected behavior

The pipeline string for a fixed program should not depend on `PYTHONHASHSEED`:

```python
+ ",".join(sorted(sources))
```

mirroring `ffi.py:610`, or iterate the already-sorted ArrayAttr directly instead of re-wrapping it in a set.

## Environment / verification

- All line references verified against NVIDIA/cutlass `main` @ dc45f97 (`python/CuTeDSL` frontend source).
- Not executed against the installed `nvidia-cutlass-dsl` wheel: the order-dependence follows from CPython set semantics and the code path above; I could not run the DSL end-to-end here (no CUDA device).


## 评论 (2)

### migarci2 · 2026-08-28

I'd like to work on this. I'll preserve the canonical order from the ArrayAttr and add a focused regression test for multiple link libraries.

### brandon-yujie-sun · 2026-09-22

For record, this is fixed in 4.8

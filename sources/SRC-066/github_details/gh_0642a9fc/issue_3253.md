# [Issue #3253] [BUG] CuTe Python DSL: cute.coalesce(cute.prepend(...)) corrupts memory for complement layout

source: https://github.com/NVIDIA/cutlass/issues/3253
state: open | updated: 2026-09-17T08:21:44Z
labels: bug, ? - Needs Triage, inactive-30d, inactive-90d, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

The CuTe Python DSL can hit native memory corruption when `cute.coalesce()` is applied to a layout produced by `cute.prepend()` using a complement layout.

Minimal example:

```python
x_ori = cute.make_layout((6,), stride=(4,))  # (6):(4)
x = cute.complement(x_ori, 24)              # 4:1
combined = cute.prepend(x_ori, x)           # (4,6):(1,4)
coalesced = cute.coalesce(combined)         # expected 24:1
print(cute.pretty_str(coalesced))           # crashes
```

Expected result:

```text
24:1
```

Actual result:

```text
malloc(): unaligned tcache chunk detected
```

## Environment

```text
OS: Linux-6.8.0-100-generic-x86_64-with-glibc2.39
Python: 3.12.13 | packaged by Anaconda, Inc. | GCC 14.3.0
Python executable: /home/tongyu/miniconda3/envs/wty_py312/bin/python
cutlass.__version__: unknown
cutlass module path: /home/tongyu/miniconda3/envs/wty_py312/lib/python3.12/site-packages/nvidia_cutlass_dsl/python_packages/cutlass/__init__.py
nvidia-cutlass-dsl: 4.3.5
nvidia-cutlass-dsl-libs-base: 4.4.1
nvidia-cutlass-dsl-libs-cu13: 4.4.1
```

Relevant installed packages:

```text
cuda-bindings                13.2.0
cuda-pathfinder              1.5.4
cuda-python                  13.2.0
cuda-tile                    1.1.0
nvidia-cutlass-dsl           4.3.5
nvidia-cutlass-dsl-libs-base 4.4.1
nvidia-cutlass-dsl-libs-cu13 4.4.1
```

## Reproduction

Save as `repro_cute_coalesce_prepend.py`:

```python
import cutlass
import cutlass.cute as cute
from cutlass._mlir import ir

print('python repro start', flush=True)
print('cutlass version:', getattr(cutlass, '__version__', 'unknown'), flush=True)

with ir.Context():
    x_ori = cute.make_layout((6,), stride=(4,))
    x = cute.complement(x_ori, 24)
    print('x_ori =', cute.pretty_str(x_ori), flush=True)
    print('x =', cute.pretty_str(x), flush=True)

    combined = cute.prepend(x_ori, x)
    print('combined =', cute.pretty_str(combined), flush=True)

    coalesced = cute.coalesce(combined)
    print('coalesced repr =', repr(coalesced), flush=True)

    # Expected: 24:1
    # Actual: malloc/tcache corruption before or during this print.
    print('coalesced pretty =', cute.pretty_str(coalesced), flush=True)
```

Run:

```bash
python repro_cute_coalesce_prepend.py
```

Observed output:

```text
python repro start
cutlass version: unknown
x_ori = (6):(4)
x = 4:1
combined = (4,6):(1,4)
coalesced repr = <cutlass.cute.core._Layout object at 0x...>
malloc(): unaligned tcache chunk detected
```

## Expected behavior

`cute.prepend(x_ori, x)` pretty-prints as:

```text
(4,6):(1,4)
```

This layout is contiguous in column-major order, so `cute.coalesce()` should return:

```text
24:1
```

Equivalent construction through `cute.make_layout()` works conceptually:

```python
with ir.Context():
    y = cute.make_layout((4, 6), stride=(1, 4))
    z = cute.coalesce(y)
    print(cute.pretty_str(z))  # 24:1
```

## Actual behavior

`cute.coalesce()` returns a `_Layout` object, but `cute.pretty_str()` on that object triggers native memory corruption:

```text
malloc(): unaligned tcache chunk detected
```

In some local runs, similar tcache/double-linked-list corruption also occurred around related layout objects after `complement()`/attribute access, suggesting a lifetime/ownership issue in the Python binding or underlying MLIR object wrapper.

## Notes / suspected cause

This looks like a native lifetime or ownership bug rather than a Python exception-level issue:

- No Python traceback is produced.
- The process aborts with glibc allocator corruption.
- The same logical layout can be represented as `(4,6):(1,4)` and should coalesce to `24:1`.
- The crash is tied to layouts produced via `cute.prepend()`/`cute.complement()` and then passed to `cute.coalesce()`.

## 评论 (2)

### github-actions[bot] · 2026-06-19

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-09-17

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

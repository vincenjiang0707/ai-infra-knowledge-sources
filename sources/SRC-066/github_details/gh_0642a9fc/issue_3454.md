# [Issue #3454] [BUG] cute.slice_ SIGABRTs on a static swizzled ComposedLayout

source: https://github.com/NVIDIA/cutlass/issues/3454
state: open | updated: 2026-09-12T08:17:22Z
labels: bug, ? - Needs Triage, inactive-30d, CuTe DSL

## 正文

**Describe the bug**

`cute.slice_` native-aborts on a fully static swizzled `ComposedLayout`. No Python exception, no MLIR diagnostic. Compiler crash, not a kernel failure.

Not the same as #3255 (that one is `tensor[…]` with dynamic `?` strides).

**Steps/Code to reproduce bug**

```python
import cutlass.cute as cute

@cute.jit
def repro():
    layout = cute.make_composed_layout(
        cute.make_swizzle(3, 4, 3),
        0,
        cute.make_layout((10, 2), stride=(2, 1)),
    )
    print(layout, flush=True)
    cute.slice_(layout, (None, 0))

if __name__ == "__main__":
    cute.compile(repro)
```

```
S<3,4,3> o 0 o (10,2):(2,1)
Aborted (core dumped)
```

Same slice succeeds if the first mode is 8 instead of 10. `cute.select(layout, [0])` on this layout also succeeds.

**Expected behavior**

Return a sliced layout, or raise a Python/MLIR error. Should not `abort()`.

**Environment details**

- Bare-metal, NVIDIA H20 (sm_90), driver 535.183.06, Linux x86_64
- Python 3.13.14, CUDA 13.0
- `nvidia-cutlass-dsl == 4.6.1` and `4.7.0` (both abort on this repro)

**Additional context**

Python stack ends in `SliceOp.__init__` (`cute.slice` MLIR op). `_cutlass_ir*.so` is stripped, so there is no usable C++ backtrace.


## 评论 (1)

### github-actions[bot] · 2026-09-12

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

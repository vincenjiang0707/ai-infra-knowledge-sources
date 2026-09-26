# [Issue #3478] [BUG] pycute: logical_product with an integer tiler computes logical_divide

source: https://github.com/NVIDIA/cutlass/issues/3478
state: open | updated: 2026-09-20T00:45:00Z
labels: inactive-30d

## 正文

**Describe the bug**

In `python/pycute/layout.py`, `logical_product` dispatches an integer tiler to `logical_divide`, so it returns a divide result under a product name. The `Layout`-wrapped form is unaffected, so the two spellings of the same call disagree.

`python/pycute/layout.py:312-316`:

```python
def logical_product(layoutA, layoutB):
  if layoutB is None:
    return layoutA
  elif is_int(layoutB):
    return logical_divide(layoutA, Layout(layoutB))   # <-- should be logical_product
```

The identical line at `python/pycute/layout.py:301` is correct: it belongs to `logical_divide` directly above.

The C++ reference does the right thing at `include/cute/layout.hpp:1670`:

```cpp
} else if constexpr (is_integral<Tiler>::value) {
    return logical_product(block, make_layout(tiler));
}
```

**Steps/Code to reproduce bug**

```
cd python
python -c "
from pycute import *
A = Layout((2,5),(5,1))
print('product Layout(4):', logical_product(A, Layout(4)))
print('product int 4    :', logical_product(A, 4))
print('divide  int 4    :', logical_divide(A, 4))
"
```

Output:

```
product Layout(4): ((2, 5), 4):((5, 1), 10)     <- correct, matches C++
product int 4    : ((2, 2), 3):((5, 1), 2)      <- wrong
divide  int 4    : ((2, 2), 3):((5, 1), 2)      <- identical to the line above
```

The size is the clearest tell: `size(A)` is 10, the product should be 40, and the returned layout has size 12.

**Expected behavior**

`logical_product(A, 4)` should equal `logical_product(A, Layout(4))`.

**Scope**

Everything reaching the integer branch is affected:

| Call | Affected |
|---|---|
| `logical_product(A, 4)` | yes |
| `logical_product(A, (4,2))` | yes, the tuple branch recurses per mode into the int branch |
| `zipped_product(A, 4)` | yes, `hier_unzip(logical_product, ...)` bottoms out there |
| `tiled_product(A, 4)` | yes, built on `zipped_product` |
| `logical_product(A, Layout(4))` | no |

`operators/cutlass/operators/fusion/pycute/layout.py:339` is a copy of the same file and has the same line.

There is currently no test for `logical_product` or `logical_divide` in `test/python/pycute/`.

**Environment details**

- Environment location: Bare-metal
- Pure Python, no GPU, CUDA or build needed
- Reproduced on `main` at the time of filing

**Additional context**

Note this is `python/pycute`, the Python reference implementation, not the CuTe DSL. The issue-form dropdown has no option for it.

I have a fix and a regression test ready and will open a PR referencing this issue.


## 评论 (2)

### ccecka · 2026-08-20

The outdated NVIDIA/cutlass version of pycute needs to be removed and pointed to the complete and supported PyCuTe here
https://github.com/NVlabs/CuTe

### github-actions[bot] · 2026-09-20

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

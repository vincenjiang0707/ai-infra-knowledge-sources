# [Issue #3513] zipped/tiled divide with a dynamic tiler skips divisibility checks on static layouts and returns a non-size-preserving layout

source: https://github.com/NVIDIA/cutlass/issues/3513
state: open | updated: 2026-09-13T03:55:29Z
labels: CUTLASS C++

## 正文

### Description

When a zipped/tiled divide receives a *dynamic* tiler against a *fully static* layout, the divisibility requirement is checked nowhere, and the result is a silently non-size-preserving layout.

```cpp
#include "cute/layout.hpp"
#include <iostream>
int main() {
    using namespace cute;
    auto L = make_layout(make_shape(_12{}, make_shape(_4{}, _8{})),
                         make_stride(_7{}, make_stride(_1{}, C<30>{})));
    auto d = zipped_divide(L, 128);   // 128 does not divide size(L) == 384
    print(d);
    print(" size="); print(size(d));   // 288
}
```

Actual output:

```
((12,4,2),(1,1,3)):((_7,_1,_30),(896,11,90))
 size=288
```

`size(d) == 288 != size(L) == 384`, strides run past the layout's cosize (896), and no diagnostic of any kind fires. Each individual configuration is handled correctly on its own:

- fully static tiler: compile-time `static_assert` fires ("Shape Divisibility Condition"),
- fully dynamic operands: the runtime assert catches it,
- mixed static layout / dynamic tiler: the static path's runtime check is compiled out (the shapes are static, so the dynamic assert sees nothing to test) and the static check cannot see the dynamic tiler, so every guard is skipped.

The Python port asserts on the same input, which highlights the gap when cross-checking.

### Suggested fix

In the mixed case, emit a runtime divisibility check (or a `CUTE_GCC_UNREACHABLE`-style guarded assert) comparing the dynamic tiler size against the known static layout size before performing the division, so misuses fail loudly instead of producing layouts whose size differs from the input.


## 评论 (1)

### XFDG · 2026-09-13

Hi, I've submitted a fix in https://github.com/NVIDIA/cutlass/pull/3622.

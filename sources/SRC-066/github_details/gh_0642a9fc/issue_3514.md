# [Issue #3514] zip2_by does not handle Underscore tiler entries: kept modes are silently split or fail to compile

source: https://github.com/NVIDIA/cutlass/issues/3514
state: open | updated: 2026-09-13T04:31:49Z
labels: CUTLASS C++

## 正文

### Description

`zip2_by` (include/cute/algorithm/tuple_algorithms.hpp ~lines 1031-1056), which underpins `zipped_divide` / `tiled_divide` / `zipped_product` / `tiled_product`, has no handling for `Underscore` tiler entries. Two failure modes result when an `_` appears in a tuple tiler and the corresponding kept profile mode is not rank-1:

1. **Kept mode of rank >= 2: silently wrong grouping.** The rank-2 mode is misread as a divide pair: its first submode is placed in the BLOCK group and its second in the REST group, instead of the whole mode being kept undivided.

2. **Kept scalar mode: compile error** (`zip2_by` "Mismatched ranks" / incomplete `tuple_size<C<...>>`).

Repro for case 1:

```cpp
#include "cute/layout.hpp"
#include <iostream>
int main() {
    using namespace cute;
    auto L = make_layout(make_shape(_12{}, make_shape(_4{}, _8{})),
                         make_stride(_7{}, make_stride(_1{}, C<30>{})));
    auto d = zipped_divide(L, make_tuple(_2{}, Underscore{}));
    print(d);
}
```

Actual output:

```
((_2,_4),(_6,_8)):((_7,_1),(_14,_30))
```

The kept profile mode `(4,8)` was split across the two groups (`_4` into the block group, `_8` into the rest group). The documented meaning of `_` ("keep this mode out of the division") would keep `(4,8)` together on the rest side. Size happens to be preserved, so nothing downstream notices - this produces layouts that are valid-looking but semantically wrong.

For contrast, the Python port treats a None tiler entry as a no-op correctly and computes `((2,1),(6,(4,8))):((7,0),(14,(1,30)))` for the same input.

### Suggested fix

Teach `zip2_by` (and its product-side counterpart) to pass Underscore entries through as "keep whole": place the entire kept mode in the REST group with an identity block entry, mirroring what the logical-divide level already does for `_`.


## 评论 (1)

### XFDG · 2026-09-13

Hi, I've submitted a fix in https://github.com/NVIDIA/cutlass/pull/3626.

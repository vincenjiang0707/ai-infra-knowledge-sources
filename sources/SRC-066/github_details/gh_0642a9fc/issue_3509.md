# [Issue #3509] LinearCombinationClamp with float output does not compile: platform numeric_limits<float> has no lowest()

source: https://github.com/NVIDIA/cutlass/issues/3509
state: open | updated: 2026-09-13T03:43:02Z
labels: CUTLASS C++

## 正文

### Description

`cutlass::platform::numeric_limits<float>` (include/cutlass/platform/platform.h ~lines 909-916) defines only `infinity()`, `max()`, `is_integer` and `has_infinity`. It has no `lowest()`.

`LinearCombinationClamp`'s primary template calls `numeric_limits<ElementOutput>::lowest()` unconditionally in both `operator()` overloads (include/cutlass/epilogue/thread/linear_combination_clamp.h lines ~225 and ~266), and its documentation accepts float output. Instantiating the clamp epilogue with float output is therefore a hard compile error:

```cpp
#include "cutlass/epilogue/thread/linear_combination_clamp.h"
using Op = cutlass::epilogue::thread::LinearCombinationClamp<float, 1, float, float>;
Op::Params p(1.0f, 0.0f);
Op op(p);
cutlass::Array<float,1> out, acc{{2.0f}};
int main(){ op(out, acc); }
```

nvcc V12.8.93:

```
linear_combination_clamp.h(225): error: class "cutlass::platform::numeric_limits<float>" has no member "lowest"
```

Default device configurations dodge this because floats route to `LinearCombination`, which is presumably why CI never catches it; the class contract still advertises float support.

### Suggested fix

Add `lowest()` (`bit_cast<float, int32_t>(0xff7fffff)`) to the float specialization, and ideally the other commonly relied-on members (`min()`, `epsilon()`, `round_style`, `denorm`) so it matches the coverage of the sibling `tfloat32_t` specialization.


## 评论 (1)

### XFDG · 2026-09-13

Hi, I've submitted a fix in https://github.com/NVIDIA/cutlass/pull/3621.

# [Issue #3495] VisitorRowReduction::Callbacks::reduction is declared to return ElementCompute but has no return statement

source: https://github.com/NVIDIA/cutlass/issues/3495
state: open | updated: 2026-09-13T04:39:22Z
labels: CUTLASS C++

## 正文

### Description

`VisitorRowReduction::Callbacks::reduction` in `include/cutlass/epilogue/threadblock/fusion/visitor_store.hpp` (lines 551-560) is declared to return `ElementCompute` but contains no `return` statement; control flows off the end of a non-void function, which is undefined behavior. Compilers flag it (`-Wreturn-type` / nvcc equivalent).

The result is currently benign because the only call site (line 508) discards the return value. The function also duplicates the existing shared helper `fragment_reduce` (line 214) that the Col and Scalar reduction visitors already use at lines 330 and 748.

### Suggested fix

Either change the signature to `void`, or delete the private duplicate and call `fragment_reduce<RegReduceFn, RoundStyle>(reduce_buffer, result)` like the sibling visitors.


## 评论 (1)

### XFDG · 2026-09-13

Hi, I've submitted a fix in https://github.com/NVIDIA/cutlass/pull/3627.

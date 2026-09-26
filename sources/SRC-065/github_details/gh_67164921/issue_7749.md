# [Issue #7749] AxisInfo: Bug in DivOpAxisInfoVisitor with negative numbers

source: https://github.com/triton-lang/triton/issues/7749
state: open | updated: 2026-09-02T05:30:51Z
labels: bug

## 正文

### Describe the bug

Example:
```
// divisibility = 64, contiguity = 8, constancy = 1
%lhs = [-64, -63, -62, -61, -60, -59, -58, -57]

// divisibility = 32, contiguity = 1, constancy = 8
%rhs = [32, 32, 32, 32, 32, 32, 32, 32]

// divisibility = 1, contiguity = 1, constancy = 1
%result = arith.divsi %lhs, %rhs : tensor<8xi8>
        = [-2, -1, -1, -1, -1, -1, -1, -1]
```

However, the axis analysis computes:
```
constancy = 8
```


### Environment details

Reproducible at HEAD


## 评论 (6)

### Jokeren · 2025-08-02

Oh alright, I mistakenly thought contiguity is only applied for positive numbers.

This is a bit tricky as I think disable the analysis may cause many perf regressions.

### Jokeren · 2025-08-02

How do you get here by the way? More specifically, how this array is generated

```
[-64, -63, -62, -61, -60, -59, -58, -57]
```

### matthias-springer · 2025-08-02

This is a hand-written test case. Not from a real-world program. I found this when I was studying the code. The negative contiguous sequence could have been the result of a `arith.subi` (contiguous - constant).

I don't think there's an easy way to fix this without a range analysis. (Or maybe redefining what it means to be "contiguous".) I wouldn't disable the analysis. Just wanted to bring this to your attention and get your thoughts on it... I believe this has the potential to cause miscompiles, but probably only in edge cases.


### Jokeren · 2025-08-02

Yeah I got what you meant. Thanks for bringing it up!

### matthias-springer · 2025-08-04

btw, `remsi` has the same issue:
```
      //     [-64, -63, -62, -61, -60, -59, -58, -57]
      //     remsi [32, 32, 32, 32, 32, 32, 32, 32]
      //     = [0, -31, -30, -29, -28, -27, -26, -25]
```


### alepot55 · 2026-09-02

Both halves are reachable from plain kernels and change the output on the device (H100, d4eb2dd39). With `offs = tl.arange(0, 128)` and `x = offs - 64` (contiguity 128, divisibility 64 after the `subi`):

```python
tl.store(out_ptr + offs, x // 32)
```

`x // 32` gets constancy 32, `maybeDeduplicate` in `ElementwiseOpToLLVMBase.h` computes one division per thread and copies it into the other three registers (`st.global.v4.b32 [...], { %r1, %r1, %r1, %r1 }` in the PTX), and `out[1:4]` comes back as -2 where the source computes -1, `out[33:36]` as -1 for 0.

```python
tl.store(out_ptr + offs, tl.load(x_ptr + x % 32))
```

`x % 32` gets contiguity 32, so the load is one `ld.global.v4.b32` per thread at `x_ptr + 4*r[0]` and reads `x_ptr[0..3]` where the source reads `x_ptr[0], x_ptr[-31], x_ptr[-30], x_ptr[-29]` (`x_ptr` 64 elements into its buffer, so every source address is in bounds).

`num_warps=1`, no hints, `TRITON_INTERPRET=1` gives the source values for both.

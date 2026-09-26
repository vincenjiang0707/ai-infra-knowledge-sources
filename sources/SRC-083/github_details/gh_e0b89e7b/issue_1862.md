# [Issue #1862] gemv_4bit silently produces wrong results when weight is quantized in (in_features, out_features) layout

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1862
state: closed | updated: 2026-05-15T20:10:28Z
labels: 

## 正文

## Summary

The `gemv_4bit` CUDA kernel (the fast path for 1D inputs in `matmul_4bit`) implicitly assumes that `quant_state.shape` follows the `nn.Linear` convention of `(out_features, in_features)`. If a weight matrix is quantized in the transposed layout `(in_features, out_features)`, the gemv path silently produces **wrong output shape and wrong values** — no error is raised.

**This does not affect production usage.** All real-world code paths (`Linear4bit`, HuggingFace transformers, etc.) store weights as `(out_features, in_features)`, so the gemv path works correctly. This is a documentation/validation issue for users of the low-level `matmul_4bit` API.

## Root cause

In `bitsandbytes/backends/cuda/ops.py`, the gemv kernel uses:

```python
# Line 431
shape = (*A.shape[:-1], shapeB[0])  # output shape

# Lines 482-484
m = ct.c_int32(shapeB[0])   # treated as output dimension
k = ct.c_int32(shapeB[1])   # treated as input dimension
```

This hardcodes `shapeB[0]` as the output dimension. When `quant_state.shape = (out_features, in_features)` (the `nn.Linear` convention), this is correct. When `quant_state.shape = (in_features, out_features)`, the kernel reads the wrong number of input elements and produces the wrong number of output elements.

Meanwhile, `MatMul4Bit.forward()` (the 2D matrix path) handles both conventions transparently:

```python
output = torch.nn.functional.linear(A, F.dequantize_4bit(B, quant_state).to(A.dtype).t(), bias)
```

It dequantizes, transposes, and lets `F.linear` handle the shapes. So the matrix path works with any weight layout, but the gemv fast path does not.

## Reproduction

```python
import torch
import bitsandbytes as bnb

K, N = 128, 64  # in_features=128, out_features=64
W = torch.randn(K, N, device='cuda', dtype=torch.float16)
B, qs = bnb.functional.quantize_4bit(W, quant_type='nf4')

x = torch.randn(K, device='cuda', dtype=torch.float16)

# gemv path (1D input, no grad) — WRONG results, no error
result_gemv = bnb.matmul_4bit(x, B, qs)

# matrix path (force via requires_grad) — correct results
x2 = x.clone().requires_grad_(True)
result_correct = bnb.matmul_4bit(x2, B, qs)

print(f'gemv shape: {result_gemv.shape}')       # torch.Size([128]) — WRONG, should be 64
print(f'correct shape: {result_correct.shape}')  # torch.Size([64])  — correct
```

## Why it doesn't affect production

- `Linear4bit` stores weights as `(out_features, in_features)`, matching the gemv convention
- HuggingFace and other frameworks go through `Linear4bit`
- The existing `test_matmul_4bit` uses 2D inputs, so it never exercises the gemv path with non-square weights

## Possible fix

Add a shape check at the gemv entry point in `matmul_4bit()` (`_functions.py` ~line 394):

```python
if A.shape[-1] != quant_state.shape[1]:
    # Weight convention mismatch — fall back to matrix path
    return MatMul4Bit.apply(A, B, out, bias, quant_state)
```

Or add an assertion that raises an informative error instead of producing silent corruption.

Found during investigation of #1235.

## 评论 (1)

### matthewdouglas · 2026-05-15

Addressed in #1949. `matmul_4bit` now detects weights quantized in `(in_features, out_features)` orientation and raises a `DeprecationWarning`, still producing correct output via fallback. Support for that layout will be removed in a future release.

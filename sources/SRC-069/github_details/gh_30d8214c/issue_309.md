# [Issue #309] fix: operator precedence bug in pack_ue8m0_to_int assertion (mantissa check always passes)

source: https://github.com/deepseek-ai/DeepGEMM/issues/309
state: open | updated: 2026-04-19T01:06:49Z
labels: 

## 正文

In `deep_gemm/utils/math.py`, the `pack_ue8m0_to_int` function has an operator precedence bug that makes the validation assertion ineffective.

## Bug

```python
def pack_ue8m0_to_int(x: torch.Tensor):
    assert x.dtype == torch.float and x.size(-1) % 4 == 0
    assert (x.view(torch.int) & ((1 << 23) - 1) == 0).all()  # BUG: wrong precedence
```

In Python, `==` has higher precedence than `&`. So the expression is parsed as:
```
x.view(torch.int) & (((1 << 23) - 1) == 0)
```

`((1 << 23) - 1) == 0` evaluates to `False` (which is `0` numerically), then `x.view(torch.int) & 0` gives all zeros, and `.all()` on all zeros returns `True`.

This means the assertion **always passes** regardless of whether the mantissa bits are actually zero, so it silently accepts invalid inputs instead of catching them.

## Fix

Add parentheses to ensure the AND operation happens before the equality check:

```python
assert ((x.view(torch.int) & ((1 << 23) - 1)) == 0).all()
```

This correctly checks that all mantissa bits (lower 23 bits) are zero, which is the intended behavior for UE8M0 format values.

## 评论 (1)

### kuishou68 · 2026-04-19

I've opened PR #310 to fix this issue.

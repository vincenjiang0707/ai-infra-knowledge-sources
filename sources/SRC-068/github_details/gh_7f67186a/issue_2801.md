# [Issue #2801] [FA4] max_seqlen_q tensor causes an argument-annotation mismatch in varlen forward

source: https://github.com/Dao-AILab/flash-attention/issues/2801
state: open | updated: 2026-08-23T16:59:06Z
labels: 

## 正文

## Summary

The FA4 varlen forward path can pass a scalar `torch.Tensor` for `max_seqlen_q` into `cute.compile()`, while the compiled function declares that parameter as `Int32 | int | None`. This makes compilation fail with an argument-annotation mismatch.

## Reproduction

From a checkout of the current default branch, run:

```bash
pytest tests/cute/test_flash_attn_fast.py -k test_flash_attn_varlen_tensor_max_seqlen_reuses_fwd_cache
```

## Actual behavior

The test fails with an error equivalent to:

```
expects argument #26 (max_seqlen_q) to be one of (Int32, int, NoneType), but got torch.Tensor
```

## Expected behavior

The cache-stabilization path should retain its intended behavior while passing a value consistent with the compiled function's type contract.

## Possible direction

Normalize the scalar before invoking `cute.compile()` (for example, construct the appropriate CUTLASS DSL scalar type), or update the relevant API contract if a tensor is the intended representation.

## 评论 (1)

### eilamc14 · 2026-08-23

Reproduced on a B200, with your exact repro — it fails in 3.7 s:

```
$ python -m pytest tests/cute/test_flash_attn_fast.py \
    -k test_flash_attn_varlen_tensor_max_seqlen_reuses_fwd_cache -q
E  cutlass.base_dsl.common.DSLRuntimeError: expects argument #26 (max_seqlen_q) to be one of
   (<class 'cutlass.base_dsl.typing.Int32'>, <class 'int'>, <class 'NoneType'>),
   but got <class 'torch.Tensor'>
1 failed, 240 deselected in 3.71s
```

`main` @ `0251105`, NVIDIA B200 (compute capability 10.0), torch 2.11.0+cu130 / CUDA 13.0,
nvidia-cutlass-dsl 4.6.0.dev0.

One detail that may be worth adding to the issue: **this looks specific to SM100/SM110.**
`max_seqlen_q` is only appended to the kernel arguments on the Blackwell path — in
`_flash_attn_fwd`, both at compile time (~L1435) and at call time (~L1524):

```python
if arch // 10 in [10, 11] and not use_dedicated_hd256_kernel:
    compile_args.extend([
        ...
        blocks_to_batch_idx_tensor,
        max_seqlen_q,                # <-- only here
    ])
elif arch // 10 in [8, 9, 12]:
    compile_args.extend([
        cu_total_m_blocks_tensor,
        cu_total_splits_m_blocks_tensor,
    ])
```

sm80/90/120 never pass it, so the scalar contract is never exercised there. That would
explain why #2762 and this test pass on Hopper while the same test fails on SM100 — and
since the test isn't arch-gated, I'd expect it to fail on any SM100 runner. Practically it
means #2762's compile-key stabilization is necessary but not sufficient on Blackwell: the
value additionally has to be a host value because it is a typed kernel argument, which is
exactly what #2802 normalizes.

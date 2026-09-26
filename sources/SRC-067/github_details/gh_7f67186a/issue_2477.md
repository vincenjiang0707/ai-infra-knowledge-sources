# [Issue #2477] [FA-4][SM120] TMA-O epilogue enabled but tma_atom_O always None on Sm80 kernel path

source: https://github.com/Dao-AILab/flash-attention/issues/2477
state: closed | updated: 2026-06-05T21:07:18Z
labels: 

## 正文

# Maybe a boolean misalignment problem when you are subclassing sm120 from sm80
### Hope this issue could help you develop your sm120 forward kernel!
## Hardware: NVIDIA RTX PRO 6000 Blackwell Server Edition
## Error:

`AttributeError: 'NoneType' object has no attribute '_trait'`
`Stack: flash_fwd.py epilogue -> copy_utils.tma_get_copy_fn -> cpasync.tma_partition — atom is None.`
## Trigger: flash_attn_func via Perceiver cross-attn (used in Microsoft Aurora)
Call chain (Aurora encoder / decoder):
```python
# perceiver.py (FA-4 import)
from flash_attn.cute import flash_attn_func  # when available
# PerceiverAttention.forward
_fa_out = flash_attn_func(q, k, v, causal=False)  # (B, Lq, H, D) x (B, Lkv, H, D)
Entry from encoder:

# encoder.py — aggregate_levels
x = self.level_agg(latents, x)  # PerceiverResampler: cross-attn over level latents
```


```python
Traceback (most recent call last):
  File "/root/flash-aurora/aurora/aurora/model/encoder.py", line 197, in aggregate_levels
    x = self.level_agg(latents, x)  # (B * L, C, D)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/flash-aurora/.venv/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/flash-aurora/.venv/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/flash-aurora/aurora/aurora/model/perceiver.py", line 263, in forward
    attn_out = ln1(attn(latents, x))
                   ^^^^^^^^^^^^^^^^
  File "/root/flash-aurora/.venv/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/flash-aurora/.venv/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/flash-aurora/aurora/aurora/model/perceiver.py", line 179, in forward
    _fa_out = flash_attn_func(q, k, v, causal=False)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/flash-aurora/flash-attention/flash_attn/cute/interface.py", line 1976, in flash_attn_func
    return FlashAttnFunc.apply(
           ^^^^^^^^^^^^^^^^^^^^
  File "/root/flash-aurora/.venv/lib/python3.12/site-packages/torch/autograd/function.py", line 596, in apply
    return super().apply(*args, **kwargs)  # type: ignore[misc]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/flash-aurora/flash-attention/flash_attn/cute/interface.py", line 1802, in forward
    out, lse = _flash_attn_fwd(
               ^^^^^^^^^^^^^^^^
  File "/root/flash-aurora/flash-attention/flash_attn/cute/interface.py", line 932, in _flash_attn_fwd
    _flash_attn_fwd.compile_cache[compile_key] = cute.compile(*compile_args, options="--enable-tvm-ffi")
                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/flash-aurora/flash-attention/flash_attn/cute/flash_fwd.py", line 731, in __call__
    ).launch(
  ^^^^^^^^^^^
  File "/root/flash-aurora/flash-attention/flash_attn/cute/flash_fwd.py", line 1061, in kernel
    self.epilogue(
^^^^^^^^^^^^^^^^^^
  File "/root/flash-aurora/flash-attention/flash_attn/cute/flash_fwd.py", line 399, in epilogue
    store_O, _, _ = copy_utils.tma_get_copy_fn(
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/flash-aurora/.venv/lib/python3.12/site-packages/quack/copy_utils.py", line 776, in tma_get_copy_fn
    s, g = cpasync.tma_partition(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/root/flash-aurora/.venv/lib/python3.12/site-packages/nvidia_cutlass_dsl/python_packages/cutlass/cute/nvgpu/cpasync/helpers.py", line 209, in tma_partition
    atom._trait.value,
    ^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute '_trait'
```

## Potential Cause: 
FlashAttentionForwardSm120 subclasses FlashAttentionForwardSm80. The SM80 kernel() always calls epilogue(..., tma_atom_O=None). Previously __call__ set use_tma_O = (self.arch >= sm_90), which is True on SM12.x, so the epilogue took the TMA-O path with no TMA atom → crash.

### I solved this by: In FlashAttentionForwardSm80.__call__, set use_tma_O = False so epilogue matches the kernel (non-TMA O store only). And I removed unused Arch import. But I am not sure if this is the best solution.


## 评论 (4)

### johnnynunez · 2026-04-21

cc @blake-snc 

### blake-snc · 2026-04-22

Thanks for the cc @johnnynunez, and thanks @CatManJr for the clean root-cause analysis. This is exactly the bug I traced while validating FA4 on SM121a (DGX Spark) last week. I filed a fix at #2484 that landed yesterday: https://github.com/Dao-AILab/flash-attention/pull/2484

Your diagnosis matches symptom #2 in the PR description — base `FlashAttentionForwardBase.__init__` assigns `self.arch = BaseDSL._get_dsl().get_arch_enum()`, which returns `sm_121a` on SM120 hardware and overwrites the class-level `arch = 80` declaration. The non-varlen path then runs the TMA-O branch on a class that does not set up a TMA atom.

Your proposed fix (set `use_tma_O = False` inside `Sm80.__call__`) is functionally correct and I considered it. The reason I went with a narrower `FlashAttentionForwardSm120.__init__` override that restores `self.arch = Arch.sm_80` is to keep the blast radius off the Sm80 class so real SM8 dispatch is untouched, and to address the underlying "subclass has the wrong `self.arch`" root cause in one place rather than papering over each downstream gate (`use_tma_O` is one; `ragged = has_cu_seqlens and use_tma_O` on the varlen path is another; the `is_split_kv` read in `__call__` is a third).

Two other symptoms you will likely hit next on the same root cause if you exercise more code paths:

1. `AttributeError: 'FlashAttentionForwardSm120' object has no attribute 'is_split_kv'` on every call (the shared `Sm80.__call__` reads `self.is_split_kv`, which the base `__init__` does not set).
2. On the varlen path, `ragged = self.use_tma_O and has_cu_seqlens` is True for the same arch reason, failing at `flash_fwd.py:398` with `expects coord and shape of view are weakly congruent`.

All three are resolved by the `__init__` override in #2484. If you apply that PR on top of current main on your RTX PRO 6000, the Perceiver cross-attn call you are running should dispatch through the non-packed path. If you hit anything else I would be happy to take a look.


### CatManJr · 2026-04-22

> Thanks for the cc [@johnnynunez](https://github.com/johnnynunez), and thanks [@CatManJr](https://github.com/CatManJr) for the clean root-cause analysis. This is exactly the bug I traced while validating FA4 on SM121a (DGX Spark) last week. I filed a fix at [#2484](https://github.com/Dao-AILab/flash-attention/pull/2484) that landed yesterday: [#2484](https://github.com/Dao-AILab/flash-attention/pull/2484)
> 
> Your diagnosis matches symptom [#2](https://github.com/Dao-AILab/flash-attention/issues/2) in the PR description — base `FlashAttentionForwardBase.__init__` assigns `self.arch = BaseDSL._get_dsl().get_arch_enum()`, which returns `sm_121a` on SM120 hardware and overwrites the class-level `arch = 80` declaration. The non-varlen path then runs the TMA-O branch on a class that does not set up a TMA atom.
> 
> Your proposed fix (set `use_tma_O = False` inside `Sm80.__call__`) is functionally correct and I considered it. The reason I went with a narrower `FlashAttentionForwardSm120.__init__` override that restores `self.arch = Arch.sm_80` is to keep the blast radius off the Sm80 class so real SM8 dispatch is untouched, and to address the underlying "subclass has the wrong `self.arch`" root cause in one place rather than papering over each downstream gate (`use_tma_O` is one; `ragged = has_cu_seqlens and use_tma_O` on the varlen path is another; the `is_split_kv` read in `__call__` is a third).
> 
> Two other symptoms you will likely hit next on the same root cause if you exercise more code paths:
> 
> 1. `AttributeError: 'FlashAttentionForwardSm120' object has no attribute 'is_split_kv'` on every call (the shared `Sm80.__call__` reads `self.is_split_kv`, which the base `__init__` does not set).
> 2. On the varlen path, `ragged = self.use_tma_O and has_cu_seqlens` is True for the same arch reason, failing at `flash_fwd.py:398` with `expects coord and shape of view are weakly congruent`.
> 
> All three are resolved by the `__init__` override in [#2484](https://github.com/Dao-AILab/flash-attention/pull/2484). If you apply that PR on top of current main on your RTX PRO 6000, the Perceiver cross-attn call you are running should dispatch through the non-packed path. If you hit anything else I would be happy to take a look.

Thank you @blake-snc!

### vient · 2026-06-05

Hi, not sure why the issue got closed, the fix was not merged. I just reproduced this issue with version 4.0.0b16 on RTX PRO 6000

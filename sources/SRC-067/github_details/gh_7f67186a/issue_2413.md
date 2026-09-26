# [Issue #2413] FA4 support for RTX 6000 Pro Blackwell

source: https://github.com/Dao-AILab/flash-attention/issues/2413
state: open | updated: 2026-08-31T03:50:50Z
labels: 

## 正文

Does FA4 fully work on RTX 6000 Pro BW edititon? Wondering since the tests are failing on my GPU setup. Are there any tests for this?

## 评论 (14)

### tridao · 2026-03-30

Some of it might be working. We've merged a few PRs to support sm120, there are still some PRs pending.

### pmotgi · 2026-03-30

@tridao - thanks for your response. When I am using the branch: feat/sm120-support forward pass works fine. On latest main I still get 12.0 support error.

here's the error with feat/sm120-support branch for FLASH_ATTENTION_FAKE_TENSOR=1 FLASH_ATTENTION_CUTE_DSL_CACHE_ENABLED=1 pytest -n 64 -x tests/cute/test_flash_attn.py

```
`/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/python_packages/cutlass/base_dsl/ast_helpers.py:317: in ifExp_executor
    return then_block(*block_args) if pred else else_block(*block_args)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    if work_tile.is_valid_tile:
        block_info = BlockInfo(
            self.tile_m,
            self.tile_n,
            self.is_causal,
            self.is_local,
            self.is_split_kv,
            window_size_left,
            window_size_right,
            qhead_per_kvhead_packgqa=self.qhead_per_kvhead if const_expr(self.pack_gqa) else 1,
        )
        seqlen = SeqlenInfoQK.create(
            batch_idx,
>           seqlen_q_static=mQ.shape[0] if const_expr(not self.pack_gqa) else mQ.shape[0][1],
            seqlen_k_static=mK.shape[0],
            mCuSeqlensQ=mCuSeqlensQ,
            mCuSeqlensK=mCuSeqlensK,
            mSeqUsedQ=mSeqUsedQ,
            mSeqUsedK=mSeqUsedK,
        )
E       TypeError: 'Int32' object is not subscriptable`

```

Is the main branch expected to support sm-120?

### pmotgi · 2026-03-30

Here's my current error on the main branch with RTX 6000 pro GPU:

```
root@test:/workspace/flash-attention# python <<'PY'
import sys
sys.modules['flash_attn_2_cuda'] = type(sys)('flash_attn_2_cuda')

import torch
from flash_attn.cute import flash_attn_func

q = torch.randn(2, 256, 8, 128, dtype=torch.bfloat16, device='cuda')
k = torch.randn(2, 256, 8, 128, dtype=torch.bfloat16, device='cuda')
v = torch.randn(2, 256, 8, 128, dtype=torch.bfloat16, device='cuda')

out = flash_attn_func(q, k, v, causal=True)

print(f"Output shape: {out[0].shape}, max: {out[0].max():.4f}")
print("Forward pass OK!")
PY
Traceback (most recent call last):
  File "<stdin>", line 11, in <module>
  File "/workspace/flash-attention/flash_attn/cute/interface.py", line 1440, in flash_attn_func
    return FlashAttnFunc.apply(
           ^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/autograd/function.py", line 596, in apply
    return super().apply(*args, **kwargs)  # type: ignore[misc]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspace/flash-attention/flash_attn/cute/interface.py", line 1293, in forward
    out, lse = _flash_attn_fwd(
               ^^^^^^^^^^^^^^^^
  File "/workspace/flash-attention/flash_attn/cute/interface.py", line 256, in _flash_attn_fwd
    assert compute_capability in [9, 10, 11], "Unsupported compute capability. Supported: 9.x, 10.x, 11.x"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Unsupported compute capability. Supported: 9.x, 10.x, 11.x
```

### tridao · 2026-03-30

It’s WIP, some of it is working, some requiring small fixes 

### pmotgi · 2026-03-30

Got it, thanks for the heads up. 

### vponnam · 2026-03-30

> It’s WIP, some of it is working, some requiring small fixes

Thanks @tridao Any high level ETA for the merge? 


### tridao · 2026-03-30

Maybe 2-3 weeks. The blocker is actually setting up a machine w 5090 to test and benchmark for CI

### tridao · 2026-03-30

We also welcome contributions here 

### moghon92 · 2026-03-31

hopefully this small PR could help further: https://github.com/Dao-AILab/flash-attention/pull/2416

### pmotgi · 2026-04-03

@moghon92 - does your PR has fix for FW and backward pass both?

### Arlo0321 · 2026-05-25

any progress?

### vanbukin · 2026-07-06

Any updates?

### puppetm4st3r · 2026-07-12

any news?

### Kelvinlby · 2026-08-31

any news/updates/progress?

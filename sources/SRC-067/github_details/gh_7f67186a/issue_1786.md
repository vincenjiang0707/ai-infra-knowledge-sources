# [Issue #1786] RuntimeError when the number of tokens is too large

source: https://github.com/Dao-AILab/flash-attention/issues/1786
state: open | updated: 2026-09-09T04:53:16Z
labels: 

## 正文

```python
import flash_attn
import torch

N = 640000
# N = 1280000 # RuntimeError!
H = 1
C = 64
patch_size = 16

qkv = torch.randn((N, 3, H, C), device="cuda", dtype=torch.float16)
cu_seqlens = torch.arange(0, N + 1, step=patch_size, device="cuda", dtype=torch.int32)
feat = flash_attn.flash_attn_varlen_qkvpacked_func(
    qkv.half(),
    cu_seqlens,
    max_seqlen=patch_size,
).reshape(-1, C)

print(feat.shape)
```

I run this code on single 80G A100, it works with N=640k but failed on 1,280k or larger. 
Note that the patch_size is too small, the GPU memory is enough.
How to avoid this issue? I need to run it with very large tokens...

Environment:
```
flash_attn                             2.7.3
torch                                  2.7.1+cu126
```

Error:
```
Traceback (most recent call last):
  File "/home/t-ykong/remesh_datamaker/1.py", line 22, in <module>
    feat = flash_attn.flash_attn_varlen_qkvpacked_func(
  File "/home/t-ykong/anaconda3/envs/py310/lib/python3.10/site-packages/flash_attn/flash_attn_interface.py", line 1267, in flash_attn_varlen_qkvpacked_func
    return FlashAttnVarlenQKVPackedFunc.apply(
  File "/home/t-ykong/anaconda3/envs/py310/lib/python3.10/site-packages/torch/autograd/function.py", line 575, in apply
    return super().apply(*args, **kwargs)  # type: ignore[misc]
  File "/home/t-ykong/anaconda3/envs/py310/lib/python3.10/site-packages/flash_attn/flash_attn_interface.py", line 553, in forward
    out_padded, softmax_lse, S_dmask, rng_state = _wrapped_flash_attn_varlen_forward(
  File "/home/t-ykong/anaconda3/envs/py310/lib/python3.10/site-packages/torch/_ops.py", line 1158, in __call__
    return self._op(*args, **(kwargs or {}))
  File "/home/t-ykong/anaconda3/envs/py310/lib/python3.10/site-packages/torch/_library/autograd.py", line 113, in autograd_impl
    result = forward_no_grad(*args, Metadata(keyset, keyword_only_args))
  File "/home/t-ykong/anaconda3/envs/py310/lib/python3.10/site-packages/torch/_library/autograd.py", line 40, in forward_no_grad
    result = op.redispatch(keyset & _C._after_autograd_keyset, *args, **kwargs)
  File "/home/t-ykong/anaconda3/envs/py310/lib/python3.10/site-packages/torch/_ops.py", line 761, in redispatch
    return self._handle.redispatch_boxed(keyset, *args, **kwargs)
  File "/home/t-ykong/anaconda3/envs/py310/lib/python3.10/site-packages/torch/_library/custom_ops.py", line 335, in backend_impl
    result = self._backend_fns[device_type](*args, **kwargs)
  File "/home/t-ykong/anaconda3/envs/py310/lib/python3.10/site-packages/torch/_compile.py", line 51, in inner
    return disable_fn(*args, **kwargs)
  File "/home/t-ykong/anaconda3/envs/py310/lib/python3.10/site-packages/torch/_dynamo/eval_frame.py", line 838, in _fn
    return fn(*args, **kwargs)
  File "/home/t-ykong/anaconda3/envs/py310/lib/python3.10/site-packages/torch/_library/custom_ops.py", line 367, in wrapped_fn
    return fn(*args, **kwargs)
  File "/home/t-ykong/anaconda3/envs/py310/lib/python3.10/site-packages/flash_attn/flash_attn_interface.py", line 170, in _flash_attn_varlen_forward
    out, softmax_lse, S_dmask, rng_state = flash_attn_gpu.varlen_fwd(
RuntimeError: CUDA error: invalid configuration argument
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.
```


## 评论 (4)

### tridao · 2025-07-30

Ya there's probably a limit of 64k in the batch dimension (in this case N / patch_size). Your best bet is to manually split the input into 2 batches, call attn twice, then concat the results. 

### Gofinge · 2025-07-31

Hey, @tridao . Thanks for your great contribution, it really helps me a lot in my research.

Back to this issue, is it possible to enlarge the limitation when using sliding window attention?

### tridao · 2025-07-31

I don't think so, nvidia gpu limits to 64k in the y, z of the grid that we launch.

### Gofinge · 2025-07-31

Thanks for your quick response! I will try to chunk the data to overlap pieces to handle this issue.

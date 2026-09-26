# [Issue #1853] Support for blackwell architecture

source: https://github.com/Dao-AILab/flash-attention/issues/1853
state: open | updated: 2026-06-02T08:29:11Z
labels: 

## 正文

I tried to use flash attention but I have follow error:
FA version 3 is not supported due to FA3 is only supported on devices with compute capability >= 8 excluding 8.6 and 8.9 and Blackwell archs (>=10) 
I have a blackwell, (RTX pro 4500 blackwell), is there any expected timeline for when FA3 kernels will be available for compute capability 10.x?

## 评论 (6)

### johnnynunez · 2025-09-02

> I tried to use flash attention but I have follow error: FA version 3 is not supported due to FA3 is only supported on devices with compute capability >= 8 excluding 8.6 and 8.9 and Blackwell archs (>=10) I have a blackwell, (RTX pro 4500 blackwell), is there any expected timeline for when FA3 kernels will be available for compute capability 10.x?

you have to wait for flash attention 4 (around 3 weeks)

### tridao · 2025-09-02

RTX pro 4500 is sm_120, which is quite different from Blackwell datacenter cards like B200 (sm_100). The Ampere code (FA2) should run fine on sm_120.

https://developer.nvidia.com/cuda-gpus

<img width="1196" height="669" alt="Image" src="https://github.com/user-attachments/assets/a23fe43a-e6b3-4078-9984-e53f2e14dafd" />

### johnnynunez · 2025-09-02

> RTX pro 4500 is sm_120, which is quite different from Blackwell datacenter cards like B200 (sm_100). The Ampere code (FA2) should run fine on sm_120.
> 
> https://developer.nvidia.com/cuda-gpus
> 
> <img alt="Image" width="1196" height="669" src="https://private-user-images.githubusercontent.com/5616128/484590538-a23fe43a-e6b3-4078-9984-e53f2e14dafd.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTY4MjcwNzgsIm5iZiI6MTc1NjgyNjc3OCwicGF0aCI6Ii81NjE2MTI4LzQ4NDU5MDUzOC1hMjNmZTQzYS1lNmIzLTQwNzgtOTk4NC1lNTNmMmUxNGRhZmQucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDkwMiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTA5MDJUMTUyNjE4WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YzI5YjEyZDE3NjA4ZjEyMzA2Yzg3YjU2OGE4ODU0YmRlNzVmYmVkNzYzNmFmMmExMWIzYjExYjI0OTAxNDlmNiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.0G1eViMIDmvOMUNpCqOOCUCFVMJ1392wm1A1yxNH08w">

i think that 11.0 Thor can shared some kernels with sm_100:
From CUDA 13.0, the Blackwell SM101 for Thor GPUs is renamed to SM110.
    - For CUDA toolkit version < 13.0, SM101 is still used for Thor GPUs.
    - For CUDA toolkit version >= 13.0, SM110 is used for Thor GPUs and SM101 is no longer valid.


### triple-mu · 2025-09-19

> > RTX pro 4500 is sm_120, which is quite different from Blackwell datacenter cards like B200 (sm_100). The Ampere code (FA2) should run fine on sm_120.
> > https://developer.nvidia.com/cuda-gpus
> > <img alt="Image" width="1196" height="669" src="https://private-user-images.githubusercontent.com/5616128/484590538-a23fe43a-e6b3-4078-9984-e53f2e14dafd.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTY4MjcwNzgsIm5iZiI6MTc1NjgyNjc3OCwicGF0aCI6Ii81NjE2MTI4LzQ4NDU5MDUzOC1hMjNmZTQzYS1lNmIzLTQwNzgtOTk4NC1lNTNmMmUxNGRhZmQucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDkwMiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTA5MDJUMTUyNjE4WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YzI5YjEyZDE3NjA4ZjEyMzA2Yzg3YjU2OGE4ODU0YmRlNzVmYmVkNzYzNmFmMmExMWIzYjExYjI0OTAxNDlmNiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.0G1eViMIDmvOMUNpCqOOCUCFVMJ1392wm1A1yxNH08w">
> 
> i think that 11.0 Thor can shared some kernels with sm_100: From CUDA 13.0, the Blackwell SM101 for Thor GPUs is renamed to SM110. - For CUDA toolkit version < 13.0, SM101 is still used for Thor GPUs. - For CUDA toolkit version >= 13.0, SM110 is used for Thor GPUs and SM101 is no longer valid.

Very urgent, I would greatly appreciate it if you have a better solution!

### mcr-ksh · 2025-11-22

+1

### Dimitri-Ingenieur · 2026-06-02

> > I tried to use flash attention but I have follow error: FA version 3 is not supported due to FA3 is only supported on devices with compute capability >= 8 excluding 8.6 and 8.9 and Blackwell archs (>=10) I have a blackwell, (RTX pro 4500 blackwell), is there any expected timeline for when FA3 kernels will be available for compute capability 10.x?
> 
> you have to wait for flash attention 4 (around 3 weeks)

I get following error with flash-attn-4 (b15):  python -c "
import torch
from flash_attn.cute import flash_attn_func
q=torch.randn(1,512,8,128,device='cuda',dtype=torch.bfloat16)
out = flash_attn_func(q,q,q)
o = out[0] if isinstance(out, tuple) else out
print('FA4 OK | Typ:', type(out).__name__, '| Output-Shape:', tuple(o.shape))
"
Traceback (most recent call last):
  File "<string>", line 5, in <module>
  File "/home/dima/miniconda3/envs/lyra2/lib/python3.12/site-packages/flash_attn/cute/interface.py", line 2151, in flash_attn_func
    return FlashAttnFunc.apply(
           ^^^^^^^^^^^^^^^^^^^^
  File "/home/dima/miniconda3/envs/lyra2/lib/python3.12/site-packages/torch/autograd/function.py", line 596, in apply
    return super().apply(*args, **kwargs)  # type: ignore[misc]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dima/miniconda3/envs/lyra2/lib/python3.12/site-packages/flash_attn/cute/interface.py", line 1943, in forward
    out, lse = _flash_attn_fwd(
               ^^^^^^^^^^^^^^^^
  File "/home/dima/miniconda3/envs/lyra2/lib/python3.12/site-packages/flash_attn/cute/interface.py", line 981, in _flash_attn_fwd
    _flash_attn_fwd.compile_cache[compile_key] = cute.compile(
                                                 ^^^^^^^^^^^^^
  File "/home/dima/miniconda3/envs/lyra2/lib/python3.12/site-packages/flash_attn/cute/flash_fwd.py", line 737, in __call__
    ).launch(
  ^^^^^^^^^^^
  File "/home/dima/miniconda3/envs/lyra2/lib/python3.12/site-packages/flash_attn/cute/flash_fwd.py", line 1067, in kernel
    self.epilogue(
^^^^^^^^^^^^^^^^^^
  File "/home/dima/miniconda3/envs/lyra2/lib/python3.12/site-packages/flash_attn/cute/flash_fwd.py", line 405, in epilogue
    store_O, _, _ = copy_utils.tma_get_copy_fn(
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dima/miniconda3/envs/lyra2/lib/python3.12/site-packages/quack/copy_utils.py", line 788, in tma_get_copy_fn
    s, g = cpasync.tma_partition(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dima/miniconda3/envs/lyra2/lib/python3.12/site-packages/nvidia_cutlass_dsl/python_packages/cutlass/cute/nvgpu/cpasync/helpers.py", line 585, in tma_partition
    atom._trait.value,
    ^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute '_trait'


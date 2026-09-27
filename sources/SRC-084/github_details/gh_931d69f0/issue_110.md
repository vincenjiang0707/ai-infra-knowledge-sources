# [Issue #110] `hqq/backends/torchao.py` line 177, KeyError: 'scale'

source: https://github.com/dropbox/hqq/issues/110
state: closed | updated: 2024-08-27T13:26:38Z
labels: 

## 正文

I am trying to run the code in a GPU cloud (Runpod) and getting this error:

```
Traceback (most recent call last):
  File "/root/run_batch.py", line 65, in <module>    prepare_for_inference(model.model.decoder, backend="torchao_int4")
  File "/root/.venv/lib/python3.10/site-packages/hqq/utils/patching.py", line 116, in prepare_for_inference    patch_linearlayers(model, patch_hqq_to_aoint4, verbose=verbose)
  File "/root/.venv/lib/python3.10/site-packages/hqq/utils/patching.py", line 25, in patch_linearlayers
    model.base_class.patch_linearlayers(
  File "/root/.venv/lib/python3.10/site-packages/hqq/models/base.py", line 154, in patch_linearlayers
    patch_fct(tmp_mapping[name], patch_param),
  File "/root/.venv/lib/python3.10/site-packages/hqq/backends/torchao.py", line 323, in patch_hqq_to_aoint4
    hqq_aoint4_layer.initialize_with_hqq_quants(
  File "/root/.venv/lib/python3.10/site-packages/hqq/backends/torchao.py", line 91, in initialize_with_hqq_quants
    self.process_hqq_quants(W_q, meta)
  File "/root/.venv/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/root/.venv/lib/python3.10/site-packages/hqq/backends/torchao.py", line 177, in process_hqq_quants
    scales = meta["scale"]
KeyError: 'scale'
```

Env:

```yaml
torch: 2.5.0.dev20240826+cu118
torchao: 0.4.0+gitc2f44608
hqq: 0.2.0
transformers: 4.44.2
```

Python 3.10.12


## 评论 (13)

### egorsmkv · 2024-08-26

<img width="1470" alt="image" src="https://github.com/user-attachments/assets/a23ff10b-1918-46d5-b375-d88f525016e1">

how it looks like

### egorsmkv · 2024-08-26

The script I'm running:

https://github.com/egorsmkv/optimized-whisper/blob/main/run_batch.py

### egorsmkv · 2024-08-26

I guess this is because cuda 11.8 ?

### mobicham · 2024-08-27

I think you need at least CUDA 12.1. 
It works if you just do `prepare_for_inference(model.model.decoder)` ?

By the way, you don't need to quantize the encoder, you can keep it in `compute_dtype` on the cuda device.

### egorsmkv · 2024-08-27

Hmmm

I see this issue with CUDA 12.4:

<img width="1160" alt="image" src="https://github.com/user-attachments/assets/ab779f2b-71db-4ece-b8cf-076efdd9846d">


### egorsmkv · 2024-08-27

> It works if you just do `prepare_for_inference(model.model.decoder)` ?

Yes, it works correctly.

### egorsmkv · 2024-08-27

Just log these issues for knowledge expanison:

<img width="1395" alt="image" src="https://github.com/user-attachments/assets/965525db-39fb-4087-b800-cfde2220da9d">


### egorsmkv · 2024-08-27

Without `torchao_int4` it works:

<img width="831" alt="image" src="https://github.com/user-attachments/assets/9b6ea80b-9ca5-4068-99eb-9d845b6251c7">

Elapsed time: `5.9743781089782715` here for batch size of 16

### mobicham · 2024-08-27

I see, then it's a Pytorch issue, maybe transformers doesn't work properly with 12.4. But it should work with cuda-12.1:

```
sudo apt install cuda-12-1
```

You can switch between different CUDA versions like this: 
```
export CUDA_HOME=/usr/local/cuda-12.1
export LD_LIBRARY_PATH=${CUDA_HOME}/lib64:$LD_LIBRARY_PATH
export PATH=${CUDA_HOME}/bin:${PATH}
```

It will work without `torch_int4` but it's gonna be very slow, you need either the bitblas or torchao_int4 backend to run it faster. 
If you have issues with cuda, maybe you can try the bitblas backend:

1- Install bitblas `pip install bitblas`
2- Change the compute_dtype from `torch.bfloat16` to `torch.float16`
3- use `prepare_for_inference(model.model.decoder, backend='bitblas`)`

### egorsmkv · 2024-08-27

Hmmm, something wrong with CUDA 12.1 too:

```
Warning: failed to import the Marlin backend. Check if marlin is correctly installed if you want to use the Marlin backend (https://github.com/IST-DAS
Lab/marlin).
Warning: failed to import the BitBlas backend. Check if BitBlas is correctly installed if you want to use the bitblas backend (https://github.com/micr
osoft/BitBLAS).
torch: 2.5.0.dev20240827+cu121
torchao: 0.4.0+git37276d61
hqq: 0.2.0
transformers: 4.44.2

...

Traceback (most recent call last):
  File "/root/optimized-whisper/run_batch.py", line 58, in <module>
    prepare_for_inference(model.model.decoder, backend="torchao_int4")
  File "/root/.venv/lib/python3.12/site-packages/hqq/utils/patching.py", line 116, in prepare_for_inference
    patch_linearlayers(model, patch_hqq_to_aoint4, verbose=verbose)
  File "/root/.venv/lib/python3.12/site-packages/hqq/utils/patching.py", line 25, in patch_linearlayers
    model.base_class.patch_linearlayers(
  File "/root/.venv/lib/python3.12/site-packages/hqq/models/base.py", line 154, in patch_linearlayers
    patch_fct(tmp_mapping[name], patch_param),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/.venv/lib/python3.12/site-packages/hqq/backends/torchao.py", line 323, in patch_hqq_to_aoint4
    hqq_aoint4_layer.initialize_with_hqq_quants(
  File "/root/.venv/lib/python3.12/site-packages/hqq/backends/torchao.py", line 91, in initialize_with_hqq_quants
    self.process_hqq_quants(W_q, meta)
  File "/root/.venv/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/root/.venv/lib/python3.12/site-packages/hqq/backends/torchao.py", line 177, in process_hqq_quants
    scales = meta["scale"]
             ~~~~^^^^^^^^^
KeyError: 'scale'



(root) root@bcc42e05e20e:~/optimized-whisper# nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Mon_Apr__3_17:16:06_PDT_2023
Cuda compilation tools, release 12.1, V12.1.105
Build cuda_12.1.r12.1/compiler.32688072_0
```


### egorsmkv · 2024-08-27

> If you have issues with cuda, maybe you can try the bitblas backend

Tested with `bitblas`, it works correctly.

### egorsmkv · 2024-08-27

@mobicham I think I have found the issue, I was configuring `hqq` with `offload_meta` enabled.

```
quant_config = BaseQuantizeConfig(
    nbits=4,
    group_size=64,
    quant_scale=False,
    quant_zero=False,
    axis=1,
    offload_meta=True,
)
```

I just disabled it and it works correctly on CUDA 12.1.


### mobicham · 2024-08-27

`offload_meta` is deprecated, gonna remove it soon

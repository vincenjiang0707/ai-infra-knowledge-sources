# [Issue #153] awq_inference_engine has no attribute 'gemm_forward_cuda_new'

source: https://github.com/mit-han-lab/llm-awq/issues/153
state: open | updated: 2026-07-16T15:06:33Z
labels: 

## 正文

Hi, when running the vlm demo 

```
python vlm_demo.py --model-path ../cache/VILA-7b --quant-path ../cache/VILA-7b-4bit-awq/vila-7b-w4-g128-v2.pt --precision W4A16 --image-file sample.jpg
```
I got the following error:
```
AttributeError: module 'awq_inference_engine' has no attribute 'gemm_forward_cuda_new'. Did you mean: 'gemm_forward_cuda'?
```

## 评论 (5)

### ys-2020 · 2024-03-07

Hi, please re-install the new version of AWQ following the readme. The new backend kernels can be installed via `python setup.py install` in `awq/kernels`.

### pribadihcr · 2024-03-08

> Hi, please re-install the new version of AWQ following the readme. The new backend kernels can be installed via `python setup.py install` in `awq/kernels`.

Thanks. I have installed. Got new error 
```
python vlm_demo.py --model-path ../cache/VILA-7b --quant-path ../cache/VILA-7b-4bit-awq/vila-7b-w4-g128-v2.pt --precision W4A16 --image-file sample.jpg
```

```
RuntimeError: CUDA error: no kernel image is available for execution on the device
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.
```

### ys-2020 · 2024-03-08

Looks like you have built and installed the awq_inference_engine, but not the correct kernel image for your device.

This might be caused by building kernel images upon previous cached image. Please try to remove the `build` folder in `awq/kernels` and try `python setup.py install` again.


### pribadihcr · 2024-03-12

Hi, suddently, In the middle of build the kernel I got the following message:

```
ptxas /tmp/tmpxft_00005e08_00000000-6_gemm_cuda.ptx, line 144; error   : Feature 'cp.async' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00005e08_00000000-6_gemm_cuda.ptx, line 159; error   : Feature 'cp.async' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00005e08_00000000-6_gemm_cuda.ptx, line 186; error   : Feature 'cp.async' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00005e08_00000000-6_gemm_cuda.ptx, line 211; error   : Feature 'cp.async' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00005e08_00000000-6_gemm_cuda.ptx, line 218; error   : Feature 'cp.async' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00005e08_00000000-6_gemm_cuda.ptx, line 227; error   : Feature 'cp.async' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00005e08_00000000-6_gemm_cuda.ptx, line 241; error   : Feature 'cp.async' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00005e08_00000000-6_gemm_cuda.ptx, line 255; error   : Feature 'cp.async' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00005e08_00000000-6_gemm_cuda.ptx, line 278; error   : Feature 'cp.async' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00005e08_00000000-6_gemm_cuda.ptx, line 285; error   : Feature 'cp.async' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00005e08_00000000-6_gemm_cuda.ptx, line 294; error   : Feature 'cp.async' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00005e08_00000000-6_gemm_cuda.ptx, line 303; error   : Feature 'cp.async' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00005e08_00000000-6_gemm_cuda.ptx, line 312; error   : Feature 'cp.async' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00005e08_00000000-6_gemm_cuda.ptx, line 335; error   : Feature 'cp.async' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00005e08_00000000-6_gemm_cuda.ptx, line 342; error   : Feature 'cp.async' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00005e08_00000000-6_gemm_cuda.ptx, line 868; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00005e08_00000000-6_gemm_cuda.ptx, line 871; error   : Feature '.m16n8k16' requires .target sm_80 or higher
....

my GPU is 2070


### Chessing234 · 2026-07-16

Fixed in #329 — fall back to `gemm_forward_cuda` when `_new` is missing.

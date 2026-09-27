# [Issue #1937] [Windows] RTX 5070 Ti (Blackwell sm_120) - quantization support missing

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1937
state: closed | updated: 2026-05-26T14:55:46Z
labels: Windows, Waiting for Info, CUDA

## 正文

### Environment
- GPU: NVIDIA GeForce RTX 5070 Ti Laptop GPU (Blackwell, compute capability 12.0)
- Driver: 595.79 (CUDA 13.2)
- OS: Windows 11
- Python: 3.14
- PyTorch: 2.11.0+cu130

### Problem
bitsandbytes does not work on RTX 5070 Ti out of the box:

1. **sm_120 not in supported architecture list** - CUDA kernels not compiled for Blackwell
2. **CUDA 13.0+ runtime** - Driver 595.79 reports CUDA 13.2, bitsandbytes may need CUDA 13.x compatible wheels
3. **Import error**: `RuntimeError: CUDA error: no kernel image is available for execution on the device` when loading 4-bit/8-bit quantized models
4. **Windows support** - bitsandbytes Windows wheels are limited; custom builds require CUDA Toolkit 12.x which conflicts with CUDA 13.0+ driver requirements

### Workaround
Currently, quantization must be done on a supported GPU (Ampere/Hopper) and the quantized weights transferred to the RTX 5070 Ti for inference. This is not ideal for Windows users who want end-to-end local quantization.

### Question
Is there a roadmap for Blackwell (sm_120) support in bitsandbytes? RTX 5070/5080/5090 are the first consumer Blackwell GPUs and many users will want to quantize models locally.

Happy to help test sm_120 CUDA kernel compilation if there's a development branch.

## 评论 (2)

### matthewdouglas · 2026-05-05

Hi @loongmiaow-pixel.

What version of bitsandbytes are you using? We do compile for sm_120 on both Windows and Linux, and have been since around v0.45.3 over one year ago.

These builds should work fine when using a PyTorch build with CUDA 12.8+. We currently do ship CUDA 13.0 binaries, which will run fine on a system with the r595 (13.2) driver. You should see a libbitsandbytes_cuda130.dll in your wheel installation. Since you're using a cu130 build of PyTorch, that's what it should be loading by default.

If you're building bitsandbytes from source it builds as expected with CUDA Toolkit 13.1 and 13.2 as well. However, depending on CMake version, it may not include sm120 by default. You can ensure that it does build sm_120 with `-DCOMPUTE_CAPABILITY=120` at configure time with cmake. But again, you shouldn't need to build from source, as our wheels do ship with sm_120 capability.

Is there more information you can share, i.e. more context with a stack trace, example code, etc that might help. 



### matthewdouglas · 2026-05-26

Closing as inactive. If there's more information we can consider reopening.

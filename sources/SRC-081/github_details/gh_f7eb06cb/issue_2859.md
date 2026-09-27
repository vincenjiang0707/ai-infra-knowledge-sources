# [Issue #2859] CUDA and torch version issue

source: https://github.com/ModelCloud/GPTQModel/issues/2859
state: closed | updated: 2026-05-07T05:50:09Z
labels: 

## 正文

During my quantization process, I found that GPTQModel **versions 6.0.0 and above** require **CUDA 13 and the corresponding torch version**. 
Upgrading to CUDA 13 is very troublesome in my current environment. 
So I would like to ask: is CUDA 12.8 supported? Or is it necessary to upgrade to CUDA 13?

`packages/torch/cuda/__init__.py:180: UserWarning: CUDA initialization: The NVIDIA driver on your system is too old (found version 12040). Please update your GPU driver by downloading and installing a new version from the URL: http://www.nvidia.com/Download/index.aspx Alternatively, go to: https://pytorch.org to install a PyTorch version that has been compiled with your version of the CUDA driver. (Triggered internally at /pytorch/c10/cuda/CUDAFunctions.cpp:119.)
  return torch._C._cuda_getDeviceCount() > 0`

## 评论 (2)

### Qubitium · 2026-05-06

@Jealousc11gx Show me the stacktrace when you run gpt-qmodel 7.0 or main under cuda 12.8 as it should be supported. 

### Jealousc11gx · 2026-05-07

After testing, it has been found that currently CUDA 12.8 is supported, while earlier CUDA 12.4 is not.

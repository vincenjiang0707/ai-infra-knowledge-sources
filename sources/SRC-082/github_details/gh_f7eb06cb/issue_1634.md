# [Issue #1634] pip install stuck

source: https://github.com/ModelCloud/GPTQModel/issues/1634
state: closed | updated: 2025-12-23T09:45:18Z
labels: 

## 正文

I use pip install: "pip install -v gptqmodel --no-build-isolation"

stuck in this process: 
Building wheels for collected packages: gptqmodel, device-smi, logbar, tokenicer
  Running command python setup.py bdist_wheel
  conda_cuda_include_dir /search/odin/miniconda3/envs/deepseek_r1_py39/lib/python3.9/site-packages/nvidia/cuda_runtime/include
  appending conda cuda include dir /search/odin/miniconda3/envs/deepseek_r1_py39/lib/python3.9/site-packages/nvidia/cuda_runtime/include
  running bdist_wheel
  Guessing wheel URL: https://github.com/ModelCloud/GPTQModel/releases/download/v2.2.0/gptqmodel-2.2.0+cu124torch2.4-cp39-cp39-linux_x86_64.whl
  wheel name=gptqmodel-2.2.0+cu124torch2.4-cp39-cp39-linux_x86_64.whl
 
who can know why & how to fix it

## 评论 (2)

### Zihan01123 · 2025-06-26

I have the same problem too

### Qubitium · 2025-12-23

Let me know if this bug persists.

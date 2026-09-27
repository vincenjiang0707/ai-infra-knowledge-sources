# [Issue #3175] [Question] Does it support multi-gpu (intel ARC A770)?

source: https://github.com/mlc-ai/mlc-llm/issues/3175
state: closed | updated: 2026-03-18T10:45:32Z
labels: question

## 正文

## ❓ Does mlc-llm support Multuple GPU (ARC A770)

Does it support multi gpu?
I have 4 gpu Intel A770 installed.

i changed "**tensor_parallel_shards**": 1 to 4 in mlc-chat-config.json

(mlc) J:\models\mlc\Qwen2.5-32B-Instruct-q4f16_1-MLC>mlc_llm chat . --device vulkan
[2025-03-14 19:32:41] INFO auto_device.py:79: Found device: vulkan:0
[2025-03-14 19:32:41] INFO auto_device.py:79: Found device: vulkan:1
[2025-03-14 19:32:41] INFO auto_device.py:79: Found device: vulkan:2
[2025-03-14 19:32:41] INFO auto_device.py:79: Found device: vulkan:3
[2025-03-14 19:32:41] INFO jit.py:43: MLC_JIT_POLICY = ON. Can be one of: ON, OFF, REDO, READONLY
[2025-03-14 19:32:41] INFO jit.py:118: Compiling using commands below:
[2025-03-14 19:32:41] INFO jit.py:119: 'C:\Users\uuk\miniforge3\envs\mlc\python.exe' -m mlc_llm compile . --opt 'flashinfer=1;cublas_gemm=1;faster_transformer=0;cudagraph=1;cutlass=1;ipc_allreduce_strategy=NONE' --overrides '' --device vulkan:0 --output 'C:\Users\uuk\AppData\Local\Temp\tmpvtiprxf9\lib.dll'
[2025-03-14 19:32:43] INFO auto_config.py:70: Found model configuration: mlc-chat-config.json
[2025-03-14 19:32:43] INFO auto_target.py:91: Detecting target device: vulkan:0
[Vulkan Loader] INFO:           Using Vulkan Loader C:\Windows\System32\vulkan-1.dll
[Vulkan Loader] INFO:           Vulkan Loader Version 1.4.309
...
ValueError: Traceback (most recent call last):
  File "D:\a\package\package\mlc-llm\cpp\serve\engine.cc", line 726
ValueError: Multi-GPU on device vulkan is not supported. Currently, only NCCL and RCCL are integrated.


[error-log.txt](https://github.com/user-attachments/files/19251356/error-log.txt)

## 评论 (1)

### MasterJH5574 · 2025-03-18

Hi @savvadesogle thank you for the question. As of now we only support CUDA and ROCm for multi-GPU, and they use NCCL and RCCL for inter-GPU communication respectively.

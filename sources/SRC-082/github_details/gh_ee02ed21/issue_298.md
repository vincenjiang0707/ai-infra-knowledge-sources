# [Issue #298] 在RTX5090上的torch 和 torchvision和CUDA的兼容问题

source: https://github.com/mit-han-lab/llm-awq/issues/298
state: open | updated: 2025-09-14T22:16:45Z
labels: 

## 正文

RuntimeError: CUDA error: no kernel image is available for execution on the device
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.  报错

## 评论 (1)

### Louym · 2025-09-14

Could you try this [file](https://github.com/Louym/llm-awq/blob/main/awq/kernels/setup.py)? Just replace the original setup.py.

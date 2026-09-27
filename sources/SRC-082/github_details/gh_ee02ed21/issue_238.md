# [Issue #238] RuntimeError: CUDA error: no kernel image is available for execution on the device

source: https://github.com/mit-han-lab/llm-awq/issues/238
state: open | updated: 2024-12-09T04:07:26Z
labels: 

## 正文

    cos = cos[position_ids].unsqueeze(unsqueeze_dim)
RuntimeError: CUDA error: no kernel image is available for execution on the device
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions

## 评论 (1)

### Yiman-GO · 2024-12-09

have you solved this problem? I met the same runtimeerror at "out = out + self.bias if self.bias is not None else out"

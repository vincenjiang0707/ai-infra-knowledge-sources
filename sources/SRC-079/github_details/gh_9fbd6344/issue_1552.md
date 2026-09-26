# [Issue #1552] Static NVFP4 weight MSE calibration fails for padded block dimensions

source: https://github.com/NVIDIA/Model-Optimizer/issues/1552
state: closed | updated: 2026-05-29T06:52:39Z
labels: bug, waiting for feedback, torch.quantization, triaged

## 正文

**Before submitting an issue, please make sure it hasn't been already addressed by searching through the [existing and past issues](https://github.com/NVIDIA/Model-Optimizer/issues?q=is%3Aissue).**

## Describe the bug

`mtq.NVFP4_W4A4_WEIGHT_MSE_FP8_SWEEP_CFG` / `nvfp4_mse` fails during static NVFP4 weight MSE calibration when the quantized weight dimension is not divisible by the NVFP4 block size (`16`).

This appears to be a padding/layout mismatch in the MSE calibration path. For a weight with shape `512x60`, static block quantization pads the last dimension to `64`, producing a blocked calibration tensor of shape `2048x16`. The quantized/dequantized result is sliced back to the logical shape `512x60`, then reshaped to `1920x16`, so `F.mse_loss` compares `2048x16` against `1920x16`.

Stack trace ends with:

```text
UserWarning: Using a target size (torch.Size([1920, 16])) that is different to the input size (torch.Size([2048, 16])).
RuntimeError: The size of tensor a (2048) must match the size of tensor b (1920) at non-singleton dimension 0
```

I did not find an existing public issue for this exact padded static NVFP4 MSE shape mismatch.

### Steps/Code to reproduce bug

```python
import copy

import torch
import torch.nn as nn

import modelopt
import modelopt.torch.quantization as mtq


class SingleLinear(nn.Module):
    def __init__(self):
        super().__init__()
        # Last weight dimension is 60, which is not divisible by NVFP4 block size 16.
        self.proj = nn.Linear(60, 512, bias=False)

    def forward(self, x):
        return self.proj(x)


def main():
    print(f"torch: {torch.__version__}")
    print(f"modelopt: {getattr(modelopt, '__version__', '<unknown>')}")

    model = SingleLinear().eval().to(device="cuda", dtype=torch.bfloat16)
    x = torch.randn(2, 60, device="cuda", dtype=torch.bfloat16)

    quant_cfg = copy.deepcopy(mtq.NVFP4_W4A4_WEIGHT_MSE_FP8_SWEEP_CFG)
    mtq.quantize(model, quant_cfg, forward_loop=lambda quantized_model: quantized_model(x))


if __name__ == "__main__":
    main()
```

Observed with ModelOpt `0.44.0`:

```text
torch: 2.8.0+cu128
modelopt: 0.44.0
Inserted 3 quantizers
MSE weight calibration:   0%|          | 0/1 [00:00<?, ?it/s]
UserWarning: Using a target size (torch.Size([1920, 16])) that is different to the input size (torch.Size([2048, 16])).
RuntimeError: The size of tensor a (2048) must match the size of tensor b (1920) at non-singleton dimension 0
```

Sanity checks:

```text
NVFP4_DEFAULT_CFG / Linear(60,512): PASS
NVFP4_W4A4_WEIGHT_MSE_FP8_SWEEP_CFG / Linear(60,512): FAIL
NVFP4_W4A4_WEIGHT_MSE_FP8_SWEEP_CFG / Linear(64,512): PASS
```

I also tested current `main` at commit `b49f9b9e2d747af992d78a3aa7f10efe5a8847e1`. The default Triton fast path passes, but forcing the reference path with:

```bash
MODELOPT_NVFP4_TRITON_SWEEP=0
```

still reproduces the same `2048x16` vs `1920x16` mismatch.

### Expected behavior

Static NVFP4 weight MSE calibration should handle weights whose block dimension is not divisible by `16`, since the quantizer already tracks padding/slicing metadata.

The MSE comparison should use matching layouts, e.g. re-pad the QDQ result before reshaping back to the blocked calibration shape:

```text
logical QDQ: 512x60
re-pad:      512x64
block view:  2048x16
```

At minimum, if this case is intentionally unsupported, ModelOpt should fail early with a clear diagnostic instead of reaching a tensor shape mismatch inside `F.mse_loss`.

### Who can help?

- ?

## System information

- Container used (if applicable): Not using a container; local Python/uv virtual environment
- OS (e.g., Ubuntu 22.04, CentOS 7, Windows 10): Ubuntu 24.04.4 LTS
- CPU architecture (x86_64, aarch64): x86_64
- GPU name (e.g. H100, A100, L40S): NVIDIA GeForce RTX 5080
- GPU memory size: 16303 MiB
- Number of GPUs: 1
- Library versions (if applicable):
  - Python: 3.12.3
  - ModelOpt version or commit hash: 0.44.0; also tested current main at `b49f9b9e2d747af992d78a3aa7f10efe5a8847e1`
  - CUDA: PyTorch CUDA 12.8; NVIDIA driver reports CUDA 13.0
  - PyTorch: 2.8.0+cu128
  - Transformers: 4.57.1
  - TensorRT-LLM: not installed
  - ONNXRuntime: not installed
  - TensorRT: 10.12.0.36
- Any other details that may help:
  - NVIDIA driver: 580.126.20
  - The issue appears specific to static NVFP4 weight MSE / FP8 scale sweep with padded block dimensions.
  - Regular `NVFP4_DEFAULT_CFG` uses dynamic block quantization and does not reproduce this issue on the same `Linear(60,512)` repro.


## 评论 (1)

### edmundshieh · 2026-05-28

A fix is open in #1557. The PR adds a CUDA regression test for the padded static NVFP4 MSE reference path and verifies that the forced reference sweep now completes for a `Linear(60, 512)` weight. Please try the PR branch when convenient and confirm whether it resolves the reported failure.

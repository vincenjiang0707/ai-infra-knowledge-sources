# [Issue #2330] After applying NVFP4 quantization followed by compression, RealQuantLinear fails to locate the corresponding GEMM implementation during inference.

source: https://github.com/NVIDIA/Model-Optimizer/issues/2330
state: open | updated: 2026-09-05T02:26:42Z
labels: bug

## 正文

**Before submitting an issue, please make sure it hasn't been already addressed by searching through the [existing and past issues](https://github.com/NVIDIA/Model-Optimizer/issues?q=is%3Aissue).**

## Describe the bug

After quantizing a model with `mtq.quantize` and subsequently applying `mtq.compress`, ModelOpt issues the following warning during inference: "RealQuantLinear: No real-quant GEMM found". However, ModelOpt does include an implementation of real-quant GEMM for nvfp4, which is located at https://github.com/NVIDIA/Model-Optimizer/blob/51cc5dbadeedd93cba5cc37eec637f26efd3f8ab/modelopt/torch/quantization/backends/nvfp4_gemm.py#L32.

### Steps/Code to reproduce bug

``` python
import modelopt
import torch

import modelopt.torch.quantization as mtq

from torch import nn

K_DTYPE = torch.bfloat16
K_BATCH = 128
K_DIM = 512


class Model(nn.Module):
    def __init__(self, dim: int) -> None:
        super().__init__()

        self.fc = nn.Linear(dim, dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out = self.fc(x)

        return out


def main():
    print(f"torch: {torch.__version__}")
    print(f"modelopt: {getattr(modelopt, '__version__', '<unknown>')}")

    device = torch.device("cuda:0")

    model = Model(K_DIM).to(K_DTYPE)
    model.to(device)

    inp = torch.randn(K_BATCH, K_DIM, dtype=K_DTYPE, device=device)

    qmodel = mtq.quantize(model, mtq.NVFP4_DEFAULT_CFG, lambda quantized_model: quantized_model(inp))
    mtq.compress(qmodel)

    qout = qmodel(inp)


if __name__ == "__main__":
    main()

```

Observed with ModelOpt current `main` with `51cc5dbadeedd93cba5cc37eec637f26efd3f8ab`:

``` scripts
torch: 2.12.0+cu130
modelopt: 0.0.1.dev1186+g51cc5dbad
Inserted 3 quantizers
[TensorRT-LLM] TensorRT LLM version: 1.3.0rc25
`PixtralImageProcessorFast` is deprecated. The `Fast` suffix for image processors has been removed; use `PixtralImageProcessor` instead.
/root/workspace/Model-Optimizer/modelopt/torch/quantization/compress.py:117: UserWarning: Real quantization has been applied to the model. This feature is still experimental, and some functionalities may not be supported. For example, converting the model back to its original state or saving and restoring the quantized model may not be available.
  warnings.warn(
/root/workspace/Model-Optimizer/modelopt/torch/quantization/nn/modules/quant_linear.py:218: UserWarning: RealQuantLinear: No real-quant GEMM found: RealQuantQuantLinear(
  in_features=512, out_features=512, bias=True
  (input_quantizer): TensorQuantizer((2, 1) bit fake block_sizes={-1: 16, 'type': 'dynamic', 'scale_bits': (4, 3)}, amax=4.22e+00 calibrator=MaxCalibrator quant)
  (output_quantizer): TensorQuantizer(disabled)
  (weight_quantizer): TensorQuantizer((2, 1) bit block_sizes={-1: 16, 'type': 'dynamic', 'scale_bits': (4, 3)}, amax=4.42e-02 calibrator=MaxCalibrator quant)
).
  warnings.warn(f"RealQuantLinear: No real-quant GEMM found: {self}.")
```

After quantizing a model with `mtq.quantize` and subsequently applying `mtq.compress`, ModelOpt issues the following warning during inference: "RealQuantLinear: No real-quant GEMM found". However, ModelOpt does include an implementation of real-quant GEMM for nvfp4, which is located at https://github.com/NVIDIA/Model-Optimizer/blob/51cc5dbadeedd93cba5cc37eec637f26efd3f8ab/modelopt/torch/quantization/backends/nvfp4_gemm.py#L32.

Upon debugging, I found that `self._real_quant_gemm_impl` in `modelopt/torch/quantization/nn/modules/quant_linear.py:241` is None, which triggers the warning: "RealQuantLinear: No real-quant GEMM found".

``` scripts
> /root/workspace/Model-Optimizer/modelopt/torch/quantization/nn/modules/quant_linear.py(214)has_real_quant_gemm_impl()
-> self._real_quant_gemm_impl = backends.gemm_registry.find_match(
(Pdb) l
209  	        )
210  	
211  	    def has_real_quant_gemm_impl(self, input, *args, **kwargs) -> bool:
212  	        """Get the real quant GEMM implementation base on input arguments."""
213  	        if not hasattr(self, "_real_quant_gemm_impl"):
214  ->	            self._real_quant_gemm_impl = backends.gemm_registry.find_match(
215  	                self, input, *args, **kwargs
216  	            )
217  	            if self._real_quant_gemm_impl is None:
218  	                warnings.warn(f"RealQuantLinear: No real-quant GEMM found: {self}.")
219 
```

The value of `self._real_quant_gemm_impl` is `None` because the check for the input quantizer config in `modelopt/torch/quantization/backends/nvfp4_gemm.py` fails.

``` scripts
  /root/workspace/Model-Optimizer/modelopt/torch/quantization/nn/modules/quant_linear.py(232)forward()
-> and self.has_real_quant_gemm_impl(input, *args, **kwargs)
  /root/workspace/Model-Optimizer/modelopt/torch/quantization/nn/modules/quant_linear.py(214)has_real_quant_gemm_impl()
-> self._real_quant_gemm_impl = backends.gemm_registry.find_match(
  /root/workspace/Model-Optimizer/modelopt/torch/quantization/backends/gemm_registry.py(92)find_match()
-> if entry["availability_check"](module, input, args, kwargs):
> /root/workspace/Model-Optimizer/modelopt/torch/quantization/backends/nvfp4_gemm.py(241)_nvfp4_availability_check()
-> return False
(Pdb) l
236  	            continue
237  	        if (
238  	            not hasattr(module.input_quantizer, key)
239  	            or getattr(module.input_quantizer, key) != value
240  	        ):
241 B->	            return False
242  	
243  	    # Check weight quantizer config
244  	    for key, value in weight_cfg.items():
245  	        if key == "enable":
246  	            continue
(Pdb) p key
'effective_bits'
(Pdb) p hasattr(module.input_quantizer, 'effective_bits')
False
(Pdb) p hasattr(module.input_quantizer, '_effective_bits')
True
```

In `mtq.quantize`, the attributes of the input quantizer are set based on the config keys with an underscore prefix added to each key; for example, "effective_bits" becomes "_effective_bits". However, the check in `modelopt/torch/quantization/backends/nvfp4_gemm.py` does not account for this underscore-prefixed naming convention, resulting in the check failure.

### Expected behavior

After performing nvfp4 quantization with `mtq.quantize` followed by `mtq.compress`, the model correctly locates the nvfp4 GEMM implementation during inference, and the warning "RealQuantLinear: No real-quant GEMM found" is no longer issued.

### Who can help?

<!-- To expedite the response to your issue, it would be helpful if you could identify the appropriate person(s) to tag using the @ symbol.
If you are unsure about whom to tag, you can leave it blank, and we will make sure to involve the appropriate person. -->

- ?

## System information

<!-- Run this script to automatically collect system information: https://github.com/NVIDIA/Model-Optimizer/blob/main/.github/ISSUE_TEMPLATE/get_system_info.py -->

- Container used (if applicable): N/A
- OS: Ubuntu 22.04
- CPU architecture: x86_64
- GPU name: RTX 5090
- GPU memory size: 32GB
- Number of GPUs: 1
- Library versions (if applicable):
  - Python: 3.12.3
  - ModelOpt version or commit hash: 51cc5dbadeedd93cba5cc37eec637f26efd3f8ab
  - CUDA: 13.2
  - PyTorch: 2.12.0
  - Transformers: 5.5.4
  - TensorRT-LLM: 1.3.0rc25
  - ONNXRuntime: 1.24.4
  - TensorRT: N/A
- Any other details that may help: N/A


## 评论 (2)

### hychiang-git · 2026-09-04

Root cause: [PR #1856](https://github.com/NVIDIA/Model-Optimizer/pull/1856) added the AutoQuantize-only effective_bits field to the shared NVFP4 config. mtq.quantize() stored it as _effective_bits, but the NVFP4 GEMM checker searched only for effective_bits, falsely rejected the compatible kernel, and fell back to the ordinary GEMM path.

### Lee-YNU · 2026-09-05

I get it. To address the current issue, would it be more appropriate to modify the checker's logic, or to avoid storing effective_bits as _effective_bits?

source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/scaled_mm/ScaledMMLinearKernel/
lastmod: 2026-09-24

#

`vllm.model_executor.kernels.linear.scaled_mm.ScaledMMLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.ScaledMMLinearKernel)

Classes:

##

`ScaledMMLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.ScaledMMLinearKernel.ScaledMMLinearKernel)

Bases:

, [Generic](https://docs.python.org/3/library/typing.html#typing.Generic)[_ConfigT, _ParamsT][ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Methods:

-
–[input_quant_key](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.ScaledMMLinearKernel.ScaledMMLinearKernel.input_quant_key)The activation quant key this kernel can consume pre-quantized.


## Source code in `vllm/model_executor/kernels/linear/scaled_mm/ScaledMMLinearKernel.py`


###

`input_quant_key()`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.ScaledMMLinearKernel.ScaledMMLinearKernel.input_quant_key)

The activation quant key this kernel can consume pre-quantized.

Manual fusion uses this to decide whether to hoist activation quantization out of apply_weights into an upstream fused kernel. Return None when the kernel needs in-kernel quantization (custom padding or swizzling, dynamic scales, etc.). Kernels that return a key must consume the activation via as_quantized_activation.
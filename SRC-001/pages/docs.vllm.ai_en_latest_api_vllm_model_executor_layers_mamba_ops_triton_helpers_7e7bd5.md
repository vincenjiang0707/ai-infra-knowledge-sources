source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/ops/triton_helpers/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.mamba.ops.triton_helpers`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.triton_helpers)

Functions:

-
–[fast_exp](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.triton_helpers.fast_exp)Faster alternative to tl.exp() using the hardware exp2 instruction.


##

`fast_exp(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.triton_helpers.fast_exp)

Faster alternative to tl.exp() using the hardware exp2 instruction.

tl.math.exp2 maps directly to a single ex2.approx.f32 PTX instruction, while tl.exp goes through libdevice __nv_expf which adds function call overhead and extra range checking.
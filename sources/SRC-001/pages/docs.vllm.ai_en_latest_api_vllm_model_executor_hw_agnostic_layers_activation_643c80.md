source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/hw_agnostic/layers/activation/
lastmod: 2026-09-23

#

`vllm.model_executor.hw_agnostic.layers.activation`

[¶](https://docs.vllm.ai#vllm.model_executor.hw_agnostic.layers.activation)

Classes:

-
–[SiluAndMul](https://docs.vllm.ai#vllm.model_executor.hw_agnostic.layers.activation.SiluAndMul)SwiGLU:

`x -> silu(x[:d]) * x[d:]`

where`d = x.shape[-1] // 2`

.

Functions:

-
–[get_act_and_mul_fn](https://docs.vllm.ai#vllm.model_executor.hw_agnostic.layers.activation.get_act_and_mul_fn)Build the hw-agnostic activation-and-mul op named

`act_fn_name`

.
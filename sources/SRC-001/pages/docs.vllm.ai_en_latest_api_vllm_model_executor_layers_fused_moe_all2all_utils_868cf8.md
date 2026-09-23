source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/all2all_utils/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.all2all_utils`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.all2all_utils)

Functions:

-
–[flashinfer_one_sided_dispatch_layout](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.all2all_utils.flashinfer_one_sided_dispatch_layout)Return the one-sided activation payload layout.

-
–[maybe_roundup_layer_hidden_size](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.all2all_utils.maybe_roundup_layer_hidden_size)Given layer hidden size and MoE configurations, round up hidden_size


##

`flashinfer_one_sided_dispatch_layout(hidden_dim, quant_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.all2all_utils.flashinfer_one_sided_dispatch_layout)

Return the one-sided activation payload layout.

## Source code in `vllm/model_executor/layers/fused_moe/all2all_utils.py`


##

`maybe_roundup_layer_hidden_size(hidden_size, act_dtype, moe_parallel_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.all2all_utils.maybe_roundup_layer_hidden_size)

Given layer hidden size and MoE configurations, round up hidden_size if necessary.

Parameters:

-

(`hidden_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.all2all_utils.maybe_roundup_layer_hidden_size(hidden_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Layer hidden-size

-

(`act_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.all2all_utils.maybe_roundup_layer_hidden_size(act_dtype))

) –[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)Data type of the layer activations.

-

(`moe_parallel_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.all2all_utils.maybe_roundup_layer_hidden_size(moe_parallel_config))

) –[FusedMoEParallelConfig](https://docs.vllm.ai/config/#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig)Fused MoE parallelization strategy configuration.


## Return

Rounded up hidden_size if rounding up is required based on the configs and all2all backend. Original hidden size otherwise.
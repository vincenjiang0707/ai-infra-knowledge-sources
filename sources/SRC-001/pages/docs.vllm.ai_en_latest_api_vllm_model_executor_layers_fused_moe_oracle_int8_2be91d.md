source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/oracle/int8/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.oracle.int8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int8)

Functions:

-
–[convert_to_int8_moe_kernel_format](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int8.convert_to_int8_moe_kernel_format)Convert INT8 MoE weights to backend-specific kernel format.

-
–[map_int8_backend](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int8.map_int8_backend)Map user's MoEBackend to Int8MoeBackend.

-
–[select_int8_moe_backend](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int8.select_int8_moe_backend)Select the primary Int8 MoE backend.


##

`_get_priority_backends(moe_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int8._get_priority_backends)

Get available backends in priority order based on platform and config.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int8.py`


##

`_humming_int8_weight_schema(weight, weight_scale)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int8._humming_int8_weight_schema)

Build the humming compressed-tensors int8 schema from the canonical on-device tensors; humming does the signed-int8 -> native conversion.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int8.py`


##

`convert_to_int8_moe_kernel_format(int8_backend, w13, w2, layer=None, w13_scale=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int8.convert_to_int8_moe_kernel_format)

Convert INT8 MoE weights to backend-specific kernel format.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int8.py`


##

`map_int8_backend(runner_backend)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int8.map_int8_backend)

Map user's MoEBackend to Int8MoeBackend.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int8.py`


##

`select_int8_moe_backend(config, weight_key=kInt8StaticChannelSym, activation_key=kInt8DynamicTokenSym)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int8.select_int8_moe_backend)

Select the primary Int8 MoE backend. Note: Shape-specific fallbacks may still occur at runtime.
source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/humming/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.quantization.utils.humming`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.humming)

Humming quantization integration.

Modules:

-
–[activation](https://docs.vllm.ai/activation/#vllm.model_executor.layers.quantization.utils.humming.activation)MoE activation expressions for Humming input processing.

-
–[linear](https://docs.vllm.ai/linear/#vllm.model_executor.layers.quantization.utils.humming.linear)Prepare and execute Humming linear layers.

-
–[moe](https://docs.vllm.ai/moe/#vllm.model_executor.layers.quantization.utils.humming.moe)Configure, prepare weights for, and assemble Humming MoE kernels.

-
–[schema](https://docs.vllm.ai/schema/#vllm.model_executor.layers.quantization.utils.humming.schema)Map Humming schemas and handle shared checkpoint quantization settings.


Functions:

-
–[convert_linear_layer_to_humming_standard](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.humming.convert_linear_layer_to_humming_standard)Rename/reshape a linear layer's quantized params (the canonical MPLinear

-
–[convert_to_humming_moe_kernel_format](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.humming.convert_to_humming_moe_kernel_format)Convert MoE weights from checkpoint format to Humming kernel format.

-
–[select_humming_moe_experts](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.humming.select_humming_moe_experts)Select the primary Humming MoE Experts class


##

`convert_linear_layer_to_humming_standard(layer, name_map)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.humming.convert_linear_layer_to_humming_standard)

Rename/reshape a linear layer's quantized params (the canonical MPLinear layout: `weight_packed`

int32 + `weight_scale`

) into the parameter names and layout humming's weight schema expects (`weight`

/ `weight_scale`

).

## Source code in `vllm/model_executor/layers/quantization/utils/humming/linear.py`


##

`convert_to_humming_moe_kernel_format(layer, quant_config=None, sublayer_configs=None, weight_schema=None, input_schema=None, force_weight_schema=None, allow_input_schema_fallback=True)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.humming.convert_to_humming_moe_kernel_format)

Convert MoE weights from checkpoint format to Humming kernel format.

This function processes weights for each sublayer (w13, w2) by: 1. Converting from checkpoint format to humming format if needed 2. Force requanting if a different quantization schema is specified 3. Preparing layer metadata for the Humming kernel 4. Transforming weights for inference

Parameters:

-

(`layer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.humming.convert_to_humming_moe_kernel_format(layer))

) –[RoutedExperts](https://docs.vllm.ai/fused_moe/routed_experts/#vllm.model_executor.layers.fused_moe.routed_experts.RoutedExperts)The RoutedExperts layer containing weights to process

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.humming.convert_to_humming_moe_kernel_format(quant_config))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)| None`None`

) –Optional quantization config dict. Required if weight_schema or input_schema are None. Used to build schemas via BaseWeightSchema.from_config().

-

(`sublayer_configs`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.humming.convert_to_humming_moe_kernel_format(sublayer_configs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Optional configuration dict for each sublayer (w13, w2). Each config must have "shape_n" and "shape_k" keys. If None, configs are built from layer.moe_config properties.

-

(`weight_schema`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.humming.convert_to_humming_moe_kernel_format(weight_schema))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)| None`None`

) –Optional initial weight quantization schema. If None, built from quant_config.

-

(`input_schema`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.humming.convert_to_humming_moe_kernel_format(input_schema))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)| None`None`

) –Optional initial input quantization schema. If None, built from quant_config or env vars.

-

(`force_weight_schema`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.humming.convert_to_humming_moe_kernel_format(force_weight_schema))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)| None`None`

) –Optional schema to force requantization to

-

(`allow_input_schema_fallback`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.humming.convert_to_humming_moe_kernel_format(allow_input_schema_fallback))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Whether incompatible input schemas may be replaced.


## Side effects

- Modifies layer parameters in place
- Sets layer.weight_schemas and layer.input_schemas
- Sets layer.humming_configs for quant config construction

## Source code in `vllm/model_executor/layers/quantization/utils/humming/moe.py`


|
|

##

`select_humming_moe_experts(config, weight_key, activation_key)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.humming.select_humming_moe_experts)

Select the primary Humming MoE Experts class Note: Shape-specific fallbacks may still occur at runtime.
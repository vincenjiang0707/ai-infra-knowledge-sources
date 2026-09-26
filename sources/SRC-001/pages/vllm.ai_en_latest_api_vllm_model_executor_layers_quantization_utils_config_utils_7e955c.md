source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/config_utils/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.quantization.utils.config_utils`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.config_utils)

Functions:

-
–[find_matching_patterns](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.config_utils.find_matching_patterns)Return matching patterns for a layer or each shard of a fused layer.

-
–[get_layer_name_after_index](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.config_utils.get_layer_name_after_index)Return the suffix following the final numeric component of a layer name.

-
–[get_quark_ocp_mx_group_size](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.config_utils.get_quark_ocp_mx_group_size)Return the OCP MX group size for a quantized Quark linear layer.

-
–[is_equal_or_regex_match](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.config_utils.is_equal_or_regex_match)Checks whether a value is exactly equal or a regex match for target

-
–[is_shared_expert_quant_fse_compatible](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.config_utils.is_shared_expert_quant_fse_compatible)Check whether quantization permits fused shared-expert execution.


##

`find_matching_patterns(layer_name, patterns, fused_mapping=MappingProxyType({}), use_fnmatch=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.config_utils.find_matching_patterns)

Return matching patterns for a layer or each shard of a fused layer.

A pattern matching the fused layer directly takes precedence. Otherwise, return one set of matching patterns for every shard.

## Source code in `vllm/model_executor/layers/quantization/utils/config_utils.py`


##

`get_layer_name_after_index(layer_name)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.config_utils.get_layer_name_after_index)

Return the suffix following the final numeric component of a layer name.

## Source code in `vllm/model_executor/layers/quantization/utils/config_utils.py`


##

`get_quark_ocp_mx_group_size(quant_config, layer_name)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.config_utils.get_quark_ocp_mx_group_size)

Return the OCP MX group size for a quantized Quark linear layer.

## Source code in `vllm/model_executor/layers/quantization/utils/config_utils.py`


##

`is_equal_or_regex_match(value, target, check_contains=False, use_fnmatch=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.config_utils.is_equal_or_regex_match)

Checks whether a value is exactly equal or a regex match for target if target starts with 're:'. If check_contains is set to True, additionally checks if the target string is contained within the value. If use_fnmatch is set, supports shell-style patterns in target.

## Source code in `vllm/model_executor/layers/quantization/utils/config_utils.py`


##

`is_shared_expert_quant_fse_compatible(quant_config, expert_prefix, shared_expert_prefix, projection_names=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.config_utils.is_shared_expert_quant_fse_compatible)

Check whether quantization permits fused shared-expert execution.

Parameters:

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.config_utils.is_shared_expert_quant_fse_compatible(quant_config))

) –[QuantizationConfig](https://docs.vllm.ai/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)| NoneModel quantization configuration.

-

(`expert_prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.config_utils.is_shared_expert_quant_fse_compatible(expert_prefix))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Routed-expert module prefix.

-

(`shared_expert_prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.config_utils.is_shared_expert_quant_fse_compatible(shared_expert_prefix))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Shared-expert module prefix.

-

(`projection_names`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.config_utils.is_shared_expert_quant_fse_compatible(projection_names))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –Shared-expert projection names.


Returns:

## Source code in `vllm/model_executor/layers/quantization/utils/config_utils.py`


|
|
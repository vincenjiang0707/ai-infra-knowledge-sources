source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/compressed_tensors/utils/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.quantization.compressed_tensors.utils`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.utils)

Functions:

-
–[find_matched_target](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.utils.find_matched_target)Helper function to look up which "target" in the compressed-tensors


##

`_find_first_match(value, targets, check_contains=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.utils._find_first_match)

Returns first element of target that matches value either exactly or as a regex after 're:'. If check_contains is set to True, additionally checks if the target string is contained within the value.

Parameters:

-

(`value`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.utils._find_first_match(value))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)string to compare the list of targets against

-

(`targets`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.utils._find_first_match(targets))

) –[Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]list of targets to match the layer against

-

(`check_contains`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.utils._find_first_match(check_contains))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –whether or not to do a substring match


## Source code in `vllm/model_executor/layers/quantization/compressed_tensors/utils.py`


##

`_match_fused_layer(layer_name, target_layers, fused_mapping)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.utils._match_fused_layer)

Match a fused layer name to its corresponding individual layer in target_layers. Returns first value in fused_mapping which matches targets

Implements an "all" matching strategy where a fused layer matches iff "all" of its components match

Parameters:

-

(`layer_name`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.utils._match_fused_layer(layer_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)layer name

-

(`target_layers`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.utils._match_fused_layer(target_layers))

) –[Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]list of targets to match the layer against

-

(`fused_mapping`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.utils._match_fused_layer(fused_mapping))

) –[Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]map from fused layer names to its components


Examples:

layer_name = "model.layers.0.self_attn.qkv_proj" target_layers = ["model.layers.0.self_attn.q_proj", "model.layers.0.self_attn.k_proj", "model.layers.0.self_attn.v_proj"]

## Source code in `vllm/model_executor/layers/quantization/compressed_tensors/utils.py`


##

`find_matched_target(layer_name, module, targets, fused_mapping=MappingProxyType({}))`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.utils.find_matched_target)

Helper function to look up which "target" in the compressed-tensors config that a layer corresponds to.

Recall that a compressed-tensors configs has a concept of config_groups, where each layer can be quantized with a different scheme.

targets in each config_group will be a list of either layer names (or regexes corresponding to layer names) or names of torch Modules.

First, we try to match the layer_name with a target Second, we try to match the module's name with a target Third, we try to map the layer_name to a list of fused module names. *All* component module names must match in order for a match to be successful. A successful match returns the first component target

Parameters:

-

(`layer_name`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.utils.find_matched_target(layer_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| Nonelayer name

-

(`module`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.utils.find_matched_target(module))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)torch.nn.Module

-

(`targets`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.utils.find_matched_target(targets))

) –[Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]list of targets to match the layer against

-

(`fused_mapping`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.utils.find_matched_target(fused_mapping))

, default:[Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]

) –[MappingProxyType](https://docs.python.org/3/library/types.html#types.MappingProxyType)({})map from fused layer names to its components
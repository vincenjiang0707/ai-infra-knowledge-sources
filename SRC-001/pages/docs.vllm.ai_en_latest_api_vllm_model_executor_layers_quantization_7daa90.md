source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.quantization`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization)

Modules:

-
–[auto_awq](https://docs.vllm.ai/auto_awq/#vllm.model_executor.layers.quantization.auto_awq) -
–[auto_gptq](https://docs.vllm.ai/auto_gptq/#vllm.model_executor.layers.quantization.auto_gptq) -
–[base_config](https://docs.vllm.ai/base_config/#vllm.model_executor.layers.quantization.base_config) -
–[compressed_tensors](https://docs.vllm.ai/compressed_tensors/#vllm.model_executor.layers.quantization.compressed_tensors) -
–[experts_int8](https://docs.vllm.ai/experts_int8/#vllm.model_executor.layers.quantization.experts_int8) -
–[fbgemm_fp8](https://docs.vllm.ai/fbgemm_fp8/#vllm.model_executor.layers.quantization.fbgemm_fp8) -
–[fp8](https://docs.vllm.ai/fp8/#vllm.model_executor.layers.quantization.fp8) -
–[fp_quant](https://docs.vllm.ai/fp_quant/#vllm.model_executor.layers.quantization.fp_quant) -
–[humming](https://docs.vllm.ai/humming/#vllm.model_executor.layers.quantization.humming) -
–[inc](https://docs.vllm.ai/inc/#vllm.model_executor.layers.quantization.inc) -
–[input_quant_fp8](https://docs.vllm.ai/input_quant_fp8/#vllm.model_executor.layers.quantization.input_quant_fp8) -
–[kv_cache](https://docs.vllm.ai/kv_cache/#vllm.model_executor.layers.quantization.kv_cache) -
–[modelopt](https://docs.vllm.ai/modelopt/#vllm.model_executor.layers.quantization.modelopt) -
–[moe_wna16](https://docs.vllm.ai/moe_wna16/#vllm.model_executor.layers.quantization.moe_wna16) -
–[mxfp4](https://docs.vllm.ai/mxfp4/#vllm.model_executor.layers.quantization.mxfp4) -
–[online](https://docs.vllm.ai/online/#vllm.model_executor.layers.quantization.online) -
–[quark](https://docs.vllm.ai/quark/#vllm.model_executor.layers.quantization.quark) -
–[qutlass_utils](https://docs.vllm.ai/qutlass_utils/#vllm.model_executor.layers.quantization.qutlass_utils) -
–[torchao](https://docs.vllm.ai/torchao/#vllm.model_executor.layers.quantization.torchao) -
–[turboquant](https://docs.vllm.ai/turboquant/#vllm.model_executor.layers.quantization.turboquant)TurboQuant: KV-cache quantization for vLLM.

-
–[utils](https://docs.vllm.ai/utils/#vllm.model_executor.layers.quantization.utils)

Classes:

-
–[QuantizationConfig](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig)Base class for quantization configs.


Functions:

-
–[register_quantization_config](https://docs.vllm.ai#vllm.model_executor.layers.quantization.register_quantization_config)Register a customized vllm quantization config.

-
–[resolve_quant_method](https://docs.vllm.ai#vllm.model_executor.layers.quantization.resolve_quant_method)Return the checkpoint method with configured online quantization.


##

`QuantizationConfig`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for quantization configs.

Methods:

-
–[apply_vllm_mapper](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.apply_vllm_mapper)Interface for models to update module names referenced in

-
–[from_config](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.from_config)Create a config class from the model's quantization config.

-
–[get_cache_scale_mapper](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_cache_scale_mapper)Mapping from checkpoint KV-cache scale names to vLLM scale names.

-
–[get_checkpoint_weight_mapper](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_checkpoint_weight_mapper)Discard activation-order metadata unused by supported kernels.

-
–[get_config_filenames](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_config_filenames)List of filenames to search for in the model directory.

-
–[get_from_keys](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_from_keys)Get a value from the model's quantization config.

-
–[get_from_keys_or](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_from_keys_or)Get an optional value from the model's quantization config.

-
–[get_min_capability](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_min_capability)Minimum GPU capability to support the quantization method.

-
–[get_name](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_name)Name of the quantization method.

-
–[get_quant_method](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_quant_method)Get the quantize method to use for the quantized layer, from the

-
–[get_supported_act_dtypes](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_supported_act_dtypes)List of supported activation dtypes.

-
–[maybe_update_config](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.maybe_update_config)Interface to update values after config initialization.

-
–[override_quantization_method](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.override_quantization_method)Detects if this quantization method can support a given checkpoint


## Source code in `vllm/model_executor/layers/quantization/base_config.py`


|
|

###

`_ignore_unexpected_suffixes = ('.q_scale', '.k_scale', '.v_scale', '.q_zero_point', '.k_zero_point', '.v_zero_point')`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig._ignore_unexpected_suffixes)

Suffixes of quantization parameters that may be present in the checkpoint but not in the model, and should be ignored if unexpected during loading. These are used after remapping, so should be in vLLM format (e.g. .q_scale, not .q.scale).

###

`apply_vllm_mapper(hf_to_vllm_mapper)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.apply_vllm_mapper)

Interface for models to update module names referenced in quantization configs in order to reflect the vllm model structure

Parameters:

-

(`hf_to_vllm_mapper`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.apply_vllm_mapper(hf_to_vllm_mapper))

) –[WeightsMapper](https://docs.vllm.ai/models/utils/#vllm.model_executor.models.utils.WeightsMapper)maps from hf model structure (the assumed structure of the qconfig) to vllm model structure


## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`from_config(config)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.from_config)

Create a config class from the model's quantization config.

###

`get_cache_scale_mapper()`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_cache_scale_mapper)

Mapping from checkpoint KV-cache scale names to vLLM scale names.

Returning a mapper here causes `AutoWeightsLoader`

to apply it to the weight stream automatically; individual model `load_weights`

methods do not need to know about KV-cache scales.

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`get_checkpoint_weight_mapper()`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_checkpoint_weight_mapper)

Discard activation-order metadata unused by supported kernels.

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`get_config_filenames()`

`abstractmethod`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_config_filenames)

List of filenames to search for in the model directory.

###

`get_from_keys(config, keys)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_from_keys)

Get a value from the model's quantization config.

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`get_from_keys_or(config, keys, default)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_from_keys_or)

Get an optional value from the model's quantization config.

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`get_min_capability()`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_min_capability)

Minimum GPU capability to support the quantization method.

E.g., 70 for Volta, 75 for Turing, 80 for Ampere. This requirement is due to the custom CUDA kernels used by the quantization method.

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`get_name()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_name)

###

`get_quant_method(layer, prefix)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_quant_method)

Get the quantize method to use for the quantized layer, from the pre-quantized checkpoint quant_method.

Parameters:

-

(`layer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_quant_method(layer))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)The layer for the quant method.

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_quant_method(prefix))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The full name of the layer in the state dict


Returns: The quantize method. None if the given layer doesn't support quant method.

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`get_supported_act_dtypes()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.get_supported_act_dtypes)

###

`maybe_update_config(model_name, hf_config=None, revision=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.maybe_update_config)

Interface to update values after config initialization.

Parameters:

-

(`model_name`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.maybe_update_config(model_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The name of the model

-

(`hf_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.maybe_update_config(hf_config))`PretrainedConfig | None`

, default:`None`

) –The Hugging Face config of the model

-

(`revision`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.maybe_update_config(revision))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The revision of the model


Returns:

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`override_quantization_method(hf_quant_cfg, user_quant, hf_config=None)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.override_quantization_method)

Detects if this quantization method can support a given checkpoint format by overriding the user specified quantization method -- this method should only be overwritten by subclasses in exceptional circumstances.

Parameters:

-

(`hf_quant_cfg`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.override_quantization_method(hf_quant_cfg))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]The checkpoint's quantization config dict.

-

(`user_quant`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.override_quantization_method(user_quant))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe user-specified quantization method string.

-

(`hf_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.QuantizationConfig.override_quantization_method(hf_config))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`None`

) –The HuggingFace model config object (e.g. for model_type checks). May be None if not available.


## Source code in `vllm/model_executor/layers/quantization/base_config.py`


##

`register_quantization_config(quantization)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.register_quantization_config)

Register a customized vllm quantization config.

When a quantization method is not supported by vllm, you can register a customized quantization config to support it.

Parameters:

Examples:

>>> from vllm.model_executor.layers.quantization import (
... register_quantization_config,
... )
>>> from vllm.model_executor.layers.quantization import get_quantization_config
>>> from vllm.model_executor.layers.quantization.base_config import (
... QuantizationConfig,
... )
>>>
>>> @register_quantization_config("my_quant")
... class MyQuantConfig(QuantizationConfig):
... pass
>>>
>>> get_quantization_config("my_quant")
<class 'MyQuantConfig'>


## Source code in `vllm/model_executor/layers/quantization/__init__.py`


##

`resolve_quant_method(quant_config, layer, prefix)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.resolve_quant_method)

Return the checkpoint method with configured online quantization.
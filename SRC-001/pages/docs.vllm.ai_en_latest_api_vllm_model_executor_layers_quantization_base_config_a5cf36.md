source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/base_config/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.quantization.base_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config)

Classes:

-
–[QuantizationConfig](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)Base class for quantization configs.

-
–[QuantizeMethodBase](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase)Base class for different quantized methods.


Functions:

-
–[method_has_implemented_embedding](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.method_has_implemented_embedding)Not all quant methods have embedding implemented, so we need to check that

-
–[resolve_quant_method](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.resolve_quant_method)Return the checkpoint method with configured online quantization.


##

`QuantizationConfig`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for quantization configs.

Methods:

-
–[apply_vllm_mapper](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.apply_vllm_mapper)Interface for models to update module names referenced in

-
–[from_config](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.from_config)Create a config class from the model's quantization config.

-
–[get_cache_scale_mapper](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_cache_scale_mapper)Mapping from checkpoint KV-cache scale names to vLLM scale names.

-
–[get_checkpoint_weight_mapper](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_checkpoint_weight_mapper)Discard activation-order metadata unused by supported kernels.

-
–[get_config_filenames](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_config_filenames)List of filenames to search for in the model directory.

-
–[get_from_keys](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_from_keys)Get a value from the model's quantization config.

-
–[get_from_keys_or](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_from_keys_or)Get an optional value from the model's quantization config.

-
–[get_min_capability](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_min_capability)Minimum GPU capability to support the quantization method.

-
–[get_name](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_name)Name of the quantization method.

-
–[get_quant_method](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_quant_method)Get the quantize method to use for the quantized layer, from the

-
–[get_supported_act_dtypes](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_supported_act_dtypes)List of supported activation dtypes.

-
–[maybe_update_config](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.maybe_update_config)Interface to update values after config initialization.

-
–[override_quantization_method](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.override_quantization_method)Detects if this quantization method can support a given checkpoint


## Source code in `vllm/model_executor/layers/quantization/base_config.py`


|
|

###

`_ignore_unexpected_suffixes = ('.q_scale', '.k_scale', '.v_scale', '.q_zero_point', '.k_zero_point', '.v_zero_point')`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig._ignore_unexpected_suffixes)

Suffixes of quantization parameters that may be present in the checkpoint but not in the model, and should be ignored if unexpected during loading. These are used after remapping, so should be in vLLM format (e.g. .q_scale, not .q.scale).

###

`apply_vllm_mapper(hf_to_vllm_mapper)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.apply_vllm_mapper)

Interface for models to update module names referenced in quantization configs in order to reflect the vllm model structure

Parameters:

-

(`hf_to_vllm_mapper`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.apply_vllm_mapper(hf_to_vllm_mapper))

) –[WeightsMapper](https://docs.vllm.ai/models/utils/#vllm.model_executor.models.utils.WeightsMapper)maps from hf model structure (the assumed structure of the qconfig) to vllm model structure


## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`from_config(config)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.from_config)

Create a config class from the model's quantization config.

###

`get_cache_scale_mapper()`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_cache_scale_mapper)

Mapping from checkpoint KV-cache scale names to vLLM scale names.

Returning a mapper here causes `AutoWeightsLoader`

to apply it to the weight stream automatically; individual model `load_weights`

methods do not need to know about KV-cache scales.

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`get_checkpoint_weight_mapper()`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_checkpoint_weight_mapper)

Discard activation-order metadata unused by supported kernels.

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`get_config_filenames()`

`abstractmethod`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_config_filenames)

List of filenames to search for in the model directory.

###

`get_from_keys(config, keys)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_from_keys)

Get a value from the model's quantization config.

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`get_from_keys_or(config, keys, default)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_from_keys_or)

Get an optional value from the model's quantization config.

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`get_min_capability()`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_min_capability)

Minimum GPU capability to support the quantization method.

E.g., 70 for Volta, 75 for Turing, 80 for Ampere. This requirement is due to the custom CUDA kernels used by the quantization method.

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`get_name()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_name)

###

`get_quant_method(layer, prefix)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_quant_method)

Get the quantize method to use for the quantized layer, from the pre-quantized checkpoint quant_method.

Parameters:

-

(`layer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_quant_method(layer))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)The layer for the quant method.

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_quant_method(prefix))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The full name of the layer in the state dict


Returns: The quantize method. None if the given layer doesn't support quant method.

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`get_supported_act_dtypes()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_supported_act_dtypes)

###

`maybe_update_config(model_name, hf_config=None, revision=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.maybe_update_config)

Interface to update values after config initialization.

Parameters:

-

(`model_name`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.maybe_update_config(model_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The name of the model

-

(`hf_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.maybe_update_config(hf_config))`PretrainedConfig | None`

, default:`None`

) –The Hugging Face config of the model

-

(`revision`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.maybe_update_config(revision))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The revision of the model


Returns:

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`override_quantization_method(hf_quant_cfg, user_quant, hf_config=None)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.override_quantization_method)

Detects if this quantization method can support a given checkpoint format by overriding the user specified quantization method -- this method should only be overwritten by subclasses in exceptional circumstances.

Parameters:

-

(`hf_quant_cfg`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.override_quantization_method(hf_quant_cfg))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]The checkpoint's quantization config dict.

-

(`user_quant`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.override_quantization_method(user_quant))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe user-specified quantization method string.

-

(`hf_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.override_quantization_method(hf_config))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`None`

) –The HuggingFace model config object (e.g. for model_type checks). May be None if not available.


## Source code in `vllm/model_executor/layers/quantization/base_config.py`


##

`QuantizeMethodBase`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for different quantized methods.

Methods:

-
–[apply](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase.apply)Apply the weights in layer to the input tensor.

-
–[create_weights](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase.create_weights)Create weights for a layer.

-
–[embedding](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase.embedding)Gather embeddings in the layer based on indices in the input tensor.

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase.process_weights_after_loading)Process the weight after loading.

-
–[tie_weights](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase.tie_weights)Tie

`layer`

's weight to`embed_tokens`

' weight.

Attributes:

-
([requires_device_loading](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase.requires_device_loading)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether post-load processing requires parameters on the target device.

-
([supports_pre_processed_weights](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase.supports_pre_processed_weights)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether

`process_weights_after_loading`

supports running under -
([uses_meta_device](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase.uses_meta_device)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether this method creates weights on meta device for online quantization.


## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`requires_device_loading = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase.requires_device_loading)

Whether post-load processing requires parameters on the target device.

###

`supports_pre_processed_weights = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase.supports_pre_processed_weights)

Whether `process_weights_after_loading`

supports running under `weights_already_processed`

. Methods must skip tensor transforms in that mode; the loader driver rejects methods that do not declare support.

###

`uses_meta_device = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase.uses_meta_device)

Whether this method creates weights on meta device for online quantization. When True, weights are created on meta device and quantized layer-wise in process_weights_after_loading, reducing peak memory during loading.

###

`apply(layer, *args, **kwargs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase.apply)

Apply the weights in layer to the input tensor.

Expects create_weights to have been called before on the layer.

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`create_weights(layer, *weight_args, **extra_weight_attrs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase.create_weights)

Create weights for a layer.

The weights will be set as attributes of the layer.

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`embedding(layer, *args, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase.embedding)

Gather embeddings in the layer based on indices in the input tensor.

Expects create_weights to have been called before on the layer.

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


###

`process_weights_after_loading(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase.process_weights_after_loading)

Process the weight after loading.

This can be used for example, to transpose weights for computation.

###

`tie_weights(layer, embed_tokens)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase.tie_weights)

Tie `layer`

's weight to `embed_tokens`

' weight.

The default shares the weight tensor, which is the standard behavior for tied word embeddings and matches what `ParallelLMHead.tie_weights`

did directly before quantization methods became responsible for it. Quantization methods that need special weight handling (e.g. repacked weights) override this.

Expects create_weights to have been called before on the layer.

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


##

`method_has_implemented_embedding(method_class)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.method_has_implemented_embedding)

Not all quant methods have embedding implemented, so we need to check that it exists for our given method. We check this by making sure the function has been changed from the base implementation.

## Source code in `vllm/model_executor/layers/quantization/base_config.py`


##

`resolve_quant_method(quant_config, layer, prefix)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.base_config.resolve_quant_method)

Return the checkpoint method with configured online quantization.
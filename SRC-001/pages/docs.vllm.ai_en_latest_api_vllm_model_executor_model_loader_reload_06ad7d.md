source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/reload/
lastmod: 2026-09-23

Layerwise weight reloading utilities for vLLM.

This module provides functionality to reload model weights layer-by-layer, which is useful for weight updates without full model reconstruction.

Limitations: 1. Composition with CPU offloading has not been implemented 2. Tied parameters will only reflect processing from one of the parent layers (for example, only processing from embed_tokens will have an effect) 3. This design assumes that the number of weights loaded from disk is the same as the number of weights created at model init time. This is not true for quant methods which (1) pad weights or (2) load qkv weights into the same parameter. Both of these cases are non-issues for today's quant methods, but future quantizations may cause reloading to fail

Modules:

Functions:

##

`finalize_layerwise_processing(model, model_config)`


Apply processing to any layers which were not layerwise processed during loading. This includes attention layers and layers which have weight elements which are not loaded (due to padding).

This function should be applied after `initialize_layerwise_reload`

is applied unwrap the layerwise weight loaders.

Parameters:

-
### `model`


([Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

) – model to finalize processing for

-
### `model_config`


([ModelConfig](../../../config/#vllm.config.ModelConfig)

) – config needed for applying processing to attention layers


## Source code in `vllm/model_executor/model_loader/reload/layerwise.py`


| def finalize_layerwise_processing(model: torch.nn.Module, model_config: ModelConfig):
"""Apply processing to any layers which were not layerwise processed during loading.
This includes attention layers and layers which have weight elements which are not
loaded (due to padding).
This function should be applied after `initialize_layerwise_reload` is applied
unwrap the layerwise weight loaders.
Args:
model: model to finalize processing for
model_config: config needed for applying processing to attention layers
"""
if hasattr(model, "_original_do_torchao_reload"):
model._do_torchao_reload = model._original_do_torchao_reload
deferred_attn: list[tuple[torch.nn.Module, LayerReloadingInfo]] = []
for layer in model.modules():
info = get_layerwise_info(layer)
if not info.can_load():
info.reset()
continue
# Deferred attention-like layers are processed after all other layers
if is_deferred_attention_layer(layer):
deferred_attn.append((layer, info))
continue
# No weights were loaded
if info.load_numel <= 0:
# first load: checkpoint did not contain weights for this layer
if info.kernel_tensors is None:
_layerwise_process(layer, info)
continue
# reloading: place kernel tensors back as a fallback. Always place, even
# when nothing is loadable (load_numel_total == 0), so parameter-alias
# buffers on such layers are restored rather than left deleted.
if info.load_numel_total > 0: # type: ignore[operator]
logger.warning("%s: Failed to load weights", layer.__class__.__name__)
_place_kernel_tensors(layer, info)
# Process non-attention layers which did not load all elements. This can happen
# if the created weight has extra padding elements which are not loaded
# Having too many of these delayed layers can lead to excess memory usage
# see Limitations(4)
elif info.load_numel > 0 and info.load_numel < info.load_numel_total: # type: ignore[operator]
logger.debug("%s: Delayed processing", layer.__class__.__name__)
_layerwise_process(layer, info)
info.reset()
# Process attention layers after all other layers are done
for layer, info in deferred_attn:
_finalize_attention_layer(layer, info, model_config)
info.reset()
LOADING_LAYERS.clear()
|

##

`initialize_layerwise_reload(model)`


Set up layerwise weight loading with deferred processing.

Must be called after `record_metadata_for_reloading`

. This function: 1. Saves current kernel tensors for later copying 2. Restores layer parameters/buffers from metadata (on meta device) 3. Wraps weight loaders to defer processing until all weights are loaded

When all weights for a layer are loaded, the wrapped loaders will: 1. Materialize the layer onto the target device 2. Load all cached weights 3. Run quantization processing if applicable 4. Copy processed values back to original tensor storage

## Source code in `vllm/model_executor/model_loader/reload/layerwise.py`


| @torch.no_grad()
def initialize_layerwise_reload(model: torch.nn.Module):
"""Set up layerwise weight loading with deferred processing.
Must be called after `record_metadata_for_reloading`. This function:
1. Saves current kernel tensors for later copying
2. Restores layer parameters/buffers from metadata (on meta device)
3. Wraps weight loaders to defer processing until all weights are loaded
When all weights for a layer are loaded, the wrapped loaders will:
1. Materialize the layer onto the target device
2. Load all cached weights
3. Run quantization processing if applicable
4. Copy processed values back to original tensor storage
"""
# disable torchao reloading to avoid infinite recursion
model._original_do_torchao_reload = getattr(model, "_do_torchao_reload", False)
model._do_torchao_reload = False
for layer in model.modules():
info = get_layerwise_info(layer)
# Skip if the layer has already been initialized
if info.can_load():
continue
# Save current tensors for later copying
info.kernel_tensors = get_layer_params_buffers(layer)
# snapshot now: restore_layer_on_meta drops alias buffers from the live set
info.kernel_non_persistent_buffers = set(layer._non_persistent_buffers_set)
# Restore layer parameters/buffers onto meta device
restore_layer_on_meta(layer, info)
# Wrap weight loaders to buffer loading
initialize_online_processing(layer)
|

Record layer metadata needed for later reloading.

Stores parameter and buffer metadata as meta tensors for restoration. Must be called before `initialize_layerwise_reload`

.

## Source code in `vllm/model_executor/model_loader/reload/layerwise.py`


| def record_metadata_for_reloading(model: torch.nn.Module):
"""Record layer metadata needed for later reloading.
Stores parameter and buffer metadata as meta tensors for restoration.
Must be called before `initialize_layerwise_reload`.
"""
for layer in model.modules():
info = get_layerwise_info(layer)
info.restore_metadata = capture_layer_to_meta(layer)
info.restore_device = torch.get_default_device()
|

##

`support_quantized_model_reload_from_hp_weights(original_load_weights)`


Decorator for `load_weights`

method for AutoWeightsLoader.load_weights to support reloading high precision (bfloat16/float16/float32) weight for an already quantized model, this involves restoring the weights to a high precision weights and then online quantize the weights.

Only applies to torchao quantized models. Assumes that all model weights are loaded within a single weights iterator (cannot perform batched updates)

## Source code in `vllm/model_executor/model_loader/reload/torchao_decorator.py`


| def support_quantized_model_reload_from_hp_weights(original_load_weights: FunctionType):
"""Decorator for `load_weights` method for AutoWeightsLoader.load_weights to support
reloading high precision (bfloat16/float16/float32) weight for an already quantized
model, this involves restoring the weights to a high precision weights and
then online quantize the weights.
Only applies to torchao quantized models. Assumes that all model weights are
loaded within a single weights iterator (cannot perform batched updates)
"""
@wraps(original_load_weights)
def patched_model_load_weights(
self: "AutoWeightsLoader",
weights: Iterable[tuple[str, torch.Tensor]],
*args,
**kwargs,
):
model = self.module
if not getattr(model, "_do_torchao_reload", False):
return original_load_weights(self, weights, *args, **kwargs)
initialize_layerwise_reload(model)
loaded_weights = original_load_weights(self, weights, *args, **kwargs)
finalize_layerwise_reload(model, model._model_config)
return loaded_weights
return patched_model_load_weights
|
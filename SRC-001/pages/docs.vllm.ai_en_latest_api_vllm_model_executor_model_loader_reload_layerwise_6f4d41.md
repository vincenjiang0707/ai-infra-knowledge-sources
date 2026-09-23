source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/reload/layerwise/
lastmod: 2026-09-23

#

`vllm.model_executor.model_loader.reload.layerwise`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.layerwise)

Functions:

-
–[finalize_layerwise_processing](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.layerwise.finalize_layerwise_processing)Apply processing to any layers which were not layerwise processed during loading.

-
–[get_layerwise_info](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.layerwise.get_layerwise_info)Get information related to restoring and layerwise processing. If no previous

-
–[initialize_layerwise_reload](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.layerwise.initialize_layerwise_reload)Set up layerwise weight loading with deferred processing.

-
–[record_metadata_for_reloading](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.layerwise.record_metadata_for_reloading)Record layer metadata needed for later reloading.


##

`_copy_and_restore_kernel_tensors(layer, info)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.layerwise._copy_and_restore_kernel_tensors)

Copy processed values into original kernel tensor storage and restore kernel tensor references on the layer. Preserves cudagraph references.

## Source code in `vllm/model_executor/model_loader/reload/layerwise.py`


##

`_get_original_loader(tensor)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.layerwise._get_original_loader)

Return the weight loader with any layerwise wrappers removed.

## Source code in `vllm/model_executor/model_loader/reload/layerwise.py`


##

`_layerwise_process(layer, info)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.layerwise._layerwise_process)

Finalize layer loading after all weights have been buffered.

This function: 1. Materializes the layer onto the target device 2. Loads all buffered weights 3. Runs quantization processing if applicable 4. Copies processed values back to original tensor storage

## Source code in `vllm/model_executor/model_loader/reload/layerwise.py`


##

`_reload_attention_scales(layer, info)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.layerwise._reload_attention_scales)

Load and process attention scale weights (k_scale, v_scale, etc.) during reload.

Assumes dtype/shapes of attention tensors do not change during processing, since we use .data.copy_() to preserve kernel tensor references.

## Source code in `vllm/model_executor/model_loader/reload/layerwise.py`


##

`_wrap_parameters_weight_loader(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.layerwise._wrap_parameters_weight_loader)

Wrap each parameter's weight loader.

## Source code in `vllm/model_executor/model_loader/reload/layerwise.py`


##

`finalize_layerwise_processing(model, model_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.layerwise.finalize_layerwise_processing)

Apply processing to any layers which were not layerwise processed during loading. This includes attention layers and layers which have weight elements which are not loaded (due to padding).

This function should be applied after `initialize_layerwise_reload`

is applied unwrap the layerwise weight loaders.

Parameters:

-

(`model`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.layerwise.finalize_layerwise_processing(model))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)model to finalize processing for

-

(`model_config`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.layerwise.finalize_layerwise_processing(model_config))

) –[ModelConfig](https://docs.vllm.ai/config/#vllm.config.ModelConfig)config needed for applying processing to attention layers


## Source code in `vllm/model_executor/model_loader/reload/layerwise.py`


##

`get_layerwise_info(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.layerwise.get_layerwise_info)

Get information related to restoring and layerwise processing. If no previous information existed, a new entry is constructed

## Source code in `vllm/model_executor/model_loader/reload/layerwise.py`


##

`initialize_layerwise_reload(model)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.layerwise.initialize_layerwise_reload)

Set up layerwise weight loading with deferred processing.

Must be called after `record_metadata_for_reloading`

. This function: 1. Saves current kernel tensors for later copying 2. Restores layer parameters/buffers from metadata (on meta device) 3. Wraps weight loaders to defer processing until all weights are loaded

When all weights for a layer are loaded, the wrapped loaders will: 1. Materialize the layer onto the target device 2. Load all cached weights 3. Run quantization processing if applicable 4. Copy processed values back to original tensor storage

## Source code in `vllm/model_executor/model_loader/reload/layerwise.py`


##

`initialize_online_processing(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.layerwise.initialize_online_processing)

Wrap a layer's weight loaders with online processing loaders. Called by either `initialize_layerwise_reload`

or an online quantization scheme, prevents double wrapping in the case of online quantization + reloading

Parameters:

## Source code in `vllm/model_executor/model_loader/reload/layerwise.py`


##

`make_online_process_loader(layer, param_name)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.layerwise.make_online_process_loader)

Create a wrapped weight loader that defers processing.

## Source code in `vllm/model_executor/model_loader/reload/layerwise.py`


|
|

##

`record_metadata_for_reloading(model)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.layerwise.record_metadata_for_reloading)

Record layer metadata needed for later reloading.

Stores parameter and buffer metadata as meta tensors for restoration. Must be called before `initialize_layerwise_reload`

.
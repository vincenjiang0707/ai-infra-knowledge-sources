source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/reload/utils/
lastmod: 2026-09-24

#

`vllm.model_executor.model_loader.reload.utils`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.utils)

Functions:

-
–[get_info_size](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.utils.get_info_size)Calculate the number of bytes used by loaded weights for a given layer.

-
–[get_layer_params_buffers](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.utils.get_layer_params_buffers)Get all parameters and buffers of a module as a tuple of dicts.

-
–[get_layer_size](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.utils.get_layer_size)Calculate total number of elements across loadable tensors in a layer.

-
–[get_layer_tensors](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.utils.get_layer_tensors)Get all parameters and buffers from a module as a dict.

-
–[get_tensor_load_numel](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.utils.get_tensor_load_numel)Count checkpoint elements, excluding padding declared by the weight creator.

-
–[has_device_tensors](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.utils.has_device_tensors)Return True if the loaded weights exist on an accelerator device.


##

`get_info_size(info)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.utils.get_info_size)

Calculate the number of bytes used by loaded weights for a given layer.

Parameters:

-

(`info`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.utils.get_info_size(info))`LayerReloadingInfo`

) –layerwise info to get size of


Returns:

-

–[int](https://docs.python.org/3/builtins/functions.html#int)number of bytes used by loaded weights


## Source code in `vllm/model_executor/model_loader/reload/utils.py`


##

`get_layer_params_buffers(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.utils.get_layer_params_buffers)

Get all parameters and buffers of a module as a tuple of dicts.

## Source code in `vllm/model_executor/model_loader/reload/utils.py`


##

`get_layer_size(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.utils.get_layer_size)

Calculate total number of elements across loadable tensors in a layer.

Excludes SKIP_LOAD_TENSORS (e.g. _expert_map) which are never loaded via weight_loader during layerwise reload.

## Source code in `vllm/model_executor/model_loader/reload/utils.py`


##

`get_layer_tensors(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.utils.get_layer_tensors)

Get all parameters and buffers from a module as a dict.

##

`get_tensor_load_numel(tensor)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.utils.get_tensor_load_numel)

Count checkpoint elements, excluding padding declared by the weight creator.

##

`has_device_tensors(bound_args)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.utils.has_device_tensors)

Return True if the loaded weights exist on an accelerator device.

Parameters:

-

(`bound_args`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.utils.has_device_tensors(bound_args))

) –[BoundArguments](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments)args to load weights


Returns:

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)True if weights are on accelerator device
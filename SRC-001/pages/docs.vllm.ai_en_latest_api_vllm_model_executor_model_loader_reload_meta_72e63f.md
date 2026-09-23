source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/reload/meta/
lastmod: 2026-09-23

#

`vllm.model_executor.model_loader.reload.meta`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.meta)

Functions:

-
–[get_numel_loaded](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.meta.get_numel_loaded)Determine how many elements would be loaded by a weight loader call.

-
–[materialize_layer](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.meta.materialize_layer)Materialize all meta tensors in a layer to actual tensors.

-
–[materialize_meta_tensor](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.meta.materialize_meta_tensor)Materialize a meta tensor into an actual tensor on the current device.

-
–[restore_layer_on_meta](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.meta.restore_layer_on_meta)Restore a layer to model format with tensors on the meta device.

-
–[to_meta_tensor](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.meta.to_meta_tensor)Convert a tensor to a meta tensor while preserving class and attributes.


##

`CopyCounter`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.meta.CopyCounter)

Bases: `TorchDispatchMode`


Tracks total number of elements modified with `copy_`

.

Useful for keeping track of weight loading where underlying weights can be arbitrarily transformed (such as with `narrow`

) before calling copy.

Note: Assumes that copy kwargs are not used.

## Source code in `vllm/model_executor/model_loader/reload/meta.py`


##

`get_numel_loaded(weight_loader, args)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.meta.get_numel_loaded)

Determine how many elements would be loaded by a weight loader call.

Parameters:

-

(`weight_loader`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.meta.get_numel_loaded(weight_loader))

) –[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)used to load weights

-

(`args`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.meta.get_numel_loaded(args))

) –[BoundArguments](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments)bound arguments to weight loader


Returns:

-

–[int](https://docs.python.org/3/builtins/functions.html#int)number of elements loaded by the weight loader, the return value of the

-

–[object](https://docs.python.org/3/builtins/functions.html#object)weight loader


## Source code in `vllm/model_executor/model_loader/reload/meta.py`


##

`materialize_layer(layer, info)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.meta.materialize_layer)

Materialize all meta tensors in a layer to actual tensors.

## Source code in `vllm/model_executor/model_loader/reload/meta.py`


##

`materialize_meta_tensor(meta_tensor)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.meta.materialize_meta_tensor)

Materialize a meta tensor into an actual tensor on the current device. Should be called within the torch device context for the given rank.

## Source code in `vllm/model_executor/model_loader/reload/meta.py`


##

`restore_layer_on_meta(layer, info)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.meta.restore_layer_on_meta)

Restore a layer to model format with tensors on the meta device.

## Source code in `vllm/model_executor/model_loader/reload/meta.py`


##

`to_meta_tensor(tensor)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.meta.to_meta_tensor)

Convert a tensor to a meta tensor while preserving class and attributes.
source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/utils/
lastmod: 2026-09-23

#

`vllm.model_executor.utils`

[¶](https://docs.vllm.ai#vllm.model_executor.utils)

Utils for model executor.

Functions:

-
–[get_moe_expert_mapping](https://docs.vllm.ai#vllm.model_executor.utils.get_moe_expert_mapping)Get the expert mapping from a model.

-
–[replace_parameter](https://docs.vllm.ai#vllm.model_executor.utils.replace_parameter)Replace a parameter of a layer while maintaining the ability to reload the

-
–[set_weight_attrs](https://docs.vllm.ai#vllm.model_executor.utils.set_weight_attrs)Set attributes on a weight tensor.

-
–[weights_already_processed](https://docs.vllm.ai#vllm.model_executor.utils.weights_already_processed)Mark that weights are already in post-processed (runtime) format, so


##

`get_moe_expert_mapping(model)`

[¶](https://docs.vllm.ai#vllm.model_executor.utils.get_moe_expert_mapping)

Get the expert mapping from a model.

It will be retrieved from the first module that has a `get_expert_mapping`

method. If the model manually implements `get_expert_mapping`

, it will be used. Otherwise, it will use the first RoutedExperts layer.

## Source code in `vllm/model_executor/utils.py`


##

`replace_parameter(layer, param_name, new_tensor, prefer_copy=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.utils.replace_parameter)

Replace a parameter of a layer while maintaining the ability to reload the weight. Called within implementations of the `process_weights_after_loading`

method.

Custom attributes set on `new_tensor`

(e.g. kernel dispatch flags such as `is_shuffled`

) are carried over to the replacement parameter, except `weight_loader`

, which is always taken from the existing parameter.

Attributes of the existing parameter are otherwise dropped when a new parameter is registered, but kept when `prefer_copy`

reuses it in place.

This function should not be called on weights which are tied/shared

Parameters:

-

(`layer`

[¶](https://docs.vllm.ai#vllm.model_executor.utils.replace_parameter(layer))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)Layer containing parameter to replace

-

(`param_name`

[¶](https://docs.vllm.ai#vllm.model_executor.utils.replace_parameter(param_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Name of parameter to replace

-

(`new_tensor`

[¶](https://docs.vllm.ai#vllm.model_executor.utils.replace_parameter(new_tensor))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneNew data of the new parameter, or None to set the parameter to None

-

(`prefer_copy`

[¶](https://docs.vllm.ai#vllm.model_executor.utils.replace_parameter(prefer_copy))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If True and the existing parameter is compatible with

`new_tensor`

(same shape, dtype, and device), copy`new_tensor`

into the existing parameter in place rather than re-registering a new parameter. This preserves the parameter's storage address (`data_ptr`

), which is required for captured CUDA graphs to remain valid across weight updates (e.g. in RL training loops).

## Source code in `vllm/model_executor/utils.py`


##

`set_weight_attrs(weight, weight_attrs)`

[¶](https://docs.vllm.ai#vllm.model_executor.utils.set_weight_attrs)

Set attributes on a weight tensor.

This method is used to set attributes on a weight tensor. This method will not overwrite existing attributes.

Parameters:

-

(`weight`

[¶](https://docs.vllm.ai#vllm.model_executor.utils.set_weight_attrs(weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The weight tensor.

-

(`weight_attrs`

[¶](https://docs.vllm.ai#vllm.model_executor.utils.set_weight_attrs(weight_attrs))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | NoneA dictionary of attributes to set on the weight tensor.


## Source code in `vllm/model_executor/utils.py`


##

`weights_already_processed()`

[¶](https://docs.vllm.ai#vllm.model_executor.utils.weights_already_processed)

Mark that weights are already in post-processed (runtime) format, so `process_weights_after_loading`

skips tensor transforms (used by the weight cache IPC loader).
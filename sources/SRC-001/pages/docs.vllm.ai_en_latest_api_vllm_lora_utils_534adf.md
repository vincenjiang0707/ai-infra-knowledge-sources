source: https://docs.vllm.ai/en/latest/api/vllm/lora/utils/
lastmod: 2026-09-24

#

`vllm.lora.utils`

[¶](https://docs.vllm.ai#vllm.lora.utils)

Functions:

-
–[get_adapter_absolute_path](https://docs.vllm.ai#vllm.lora.utils.get_adapter_absolute_path)Resolves the given lora_path to an absolute local path.

-
–[get_captured_lora_counts](https://docs.vllm.ai#vllm.lora.utils.get_captured_lora_counts)Returns num_active_loras values for cudagraph capture.

-
–[get_supported_lora_modules](https://docs.vllm.ai#vllm.lora.utils.get_supported_lora_modules)In vLLM, all linear layers support LoRA.

-
–[is_in_target_modules](https://docs.vllm.ai#vllm.lora.utils.is_in_target_modules)Check if a module passes the deployment-time target_modules filter.

-
–[is_moe_model](https://docs.vllm.ai#vllm.lora.utils.is_moe_model)Checks if the model contains MoERunner layers and warns the user.

-
–[is_supported_lora_module](https://docs.vllm.ai#vllm.lora.utils.is_supported_lora_module)Check if a module is in the model's supported LoRA modules.

-
–[parse_fine_tuned_lora_name](https://docs.vllm.ai#vllm.lora.utils.parse_fine_tuned_lora_name)Parse the name of lora weights.

-
–[replace_submodule](https://docs.vllm.ai#vllm.lora.utils.replace_submodule)Replace a submodule in a model with a new module.


##

`get_adapter_absolute_path(lora_path)`

[¶](https://docs.vllm.ai#vllm.lora.utils.get_adapter_absolute_path)

Resolves the given lora_path to an absolute local path.

If the lora_path is identified as a Hugging Face model identifier, it will download the model and return the local snapshot path. Otherwise, it treats the lora_path as a local file path and converts it to an absolute path.

Parameters:

-

(`lora_path`

[¶](https://docs.vllm.ai#vllm.lora.utils.get_adapter_absolute_path(lora_path))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The path to the lora model, which can be an absolute path, a relative path, or a Hugging Face model identifier.


Returns:

-
(`str`


) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The resolved absolute local path to the lora model.


## Source code in `vllm/lora/utils.py`


##

`get_captured_lora_counts(max_loras, specialize)`

[¶](https://docs.vllm.ai#vllm.lora.utils.get_captured_lora_counts)

Returns num_active_loras values for cudagraph capture.

When specialize=True: powers of 2 up to max_loras, plus max_loras + 1. When specialize=False: just [max_loras + 1].

This is the single source of truth for LoRA capture cases, used by both CudagraphDispatcher and PunicaWrapperGPU.

## Source code in `vllm/lora/utils.py`


##

`get_supported_lora_modules(model)`

[¶](https://docs.vllm.ai#vllm.lora.utils.get_supported_lora_modules)

In vLLM, all linear layers support LoRA.

## Source code in `vllm/lora/utils.py`


##

`is_in_target_modules(module_name, target_modules, packed_modules_mapping=None)`

[¶](https://docs.vllm.ai#vllm.lora.utils.is_in_target_modules)

Check if a module passes the deployment-time target_modules filter.

When target_modules is None (no restriction), all modules pass. Otherwise, the module's suffix must be in the target_modules list.

Parameters:

-

(`module_name`

[¶](https://docs.vllm.ai#vllm.lora.utils.is_in_target_modules(module_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Full dot-separated module name.

-

(`target_modules`

[¶](https://docs.vllm.ai#vllm.lora.utils.is_in_target_modules(target_modules))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneOptional deployment-time restriction list from LoRAConfig.target_modules.

-

(`packed_modules_mapping`

[¶](https://docs.vllm.ai#vllm.lora.utils.is_in_target_modules(packed_modules_mapping))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]] | None`None`

) –Optional model-defined mapping from packed runtime module names to their adapter-visible submodule names (e.g.

`{"gate_up_proj": ["gate_proj", "up_proj"]}`

).

Returns:

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)True if the module passes the filter, False otherwise.


## Source code in `vllm/lora/utils.py`


##

`is_moe_model(model)`

[¶](https://docs.vllm.ai#vllm.lora.utils.is_moe_model)

Checks if the model contains MoERunner layers and warns the user.

## Source code in `vllm/lora/utils.py`


##

`is_supported_lora_module(module_name, module, supported_lora_modules)`

[¶](https://docs.vllm.ai#vllm.lora.utils.is_supported_lora_module)

Check if a module is in the model's supported LoRA modules.

The module name must match a model-supported suffix, and the runtime module must belong to a module family handled by LoRA.

Parameters:

-

(`module_name`

[¶](https://docs.vllm.ai#vllm.lora.utils.is_supported_lora_module(module_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Full dot-separated module name.

-

(`module`

[¶](https://docs.vllm.ai#vllm.lora.utils.is_supported_lora_module(module))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)Runtime module associated with

`module_name`

. -

(`supported_lora_modules`

[¶](https://docs.vllm.ai#vllm.lora.utils.is_supported_lora_module(supported_lora_modules))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]List of module suffixes supported by the model.


Returns:

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)True if the module is supported, False otherwise.


## Source code in `vllm/lora/utils.py`


##

`parse_fine_tuned_lora_name(name, weights_mapper=None)`

[¶](https://docs.vllm.ai#vllm.lora.utils.parse_fine_tuned_lora_name)

Parse the name of lora weights.

Parameters:

-

(`name`

[¶](https://docs.vllm.ai#vllm.lora.utils.parse_fine_tuned_lora_name(name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)the name of the fine-tuned LoRA, e.g. base_model.model.dense1.weight

-

(`weights_mapper`

[¶](https://docs.vllm.ai#vllm.lora.utils.parse_fine_tuned_lora_name(weights_mapper))

, default:[WeightsMapper](https://docs.vllm.ai/model_executor/models/utils/#vllm.model_executor.models.utils.WeightsMapper)| None`None`

) –maps the name of weight, e.g.

`model.`

->`language_model.model.`

,

return: tuple(module_name, is_lora_a): module_name: the name of the module, e.g. model.dense1, is_lora_a whether the tensor is lora_a or lora_b.

## Source code in `vllm/lora/utils.py`


##

`replace_submodule(model, module_name, new_module)`

[¶](https://docs.vllm.ai#vllm.lora.utils.replace_submodule)

Replace a submodule in a model with a new module.
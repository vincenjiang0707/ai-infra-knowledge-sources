source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/utils/
lastmod: 2026-09-23

#

`vllm.model_executor.model_loader.utils`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.utils)

Utilities for selecting and loading models.

Functions:

-
–[configure_quant_config](https://docs.vllm.ai#vllm.model_executor.model_loader.utils.configure_quant_config)Pass packed_modules_mapping by reference to quant_config so that

-
–[get_draft_load_config](https://docs.vllm.ai#vllm.model_executor.model_loader.utils.get_draft_load_config)Get load config for the speculative draft model.

-
–[initialize_model](https://docs.vllm.ai#vllm.model_executor.model_loader.utils.initialize_model)Initialize a model with the given configurations.

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.model_loader.utils.process_weights_after_loading)Post-process loaded weights into runtime format.


##

`_MODEL_ARCH_BY_HASH = dict[int, tuple[type[nn.Module], str]]()`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.utils._MODEL_ARCH_BY_HASH)

Caches the outputs of `_get_model_architecture`

.

##

`configure_quant_config(quant_config, model_class)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.utils.configure_quant_config)

Pass packed_modules_mapping by reference to quant_config so that quant_config can properly match fused modules

Note that model attributes are passed by reference to quant_config, enabling them to be updated by model_class.**new** (ex. chatglm, qwen)

Once the `SupportsQuant`

mixin has been added to all models, this function can be removed

## Source code in `vllm/model_executor/model_loader/utils.py`


##

`get_draft_load_config(vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.utils.get_draft_load_config)

Get load config for the speculative draft model.

## Source code in `vllm/model_executor/model_loader/utils.py`


##

`initialize_model(vllm_config, *, prefix='', model_class=None, model_config=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.utils.initialize_model)

Initialize a model with the given configurations.

## Source code in `vllm/model_executor/model_loader/utils.py`


##

`process_weights_after_loading(model, model_config, target_device)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.utils.process_weights_after_loading)

Post-process loaded weights into runtime format.

Under `weights_already_processed`

(weight cache IPC loader), quant methods skip tensor transforms and must declare `supports_pre_processed_weights`

, otherwise this raises `RuntimeError`

.
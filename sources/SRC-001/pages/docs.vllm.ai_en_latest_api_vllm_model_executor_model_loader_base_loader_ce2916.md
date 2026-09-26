source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/base_loader/
lastmod: 2026-09-24

#

`vllm.model_executor.model_loader.base_loader`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.base_loader)

Classes:

-
–[BaseModelLoader](https://docs.vllm.ai#vllm.model_executor.model_loader.base_loader.BaseModelLoader)Base class for model loaders.


Functions:

-
–[log_model_inspection](https://docs.vllm.ai#vllm.model_executor.model_loader.base_loader.log_model_inspection)Log model structure if VLLM_LOG_MODEL_INSPECTION=1.

-
–[log_online_quantization](https://docs.vllm.ai#vllm.model_executor.model_loader.base_loader.log_online_quantization)Log the online-quantized layer count and types, when applicable.


##

`BaseModelLoader`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.base_loader.BaseModelLoader)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for model loaders.

Methods:

-
–[create_model](https://docs.vllm.ai#vllm.model_executor.model_loader.base_loader.BaseModelLoader.create_model)Create a model with the given configurations.

-
–[download_model](https://docs.vllm.ai#vllm.model_executor.model_loader.base_loader.BaseModelLoader.download_model)Download a model so that it can be immediately loaded.

-
–[load_model](https://docs.vllm.ai#vllm.model_executor.model_loader.base_loader.BaseModelLoader.load_model)Load a model with the given configurations.

-
–[load_weights](https://docs.vllm.ai#vllm.model_executor.model_loader.base_loader.BaseModelLoader.load_weights)Load weights into a model. This standalone API allows


## Source code in `vllm/model_executor/model_loader/base_loader.py`


###

`create_model(vllm_config, model_config, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.base_loader.BaseModelLoader.create_model)

Create a model with the given configurations.

## Source code in `vllm/model_executor/model_loader/base_loader.py`


###

`download_model(model_config)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.base_loader.BaseModelLoader.download_model)

###

`load_model(vllm_config, model_config, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.base_loader.BaseModelLoader.load_model)

Load a model with the given configurations.

## Source code in `vllm/model_executor/model_loader/base_loader.py`


###

`load_weights(model, model_config)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.base_loader.BaseModelLoader.load_weights)

Load weights into a model. This standalone API allows inplace weights loading for an already-initialized model

## Source code in `vllm/model_executor/model_loader/base_loader.py`


##

`log_model_inspection(model)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.base_loader.log_model_inspection)

Log model structure if VLLM_LOG_MODEL_INSPECTION=1.

## Source code in `vllm/model_executor/model_loader/base_loader.py`


##

`log_online_quantization(vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.base_loader.log_online_quantization)

Log the online-quantized layer count and types, when applicable.
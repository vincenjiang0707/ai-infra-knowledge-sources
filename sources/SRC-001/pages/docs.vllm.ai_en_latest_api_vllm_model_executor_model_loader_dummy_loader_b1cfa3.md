source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/dummy_loader/
lastmod: 2026-09-24

#

`vllm.model_executor.model_loader.dummy_loader`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.dummy_loader)

Classes:

-
–[DummyModelLoader](https://docs.vllm.ai#vllm.model_executor.model_loader.dummy_loader.DummyModelLoader)Model loader that will set model weights to random values.


##

`DummyModelLoader`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.dummy_loader.DummyModelLoader)

Bases: [BaseModelLoader](https://docs.vllm.ai/base_loader/#vllm.model_executor.model_loader.base_loader.BaseModelLoader)

Model loader that will set model weights to random values.

## Source code in `vllm/model_executor/model_loader/dummy_loader.py`


###

`_process_online_quant_layer(layer, info)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.dummy_loader.DummyModelLoader._process_online_quant_layer)

Materialize, apply dummy weights, and run quantization processing.
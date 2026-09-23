source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/pooler/abstract/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.pooler.abstract`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.pooler.abstract)

Classes:

-
–[Pooler](https://docs.vllm.ai#vllm.model_executor.layers.pooler.abstract.Pooler)The interface required for all poolers used in pooling models in vLLM.


##

`Pooler`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.pooler.abstract.Pooler)

The interface required for all poolers used in pooling models in vLLM.

Methods:

-
–[get_pooling_updates](https://docs.vllm.ai#vllm.model_executor.layers.pooler.abstract.Pooler.get_pooling_updates)Construct the updated pooling parameters to use for a supported task.

-
–[get_supported_tasks](https://docs.vllm.ai#vllm.model_executor.layers.pooler.abstract.Pooler.get_supported_tasks)Determine which pooling tasks are supported.


## Source code in `vllm/model_executor/layers/pooler/abstract.py`


###

`get_pooling_updates(task)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.pooler.abstract.Pooler.get_pooling_updates)

Construct the updated pooling parameters to use for a supported task.
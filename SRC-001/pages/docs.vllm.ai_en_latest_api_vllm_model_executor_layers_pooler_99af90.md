source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/pooler/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.pooler`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.pooler)

Modules:

-
–[abstract](https://docs.vllm.ai/abstract/#vllm.model_executor.layers.pooler.abstract) -
–[common](https://docs.vllm.ai/common/#vllm.model_executor.layers.pooler.common) -
–[seqwise](https://docs.vllm.ai/seqwise/#vllm.model_executor.layers.pooler.seqwise)Poolers that produce an output aggregating all tokens in the sequence.

-
–[special](https://docs.vllm.ai/special/#vllm.model_executor.layers.pooler.special) -
–[tokwise](https://docs.vllm.ai/tokwise/#vllm.model_executor.layers.pooler.tokwise)Poolers that produce an output for each token in the sequence.


Classes:

-
–[BOSEOSFilter](https://docs.vllm.ai#vllm.model_executor.layers.pooler.BOSEOSFilter)Filters the BOS and EOS token results from outputs.

-
–[DispatchPooler](https://docs.vllm.ai#vllm.model_executor.layers.pooler.DispatchPooler)Dispatches calls to a sub-pooler based on the pooling task.

-
–[Pooler](https://docs.vllm.ai#vllm.model_executor.layers.pooler.Pooler)The interface required for all poolers used in pooling models in vLLM.

-
–[PoolingParamsUpdate](https://docs.vllm.ai#vllm.model_executor.layers.pooler.PoolingParamsUpdate)

##

`BOSEOSFilter`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.pooler.BOSEOSFilter)

Bases: [Pooler](https://docs.vllm.ai/abstract/#vllm.model_executor.layers.pooler.abstract.Pooler)

Filters the BOS and EOS token results from outputs.

## Source code in `vllm/model_executor/layers/pooler/special.py`


##

`DispatchPooler`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.pooler.DispatchPooler)

Bases: [Pooler](https://docs.vllm.ai/abstract/#vllm.model_executor.layers.pooler.abstract.Pooler)

Dispatches calls to a sub-pooler based on the pooling task.

Methods:

-
–[replace_classifier](https://docs.vllm.ai#vllm.model_executor.layers.pooler.DispatchPooler.replace_classifier)Replaces the classifier to the LoRA-wrapped version.


## Source code in `vllm/model_executor/layers/pooler/special.py`


|
|

###

`replace_classifier(new_classifier)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.pooler.DispatchPooler.replace_classifier)

Replaces the classifier to the LoRA-wrapped version.

## Source code in `vllm/model_executor/layers/pooler/special.py`


##

`Pooler`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.pooler.Pooler)

The interface required for all poolers used in pooling models in vLLM.

Methods:

-
–[get_pooling_updates](https://docs.vllm.ai#vllm.model_executor.layers.pooler.Pooler.get_pooling_updates)Construct the updated pooling parameters to use for a supported task.

-
–[get_supported_tasks](https://docs.vllm.ai#vllm.model_executor.layers.pooler.Pooler.get_supported_tasks)Determine which pooling tasks are supported.


## Source code in `vllm/model_executor/layers/pooler/abstract.py`


###

`get_pooling_updates(task)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.pooler.Pooler.get_pooling_updates)

Construct the updated pooling parameters to use for a supported task.

##

`PoolingParamsUpdate`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.pooler.PoolingParamsUpdate)

Attributes:

-
([requires_token_ids](https://docs.vllm.ai#vllm.model_executor.layers.pooler.PoolingParamsUpdate.requires_token_ids)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Set this flag to enable CPU prompt token IDs for your pooler.


## Source code in `vllm/model_executor/layers/pooler/common.py`


###

`requires_token_ids = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.pooler.PoolingParamsUpdate.requires_token_ids)

Set this flag to enable CPU prompt token IDs for your pooler.
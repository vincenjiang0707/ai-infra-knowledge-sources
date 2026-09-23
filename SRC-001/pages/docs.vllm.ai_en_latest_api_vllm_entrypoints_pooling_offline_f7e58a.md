source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/pooling/offline/
lastmod: 2026-09-23

#

`vllm.entrypoints.pooling.offline`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline)

Classes:

-
–[PoolingOfflineMixin](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin)Offline inference for pooling models.


##

`PoolingOfflineMixin`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin)

Bases: [OfflineInferenceMixin](https://docs.vllm.ai/offline_utils/#vllm.entrypoints.offline_utils.OfflineInferenceMixin)

Offline inference for pooling models.

Methods:

-
–[classify](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.classify)Generate class logits for each prompt.

-
–[embed](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.embed)Generate an embedding vector for each prompt.

-
–[encode](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.encode)Apply pooling to the hidden states corresponding to the input

-
–[score](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.score)Generate similarity scores for all pairs

`<text,text_pair>`

or

## Source code in `vllm/entrypoints/pooling/offline.py`


|
|

###

`classify(prompts, *, pooling_params=None, use_tqdm=True, lora_request=None, tokenization_kwargs=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.classify)

Generate class logits for each prompt.

This class automatically batches the given prompts, considering the memory constraint. For the best performance, put all of your prompts into a single list and pass it to this method.

Parameters:

-

(`prompts`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.classify(prompts))

) –[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)|[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)]The prompts to the LLM. You may pass a sequence of prompts for batch inference. See

[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)for more details about the format of each prompt. -

(`pooling_params`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.classify(pooling_params))

, default:[PoolingParams](https://docs.vllm.ai/pooling_params/#vllm.pooling_params.PoolingParams)|[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[PoolingParams](https://docs.vllm.ai/pooling_params/#vllm.pooling_params.PoolingParams)] | None`None`

) –The pooling parameters for pooling. If None, we use the default pooling parameters.

-

(`use_tqdm`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.classify(use_tqdm))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)|[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[..., tqdm]`True`

) –If

`True`

, shows a tqdm progress bar. If a callable (e.g.,`functools.partial(tqdm, leave=False)`

), it is used to create the progress bar. If`False`

, no progress bar is created. -

(`lora_request`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.classify(lora_request))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)] |[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| None`None`

) –LoRA request to use for generation, if any.

-

(`tokenization_kwargs`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.classify(tokenization_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Overrides for

`tokenizer.encode`

.

Returns:

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ClassificationRequestOutput]A list of

`ClassificationRequestOutput`

objects containing the -

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ClassificationRequestOutput]embedding vectors in the same order as the input prompts.


## Source code in `vllm/entrypoints/pooling/offline.py`


###

`embed(prompts, *, use_tqdm=True, pooling_params=None, lora_request=None, tokenization_kwargs=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.embed)

Generate an embedding vector for each prompt.

This class automatically batches the given prompts, considering the memory constraint. For the best performance, put all of your prompts into a single list and pass it to this method.

Parameters:

-

(`prompts`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.embed(prompts))

) –[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)|[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)]The prompts to the LLM. You may pass a sequence of prompts for batch inference. See

[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)for more details about the format of each prompt. -

(`pooling_params`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.embed(pooling_params))

, default:[PoolingParams](https://docs.vllm.ai/pooling_params/#vllm.pooling_params.PoolingParams)|[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[PoolingParams](https://docs.vllm.ai/pooling_params/#vllm.pooling_params.PoolingParams)] | None`None`

) –The pooling parameters for pooling. If None, we use the default pooling parameters.

-

(`use_tqdm`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.embed(use_tqdm))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)|[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[..., tqdm]`True`

) –If

`True`

, shows a tqdm progress bar. If a callable (e.g.,`functools.partial(tqdm, leave=False)`

), it is used to create the progress bar. If`False`

, no progress bar is created. -

(`lora_request`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.embed(lora_request))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)] |[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| None`None`

) –LoRA request to use for generation, if any.

-

(`tokenization_kwargs`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.embed(tokenization_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Overrides for

`tokenizer.encode`

.

Returns:

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[EmbeddingRequestOutput]A list of

`EmbeddingRequestOutput`

objects containing the -

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[EmbeddingRequestOutput]embedding vectors in the same order as the input prompts.


## Source code in `vllm/entrypoints/pooling/offline.py`


###

`encode(prompts, pooling_params=None, *, use_tqdm=True, lora_request=None, pooling_task=None, tokenization_kwargs=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.encode)

Apply pooling to the hidden states corresponding to the input prompts.

This class automatically batches the given prompts, considering the memory constraint. For the best performance, put all of your prompts into a single list and pass it to this method.

Parameters:

-

(`prompts`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.encode(prompts))

) –[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)|[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)] |[DataPrompt](https://docs.vllm.ai/inputs/#vllm.inputs.DataPrompt)The prompts to the LLM. You may pass a sequence of prompts for batch inference. See

[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)for more details about the format of each prompt. -

(`pooling_params`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.encode(pooling_params))

, default:[PoolingParams](https://docs.vllm.ai/pooling_params/#vllm.pooling_params.PoolingParams)|[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[PoolingParams](https://docs.vllm.ai/pooling_params/#vllm.pooling_params.PoolingParams)] | None`None`

) –The pooling parameters for pooling. If None, we use the default pooling parameters.

-

(`use_tqdm`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.encode(use_tqdm))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)|[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[..., tqdm]`True`

) –If

`True`

, shows a tqdm progress bar. If a callable (e.g.,`functools.partial(tqdm, leave=False)`

), it is used to create the progress bar. If`False`

, no progress bar is created. -

(`lora_request`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.encode(lora_request))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)] |[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| None`None`

) –LoRA request to use for generation, if any.

-

(`pooling_task`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.encode(pooling_task))`PoolingTask | None`

, default:`None`

) –Override the pooling task to use.

-

(`tokenization_kwargs`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.encode(tokenization_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Overrides for

`tokenizer.encode`

.

Returns:

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[PoolingRequestOutput](https://docs.vllm.ai/outputs/#vllm.outputs.PoolingRequestOutput)]A list of

`PoolingRequestOutput`

objects containing the -

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[PoolingRequestOutput](https://docs.vllm.ai/outputs/#vllm.outputs.PoolingRequestOutput)]pooled hidden states in the same order as the input prompts.


## Source code in `vllm/entrypoints/pooling/offline.py`


###

`score(data_1, data_2, /, *, use_tqdm=True, pooling_params=None, lora_request=None, tokenization_kwargs=None, chat_template=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.score)

Generate similarity scores for all pairs `<text,text_pair>`

or `<multi-modal data, multi-modal data pair>`

.

The inputs can be `1 -> 1`

, `1 -> N`

or `N -> N`

. In the `1 - N`

case the `data_1`

input will be replicated `N`

times to pair with the `data_2`

inputs. The input pairs are used to build a list of prompts for the cross encoder model. This class automatically batches the prompts, considering the memory constraint. For the best performance, put all of your inputs into a single list and pass it to this method.

Supports both text and multi-modal data (images, etc.) when used with appropriate multi-modal models. For multi-modal inputs, ensure the prompt structure matches the model's expected input format.

Parameters:

-

(`data_1`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.score(data_1))`ScoreInput |`

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ScoreInput]Can be a single prompt, a list of prompts or

`ScoreMultiModalParam`

, which can contain either text or multi-modal data. When a list, it must have the same length as the`data_2`

list. -

(`data_2`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.score(data_2))`ScoreInput |`

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ScoreInput]The data to pair with the query to form the input to the LLM. Can be text or multi-modal data. See

[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)for more details about the format of each prompt. -

(`pooling_params`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.score(pooling_params))

, default:[PoolingParams](https://docs.vllm.ai/pooling_params/#vllm.pooling_params.PoolingParams)| None`None`

) –The pooling parameters for pooling. If None, we use the default pooling parameters.

-

(`use_tqdm`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.score(use_tqdm))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)|[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[..., tqdm]`True`

) –If

`True`

, shows a tqdm progress bar. If a callable (e.g.,`functools.partial(tqdm, leave=False)`

), it is used to create the progress bar. If`False`

, no progress bar is created. -

(`lora_request`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.score(lora_request))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)] |[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| None`None`

) –LoRA request to use for generation, if any.

-

(`chat_template`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.score(chat_template))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The chat template to use for the scoring. If None, we use the model's default chat template.

-

(`tokenization_kwargs`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.score(tokenization_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Overrides for

`tokenizer.encode`

.

Returns:

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ScoringRequestOutput]A list of

`ScoringRequestOutput`

objects containing the -

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ScoringRequestOutput]generated scores in the same order as the input prompts.


## Source code in `vllm/entrypoints/pooling/offline.py`


|
|
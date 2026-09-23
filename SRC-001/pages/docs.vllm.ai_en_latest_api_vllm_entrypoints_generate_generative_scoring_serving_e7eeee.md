source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/generate/generative_scoring/serving/
lastmod: 2026-09-23

#

`vllm.entrypoints.generate.generative_scoring.serving`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving)

Generative Scoring implementation for generative models.

This module implements generative scoring functionality that computes the probability of specified token IDs appearing as the next token after a given query+item prompt. This works on any generative model that produces logits (task="generate").

Classes:

-
–[GenerativeScoringItemResult](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.GenerativeScoringItemResult)Result for a single item in the generative scoring response.

-
–[GenerativeScoringRequest](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.GenerativeScoringRequest)Request for computing generative scoring.

-
–[GenerativeScoringResponse](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.GenerativeScoringResponse)Response from the generative scoring computation.

-
–[ServingGenerativeScoring](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.ServingGenerativeScoring)Serving class for generative scoring computation.


##

`GenerativeScoringItemResult`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.GenerativeScoringItemResult)

Bases: `OpenAIBaseModel`


Result for a single item in the generative scoring response.

Attributes:

-
(`index`


) –[int](https://docs.python.org/3/builtins/functions.html#int)The index of this item in the input items list.

-
(`object`


) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['score']Type of object, always "score".

-
(`score`


) –[float](https://docs.python.org/3/builtins/functions.html#float)The probability score for the first label token.


## Source code in `vllm/entrypoints/generate/generative_scoring/serving.py`


##

`GenerativeScoringRequest`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.GenerativeScoringRequest)

Bases: `OpenAIBaseModel`


Request for computing generative scoring.

Attributes:

-
(`model`


) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe model to use for scoring. Optional, follows existing patterns.

-
(`query`


) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)|[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]The query text or pre-tokenized query token IDs.

-
(`items`


) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] |[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]The item text(s) or pre-tokenized item token IDs.

-
(`label_token_ids`


) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]List of token IDs to compute probabilities for.

-
(`apply_softmax`


) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to normalize probabilities using softmax over only the label_token_ids (True) or return true model probabilities over the full vocab for those ids (False).

-
(`item_first`


) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, prepend items to query. Otherwise append items to query.

-
(`add_special_tokens`


) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to add special tokens when tokenizing.


## Source code in `vllm/entrypoints/generate/generative_scoring/serving.py`


##

`GenerativeScoringResponse`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.GenerativeScoringResponse)

Bases: `OpenAIBaseModel`


Response from the generative scoring computation.

Attributes:

-
(`id`


) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Unique identifier for this response.

-
(`object`


) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['list']Type of object, always "list".

-
(`created`


) –[int](https://docs.python.org/3/builtins/functions.html#int)Unix timestamp of when the response was created.

-
(`model`


) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The model used for scoring.

-
(`data`


) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[GenerativeScoringItemResult](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.GenerativeScoringItemResult)]List of scoring results, one per input item.

-
(`usage`

`UsageInfo`

) –Token usage information.


## Source code in `vllm/entrypoints/generate/generative_scoring/serving.py`


##

`ServingGenerativeScoring`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.ServingGenerativeScoring)

Bases: [BaseServing](https://docs.vllm.ai/serve/engine/serving/#vllm.entrypoints.serve.engine.serving.BaseServing)

Serving class for generative scoring computation.

This class handles computing the probability of specified token IDs appearing as the next token after concatenating query and item prompts.

The key operation is: 1. For each item, build a prompt: query + item (or item + query if item_first) 2. Run a forward pass to get the next token distribution 3. Extract probabilities for the specified label_token_ids 4. Normalize either over the full vocab (apply_softmax=False) or over just the label_token_ids (apply_softmax=True)

Methods:

-
–[create_generative_scoring](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.ServingGenerativeScoring.create_generative_scoring)Create generative scoring for the given request.


## Source code in `vllm/entrypoints/generate/generative_scoring/serving.py`


|
|

###

`_build_prompts(request, tokenizer, max_model_len)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.ServingGenerativeScoring._build_prompts)

Build prompts by concatenating query and items.

Uses the Renderer's tokenizer to tokenize text inputs, then creates EngineInput via tokens_input() for engine consumption.

Parameters:

-

(`request`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.ServingGenerativeScoring._build_prompts(request))

) –[GenerativeScoringRequest](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.GenerativeScoringRequest)The request containing query, items, and settings.

-

(`tokenizer`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.ServingGenerativeScoring._build_prompts(tokenizer))`TokenizerLike`

) –The tokenizer to use.

-

(`max_model_len`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.ServingGenerativeScoring._build_prompts(max_model_len))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum model context length for truncation.


Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[EngineInput](https://docs.vllm.ai/inputs/#vllm.inputs.EngineInput)],[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]Tuple of (list of EngineInput, list of prompt token counts).


## Source code in `vllm/entrypoints/generate/generative_scoring/serving.py`


###

`_compute_probabilities(label_logprobs, apply_softmax)`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.ServingGenerativeScoring._compute_probabilities)

Compute probabilities from logprobs.

Parameters:

-

(`label_logprobs`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.ServingGenerativeScoring._compute_probabilities(label_logprobs))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[int](https://docs.python.org/3/builtins/functions.html#int),[float](https://docs.python.org/3/builtins/functions.html#float)]Dictionary mapping token_id to logprob.

-

(`apply_softmax`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.ServingGenerativeScoring._compute_probabilities(apply_softmax))

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, normalize over only the label tokens. If False, return true model probabilities (exp(logprob)).


Returns:

## Source code in `vllm/entrypoints/generate/generative_scoring/serving.py`


###

`_get_trace_headers(headers)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.ServingGenerativeScoring._get_trace_headers)

Extract trace headers from request headers.

## Source code in `vllm/entrypoints/generate/generative_scoring/serving.py`


###

`create_generative_scoring(request, raw_request=None)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.ServingGenerativeScoring.create_generative_scoring)

Create generative scoring for the given request.

Parameters:

-

(`request`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.ServingGenerativeScoring.create_generative_scoring(request))

) –[GenerativeScoringRequest](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.GenerativeScoringRequest)The GenerativeScoringRequest containing query, items, and label_token_ids.

-

(`raw_request`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.ServingGenerativeScoring.create_generative_scoring(raw_request))`Request | None`

, default:`None`

) –The raw FastAPI request object.


Returns:

-

–[GenerativeScoringResponse](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.GenerativeScoringResponse)| ErrorResponseGenerativeScoringResponse with probabilities for each item, or

-

–[GenerativeScoringResponse](https://docs.vllm.ai#vllm.entrypoints.generate.generative_scoring.serving.GenerativeScoringResponse)| ErrorResponseErrorResponse if an error occurred.


## Source code in `vllm/entrypoints/generate/generative_scoring/serving.py`


|
|
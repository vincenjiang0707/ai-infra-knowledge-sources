source: https://docs.vllm.ai/en/latest/api/vllm/inputs/engine/
lastmod: 2026-09-24

#

`vllm.inputs.engine`

[¶](https://docs.vllm.ai#vllm.inputs.engine)

Schema and utilities for inputs to the engine client (`LLMEngine`

/`AsyncLLM`

).

Classes:

-
–[EmbedsInput](https://docs.vllm.ai#vllm.inputs.engine.EmbedsInput)Represents embeddings-based input to the engine.

-
–[EncoderDecoderInput](https://docs.vllm.ai#vllm.inputs.engine.EncoderDecoderInput)A rendered

`EncoderDecoderPrompt`

-
–[MultiModalEncDecInput](https://docs.vllm.ai#vllm.inputs.engine.MultiModalEncDecInput)Represents multi-modal input to the engine for encoder-decoder models.

-
–[MultiModalInput](https://docs.vllm.ai#vllm.inputs.engine.MultiModalInput)Represents multi-modal input to the engine.

-
–[TokensInput](https://docs.vllm.ai#vllm.inputs.engine.TokensInput)Represents token-based input to the engine.


Functions:

-
–[embeds_input](https://docs.vllm.ai#vllm.inputs.engine.embeds_input)Construct

`EmbedsInput`

-
–[tokens_input](https://docs.vllm.ai#vllm.inputs.engine.tokens_input)Construct

`TokensInput`


Attributes:

-
([DecoderEngineInput](https://docs.vllm.ai#vllm.inputs.engine.DecoderEngineInput)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)A rendered

`DecoderPrompt`

-
([DecoderOnlyEngineInput](https://docs.vllm.ai#vllm.inputs.engine.DecoderOnlyEngineInput)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)A rendered

`DecoderOnlyPrompt`

-
([EncoderInput](https://docs.vllm.ai#vllm.inputs.engine.EncoderInput)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)A rendered

`EncoderPrompt`

-
([EngineInput](https://docs.vllm.ai#vllm.inputs.engine.EngineInput)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)A rendered

`PromptType`

-
([MultiModalHashes](https://docs.vllm.ai#vllm.inputs.engine.MultiModalHashes)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)A dictionary containing per-item hashes for each modality.

-
([MultiModalPlaceholders](https://docs.vllm.ai#vllm.inputs.engine.MultiModalPlaceholders)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)A dictionary containing per-item placeholder ranges for each modality.

-
([SingletonInput](https://docs.vllm.ai#vllm.inputs.engine.SingletonInput)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)A rendered

`SingletonPrompt`


##

`DecoderEngineInput = TokensInput | MultiModalInput`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.DecoderEngineInput)

A rendered [ DecoderPrompt](https://docs.vllm.ai/llm/#vllm.inputs.llm.DecoderPrompt) which can be passed to

`LLMEngine.add_request`

or `AsyncLLM.add_request`

.##

`DecoderOnlyEngineInput = TokensInput | EmbedsInput | MultiModalInput`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.DecoderOnlyEngineInput)

A rendered [ DecoderOnlyPrompt](https://docs.vllm.ai/llm/#vllm.inputs.llm.DecoderOnlyPrompt) which can be passed to

`LLMEngine.add_request`

or `AsyncLLM.add_request`

.##

`EncoderInput = TokensInput | MultiModalEncDecInput`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.EncoderInput)

A rendered [ EncoderPrompt](https://docs.vllm.ai/llm/#vllm.inputs.llm.EncoderPrompt) which can be passed to

`LLMEngine.add_request`

or `AsyncLLM.add_request`

.##

`EngineInput = DecoderOnlyEngineInput | EncoderDecoderInput`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.EngineInput)

A rendered [ PromptType](https://docs.vllm.ai/llm/#vllm.inputs.llm.PromptType) which can be passed to

`LLMEngine.add_request`

or `AsyncLLM.add_request`

.##

`MultiModalHashes = Mapping[str, list[str]]`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.MultiModalHashes)

A dictionary containing per-item hashes for each modality.

##

`MultiModalPlaceholders = Mapping[str, Sequence['PlaceholderRange']]`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.MultiModalPlaceholders)

A dictionary containing per-item placeholder ranges for each modality.

##

`SingletonInput = DecoderOnlyEngineInput | MultiModalEncDecInput`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.SingletonInput)

A rendered [ SingletonPrompt](https://docs.vllm.ai/llm/#vllm.inputs.llm.SingletonPrompt) which can be passed to

`LLMEngine.add_request`

or `AsyncLLM.add_request`

.##

`EmbedsInput`

[¶](https://docs.vllm.ai#vllm.inputs.engine.EmbedsInput)

Bases: [_InputOptions](https://docs.vllm.ai#vllm.inputs.engine._InputOptions)

Represents embeddings-based input to the engine.

Attributes:

-
([is_token_ids](https://docs.vllm.ai#vllm.inputs.engine.EmbedsInput.is_token_ids)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[bool](https://docs.python.org/3/builtins/functions.html#bool)]]Per-position mask for mixed-mode inputs.

`True`

means the position -
([prompt](https://docs.vllm.ai#vllm.inputs.engine.EmbedsInput.prompt)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The prompt text corresponding to the token IDs, if available.

-
([prompt_embeds](https://docs.vllm.ai#vllm.inputs.engine.EmbedsInput.prompt_embeds)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The embeddings of the prompt.

-
([prompt_token_ids](https://docs.vllm.ai#vllm.inputs.engine.EmbedsInput.prompt_token_ids)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]Token IDs of the rendered prompt. Only set for mixed-mode inputs

-
([type](https://docs.vllm.ai#vllm.inputs.engine.EmbedsInput.type)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['embeds']The type of input.


## Source code in `vllm/inputs/engine.py`


###

`is_token_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.EmbedsInput.is_token_ids)

Per-position mask for mixed-mode inputs. `True`

means the position is a real token ID (use the model's embedding layer); `False`

means the position uses a pre-computed embedding row from `prompt_embeds`

. Length MUST equal `len(prompt_token_ids)`

. For pure-embeds inputs this field is absent.

###

`prompt`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.EmbedsInput.prompt)

The prompt text corresponding to the token IDs, if available.

###

`prompt_embeds`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.EmbedsInput.prompt_embeds)

The embeddings of the prompt.

###

`prompt_token_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.EmbedsInput.prompt_token_ids)

Token IDs of the rendered prompt. Only set for mixed-mode inputs (chat completion with `prompt_embeds`

content parts). When present, `is_token_ids`

MUST also be present and have the same length. For pure-embeds inputs this field is absent.

###

`type`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.EmbedsInput.type)

The type of input.

##

`EncoderDecoderInput`

[¶](https://docs.vllm.ai#vllm.inputs.engine.EncoderDecoderInput)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

A rendered [ EncoderDecoderPrompt](https://docs.vllm.ai/llm/#vllm.inputs.llm.EncoderDecoderPrompt) which can be passed to

`LLMEngine.add_request`

or `AsyncLLM.add_request`

.Attributes:

-
([arrival_time](https://docs.vllm.ai#vllm.inputs.engine.EncoderDecoderInput.arrival_time)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[float](https://docs.python.org/3/builtins/functions.html#float)]The time when the input was received (before rendering).

-
([decoder_prompt](https://docs.vllm.ai#vllm.inputs.engine.EncoderDecoderInput.decoder_prompt)

) –[DecoderEngineInput](https://docs.vllm.ai#vllm.inputs.engine.DecoderEngineInput)The inputs for the decoder portion.

-
([encoder_prompt](https://docs.vllm.ai#vllm.inputs.engine.EncoderDecoderInput.encoder_prompt)

) –[EncoderInput](https://docs.vllm.ai#vllm.inputs.engine.EncoderInput)The inputs for the encoder portion.


## Source code in `vllm/inputs/engine.py`


##

`MultiModalEncDecInput`

[¶](https://docs.vllm.ai#vllm.inputs.engine.MultiModalEncDecInput)

Bases: [MultiModalInput](https://docs.vllm.ai#vllm.inputs.engine.MultiModalInput)

Represents multi-modal input to the engine for encoder-decoder models.

## Note

Even text-only encoder-decoder models are currently implemented as multi-modal models for convenience. (Example: https://github.com/vllm-project/bart-plugin)

Attributes:

-
([encoder_prompt](https://docs.vllm.ai#vllm.inputs.engine.MultiModalEncDecInput.encoder_prompt)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The prompt text corresponding to the encoder token IDs, if available.

-
([encoder_prompt_token_ids](https://docs.vllm.ai#vllm.inputs.engine.MultiModalEncDecInput.encoder_prompt_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]The processed token IDs of the encoder prompt.


## Source code in `vllm/inputs/engine.py`


##

`MultiModalInput`

[¶](https://docs.vllm.ai#vllm.inputs.engine.MultiModalInput)

Bases: [_InputOptions](https://docs.vllm.ai#vllm.inputs.engine._InputOptions)

Represents multi-modal input to the engine.

Attributes:

-
([mm_hashes](https://docs.vllm.ai#vllm.inputs.engine.MultiModalInput.mm_hashes)

) –[MultiModalHashes](https://docs.vllm.ai#vllm.inputs.engine.MultiModalHashes)The hashes of the multi-modal data.

-
([mm_kwargs](https://docs.vllm.ai#vllm.inputs.engine.MultiModalInput.mm_kwargs)`MultiModalKwargsOptionalItems`

) –Keyword arguments to be directly passed to the model after batching.

-
([mm_placeholders](https://docs.vllm.ai#vllm.inputs.engine.MultiModalInput.mm_placeholders)

) –[MultiModalPlaceholders](https://docs.vllm.ai#vllm.inputs.engine.MultiModalPlaceholders)For each modality, information about the placeholder tokens in

-
([prompt](https://docs.vllm.ai#vllm.inputs.engine.MultiModalInput.prompt)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The prompt text corresponding to the token IDs, if available.

-
([prompt_token_ids](https://docs.vllm.ai#vllm.inputs.engine.MultiModalInput.prompt_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]The processed token IDs which includes placeholder tokens.

-
([type](https://docs.vllm.ai#vllm.inputs.engine.MultiModalInput.type)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['multimodal']The type of input.


## Source code in `vllm/inputs/engine.py`


###

`mm_hashes`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.MultiModalInput.mm_hashes)

The hashes of the multi-modal data.

###

`mm_kwargs`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.MultiModalInput.mm_kwargs)

Keyword arguments to be directly passed to the model after batching.

###

`mm_placeholders`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.MultiModalInput.mm_placeholders)

For each modality, information about the placeholder tokens in `prompt_token_ids`

.

###

`prompt`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.MultiModalInput.prompt)

The prompt text corresponding to the token IDs, if available.

###

`prompt_token_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.MultiModalInput.prompt_token_ids)

The processed token IDs which includes placeholder tokens.

###

`type`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.MultiModalInput.type)

The type of input.

##

`TokensInput`

[¶](https://docs.vllm.ai#vllm.inputs.engine.TokensInput)

Bases: [_InputOptions](https://docs.vllm.ai#vllm.inputs.engine._InputOptions)

Represents token-based input to the engine.

Attributes:

-
([prompt](https://docs.vllm.ai#vllm.inputs.engine.TokensInput.prompt)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The prompt text corresponding to the token IDs, if available.

-
([prompt_token_ids](https://docs.vllm.ai#vllm.inputs.engine.TokensInput.prompt_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]The token IDs of the prompt.

-
([prompt_token_offsets](https://docs.vllm.ai#vllm.inputs.engine.TokensInput.prompt_token_offsets)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]] | None]Char-level (start, end) offsets per token, propagated from the

-
([type](https://docs.vllm.ai#vllm.inputs.engine.TokensInput.type)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['token']The type of input.


## Source code in `vllm/inputs/engine.py`


###

`prompt`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.TokensInput.prompt)

The prompt text corresponding to the token IDs, if available.

###

`prompt_token_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.TokensInput.prompt_token_ids)

The token IDs of the prompt.

###

`prompt_token_offsets`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.TokensInput.prompt_token_offsets)

Char-level (start, end) offsets per token, propagated from the renderer's TokensPrompt when offsets were computed.

###

`type`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.engine.TokensInput.type)

The type of input.

##

`_InputOptions`

[¶](https://docs.vllm.ai#vllm.inputs.engine._InputOptions)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

Additional options available to all [ SingletonInput](https://docs.vllm.ai#vllm.inputs.engine.SingletonInput) types.

Attributes:

-
([arrival_time](https://docs.vllm.ai#vllm.inputs.engine._InputOptions.arrival_time)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[float](https://docs.python.org/3/builtins/functions.html#float)]The time when the input was received (before rendering).

-
([cache_salt](https://docs.vllm.ai#vllm.inputs.engine._InputOptions.cache_salt)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Optional cache salt to be used for prefix caching.


## Source code in `vllm/inputs/engine.py`


##

`_prepare_decoder_input_ids_for_generation(decoder_input_ids, decoder_start_token_id)`

[¶](https://docs.vllm.ai#vllm.inputs.engine._prepare_decoder_input_ids_for_generation)

Prepare `decoder_input_ids`

for generation with encoder-decoder models, according to `GenerationMixin._prepare_decoder_input_ids_for_generation()`

.

Source: https://github.com/huggingface/transformers/blob/v5.1.0/src/transformers/generation/utils.py

## Source code in `vllm/inputs/engine.py`


##

`embeds_input(prompt_embeds, *, prompt=None, cache_salt=None, prompt_token_ids=None, is_token_ids=None)`

[¶](https://docs.vllm.ai#vllm.inputs.engine.embeds_input)

Construct [ EmbedsInput](https://docs.vllm.ai#vllm.inputs.engine.EmbedsInput) from optional values.

## Source code in `vllm/inputs/engine.py`


##

`tokens_input(prompt_token_ids, *, prompt=None, cache_salt=None)`

[¶](https://docs.vllm.ai#vllm.inputs.engine.tokens_input)

Construct [ TokensInput](https://docs.vllm.ai#vllm.inputs.engine.TokensInput) from optional values.
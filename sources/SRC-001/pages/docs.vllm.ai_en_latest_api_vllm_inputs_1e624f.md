source: https://docs.vllm.ai/en/latest/api/vllm/inputs/
lastmod: 2026-09-24

#

`vllm.inputs`

[¶](https://docs.vllm.ai#vllm.inputs)

Modules:

-
–[engine](https://docs.vllm.ai/engine/#vllm.inputs.engine)Schema and utilities for inputs to the engine client (

`LLMEngine`

/`AsyncLLM`

). -
–[llm](https://docs.vllm.ai/llm/#vllm.inputs.llm)Schema and utilities for input prompts to the LLM API.


Classes:

-
–[DataPrompt](https://docs.vllm.ai#vllm.inputs.DataPrompt)Represents generic inputs that are converted to

-
–[EmbedsInput](https://docs.vllm.ai#vllm.inputs.EmbedsInput)Represents embeddings-based input to the engine.

-
–[EmbedsPrompt](https://docs.vllm.ai#vllm.inputs.EmbedsPrompt)Schema for a prompt provided via token embeddings.

-
–[EncoderDecoderInput](https://docs.vllm.ai#vllm.inputs.EncoderDecoderInput)A rendered

`EncoderDecoderPrompt`

-
–[ExplicitEncoderDecoderPrompt](https://docs.vllm.ai#vllm.inputs.ExplicitEncoderDecoderPrompt)Schema for a pair of encoder and decoder singleton prompts.

-
–[MultiModalDataBuiltins](https://docs.vllm.ai#vllm.inputs.MultiModalDataBuiltins)Type annotations for modality types predefined by vLLM.

-
–[MultiModalEncDecInput](https://docs.vllm.ai#vllm.inputs.MultiModalEncDecInput)Represents multi-modal input to the engine for encoder-decoder models.

-
–[MultiModalInput](https://docs.vllm.ai#vllm.inputs.MultiModalInput)Represents multi-modal input to the engine.

-
–[TextPrompt](https://docs.vllm.ai#vllm.inputs.TextPrompt)Schema for a text prompt.

-
–[TokensInput](https://docs.vllm.ai#vllm.inputs.TokensInput)Represents token-based input to the engine.

-
–[TokensPrompt](https://docs.vllm.ai#vllm.inputs.TokensPrompt)Schema for a tokenized prompt.


Functions:

-
–[embeds_input](https://docs.vllm.ai#vllm.inputs.embeds_input)Construct

`EmbedsInput`

-
–[tokens_input](https://docs.vllm.ai#vllm.inputs.tokens_input)Construct

`TokensInput`


Attributes:

-
([DecoderOnlyEngineInput](https://docs.vllm.ai#vllm.inputs.DecoderOnlyEngineInput)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)A rendered

`DecoderOnlyPrompt`

-
([EngineInput](https://docs.vllm.ai#vllm.inputs.EngineInput)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)A rendered

`PromptType`

-
([ModalityData](https://docs.vllm.ai#vllm.inputs.ModalityData)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)Either a single data item, or a list of data items. Can only be None if UUID

-
([MultiModalDataDict](https://docs.vllm.ai#vllm.inputs.MultiModalDataDict)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)A dictionary containing an entry for each modality type to input.

-
([MultiModalHashes](https://docs.vllm.ai#vllm.inputs.MultiModalHashes)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)A dictionary containing per-item hashes for each modality.

-
([MultiModalPlaceholders](https://docs.vllm.ai#vllm.inputs.MultiModalPlaceholders)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)A dictionary containing per-item placeholder ranges for each modality.

-
([MultiModalUUIDDict](https://docs.vllm.ai#vllm.inputs.MultiModalUUIDDict)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)A dictionary containing user-provided UUIDs for items in each modality.

-
([PromptType](https://docs.vllm.ai#vllm.inputs.PromptType)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)Schema for any prompt, regardless of model type.

-
([SingletonInput](https://docs.vllm.ai#vllm.inputs.SingletonInput)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)A rendered

`SingletonPrompt`

-
([SingletonPrompt](https://docs.vllm.ai#vllm.inputs.SingletonPrompt)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)Schema for a single prompt. This is as opposed to a data structure


##

`DecoderOnlyEngineInput = TokensInput | EmbedsInput | MultiModalInput`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.DecoderOnlyEngineInput)

A rendered [ DecoderOnlyPrompt](https://docs.vllm.ai/llm/#vllm.inputs.llm.DecoderOnlyPrompt) which can be passed to

`LLMEngine.add_request`

or `AsyncLLM.add_request`

.##

`EngineInput = DecoderOnlyEngineInput | EncoderDecoderInput`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.EngineInput)

A rendered [ PromptType](https://docs.vllm.ai/llm/#vllm.inputs.llm.PromptType) which can be passed to

`LLMEngine.add_request`

or `AsyncLLM.add_request`

.##

`ModalityData = _T | list[_T | None] | None`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.ModalityData)

Either a single data item, or a list of data items. Can only be None if UUID is provided.

The number of data items allowed per modality is restricted by `--limit-mm-per-prompt`

.

##

`MultiModalDataDict = Mapping[str, ModalityData[Any]]`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.MultiModalDataDict)

A dictionary containing an entry for each modality type to input.

The built-in modalities are defined by [ MultiModalDataBuiltins](https://docs.vllm.ai/llm/#vllm.inputs.llm.MultiModalDataBuiltins).

##

`MultiModalHashes = Mapping[str, list[str]]`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.MultiModalHashes)

A dictionary containing per-item hashes for each modality.

##

`MultiModalPlaceholders = Mapping[str, Sequence['PlaceholderRange']]`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.MultiModalPlaceholders)

A dictionary containing per-item placeholder ranges for each modality.

##

`MultiModalUUIDDict = Mapping[str, Sequence[str | None] | str]`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.MultiModalUUIDDict)

A dictionary containing user-provided UUIDs for items in each modality. If a UUID for an item is not provided, its entry will be `None`

and MultiModalHasher will compute a hash for the item.

The UUID will be used to identify the item for all caching purposes (input processing caching, embedding caching, prefix caching, etc).

##

`PromptType = DecoderOnlyPrompt | EncoderDecoderPrompt`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.PromptType)

Schema for any prompt, regardless of model type.

This is the input format accepted by most [ LLM](https://docs.vllm.ai/entrypoints/llm/#vllm.entrypoints.llm.LLM) APIs.

##

`SingletonInput = DecoderOnlyEngineInput | MultiModalEncDecInput`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.SingletonInput)

A rendered [ SingletonPrompt](https://docs.vllm.ai/llm/#vllm.inputs.llm.SingletonPrompt) which can be passed to

`LLMEngine.add_request`

or `AsyncLLM.add_request`

.##

`SingletonPrompt = DecoderOnlyPrompt | EncoderPrompt | DecoderPrompt`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.SingletonPrompt)

Schema for a single prompt. This is as opposed to a data structure which encapsulates multiple prompts, such as [ ExplicitEncoderDecoderPrompt](https://docs.vllm.ai/llm/#vllm.inputs.llm.ExplicitEncoderDecoderPrompt).

##

`DataPrompt`

[¶](https://docs.vllm.ai#vllm.inputs.DataPrompt)

Bases: [_PromptOptions](https://docs.vllm.ai/llm/#vllm.inputs.llm._PromptOptions)

Represents generic inputs that are converted to [ PromptType](https://docs.vllm.ai/llm/#vllm.inputs.llm.PromptType) by IO processor plugins.

Attributes:

-
([data](https://docs.vllm.ai#vllm.inputs.DataPrompt.data)

) –[Any](https://docs.python.org/3/library/typing.html#typing.Any)The input data.

-
([data_format](https://docs.vllm.ai#vllm.inputs.DataPrompt.data_format)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The input data format.


## Source code in `vllm/inputs/llm.py`


##

`EmbedsInput`

[¶](https://docs.vllm.ai#vllm.inputs.EmbedsInput)

Bases: [_InputOptions](https://docs.vllm.ai/engine/#vllm.inputs.engine._InputOptions)

Represents embeddings-based input to the engine.

Attributes:

-
([is_token_ids](https://docs.vllm.ai#vllm.inputs.EmbedsInput.is_token_ids)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[bool](https://docs.python.org/3/builtins/functions.html#bool)]]Per-position mask for mixed-mode inputs.

`True`

means the position -
([prompt](https://docs.vllm.ai#vllm.inputs.EmbedsInput.prompt)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The prompt text corresponding to the token IDs, if available.

-
([prompt_embeds](https://docs.vllm.ai#vllm.inputs.EmbedsInput.prompt_embeds)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The embeddings of the prompt.

-
([prompt_token_ids](https://docs.vllm.ai#vllm.inputs.EmbedsInput.prompt_token_ids)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]Token IDs of the rendered prompt. Only set for mixed-mode inputs

-
([type](https://docs.vllm.ai#vllm.inputs.EmbedsInput.type)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['embeds']The type of input.


## Source code in `vllm/inputs/engine.py`


###

`is_token_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.EmbedsInput.is_token_ids)

Per-position mask for mixed-mode inputs. `True`

means the position is a real token ID (use the model's embedding layer); `False`

means the position uses a pre-computed embedding row from `prompt_embeds`

. Length MUST equal `len(prompt_token_ids)`

. For pure-embeds inputs this field is absent.

###

`prompt`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.EmbedsInput.prompt)

The prompt text corresponding to the token IDs, if available.

###

`prompt_embeds`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.EmbedsInput.prompt_embeds)

The embeddings of the prompt.

###

`prompt_token_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.EmbedsInput.prompt_token_ids)

Token IDs of the rendered prompt. Only set for mixed-mode inputs (chat completion with `prompt_embeds`

content parts). When present, `is_token_ids`

MUST also be present and have the same length. For pure-embeds inputs this field is absent.

###

`type`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.EmbedsInput.type)

The type of input.

##

`EmbedsPrompt`

[¶](https://docs.vllm.ai#vllm.inputs.EmbedsPrompt)

Bases: [_PromptOptions](https://docs.vllm.ai/llm/#vllm.inputs.llm._PromptOptions)

Schema for a prompt provided via token embeddings.

Attributes:

-
([prompt](https://docs.vllm.ai#vllm.inputs.EmbedsPrompt.prompt)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The prompt text corresponding to the token embeddings, if available.

-
([prompt_embeds](https://docs.vllm.ai#vllm.inputs.EmbedsPrompt.prompt_embeds)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The embeddings of the prompt.

-
([prompt_is_token_ids](https://docs.vllm.ai#vllm.inputs.EmbedsPrompt.prompt_is_token_ids)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[bool](https://docs.python.org/3/builtins/functions.html#bool)]]Per-position mask,

`True`

uses the real token ID,`False`

uses -
([prompt_token_ids](https://docs.vllm.ai#vllm.inputs.EmbedsPrompt.prompt_token_ids)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]Token IDs for mixed-mode inputs (chat completion with


## Source code in `vllm/inputs/llm.py`


###

`prompt`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.EmbedsPrompt.prompt)

The prompt text corresponding to the token embeddings, if available.

###

`prompt_embeds`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.EmbedsPrompt.prompt_embeds)

The embeddings of the prompt.

###

`prompt_is_token_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.EmbedsPrompt.prompt_is_token_ids)

Per-position mask, `True`

uses the real token ID, `False`

uses the corresponding entry from `prompt_embeds`

. Must be the same length as `prompt_token_ids`

when both are set.

###

`prompt_token_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.EmbedsPrompt.prompt_token_ids)

Token IDs for mixed-mode inputs (chat completion with `prompt_embeds`

content parts). The tokens at positions where `prompt_is_token_ids`

is `False`

are placeholder tokens that get replaced by entries from `prompt_embeds`

in the forward pass.

##

`EncoderDecoderInput`

[¶](https://docs.vllm.ai#vllm.inputs.EncoderDecoderInput)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

A rendered [ EncoderDecoderPrompt](https://docs.vllm.ai/llm/#vllm.inputs.llm.EncoderDecoderPrompt) which can be passed to

`LLMEngine.add_request`

or `AsyncLLM.add_request`

.Attributes:

-
([arrival_time](https://docs.vllm.ai#vllm.inputs.EncoderDecoderInput.arrival_time)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[float](https://docs.python.org/3/builtins/functions.html#float)]The time when the input was received (before rendering).

-
([decoder_prompt](https://docs.vllm.ai#vllm.inputs.EncoderDecoderInput.decoder_prompt)

) –[DecoderEngineInput](https://docs.vllm.ai/engine/#vllm.inputs.engine.DecoderEngineInput)The inputs for the decoder portion.

-
([encoder_prompt](https://docs.vllm.ai#vllm.inputs.EncoderDecoderInput.encoder_prompt)

) –[EncoderInput](https://docs.vllm.ai/engine/#vllm.inputs.engine.EncoderInput)The inputs for the encoder portion.


## Source code in `vllm/inputs/engine.py`


##

`ExplicitEncoderDecoderPrompt`

[¶](https://docs.vllm.ai#vllm.inputs.ExplicitEncoderDecoderPrompt)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

Schema for a pair of encoder and decoder singleton prompts.

## Note

This schema is not valid for decoder-only models.

Attributes:

-
([decoder_prompt](https://docs.vllm.ai#vllm.inputs.ExplicitEncoderDecoderPrompt.decoder_prompt)

) –[DecoderPrompt](https://docs.vllm.ai/llm/#vllm.inputs.llm.DecoderPrompt)| NoneThe prompt for the decoder part of the model.

-
([encoder_prompt](https://docs.vllm.ai#vllm.inputs.ExplicitEncoderDecoderPrompt.encoder_prompt)

) –[EncoderPrompt](https://docs.vllm.ai/llm/#vllm.inputs.llm.EncoderPrompt)The prompt for the encoder part of the model.


## Source code in `vllm/inputs/llm.py`


##

`MultiModalDataBuiltins`

[¶](https://docs.vllm.ai#vllm.inputs.MultiModalDataBuiltins)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

Type annotations for modality types predefined by vLLM.

Attributes:

-
([audio](https://docs.vllm.ai#vllm.inputs.MultiModalDataBuiltins.audio)

) –[ModalityData](https://docs.vllm.ai/llm/#vllm.inputs.llm.ModalityData)[[AudioItem](https://docs.vllm.ai/multimodal/inputs/#vllm.multimodal.inputs.AudioItem)]The input audio(s).

-
([image](https://docs.vllm.ai#vllm.inputs.MultiModalDataBuiltins.image)

) –[ModalityData](https://docs.vllm.ai/llm/#vllm.inputs.llm.ModalityData)[[ImageItem](https://docs.vllm.ai/multimodal/inputs/#vllm.multimodal.inputs.ImageItem)]The input image(s).

-
([video](https://docs.vllm.ai#vllm.inputs.MultiModalDataBuiltins.video)

) –[ModalityData](https://docs.vllm.ai/llm/#vllm.inputs.llm.ModalityData)[[VideoItem](https://docs.vllm.ai/multimodal/inputs/#vllm.multimodal.inputs.VideoItem)]The input video(s).

-
([vision_chunk](https://docs.vllm.ai#vllm.inputs.MultiModalDataBuiltins.vision_chunk)

) –[ModalityData](https://docs.vllm.ai/llm/#vllm.inputs.llm.ModalityData)[[VisionChunk](https://docs.vllm.ai/multimodal/inputs/#vllm.multimodal.inputs.VisionChunk)]The input visual atom(s) - unified modality for images and video chunks.


## Source code in `vllm/inputs/llm.py`


##

`MultiModalEncDecInput`

[¶](https://docs.vllm.ai#vllm.inputs.MultiModalEncDecInput)

Bases: [MultiModalInput](https://docs.vllm.ai/engine/#vllm.inputs.engine.MultiModalInput)

Represents multi-modal input to the engine for encoder-decoder models.

## Note

Even text-only encoder-decoder models are currently implemented as multi-modal models for convenience. (Example: https://github.com/vllm-project/bart-plugin)

Attributes:

-
([encoder_prompt](https://docs.vllm.ai#vllm.inputs.MultiModalEncDecInput.encoder_prompt)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The prompt text corresponding to the encoder token IDs, if available.

-
([encoder_prompt_token_ids](https://docs.vllm.ai#vllm.inputs.MultiModalEncDecInput.encoder_prompt_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]The processed token IDs of the encoder prompt.


## Source code in `vllm/inputs/engine.py`


##

`MultiModalInput`

[¶](https://docs.vllm.ai#vllm.inputs.MultiModalInput)

Bases: [_InputOptions](https://docs.vllm.ai/engine/#vllm.inputs.engine._InputOptions)

Represents multi-modal input to the engine.

Attributes:

-
([mm_hashes](https://docs.vllm.ai#vllm.inputs.MultiModalInput.mm_hashes)

) –[MultiModalHashes](https://docs.vllm.ai/engine/#vllm.inputs.engine.MultiModalHashes)The hashes of the multi-modal data.

-
([mm_kwargs](https://docs.vllm.ai#vllm.inputs.MultiModalInput.mm_kwargs)`MultiModalKwargsOptionalItems`

) –Keyword arguments to be directly passed to the model after batching.

-
([mm_placeholders](https://docs.vllm.ai#vllm.inputs.MultiModalInput.mm_placeholders)

) –[MultiModalPlaceholders](https://docs.vllm.ai/engine/#vllm.inputs.engine.MultiModalPlaceholders)For each modality, information about the placeholder tokens in

-
([prompt](https://docs.vllm.ai#vllm.inputs.MultiModalInput.prompt)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The prompt text corresponding to the token IDs, if available.

-
([prompt_token_ids](https://docs.vllm.ai#vllm.inputs.MultiModalInput.prompt_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]The processed token IDs which includes placeholder tokens.

-
([type](https://docs.vllm.ai#vllm.inputs.MultiModalInput.type)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['multimodal']The type of input.


## Source code in `vllm/inputs/engine.py`


###

`mm_hashes`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.MultiModalInput.mm_hashes)

The hashes of the multi-modal data.

###

`mm_kwargs`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.MultiModalInput.mm_kwargs)

Keyword arguments to be directly passed to the model after batching.

###

`mm_placeholders`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.MultiModalInput.mm_placeholders)

For each modality, information about the placeholder tokens in `prompt_token_ids`

.

###

`prompt`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.MultiModalInput.prompt)

The prompt text corresponding to the token IDs, if available.

###

`prompt_token_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.MultiModalInput.prompt_token_ids)

The processed token IDs which includes placeholder tokens.

###

`type`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.MultiModalInput.type)

The type of input.

##

`TextPrompt`

[¶](https://docs.vllm.ai#vllm.inputs.TextPrompt)

Bases: [_PromptOptions](https://docs.vllm.ai/llm/#vllm.inputs.llm._PromptOptions)

Schema for a text prompt.

Attributes:

## Source code in `vllm/inputs/llm.py`


###

`prompt`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.TextPrompt.prompt)

The input text to be tokenized before passing to the model.

##

`TokensInput`

[¶](https://docs.vllm.ai#vllm.inputs.TokensInput)

Bases: [_InputOptions](https://docs.vllm.ai/engine/#vllm.inputs.engine._InputOptions)

Represents token-based input to the engine.

Attributes:

-
([prompt](https://docs.vllm.ai#vllm.inputs.TokensInput.prompt)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The prompt text corresponding to the token IDs, if available.

-
([prompt_token_ids](https://docs.vllm.ai#vllm.inputs.TokensInput.prompt_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]The token IDs of the prompt.

-
([prompt_token_offsets](https://docs.vllm.ai#vllm.inputs.TokensInput.prompt_token_offsets)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]] | None]Char-level (start, end) offsets per token, propagated from the

-
([type](https://docs.vllm.ai#vllm.inputs.TokensInput.type)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['token']The type of input.


## Source code in `vllm/inputs/engine.py`


###

`prompt`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.TokensInput.prompt)

The prompt text corresponding to the token IDs, if available.

###

`prompt_token_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.TokensInput.prompt_token_ids)

The token IDs of the prompt.

###

`prompt_token_offsets`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.TokensInput.prompt_token_offsets)

Char-level (start, end) offsets per token, propagated from the renderer's TokensPrompt when offsets were computed.

###

`type`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.TokensInput.type)

The type of input.

##

`TokensPrompt`

[¶](https://docs.vllm.ai#vllm.inputs.TokensPrompt)

Bases: [_PromptOptions](https://docs.vllm.ai/llm/#vllm.inputs.llm._PromptOptions)

Schema for a tokenized prompt.

Attributes:

-
([prompt](https://docs.vllm.ai#vllm.inputs.TokensPrompt.prompt)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The prompt text corresponding to the token IDs, if available.

-
([prompt_token_ids](https://docs.vllm.ai#vllm.inputs.TokensPrompt.prompt_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]A list of token IDs to pass to the model.

-
([prompt_token_offsets](https://docs.vllm.ai#vllm.inputs.TokensPrompt.prompt_token_offsets)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]] | None]Char-level (start, end) offsets per token, relative to the

-
([token_type_ids](https://docs.vllm.ai#vllm.inputs.TokensPrompt.token_type_ids)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]A list of token type IDs to pass to the cross encoder model.


## Source code in `vllm/inputs/llm.py`


###

`prompt`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.TokensPrompt.prompt)

The prompt text corresponding to the token IDs, if available.

###

`prompt_token_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.TokensPrompt.prompt_token_ids)

A list of token IDs to pass to the model.

###

`prompt_token_offsets`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.TokensPrompt.prompt_token_offsets)

Char-level (start, end) offsets per token, relative to the tokenized source string. Present only when offsets were requested AND a Fast (Rust-backed) tokenizer was used AND no multimodal data was present. The list length equals the length of `prompt_token_ids`

.

###

`token_type_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.TokensPrompt.token_type_ids)

A list of token type IDs to pass to the cross encoder model.

##

`embeds_input(prompt_embeds, *, prompt=None, cache_salt=None, prompt_token_ids=None, is_token_ids=None)`

[¶](https://docs.vllm.ai#vllm.inputs.embeds_input)

Construct [ EmbedsInput](https://docs.vllm.ai/engine/#vllm.inputs.engine.EmbedsInput) from optional values.

## Source code in `vllm/inputs/engine.py`


##

`tokens_input(prompt_token_ids, *, prompt=None, cache_salt=None)`

[¶](https://docs.vllm.ai#vllm.inputs.tokens_input)

Construct [ TokensInput](https://docs.vllm.ai/engine/#vllm.inputs.engine.TokensInput) from optional values.
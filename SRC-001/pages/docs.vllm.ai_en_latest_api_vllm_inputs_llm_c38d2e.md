source: https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/
lastmod: 2026-09-23

#

`vllm.inputs.llm`

[¶](https://docs.vllm.ai#vllm.inputs.llm)

Schema and utilities for input prompts to the LLM API.

Classes:

-
–[DataPrompt](https://docs.vllm.ai#vllm.inputs.llm.DataPrompt)Represents generic inputs that are converted to

-
–[EmbedsPrompt](https://docs.vllm.ai#vllm.inputs.llm.EmbedsPrompt)Schema for a prompt provided via token embeddings.

-
–[ExplicitEncoderDecoderPrompt](https://docs.vllm.ai#vllm.inputs.llm.ExplicitEncoderDecoderPrompt)Schema for a pair of encoder and decoder singleton prompts.

-
–[MultiModalDataBuiltins](https://docs.vllm.ai#vllm.inputs.llm.MultiModalDataBuiltins)Type annotations for modality types predefined by vLLM.

-
–[TextPrompt](https://docs.vllm.ai#vllm.inputs.llm.TextPrompt)Schema for a text prompt.

-
–[TokensPrompt](https://docs.vllm.ai#vllm.inputs.llm.TokensPrompt)Schema for a tokenized prompt.


Attributes:

-
([DecoderOnlyPrompt](https://docs.vllm.ai#vllm.inputs.llm.DecoderOnlyPrompt)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)Schema of a prompt for a decoder-only model:

-
([DecoderPrompt](https://docs.vllm.ai#vllm.inputs.llm.DecoderPrompt)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)Schema of a prompt for the decoder part of an encoder-decoder model:

-
([EncoderDecoderPrompt](https://docs.vllm.ai#vllm.inputs.llm.EncoderDecoderPrompt)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)Schema for a prompt for an encoder-decoder model.

-
([EncoderPrompt](https://docs.vllm.ai#vllm.inputs.llm.EncoderPrompt)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)Schema of a prompt for the encoder part of a encoder-decoder model:

-
([ModalityData](https://docs.vllm.ai#vllm.inputs.llm.ModalityData)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)Either a single data item, or a list of data items. Can only be None if UUID

-
([MultiModalDataDict](https://docs.vllm.ai#vllm.inputs.llm.MultiModalDataDict)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)A dictionary containing an entry for each modality type to input.

-
([MultiModalUUIDDict](https://docs.vllm.ai#vllm.inputs.llm.MultiModalUUIDDict)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)A dictionary containing user-provided UUIDs for items in each modality.

-
([PromptType](https://docs.vllm.ai#vllm.inputs.llm.PromptType)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)Schema for any prompt, regardless of model type.

-
([SingletonPrompt](https://docs.vllm.ai#vllm.inputs.llm.SingletonPrompt)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)Schema for a single prompt. This is as opposed to a data structure


##

`DecoderOnlyPrompt = str | TextPrompt | list[int] | TokensPrompt | EmbedsPrompt`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm.DecoderOnlyPrompt)

Schema of a prompt for a decoder-only model:

- A text prompt (string or
)`TextPrompt`

- A tokenized prompt (list of token IDs, or
)`TokensPrompt`

- An embeddings prompt (
)`EmbedsPrompt`


For encoder-decoder models, passing a singleton prompt is shorthand for passing `ExplicitEncoderDecoderPrompt(encoder_prompt=prompt, decoder_prompt=None)`

.

##

`DecoderPrompt = str | TextPrompt | list[int] | TokensPrompt`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm.DecoderPrompt)

Schema of a prompt for the decoder part of an encoder-decoder model:

- A text prompt (string or
)`TextPrompt`

- A tokenized prompt (list of token IDs, or
)`TokensPrompt`


## Note

Multi-modal inputs are not supported for decoder prompts.

##

`EncoderDecoderPrompt = EncoderPrompt | ExplicitEncoderDecoderPrompt`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm.EncoderDecoderPrompt)

Schema for a prompt for an encoder-decoder model.

You can pass a singleton encoder prompt, in which case the decoder prompt is considered to be `None`

(i.e., infer automatically).

##

`EncoderPrompt = str | TextPrompt | list[int] | TokensPrompt`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm.EncoderPrompt)

Schema of a prompt for the encoder part of a encoder-decoder model:

- A text prompt (string or
)`TextPrompt`

- A tokenized prompt (list of token IDs, or
)`TokensPrompt`


##

`ModalityData = _T | list[_T | None] | None`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm.ModalityData)

Either a single data item, or a list of data items. Can only be None if UUID is provided.

The number of data items allowed per modality is restricted by `--limit-mm-per-prompt`

.

##

`MultiModalDataDict = Mapping[str, ModalityData[Any]]`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm.MultiModalDataDict)

A dictionary containing an entry for each modality type to input.

The built-in modalities are defined by [ MultiModalDataBuiltins](https://docs.vllm.ai#vllm.inputs.llm.MultiModalDataBuiltins).

##

`MultiModalUUIDDict = Mapping[str, Sequence[str | None] | str]`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm.MultiModalUUIDDict)

A dictionary containing user-provided UUIDs for items in each modality. If a UUID for an item is not provided, its entry will be `None`

and MultiModalHasher will compute a hash for the item.

The UUID will be used to identify the item for all caching purposes (input processing caching, embedding caching, prefix caching, etc).

##

`PromptType = DecoderOnlyPrompt | EncoderDecoderPrompt`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm.PromptType)

Schema for any prompt, regardless of model type.

This is the input format accepted by most [ LLM](https://docs.vllm.ai/entrypoints/llm/#vllm.entrypoints.llm.LLM) APIs.

##

`SingletonPrompt = DecoderOnlyPrompt | EncoderPrompt | DecoderPrompt`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm.SingletonPrompt)

Schema for a single prompt. This is as opposed to a data structure which encapsulates multiple prompts, such as [ ExplicitEncoderDecoderPrompt](https://docs.vllm.ai#vllm.inputs.llm.ExplicitEncoderDecoderPrompt).

##

`DataPrompt`

[¶](https://docs.vllm.ai#vllm.inputs.llm.DataPrompt)

Bases: [_PromptOptions](https://docs.vllm.ai#vllm.inputs.llm._PromptOptions)

Represents generic inputs that are converted to [ PromptType](https://docs.vllm.ai#vllm.inputs.llm.PromptType) by IO processor plugins.

Attributes:

-
([data](https://docs.vllm.ai#vllm.inputs.llm.DataPrompt.data)

) –[Any](https://docs.python.org/3/library/typing.html#typing.Any)The input data.

-
([data_format](https://docs.vllm.ai#vllm.inputs.llm.DataPrompt.data_format)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The input data format.


## Source code in `vllm/inputs/llm.py`


##

`EmbedsPrompt`

[¶](https://docs.vllm.ai#vllm.inputs.llm.EmbedsPrompt)

Bases: [_PromptOptions](https://docs.vllm.ai#vllm.inputs.llm._PromptOptions)

Schema for a prompt provided via token embeddings.

Attributes:

-
([prompt](https://docs.vllm.ai#vllm.inputs.llm.EmbedsPrompt.prompt)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The prompt text corresponding to the token embeddings, if available.

-
([prompt_embeds](https://docs.vllm.ai#vllm.inputs.llm.EmbedsPrompt.prompt_embeds)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The embeddings of the prompt.

-
([prompt_is_token_ids](https://docs.vllm.ai#vllm.inputs.llm.EmbedsPrompt.prompt_is_token_ids)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[bool](https://docs.python.org/3/builtins/functions.html#bool)]]Per-position mask,

`True`

uses the real token ID,`False`

uses -
([prompt_token_ids](https://docs.vllm.ai#vllm.inputs.llm.EmbedsPrompt.prompt_token_ids)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]Token IDs for mixed-mode inputs (chat completion with


## Source code in `vllm/inputs/llm.py`


###

`prompt`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm.EmbedsPrompt.prompt)

The prompt text corresponding to the token embeddings, if available.

###

`prompt_embeds`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm.EmbedsPrompt.prompt_embeds)

The embeddings of the prompt.

###

`prompt_is_token_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm.EmbedsPrompt.prompt_is_token_ids)

Per-position mask, `True`

uses the real token ID, `False`

uses the corresponding entry from `prompt_embeds`

. Must be the same length as `prompt_token_ids`

when both are set.

###

`prompt_token_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm.EmbedsPrompt.prompt_token_ids)

Token IDs for mixed-mode inputs (chat completion with `prompt_embeds`

content parts). The tokens at positions where `prompt_is_token_ids`

is `False`

are placeholder tokens that get replaced by entries from `prompt_embeds`

in the forward pass.

##

`ExplicitEncoderDecoderPrompt`

[¶](https://docs.vllm.ai#vllm.inputs.llm.ExplicitEncoderDecoderPrompt)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

Schema for a pair of encoder and decoder singleton prompts.

## Note

This schema is not valid for decoder-only models.

Attributes:

-
([decoder_prompt](https://docs.vllm.ai#vllm.inputs.llm.ExplicitEncoderDecoderPrompt.decoder_prompt)

) –[DecoderPrompt](https://docs.vllm.ai#vllm.inputs.llm.DecoderPrompt)| NoneThe prompt for the decoder part of the model.

-
([encoder_prompt](https://docs.vllm.ai#vllm.inputs.llm.ExplicitEncoderDecoderPrompt.encoder_prompt)

) –[EncoderPrompt](https://docs.vllm.ai#vllm.inputs.llm.EncoderPrompt)The prompt for the encoder part of the model.


## Source code in `vllm/inputs/llm.py`


##

`MultiModalDataBuiltins`

[¶](https://docs.vllm.ai#vllm.inputs.llm.MultiModalDataBuiltins)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

Type annotations for modality types predefined by vLLM.

Attributes:

-
([audio](https://docs.vllm.ai#vllm.inputs.llm.MultiModalDataBuiltins.audio)

) –[ModalityData](https://docs.vllm.ai#vllm.inputs.llm.ModalityData)[[AudioItem](https://docs.vllm.ai/multimodal/inputs/#vllm.multimodal.inputs.AudioItem)]The input audio(s).

-
([image](https://docs.vllm.ai#vllm.inputs.llm.MultiModalDataBuiltins.image)

) –[ModalityData](https://docs.vllm.ai#vllm.inputs.llm.ModalityData)[[ImageItem](https://docs.vllm.ai/multimodal/inputs/#vllm.multimodal.inputs.ImageItem)]The input image(s).

-
([video](https://docs.vllm.ai#vllm.inputs.llm.MultiModalDataBuiltins.video)

) –[ModalityData](https://docs.vllm.ai#vllm.inputs.llm.ModalityData)[[VideoItem](https://docs.vllm.ai/multimodal/inputs/#vllm.multimodal.inputs.VideoItem)]The input video(s).

-
([vision_chunk](https://docs.vllm.ai#vllm.inputs.llm.MultiModalDataBuiltins.vision_chunk)

) –[ModalityData](https://docs.vllm.ai#vllm.inputs.llm.ModalityData)[[VisionChunk](https://docs.vllm.ai/multimodal/inputs/#vllm.multimodal.inputs.VisionChunk)]The input visual atom(s) - unified modality for images and video chunks.


## Source code in `vllm/inputs/llm.py`


##

`TextPrompt`

[¶](https://docs.vllm.ai#vllm.inputs.llm.TextPrompt)

Bases: [_PromptOptions](https://docs.vllm.ai#vllm.inputs.llm._PromptOptions)

Schema for a text prompt.

Attributes:

## Source code in `vllm/inputs/llm.py`


###

`prompt`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm.TextPrompt.prompt)

The input text to be tokenized before passing to the model.

##

`TokensPrompt`

[¶](https://docs.vllm.ai#vllm.inputs.llm.TokensPrompt)

Bases: [_PromptOptions](https://docs.vllm.ai#vllm.inputs.llm._PromptOptions)

Schema for a tokenized prompt.

Attributes:

-
([prompt](https://docs.vllm.ai#vllm.inputs.llm.TokensPrompt.prompt)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The prompt text corresponding to the token IDs, if available.

-
([prompt_token_ids](https://docs.vllm.ai#vllm.inputs.llm.TokensPrompt.prompt_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]A list of token IDs to pass to the model.

-
([prompt_token_offsets](https://docs.vllm.ai#vllm.inputs.llm.TokensPrompt.prompt_token_offsets)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]] | None]Char-level (start, end) offsets per token, relative to the

-
([token_type_ids](https://docs.vllm.ai#vllm.inputs.llm.TokensPrompt.token_type_ids)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]A list of token type IDs to pass to the cross encoder model.


## Source code in `vllm/inputs/llm.py`


###

`prompt`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm.TokensPrompt.prompt)

The prompt text corresponding to the token IDs, if available.

###

`prompt_token_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm.TokensPrompt.prompt_token_ids)

A list of token IDs to pass to the model.

###

`prompt_token_offsets`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm.TokensPrompt.prompt_token_offsets)

Char-level (start, end) offsets per token, relative to the tokenized source string. Present only when offsets were requested AND a Fast (Rust-backed) tokenizer was used AND no multimodal data was present. The list length equals the length of `prompt_token_ids`

.

###

`token_type_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm.TokensPrompt.token_type_ids)

A list of token type IDs to pass to the cross encoder model.

##

`_PromptOptions`

[¶](https://docs.vllm.ai#vllm.inputs.llm._PromptOptions)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

Additional options available to all [ SingletonPrompt](https://docs.vllm.ai#vllm.inputs.llm.SingletonPrompt) types.

Attributes:

-
([cache_salt](https://docs.vllm.ai#vllm.inputs.llm._PromptOptions.cache_salt)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Optional cache salt to be used for prefix caching.

-
([media_io_kwargs](https://docs.vllm.ai#vllm.inputs.llm._PromptOptions.media_io_kwargs)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]] | None]Optional per-modality media loading and decoding arguments.

-
([mm_processor_kwargs](https://docs.vllm.ai#vllm.inputs.llm._PromptOptions.mm_processor_kwargs)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None]Optional multi-modal processor kwargs to be forwarded to the

-
([multi_modal_data](https://docs.vllm.ai#vllm.inputs.llm._PromptOptions.multi_modal_data)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[MultiModalDataDict](https://docs.vllm.ai#vllm.inputs.llm.MultiModalDataDict)| None]Optional multi-modal data to pass to the model,

-
([multi_modal_uuids](https://docs.vllm.ai#vllm.inputs.llm._PromptOptions.multi_modal_uuids)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[MultiModalUUIDDict](https://docs.vllm.ai#vllm.inputs.llm.MultiModalUUIDDict)]Optional user-specified UUIDs for multimodal items, mapped by modality.


## Source code in `vllm/inputs/llm.py`


###

`cache_salt`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm._PromptOptions.cache_salt)

Optional cache salt to be used for prefix caching.

###

`media_io_kwargs`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm._PromptOptions.media_io_kwargs)

Optional per-modality media loading and decoding arguments. Used only for hash derivation when using multi-modal UUIDs.

###

`mm_processor_kwargs`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm._PromptOptions.mm_processor_kwargs)

Optional multi-modal processor kwargs to be forwarded to the multimodal input mapper & processor. Note that if multiple modalities have registered mappers etc for the model being considered, we attempt to pass the mm_processor_kwargs to each of them.

###

`multi_modal_data`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm._PromptOptions.multi_modal_data)

Optional multi-modal data to pass to the model, if the model supports it.

###

`multi_modal_uuids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.inputs.llm._PromptOptions.multi_modal_uuids)

Optional user-specified UUIDs for multimodal items, mapped by modality. Lists must match the number of items per modality and may contain `None`

. For `None`

entries, the hasher will compute IDs automatically; non-None entries override the default hashes for caching, and MUST be unique per multimodal item.
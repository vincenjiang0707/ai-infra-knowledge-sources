source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cohere/cohere_chat_message/
lastmod: 2026-09-24

#

`vllm.entrypoints.cohere.cohere_chat_message`

[¶](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message)

vLLM chat-protocol extensions for grounded (citation-carrying) models.

This module keeps the OpenAI chat completion protocol classes (:class:`ChatMessage`

/ :class:`DeltaMessage`

) free of Cohere-specific fields. It provides two things:

- :class:
`Citation`

/ :class:`CitationSource`

: the vLLM-internal citation representation produced by the Cohere parser (:mod:`vllm.parser.cohere_command`

) and consumed by :mod:`vllm.entrypoints.cohere.serving`

. This is*not*the on-wire Cohere SDK shape -- that conversion happens in the serving layer. - :class:
`CohereChatMessage`

/ :class:`CohereDeltaMessage`

: :class:`ChatMessage`

/ :class:`DeltaMessage`

subclasses that add a`citations`

field. They are only instantiated by the citation-aware serving handler (:class:`vllm.entrypoints.cohere.serving.CohereServingChatV2`

) and by the Cohere reasoning parser's streaming path. Non-Cohere code paths continue to construct plain :class:`ChatMessage`

/ :class:`DeltaMessage`

.

The module intentionally does *not* import the `cohere`

Python SDK so the reasoning parser (which is Cohere-model-specific but ships without the SDK dependency) can import from here freely.

Classes:

-
–[Citation](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.Citation)A citation grounding a span of generated text in source material.

-
–[CitationSource](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.CitationSource)Source attribution for a :class:

`Citation`

. -
–[CohereChatMessage](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.CohereChatMessage):class:

`ChatMessage`

extension carrying grounding citations. -
–[CohereDeltaMessage](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.CohereDeltaMessage):class:

`DeltaMessage`

extension carrying grounding citations for streaming.

##

`Citation`

[¶](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.Citation)

Bases: `OpenAIBaseModel`


A citation grounding a span of generated text in source material.

vLLM-internal representation used by the Cohere reasoning parser and the Cohere v2 serving layer. This is not the on-wire Cohere SDK shape: conversion to the SDK's `cohere.types.Citation`

happens in :mod:`vllm.entrypoints.cohere.serving`

.

Attributes:

-
([content_index](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.Citation.content_index)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneIndex of the content block this citation refers to (when the message

-
([end](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.Citation.end)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneEnd character offset (exclusive) in the surrounding text content.

-
([sources](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.Citation.sources)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[CitationSource](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.CitationSource)]Source documents / tool outputs that ground this citation.

-
([start](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.Citation.start)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneStart character offset in the surrounding text content.

-
([text](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.Citation.text)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe cited text snippet.

-
([type](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.Citation.type)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['TEXT_CONTENT', 'THINKING_CONTENT', 'PLAN'] | NoneWhich kind of content block this citation grounds: the user-visible


## Source code in `vllm/entrypoints/cohere/cohere_chat_message.py`


###

`content_index = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.Citation.content_index)

Index of the content block this citation refers to (when the message has multiple content blocks).

###

`end = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.Citation.end)

End character offset (exclusive) in the surrounding text content.

###

`sources = Field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.Citation.sources)

Source documents / tool outputs that ground this citation.

###

`start = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.Citation.start)

Start character offset in the surrounding text content.

###

`text = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.Citation.text)

The cited text snippet.

###

`type = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.Citation.type)

Which kind of content block this citation grounds: the user-visible text (`TEXT_CONTENT`

), a thinking block (`THINKING_CONTENT`

), or a tool-plan block (`PLAN`

). `None`

means unspecified.

##

`CitationSource`

[¶](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.CitationSource)

Bases: `OpenAIBaseModel`


Source attribution for a :class:`Citation`

.

Mirrors the shape used by Cohere's Chat v2 API. `type`

is the source discriminator (`document`

or `tool`

); `id`

is the citing document/tool-output identifier; `document`

and `tool_output`

carry the original payload that produced the citation.

Sources are fully resolved by the parser at emit time (see :func:`_melody_sources_to_vllm`

in :mod:`vllm.parser.cohere_command`

) using the `POSITION_TO_SOURCE_KEY`

map forwarded through `chat_template_kwargs`

by :meth:`vllm.entrypoints.cohere.serving.CohereServingChatV2._apply_cohere_template_kwargs`

. That means every instance that reaches the serving / wire layer already has `type`

/ `id`

populated; the serving layer only has to coerce to :class:`cohere.types.Citation`

and rewrite `THINKING_CONTENT`

-> `PLAN`

for non-reasoning models.

## Source code in `vllm/entrypoints/cohere/cohere_chat_message.py`


##

`CohereChatMessage`

[¶](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.CohereChatMessage)

Bases: `ChatMessage`


:class:`ChatMessage`

extension carrying grounding citations.

Only instantiated by :class:`CohereServingChatV2`

(and any other :class:`OpenAIServingChat`

subclass that opts in by overriding `_create_chat_message`

). Regular OpenAI-compatible handlers keep emitting plain :class:`ChatMessage`

so their response schema is unchanged.

The response envelope declares `message: SerializeAsAny[ChatMessage]`

, so pydantic serializes this subclass with its own schema (including `citations`

) when it flows through :class:`ChatCompletionResponseChoice`

.

## Source code in `vllm/entrypoints/cohere/cohere_chat_message.py`


##

`CohereDeltaMessage`

[¶](https://docs.vllm.ai#vllm.entrypoints.cohere.cohere_chat_message.CohereDeltaMessage)

Bases: `DeltaMessage`


:class:`DeltaMessage`

extension carrying grounding citations for streaming.

Emitted by :class:`vllm.parser.cohere_command.CohereCommandParser`

on delta events whose payload includes citations. Non-Cohere parsers return plain :class:`DeltaMessage`

, so their streamed shape is unchanged.

The response envelope declares `delta: SerializeAsAny[DeltaMessage]`

, so pydantic serializes this subclass with its own schema when it flows through :class:`ChatCompletionResponseStreamChoice`

.
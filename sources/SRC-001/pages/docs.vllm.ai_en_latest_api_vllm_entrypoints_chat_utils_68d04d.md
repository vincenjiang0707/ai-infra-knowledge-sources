source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/chat_utils/
lastmod: 2026-09-24

#

`vllm.entrypoints.chat_utils`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils)

Classes:

-
–[AsyncMultiModalContentParser](https://docs.vllm.ai#vllm.entrypoints.chat_utils.AsyncMultiModalContentParser) -
–[AudioURL](https://docs.vllm.ai#vllm.entrypoints.chat_utils.AudioURL) -
–[BaseMultiModalItemTracker](https://docs.vllm.ai#vllm.entrypoints.chat_utils.BaseMultiModalItemTracker)Tracks multi-modal items in a given request and ensures that the number

-
–[ChatCompletionContentPartAudioEmbedsParam](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartAudioEmbedsParam) -
–[ChatCompletionContentPartAudioParam](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartAudioParam) -
–[ChatCompletionContentPartImageEmbedsParam](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartImageEmbedsParam) -
–[ChatCompletionContentPartPromptEmbedsParam](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartPromptEmbedsParam) -
–[ChatCompletionContentPartVideoEmbedsParam](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartVideoEmbedsParam) -
–[ChatCompletionContentPartVideoParam](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartVideoParam) -
–[ChatTemplateResolutionError](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatTemplateResolutionError)Raised when chat template resolution fails.

-
–[ConversationMessage](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage) -
–[CustomChatCompletionContentPILImageParam](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionContentPILImageParam)A simpler version of the param that only accepts a PIL image.

-
–[CustomChatCompletionContentSimpleAudioParam](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionContentSimpleAudioParam)A simpler version of the param that only accepts a plain audio_url.

-
–[CustomChatCompletionContentSimpleImageParam](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionContentSimpleImageParam)A simpler version of the param that only accepts a plain image_url.

-
–[CustomChatCompletionContentSimpleVideoParam](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionContentSimpleVideoParam)A simpler version of the param that only accepts a plain audio_url.

-
–[CustomChatCompletionContentToolReferenceParam](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionContentToolReferenceParam)A tool reference content param that only accepts a plain tool name.

-
–[CustomChatCompletionMessageParam](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionMessageParam)Enables custom roles in the Chat Completion API.

-
–[CustomThinkCompletionContentParam](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomThinkCompletionContentParam)A Think Completion Content Param that accepts a plain text and a boolean.

-
–[MultiModalContentParser](https://docs.vllm.ai#vllm.entrypoints.chat_utils.MultiModalContentParser) -
–[PILImage](https://docs.vllm.ai#vllm.entrypoints.chat_utils.PILImage)A PIL.Image.Image object.

-
–[VideoURL](https://docs.vllm.ai#vllm.entrypoints.chat_utils.VideoURL)

Functions:

-
–[get_tool_call_id_type](https://docs.vllm.ai#vllm.entrypoints.chat_utils.get_tool_call_id_type)Return the tool-call ID type for a given model configuration.

-
–[validate_chat_template](https://docs.vllm.ai#vllm.entrypoints.chat_utils.validate_chat_template)Raises if the provided chat template appears invalid.


Attributes:

-
([PROMPT_EMBEDS_PLACEHOLDER_TOKEN](https://docs.vllm.ai#vllm.entrypoints.chat_utils.PROMPT_EMBEDS_PLACEHOLDER_TOKEN)

) –[Final](https://docs.python.org/3/library/typing.html#typing.Final)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The special token used as a placeholder for each embedding


##

`PROMPT_EMBEDS_PLACEHOLDER_TOKEN = '<prompt_embeds>'`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.PROMPT_EMBEDS_PLACEHOLDER_TOKEN)

The special token used as a placeholder for each embedding position during chat template rendering.

Registered as an additional special token when `--enable-prompt-embeds`

is set. See `_ensure_prompt_embeds_placeholder_token`

in `vllm/renderers/hf.py`

.

##

`AsyncMultiModalContentParser`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.AsyncMultiModalContentParser)

Bases: `BaseMultiModalContentParser`


Methods:

-
–[parse_prompt_embeds](https://docs.vllm.ai#vllm.entrypoints.chat_utils.AsyncMultiModalContentParser.parse_prompt_embeds)Schedule async prompt embeds decode and store the coroutine in the tracker.


## Source code in `vllm/entrypoints/chat_utils.py`


|
|

###

`parse_prompt_embeds(data)`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.AsyncMultiModalContentParser.parse_prompt_embeds)

Schedule async prompt embeds decode and store the coroutine in the tracker.

Like the sync variant, emits a single sentinel `PROMPT_EMBEDS_PLACEHOLDER_TOKEN`

per content part. Unlike the sync variant, the tensor decode is deferred to a thread-pool executor via `safe_load_prompt_embeds_async`

.

## Source code in `vllm/entrypoints/chat_utils.py`


##

`AudioURL`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.AudioURL)

##

`BaseMultiModalItemTracker`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.BaseMultiModalItemTracker)

Tracks multi-modal items in a given request and ensures that the number of multi-modal items in a given request does not exceed the configured maximum per prompt.

Methods:

-
–[add](https://docs.vllm.ai#vllm.entrypoints.chat_utils.BaseMultiModalItemTracker.add)Add a multi-modal item to the current prompt and returns the


Attributes:

-
([use_unified_vision_chunk_modality](https://docs.vllm.ai#vllm.entrypoints.chat_utils.BaseMultiModalItemTracker.use_unified_vision_chunk_modality)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Check if model uses unified vision_chunk modality for images/videos.


## Source code in `vllm/entrypoints/chat_utils.py`


|
|

###

`use_unified_vision_chunk_modality`

`cached`

`property`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.BaseMultiModalItemTracker.use_unified_vision_chunk_modality)

Check if model uses unified vision_chunk modality for images/videos.

###

`_validate_add(modality)`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.BaseMultiModalItemTracker._validate_add)

Validate that one more item of the modality can be tracked.

## Source code in `vllm/entrypoints/chat_utils.py`


###

`add(modality, item)`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.BaseMultiModalItemTracker.add)

Add a multi-modal item to the current prompt and returns the placeholder string to use, if any.

An optional uuid can be added which serves as a unique identifier of the media.

## Note

`prompt_embeds`

bypass MM-processor validation because they are pre-computed embeddings that do not go through any HF processor, encoder, or model-specific placeholder logic. The corresponding placeholder string is managed by the parser via `_add_placeholder`

, so we return None here.

## Source code in `vllm/entrypoints/chat_utils.py`


##

`ChatCompletionContentPartAudioEmbedsParam`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartAudioEmbedsParam)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

Attributes:

-
([audio_embeds](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartAudioEmbedsParam.audio_embeds)`MultiModalEmbedsPayload | None`

) –The audio embeddings. It can be either:

-
([type](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartAudioEmbedsParam.type)

) –[Required](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Required)[[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['audio_embeds']]The type of the content part.

-
([uuid](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartAudioEmbedsParam.uuid)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneUser-provided UUID of a media. User must guarantee that it is properly


## Source code in `vllm/entrypoints/chat_utils.py`


###

`audio_embeds`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartAudioEmbedsParam.audio_embeds)

The audio embeddings. It can be either: - A single base64 string representing a serialized torch tensor. - A dictionary of base64 tensors or numeric JSON metadata arrays.

###

`type`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartAudioEmbedsParam.type)

The type of the content part.

###

`uuid`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartAudioEmbedsParam.uuid)

User-provided UUID of a media. User must guarantee that it is properly generated and unique for different medias.

##

`ChatCompletionContentPartAudioParam`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartAudioParam)

##

`ChatCompletionContentPartImageEmbedsParam`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartImageEmbedsParam)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

Attributes:

-
([image_embeds](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartImageEmbedsParam.image_embeds)`MultiModalEmbedsPayload | None`

) –The image embeddings. It can be either:

-
([type](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartImageEmbedsParam.type)

) –[Required](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Required)[[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['image_embeds']]The type of the content part.

-
([uuid](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartImageEmbedsParam.uuid)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneUser-provided UUID of a media. User must guarantee that it is properly


## Source code in `vllm/entrypoints/chat_utils.py`


###

`image_embeds`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartImageEmbedsParam.image_embeds)

The image embeddings. It can be either: - A single base64 string. - A dictionary of base64 tensors or numeric JSON metadata arrays.

###

`type`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartImageEmbedsParam.type)

The type of the content part.

###

`uuid`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartImageEmbedsParam.uuid)

User-provided UUID of a media. User must guarantee that it is properly generated and unique for different medias.

##

`ChatCompletionContentPartPromptEmbedsParam`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartPromptEmbedsParam)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

Attributes:

-
([data](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartPromptEmbedsParam.data)

) –[Required](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Required)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Base64-encoded bytes of a serialized

`torch.Tensor`

of shape -
([type](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartPromptEmbedsParam.type)

) –[Required](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Required)[[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['prompt_embeds']]The type of the content part.


## Source code in `vllm/entrypoints/chat_utils.py`


##

`ChatCompletionContentPartVideoEmbedsParam`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartVideoEmbedsParam)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

Attributes:

-
([type](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartVideoEmbedsParam.type)

) –[Required](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Required)[[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['video_embeds']]The type of the content part.

-
([uuid](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartVideoEmbedsParam.uuid)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneUser-provided UUID of a media. User must guarantee that it is properly

-
([video_embeds](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartVideoEmbedsParam.video_embeds)`MultiModalEmbedsPayload | None`

) –The video embeddings. It can be either:


## Source code in `vllm/entrypoints/chat_utils.py`


###

`type`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartVideoEmbedsParam.type)

The type of the content part.

###

`uuid`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartVideoEmbedsParam.uuid)

User-provided UUID of a media. User must guarantee that it is properly generated and unique for different medias.

###

`video_embeds`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartVideoEmbedsParam.video_embeds)

The video embeddings. It can be either: - A single base64 string representing a serialized torch tensor. - A dictionary of base64 tensors or numeric JSON metadata arrays.

##

`ChatCompletionContentPartVideoParam`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatCompletionContentPartVideoParam)

##

`ChatTemplateResolutionError`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ChatTemplateResolutionError)

Bases: [ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)

Raised when chat template resolution fails.

This is a subclass of ValueError for backward compatibility with existing exception handlers.

##

`ConversationMessage`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

Attributes:

-
([content](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage.content)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None |[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]The contents of the message

-
([name](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage.name)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe name of the function to call

-
([reasoning](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage.reasoning)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe reasoning content for interleaved thinking.

-
([reasoning_content](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage.reasoning_content)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneDeprecated: The reasoning content for interleaved thinking.

-
([role](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage.role)

) –[Required](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Required)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The role of the message's author.

-
([task](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage.task)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneModel-specific task marker. Currently passed through for DeepSeek V4.

-
([tool_call_id](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage.tool_call_id)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneTool call that this message is responding to.

-
([tool_calls](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage.tool_calls)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ChatCompletionMessageToolCallParam] | NoneThe tool calls generated by the model, such as function calls.

-
([tools](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage.tools)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ChatCompletionFunctionToolParam] | NoneThe tools for developer role.


## Source code in `vllm/entrypoints/chat_utils.py`


###

`content`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage.content)

The contents of the message

###

`name`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage.name)

The name of the function to call

###

`reasoning`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage.reasoning)

The reasoning content for interleaved thinking.

###

`reasoning_content`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage.reasoning_content)

Deprecated: The reasoning content for interleaved thinking.

###

`role`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage.role)

The role of the message's author.

###

`task`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage.task)

Model-specific task marker. Currently passed through for DeepSeek V4.

###

`tool_call_id`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage.tool_call_id)

Tool call that this message is responding to.

###

`tool_calls`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage.tool_calls)

The tool calls generated by the model, such as function calls.

###

`tools`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.ConversationMessage.tools)

The tools for developer role.

##

`CustomChatCompletionContentPILImageParam`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionContentPILImageParam)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

A simpler version of the param that only accepts a PIL image.

Example: { "image_pil": ImageAsset('cherry_blossom').pil_image }

Attributes:

## Source code in `vllm/entrypoints/chat_utils.py`


###

`uuid`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionContentPILImageParam.uuid)

User-provided UUID of a media. User must guarantee that it is properly generated and unique for different medias.

##

`CustomChatCompletionContentSimpleAudioParam`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionContentSimpleAudioParam)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

A simpler version of the param that only accepts a plain audio_url.

Example: { "audio_url": "https://example.com/audio.mp3" }

## Source code in `vllm/entrypoints/chat_utils.py`


##

`CustomChatCompletionContentSimpleImageParam`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionContentSimpleImageParam)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

A simpler version of the param that only accepts a plain image_url. This is supported by OpenAI API, although it is not documented.

Example: { "image_url": "https://example.com/image.jpg" }

Attributes:

## Source code in `vllm/entrypoints/chat_utils.py`


###

`uuid`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionContentSimpleImageParam.uuid)

User-provided UUID of a media. User must guarantee that it is properly generated and unique for different medias.

##

`CustomChatCompletionContentSimpleVideoParam`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionContentSimpleVideoParam)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

A simpler version of the param that only accepts a plain audio_url.

Example: { "video_url": "https://example.com/video.mp4" }

Attributes:

## Source code in `vllm/entrypoints/chat_utils.py`


###

`uuid`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionContentSimpleVideoParam.uuid)

User-provided UUID of a media. User must guarantee that it is properly generated and unique for different medias.

##

`CustomChatCompletionContentToolReferenceParam`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionContentToolReferenceParam)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

A tool reference content param that only accepts a plain tool name.

Example: { "name": "get_weather", "type": "tool_reference" }

Attributes:

-
([name](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionContentToolReferenceParam.name)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The name of the tool being referenced.

-
([type](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionContentToolReferenceParam.type)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['tool_reference']The content type.


## Source code in `vllm/entrypoints/chat_utils.py`


##

`CustomChatCompletionMessageParam`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionMessageParam)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

Enables custom roles in the Chat Completion API.

Attributes:

-
([content](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionMessageParam.content)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)|[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ChatCompletionContentPartParam]The contents of the message.

-
([name](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionMessageParam.name)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)An optional name for the participant.

-
([reasoning](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionMessageParam.reasoning)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe reasoning content for interleaved thinking.

-
([role](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionMessageParam.role)

) –[Required](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Required)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The role of the message's author.

-
([task](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionMessageParam.task)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneModel-specific task marker. Currently passed through for DeepSeek V4.

-
([tool_call_id](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionMessageParam.tool_call_id)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneTool call that this message is responding to.

-
([tool_calls](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionMessageParam.tool_calls)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ChatCompletionMessageToolCallParam] | NoneThe tool calls generated by the model, such as function calls.

-
([tools](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionMessageParam.tools)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ChatCompletionFunctionToolParam] | NoneThe tools for developer role.


## Source code in `vllm/entrypoints/chat_utils.py`


###

`content`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionMessageParam.content)

The contents of the message.

###

`name`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionMessageParam.name)

An optional name for the participant.

Provides the model information to differentiate between participants of the same role.

###

`reasoning`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionMessageParam.reasoning)

The reasoning content for interleaved thinking.

###

`role`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionMessageParam.role)

The role of the message's author.

###

`task`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionMessageParam.task)

Model-specific task marker. Currently passed through for DeepSeek V4.

###

`tool_call_id`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionMessageParam.tool_call_id)

Tool call that this message is responding to.

###

`tool_calls`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionMessageParam.tool_calls)

The tool calls generated by the model, such as function calls.

###

`tools`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomChatCompletionMessageParam.tools)

The tools for developer role.

##

`CustomThinkCompletionContentParam`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomThinkCompletionContentParam)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

A Think Completion Content Param that accepts a plain text and a boolean.

Example: { "thinking": "I am thinking about the answer", "closed": True, "type": "thinking" }

Attributes:

-
([closed](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomThinkCompletionContentParam.closed)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether the thinking is closed.

-
([thinking](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomThinkCompletionContentParam.thinking)

) –[Required](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Required)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The thinking content.

-
([type](https://docs.vllm.ai#vllm.entrypoints.chat_utils.CustomThinkCompletionContentParam.type)

) –[Required](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Required)[[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['thinking']]The thinking type.


## Source code in `vllm/entrypoints/chat_utils.py`


##

`MultiModalContentParser`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.MultiModalContentParser)

Bases: `BaseMultiModalContentParser`


Methods:

-
–[parse_prompt_embeds](https://docs.vllm.ai#vllm.entrypoints.chat_utils.MultiModalContentParser.parse_prompt_embeds)Decode a base64 prompt embeds tensor and store it in the tracker.


## Source code in `vllm/entrypoints/chat_utils.py`


|
|

###

`parse_prompt_embeds(data)`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.MultiModalContentParser.parse_prompt_embeds)

Decode a base64 prompt embeds tensor and store it in the tracker.

Emits a single `PROMPT_EMBEDS_PLACEHOLDER_TOKEN`

sentinel per content part. The renderer later expands each sentinel to a span of `tensor.shape[0]`

placeholder tokens after tokenization.

## Source code in `vllm/entrypoints/chat_utils.py`


##

`PILImage`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.PILImage)

##

`VideoURL`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.VideoURL)

##

`_get_full_multimodal_text_prompt(placeholder_storage, texts, interleave_strings, multimodal_content_part_separator='\n')`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils._get_full_multimodal_text_prompt)

Combine multimodal prompts for a multimodal language model.

## Source code in `vllm/entrypoints/chat_utils.py`


##

`_parse_chat_message_content_mm_part(part)`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils._parse_chat_message_content_mm_part)

Parses a given multi-modal content part based on its type.

Parameters:

-

(`part`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils._parse_chat_message_content_mm_part(part))`ChatCompletionContentPartParam`

) –A dict containing the content part, with a potential 'type' field.


Returns:

-

–[str](https://docs.python.org/3/builtins/stdtypes.html#str)A tuple (part_type, content) where:

-
`_ContentPart`

–- part_type: Type of the part (e.g., 'text', 'image_url').

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), _ContentPart]- content: Parsed content (e.g., text, image URL).


Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If the 'type' field is missing and no direct URL is found.


## Source code in `vllm/entrypoints/chat_utils.py`


|
|

##

`_parse_chat_message_content_part(part, mm_parser, *, wrap_dicts, interleave_strings)`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils._parse_chat_message_content_part)

Parses a single part of a conversation. If wrap_dicts is True, structured dictionary pieces for texts and images will be wrapped in dictionaries, i.e., {"type": "text", "text", ...} and {"type": "image"}, respectively. Otherwise multimodal data will be handled by mm_parser, and texts will be returned as strings to be joined with multimodal placeholders.

## Source code in `vllm/entrypoints/chat_utils.py`


|
|

##

`_reject_reserved_placeholder_in_text(text, model_config)`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils._reject_reserved_placeholder_in_text)

Reject user-supplied text parts that contains the reserved `prompt_embeds`

placeholder sentinel.

When the server accepts `prompt_embeds`

, the placeholder token is registered as a single unsplittable special token on the tokenizer. Any user text that happens to contain the literal sequence would tokenize to the same ID and be mistaken for a splice point by the renderer, letting a caller move or inject splice positions via plain text content.

## Source code in `vllm/entrypoints/chat_utils.py`


##

`_resolve_items(items_by_modality, mm_processor, modality_order)`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils._resolve_items)

Materialize the tracker's per-modality items into `mm_data`

/ `mm_uuids`

.

## Note

`mm_processor`

is `None`

for text-only models (no registered HF processor) whose only modality is `prompt_embeds`

. Every other modality requires a processor, enforced by the guard below.

## Source code in `vllm/entrypoints/chat_utils.py`


|
|

##

`get_tool_call_id_type(model_config)`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.get_tool_call_id_type)

Return the tool-call ID type for a given model configuration.

## Source code in `vllm/entrypoints/chat_utils.py`


##

`validate_chat_template(chat_template)`

[¶](https://docs.vllm.ai#vllm.entrypoints.chat_utils.validate_chat_template)

Raises if the provided chat template appears invalid.
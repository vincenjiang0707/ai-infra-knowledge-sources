source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/anthropic/protocol/
lastmod: 2026-09-23

#

`vllm.entrypoints.anthropic.protocol`

[¶](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol)

Pydantic models for Anthropic API protocol.

Classes:

-
–[AnthropicContentBlock](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicContentBlock)Content block in message.

-
–[AnthropicContextManagement](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicContextManagement)Context management information for token counting.

-
–[AnthropicCountTokensRequest](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicCountTokensRequest)Anthropic messages.count_tokens request.

-
–[AnthropicCountTokensResponse](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicCountTokensResponse)Anthropic messages.count_tokens response.

-
–[AnthropicDelta](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicDelta)Delta for streaming responses.

-
–[AnthropicError](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicError)Error structure for Anthropic API.

-
–[AnthropicErrorResponse](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicErrorResponse)Error response structure for Anthropic API.

-
–[AnthropicJsonOutputFormat](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicJsonOutputFormat)JSON output format configuration.

-
–[AnthropicMessage](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicMessage)Message structure.

-
–[AnthropicMessagesRequest](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicMessagesRequest)Anthropic Messages API request.

-
–[AnthropicMessagesResponse](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicMessagesResponse)Anthropic Messages API response.

-
–[AnthropicOutputConfig](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicOutputConfig)Configuration options for the model's output, such as the output format.

-
–[AnthropicStreamEvent](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicStreamEvent)Streaming event.

-
–[AnthropicTool](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicTool)Tool definition.

-
–[AnthropicToolChoice](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicToolChoice)Tool Choice definition.

-
–[AnthropicUsage](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicUsage)Token usage information.


##

`AnthropicContentBlock`

[¶](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicContentBlock)

Bases: `BaseModel`


Content block in message.

## Source code in `vllm/entrypoints/anthropic/protocol.py`


##

`AnthropicContextManagement`

[¶](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicContextManagement)

##

`AnthropicCountTokensRequest`

[¶](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicCountTokensRequest)

Bases: `BaseModel`


Anthropic messages.count_tokens request.

## Source code in `vllm/entrypoints/anthropic/protocol.py`


##

`AnthropicCountTokensResponse`

[¶](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicCountTokensResponse)

Bases: `BaseModel`


Anthropic messages.count_tokens response.

## Source code in `vllm/entrypoints/anthropic/protocol.py`


##

`AnthropicDelta`

[¶](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicDelta)

Bases: `BaseModel`


Delta for streaming responses.

## Source code in `vllm/entrypoints/anthropic/protocol.py`


##

`AnthropicError`

[¶](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicError)

##

`AnthropicErrorResponse`

[¶](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicErrorResponse)

##

`AnthropicJsonOutputFormat`

[¶](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicJsonOutputFormat)

Bases: `BaseModel`


JSON output format configuration.

## Source code in `vllm/entrypoints/anthropic/protocol.py`


##

`AnthropicMessage`

[¶](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicMessage)

##

`AnthropicMessagesRequest`

[¶](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicMessagesRequest)

Bases: `BaseModel`


Anthropic Messages API request.

## Source code in `vllm/entrypoints/anthropic/protocol.py`


##

`AnthropicMessagesResponse`

[¶](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicMessagesResponse)

Bases: `BaseModel`


Anthropic Messages API response.

## Source code in `vllm/entrypoints/anthropic/protocol.py`


##

`AnthropicOutputConfig`

[¶](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicOutputConfig)

Bases: `BaseModel`


Configuration options for the model's output, such as the output format.

## Source code in `vllm/entrypoints/anthropic/protocol.py`


##

`AnthropicStreamEvent`

[¶](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicStreamEvent)

Bases: `BaseModel`


Streaming event.

## Source code in `vllm/entrypoints/anthropic/protocol.py`


##

`AnthropicTool`

[¶](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicTool)

Bases: `BaseModel`


Tool definition.

## Source code in `vllm/entrypoints/anthropic/protocol.py`


##

`AnthropicToolChoice`

[¶](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicToolChoice)

Bases: `BaseModel`


Tool Choice definition.

## Source code in `vllm/entrypoints/anthropic/protocol.py`


##

`AnthropicUsage`

[¶](https://docs.vllm.ai#vllm.entrypoints.anthropic.protocol.AnthropicUsage)

Bases: `BaseModel`


Token usage information.
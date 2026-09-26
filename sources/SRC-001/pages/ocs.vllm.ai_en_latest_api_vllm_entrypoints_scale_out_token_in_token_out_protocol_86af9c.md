source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/scale_out/token_in_token_out/protocol/
lastmod: 2026-09-24

#

`vllm.entrypoints.scale_out.token_in_token_out.protocol`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol)

Classes:

-
–[DerenderChatRequest](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatRequest)Request for the /v1/chat/completions/derender endpoint (non-streaming).

-
–[DerenderChatStreamRequest](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatStreamRequest)One chunk streaming derender request for /v1/chat/completions/derender.

-
–[DerenderChatStreamResponse](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatStreamResponse)Response for one streaming chat derender chunk.

-
–[DerenderCompletionRequest](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionRequest)Request for the /v1/completions/derender endpoint (non-streaming).

-
–[DerenderCompletionStreamRequest](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionStreamRequest)One chunk streaming derender request for /v1/completions/derender.

-
–[DerenderCompletionStreamResponse](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionStreamResponse)Response for one streaming completions derender chunk.

-
–[DerenderStreamState](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState)Per sequence state for stateless streaming derender.

-
–[GenerateRequest](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.GenerateRequest) -
–[MultiModalFeatures](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.MultiModalFeatures)Lightweight multimodal metadata produced by the render step.

-
–[PlaceholderRangeInfo](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.PlaceholderRangeInfo)Serializable placeholder location for a single multi-modal item.


##

`DerenderChatRequest`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatRequest)

Bases: `BaseModel`


Request for the /v1/chat/completions/derender endpoint (non-streaming).

Wraps a complete GenerateResponse and caller supplied metadata needed to produce a fully formed ChatCompletionResponse without a GPU.

Attributes:

-
([chat_request](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatRequest.chat_request)

) –[ChatCompletionRequest](https://docs.vllm.ai/openai/chat_completion/protocol/#vllm.entrypoints.openai.chat_completion.protocol.ChatCompletionRequest)| NoneThe original (post-adjust_request) ChatCompletionRequest from /render.

-
([generate_response](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatRequest.generate_response)`GenerateResponse`

) –The complete token-in / token-out engine response to derender.

-
([model](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatRequest.model)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneServed model name. Defaults to the server's served model name.

-
([prompt_tokens](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatRequest.prompt_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NonePrompt token count for usage; defaults to 0 if omitted.


## Source code in `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`


###

`chat_request = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatRequest.chat_request)

The original (post-adjust_request) ChatCompletionRequest from /render.

Required by the parsing so that tool/reasoning parsers can receive the full request context they expect (request.tools, request.tool_choice, request._grammar_from_parser, etc.).

###

`generate_response`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatRequest.generate_response)

The complete token-in / token-out engine response to derender.

###

`model = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatRequest.model)

Served model name. Defaults to the server's served model name.

###

`prompt_tokens = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatRequest.prompt_tokens)

Prompt token count for usage; defaults to 0 if omitted.

GenerateResponse carries only output tokens; the caller already has len(GenerateRequest.token_ids) from the render step.

##

`DerenderChatStreamRequest`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatStreamRequest)

Bases: `BaseModel`


One chunk streaming derender request for /v1/chat/completions/derender.

The client sends one request per SSE chunk received from `/inference/v1/generate`

. Each request carries the generate chunk plus the `stream_state`

returned by the previous call (`None`

on the first call). The response contains the derendered chunk and the updated state to be passed to the next call.

This implements stateless no server side session. All mutable state lives in the client carried `stream_state`

.

Attributes:

-
([chat_request](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatStreamRequest.chat_request)

) –[ChatCompletionRequest](https://docs.vllm.ai/openai/chat_completion/protocol/#vllm.entrypoints.openai.chat_completion.protocol.ChatCompletionRequest)| NoneThe original (post adjust_request) ChatCompletionRequest from /render.

-
([generate_chunk](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatStreamRequest.generate_chunk)`GenerateStreamResponse`

) –One SSE chunk from

`/inference/v1/generate`

(`stream=True`

). -
([prompt_token_ids](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatStreamRequest.prompt_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NonePrompt token IDs. Required by the parser path's

`parse_delta`

to -
([prompt_tokens](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatStreamRequest.prompt_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NonePrompt token count for usage. Forwarded from the render step.

-
([stream_state](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatStreamRequest.stream_state)

) –[DerenderStreamState](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState)| NoneClient carried detok state from the previous call.

`None`

on first.

## Source code in `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`


###

`chat_request = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatStreamRequest.chat_request)

The original (post adjust_request) ChatCompletionRequest from /render.

###

`generate_chunk`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatStreamRequest.generate_chunk)

One SSE chunk from `/inference/v1/generate`

(`stream=True`

).

###

`prompt_token_ids = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatStreamRequest.prompt_token_ids)

Prompt token IDs. Required by the parser path's `parse_delta`

to settle its initial reasoning state (e.g. chat templates that pre-open `<think>`

). `prompt_tokens`

is a usage count and cannot serve this purpose. Sourced from `GenerateRequest.token_ids`

at the render step.

Rejected with a 400 (by `ServingDerender`

) when a tool or reasoning parser is configured and this is omitted. Without it, `parse_delta`

cannot tell whether the prompt left reasoning open and would silently misclassify reasoning content as plain content. Unused on the plain detokenization path.

###

`prompt_tokens = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatStreamRequest.prompt_tokens)

Prompt token count for usage. Forwarded from the render step.

###

`stream_state = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatStreamRequest.stream_state)

Client carried detok state from the previous call. `None`

on first.

##

`DerenderChatStreamResponse`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderChatStreamResponse)

Bases: `BaseModel`


Response for one streaming chat derender chunk.

Pairs the derendered SSE chunk with the updated client carried state to pass to the next call.

## Source code in `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`


##

`DerenderCompletionRequest`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionRequest)

Bases: `BaseModel`


Request for the /v1/completions/derender endpoint (non-streaming).

Parallel to DerenderChatRequest but handles the multi-prompt completions case: one GenerateResponse per prompt, mirroring the list[GenerateRequest] returned by /v1/completions/render.

Attributes:

-
([completion_request](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionRequest.completion_request)

) –[CompletionRequest](https://docs.vllm.ai/openai/completion/protocol/#vllm.entrypoints.openai.completion.protocol.CompletionRequest)| NoneThe original (post-adjust_request) CompletionRequest from /render.

-
([generate_responses](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionRequest.generate_responses)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[GenerateResponse]One response per prompt, parallel to the list[GenerateRequest]

-
([model](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionRequest.model)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneServed model name. Defaults to the server's served model name.

-
([prompt_tokens](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionRequest.prompt_tokens)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneOne prompt token count per response; each defaults to 0 if omitted.


## Source code in `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`


###

`completion_request = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionRequest.completion_request)

The original (post-adjust_request) CompletionRequest from /render.

Mirrors chat_request on DerenderChatRequest. Required by the parsing so parsers receive the full request context.

###

`generate_responses`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionRequest.generate_responses)

One response per prompt, parallel to the list[GenerateRequest] returned by /v1/completions/render.

###

`model = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionRequest.model)

Served model name. Defaults to the server's served model name.

###

`prompt_tokens = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionRequest.prompt_tokens)

One prompt token count per response; each defaults to 0 if omitted.

If provided, len(prompt_tokens) must equal len(generate_responses).

##

`DerenderCompletionStreamRequest`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionStreamRequest)

Bases: `BaseModel`


One chunk streaming derender request for /v1/completions/derender.

Parallel to `DerenderChatStreamRequest`

for the completions endpoint. Each call processes one SSE chunk (one output sequence's delta) and returns the derendered chunk plus updated state.

Attributes:

-
([completion_request](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionStreamRequest.completion_request)

) –[CompletionRequest](https://docs.vllm.ai/openai/completion/protocol/#vllm.entrypoints.openai.completion.protocol.CompletionRequest)| NoneThe original (post adjust_request) CompletionRequest from /render.

-
([generate_chunk](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionStreamRequest.generate_chunk)`GenerateStreamResponse`

) –One SSE chunk from

`/inference/v1/generate`

. -
([prompt_tokens](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionStreamRequest.prompt_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NonePrompt token count for usage.

-
([stream_state](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionStreamRequest.stream_state)

) –[DerenderStreamState](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState)| NoneClient-carried detok state.

`None`

on the first call.

## Source code in `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`


###

`completion_request = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionStreamRequest.completion_request)

The original (post adjust_request) CompletionRequest from /render.

###

`generate_chunk`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionStreamRequest.generate_chunk)

One SSE chunk from `/inference/v1/generate`

.

###

`prompt_tokens = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionStreamRequest.prompt_tokens)

Prompt token count for usage.

###

`stream_state = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionStreamRequest.stream_state)

Client-carried detok state. `None`

on the first call.

##

`DerenderCompletionStreamResponse`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderCompletionStreamResponse)

Bases: `BaseModel`


Response for one streaming completions derender chunk.

Parallel to `DerenderChatStreamResponse`

for the completions endpoint.

## Source code in `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`


##

`DerenderStreamState`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState)

Bases: `BaseModel`


Per sequence state for stateless streaming derender.

The client carries this between successive per chunk HTTP calls to the streaming derender endpoint. All fields are plain JSON serializable data. No opaque tokenizer or parser internals are stored here.

Two separate sets of fields support two different streaming modes:

- For plain streaming (no parser configured including the completions path):
`prev_tokens`

,`prefix_offset`

and`read_offset`

maintain a bounded incremental decoding window. This requires O(window) transport and O(delta) computation per chunk. - For parser enabled chat streaming:
`output_token_ids`

,`output_chunk_lens`

,`tools_streamed`

and`last_tool_call_ids`

are used to replay`parse_delta()`

from scratch on every chunk because parser state cannot be serialized. This incurs O(n) transport per chunk (O(n²) per generation) and O(n²)`parse_delta()`

calls per generation. Since many parsers re-scan the entire accumulated text on each invocation,`parse_delta()`

itself is O(n) yielding a true worst case compute cost of O(n³) per generation. No caching is performed. Work is bounded by`max_model_len`

. See`OnlineDerenderer._derender_chat_stream_parsed`

.

The detokenization strategy carries the incremental decode offsets directly rather than re-sending the whole token history each chunk. `detokenize_incrementally`

only ever reads the trailing token window `prev_tokens[prefix_offset:]`

, so we carry just that tail plus the two offsets. Each chunk resumes exactly where the last one stopped, including any partially processed multi-byte character (tracked by `read_offset`

), then trims and rebases the window so it never grows with generation length.

Performance: - Compute per chunk is O(delta). One `detokenize_incrementally`

call per new token, independent of how many tokens preceded it. - Transport per chunk is O(window). The carried tail is bounded by the incremental detokenization offset, so cumulative bytes over the wire are O(n) rather than the O(n^2) a full history round trip would incur.

Attributes:

-
([last_tool_call_ids](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState.last_tool_call_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Stable tool call IDs, assigned once when each call first appears.

-
([output_chunk_lens](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState.output_chunk_lens)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[int](https://docs.python.org/3/builtins/functions.html#int), Field(gt=0)]]Token count of each chunk in

`output_token_ids`

. Parser path only. -
([output_token_ids](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState.output_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]All output tokens seen so far. Parser path only.

-
([prefix_offset](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState.prefix_offset)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Prefix offset into

`prev_tokens`

for incremental detokenization. -
([prev_tokens](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState.prev_tokens)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Trailing decode window. Token strings from

`prefix_offset`

onward. -
([read_offset](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState.read_offset)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Read offset into

`prev_tokens`

for incremental detokenization. -
([role_sent](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState.role_sent)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)True once the initial

`role: "assistant"`

delta has been emitted. -
([tools_streamed](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState.tools_streamed)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)True once a tool call delta has been emitted. Parser path only.


## Source code in `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`


|
|

###

`last_tool_call_ids = Field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState.last_tool_call_ids)

Stable tool call IDs, assigned once when each call first appears.

Indexed by tool call index. Parser path only. Prevents ID regeneration when replay reprocesses a tool call that already has a pinned ID.

###

`output_chunk_lens = Field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState.output_chunk_lens)

Token count of each chunk in `output_token_ids`

. Parser path only.

Replay uses these to reproduce the original `parse_delta`

call boundaries. Must sum to `len(output_token_ids)`

.

###

`output_token_ids = Field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState.output_token_ids)

All output tokens seen so far. Parser path only.

Replay buffer: each chunk rebuilds a fresh parser and replays every token in here through `parse_delta`

(discarding the result) before processing the current chunk's tokens since parser internal state cannot be serialized into this stateless model. Unavoidably O(n) bounded by `max_model_len`

(enforced server side, not by a field validator here since the bound is model dependent).

###

`prefix_offset = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState.prefix_offset)

Prefix offset into `prev_tokens`

for incremental detokenization.

###

`prev_tokens = Field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState.prev_tokens)

Trailing decode window. Token strings from `prefix_offset`

onward.

Bounded, trimmed and rebased each chunk to the tail `detokenize_incrementally`

still reads, so it does not grow with the number of chunks.

###

`read_offset = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState.read_offset)

Read offset into `prev_tokens`

for incremental detokenization.

###

`role_sent = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState.role_sent)

True once the initial `role: "assistant"`

delta has been emitted.

Prevents re-emitting the role on subsequent chunks even when the detok window is transiently empty (e.g. usage only final chunk).

###

`tools_streamed = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.DerenderStreamState.tools_streamed)

True once a tool call delta has been emitted. Parser path only.

Drives the `finish_reason`

-> `"tool_calls"`

rewrite on the final chunk mirroring the generate streaming path.

##

`GenerateRequest`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.GenerateRequest)

Bases: `BaseModel`


Methods:

-
–[is_sampling_param_provided](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.GenerateRequest.is_sampling_param_provided)Whether the caller explicitly set

`sampling_params.<name>`

.

Attributes:

-
([content_parts](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.GenerateRequest.content_parts)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]] | NoneRaw multimodal input; server resolves media. Mutually exclusive

-
([features](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.GenerateRequest.features)

) –[MultiModalFeatures](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.MultiModalFeatures)| NoneMultimodal hashes and placeholder positions (populated for MM inputs).

-
([sampling_params](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.GenerateRequest.sampling_params)

) –[SamplingParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.SamplingParams)The sampling parameters for the model.

-
([token_ids](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.GenerateRequest.token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]The token ids to generate text from.

-
([token_offsets](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.GenerateRequest.token_offsets)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]] | NoneChar-level (start, end) offsets per token, relative to the


## Source code in `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`


|
|

###

`content_parts = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.GenerateRequest.content_parts)

Raw multimodal input; server resolves media. Mutually exclusive with `features`

.

###

`features = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.GenerateRequest.features)

Multimodal hashes and placeholder positions (populated for MM inputs).

###

`sampling_params`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.GenerateRequest.sampling_params)

The sampling parameters for the model.

###

`token_ids = Field(min_length=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.GenerateRequest.token_ids)

The token ids to generate text from.

###

`token_offsets = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.GenerateRequest.token_offsets)

Char-level (start, end) offsets per token, relative to the tokenized source string. Present only when the request set `return_token_offsets=True`

and the renderer was able to compute them (Fast tokenizer, text input, no multimodal data). List length equals `token_ids`

length when present. None otherwise.

###

`is_sampling_param_provided(name)`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.GenerateRequest.is_sampling_param_provided)

Whether the caller explicitly set `sampling_params.<name>`

.

For requests parsed from a JSON body, this reflects the raw input dict. For requests constructed with a pre-built `SamplingParams`

instance, all fields are considered provided so server-side defaults do not clobber values already resolved upstream.

## Source code in `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`


##

`MultiModalFeatures`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.MultiModalFeatures)

Bases: `BaseModel`


Lightweight multimodal metadata produced by the render step.

Carries hashes (for cache lookup / identification) and placeholder positions so the downstream `/generate`

service knows *where* in the token sequence each multimodal item lives.

Attributes:

-
([kwargs_data](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.MultiModalFeatures.kwargs_data)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None]] | NonePer-modality serialized tensor data.

-
([mm_hashes](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.MultiModalFeatures.mm_hashes)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]Per-modality item hashes, e.g.

`{"image": ["abc", "def"]}`

. -
([mm_metadata](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.MultiModalFeatures.mm_metadata)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None]] | NonePer-modality serialized metadata for disaggregated prefill.

-
([mm_placeholders](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.MultiModalFeatures.mm_placeholders)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[PlaceholderRangeInfo](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.PlaceholderRangeInfo)]]Per-modality placeholder ranges in the token sequence.


## Source code in `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`


###

`kwargs_data = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.MultiModalFeatures.kwargs_data)

Per-modality serialized tensor data.

Each value is a list parallel to `mm_hashes[modality]`

. A `str`

entry is a base64-encoded `MultiModalKwargsItem`

; `None`

means the item should be resolved from cache. The entire field is `None`

for metadata-only (cache-hit) responses.

###

`mm_hashes`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.MultiModalFeatures.mm_hashes)

Per-modality item hashes, e.g. `{"image": ["abc", "def"]}`

.

###

`mm_metadata = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.MultiModalFeatures.mm_metadata)

Per-modality serialized metadata for disaggregated prefill.

Each value is a list parallel to `mm_hashes[modality]`

. A `str`

entry is a base64-encoded `MultiModalKwargsItem`

containing only placeholder-metadata and `keep_on_cpu`

fields. `None`

means that the metadata is unavailable for that item. Prefill can use this instead of `kwargs_data`

only when `ec_transfer_params`

is also set, so embeddings arrive through the EC connector rather than from `pixel_values`

.

###

`mm_placeholders`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.token_in_token_out.protocol.MultiModalFeatures.mm_placeholders)

Per-modality placeholder ranges in the token sequence.
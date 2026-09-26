source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/scale_out/derender/api_router/
lastmod: 2026-09-24

#

`vllm.entrypoints.scale_out.derender.api_router`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.derender.api_router)

Functions:

-
–[derender_chat_completion](https://docs.vllm.ai#vllm.entrypoints.scale_out.derender.api_router.derender_chat_completion)Derender a generate response into a ChatCompletionResponse.

-
–[derender_completion](https://docs.vllm.ai#vllm.entrypoints.scale_out.derender.api_router.derender_completion)Derender a generate response into a CompletionResponse.


##

`derender_chat_completion(request, raw_request)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.derender.api_router.derender_chat_completion)

Derender a generate response into a ChatCompletionResponse.

Accepts both non-streaming (`stream=false`

, default) and streaming (`stream=true`

) request bodies on the same path; FastAPI validates and routes on the `stream`

discriminator.

Non-streaming: body is `DerenderChatRequest`

(`generate_response`

with the complete token list). Returns a `ChatCompletionResponse`

.

Streaming: body is `DerenderChatStreamRequest`

(one `generate_chunk`

delta + optional `stream_state`

). Returns a `DerenderChatStreamResponse`

(`chunk`

+ `stream_state`

). The client carries `stream_state`

between successive calls, one per SSE chunk from `/inference/v1/generate`

.

## Source code in `vllm/entrypoints/scale_out/derender/api_router.py`


##

`derender_completion(request, raw_request)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.scale_out.derender.api_router.derender_completion)

Derender a generate response into a CompletionResponse.

Accepts both non-streaming (`stream=false`

, default) and streaming (`stream=true`

) request bodies on the same path.

Non-streaming: body is `DerenderCompletionRequest`

. Returns a `CompletionResponse`

.

Streaming: body is `DerenderCompletionStreamRequest`

(one `generate_chunk`

+ optional `stream_state`

). Returns a `DerenderCompletionStreamResponse`

(`chunk`

+ `stream_state`

).
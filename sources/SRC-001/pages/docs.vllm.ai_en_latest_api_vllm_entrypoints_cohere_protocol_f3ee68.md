source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cohere/protocol/
lastmod: 2026-09-24

#

`vllm.entrypoints.cohere.protocol`

[¶](https://docs.vllm.ai#vllm.entrypoints.cohere.protocol)

Cohere Chat v2 API protocol.

The bulk of the wire types come straight from the official `cohere`

Python SDK so we stay in sync with the upstream specification and avoid re-declaring the schema. We only own three things locally:

- The top-level request body model (the SDK doesn't ship one — its
`ClientV2.chat`

takes the body as kwargs), with vLLM-specific extensions (`kv_transfer_params`

/`chat_template_kwargs`

). - The non-streaming response envelope (the SDK exposes the message shape via :class:
`AssistantMessageResponse`

but no full response wrapper). - The streaming discriminated union (the SDK exports each event type individually but not as a combined
`Annotated[Union[...], discriminator]`

).

Importing this module pulls in the `cohere`

package. The router that mounts `POST /cohere/v2/chat`

guards on that import succeeding so vLLM still boots without the SDK installed.

See https://docs.cohere.com/reference/chat for the upstream spec.

Classes:

-
–[CohereChatV2Request](https://docs.vllm.ai#vllm.entrypoints.cohere.protocol.CohereChatV2Request)Cohere Chat v2 request body.

-
–[CohereChatV2Response](https://docs.vllm.ai#vllm.entrypoints.cohere.protocol.CohereChatV2Response)Cohere Chat v2 non-streaming response body.

-
–[CohereError](https://docs.vllm.ai#vllm.entrypoints.cohere.protocol.CohereError)Top-level error body returned by

`/cohere/v2/chat`

error responses.

##

`CohereChatV2Request`

[¶](https://docs.vllm.ai#vllm.entrypoints.cohere.protocol.CohereChatV2Request)

Bases: `BaseModel`


Cohere Chat v2 request body.

Mirrors the schema documented at https://docs.cohere.com/reference/chat. All structured fields delegate to the official SDK types so the body schema stays in sync with the upstream spec.

## Source code in `vllm/entrypoints/cohere/protocol.py`


|
|

###

`_normalize_message_roles(v)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.entrypoints.cohere.protocol.CohereChatV2Request._normalize_message_roles)

Rewrite OpenAI-style `developer`

roles to `system`

.

Cohere's v2 `ChatMessageV2`

discriminated union only admits the four literal roles `user`

/ `assistant`

/ `system`

/ `tool`

. OpenAI's `developer`

role is documented as high-priority system instructions, so we alias it onto `system`

*before* the SDK discriminator runs (otherwise it rejects the message with a `literal_error`

against each union member). Mirrors `_role_to_melody`

in the renderer so the same alias is honoured no matter which surface the message arrives through.

`mode="before"`

is required so the rewrite happens before the `list[ChatMessageV2]`

coercion runs the SDK's discriminated union; a default-mode validator would never see `developer`

because validation would have already failed. On any structural malformation (non-iterable input, items without a dict-shaped `role`

field, etc.) we hand `v`

back unchanged and let Pydantic's normal coercion surface a precise error.

## Source code in `vllm/entrypoints/cohere/protocol.py`


##

`CohereChatV2Response`

[¶](https://docs.vllm.ai#vllm.entrypoints.cohere.protocol.CohereChatV2Response)

Bases: `BaseModel`


Cohere Chat v2 non-streaming response body.

Wraps the SDK :class:`AssistantMessageResponse`

(the message shape) in the documented v2 response envelope (`id`

, `finish_reason`

, `usage`

, `logprobs`

). The single constructor in :class:`CohereServingChatV2._chat_completion_to_v2`

is responsible for supplying a non-empty `id`

(falling back to a synthesized one if the upstream response is missing it) to this model.

## Source code in `vllm/entrypoints/cohere/protocol.py`


##

`CohereError`

[¶](https://docs.vllm.ai#vllm.entrypoints.cohere.protocol.CohereError)

Bases: `BaseModel`


Top-level error body returned by `/cohere/v2/chat`

error responses.

Cohere's documented error schemas are uniform: `{message, id}`

.
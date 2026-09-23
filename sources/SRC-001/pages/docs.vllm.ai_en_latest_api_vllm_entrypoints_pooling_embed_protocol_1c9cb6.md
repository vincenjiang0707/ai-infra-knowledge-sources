source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/pooling/embed/protocol/
lastmod: 2026-09-23

#

`vllm.entrypoints.pooling.embed.protocol`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.embed.protocol)

Embedding API protocol models for OpenAI and Cohere formats.

OpenAI: https://platform.openai.com/docs/api-reference/embeddings Cohere: https://docs.cohere.com/reference/embed

Classes:

-
–[EmbeddingBatchChatInputRequest](https://docs.vllm.ai#vllm.entrypoints.pooling.embed.protocol.EmbeddingBatchChatInputRequest)OpenAI embeddings request with batched chat conversations in

`input`

. -
–[EmbeddingBatchChatRequest](https://docs.vllm.ai#vllm.entrypoints.pooling.embed.protocol.EmbeddingBatchChatRequest)OpenAI embeddings request with batched top-level chat conversations.

-
–[EmbeddingChatInputRequest](https://docs.vllm.ai#vllm.entrypoints.pooling.embed.protocol.EmbeddingChatInputRequest)OpenAI embeddings request with one chat conversation in

`input`

. -
–[EmbeddingChatRequest](https://docs.vllm.ai#vllm.entrypoints.pooling.embed.protocol.EmbeddingChatRequest)OpenAI embeddings request with one top-level chat conversation.


Functions:

-
–[build_typed_embeddings](https://docs.vllm.ai#vllm.entrypoints.pooling.embed.protocol.build_typed_embeddings)Convert float embeddings to all requested Cohere embedding types.


##

`EmbeddingBatchChatInputRequest`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.embed.protocol.EmbeddingBatchChatInputRequest)

Bases: [EmbeddingBatchChatRequest](https://docs.vllm.ai#vllm.entrypoints.pooling.embed.protocol.EmbeddingBatchChatRequest)

OpenAI embeddings request with batched chat conversations in `input`

.

## Source code in `vllm/entrypoints/pooling/embed/protocol.py`


##

`EmbeddingBatchChatRequest`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.embed.protocol.EmbeddingBatchChatRequest)

Bases: `PoolingBasicRequestMixin`

, `ChatRequestOptionsMixin`

, `EmbedRequestMixin`

, `EmbeddingTokenizeParamsMixin`


OpenAI embeddings request with batched top-level chat conversations.

Mirrors `BatchChatCompletionRequest`

by keeping batched conversations in `messages`

instead of introducing a separate batch-specific field.

## Source code in `vllm/entrypoints/pooling/embed/protocol.py`


##

`EmbeddingChatInputRequest`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.embed.protocol.EmbeddingChatInputRequest)

Bases: [EmbeddingChatRequest](https://docs.vllm.ai#vllm.entrypoints.pooling.embed.protocol.EmbeddingChatRequest)

OpenAI embeddings request with one chat conversation in `input`

.

## Source code in `vllm/entrypoints/pooling/embed/protocol.py`


##

`EmbeddingChatRequest`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.embed.protocol.EmbeddingChatRequest)

Bases: `PoolingBasicRequestMixin`

, `ChatRequestMixin`

, `EmbedRequestMixin`

, `EmbeddingTokenizeParamsMixin`


OpenAI embeddings request with one top-level chat conversation.

## Source code in `vllm/entrypoints/pooling/embed/protocol.py`


##

`_encode_base64_embeddings(float_embeddings)`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.embed.protocol._encode_base64_embeddings)

Encode float embeddings as base64 (little-endian float32).

## Source code in `vllm/entrypoints/pooling/embed/protocol.py`


##

`_pack_binary_embeddings(float_embeddings, signed)`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.embed.protocol._pack_binary_embeddings)

Bit-pack float embeddings: positive -> 1, negative -> 0.

Bits are packed MSB-first, eight per byte.

## Source code in `vllm/entrypoints/pooling/embed/protocol.py`


##

`build_typed_embeddings(float_embeddings, embedding_types)`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.embed.protocol.build_typed_embeddings)

Convert float embeddings to all requested Cohere embedding types.
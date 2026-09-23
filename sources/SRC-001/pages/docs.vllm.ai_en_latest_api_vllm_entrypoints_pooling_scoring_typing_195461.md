source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/pooling/scoring/typing/
lastmod: 2026-09-23

#

`vllm.entrypoints.pooling.scoring.typing`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.typing)

Classes:

-
–[ScoreMultiModalParam](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.typing.ScoreMultiModalParam)A specialized parameter type for scoring multimodal content.


##

`ScoreMultiModalParam`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.typing.ScoreMultiModalParam)

Bases: [TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict)

A specialized parameter type for scoring multimodal content.

The reasons why don't reuse `CustomChatCompletionMessageParam`

directly: 1. Score tasks don't need the 'role' field (user/assistant/system) that's required in chat completions 2. Including chat-specific fields would confuse users about their purpose in scoring 3. This is a more focused interface that only exposes what's needed for scoring

Attributes:

## Source code in `vllm/entrypoints/pooling/scoring/typing.py`


###

`content`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.typing.ScoreMultiModalParam.content)

The multimodal contents
source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/engine/protocol/
lastmod: 2026-09-23

#

`vllm.entrypoints.serve.engine.protocol`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.engine.protocol)

Classes:

##

`PromptTokenUsageInfo`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.engine.protocol.PromptTokenUsageInfo)

Bases: `OpenAIBaseModel`


Attributes:

-
([multimodal_tokens](https://docs.vllm.ai#vllm.entrypoints.serve.engine.protocol.PromptTokenUsageInfo.multimodal_tokens)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[int](https://docs.python.org/3/builtins/functions.html#int)] | NonePrompt tokens contributed by each input modality, keyed by modality name


## Source code in `vllm/entrypoints/serve/engine/protocol.py`


###

`multimodal_tokens = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.engine.protocol.PromptTokenUsageInfo.multimodal_tokens)

Prompt tokens contributed by each input modality, keyed by modality name (e.g. `image`

, `audio`

, `video`

). A breakdown of the multimodal placeholder tokens already counted in `prompt_tokens`

; `None`

when the request has no multimodal input.
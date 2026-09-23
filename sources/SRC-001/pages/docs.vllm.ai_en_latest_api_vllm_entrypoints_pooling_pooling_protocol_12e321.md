source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/pooling/pooling/protocol/
lastmod: 2026-09-23

#

`vllm.entrypoints.pooling.pooling.protocol`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.pooling.protocol)

Classes:

##

`IOProcessorResponse`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.pooling.protocol.IOProcessorResponse)

Bases: `OpenAIBaseModel`

, [Generic](https://docs.python.org/3/library/typing.html#typing.Generic)[T]

Attributes:

-
([data](https://docs.vllm.ai#vllm.entrypoints.pooling.pooling.protocol.IOProcessorResponse.data)`T`

) –When using plugins IOProcessor plugins, the actual output is generated

-
([request_id](https://docs.vllm.ai#vllm.entrypoints.pooling.pooling.protocol.IOProcessorResponse.request_id)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe request_id associated with this response
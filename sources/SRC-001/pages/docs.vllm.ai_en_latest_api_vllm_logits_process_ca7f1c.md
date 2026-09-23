source: https://docs.vllm.ai/en/latest/api/vllm/logits_process/
lastmod: 2026-09-23

#

`vllm.logits_process`

[¶](https://docs.vllm.ai#vllm.logits_process)

Attributes:

-
([LogitsProcessor](https://docs.vllm.ai#vllm.logits_process.LogitsProcessor)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)LogitsProcessor is a function that takes a list


##

`LogitsProcessor = Callable[[list[int], torch.Tensor], torch.Tensor] | Callable[[list[int], list[int], torch.Tensor], torch.Tensor]`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.logits_process.LogitsProcessor)

LogitsProcessor is a function that takes a list of previously generated tokens, the logits tensor for the next token and, optionally, prompt tokens as a first argument, and returns a modified tensor of logits to sample from.
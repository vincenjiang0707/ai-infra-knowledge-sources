source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/blip/
lastmod: 2026-09-23

#

`vllm.model_executor.models.blip`

[¶](https://docs.vllm.ai#vllm.model_executor.models.blip)

Minimal implementation of BlipVisionModel intended to be only used within a vision language model.

Classes:

-
–[BlipAttention](https://docs.vllm.ai#vllm.model_executor.models.blip.BlipAttention)Multi-headed attention from 'Attention Is All You Need' paper.

-
–[BlipEncoder](https://docs.vllm.ai#vllm.model_executor.models.blip.BlipEncoder)Transformer encoder consisting of

`config.num_hidden_layers`

self

##

`BlipAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.blip.BlipAttention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Multi-headed attention from 'Attention Is All You Need' paper.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.blip.BlipAttention.forward)Input shape: Batch x Time x Channel.


## Source code in `vllm/model_executor/models/blip.py`


###

`forward(hidden_states)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.blip.BlipAttention.forward)

Input shape: Batch x Time x Channel.

## Source code in `vllm/model_executor/models/blip.py`


##

`BlipEncoder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.blip.BlipEncoder)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Transformer encoder consisting of `config.num_hidden_layers`

self attention layers. Each layer is a [`BlipEncoderLayer`

].

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.blip.BlipEncoder(config))`BlipVisionConfig`

) –BlipConfig
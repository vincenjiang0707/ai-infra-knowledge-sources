source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/arcee/
lastmod: 2026-09-24

#

`vllm.model_executor.models.arcee`

[¶](https://docs.vllm.ai#vllm.model_executor.models.arcee)

Classes:

-
–[ArceeDecoderLayer](https://docs.vllm.ai#vllm.model_executor.models.arcee.ArceeDecoderLayer)Transformer decoder block for Arcee, with self-attention and

-
–[ArceeForCausalLM](https://docs.vllm.ai#vllm.model_executor.models.arcee.ArceeForCausalLM)Arcee Model for causal language modeling, integrated with vLLM

-
–[ArceeMLP](https://docs.vllm.ai#vllm.model_executor.models.arcee.ArceeMLP)Feed-forward layer for Arcee using ReLU^2 activation

-
–[ArceeModel](https://docs.vllm.ai#vllm.model_executor.models.arcee.ArceeModel)The transformer model backbone for Arcee (embedding layer + stacked


##

`ArceeDecoderLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.arcee.ArceeDecoderLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Transformer decoder block for Arcee, with self-attention and ReLU^2 MLP.

## Source code in `vllm/model_executor/models/arcee.py`


|
|

##

`ArceeForCausalLM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.arcee.ArceeForCausalLM)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsLoRA](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)

, [SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)

, [SupportsEagle](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsEagle)[SupportsEagle3](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsEagle3)

Arcee Model for causal language modeling, integrated with vLLM runtime.

Methods:

-
–[load_weights](https://docs.vllm.ai#vllm.model_executor.models.arcee.ArceeForCausalLM.load_weights)Load weights into the model (delegates to inner model and handles


## Source code in `vllm/model_executor/models/arcee.py`


|
|

###

`load_weights(weights)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.arcee.ArceeForCausalLM.load_weights)

Load weights into the model (delegates to inner model and handles tied embeddings).

## Source code in `vllm/model_executor/models/arcee.py`


##

`ArceeMLP`

[¶](https://docs.vllm.ai#vllm.model_executor.models.arcee.ArceeMLP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Feed-forward layer for Arcee using ReLU^2 activation (no gating as in LLaMA).

## Source code in `vllm/model_executor/models/arcee.py`


##

`ArceeModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.arcee.ArceeModel)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)`EagleModelMixin`


The transformer model backbone for Arcee (embedding layer + stacked decoder blocks + final norm).

## Source code in `vllm/model_executor/models/arcee.py`


|
|
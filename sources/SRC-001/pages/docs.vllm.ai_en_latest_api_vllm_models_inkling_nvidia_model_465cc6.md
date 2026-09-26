source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/nvidia/model/
lastmod: 2026-09-24

#

`vllm.models.inkling.nvidia.model`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.model)

Inkling model implementation for NVIDIA GPUs.

Classes:

-
–[InklingForCausalLM](https://docs.vllm.ai#vllm.models.inkling.nvidia.model.InklingForCausalLM)Text-only entry point (

`inkling_model`

checkpoints). -
–[InklingForConditionalGeneration](https://docs.vllm.ai#vllm.models.inkling.nvidia.model.InklingForConditionalGeneration)Top-level (multimodal) entry point.

-
–[InklingReplicatedEmbedding](https://docs.vllm.ai#vllm.models.inkling.nvidia.model.InklingReplicatedEmbedding)Full-vocab embedding table replicated on every TP rank.


##

`InklingForCausalLM`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.model.InklingForCausalLM)

Bases: [_TmlForCausalLMBase](https://docs.vllm.ai#vllm.models.inkling.nvidia.model._TmlForCausalLMBase)

Text-only entry point (`inkling_model`

checkpoints).

## Source code in `vllm/models/inkling/nvidia/model.py`


##

`InklingForConditionalGeneration`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.model.InklingForConditionalGeneration)

Bases:

, [_TmlForCausalLMBase](https://docs.vllm.ai#vllm.models.inkling.nvidia.model._TmlForCausalLMBase)[SupportsMultiModal](https://docs.vllm.ai/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

Top-level (multimodal) entry point.

Builds the vision + audio towers on top of the shared text backbone. Inkling has NO cross-modal fusion (the vision tower emits one token per patch, the audio tower one token per frame), so generation reuses the inherited backbone `forward`

/ `compute_logits`

(the latter already applies muP) and this class only adds multimodal embedding + merge.

## Source code in `vllm/models/inkling/nvidia/model.py`


|
|

##

`InklingReplicatedEmbedding`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.model.InklingReplicatedEmbedding)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Full-vocab embedding table replicated on every TP rank.

Trades the full table per rank (~2.3 GiB at V=201k / H=6144 bf16, vs a 1/tp shard) for no masked lookup or per-lookup TP all-reduce, and keeps the full table on-rank for the fused gather+norm kernel. Bit-exact vs vocab-parallel: the all-reduce there only ever summed one real row against exact zeros. The LM head stays vocab-sharded.

## Source code in `vllm/models/inkling/nvidia/model.py`


##

`_TmlForCausalLMBase`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.model._TmlForCausalLMBase)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsPP](https://docs.vllm.ai/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)[SupportsLoRA](https://docs.vllm.ai/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)

Shared text-backbone causal-LM scaffolding for both entry classes.

## Source code in `vllm/models/inkling/nvidia/model.py`


|
|

##

`_sconv_add_norm(delta, hidden, sconv, norm, positions)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.model._sconv_add_norm)

`h = hidden + sconv(TP-sum(delta)); y = rmsnorm(h)`

.

The Lamport path performs reduce-scatter + shard sconv + all-gather + residual add + norm. The NCCL path handles unsupported configurations.
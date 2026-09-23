source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/moondream3/
lastmod: 2026-09-23

#

`vllm.model_executor.models.moondream3`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3)

Inference-only Moondream3 model implementation.

Classes:

-
–[Moondream3Attention](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3Attention)Decoder attention with RoPE and tau scaling.

-
–[Moondream3DecoderLayer](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3DecoderLayer)Decoder layer with attention + MLP/MoE.

-
–[Moondream3DummyInputsBuilder](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3DummyInputsBuilder)Dummy inputs builder for profiling.

-
–[Moondream3ForCausalLM](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3ForCausalLM)Moondream3 multimodal model for causal language modeling.

-
–[Moondream3ImageInput](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3ImageInput)Container holding per-image inputs for embedding.

-
–[Moondream3MultiModalProcessor](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3MultiModalProcessor)Multimodal processor for Moondream3.

-
–[Moondream3ProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3ProcessingInfo)Processing info for Moondream3.

-
–[Moondream3TextMLP](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3TextMLP)Standard MLP for non-MoE layers (layers 0-3).

-
–[Moondream3TextMoE](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3TextMoE)Mixture of Experts layer for layers 4+ with expert parallelism.

-
–[Moondream3TextModel](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3TextModel)Text decoder model.

-
–[Moondream3VisionAttention](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3VisionAttention)Self-attention for vision encoder (bidirectional).

-
–[Moondream3VisionBlock](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3VisionBlock)Transformer block for vision encoder.

-
–[Moondream3VisionEncoder](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3VisionEncoder)Vision encoder (SigLIP-style ViT).

-
–[Moondream3VisionMLP](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3VisionMLP)MLP for vision encoder blocks.

-
–[Moondream3VisionProjection](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3VisionProjection)Projects vision features to text embedding dimension.


Functions:

-
–[reconstruct_from_crops](https://docs.vllm.ai#vllm.model_executor.models.moondream3.reconstruct_from_crops)Reconstruct features from overlapping crops.


##

`Moondream3Attention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3Attention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Decoder attention with RoPE and tau scaling.

Moondream3 uses a tau attention mechanism that scales Q and V based on both token content and position.

## Source code in `vllm/model_executor/models/moondream3.py`


|
|

##

`Moondream3DecoderLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3DecoderLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Decoder layer with attention + MLP/MoE.

## Source code in `vllm/model_executor/models/moondream3.py`


##

`Moondream3DummyInputsBuilder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3DummyInputsBuilder)

Bases: [BaseDummyInputsBuilder](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseDummyInputsBuilder)[[Moondream3ProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3ProcessingInfo)]

Dummy inputs builder for profiling.

## Source code in `vllm/model_executor/models/moondream3.py`


##

`Moondream3ForCausalLM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3ForCausalLM)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)[SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)

Moondream3 multimodal model for causal language modeling.

vLLM supports the standard autoregressive Moondream3 query and caption prompt formats. The region-module point/detect skills require custom coordinate decoding and are intentionally not exposed here.

Methods:

-
–[embed_multimodal](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3ForCausalLM.embed_multimodal)Generate the HF image prefix: BOS embedding + 729 image embeddings.

-
–[load_weights](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3ForCausalLM.load_weights)Load weights with remapping from HuggingFace format.


## Source code in `vllm/model_executor/models/moondream3.py`


|
|

###

`embed_multimodal(**kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3ForCausalLM.embed_multimodal)

Generate the HF image prefix: BOS embedding + 729 image embeddings.

## Source code in `vllm/model_executor/models/moondream3.py`


###

`load_weights(weights)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3ForCausalLM.load_weights)

Load weights with remapping from HuggingFace format.

## Source code in `vllm/model_executor/models/moondream3.py`


|
|

##

`Moondream3ImageInput`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3ImageInput)

##

`Moondream3MultiModalProcessor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3MultiModalProcessor)

Bases: [BaseMultiModalProcessor](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor)[[Moondream3ProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3ProcessingInfo)]

Multimodal processor for Moondream3.

## Source code in `vllm/model_executor/models/moondream3.py`


##

`Moondream3ProcessingInfo`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3ProcessingInfo)

Bases: [BaseProcessingInfo](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseProcessingInfo)

Processing info for Moondream3.

## Source code in `vllm/model_executor/models/moondream3.py`


##

`Moondream3TextMLP`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3TextMLP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Standard MLP for non-MoE layers (layers 0-3).

## Source code in `vllm/model_executor/models/moondream3.py`


##

`Moondream3TextMoE`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3TextMoE)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Mixture of Experts layer for layers 4+ with expert parallelism.

Moondream3 uses a custom GeGLU activation: gelu(h) * (g + 1) where fc1 outputs [gate, up] and the activation is gelu(gate) * (up + 1).

Uses expert parallelism where each GPU stores num_experts/tp_size experts. Routing and communication handled via all-to-all or replicated computation.

Checkpoint format: - fc1.weight: [num_experts, expert_inner_dim * 2, hidden_size] (gate+up) - fc2.weight: [num_experts, hidden_size, expert_inner_dim] (down) - router.weight: [num_experts, hidden_size] - router.bias: [num_experts]

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3TextMoE.forward)Forward pass with expert parallelism and custom GeGLU activation.


## Source code in `vllm/model_executor/models/moondream3.py`


|
|

###

`_expert_loop(x, topk_weights, topk_ids)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3TextMoE._expert_loop)

Fallback for environments where fused kernels are unavailable.

Returns this rank's partial output; the caller performs the all-reduce.

## Source code in `vllm/model_executor/models/moondream3.py`


###

`forward(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3TextMoE.forward)

Forward pass with expert parallelism and custom GeGLU activation.

## Source code in `vllm/model_executor/models/moondream3.py`


##

`Moondream3TextModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3TextModel)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Text decoder model.

## Source code in `vllm/model_executor/models/moondream3.py`


##

`Moondream3VisionAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3VisionAttention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Self-attention for vision encoder (bidirectional).

## Source code in `vllm/model_executor/models/moondream3.py`


##

`Moondream3VisionBlock`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3VisionBlock)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Transformer block for vision encoder.

## Source code in `vllm/model_executor/models/moondream3.py`


##

`Moondream3VisionEncoder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3VisionEncoder)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Vision encoder (SigLIP-style ViT).

Methods:

-
–[create_patches](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3VisionEncoder.create_patches)Convert images to patch embeddings.

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3VisionEncoder.forward)Encode images.


## Source code in `vllm/model_executor/models/moondream3.py`


|
|

###

`create_patches(images)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3VisionEncoder.create_patches)

Convert images to patch embeddings.

Parameters:

Returns:

-
(`patches`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(batch, num_patches, patch_dim)


## Source code in `vllm/model_executor/models/moondream3.py`


###

`forward(pixel_values)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3VisionEncoder.forward)

Encode images.

Parameters:

Returns:

-
(`features`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(batch, num_patches, hidden_size)


## Source code in `vllm/model_executor/models/moondream3.py`


##

`Moondream3VisionMLP`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3VisionMLP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

MLP for vision encoder blocks.

## Source code in `vllm/model_executor/models/moondream3.py`


##

`Moondream3VisionProjection`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.Moondream3VisionProjection)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Projects vision features to text embedding dimension.

## Source code in `vllm/model_executor/models/moondream3.py`


##

`reconstruct_from_crops(crops, tiling, overlap_margin, patch_size=14)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moondream3.reconstruct_from_crops)

Reconstruct features from overlapping crops.
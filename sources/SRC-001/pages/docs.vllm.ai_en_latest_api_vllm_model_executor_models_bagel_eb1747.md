source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/bagel/
lastmod: 2026-09-24

#

`vllm.model_executor.models.bagel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel)

Inference-only BAGEL model compatible with HuggingFace weights.

BAGEL is a unified multimodal model for image understanding and generation. For vLLM, we focus on the image understanding (vision-to-text) capabilities.

Classes:

-
–[BagelDummyInputsBuilder](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelDummyInputsBuilder)Build dummy inputs for BAGEL model profiling.

-
–[BagelForConditionalGeneration](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelForConditionalGeneration)BAGEL: A unified multimodal model for image understanding and generation.

-
–[BagelImagePixelInputs](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelImagePixelInputs)Dimensions:

-
–[BagelMultiModalProcessor](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelMultiModalProcessor)Multimodal processor for BAGEL model.

-
–[BagelProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelProcessingInfo)Processing information for BAGEL model.

-
–[BagelVisionMLP](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelVisionMLP)MLP connector for vision features.

-
–[PositionEmbedding](https://docs.vllm.ai#vllm.model_executor.models.bagel.PositionEmbedding)2D position embedding for vision tokens using sin-cos embeddings.


##

`BagelDummyInputsBuilder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelDummyInputsBuilder)

Bases: [BaseDummyInputsBuilder](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseDummyInputsBuilder)[[BagelProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelProcessingInfo)]

Build dummy inputs for BAGEL model profiling.

## Source code in `vllm/model_executor/models/bagel.py`


##

`BagelForConditionalGeneration`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelForConditionalGeneration)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

, [SupportsLoRA](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)[SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)

BAGEL: A unified multimodal model for image understanding and generation.

For vLLM, we focus on the image understanding (vision-to-text) capabilities. The image generation part is not supported in vLLM.

Methods:

-
–[embed_multimodal](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelForConditionalGeneration.embed_multimodal)Get multimodal embeddings from input.

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelForConditionalGeneration.forward)Run forward pass for BAGEL.

-
–[load_weights](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelForConditionalGeneration.load_weights)Load weights from checkpoint.


## Source code in `vllm/model_executor/models/bagel.py`


|
|

###

`_process_image_input(image_input)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelForConditionalGeneration._process_image_input)

Process image inputs through vision encoder and connector.

## Source code in `vllm/model_executor/models/bagel.py`


###

`embed_multimodal(**kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelForConditionalGeneration.embed_multimodal)

Get multimodal embeddings from input.

## Source code in `vllm/model_executor/models/bagel.py`


###

`forward(input_ids, positions, intermediate_tensors=None, inputs_embeds=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelForConditionalGeneration.forward)

Run forward pass for BAGEL.

Parameters:

-

(`input_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelForConditionalGeneration.forward(input_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneFlattened (concatenated) input_ids corresponding to a batch.

-

(`positions`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelForConditionalGeneration.forward(positions))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Flattened (concatenated) position ids corresponding to a batch.

-

(`intermediate_tensors`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelForConditionalGeneration.forward(intermediate_tensors))

, default:[IntermediateTensors](https://docs.vllm.ai/sequence/#vllm.sequence.IntermediateTensors)| None`None`

) –Intermediate tensors from prior forward pass.

-

(`inputs_embeds`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelForConditionalGeneration.forward(inputs_embeds))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional tensor of input embeddings.

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelForConditionalGeneration.forward(**kwargs))

, default:[object](https://docs.python.org/3/builtins/functions.html#object)`{}`

) –Multimodal inputs for this batch, forwarded to the multimodal embedding path.


## Source code in `vllm/model_executor/models/bagel.py`


###

`load_weights(weights)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelForConditionalGeneration.load_weights)

Load weights from checkpoint.

## Source code in `vllm/model_executor/models/bagel.py`


##

`BagelImagePixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelImagePixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - bn: Batch size * number of images - c: Number of channels (3) - h: Height of each image - w: Width of each image

## Source code in `vllm/model_executor/models/bagel.py`


##

`BagelMultiModalProcessor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelMultiModalProcessor)

Bases: [BaseMultiModalProcessor](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor)[[BagelProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelProcessingInfo)]

Multimodal processor for BAGEL model.

## Source code in `vllm/model_executor/models/bagel.py`


###

`_get_prompt_updates(mm_items, hf_processor_mm_kwargs, out_mm_kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelMultiModalProcessor._get_prompt_updates)

Replace image placeholders with the correct number of tokens.

## Source code in `vllm/model_executor/models/bagel.py`


##

`BagelProcessingInfo`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelProcessingInfo)

Bases: [BaseProcessingInfo](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseProcessingInfo)

Processing information for BAGEL model.

## Source code in `vllm/model_executor/models/bagel.py`


##

`BagelVisionMLP`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.BagelVisionMLP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

MLP connector for vision features.

## Source code in `vllm/model_executor/models/bagel.py`


##

`PositionEmbedding`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.PositionEmbedding)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

2D position embedding for vision tokens using sin-cos embeddings.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.bagel.PositionEmbedding.forward)Args:


## Source code in `vllm/model_executor/models/bagel.py`


|
|

###

`_get_1d_sincos_pos_embed_from_grid(embed_dim, pos)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.PositionEmbedding._get_1d_sincos_pos_embed_from_grid)

Generate 1D sin-cos position embeddings.

## Source code in `vllm/model_executor/models/bagel.py`


###

`_get_2d_sincos_pos_embed(embed_dim, grid_size)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.PositionEmbedding._get_2d_sincos_pos_embed)

Generate 2D sin-cos position embeddings.

## Source code in `vllm/model_executor/models/bagel.py`


###

`_get_2d_sincos_pos_embed_from_grid(embed_dim, grid)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.PositionEmbedding._get_2d_sincos_pos_embed_from_grid)

Generate 2D sin-cos position embeddings from grid.

## Source code in `vllm/model_executor/models/bagel.py`


###

`forward(position_ids)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.PositionEmbedding.forward)

Parameters:

-

(`position_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bagel.PositionEmbedding.forward(position_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Flattened position IDs, shape (N,) where each ID corresponds to a position in the flattened grid


Returns: Position embeddings of shape (N, hidden_size)
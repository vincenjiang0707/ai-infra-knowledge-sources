source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/eagle2_5_vl/
lastmod: 2026-09-23

#

`vllm.model_executor.models.eagle2_5_vl`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl)

Classes:

-
–[Eagle2_5_VLDummyInputsBuilder](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLDummyInputsBuilder)Dummy inputs builder for Eagle2.5-VL model.

-
–[Eagle2_5_VLForConditionalGeneration](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration)Eagle2.5-VL model for conditional generation.

-
–[Eagle2_5_VLImageEmbeddingInputs](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLImageEmbeddingInputs)Dimensions:

-
–[Eagle2_5_VLImagePixelInputs](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLImagePixelInputs)Dimensions:

-
–[Eagle2_5_VLMultiModalProcessor](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLMultiModalProcessor)Multi-modal processor for Eagle2.5-VL model.

-
–[Eagle2_5_VLProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLProcessingInfo)Processing info for Eagle2.5-VL model.


##

`Eagle2_5_VLDummyInputsBuilder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLDummyInputsBuilder)

Bases: [BaseInternVLDummyInputsBuilder](https://docs.vllm.ai/internvl/#vllm.model_executor.models.internvl.BaseInternVLDummyInputsBuilder)[[Eagle2_5_VLProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLProcessingInfo)]

Dummy inputs builder for Eagle2.5-VL model.

## Source code in `vllm/model_executor/models/eagle2_5_vl.py`


##

`Eagle2_5_VLForConditionalGeneration`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

, [SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)[SupportsLoRA](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)

Eagle2.5-VL model for conditional generation.

## Architecture

- Vision Encoder: SigLIP
- Language Model: Qwen2
- Projection: MLP with pixel shuffle downsampling

Methods:

-
–[compute_logits](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration.compute_logits)Compute logits from hidden states.

-
–[embed_input_ids](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration.embed_input_ids)Embed input IDs with optional multimodal embeddings.

-
–[embed_multimodal](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration.embed_multimodal)Embed multimodal inputs.

-
–[extract_feature](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration.extract_feature)Extract visual features from pixel values.

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration.forward)Forward pass through the model.

-
–[get_mm_mapping](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration.get_mm_mapping)Get the module prefix mapping for multimodal models.

-
–[load_weights](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration.load_weights)Load model weights.

-
–[pixel_shuffle](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration.pixel_shuffle)Pixel shuffle operation for downsampling vision features.


## Source code in `vllm/model_executor/models/eagle2_5_vl.py`


|
|

###

`_init_mlp1(config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration._init_mlp1)

Initialize MLP projection layer.

## Source code in `vllm/model_executor/models/eagle2_5_vl.py`


###

`_init_vision_model(config, quant_config, prefix)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration._init_vision_model)

Initialize SigLIP vision model.

## Source code in `vllm/model_executor/models/eagle2_5_vl.py`


###

`_parse_and_validate_image_input(**kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration._parse_and_validate_image_input)

Parse and validate image inputs.

## Source code in `vllm/model_executor/models/eagle2_5_vl.py`


###

`_process_image_input(image_input)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration._process_image_input)

Process image input to get embeddings.

## Source code in `vllm/model_executor/models/eagle2_5_vl.py`


###

`compute_logits(hidden_states)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration.compute_logits)

###

`embed_input_ids(input_ids, multimodal_embeddings=None, *, is_multimodal=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration.embed_input_ids)

Embed input IDs with optional multimodal embeddings.

## Source code in `vllm/model_executor/models/eagle2_5_vl.py`


###

`embed_multimodal(**kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration.embed_multimodal)

Embed multimodal inputs.

## Source code in `vllm/model_executor/models/eagle2_5_vl.py`


###

`extract_feature(pixel_values)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration.extract_feature)

Extract visual features from pixel values.

Parameters:

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Visual embeddings


## Source code in `vllm/model_executor/models/eagle2_5_vl.py`


###

`forward(input_ids, positions, intermediate_tensors=None, inputs_embeds=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration.forward)

Forward pass through the model.

## Source code in `vllm/model_executor/models/eagle2_5_vl.py`


###

`get_mm_mapping()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration.get_mm_mapping)

Get the module prefix mapping for multimodal models.

## Source code in `vllm/model_executor/models/eagle2_5_vl.py`


###

`load_weights(weights)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration.load_weights)

###

`pixel_shuffle(x, scale_factor=0.5)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration.pixel_shuffle)

Pixel shuffle operation for downsampling vision features.

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration.pixel_shuffle(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor of shape (n, w, h, c)

-

(`scale_factor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLForConditionalGeneration.pixel_shuffle(scale_factor))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`0.5`

) –Downsampling factor


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Downsampled tensor


## Source code in `vllm/model_executor/models/eagle2_5_vl.py`


##

`Eagle2_5_VLImageEmbeddingInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLImageEmbeddingInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - n: Number of images - f: Total image feature size - h: Hidden size (must match the hidden size of language model backbone)

## Source code in `vllm/model_executor/models/eagle2_5_vl.py`


##

`Eagle2_5_VLImagePixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLImagePixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - bn: Batch size * number of images - bnp: Batch size * number of images * (1 + num_patches) - c: Number of channels (3) - h: Height of each image patch - w: Width of each image patch

## Source code in `vllm/model_executor/models/eagle2_5_vl.py`


##

`Eagle2_5_VLMultiModalProcessor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLMultiModalProcessor)

Bases: [BaseInternVLMultiModalProcessor](https://docs.vllm.ai/internvl/#vllm.model_executor.models.internvl.BaseInternVLMultiModalProcessor)[[Eagle2_5_VLProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLProcessingInfo)]

Multi-modal processor for Eagle2.5-VL model.

## Source code in `vllm/model_executor/models/eagle2_5_vl.py`


##

`Eagle2_5_VLProcessingInfo`

[¶](https://docs.vllm.ai#vllm.model_executor.models.eagle2_5_vl.Eagle2_5_VLProcessingInfo)

Bases: [BaseInternVLProcessingInfo](https://docs.vllm.ai/internvl/#vllm.model_executor.models.internvl.BaseInternVLProcessingInfo)

Processing info for Eagle2.5-VL model.
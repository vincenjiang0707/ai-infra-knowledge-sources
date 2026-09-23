source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gemma4_unified/
lastmod: 2026-09-23

#

`vllm.model_executor.models.gemma4_unified`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_unified)

Gemma 4 Unified multimodal model (encoder-free image + audio + video).

The Unified Gemma4 variant has no SigLIP vision tower and no audio tower. Raw pixel patches are projected directly to LM space via a Dense+LayerNorm pipeline with factorized 2D positional embeddings (Gemma4UnifiedVisionEmbedder), then routed through the same Gemma4MultimodalEmbedder used by the tower-based variant. Audio inputs are raw waveform frames projected directly through the multimodal embedder.

This module subclasses Gemma4ForConditionalGeneration from gemma4_mm rather than reimplementing it from scratch. Only the multimodal pipeline differs; the language model, MTP integration, bidirectional attention helpers, embedding/forward path, and LoRA support are all inherited unchanged.

Classes:

-
–[Gemma4ImagePixelInputs](https://docs.vllm.ai#vllm.model_executor.models.gemma4_unified.Gemma4ImagePixelInputs)Pre-patchified image inputs from the Gemma4 image processor.

-
–[Gemma4UnifiedForConditionalGeneration](https://docs.vllm.ai#vllm.model_executor.models.gemma4_unified.Gemma4UnifiedForConditionalGeneration)Encoder-free Gemma4 (Unified) for conditional generation.

-
–[Gemma4UnifiedProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.gemma4_unified.Gemma4UnifiedProcessingInfo)ProcessingInfo for the Gemma4 Unified variant.

-
–[Gemma4UnifiedVisionEmbedder](https://docs.vllm.ai#vllm.model_executor.models.gemma4_unified.Gemma4UnifiedVisionEmbedder)Encoder-free vision embedder for Gemma4 Unified variants.


##

`Gemma4ImagePixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_unified.Gemma4ImagePixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Pre-patchified image inputs from the Gemma4 image processor.

## Dimensions

- bn: Batch size * number of images
- np: Number of patches (max_patches = max_soft_tokens * pooling_kernel_size²)
- pp: Patch pixels (patch_size² * 3)

The Gemma4 image processor outputs pixel_values as (batch, max_patches, patch_pixels) — already patchified with zero-padding for patches beyond the real image content. pixel_position_ids provides (x, y) coordinates per patch, with (-1, -1) for padding patches.

## Source code in `vllm/model_executor/models/gemma4_mm.py`


##

`Gemma4UnifiedForConditionalGeneration`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_unified.Gemma4UnifiedForConditionalGeneration)

Bases: [Gemma4ForConditionalGeneration](https://docs.vllm.ai/gemma4_mm/#vllm.model_executor.models.gemma4_mm.Gemma4ForConditionalGeneration)

Encoder-free Gemma4 (Unified) for conditional generation.

Inherits multimodal embedding routing, PLE handling, bidirectional attention helpers, language-model forward, LoRA, and pipeline-parallel support from :class:`Gemma4ForConditionalGeneration`

. Overrides only:

`__init__`

— builds the encoder-free vision embedder instead of SigLIP/audio towers (LightOnOCR-style:`nn.Module.__init__`

+ full rebuild, no`super().__init__()`

).`hf_to_vllm_mapper`

— adds the`model.vision_embedder.`

prefix.`_process_image_input`

/`_process_video_input`

/`_process_audio_input`

— encoder-free projection paths.`load_weights`

— ignore-prefix list excludes the absent towers.`get_mm_mapping`

— no tower entries.

Methods:

-
–[get_mm_mapping](https://docs.vllm.ai#vllm.model_executor.models.gemma4_unified.Gemma4UnifiedForConditionalGeneration.get_mm_mapping)Module prefix mapping for the encoder-free model (no towers).


## Source code in `vllm/model_executor/models/gemma4_unified.py`


|
|

###

`_process_audio_input(audio_input)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_unified.Gemma4UnifiedForConditionalGeneration._process_audio_input)

Project raw waveform-frame features directly to LM space.

No audio tower: the per-frame raw features are passed straight through the multimodal embedder, then padding is stripped.

## Source code in `vllm/model_executor/models/gemma4_unified.py`


###

`_process_image_input(image_input)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_unified.Gemma4UnifiedForConditionalGeneration._process_image_input)

Project raw image patches directly to LM space.

No vision tower: each image's pre-patchified pixel values are embedded via Gemma4UnifiedVisionEmbedder, projected through Gemma4MultimodalEmbedder, and padding patches (pp == -1) are stripped per image.

## Source code in `vllm/model_executor/models/gemma4_unified.py`


###

`_process_video_input(video_input)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_unified.Gemma4UnifiedForConditionalGeneration._process_video_input)

Project video frames to LM space, one frame at a time.

Frames are split per video, each frame is embedded + projected, and per-frame valid embeddings are concatenated per video.

## Source code in `vllm/model_executor/models/gemma4_unified.py`


###

`get_mm_mapping()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_unified.Gemma4UnifiedForConditionalGeneration.get_mm_mapping)

Module prefix mapping for the encoder-free model (no towers).

## Source code in `vllm/model_executor/models/gemma4_unified.py`


##

`Gemma4UnifiedProcessingInfo`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_unified.Gemma4UnifiedProcessingInfo)

Bases: [Gemma4ProcessingInfo](https://docs.vllm.ai/gemma4_mm/#vllm.model_executor.models.gemma4_mm.Gemma4ProcessingInfo)

ProcessingInfo for the Gemma4 Unified variant.

## Two field-name differences from the tower-based parent

- config →
`Gemma4UnifiedConfig`

(not`Gemma4Config`

) - vision_config.
`num_soft_tokens`

(not`default_output_length`

)

Everything else (token sequencing, audio limits, video frame budget, parser construction) is inherited unchanged.

## Source code in `vllm/model_executor/models/gemma4_unified.py`


##

`Gemma4UnifiedVisionEmbedder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_unified.Gemma4UnifiedVisionEmbedder)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Encoder-free vision embedder for Gemma4 Unified variants.

Projects raw pixel patches to LM space via dense projection and factorized 2D positional embeddings. Replaces the SigLIP vision tower used by the tower-based Gemma4 variant.

Pipeline: raw patches → LN₁ → Dense → LN₂ → +factorized_posemb → LN₃.
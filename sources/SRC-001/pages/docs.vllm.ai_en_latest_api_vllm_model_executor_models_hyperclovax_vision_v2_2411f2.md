source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/hyperclovax_vision_v2/
lastmod: 2026-09-24

#

`vllm.model_executor.models.hyperclovax_vision_v2`

[¶](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2)

HyperCLOVAX V2 (32B Think Model) Implementation.

This module contains the V2 architecture that uses Qwen2.5 Vision Transformer instead of CLIP/SigLIP used in V1.

Supports: - HyperCLOVAX-SEED-Think-32B: Vision + Text

Classes:

-
–[HCXVisionV2DummyInputsBuilder](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2DummyInputsBuilder)Dummy inputs builder for HyperCLOVAX V2 memory profiling.

-
–[HCXVisionV2ForCausalLM](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2ForCausalLM)HyperCLOVAX-SEED Vision-Language Model (V2 architecture).

-
–[HCXVisionV2ImageEmbeddingInputs](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2ImageEmbeddingInputs)V2 Image embedding inputs.

-
–[HCXVisionV2ImagePixelInputs](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2ImagePixelInputs)V2 Image inputs using Qwen2.5-VL style grid_thw format.

-
–[HCXVisionV2MultiModalProcessor](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2MultiModalProcessor)Multimodal processor for HyperCLOVAX V2 (32B Think model).

-
–[HCXVisionV2ProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2ProcessingInfo)Processing info for HyperCLOVAX V2 (32B Think model).

-
–[HCXVisionV2VideoEmbeddingInputs](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2VideoEmbeddingInputs)V2 Video embedding inputs.

-
–[HCXVisionV2VideoPixelInputs](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2VideoPixelInputs)V2 Video inputs using Qwen2.5-VL style grid_thw format.


##

`HCXVisionV2DummyInputsBuilder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2DummyInputsBuilder)

Bases: [BaseDummyInputsBuilder](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseDummyInputsBuilder)[[HCXVisionV2ProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2ProcessingInfo)]

Dummy inputs builder for HyperCLOVAX V2 memory profiling.

## Source code in `vllm/model_executor/models/hyperclovax_vision_v2.py`


##

`HCXVisionV2ForCausalLM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2ForCausalLM)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)[SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)

HyperCLOVAX-SEED Vision-Language Model (V2 architecture).

Supports: - HyperCLOVAX-SEED-Think-32B: Vision + Text

Uses Qwen2.5 Vision Transformer as the vision encoder.

## Source code in `vllm/model_executor/models/hyperclovax_vision_v2.py`


|
|

###

`_process_image_input(image_input)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2ForCausalLM._process_image_input)

Process images through Qwen2.5 ViT and projector.

## Source code in `vllm/model_executor/models/hyperclovax_vision_v2.py`


###

`_process_video_input(video_input)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2ForCausalLM._process_video_input)

Process videos through Qwen2.5 ViT and projector.

## Source code in `vllm/model_executor/models/hyperclovax_vision_v2.py`


##

`HCXVisionV2ImageEmbeddingInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2ImageEmbeddingInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

V2 Image embedding inputs.

## Dimensions

- nf: Number of image features
- hs: Hidden size
- ni: Number of images

## Source code in `vllm/model_executor/models/hyperclovax_vision_v2.py`


##

`HCXVisionV2ImagePixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2ImagePixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

V2 Image inputs using Qwen2.5-VL style grid_thw format.

## Dimensions

- np: Number of patches
- ni: Number of images
- cps: Number of channels * patch_size * patch_size

## Source code in `vllm/model_executor/models/hyperclovax_vision_v2.py`


##

`HCXVisionV2MultiModalProcessor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2MultiModalProcessor)

Bases: [BaseMultiModalProcessor](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor)[[HCXVisionV2ProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2ProcessingInfo)]

Multimodal processor for HyperCLOVAX V2 (32B Think model).

## Source code in `vllm/model_executor/models/hyperclovax_vision_v2.py`


|
|

##

`HCXVisionV2ProcessingInfo`

[¶](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2ProcessingInfo)

Bases: [BaseProcessingInfo](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseProcessingInfo)

Processing info for HyperCLOVAX V2 (32B Think model).

## Source code in `vllm/model_executor/models/hyperclovax_vision_v2.py`


##

`HCXVisionV2VideoEmbeddingInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2VideoEmbeddingInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

V2 Video embedding inputs.

## Dimensions

- nf: Number of video features
- hs: Hidden size
- nv: Number of videos

## Source code in `vllm/model_executor/models/hyperclovax_vision_v2.py`


##

`HCXVisionV2VideoPixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.hyperclovax_vision_v2.HCXVisionV2VideoPixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

V2 Video inputs using Qwen2.5-VL style grid_thw format.

## Dimensions

- np: Number of patches
- nv: Number of videos
- ctps: Number of channels * temporal_patch_size * patch_size * patch_size
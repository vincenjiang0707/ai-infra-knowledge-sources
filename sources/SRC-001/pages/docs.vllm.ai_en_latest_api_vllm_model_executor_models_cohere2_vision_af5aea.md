source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/cohere2_vision/
lastmod: 2026-09-24

#

`vllm.model_executor.models.cohere2_vision`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere2_vision)

Command-A-Vision (Cohere2Vision) multimodal model implementation for vLLM.

Classes:

-
–[Cohere2VisionForConditionalGeneration](https://docs.vllm.ai#vllm.model_executor.models.cohere2_vision.Cohere2VisionForConditionalGeneration) -
–[Cohere2VisionImagePixelInputs](https://docs.vllm.ai#vllm.model_executor.models.cohere2_vision.Cohere2VisionImagePixelInputs)Dimensions:

-
–[Cohere2VisionMultiModalProjector](https://docs.vllm.ai#vllm.model_executor.models.cohere2_vision.Cohere2VisionMultiModalProjector)Multimodal projector that maps vision features to text embedding space.

-
–[Cohere2VisionProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.cohere2_vision.Cohere2VisionProcessingInfo)

##

`Cohere2VisionForConditionalGeneration`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere2_vision.Cohere2VisionForConditionalGeneration)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

, [SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)[SupportsQuant](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsQuant)

## Source code in `vllm/model_executor/models/cohere2_vision.py`


|
|

###

`_process_image_input(image_input, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere2_vision.Cohere2VisionForConditionalGeneration._process_image_input)

Process image pixels through vision tower and projector.

Parameters:

-

(`image_input`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere2_vision.Cohere2VisionForConditionalGeneration._process_image_input(image_input))

) –[Cohere2VisionImagePixelInputs](https://docs.vllm.ai#vllm.model_executor.models.cohere2_vision.Cohere2VisionImagePixelInputs)Validated image input containing pixel values and patch counts

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere2_vision.Cohere2VisionForConditionalGeneration._process_image_input(**kwargs))

, default:[object](https://docs.python.org/3/builtins/functions.html#object)`{}`

) –Unused; accepted for interface compatibility.


Returns:

## Source code in `vllm/model_executor/models/cohere2_vision.py`


##

`Cohere2VisionImagePixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere2_vision.Cohere2VisionImagePixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - np: The total number of patches over each image over each prompt in the batch - c: Number of channels - h: Height of each image patch - w: Width of each image patch - bn: Batch size * number of images

## Source code in `vllm/model_executor/models/cohere2_vision.py`


##

`Cohere2VisionMultiModalProjector`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere2_vision.Cohere2VisionMultiModalProjector)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Multimodal projector that maps vision features to text embedding space.

Uses pixel shuffle downsampling followed by SwiGLU activation.

Methods:

-
–[pixel_shuffle](https://docs.vllm.ai#vllm.model_executor.models.cohere2_vision.Cohere2VisionMultiModalProjector.pixel_shuffle)Apply pixel shuffle downsampling to reduce spatial dimensions.


## Source code in `vllm/model_executor/models/cohere2_vision.py`


###

`pixel_shuffle(image_features)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere2_vision.Cohere2VisionMultiModalProjector.pixel_shuffle)

Apply pixel shuffle downsampling to reduce spatial dimensions.

Parameters:

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Downsampled tensor with increased channel dimension


## Source code in `vllm/model_executor/models/cohere2_vision.py`


##

`Cohere2VisionProcessingInfo`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere2_vision.Cohere2VisionProcessingInfo)

Bases: [BaseProcessingInfo](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseProcessingInfo)

Methods:

-
–[get_num_patches](https://docs.vllm.ai#vllm.model_executor.models.cohere2_vision.Cohere2VisionProcessingInfo.get_num_patches)Calculate the number of image patches for a given image.


## Source code in `vllm/model_executor/models/cohere2_vision.py`


###

`get_num_patches(*, image_width, image_height, processor, mm_kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere2_vision.Cohere2VisionProcessingInfo.get_num_patches)

Calculate the number of image patches for a given image. Uses the HF processor to determine the actual number of patches.
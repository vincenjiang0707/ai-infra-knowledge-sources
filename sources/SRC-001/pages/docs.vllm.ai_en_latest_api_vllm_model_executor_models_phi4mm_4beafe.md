source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/phi4mm/
lastmod: 2026-09-24

#

`vllm.model_executor.models.phi4mm`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm)

Classes:

-
–[Phi4MMAudioEmbeddingInputs](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMAudioEmbeddingInputs)Dimensions:

-
–[Phi4MMAudioFeatureInputs](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMAudioFeatureInputs)Dimensions:

-
–[Phi4MMForCausalLM](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMForCausalLM)Implements the Phi-4-multimodal-instruct model in vLLM.

-
–[Phi4MMImageEncoder](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMImageEncoder)Image embedding.

-
–[Phi4MMImagePixelInputs](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMImagePixelInputs)Dimensions:

-
–[Phi4MMProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMProcessingInfo)

Functions:

-
–[stack_with_pad](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.stack_with_pad)Stack tensors, padding dimensions that differ across items.


##

`Phi4MMAudioEmbeddingInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMAudioEmbeddingInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - b: Batch size - n: Number of audios - f: Audio feature size - h: Hidden size (must match language model backbone)

## Source code in `vllm/model_executor/models/phi4mm.py`


##

`Phi4MMAudioFeatureInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMAudioFeatureInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - bn: Batch size * number of audios - t: Time frames (M)

## Source code in `vllm/model_executor/models/phi4mm.py`


##

`Phi4MMForCausalLM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMForCausalLM)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsLoRA](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)[SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

Implements the Phi-4-multimodal-instruct model in vLLM.

Methods:

-
–[get_mm_mapping](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMForCausalLM.get_mm_mapping)Get the module prefix in multimodal models.


## Source code in `vllm/model_executor/models/phi4mm.py`


|
|

###

`_parse_and_validate_audio_input(**kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMForCausalLM._parse_and_validate_audio_input)

Parse and validate the audio input to the model. This handles both audio features and audio embeddings, but only the former is used for now.

Parameters:

Returns:

-
`Phi4MMAudioInputs | None`

–Optional[Phi4MMAudioInputs]: Parsed and validated audio inputs.


## Source code in `vllm/model_executor/models/phi4mm.py`


###

`_process_audio_input(audio_input, audio_projection_mode)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMForCausalLM._process_audio_input)

Create the audio embeddings from the audio input, where the audio input is pairs of audio features and audio embed lengths. The audio input is created by `input_mapper_for_phi4mm_audio`

.

Parameters:

-

(`audio_input`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMForCausalLM._process_audio_input(audio_input))`Phi4MMAudioInputs`

) –Audio input.

-

(`audio_projection_mode`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMForCausalLM._process_audio_input(audio_projection_mode))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Projection mode to use, selecting which audio projector weights are applied.


Returns:

-
(`NestedTensors`


) –[NestedTensors](https://docs.vllm.ai/multimodal/inputs/#vllm.multimodal.inputs.NestedTensors)Audio embeddings


## Source code in `vllm/model_executor/models/phi4mm.py`


###

`get_mm_mapping()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMForCausalLM.get_mm_mapping)

Get the module prefix in multimodal models.

## Source code in `vllm/model_executor/models/phi4mm.py`


##

`Phi4MMImageEncoder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMImageEncoder)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Image embedding.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMImageEncoder.forward)Process image and return vision embeddings.


## Source code in `vllm/model_executor/models/phi4mm.py`


|
|

###

`forward(pixel_values, image_sizes, image_attention_mask)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMImageEncoder.forward)

Process image and return vision embeddings.

pixel_values: (num_images, num_crops, c, h, w) image_sizes: [[h1, w1], [h2, w2]] image_attention_mask: num_images x num_crops x 32 x 32 output: (num_images, num_img_tokens, hidden_size)

## Source code in `vllm/model_executor/models/phi4mm.py`


|
|

##

`Phi4MMImagePixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMImagePixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - bn: Batch size * number of images - p: Number of patches (1 + num_patches) - c: Number of channels (3) - h: Height of each image patch - w: Width of each image patch - nc: Number of crops - H_mask: Height of attention mask - W_mask: Width of attention mask

## Source code in `vllm/model_executor/models/phi4mm.py`


##

`Phi4MMProcessingInfo`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMProcessingInfo)

Bases: [BaseProcessingInfo](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseProcessingInfo)

Methods:

-
–[get_audio_num_frames](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMProcessingInfo.get_audio_num_frames)Compute the output size of the

`extract_features`

method.

## Source code in `vllm/model_executor/models/phi4mm.py`


|
|

###

`_compute_audio_embed_size(audio_frames)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMProcessingInfo._compute_audio_embed_size)

Compute the audio embedding size based on the audio frames and compression rate.

## Source code in `vllm/model_executor/models/phi4mm.py`


###

`_compute_num_image_tokens(orig_width, orig_height, dynamic_hd_size, vit_image_size, vit_patch_size, token_compression_factor=2)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMProcessingInfo._compute_num_image_tokens)

Compute the number of tokens an image is expected to take up considering the image encoder architecture and exclude output features containing only padding pixels

for siglip, vit_image_size=448, vit_patch_size=14, so output will be 32x32 feature map NOTE right now, Phi4MM uses hard-coded token_compression_factor=2

## Source code in `vllm/model_executor/models/phi4mm.py`


|
|

###

`get_audio_num_frames(audio_len, sr)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMProcessingInfo.get_audio_num_frames)

Compute the output size of the `extract_features`

method.

Parameters:

-

(`audio_len`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMProcessingInfo.get_audio_num_frames(audio_len))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Length of the input waveform in samples.

-

(`sr`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.Phi4MMProcessingInfo.get_audio_num_frames(sr))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Sampling rate of the waveform, either 16000 or 8000.


Returns:

-
(`tuple`

`(`

) –[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int))Output size as (T, D), where: T: Number of time frames. D: Number of Mel filterbank bins (80).


## Source code in `vllm/model_executor/models/phi4mm.py`


##

`stack_with_pad(tensors, padding_value=0)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm.stack_with_pad)

Stack tensors, padding dimensions that differ across items.
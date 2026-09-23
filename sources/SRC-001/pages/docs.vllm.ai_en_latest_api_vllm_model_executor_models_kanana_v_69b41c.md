source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/kanana_v/
lastmod: 2026-09-23

#

`vllm.model_executor.models.kanana_v`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kanana_v)

Classes:

-
–[CustomQwen2VLVE](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.CustomQwen2VLVE)Thin wrapper around the Qwen2-VL used as a vision encoder.

-
–[DynamicCAbstractor](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.DynamicCAbstractor)Dynamic C-Abstractor based on RegNet blocks.

-
–[KananaVImagePixelInputs](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.KananaVImagePixelInputs)Dimensions:

-
–[KananaVMultiModalProcessor](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.KananaVMultiModalProcessor)vLLM multimodal processor for Kanana-V (text + image).

-
–[PatchMerge](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.PatchMerge)Merge neighboring patches spatially to reduce resolution.


Functions:

-
–[build_mlp](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.build_mlp)Simple SiLU-activated MLP used as a projector readout.

-
–[build_pos_embeds](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.build_pos_embeds)Build positional embeddings for the visual encoder output.


##

`CustomQwen2VLVE`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.CustomQwen2VLVE)

Bases: `Qwen2VisionTransformer`


Thin wrapper around the Qwen2-VL used as a vision encoder.

This mirrors the original HF-based vision encoder used in Kanana-V, but reuses vLLM's optimized `Qwen2VisionTransformer`

building blocks.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.CustomQwen2VLVE.forward)Run the vision transformer and optionally return intermediate states.


## Source code in `vllm/model_executor/models/kanana_v.py`


|
|

###

`_from_config(config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.CustomQwen2VLVE._from_config)

###

`forward(pixel_values, grid_thw, output_hidden_states=None, return_dict=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.CustomQwen2VLVE.forward)

Run the vision transformer and optionally return intermediate states.

Unlike the base `Qwen2VisionTransformer`

, this wrapper exposes the pre-merger patch-level representations and a HF-style `BaseModelOutput`

so that the existing projector / abstractor code can be reused.

## Source code in `vllm/model_executor/models/kanana_v.py`


##

`DynamicCAbstractor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.DynamicCAbstractor)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Dynamic C-Abstractor based on RegNet blocks.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.DynamicCAbstractor.forward)Apply the dynamic abstractor over flattened visual embeddings.


## Source code in `vllm/model_executor/models/kanana_v.py`


|
|

###

`forward(flattened_visual_embeds, grid_thw, **unused_kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.DynamicCAbstractor.forward)

Apply the dynamic abstractor over flattened visual embeddings.

## Source code in `vllm/model_executor/models/kanana_v.py`


##

`KananaVImagePixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.KananaVImagePixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - np: The total number of patches over all images in the batch - cps: Number of channels * patch_size * patch_size - ni: Number of images

## Source code in `vllm/model_executor/models/kanana_v.py`


##

`KananaVMultiModalProcessor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.KananaVMultiModalProcessor)

Bases: [BaseMultiModalProcessor](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor)[KananaVProcessingInfo]

vLLM multimodal processor for Kanana-V (text + image).

## Source code in `vllm/model_executor/models/kanana_v.py`


|
|

###

`_apply_hf_processor_main(mm_items, hf_kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.KananaVMultiModalProcessor._apply_hf_processor_main)

Run the underlying HF processor on text and image data.

## Source code in `vllm/model_executor/models/kanana_v.py`


##

`PatchMerge`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.PatchMerge)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Merge neighboring patches spatially to reduce resolution.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.PatchMerge.forward)Merge patches by

`merge_size x merge_size`

.

## Source code in `vllm/model_executor/models/kanana_v.py`


###

`forward(x, channel_last=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.PatchMerge.forward)

Merge patches by `merge_size x merge_size`

.

## Source code in `vllm/model_executor/models/kanana_v.py`


##

`build_mlp(depth, hidden_size, output_hidden_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.build_mlp)

Simple SiLU-activated MLP used as a projector readout.

## Source code in `vllm/model_executor/models/kanana_v.py`


##

`build_pos_embeds(config, num_input_tokens, vision_hidden_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kanana_v.build_pos_embeds)

Build positional embeddings for the visual encoder output.
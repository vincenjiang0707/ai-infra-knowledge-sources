source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/ovis2_5/
lastmod: 2026-09-24

#

`vllm.model_executor.models.ovis2_5`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ovis2_5)

PyTorch Ovis model.

Classes:

-
–[Ovis2_5ImagePatchInputs](https://docs.vllm.ai#vllm.model_executor.models.ovis2_5.Ovis2_5ImagePatchInputs)Dimensions:

-
–[Ovis2_5MultiModalProcessor](https://docs.vllm.ai#vllm.model_executor.models.ovis2_5.Ovis2_5MultiModalProcessor) -
–[Ovis2_5VideoPatchInputs](https://docs.vllm.ai#vllm.model_executor.models.ovis2_5.Ovis2_5VideoPatchInputs)Dimensions:

-
–[VisualTokenizer](https://docs.vllm.ai#vllm.model_executor.models.ovis2_5.VisualTokenizer)VIT.


##

`Ovis2_5ImagePatchInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ovis2_5.Ovis2_5ImagePatchInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - bnp: Batch size * number of images * number of patches - patch_size: patch_size_x * patch_size_y * num_channels - patch_indicators: Batch size * (number of patches + 1) - bn: Batch size * number of images

## Source code in `vllm/model_executor/models/ovis2_5.py`


##

`Ovis2_5MultiModalProcessor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ovis2_5.Ovis2_5MultiModalProcessor)

Bases: [BaseMultiModalProcessor](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor)[Ovis2_5ProcessingInfo]

Methods:

-
–[visual_indicators_to_visual_tokens](https://docs.vllm.ai#vllm.model_executor.models.ovis2_5.Ovis2_5MultiModalProcessor.visual_indicators_to_visual_tokens)Filter image indicators placeholders and convert them to corresponding


## Source code in `vllm/model_executor/models/ovis2_5.py`


|
|

###

`visual_indicators_to_visual_tokens(visual_indicators)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ovis2_5.Ovis2_5MultiModalProcessor.visual_indicators_to_visual_tokens)

Filter image indicators placeholders and convert them to corresponding tokens in visual tokenizer.

## Source code in `vllm/model_executor/models/ovis2_5.py`


##

`Ovis2_5VideoPatchInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ovis2_5.Ovis2_5VideoPatchInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - bnp: Batch size * number of videos * number of patches - patch_size: patch_size_x * patch_size_y * num_channels - patch_indicators: Batch size * (number of patches + 1) - bn: Batch size * number of videos

## Source code in `vllm/model_executor/models/ovis2_5.py`


##

`VisualTokenizer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ovis2_5.VisualTokenizer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

VIT.

## Source code in `vllm/model_executor/models/ovis2_5.py`


|
|
source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/glm4v/
lastmod: 2026-09-24

#

`vllm.model_executor.models.glm4v`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glm4v)

Inference-only CogAgent model compatible with THUDM weights.

Classes:

-
–[EVA2CLIPGLU](https://docs.vllm.ai#vllm.model_executor.models.glm4v.EVA2CLIPGLU) -
–[EVA2CLIPModel](https://docs.vllm.ai#vllm.model_executor.models.glm4v.EVA2CLIPModel) -
–[EVA2CLIPPatchEmbedding](https://docs.vllm.ai#vllm.model_executor.models.glm4v.EVA2CLIPPatchEmbedding) -
–[GLM4VForCausalLM](https://docs.vllm.ai#vllm.model_executor.models.glm4v.GLM4VForCausalLM) -
–[GLMVImagePixelInputs](https://docs.vllm.ai#vllm.model_executor.models.glm4v.GLMVImagePixelInputs)Dimensions:


##

`EVA2CLIPGLU`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glm4v.EVA2CLIPGLU)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.models.glm4v.EVA2CLIPGLU.__init__)The original implementation is the same as:


## Source code in `vllm/model_executor/models/glm4v.py`


|
|

###

`__init__(config, in_features, quant_config=None, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glm4v.EVA2CLIPGLU.__init__)

The original implementation is the same as:

self.dense_h_to_4h = ColumnParallelLinear(
config.hidden_size,
config.ffn_hidden_size,
bias=False,
quant_config=quant_config,
)
self.gate_proj = ColumnParallelLinear(
config.hidden_size,
config.ffn_hidden_size,
bias=False,
quant_config=quant_config,
)


gate_proj_output, _ = self.gate_proj(x)
dense_h_to_4h_output, _ = self.dense_h_to_4h(x)
x = torch.cat([gate_proj_output, dense_h_to_4h_output], dim=-1)


We merge two ColumnParallelLinear into one MergedColumnParallelLinear:

self.merged_proj = MergedColumnParallelLinear(
config.hidden_size,
[config.ffn_hidden_size] * 2,
bias=False,
quant_config=quant_config,
)


## Source code in `vllm/model_executor/models/glm4v.py`


##

`EVA2CLIPModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glm4v.EVA2CLIPModel)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.glm4v.EVA2CLIPModel.forward)Parameters


## Source code in `vllm/model_executor/models/glm4v.py`


###

`forward(images)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glm4v.EVA2CLIPModel.forward)

Parameters images : torch.Tensor Input image tensor with shape (B, C, H, W)

##### Returns[¶](https://docs.vllm.ai#vllm.model_executor.models.glm4v.EVA2CLIPModel.forward--returns)

torch.Tensor Transformed tensor with shape (B, L, D)

## Source code in `vllm/model_executor/models/glm4v.py`


##

`EVA2CLIPPatchEmbedding`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glm4v.EVA2CLIPPatchEmbedding)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.glm4v.EVA2CLIPPatchEmbedding.forward)Parameters


## Source code in `vllm/model_executor/models/glm4v.py`


###

`forward(images)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glm4v.EVA2CLIPPatchEmbedding.forward)

Parameters images : torch.Tensor Input image tensor with shape (B, C, H, W)

##### Returns[¶](https://docs.vllm.ai#vllm.model_executor.models.glm4v.EVA2CLIPPatchEmbedding.forward--returns)

torch.Tensor Transformed tensor with shape (B, L, D)

## Source code in `vllm/model_executor/models/glm4v.py`


##

`GLM4VForCausalLM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glm4v.GLM4VForCausalLM)

Bases: `ChatGLMBaseModel`

,

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

, [SupportsLoRA](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)

, [SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)[SupportsMRoPE](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMRoPE)

Methods:

-
–[get_mm_mapping](https://docs.vllm.ai#vllm.model_executor.models.glm4v.GLM4VForCausalLM.get_mm_mapping)Get the module prefix in multimodal models.


## Source code in `vllm/model_executor/models/glm4v.py`


|
|

###

`get_mm_mapping()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glm4v.GLM4VForCausalLM.get_mm_mapping)

Get the module prefix in multimodal models.

## Source code in `vllm/model_executor/models/glm4v.py`


##

`GLMVImagePixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glm4v.GLMVImagePixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - b: Batch size - c: Number of channels (3) - h: Height of image - w: Width of image
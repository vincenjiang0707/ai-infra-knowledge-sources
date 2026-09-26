source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/molmo/
lastmod: 2026-09-24

#

`vllm.model_executor.models.molmo`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo)

Classes:

-
–[BlockCollection](https://docs.vllm.ai#vllm.model_executor.models.molmo.BlockCollection)Collection of residual attention blocks used in Vision Transformer.

-
–[ImageProjectorMLP](https://docs.vllm.ai#vllm.model_executor.models.molmo.ImageProjectorMLP)Molmo's image_projector mlp.

-
–[LanguageModelMLP](https://docs.vllm.ai#vllm.model_executor.models.molmo.LanguageModelMLP)Molmo's LLM mlp.

-
–[MolmoAttention](https://docs.vllm.ai#vllm.model_executor.models.molmo.MolmoAttention)Molmo's LLM attention.

-
–[MolmoForCausalLM](https://docs.vllm.ai#vllm.model_executor.models.molmo.MolmoForCausalLM) -
–[MolmoImageInputs](https://docs.vllm.ai#vllm.model_executor.models.molmo.MolmoImageInputs)Dimensions:

-
–[MolmoVisionBackbone](https://docs.vllm.ai#vllm.model_executor.models.molmo.MolmoVisionBackbone) -
–[MultiHeadDotProductAttention](https://docs.vllm.ai#vllm.model_executor.models.molmo.MultiHeadDotProductAttention)Multi-head attention used in Vision Transformer.

-
–[ResidualAttentionBlock](https://docs.vllm.ai#vllm.model_executor.models.molmo.ResidualAttentionBlock)Residual attention block used in Vision Transformer.

-
–[ViTMLP](https://docs.vllm.ai#vllm.model_executor.models.molmo.ViTMLP)MLP used in Vision Transformer.

-
–[VisionTransformer](https://docs.vllm.ai#vllm.model_executor.models.molmo.VisionTransformer)Vision Transformer used in Vision Backbone.


##

`BlockCollection`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo.BlockCollection)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Collection of residual attention blocks used in Vision Transformer.

## Source code in `vllm/model_executor/models/molmo.py`


##

`ImageProjectorMLP`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo.ImageProjectorMLP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Molmo's image_projector mlp.

## Source code in `vllm/model_executor/models/molmo.py`


##

`LanguageModelMLP`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo.LanguageModelMLP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Molmo's LLM mlp.

## Source code in `vllm/model_executor/models/molmo.py`


##

`MolmoAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo.MolmoAttention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Molmo's LLM attention.

## Source code in `vllm/model_executor/models/molmo.py`


|
|

##

`MolmoForCausalLM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo.MolmoForCausalLM)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

, [SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)

, [SupportsLoRA](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)[SupportsQuant](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsQuant)

Methods:

-
–[get_mm_mapping](https://docs.vllm.ai#vllm.model_executor.models.molmo.MolmoForCausalLM.get_mm_mapping)Get the module prefix in multimodal models.


## Source code in `vllm/model_executor/models/molmo.py`


|
|

###

`get_mm_mapping()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo.MolmoForCausalLM.get_mm_mapping)

Get the module prefix in multimodal models.

## Source code in `vllm/model_executor/models/molmo.py`


##

`MolmoImageInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo.MolmoImageInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - bn: Batch size * number of images - bnc: Batch size * number of images * number of crops (dynamic) - np: Number of patches - tp: Token sequence positions - pd: Patch dimension

Attributes:

-
([image_input_idx](https://docs.vllm.ai#vllm.model_executor.models.molmo.MolmoImageInputs.image_input_idx)

) –[Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[TensorShape](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorShape)(bnc, tp)]An index tensor that maps image features to their corresponding patch tokens.


## Source code in `vllm/model_executor/models/molmo.py`


###

`image_input_idx`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo.MolmoImageInputs.image_input_idx)

An index tensor that maps image features to their corresponding patch tokens.

##

`MolmoVisionBackbone`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo.MolmoVisionBackbone)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)[SupportsQuant](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsQuant)

Methods:

-
–[encode_image](https://docs.vllm.ai#vllm.model_executor.models.molmo.MolmoVisionBackbone.encode_image): param images: (batch_size, num_crops, num_patch, n_pixels).


## Source code in `vllm/model_executor/models/molmo.py`


|
|

###

`encode_image(images)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo.MolmoVisionBackbone.encode_image)

: param images: (batch_size, num_crops, num_patch, n_pixels).

## Source code in `vllm/model_executor/models/molmo.py`


##

`MultiHeadDotProductAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo.MultiHeadDotProductAttention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Multi-head attention used in Vision Transformer.

## Source code in `vllm/model_executor/models/molmo.py`


|
|

##

`ResidualAttentionBlock`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo.ResidualAttentionBlock)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Residual attention block used in Vision Transformer.

## Source code in `vllm/model_executor/models/molmo.py`


##

`ViTMLP`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo.ViTMLP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

MLP used in Vision Transformer.

## Source code in `vllm/model_executor/models/molmo.py`


##

`VisionTransformer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo.VisionTransformer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Vision Transformer used in Vision Backbone.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.molmo.VisionTransformer.forward): param x: (batch_size, num_patch, n_pixels).


## Source code in `vllm/model_executor/models/molmo.py`


|
|

###

`forward(x, patch_num=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo.VisionTransformer.forward)

: param x: (batch_size, num_patch, n_pixels).
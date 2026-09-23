source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/molmo2/
lastmod: 2026-09-23

#

`vllm.model_executor.models.molmo2`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2)

Classes:

-
–[AdapterConfig](https://docs.vllm.ai#vllm.model_executor.models.molmo2.AdapterConfig)Config for a vit-llm adapter.

-
–[ImagePoolingAttention](https://docs.vllm.ai#vllm.model_executor.models.molmo2.ImagePoolingAttention)Multi-head attention used for image pooling.

-
–[ImageProjectorMLP](https://docs.vllm.ai#vllm.model_executor.models.molmo2.ImageProjectorMLP)MLP used for the image projector.

-
–[LanguageModelMLP](https://docs.vllm.ai#vllm.model_executor.models.molmo2.LanguageModelMLP)Molmo2's LLM mlp.

-
–[Molmo2Attention](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2Attention)Molmo2's LLM Attention.

-
–[Molmo2ForConditionalGeneration](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2ForConditionalGeneration) -
–[Molmo2ImageInputs](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2ImageInputs)Dimensions:

-
–[Molmo2VideoInputs](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2VideoInputs)Dimensions:

-
–[Molmo2VisionBackbone](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2VisionBackbone) -
–[Molmo2VisionBlock](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2VisionBlock)Residual attention block used in Vision Transformer.

-
–[Molmo2VisionBlockCollection](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2VisionBlockCollection)Collection of residual attention blocks used in Vision Transformer.

-
–[Molmo2VisionTransformer](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2VisionTransformer)Vision Transformer used in Vision Backbone.

-
–[TextConfig](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig)Configuration for a text model transformer.

-
–[ViTMLP](https://docs.vllm.ai#vllm.model_executor.models.molmo2.ViTMLP)MLP used in Vision Transformer.

-
–[ViTMultiHeadDotProductAttention](https://docs.vllm.ai#vllm.model_executor.models.molmo2.ViTMultiHeadDotProductAttention)Multi-head attention used in Vision Transformer.

-
–[VitConfig](https://docs.vllm.ai#vllm.model_executor.models.molmo2.VitConfig)Config for a vision transformer.


Functions:

-
–[get_candidate_target_fps](https://docs.vllm.ai#vllm.model_executor.models.molmo2.get_candidate_target_fps)Return the subset of

`video_fps`

factors that remain multiples -
–[get_target_fps](https://docs.vllm.ai#vllm.model_executor.models.molmo2.get_target_fps)Get the target fps that best spans the video and has the most frames sampled.


##

`AdapterConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.AdapterConfig)

Config for a vit-llm adapter.

## Source code in `vllm/model_executor/models/molmo2.py`


##

`ImagePoolingAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.ImagePoolingAttention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Multi-head attention used for image pooling.

## Source code in `vllm/model_executor/models/molmo2.py`


|
|

##

`ImageProjectorMLP`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.ImageProjectorMLP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

MLP used for the image projector.

## Source code in `vllm/model_executor/models/molmo2.py`


##

`LanguageModelMLP`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.LanguageModelMLP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Molmo2's LLM mlp.

## Source code in `vllm/model_executor/models/molmo2.py`


##

`Molmo2Attention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2Attention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Molmo2's LLM Attention.

## Source code in `vllm/model_executor/models/molmo2.py`


|
|

##

`Molmo2ForConditionalGeneration`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2ForConditionalGeneration)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

, [SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)

, [SupportsLoRA](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)[SupportsQuant](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsQuant)

Methods:

-
–[get_mm_mapping](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2ForConditionalGeneration.get_mm_mapping)Get the module prefix in multimodal models.


## Source code in `vllm/model_executor/models/molmo2.py`


|
|

###

`get_mm_mapping()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2ForConditionalGeneration.get_mm_mapping)

Get the module prefix in multimodal models.

## Source code in `vllm/model_executor/models/molmo2.py`


##

`Molmo2ImageInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2ImageInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - nc: The total number of crops (dynamic) - np: The total number of patches per crop - cps: Number of channels * patch_size * patch_size - npp: Number of pooled patches (dynamic) - pp: pooling_size * pooling_size - ni: Number of images - nt: Number of image tokens (dynamic)

Attributes:

-
([token_pooling](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2ImageInputs.token_pooling)

) –[Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[TensorShape](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorShape)(npp, pp)]An index tensor that maps image features to their corresponding


## Source code in `vllm/model_executor/models/molmo2.py`


###

`token_pooling`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2ImageInputs.token_pooling)

An index tensor that maps image features to their corresponding patch tokens before pooling.

##

`Molmo2VideoInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2VideoInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - nc: The total number of frames (dynamic) - np: The total number of patches per frame - cps: Number of channels * patch_size * patch_size - npp: Number of pooled patches (dynamic) - pp: pooling_size * pooling_size - nv: Number of videos - nt: Number of video tokens (dynamic)

Attributes:

-
([token_pooling](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2VideoInputs.token_pooling)

) –[Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[TensorShape](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorShape)(npp, pp)]An index tensor that maps image features to their corresponding


## Source code in `vllm/model_executor/models/molmo2.py`


###

`token_pooling`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2VideoInputs.token_pooling)

An index tensor that maps image features to their corresponding patch tokens before pooling.

##

`Molmo2VisionBackbone`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2VisionBackbone)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)[SupportsQuant](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsQuant)

Methods:

-
–[encode_image](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2VisionBackbone.encode_image): param images: (batch_size, num_crops, num_patch, n_pixels).


## Source code in `vllm/model_executor/models/molmo2.py`


|
|

###

`encode_image(images)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2VisionBackbone.encode_image)

: param images: (batch_size, num_crops, num_patch, n_pixels).

## Source code in `vllm/model_executor/models/molmo2.py`


##

`Molmo2VisionBlock`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2VisionBlock)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Residual attention block used in Vision Transformer.

## Source code in `vllm/model_executor/models/molmo2.py`


##

`Molmo2VisionBlockCollection`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2VisionBlockCollection)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Collection of residual attention blocks used in Vision Transformer.

## Source code in `vllm/model_executor/models/molmo2.py`


##

`Molmo2VisionTransformer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2VisionTransformer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Vision Transformer used in Vision Backbone.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2VisionTransformer.forward): param x: (batch_size, num_patch, n_pixels).


## Source code in `vllm/model_executor/models/molmo2.py`


###

`forward(x, patch_num=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.Molmo2VisionTransformer.forward)

: param x: (batch_size, num_patch, n_pixels).

## Source code in `vllm/model_executor/models/molmo2.py`


##

`TextConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig)

Configuration for a text model transformer.

Attributes:

-
([additional_vocab_size](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.additional_vocab_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of additional tokens to have the input embeddings for

-
([head_dim](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.head_dim)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The head dimensionality for the attention mechanism.

-
([hidden_act](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.hidden_act)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The activation function to use within the MLP layers.

-
([hidden_size](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.hidden_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The hidden size of the model.

-
([intermediate_size](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.intermediate_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The hidden size for the MLP.

-
([layer_norm_eps](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.layer_norm_eps)

) –[float](https://docs.python.org/3/builtins/functions.html#float)epsilon for layer norms

-
([max_position_embeddings](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.max_position_embeddings)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Max positional embeddings to use in RoPE cache

-
([norm_after](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.norm_after)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Apply layer norm before and after the attention and MLP blocks.

-
([num_attention_heads](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.num_attention_heads)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The number of self-attention heads.

-
([num_hidden_layers](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.num_hidden_layers)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The number of layers/blocks.

-
([num_key_value_heads](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.num_key_value_heads)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The number of heads to use for keys and values.

-
([qk_norm_type](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.qk_norm_type)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The type of layer norm to use for the keys and queries.

-
([qkv_bias](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.qkv_bias)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Do QKV projection a bias

-
([rope_scaling_layers](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.rope_scaling_layers)

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), ...] | NoneRoPE scaling layers.

-
([rope_theta](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.rope_theta)

) –[float](https://docs.python.org/3/builtins/functions.html#float)RoPE theta parameter.

-
([use_qk_norm](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.use_qk_norm)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Apply layer norm to the keys and queries within the attention mechanism.

-
([vocab_size](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.vocab_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Vocabulary size of the model.


## Source code in `vllm/model_executor/models/molmo2.py`


|
|

###

`additional_vocab_size = 128`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.additional_vocab_size)

Number of additional tokens to have the input embeddings for

###

`head_dim = 128`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.head_dim)

The head dimensionality for the attention mechanism.

###

`hidden_act = 'silu'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.hidden_act)

The activation function to use within the MLP layers.

###

`hidden_size = 3584`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.hidden_size)

The hidden size of the model.

###

`intermediate_size = 18944`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.intermediate_size)

The hidden size for the MLP.

###

`layer_norm_eps = 1e-06`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.layer_norm_eps)

epsilon for layer norms

###

`max_position_embeddings = 4096`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.max_position_embeddings)

Max positional embeddings to use in RoPE cache

###

`norm_after = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.norm_after)

Apply layer norm before and after the attention and MLP blocks.

###

`num_attention_heads = 28`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.num_attention_heads)

The number of self-attention heads.

###

`num_hidden_layers = 48`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.num_hidden_layers)

The number of layers/blocks.

###

`num_key_value_heads = 4`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.num_key_value_heads)

The number of heads to use for keys and values.

###

`qk_norm_type = 'olmo'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.qk_norm_type)

The type of layer norm to use for the keys and queries. Can be "olmo" or "qwen3".

###

`qkv_bias = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.qkv_bias)

Do QKV projection a bias

###

`rope_scaling_layers = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.rope_scaling_layers)

RoPE scaling layers.

###

`rope_theta = 1000000.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.rope_theta)

RoPE theta parameter.

###

`use_qk_norm = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.use_qk_norm)

Apply layer norm to the keys and queries within the attention mechanism. This can help stabilize training.

###

`vocab_size = 152064`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.TextConfig.vocab_size)

Vocabulary size of the model.

##

`ViTMLP`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.ViTMLP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

MLP used in Vision Transformer.

## Source code in `vllm/model_executor/models/molmo2.py`


##

`ViTMultiHeadDotProductAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.ViTMultiHeadDotProductAttention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Multi-head attention used in Vision Transformer.

## Source code in `vllm/model_executor/models/molmo2.py`


##

`VitConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.VitConfig)

Config for a vision transformer.

## Source code in `vllm/model_executor/models/molmo2.py`


##

`get_candidate_target_fps(video_fps, sampling_fps, max_fps=_MAX_VIDEO_FPS)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.get_candidate_target_fps)

Return the subset of `video_fps`

factors that remain multiples of `sampling_fps`

.

Examples:

>>> get_candidate_target_fps(video_fps=6, sampling_fps=2)
[2, 6]
>>> get_candidate_target_fps(video_fps=5, sampling_fps=1)
[1, 5]
>>> get_candidate_target_fps(video_fps=2, sampling_fps=2)
[2]
>>> get_candidate_target_fps(video_fps=5, sampling_fps=2)
Traceback (most recent call last):
...
ValueError: sampling_fps=2 must divide video_fps=5 to produce
consistent frame steps.


## Source code in `vllm/model_executor/models/molmo2.py`


##

`get_target_fps(video_fps, max_frames, total_frames, frame_sample_mode, candidate_target_fps)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.molmo2.get_target_fps)

Get the target fps that best spans the video and has the most frames sampled.
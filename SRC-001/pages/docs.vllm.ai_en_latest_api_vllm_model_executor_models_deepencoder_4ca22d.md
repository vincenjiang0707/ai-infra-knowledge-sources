source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/deepencoder/
lastmod: 2026-09-23

#

`vllm.model_executor.models.deepencoder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder)

Classes:

-
–[Block](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.Block)Transformer blocks with support of window attention and residual propagation

-
–[ImageEncoderViT](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.ImageEncoderViT) -
–[PatchEmbed](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.PatchEmbed)Image to Patch Embedding.

-
–[RelPosAttention](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.RelPosAttention)Multi-head Attention block with relative position embeddings.


Functions:

-
–[add_decomposed_rel_pos](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.add_decomposed_rel_pos)Calculate decomposed Relative Positional Embeddings from :paper:

`mvitv2`

. -
–[deepencoder_rel_pos_attention](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.deepencoder_rel_pos_attention)Run DeepEncoder global attention with fused relative-position bias.

-
–[get_rel_pos](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.get_rel_pos)Get relative positional embeddings according to the relative positions of

-
–[window_partition](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.window_partition)Partition into non-overlapping windows with padding if needed.

-
–[window_unpartition](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.window_unpartition)Window unpartition into original sequences and removing padding.


##

`Block`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.Block)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Transformer blocks with support of window attention and residual propagation blocks

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.Block.__init__)Args:


## Source code in `vllm/model_executor/models/deepencoder.py`


###

`__init__(dim, num_heads, mlp_ratio=4.0, qkv_bias=True, norm_layer=nn.LayerNorm, act_layer=nn.GELU, use_rel_pos=False, rel_pos_zero_init=True, window_size=0, input_size=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.Block.__init__)

Args: dim (int): Number of input channels. num_heads (int): Number of attention heads in each ViT block. mlp_ratio (float): Ratio of mlp hidden dim to embedding dim. qkv_bias (bool): If True, add a learnable bias to query, key, value. norm_layer (nn.Module): Normalization layer. act_layer (nn.Module): Activation layer. use_rel_pos (bool): If True, add relative positional embeddings to the attention map. rel_pos_zero_init (bool): If True, zero initialize relative positional parameters. window_size (int): Window size for window attention blocks. If it equals 0, then use global attention. input_size (tuple(int, int) or None): Input resolution for calculating the relative positional parameter size.

## Source code in `vllm/model_executor/models/deepencoder.py`


##

`ImageEncoderViT`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.ImageEncoderViT)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.ImageEncoderViT.__init__)Args:


## Source code in `vllm/model_executor/models/deepencoder.py`


|
|

###

`__init__(img_size=1024, patch_size=16, in_chans=3, embed_dim=768, depth=12, num_heads=12, mlp_ratio=4.0, out_chans=256, qkv_bias=True, norm_layer=nn.LayerNorm, act_layer=nn.GELU, use_abs_pos=True, use_rel_pos=False, rel_pos_zero_init=True, window_size=0, global_attn_indexes=(), last_conv_output=1024)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.ImageEncoderViT.__init__)

Args: img_size (int): Input image size. patch_size (int): Patch size. in_chans (int): Number of input image channels. embed_dim (int): Patch embedding dimension. depth (int): Depth of ViT. num_heads (int): Number of attention heads in each ViT block. mlp_ratio (float): Ratio of mlp hidden dim to embedding dim. qkv_bias (bool): If True, add a learnable bias to query, key, value. norm_layer (nn.Module): Normalization layer. act_layer (nn.Module): Activation layer. use_abs_pos (bool): If True, use absolute positional embeddings. use_rel_pos (bool): If True, add relative positional embeddings to the attention map. rel_pos_zero_init (bool): If True, zero initialize relative positional parameters. window_size (int): Window size for window attention blocks. global_attn_indexes (list): Indexes for blocks using global attention.

## Source code in `vllm/model_executor/models/deepencoder.py`


|
|

##

`PatchEmbed`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.PatchEmbed)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Image to Patch Embedding.

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.PatchEmbed.__init__)Args:


## Source code in `vllm/model_executor/models/deepencoder.py`


###

`__init__(kernel_size=(16, 16), stride=(16, 16), padding=(0, 0), in_chans=3, embed_dim=768)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.PatchEmbed.__init__)

Args: kernel_size (Tuple): kernel size of the projection layer. stride (Tuple): stride of the projection layer. padding (Tuple): padding size of the projection layer. in_chans (int): Number of input image channels. embed_dim (int): Patch embedding dimension.

## Source code in `vllm/model_executor/models/deepencoder.py`


##

`RelPosAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.RelPosAttention)

Bases: [PluggableLayer](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.PluggableLayer)

Multi-head Attention block with relative position embeddings.

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.RelPosAttention.__init__)Args:


## Source code in `vllm/model_executor/models/deepencoder.py`


|
|

###

`__init__(dim, num_heads=8, qkv_bias=True, use_rel_pos=False, use_triton_attention=False, rel_pos_zero_init=True, input_size=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.RelPosAttention.__init__)

Args: dim (int): Number of input channels. num_heads (int): Number of attention heads. qkv_bias (bool): If True, add a learnable bias to query, key, value. use_triton_attention (bool): If True, fuse relative position bias in a Triton attention kernel on CUDA-alike platforms. rel_pos_zero_init (bool): If True, zero initialize relative positional parameters. input_size (tuple(int, int) or None): Input resolution for calculating the relative positional parameter size.

## Source code in `vllm/model_executor/models/deepencoder.py`


##

`add_decomposed_rel_pos(q, rel_pos_h, rel_pos_w, q_size, k_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.add_decomposed_rel_pos)

Calculate decomposed Relative Positional Embeddings from :paper:`mvitv2`

. https://github.com/facebookresearch/mvit/blob/19786631e330df9f3622e5402b4a419a263a2c80/mvit/models/attention.py Args: q (Tensor): query q in the attention layer with shape (B, q_h * q_w, C). rel_pos_h (Tensor): relative position embeddings (Lh, C) for height axis. rel_pos_w (Tensor): relative position embeddings (Lw, C) for width axis. q_size (Tuple): spatial sequence size of query q with (q_h, q_w). k_size (Tuple): spatial sequence size of key k with (k_h, k_w).

Returns:

-
(`attn`

`Tensor`

) –attention map with added relative positional embeddings.


## Source code in `vllm/model_executor/models/deepencoder.py`


##

`deepencoder_rel_pos_attention(q, k, v, rel_h, rel_w, width, scale)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.deepencoder_rel_pos_attention)

Run DeepEncoder global attention with fused relative-position bias.

## Source code in `vllm/model_executor/models/deepencoder.py`


##

`get_rel_pos(q_size, k_size, rel_pos)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.get_rel_pos)

Get relative positional embeddings according to the relative positions of query and key sizes.

Parameters:

-

(`q_size`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.get_rel_pos(q_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)size of query q.

-

(`k_size`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.get_rel_pos(k_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)size of key k.

-

(`rel_pos`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.get_rel_pos(rel_pos))`Tensor`

) –relative position embeddings (L, C).


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Extracted positional embeddings according to relative positions.


## Source code in `vllm/model_executor/models/deepencoder.py`


##

`window_partition(x, window_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.window_partition)

Partition into non-overlapping windows with padding if needed.

Parameters:

Returns:

-
(`windows`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)windows after partition with [B * num_windows, window_size, window_size, C].

-
`(Hp, Wp)`

–padded height and width before partition


## Source code in `vllm/model_executor/models/deepencoder.py`


##

`window_unpartition(windows, window_size, pad_hw, hw)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.window_unpartition)

Window unpartition into original sequences and removing padding.

Parameters:

-

(`windows`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.window_unpartition(windows))`tensor`

) –input tokens with [B * num_windows, window_size, window_size, C].

-

(`window_size`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.window_unpartition(window_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)window size.

-

(`pad_hw`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.window_unpartition(pad_hw))`Tuple`

) –padded height and width (Hp, Wp).

-

(`hw`

[¶](https://docs.vllm.ai#vllm.model_executor.models.deepencoder.window_unpartition(hw))`Tuple`

) –original height and width (H, W) before padding.


Returns:

-
(`x`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)unpartitioned sequences with [B, H, W, C].
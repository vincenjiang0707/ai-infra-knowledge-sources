source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/resampler/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.resampler`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.resampler)

Shared resampler perceiver network used in multimodal models and related helpers for sincos positional embeddings.

Example models: Qwen (Qwen-VL), MiniCPM-V 2.0

Classes:

-
–[BaseResampler](https://docs.vllm.ai#vllm.model_executor.layers.resampler.BaseResampler)A 2D perceiver-resampler network with one cross attention layers by

-
–[Resampler2](https://docs.vllm.ai#vllm.model_executor.layers.resampler.Resampler2)Resampler-perceiver network to be used for a variety of model types,


Functions:

-
–[get_1d_sincos_pos_embed_from_grid](https://docs.vllm.ai#vllm.model_executor.layers.resampler.get_1d_sincos_pos_embed_from_grid)embed_dim: output dimension for each position

-
–[get_2d_sincos_pos_embed](https://docs.vllm.ai#vllm.model_executor.layers.resampler.get_2d_sincos_pos_embed)grid_size: int of the grid height and width


##

`BaseResampler`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.resampler.BaseResampler)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

A 2D perceiver-resampler network with one cross attention layers by (grid_size**2) learnable queries and 2d sincos pos_emb. Outputs: A tensor with the shape of (grid_size**2, embed_dim)

## Source code in `vllm/model_executor/layers/resampler.py`


##

`Resampler2`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.resampler.Resampler2)

Bases: [BaseResampler](https://docs.vllm.ai#vllm.model_executor.layers.resampler.BaseResampler)

Resampler-perceiver network to be used for a variety of model types, e.g., Qwen-vl / Minicpmv 2.0. The main difference is the addition of the do_post_projection arg, which indicates whether or not there should be a post layer normalization and projector after the attention. This is present in minicpmv2.0, but not qwen-vl.

## Source code in `vllm/model_executor/layers/resampler.py`


##

`get_1d_sincos_pos_embed_from_grid(embed_dim, pos, version=(2, 0))`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.resampler.get_1d_sincos_pos_embed_from_grid)

embed_dim: output dimension for each position pos: a list of positions to be encoded: size (M,) / (H, W) out: (M, D) / (H, W, D)

## Source code in `vllm/model_executor/layers/resampler.py`


##

`get_2d_sincos_pos_embed(embed_dim, grid_size, cls_token=False, version=(2, 0))`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.resampler.get_2d_sincos_pos_embed)

grid_size: int of the grid height and width return: pos_embed: [grid_size*grid_size, embed_dim] or [1+grid_size*grid_size, embed_dim] (w/ or w/o cls_token)
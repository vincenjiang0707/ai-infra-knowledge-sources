source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/rotary_embedding/mrope_vit_setup/
lastmod: 2026-09-27

#

`vllm.model_executor.layers.rotary_embedding.mrope_vit_setup`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.mrope_vit_setup)

Functions:

-
–[vit_mrope_setup](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.mrope_vit_setup.vit_mrope_setup)(3, total_N, half_rot_dim) fp32 cos/sin t/h/w planes for triton_mrope.


##

`_vit_mrope_setup_kernel(inv_freq_t_ptr, inv_freq_h_ptr, inv_freq_w_ptr, cos_out_ptr, sin_out_ptr, cu_seqlens_ptr, grids_ptr, num_tokens, num_grids, half_t, half_h, half_w, spatial_merge, BLOCK_N, BLOCK_D)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.mrope_vit_setup._vit_mrope_setup_kernel)

Build triton_mrope's (3, N, half_rot) cos/sin t/h/w planes in one launch: compute each token's (t, h, w) position arithmetically and the rotation in fp32 from the per-axis inv_freq. Only each axis's mrope section columns are written; the rest is left uninitialized (the consumer's per-axis masked loads read only the section columns).

## Source code in `vllm/model_executor/layers/rotary_embedding/mrope_vit_setup.py`


##

`vit_mrope_setup(inv_freq_t, inv_freq_h, inv_freq_w, grid_thw, spatial_merge_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.mrope_vit_setup.vit_mrope_setup)

(3, total_N, half_rot_dim) fp32 cos/sin t/h/w planes for triton_mrope.

One fused kernel: positions are computed arithmetically from the grids and the rotation comes from the per-axis inv_freq, so there is no cos/sin cache to size or grow.

Parameters:

-

(`inv_freq_t`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.mrope_vit_setup.vit_mrope_setup(inv_freq_t))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)t-axis inverse frequencies, (t_dim // 2,).

-

(`inv_freq_h`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.mrope_vit_setup.vit_mrope_setup(inv_freq_h))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)h-axis inverse frequencies, (h_dim // 2,).

-

(`inv_freq_w`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.mrope_vit_setup.vit_mrope_setup(inv_freq_w))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)w-axis inverse frequencies, (w_dim // 2,).

-

(`grid_thw`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.mrope_vit_setup.vit_mrope_setup(grid_thw))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]per-grid [t, h, w] patch counts (host metadata).

-

(`spatial_merge_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.mrope_vit_setup.vit_mrope_setup(spatial_merge_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)spatial merge factor of the ViT.
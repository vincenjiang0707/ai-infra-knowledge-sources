source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/mhc/tilelang_kernels/
lastmod: 2026-09-24

#

`vllm.model_executor.kernels.mhc.tilelang_kernels`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang_kernels)

Functions:

-
–[hc_head_fuse_tilelang](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang_kernels.hc_head_fuse_tilelang)Two-pass fused kernel for hc_head.

-
–[mhc_fused_post_pre_split_config](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang_kernels.mhc_fused_post_pre_split_config)Pick

`(tile_n, n_splits, n_thr)`

for the fused post + pre-norm GEMM. -
–[mhc_fused_post_pre_splits](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang_kernels.mhc_fused_post_pre_splits)Every split-k factor the fused post + pre-norm GEMM path can pick.

-
–[mhc_fused_tilelang](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang_kernels.mhc_fused_tilelang)Fused mhc post-mapping + pre-norm GEMM FMA.

-
–[mhc_pre_big_fuse_tilelang](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang_kernels.mhc_pre_big_fuse_tilelang)Fuse coefficient generation and residual collapse after the projection.

-
–[require_fused_post_pre_config](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang_kernels.require_fused_post_pre_config)The config for a shape the caller has already committed to fusing.


##

`hc_head_fuse_tilelang(residual, fn, hc_scale, hc_base, out, hidden_size, rms_eps, hc_eps, hc_mult=4, n_thr=128, h_blk=1024)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang_kernels.hc_head_fuse_tilelang)

Two-pass fused kernel for hc_head.

## accumulate per-token squared sum and hc_mult dot-products

(projections onto fn rows) using cross-thread reducers.

Pass 2: apply sigmoid-gated weighted sum of residual channels to output.

Avoids materialising mixes / rsqrt / pre tensors to global memory.

## Source code in `vllm/model_executor/kernels/mhc/tilelang_kernels.py`


|
|

##

`mhc_fused_post_pre_split_config(num_tokens, hidden_size, hc_mult)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang_kernels.mhc_fused_post_pre_split_config)

Pick `(tile_n, n_splits, n_thr)`

for the fused post + pre-norm GEMM.

Returns None when a separate post kernel followed by a split-k GEMM is the better choice, or when the hidden size does not divide evenly across the fused kernel's block. One source of truth for the dispatch decision, the compile key and the launch, which must agree.

## Source code in `vllm/model_executor/kernels/mhc/tilelang_kernels.py`


##

`mhc_fused_post_pre_splits(hidden_size, hc_mult)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang_kernels.mhc_fused_post_pre_splits)

Every split-k factor the fused post + pre-norm GEMM path can pick.

## Source code in `vllm/model_executor/kernels/mhc/tilelang_kernels.py`


##

`mhc_fused_tilelang(comb_mix, residual_in, post_mix, x_in, weight_t, yp_out, rp_out, residual_out, hc, hidden, n_out, n_thr=256, h_blk=256, tile_n=1, split_k=1)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang_kernels.mhc_fused_tilelang)

Fused mhc post-mapping + pre-norm GEMM FMA.

## Source code in `vllm/model_executor/kernels/mhc/tilelang_kernels.py`


|
|

##

`mhc_pre_big_fuse_tilelang(gemm_out_mul, gemm_out_sqrsum, hc_scale, hc_base, residual, post_mix, comb_mix, layer_input, pre_mix_in, pre_mix_out, aux_out, hidden_size, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, n_splits=16, hc_mult=4, use_pre_mix_in=False, save_pre_mix=False, rms_numel=0, write_aux=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang_kernels.mhc_pre_big_fuse_tilelang)

Fuse coefficient generation and residual collapse after the projection.

With save_pre_mix, store the new pre-mix and collapse with pre_mix_in, or select stream zero when use_pre_mix_in is false.

## Source code in `vllm/model_executor/kernels/mhc/tilelang_kernels.py`


|
|

##

`require_fused_post_pre_config(num_tokens, hidden_size, hc_mult)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang_kernels.require_fused_post_pre_config)

The config for a shape the caller has already committed to fusing.
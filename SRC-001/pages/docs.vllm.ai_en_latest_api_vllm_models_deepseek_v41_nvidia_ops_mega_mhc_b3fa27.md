source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/nvidia/ops/mega_mhc/
lastmod: 2026-09-23

#

`vllm.models.deepseek_v41.nvidia.ops.mega_mhc`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops.mega_mhc)

Functions:

-
–[is_mega_mhc_supported](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops.mega_mhc.is_mega_mhc_supported)Return whether DeepGEMM can run the DSV4.1 shifted mHC kernel.

-
–[mhc_shifted_post_pre_deep_gemm](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops.mega_mhc.mhc_shifted_post_pre_deep_gemm)Run DSV4.1 shifted post, next pre, and BF16 RMSNorm with Mega mHC.


##

`is_mega_mhc_supported(hidden_size, hc_mult)`

`cached`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops.mega_mhc.is_mega_mhc_supported)

Return whether DeepGEMM can run the DSV4.1 shifted mHC kernel.

## Source code in `vllm/models/deepseek_v41/nvidia/ops/mega_mhc.py`


##

`mhc_shifted_post_pre_deep_gemm(x, residual, shifted_prev_mix, post_mix, comb_res_mix, fn, mix_scales, mix_bases, hc_norm_eps, hc_pre_eps, hc_post_scale, sinkhorn_eps, num_sinkhorn_iters, rmsnorm_weight, rmsnorm_eps)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops.mega_mhc.mhc_shifted_post_pre_deep_gemm)

Run DSV4.1 shifted post, next pre, and BF16 RMSNorm with Mega mHC.
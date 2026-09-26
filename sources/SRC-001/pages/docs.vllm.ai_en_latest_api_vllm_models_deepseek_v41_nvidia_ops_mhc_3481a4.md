source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/nvidia/ops/mhc/
lastmod: 2026-09-24

#

`vllm.models.deepseek_v41.nvidia.ops.mhc`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops.mhc)

Dispatch DSV4.1 mHC operations and overlap coefficient generation.

Functions:

-
–[mhc_pre_delayed_overlap](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops.mhc.mhc_pre_delayed_overlap)Prepare the input on the caller stream and coefficients on another stream.

-
–[mhc_shifted_post_pre](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops.mhc.mhc_shifted_post_pre)Dispatch shifted post/pre to overlap, Mega-mHC, or fused TileLang.

-
–[supports_mhc_overlap](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops.mhc.supports_mhc_overlap)Check kernel requirements and safety of sharing the coefficient stream.


##

`mhc_pre_delayed_overlap(residual, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, pre_mix=None, x=None, norm_weight=None, norm_eps=1e-06, *, stream, layer_input=None)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops.mhc.mhc_pre_delayed_overlap)

Prepare the input on the caller stream and coefficients on another stream.

Returns post mix, residual mix, normalized input, and next pre-mix. Only the input is ready on the caller stream; join stream before using coefficients. The caller must retain the weights and coefficient outputs until the join.

## Source code in `vllm/models/deepseek_v41/nvidia/ops/mhc.py`


|
|

##

`mhc_shifted_post_pre(x, residual, post_layer_mix, comb_res_mix, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, pre_mix=None, norm_weight=None, norm_eps=1e-06, capture_aux=False, *, stream=None, reduce_results=False)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops.mhc.mhc_shifted_post_pre)

Dispatch shifted post/pre to overlap, Mega-mHC, or fused TileLang.

When stream is supplied, join it before consuming the returned coefficients.

## Source code in `vllm/models/deepseek_v41/nvidia/ops/mhc.py`


|
|

##

`supports_mhc_overlap(vllm_config)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops.mhc.supports_mhc_overlap)

Check kernel requirements and safety of sharing the coefficient stream.
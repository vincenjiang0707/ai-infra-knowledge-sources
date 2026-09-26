source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/common/towers/
lastmod: 2026-09-24

#

`vllm.models.inkling.common.towers`

[¶](https://docs.vllm.ai#vllm.models.inkling.common.towers)

Inkling Titan vision + audio towers.

The vision tower (`InklingVision`

/ `HMLPPatchEncoder`

) emits one token per image patch; the audio tower (`InklingAudio`

) emits one token per audio frame. Both use vLLM's standard `RMSNorm`

(CPU-friendly, with a native fallback).

Functions:

-
–[fold_timespace_to_depth](https://docs.vllm.ai#vllm.models.inkling.common.towers.fold_timespace_to_depth)(B, T, H, W, C) -> (B, T//t, H//hw, W//hw, C

*(t*hw**2)). -
–[linear_sum_assignment](https://docs.vllm.ai#vllm.models.inkling.common.towers.linear_sum_assignment)Implement SciPy's assignment for Inkling's ordered L1 cost matrix.

-
–[plan_out_scales](https://docs.vllm.ai#vllm.models.inkling.common.towers.plan_out_scales)Plan the (t, h, w, c) dimensions for each HMLP layer.


##

`_prime_factors(n)`

[¶](https://docs.vllm.ai#vllm.models.inkling.common.towers._prime_factors)

Return the prime factors of *n* in ascending order.

## Source code in `vllm/models/inkling/common/towers.py`


##

`fold_timespace_to_depth(vision_patches_bthwc, t_fold, hw_fold)`

[¶](https://docs.vllm.ai#vllm.models.inkling.common.towers.fold_timespace_to_depth)

(B, T, H, W, C) -> (B, T//t, H//hw, W//hw, C*(t*hw**2)).

## Source code in `vllm/models/inkling/common/towers.py`


##

`linear_sum_assignment(cost_matrix)`

[¶](https://docs.vllm.ai#vllm.models.inkling.common.towers.linear_sum_assignment)

Implement SciPy's assignment for Inkling's ordered L1 cost matrix.

## Source code in `vllm/models/inkling/common/towers.py`


##

`plan_out_scales(temporal_patch_size, patch_size, n_layers, n_channels=3)`

[¶](https://docs.vllm.ai#vllm.models.inkling.common.towers.plan_out_scales)

Plan the (t, h, w, c) dimensions for each HMLP layer.

Spatial dims expand first, then temporal; channel counts round up to multiples of 64.
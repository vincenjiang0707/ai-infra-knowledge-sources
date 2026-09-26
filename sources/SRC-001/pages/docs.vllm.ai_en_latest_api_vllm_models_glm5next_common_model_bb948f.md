source: https://docs.vllm.ai/en/latest/api/vllm/models/glm5next/common/model/
lastmod: 2026-09-24

#

`vllm.models.glm5next.common.model`

[¶](https://docs.vllm.ai#vllm.models.glm5next.common.model)

##

`_dequant_fp8_block(weight_fp8, scale_inv, block_size=128)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.common.model._dequant_fp8_block)

Dequantize a block-FP8 (e4m3) weight with per-block scale to BF16.

Unlike `scaled_dequantize`

this tolerates a non-divisible (partial last block) shape by zero-padding to a multiple of `block_size`

before the scale broadcast and trimming back afterwards (e.g. kv_a_proj_with_mqa is 576 rows = 4*128 + 64).

## Source code in `vllm/models/glm5next/common/model.py`


##

`_try_load_fp8_attn_proj(name, tensor, buf, params_dict, loaded_params, kv_a_pad_size)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.common.model._try_load_fp8_attn_proj)

Dequantize FP8 q_a_proj / kv_a_proj_with_mqa / o_proj to BF16 on load.

The FP8 checkpoint stores these as block-FP8 (weight + weight_scale_inv), but the model holds them in BF16 (`fused_qkv_a_proj`

is always BF16 via DeepSeekV2FusedQkvAProjLinear; `o_proj`

is excluded by modules_to_not_convert). When the model target is BF16 (no `weight_scale_inv`

param) we dequantize; otherwise we return False so the normal stacked/direct path loads the FP8 tensor as-is.

## Source code in `vllm/models/glm5next/common/model.py`


|
|
source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/quark/utils/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.quantization.quark.utils`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.utils)

Functions:

-
–[canonicalize_quark_packed_int4](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.utils.canonicalize_quark_packed_int4)Convert Quark export nibble layout to AWQ checkpoint layout.

-
–[parse_w4a16_int4_weight_config](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.utils.parse_w4a16_int4_weight_config)Parse required W4A16 INT4/UINT4 weight fields from Quark config.


##

`canonicalize_quark_packed_int4(packed_weight, *, pack_reorder, is_symmetric, pack_factor=8)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.utils.canonicalize_quark_packed_int4)

Convert Quark export nibble layout to AWQ checkpoint layout.

## Source code in `vllm/model_executor/layers/quantization/quark/utils.py`


##

`parse_w4a16_int4_weight_config(weight_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.utils.parse_w4a16_int4_weight_config)

Parse required W4A16 INT4/UINT4 weight fields from Quark config.
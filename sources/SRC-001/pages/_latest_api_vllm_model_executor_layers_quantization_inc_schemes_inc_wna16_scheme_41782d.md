source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/inc/schemes/inc_wna16_scheme/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.quantization.inc.schemes.inc_wna16_scheme`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.inc.schemes.inc_wna16_scheme)

##

`_check_xpu_w4a8_supported(layer_config, prefix)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.inc.schemes.inc_wna16_scheme._check_xpu_w4a8_supported)

Raise unless `int4_gemm_w4a8`

can serve this layer.

The backend is requested explicitly, so an unusable configuration is an error rather than something to silently fall back from.

## Source code in `vllm/model_executor/layers/quantization/inc/schemes/inc_wna16_scheme.py`


##

`_humming_weight_config(layer_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.inc.schemes.inc_wna16_scheme._humming_weight_config)

Build the humming weight-schema config for a WNA16 int checkpoint.
source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/inc/schemes/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.quantization.inc.schemes`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.inc.schemes)

Modules:

-
–[inc_ark_ops](https://docs.vllm.ai/inc_ark_ops/#vllm.model_executor.layers.quantization.inc.schemes.inc_ark_ops) -
–[inc_mxfp4_linear](https://docs.vllm.ai/inc_mxfp4_linear/#vllm.model_executor.layers.quantization.inc.schemes.inc_mxfp4_linear) -
–[inc_mxfp4_moe](https://docs.vllm.ai/inc_mxfp4_moe/#vllm.model_executor.layers.quantization.inc.schemes.inc_mxfp4_moe) -
–[inc_mxfp4_scheme](https://docs.vllm.ai/inc_mxfp4_scheme/#vllm.model_executor.layers.quantization.inc.schemes.inc_mxfp4_scheme) -
–[inc_mxfp8_moe](https://docs.vllm.ai/inc_mxfp8_moe/#vllm.model_executor.layers.quantization.inc.schemes.inc_mxfp8_moe) -
–[inc_scheme](https://docs.vllm.ai/inc_scheme/#vllm.model_executor.layers.quantization.inc.schemes.inc_scheme) -
–[inc_w4a8_linear](https://docs.vllm.ai/inc_w4a8_linear/#vllm.model_executor.layers.quantization.inc.schemes.inc_w4a8_linear) -
–[inc_wna16_linear](https://docs.vllm.ai/inc_wna16_linear/#vllm.model_executor.layers.quantization.inc.schemes.inc_wna16_linear) -
–[inc_wna16_scheme](https://docs.vllm.ai/inc_wna16_scheme/#vllm.model_executor.layers.quantization.inc.schemes.inc_wna16_scheme)

Classes:

-
–[INCMxfp4Scheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.inc.schemes.INCMxfp4Scheme)MXFP4 (W4A4) scheme for AutoRound checkpoints.

-
–[INCScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.inc.schemes.INCScheme)One class per quant type. Single registration point for the factory.


##

`INCMxfp4Scheme`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.inc.schemes.INCMxfp4Scheme)

Bases: [INCScheme](https://docs.vllm.ai/inc_scheme/#vllm.model_executor.layers.quantization.inc.schemes.inc_scheme.INCScheme)

MXFP4 (W4A4) scheme for AutoRound checkpoints.

Dispatches to :class:`INCMxfp4LinearMethod`

for linear layers and :class:`INCMxfp4MoEMethod`

for fused MoE layers; see those classes for the per-module weight layout and kernel-selection details.

## Source code in `vllm/model_executor/layers/quantization/inc/schemes/inc_mxfp4_scheme.py`


##

`INCScheme`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.inc.schemes.INCScheme)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

One class per quant type. Single registration point for the factory.

## Each subclass defines

- can_handle(): when does this scheme apply?
- get_linear_method(): required — how to quantize Linear layers
- get_moe_method(): optional — how to quantize MoE layers

Schemes that don't support MoE/KVCache inherit the default raise.

Methods:

-
–[get_moe_method](https://docs.vllm.ai#vllm.model_executor.layers.quantization.inc.schemes.INCScheme.get_moe_method)Optional. Override if this scheme supports MoE.


## Source code in `vllm/model_executor/layers/quantization/inc/schemes/inc_scheme.py`


###

`get_moe_method(config, layer, prefix, layer_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.inc.schemes.INCScheme.get_moe_method)

Optional. Override if this scheme supports MoE. Default raises NotImplementedError.
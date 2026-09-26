source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/online/fp8/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.quantization.online.fp8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8)

Classes:

-
–[Fp8PerBlockOnlineLinearMethod](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8.Fp8PerBlockOnlineLinearMethod)Online blockwise FP8 linear quantization.

-
–[Fp8PerBlockOnlineMoEMethod](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8.Fp8PerBlockOnlineMoEMethod)Online blockwise FP8 MoE quantization.

-
–[Fp8PerTensorOnlineLinearMethod](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8.Fp8PerTensorOnlineLinearMethod)Online tensorwise FP8 linear quantization.

-
–[Fp8PerTensorOnlineMoEMethod](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8.Fp8PerTensorOnlineMoEMethod)Online tensorwise FP8 MoE quantization.

-
–[Fp8PtpcOnlineLinearMethod](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8.Fp8PtpcOnlineLinearMethod)Online PTPC FP8 linear quantization.

-
–[Fp8PtpcOnlineMoEMethod](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8.Fp8PtpcOnlineMoEMethod)Online PTPC FP8 MoE quantization.

-
–[OnlineLinearBase](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8.OnlineLinearBase)Shared base for online FP8 linear methods. Loads fp16/bf16 checkpoint


##

`Fp8PerBlockOnlineLinearMethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8.Fp8PerBlockOnlineLinearMethod)

Bases: [OnlineLinearBase](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8.OnlineLinearBase)

Online blockwise FP8 linear quantization. Loads fp16/bf16 weights and quantizes them per-block during loading.

## Source code in `vllm/model_executor/layers/quantization/online/fp8.py`


|
|

##

`Fp8PerBlockOnlineMoEMethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8.Fp8PerBlockOnlineMoEMethod)

Bases: [_Fp8OnlineMoEBase](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8._Fp8OnlineMoEBase)

Online blockwise FP8 MoE quantization. Loads fp16/bf16 weights and quantizes them per-block during loading.

## Source code in `vllm/model_executor/layers/quantization/online/fp8.py`


|
|

##

`Fp8PerTensorOnlineLinearMethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8.Fp8PerTensorOnlineLinearMethod)

Bases: [OnlineLinearBase](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8.OnlineLinearBase)

Online tensorwise FP8 linear quantization. Loads fp16/bf16 weights and quantizes them per-tensor during loading.

## Source code in `vllm/model_executor/layers/quantization/online/fp8.py`


|
|

##

`Fp8PerTensorOnlineMoEMethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8.Fp8PerTensorOnlineMoEMethod)

Bases: [_Fp8OnlineMoEBase](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8._Fp8OnlineMoEBase)

Online tensorwise FP8 MoE quantization. Loads fp16/bf16 weights and quantizes them per-tensor during loading.

## Source code in `vllm/model_executor/layers/quantization/online/fp8.py`


##

`Fp8PtpcOnlineLinearMethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8.Fp8PtpcOnlineLinearMethod)

Bases: [OnlineLinearBase](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8.OnlineLinearBase)

Online PTPC FP8 linear quantization.

Per-output-channel weight scale + dynamic per-token activation scale. The layout matches the llmcompressor's FP8_DYNAMIC recipe, so accuracy is comparable but no pre-quantized checkpoint is required.

## Source code in `vllm/model_executor/layers/quantization/online/fp8.py`


|
|

##

`Fp8PtpcOnlineMoEMethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8.Fp8PtpcOnlineMoEMethod)

Bases: [_Fp8OnlineMoEBase](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8._Fp8OnlineMoEBase)

Online PTPC FP8 MoE quantization.

Quantizes each expert's weights per output channel during loading. Activations are quantized dynamically per token at runtime.

## Source code in `vllm/model_executor/layers/quantization/online/fp8.py`


|
|

##

`OnlineLinearBase`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8.OnlineLinearBase)

Bases: [LinearMethodBase](https://docs.vllm.ai/linear/#vllm.model_executor.layers.linear.LinearMethodBase)

Shared base for online FP8 linear methods. Loads fp16/bf16 checkpoint weights onto meta device and materializes them just-in-time.

## Source code in `vllm/model_executor/layers/quantization/online/fp8.py`


##

`_Fp8OnlineMoEBase`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8._Fp8OnlineMoEBase)

Bases: [OnlineMoEMethodBase](https://docs.vllm.ai/moe_base/#vllm.model_executor.layers.quantization.online.moe_base.OnlineMoEMethodBase)

Shared base for online FP8 MoE methods. Loads fp16/bf16 checkpoint weights onto meta device and materializes them just-in-time.

## Source code in `vllm/model_executor/layers/quantization/online/fp8.py`


|
|

##

`_is_tp_sharded(layer, *, reduces_output_dim=True)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.online.fp8._is_tp_sharded)

Whether the weight is sharded along a dim its `amax`

reduces over.

Row parallel shards the input dim, column parallel the output dim. Per-output-channel scales only reduce the input dim, so they are already unsharded-equivalent on column-parallel layers.
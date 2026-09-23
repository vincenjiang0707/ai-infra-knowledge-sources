source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/experts_int8/
lastmod: 2026-09-23

Bases: [QuantizationConfig](../base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)


Online int8 quantization for MoE expert weights. Linear layers are left unquantized.

Backward-compatible config for `--quantization experts_int8`

. Prefer `--quantization int8_per_channel`


## Source code in `vllm/model_executor/layers/quantization/experts_int8.py`


| class ExpertsInt8Config(QuantizationConfig):
"""Online int8 quantization for MoE expert weights.
Linear layers are left unquantized.
Backward-compatible config for ``--quantization experts_int8``.
Prefer ``--quantization int8_per_channel``
"""
def __init__(self) -> None:
super().__init__()
@classmethod
def get_name(cls) -> QuantizationMethods:
return "experts_int8"
@classmethod
def get_supported_act_dtypes(cls) -> list[torch.dtype]:
return [torch.bfloat16, torch.half]
@classmethod
def get_min_capability(cls) -> int:
return 80
@classmethod
def get_config_filenames(cls) -> list[str]:
return []
@classmethod
def from_config(cls, config: dict[str, Any]) -> "ExpertsInt8Config":
return cls()
def get_quant_method(
self, layer: torch.nn.Module, prefix: str
) -> "QuantizeMethodBase | None":
if isinstance(layer, LinearBase):
return UnquantizedLinearMethod()
elif isinstance(layer, RoutedExperts):
return Int8OnlineMoEMethod(moe=layer.moe_config)
return None
|
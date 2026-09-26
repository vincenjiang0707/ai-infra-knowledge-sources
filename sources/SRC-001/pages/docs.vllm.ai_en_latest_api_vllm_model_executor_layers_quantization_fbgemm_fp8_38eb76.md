source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/fbgemm_fp8/
lastmod: 2026-09-24

Bases: [QuantizationConfig](../base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)


Config class for FBGEMM Fp8.

## Source code in `vllm/model_executor/layers/quantization/fbgemm_fp8.py`


| class FBGEMMFp8Config(QuantizationConfig):
"""Config class for FBGEMM Fp8."""
def __init__(self, ignore_list: list[str], input_scale_ub: float):
super().__init__()
self.ignore_list = ignore_list if ignore_list else []
self.input_scale_ub = input_scale_ub
# For GPUs that lack FP8 hardware support, we can leverage the Marlin
# kernel for fast weight-only FP8 quantization
self.use_marlin = not current_platform.has_device_capability(89)
@classmethod
def get_name(cls) -> QuantizationMethods:
return "fbgemm_fp8"
@classmethod
def get_supported_act_dtypes(cls) -> list[torch.dtype]:
return [torch.bfloat16, torch.float16]
@classmethod
def get_min_capability(cls) -> int:
return 80
@classmethod
def get_config_filenames(cls) -> list[str]:
return []
@classmethod
def from_config(cls, config: dict[str, Any]) -> "FBGEMMFp8Config":
ignore_list = cls.get_from_keys(config, ["modules_to_not_convert"])
input_scale_ub = cls.get_from_keys(config, ["activation_scale_ub"])
return cls(ignore_list=ignore_list, input_scale_ub=input_scale_ub)
def get_quant_method(
self, layer: torch.nn.Module, prefix: str
) -> "QuantizeMethodBase | None":
if isinstance(layer, LinearBase):
if is_layer_skipped(
prefix=prefix,
ignored_layers=self.ignore_list,
fused_mapping=self.packed_modules_mapping,
):
return UnquantizedLinearMethod()
return FBGEMMFp8LinearMethod(self)
return None
|
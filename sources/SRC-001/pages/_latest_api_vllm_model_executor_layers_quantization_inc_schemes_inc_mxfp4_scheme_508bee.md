source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/inc/schemes/inc_mxfp4_scheme/
lastmod: 2026-09-24

Bases: [INCScheme](../inc_scheme/#vllm.model_executor.layers.quantization.inc.schemes.inc_scheme.INCScheme)


MXFP4 (W4A4) scheme for AutoRound checkpoints.

Dispatches to :class:`INCMxfp4LinearMethod`

for linear layers and :class:`INCMxfp4MoEMethod`

for fused MoE layers; see those classes for the per-module weight layout and kernel-selection details.

## Source code in `vllm/model_executor/layers/quantization/inc/schemes/inc_mxfp4_scheme.py`


| class INCMxfp4Scheme(INCScheme):
"""MXFP4 (W4A4) scheme for AutoRound checkpoints.
Dispatches to :class:`INCMxfp4LinearMethod` for linear layers and
:class:`INCMxfp4MoEMethod` for fused MoE layers; see those classes for the
per-module weight layout and kernel-selection details.
"""
@staticmethod
def can_handle(layer_config: "INCLayerConfig") -> bool:
return layer_config.is_mxfp4
def get_linear_method(
self,
config: "INCConfig",
layer: "torch.nn.Module",
prefix: str,
layer_config: "INCLayerConfig",
):
del config, layer, prefix
from .inc_mxfp4_linear import INCMxfp4LinearMethod
return INCLinearMethod(INCMxfp4LinearMethod(layer_config))
def get_moe_method(
self,
config: "INCConfig",
layer: "torch.nn.Module",
prefix: str,
layer_config: "INCLayerConfig",
):
del config, prefix, layer_config
from .inc_mxfp4_moe import INCMxfp4MoEMethod
return INCMxfp4MoEMethod(layer.moe_config)
|
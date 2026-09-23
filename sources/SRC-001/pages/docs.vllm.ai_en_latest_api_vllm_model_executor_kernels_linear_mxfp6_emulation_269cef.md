source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/mxfp6/emulation/
lastmod: 2026-09-23

class EmulationMxfp6LinearKernel(MxFp6LinearKernel):
"""Software emulation fallback for OCP MXFP4/MXFP6 (dequant + F.linear)."""
def __init__(self, config: MxFp6LinearLayerConfig) -> None:
super().__init__(config)
self.dequant_func = _WEIGHT_DEQUANT_FUNCS[config.weight_quant_key]
if config.activation_quant_key is None:
# no input Q/DQ for weight-only
self.quant_dequant_func: Callable[[torch.Tensor], torch.Tensor] = (
lambda x: x
)
else:
self.quant_dequant_func = _ACTIVATION_QUANT_DEQUANT_FUNCS[
config.activation_quant_key
]
@classmethod
def is_supported(
cls, compute_capability: int | None = None
) -> tuple[bool, str | None]:
return True, None
@classmethod
def can_implement(cls, config: MxFp6LinearLayerConfig) -> tuple[bool, str | None]:
if config.weight_quant_key not in (
kMxfp6E2M3Static,
kMxfp6E3M2Static,
):
return False, "only supports MXFP6 weights"
if config.activation_quant_key not in (
None,
kMxfp4Dynamic,
kMxfp6E3M2Dynamic,
kMxfp6E2M3Dynamic,
):
return False, "only supports MXFP4 or MXFP6 or unquantized activations"
return True, None
def process_weights_after_loading(self, layer: torch.nn.Module) -> None:
layer.weight_scale = Parameter(layer.weight_scale.data, requires_grad=False)
def apply_weights(
self,
layer: torch.nn.Module,
x: torch.Tensor,
bias: torch.Tensor | None = None,
) -> torch.Tensor:
dq_w = self.dequant_func(layer.weight, layer.weight_scale, x.dtype)
qdq_x = self.quant_dequant_func(x)
return F.linear(qdq_x, dq_w, bias)
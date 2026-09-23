source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/mxfp4/aiter/
lastmod: 2026-09-23

class AiterMxfp4LinearKernel(MxFp4LinearKernel):
"""AITER-based native MXFP4 GEMM kernel for ROCm."""
def __init__(self, config: MxFp4LinearLayerConfig) -> None:
super().__init__(config)
self.use_asm_gemm = rocm_aiter_ops.is_asm_fp4_gemm_dynamic_quant_enabled()
self.out_dtype = torch.get_default_dtype()
@classmethod
def is_supported(
cls, compute_capability: int | None = None
) -> tuple[bool, str | None]:
if not current_platform.supports_mx():
return False, "current platform does not support native MXFP4 computation"
from vllm._aiter_ops import is_aiter_found_and_supported
from vllm.model_executor.kernels.linear import _get_linear_backend
linear_backend = _get_linear_backend(quantization="mxfp4")
if (
current_platform.is_rocm()
and current_platform.supports_mx()
and "AiterMxfp4LinearKernel" not in envs.VLLM_DISABLED_KERNELS
and linear_backend == "auto"
and not is_aiter_found_and_supported()
):
logger.warning_once(
"This platform supports native MXFP4 W4A4 MOE "
"computation via AITER MOE backend, but AITER is not "
"found or not supported. Consider installing AITER: "
"https://github.com/ROCm/aiter."
)
if is_aiter_found_and_supported():
return True, None
return False, "AITER not found or not supported on the current platform"
@classmethod
def can_implement(cls, config: MxFp4LinearLayerConfig) -> tuple[bool, str | None]:
if config.activation_quant_key != kMxfp4Dynamic:
return False, "only supports MXFP4 dynamic activation"
return True, None
def process_weights_after_loading(self, layer: torch.nn.Module) -> None:
if self.use_asm_gemm and not _asm_fp4_scale_swizzle_supported(
layer.weight_scale.data
):
logger.warning_once(
"AITER ASM FP4 GEMM requires weight_scale dims divisible by "
"(%d, %d), but this layer has weight_scale shape %s. Falling "
"back to the AITER Triton FP4 GEMM for this layer.",
_ASM_FP4_SCALE_ROW_MULTIPLE,
_ASM_FP4_SCALE_COL_MULTIPLE,
tuple(layer.weight_scale.data.shape),
)
self.use_asm_gemm = False
if self.use_asm_gemm:
from aiter.ops.shuffle import shuffle_weight
weight_scale = layer.weight_scale.data
sm, sn = weight_scale.shape
weight_scale = weight_scale.view(sm // 32, 2, 16, sn // 8, 2, 4, 1)
weight_scale = weight_scale.permute(0, 3, 5, 2, 4, 1, 6).contiguous()
weight_scale = weight_scale.view(sm, sn)
layer.weight_scale = Parameter(weight_scale, requires_grad=False)
layer.weight = Parameter(
shuffle_weight(layer.weight.data, layout=(16, 16)),
requires_grad=False,
)
else:
layer.weight_scale = Parameter(
layer.weight_scale.data.T.contiguous(), requires_grad=False
)
def apply_weights(
self,
layer: torch.nn.Module,
x: torch.Tensor,
bias: torch.Tensor | None = None,
) -> torch.Tensor:
y = torch.ops.vllm.gemm_with_dynamic_quant(
x,
layer.weight,
layer.weight_scale,
self.use_asm_gemm,
self.out_dtype,
)
if bias is not None:
y = y + bias
return y
source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/mxfp4/b12x/
lastmod: 2026-09-23

class B12xMxFp4LinearKernel(MxFp4LinearKernel):
"""MXFP4 linear through the native B12X SM120 dense GEMM."""
@classmethod
def is_supported(
cls, compute_capability: int | None = None
) -> tuple[bool, str | None]:
del compute_capability
if not current_platform.is_cuda():
return False, "B12X MXFP4 kernels are only available on CUDA"
if not current_platform.is_device_capability_family(120):
return False, "B12X MXFP4 kernels require a Blackwell 12x device"
blockscaled = _import_b12x_blockscaled()
if blockscaled is None or _import_b12x_intrinsics() is None:
return False, "Install the B12X backend with `pip install vllm[b12x]`"
if not blockscaled.is_supported():
return False, "b12x native MXFP4 GEMM is not supported"
return True, None
@classmethod
def can_implement(cls, config: MxFp4LinearLayerConfig) -> tuple[bool, str | None]:
if config.activation_quant_key != kMxfp4Dynamic:
return False, "B12X MXFP4 GEMM requires dynamic MXFP4 activations"
return True, None
def process_weights_after_loading(self, layer: torch.nn.Module) -> None:
intrinsics = _import_b12x_intrinsics()
assert intrinsics is not None
replace_parameter(
layer,
"weight_scale",
intrinsics.swizzle_block_scale(layer.weight_scale.data),
)
layer.b12x_warmup_provider = self
def get_b12x_warmup_unit(
self,
layer: torch.nn.Module,
token_counts: tuple[int, ...],
output_dtype: torch.dtype,
) -> B12xWarmupUnit:
weight = layer.weight
weight_scale = layer.weight_scale
n, packed_k = map(int, weight.shape)
k = packed_k * 2
def compile() -> None:
for tokens in token_counts:
source = torch.zeros(
(tokens, k), dtype=output_dtype, device=weight.device
)
_apply_b12x_mxfp4_linear(source, weight, weight_scale, None)
return B12xWarmupUnit(
name="MXFP4",
key=(
type(self),
weight.device,
n,
k,
weight.dtype,
weight_scale.dtype,
output_dtype,
),
compile=compile,
)
def apply_weights(
self,
layer: torch.nn.Module,
x: torch.Tensor,
bias: torch.Tensor | None = None,
) -> torch.Tensor:
return _apply_b12x_mxfp4_linear(
x,
layer.weight,
layer.weight_scale,
bias,
)
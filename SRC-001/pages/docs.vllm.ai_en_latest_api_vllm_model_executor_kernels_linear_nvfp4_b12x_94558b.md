source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/nvfp4/b12x/
lastmod: 2026-09-23

class B12xNvFp4LinearKernel(NvFp4LinearKernel):
"""ModelOpt NVFP4 linear through the native B12X SM120 dense GEMM."""
@classmethod
def is_supported(
cls, compute_capability: int | None = None
) -> tuple[bool, str | None]:
del compute_capability
if not current_platform.is_cuda():
return False, "B12X NVFP4 kernels are only available on CUDA"
if not current_platform.is_device_capability_family(120):
return False, "B12X NVFP4 kernels require a Blackwell 12x device"
blockscaled = _import_b12x_blockscaled()
if blockscaled is None or _import_b12x_intrinsics() is None:
return False, "Install the B12X backend with `pip install vllm[b12x]`"
if not blockscaled.is_supported():
return False, "b12x native NVFP4 GEMM is not supported"
return True, None
@classmethod
def can_implement(cls, config: NvFp4LinearLayerConfig) -> tuple[bool, str | None]:
del config
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
_apply_b12x_nvfp4_linear(
source,
weight,
weight_scale,
layer.input_global_scale_inv,
layer.alpha,
None,
)
return B12xWarmupUnit(
name="NVFP4",
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
return _apply_b12x_nvfp4_linear(
x,
layer.weight,
layer.weight_scale,
layer.input_global_scale_inv,
layer.alpha,
bias,
)
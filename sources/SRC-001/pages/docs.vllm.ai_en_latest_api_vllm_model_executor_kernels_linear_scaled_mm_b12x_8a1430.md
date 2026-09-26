source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/scaled_mm/b12x/
lastmod: 2026-09-24

class B12xTensorFP8ScaledMMLinearKernel(FP8ScaledMMLinearKernel):
"""Static per-tensor FP8 linear through the B12X SM12x dense GEMM."""
@classmethod
def is_supported(
cls,
compute_capability: int | None = None,
) -> tuple[bool, str | None]:
del compute_capability
if not current_platform.is_cuda():
return False, "b12x tensor FP8 kernels are only available on CUDA"
if not current_platform.is_device_capability_family(120):
return False, "b12x tensor FP8 kernels require a Blackwell 12x device"
tensor_fp8 = _import_b12x_tensor_fp8()
if tensor_fp8 is None:
return False, "Install the B12X backend with `pip install vllm[b12x]`"
if not tensor_fp8.is_supported():
return False, "b12x.gemm.tensor_fp8_linear is not supported"
return True, None
@classmethod
def can_implement(
cls,
config: FP8ScaledMMLinearLayerConfig,
) -> tuple[bool, str | None]:
activation_scale = config.activation_quant_key.scale
weight_scale = config.weight_quant_key.scale
if (
not activation_scale.static
or not activation_scale.group_shape.is_per_tensor()
):
return False, "requires static per-tensor activation scales"
if not weight_scale.static or not weight_scale.group_shape.is_per_tensor():
return False, "requires static per-tensor weight scales"
if config.input_dtype not in (torch.bfloat16, torch.float16):
return False, "supports only bf16/fp16 input dtype"
if config.out_dtype not in (torch.bfloat16, torch.float16):
return False, "supports only bf16/fp16 output dtype"
out_features, in_features = config.weight_shape
if out_features <= 0 or in_features <= 0 or in_features % 32 != 0:
return False, "weight dimensions must be positive with K divisible by 32"
return True, None
def process_weights_after_loading(self, layer: torch.nn.Module) -> None:
weight, weight_scale, input_scale, _ = self._get_layer_params(layer)
assert weight.dtype == torch.float8_e4m3fn
assert input_scale is not None
assert weight_scale.numel() == input_scale.numel() == 1
out_features, in_features = map(int, self.config.weight_shape)
assert tuple(weight.shape) == (in_features, out_features)
tensor_fp8 = _import_b12x_tensor_fp8()
assert tensor_fp8 is not None
output_scale = (
input_scale.detach().to(torch.float32).reshape(1)
* weight_scale.detach().to(torch.float32).reshape(1)
).contiguous()
packed_weight = tensor_fp8.pack_weight(
weight.detach().T.contiguous(),
output_scale,
)
layer.b12x_tensor_fp8_packed_weight = reuse_packed_weight_storage(
getattr(layer, "b12x_tensor_fp8_packed_weight", None),
packed_weight,
)
weight_name, weight_scale_name, _, _ = self.layer_param_names
replace_parameter(layer, weight_name, weight.new_empty((0,)))
replace_parameter(layer, weight_scale_name, weight_scale.new_empty((0,)))
layer.b12x_warmup_provider = self
def get_b12x_warmup_unit(
self,
layer: torch.nn.Module,
token_counts: tuple[int, ...],
output_dtype: torch.dtype,
) -> B12xWarmupUnit:
packed_weight = layer.b12x_tensor_fp8_packed_weight
device = torch.device(packed_weight.values.device)
def compile() -> None:
tensor_fp8 = _import_b12x_tensor_fp8()
assert tensor_fp8 is not None
tensor_fp8.prewarm(
packed_weight,
token_counts,
out_dtype=output_dtype,
stream=current_stream().cuda_stream,
)
return B12xWarmupUnit(
name="tensor FP8",
key=(
type(self),
device,
int(packed_weight.in_features),
int(packed_weight.padded_in_features),
int(packed_weight.out_features),
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
assert isinstance(x, torch.Tensor)
_, _, input_scale, input_scale_ub = self._get_layer_params(layer)
input_2d = x.reshape(-1, x.shape[-1])
x_q, _ = self.quant_fp8(input_2d, input_scale, input_scale_ub)
out_dtype = self.config.out_dtype
output = _apply_b12x_tensor_fp8_packed_linear(
layer,
x_q,
bias,
out_dtype,
)
return output.view(*x.shape[:-1], output.shape[-1])
def apply_scaled_mm(
self,
*,
A: torch.Tensor,
B: torch.Tensor,
out_dtype: torch.dtype,
As: torch.Tensor,
Bs: torch.Tensor,
bias: torch.Tensor | None,
output_shape: list,
) -> torch.Tensor:
del A, B, out_dtype, As, Bs, bias, output_shape
raise NotImplementedError("b12x tensor FP8 linear overrides apply_weights")
source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/scaled_mm/humming/
lastmod: 2026-09-24

class HummingFP8ScaledMMLinearKernel(FP8ScaledMMLinearKernel):
"""Humming GEMM Kernel for FP8."""
@classmethod
def is_supported(
cls, compute_capability: int | None = None
) -> tuple[bool, str | None]:
if not current_platform.is_cuda():
return False, "Humming only supported on CUDA"
if not has_humming():
return False, "Humming is not installed"
if not current_platform.has_device_capability(75):
return False, "Humming only supported on SM75+"
return True, None
@classmethod
def can_implement(
cls, config: FP8ScaledMMLinearLayerConfig
) -> tuple[bool, str | None]:
return True, None
def process_weights_after_loading(self, layer: torch.nn.Module) -> None:
from vllm.utils.humming import dtypes
name_map = {"weight": "weight", "weight_scale": "weight_scale"}
scale_torch_dtype = self.config.weight_quant_key.scale.dtype
scale_dtype = dtypes.DataType.from_torch_dtype(scale_torch_dtype)
quant_config = {
"quant_method": "humming",
"dtype": "float8e4m3",
"scale_dtype": scale_dtype,
}
assert self.config.weight_quant_key.scale2 is None
scale_group_shape = self.config.weight_quant_key.scale.group_shape
if scale_group_shape.is_per_tensor():
quant_config["weight_scale_type"] = "tensor"
elif scale_group_shape.is_per_channel():
quant_config["weight_scale_type"] = "channel"
elif scale_group_shape.is_per_group():
quant_config["weight_scale_type"] = "group"
quant_config["group_size"] = scale_group_shape.col
else:
assert scale_group_shape.row > 0 and scale_group_shape.col > 0
quant_config["weight_scale_type"] = "block"
quant_config["weight_scale_group_size_n"] = scale_group_shape.row
quant_config["weight_scale_group_size"] = scale_group_shape.col
if hasattr(layer, "weight_scale_inv"):
name_map["weight_scale"] = "weight_scale_inv"
convert_linear_layer_to_humming_standard(layer=layer, name_map=name_map)
self.layer_config = prepare_humming_linear_layer_config(layer, quant_config)
self.compute_config = get_humming_linear_compute_config()
self.locks = torch.zeros(1024, dtype=torch.int32, device=layer.weight.device)
def apply_weights(
self,
layer: torch.nn.Module,
x: torch.Tensor,
bias: torch.Tensor | None = None,
) -> torch.Tensor:
return apply_humming_linear(
layer,
x,
skip_bias_add=bias is None,
layer_config=self.layer_config,
compute_config=self.compute_config,
locks=self.locks,
)
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
raise NotImplementedError(
"HummingFP8ScaledMMLinearKernel uses apply_weights directly"
)
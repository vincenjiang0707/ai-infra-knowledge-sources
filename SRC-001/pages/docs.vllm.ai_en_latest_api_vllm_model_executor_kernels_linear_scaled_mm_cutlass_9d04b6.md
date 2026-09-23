source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/scaled_mm/cutlass/
lastmod: 2026-09-23

class CutlassFP8ScaledMMLinearKernel(FP8ScaledMMLinearKernel):
def __init__(
self, c: FP8ScaledMMLinearLayerConfig, layer_param_names: Sequence[str]
) -> None:
self.logical_output_size: int | None = None
super().__init__(c, layer_param_names)
@classmethod
def is_supported(
cls, compute_capability: int | None = None
) -> tuple[bool, str | None]:
if not cutlass_fp8_supported():
return False, "CUTLASS FP8 kernels not available"
return True, None
@classmethod
def can_implement(cls, c: FP8ScaledMMLinearLayerConfig) -> tuple[bool, str | None]:
return True, None
def input_quant_key(self) -> QuantKey | None:
"""Only static per-tensor activation quantization is supported for external
quantization."""
if self.config.activation_quant_key == kFp8StaticTensorSym:
return kFp8StaticTensorSym
return None
@staticmethod
def _pad_to_alignment(
x: torch.Tensor, dim: int, alignment: int, value: float = 0.0
) -> torch.Tensor:
"""Pad tensor ``x`` along ``dim`` to the next multiple of
``alignment``."""
remainder = x.shape[dim] % alignment
if remainder == 0:
return x
pad_size = alignment - remainder
pad_spec = [0] * (2 * x.dim())
pad_spec[-(2 * dim + 1)] = pad_size
return torch.nn.functional.pad(x, pad_spec, value=value)
@staticmethod
def padded_weight_loader(param: torch.Tensor, loaded_weight: torch.Tensor) -> None:
if loaded_weight.shape != param.shape:
slices = tuple(slice(0, s) for s in loaded_weight.shape)
param.data[slices].copy_(loaded_weight)
else:
param.data.copy_(loaded_weight.view(param.shape))
def process_weights_after_loading(self, layer: torch.nn.Module) -> None:
weight_name, weight_scale_name, _, _ = self.layer_param_names
weight = getattr(layer, weight_name)
# keep the logical output width so runtime can slice away static padding.
self.logical_output_size = weight.shape[1]
pad_k = (16 - weight.shape[0] % 16) % 16
pad_n = (16 - weight.shape[1] % 16) % 16
if pad_k == 0 and pad_n == 0:
return
# B is column-major [K, N]
padded_weight = torch.nn.functional.pad(
weight.t().contiguous(),
(0, pad_k, 0, pad_n),
).t()
replace_parameter(layer, weight_name, padded_weight.data)
set_weight_attrs(
getattr(layer, weight_name),
{
"weight_loader": self.padded_weight_loader,
},
)
weight_scale = getattr(layer, weight_scale_name, None)
if weight_scale is not None and pad_n > 0 and weight_scale.numel() > 1:
flat_scale = weight_scale.reshape(-1)
padded_scale = self._pad_to_alignment(
flat_scale, dim=0, alignment=16, value=1.0
).view(-1, *weight_scale.shape[1:])
replace_parameter(layer, weight_scale_name, padded_scale.data)
set_weight_attrs(
getattr(layer, weight_name),
{
"weight_loader": self.padded_weight_loader,
},
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
padded_k, padded_n = B.shape
output_size = self.logical_output_size
assert output_size is not None
pad_k = padded_k - A.shape[1]
pad_n = padded_n - output_size
if pad_k > 0:
A = self._pad_to_alignment(A, dim=1, alignment=16)
if pad_n > 0 and bias is not None:
bias = self._pad_to_alignment(bias, dim=0, alignment=16)
output = ops.cutlass_scaled_mm(
A, B, out_dtype=out_dtype, scale_a=As, scale_b=Bs, bias=bias
)
if pad_n > 0:
output = output[..., :output_size].contiguous()
return output.view(*output_shape[:-1], output_size)
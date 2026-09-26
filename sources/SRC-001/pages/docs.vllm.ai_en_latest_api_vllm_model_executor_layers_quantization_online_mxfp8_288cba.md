source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/online/mxfp8/
lastmod: 2026-09-24

class Mxfp8OnlineMoEMethod(OnlineMoEMethodBase):
"""MoE method for online MXFP8 (block) quantization."""
fp8_backend: "Fp8MoeBackend"
experts_cls: "type[mk.FusedMoEExperts] | None"
def __init__(self, *, moe: FusedMoEConfig):
super().__init__(moe)
self.weight_block_size: list[int] = [1, MXFP8_BLOCK_SIZE]
self.weight_scale_name = "weight_scale"
self.fp8_backend, self.experts_cls = select_mxfp8_moe_backend(config=self.moe)
def create_weights(
self,
layer: Module,
num_experts: int,
hidden_size: int,
intermediate_size_per_partition: int,
params_dtype: torch.dtype,
**extra_weight_attrs,
):
if (
hidden_size % MXFP8_BLOCK_SIZE != 0
or intermediate_size_per_partition % MXFP8_BLOCK_SIZE != 0
):
raise ValueError(
"Online MXFP8 MoE requires hidden/intermediate sizes divisible "
f"by {MXFP8_BLOCK_SIZE}."
)
super().create_weights(
layer=layer,
num_experts=num_experts,
hidden_size=hidden_size,
intermediate_size_per_partition=intermediate_size_per_partition,
params_dtype=params_dtype,
**extra_weight_attrs,
)
layer.weight_block_size = [1, MXFP8_BLOCK_SIZE]
def _quantize_mxfp8_moe_weight(
self, weight: torch.Tensor
) -> tuple[torch.Tensor, torch.Tensor]:
"""Batch quantization: bf16/fp16 weights -> MXFP8 (fp8 + uint8 scales)."""
E = weight.size(0)
first_q, first_s = mxfp8_e4m3_quantize(weight[0], is_sf_swizzled_layout=False)
# Pre-allocate the output tensors rather than stacking.
# This is important for consistent memory layout.
w_quant = torch.empty(
(E, *first_q.shape), dtype=first_q.dtype, device=weight.device
)
w_scales = torch.empty(
(E, *first_s.shape), dtype=first_s.dtype, device=weight.device
)
w_quant[0] = first_q
w_scales[0] = first_s
for i in range(1, E):
w_quant[i], w_scales[i] = mxfp8_e4m3_quantize(
weight[i], is_sf_swizzled_layout=False
)
return w_quant, w_scales
def _setup_kernel(
self,
layer: "RoutedExperts",
w13: torch.Tensor,
w2: torch.Tensor,
w13_scale: torch.Tensor,
w2_scale: torch.Tensor,
w13_input_scale: torch.Tensor | None,
w2_input_scale: torch.Tensor | None,
) -> None:
from vllm.model_executor.layers.fused_moe.oracle.fp8 import (
convert_to_fp8_moe_kernel_format,
make_fp8_moe_kernel,
)
# Shuffle weights to runtime format.
w13, w2, w13_scale, w2_scale = convert_to_fp8_moe_kernel_format(
fp8_backend=self.fp8_backend,
layer=layer,
w13=w13,
w2=w2,
w13_scale=w13_scale,
w2_scale=w2_scale,
w13_input_scale=w13_input_scale,
w2_input_scale=w2_input_scale,
)
replace_parameter(layer, "w13_weight", w13)
replace_parameter(layer, "w2_weight", w2)
replace_parameter(layer, f"w13_{self.weight_scale_name}", w13_scale)
replace_parameter(layer, f"w2_{self.weight_scale_name}", w2_scale)
self.moe_quant_config = self.get_fused_moe_quant_config(layer)
if self.moe_quant_config:
assert self.experts_cls is not None
self.moe_kernel = make_fp8_moe_kernel(
moe_quant_config=self.moe_quant_config,
moe_config=self.moe,
fp8_backend=self.fp8_backend,
experts_cls=self.experts_cls,
routing_tables=layer._expert_routing_tables(),
)
def get_fused_moe_quant_config(
self, layer: torch.nn.Module
) -> "FusedMoEQuantConfig":
from vllm.model_executor.layers.fused_moe.oracle.fp8 import (
make_fp8_moe_quant_config,
)
w1_scale = getattr(layer, f"w13_{self.weight_scale_name}")
w2_scale = getattr(layer, f"w2_{self.weight_scale_name}")
a1_scale = layer.w13_input_scale
a2_scale = layer.w2_input_scale
return make_fp8_moe_quant_config(
fp8_backend=self.fp8_backend,
w1_scale=w1_scale,
w2_scale=w2_scale,
a1_scale=a1_scale,
a2_scale=a2_scale,
w1_bias=getattr(layer, "w13_bias", None),
w2_bias=getattr(layer, "w2_bias", None),
block_shape=self.weight_block_size,
swiglu_limit=getattr(layer, "swiglu_limit", None),
gemm1_alpha=getattr(layer, "swiglu_alpha", None),
gemm1_beta=getattr(layer, "swiglu_beta", None),
layer=layer,
)
def process_weights_after_loading(self, layer: Module) -> None:
if getattr(layer, "_already_called_process_weights_after_loading", False):
return
fp8_dtype = current_platform.fp8_dtype()
w13 = torch.empty_like(layer.w13_weight, dtype=fp8_dtype)
w2 = torch.empty_like(layer.w2_weight, dtype=fp8_dtype)
layer.w13_input_scale = None
layer.w2_input_scale = None
w13, w13_scale = self._quantize_mxfp8_moe_weight(layer.w13_weight)
w2, w2_scale = self._quantize_mxfp8_moe_weight(layer.w2_weight)
self._setup_kernel(
layer,
w13,
w2,
w13_scale,
w2_scale,
layer.w13_input_scale,
layer.w2_input_scale,
)
layer._already_called_process_weights_after_loading = True
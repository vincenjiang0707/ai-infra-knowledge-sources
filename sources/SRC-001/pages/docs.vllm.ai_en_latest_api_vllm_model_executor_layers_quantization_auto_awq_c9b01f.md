source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/auto_awq/
lastmod: 2026-09-24

class AutoAWQMoEMethod(FusedMoEMethodBase):
def __init__(
self,
quant_config: AutoAWQConfig,
moe: FusedMoEConfig,
):
super().__init__(moe)
self.quant_config = quant_config
if self.quant_config.weight_bits != 4:
raise ValueError("AutoAWQMoEMethod only supports 4bit now.")
self.quant_type = scalar_types.uint4
self.input_dtype = None
self.use_marlin = True
self.wna16_moe_backend, self.experts_cls = select_wna16_moe_backend(
moe,
kInt4Static,
quant_config=self.quant_config,
may_have_zp=self.quant_config.zero_point,
may_have_bias=True,
allow_tile_padding=True,
)
def create_weights(
self,
layer: RoutedExperts,
num_experts: int,
hidden_size: int,
intermediate_size_per_partition: int,
params_dtype: torch.dtype,
**extra_weight_attrs,
):
layer.input_dtype = self.input_dtype
extra_weight_attrs.update(
{
"is_transposed": True,
"quant_method": FusedMoeWeightScaleSupported.GROUP.value,
}
)
w13_qweight = Parameter(
torch.empty(
num_experts,
hidden_size,
self.moe.w13_num_shards
* intermediate_size_per_partition
// self.quant_config.pack_factor,
dtype=torch.int32,
),
requires_grad=False,
)
layer.register_parameter("w13_qweight", w13_qweight)
set_weight_attrs(w13_qweight, extra_weight_attrs)
w2_qweight = Parameter(
torch.empty(
num_experts,
intermediate_size_per_partition,
hidden_size // self.quant_config.pack_factor,
dtype=torch.int32,
),
requires_grad=False,
)
layer.register_parameter("w2_qweight", w2_qweight)
set_weight_attrs(w2_qweight, extra_weight_attrs)
num_groups_w13 = hidden_size // self.quant_config.group_size
num_groups_w2 = intermediate_size_per_partition // self.quant_config.group_size
layer.num_groups_w13 = num_groups_w13
layer.num_groups_w2 = num_groups_w2
# WEIGHT_SCALES
# Allocate 2 scales for w1 and w3 respectively.
w13_scales = Parameter(
torch.empty(
num_experts,
num_groups_w13,
intermediate_size_per_partition * self.moe.w13_num_shards,
dtype=params_dtype,
),
requires_grad=False,
)
layer.register_parameter("w13_scales", w13_scales)
set_weight_attrs(w13_scales, extra_weight_attrs)
w2_scales = Parameter(
torch.empty(num_experts, num_groups_w2, hidden_size, dtype=params_dtype),
requires_grad=False,
)
layer.register_parameter("w2_scales", w2_scales)
set_weight_attrs(w2_scales, extra_weight_attrs)
# WEIGHT_ZERO_POINT
# Allocate 2 zero points for w1 and w3 respectively.
w13_qzeros = Parameter(
torch.empty(
num_experts,
num_groups_w13,
self.moe.w13_num_shards
* intermediate_size_per_partition
// self.quant_config.pack_factor,
dtype=torch.int32,
),
requires_grad=False,
)
layer.register_parameter("w13_qzeros", w13_qzeros)
set_weight_attrs(w13_qzeros, extra_weight_attrs)
w2_qzeros = Parameter(
torch.empty(
num_experts,
num_groups_w2,
hidden_size // self.quant_config.pack_factor,
dtype=torch.int32,
),
requires_grad=False,
)
layer.register_parameter("w2_qzeros", w2_qzeros)
set_weight_attrs(w2_qzeros, extra_weight_attrs)
def process_weights_after_loading(self, layer: RoutedExperts) -> None:
converted = convert_to_wna16_moe_kernel_format(
backend=self.wna16_moe_backend,
layer=layer,
quant_config=self.quant_config,
input_dtype=self.input_dtype,
w13=layer.w13_qweight,
w2=layer.w2_qweight,
w13_scale=layer.w13_scales,
w2_scale=layer.w2_scales,
w13_qzeros=layer.w13_qzeros,
w2_qzeros=layer.w2_qzeros,
w13_bias=getattr(layer, "w13_bias", None),
w2_bias=getattr(layer, "w2_bias", None),
)
if converted is None:
# Backend rewrote the layer's params in place (e.g. Humming).
self._setup_kernel(layer)
return
(
w13,
w2,
w13_scale,
w2_scale,
w13_qzeros,
w2_qzeros,
w13_input_global_scale,
w2_input_global_scale,
w13_bias,
w2_bias,
) = converted
replace_parameter(layer, "w13_qweight", w13)
replace_parameter(layer, "w2_qweight", w2)
# The modular kernel expects w13_weight and w2_weight,
# but AWQ uses w13_qweight and w2_qweight
# Alias for modular kernel
layer.w13_weight = layer.w13_qweight
# Alias for modular kernel
layer.w2_weight = layer.w2_qweight
replace_parameter(layer, "w13_scales", w13_scale)
replace_parameter(layer, "w2_scales", w2_scale)
_replace_or_register_parameter(layer, "w13_qzeros", w13_qzeros)
_replace_or_register_parameter(layer, "w2_qzeros", w2_qzeros)
_replace_or_register_parameter(
layer, "w13_input_global_scale", w13_input_global_scale
)
_replace_or_register_parameter(
layer, "w2_input_global_scale", w2_input_global_scale
)
_replace_or_register_parameter(layer, "w13_bias", w13_bias)
_replace_or_register_parameter(layer, "w2_bias", w2_bias)
self._setup_kernel(layer)
def _setup_kernel(self, layer: RoutedExperts) -> None:
"""Build the FusedMoEKernel for this layer."""
self.moe_quant_config = self.get_fused_moe_quant_config(layer)
self.moe_kernel = make_wna16_moe_kernel(
moe_quant_config=self.moe_quant_config,
moe_config=self.moe,
experts_cls=self.experts_cls,
backend=self.wna16_moe_backend,
routing_tables=layer._expert_routing_tables(),
)
def get_fused_moe_quant_config(self, layer: RoutedExperts) -> FusedMoEQuantConfig:
if self.wna16_moe_backend == WNA16MoEBackend.HUMMING:
from vllm.model_executor.layers.quantization.utils.humming import (
get_humming_moe_quant_config,
)
return get_humming_moe_quant_config(
layer,
gemm1_alpha=getattr(layer, "swiglu_alpha", None),
gemm1_beta=getattr(layer, "swiglu_beta", None),
gemm1_clamp_limit=getattr(layer, "swiglu_limit", None),
)
return make_wna16_moe_quant_config(
w1_scale=layer.w13_scales,
w2_scale=layer.w2_scales,
group_size=self.quant_config.group_size,
num_bits=self.quant_config.weight_bits,
w1_zp=getattr(layer, "w13_qzeros", None)
if self.quant_config.zero_point
else None,
w2_zp=getattr(layer, "w2_qzeros", None)
if self.quant_config.zero_point
else None,
w1_bias=getattr(layer, "w13_bias", None),
w2_bias=getattr(layer, "w2_bias", None),
a1_gscale=getattr(layer, "w13_input_global_scale", None),
a2_gscale=getattr(layer, "w2_input_global_scale", None),
gemm1_clamp_limit=getattr(layer, "swiglu_limit", None),
gemm1_alpha=getattr(layer, "swiglu_alpha", None),
gemm1_beta=getattr(layer, "swiglu_beta", None),
)
def apply(
self,
layer: RoutedExperts,
x: torch.Tensor,
topk_weights: torch.Tensor,
topk_ids: torch.Tensor,
shared_experts: SharedExperts | None,
shared_experts_input: torch.Tensor | None,
) -> torch.Tensor:
assert not self.is_monolithic
assert self.moe_kernel is not None
return self.moe_kernel.apply(
hidden_states=x,
w1=layer.w13_weight,
w2=layer.w2_weight,
topk_weights=topk_weights,
topk_ids=topk_ids,
activation=layer.activation,
global_num_experts=layer.global_num_experts,
apply_router_weight_on_input=layer.apply_router_weight_on_input,
expert_map=layer.expert_map,
shared_experts=shared_experts,
shared_experts_input=shared_experts_input,
)
def apply_monolithic(
self,
layer: RoutedExperts,
x: torch.Tensor,
router_logits: torch.Tensor,
input_ids: torch.Tensor | None = None,
) -> torch.Tensor:
assert self.is_monolithic
assert self.moe_kernel is not None
return self.moe_kernel.apply_monolithic(
hidden_states=x,
w1=layer.w13_weight,
w2=layer.w2_weight,
router_logits=router_logits,
activation=layer.activation,
global_num_experts=layer.global_num_experts,
expert_map=layer.expert_map,
apply_router_weight_on_input=layer.apply_router_weight_on_input,
num_expert_group=layer.num_expert_group,
topk_group=layer.topk_group,
e_score_correction_bias=layer.e_score_correction_bias,
routed_scaling_factor=layer.routed_scaling_factor,
)
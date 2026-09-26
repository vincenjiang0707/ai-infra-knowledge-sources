source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/auto_gptq/
lastmod: 2026-09-24

class AutoGPTQMoEMethod(FusedMoEMethodBase):
"""MoE Marlin method with quantization."""
def __init__(
self,
quant_config: AutoGPTQConfig,
moe: FusedMoEConfig,
) -> None:
super().__init__(moe)
self.quant_config = quant_config
if self.quant_config.quant_type.size_bits == 4:
quant_type = scalar_types.uint4b8
scale = kInt4StaticGroupScale
elif self.quant_config.quant_type.size_bits == 8:
quant_type = scalar_types.uint8b128
scale = kInt8StaticGroupScale
else:
raise ValueError("AutoGPTQMoEMethod only supports int4 and int8 now.")
self.input_dtype = None
self.use_marlin = True
weight_key = QuantKey(quant_type, scale)
self.wna16_moe_backend, self.experts_cls = select_wna16_moe_backend(
moe,
weight_key,
quant_config=self.quant_config,
may_have_zp=not self.quant_config.is_sym,
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
is_a_8bit = self.input_dtype is not None and self.input_dtype.itemsize == 1
if is_a_8bit:
assert self.quant_config.quant_type.size_bits == 8, (
"W8A8-INT8 is not supported by marlin kernel."
)
if self.quant_config.group_size != -1:
scales_size13 = hidden_size // self.quant_config.group_size
w2_scales_size = intermediate_size_per_partition
scales_size2 = w2_scales_size // self.quant_config.group_size
strategy = FusedMoeWeightScaleSupported.GROUP.value
else:
scales_size13 = 1
scales_size2 = 1
strategy = FusedMoeWeightScaleSupported.CHANNEL.value
layer.num_groups_w13 = scales_size13
layer.num_groups_w2 = scales_size2
extra_weight_attrs.update({"quant_method": strategy, "is_transposed": True})
# Fused gate_up_proj (column parallel)
w13_qweight = torch.nn.Parameter(
torch.empty(
num_experts,
hidden_size // self.quant_config.pack_factor,
self.moe.w13_num_shards * intermediate_size_per_partition,
dtype=torch.int32,
),
requires_grad=False,
)
layer.register_parameter("w13_qweight", w13_qweight)
set_weight_attrs(w13_qweight, extra_weight_attrs)
# down_proj (row parallel)
w2_qweight = torch.nn.Parameter(
torch.empty(
num_experts,
intermediate_size_per_partition // self.quant_config.pack_factor,
hidden_size,
dtype=torch.int32,
),
requires_grad=False,
)
layer.register_parameter("w2_qweight", w2_qweight)
set_weight_attrs(w2_qweight, extra_weight_attrs)
# up_proj scales
w13_scales = torch.nn.Parameter(
torch.empty(
num_experts,
scales_size13,
self.moe.w13_num_shards * intermediate_size_per_partition,
dtype=params_dtype,
),
requires_grad=False,
)
layer.register_parameter("w13_scales", w13_scales)
set_weight_attrs(w13_scales, extra_weight_attrs)
# down_proj scales
w2_scales = torch.nn.Parameter(
torch.empty(num_experts, scales_size2, hidden_size, dtype=params_dtype),
requires_grad=False,
)
layer.register_parameter("w2_scales", w2_scales)
set_weight_attrs(w2_scales, extra_weight_attrs)
# up_proj zero points
w13_qzeros = torch.nn.Parameter(
torch.empty(
num_experts,
scales_size13,
self.moe.w13_num_shards
* intermediate_size_per_partition
// self.quant_config.pack_factor,
dtype=torch.int32,
),
requires_grad=False,
)
layer.register_parameter("w13_qzeros", w13_qzeros)
set_weight_attrs(w13_qzeros, extra_weight_attrs)
# down_proj zero points
w2_qzeros = torch.nn.Parameter(
torch.empty(
num_experts,
scales_size2,
hidden_size // self.quant_config.pack_factor,
dtype=torch.int32,
),
requires_grad=False,
)
layer.register_parameter("w2_qzeros", w2_qzeros)
set_weight_attrs(w2_qzeros, extra_weight_attrs)
# Some GPTQ checkpoints contain expert biases even when the model
# architecture does not declare them. Zero initialization keeps
# checkpoints without biases equivalent to the bias-free path.
w13_bias = torch.nn.Parameter(
torch.zeros(
num_experts,
self.moe.w13_num_shards * intermediate_size_per_partition,
dtype=params_dtype,
),
requires_grad=False,
)
layer.register_parameter("w13_bias", w13_bias)
set_weight_attrs(w13_bias, extra_weight_attrs)
w2_bias = torch.nn.Parameter(
torch.zeros(num_experts, hidden_size, dtype=params_dtype),
requires_grad=False,
)
layer.register_parameter("w2_bias", w2_bias)
set_weight_attrs(w2_bias, extra_weight_attrs)
def process_weights_after_loading(self, layer: RoutedExperts) -> None:
def replace_or_register(name: str, val: torch.Tensor | None):
if val is None:
return
if hasattr(layer, name):
replace_parameter(layer, name, val)
else:
layer.register_parameter(
name, torch.nn.Parameter(val, requires_grad=False)
)
is_a_8bit = self.input_dtype is not None and self.input_dtype.itemsize == 1
assert not is_a_8bit or self.quant_config.quant_type.size_bits == 8, (
"W8A8-INT8 is not supported by marlin kernel."
)
w13_bias = getattr(layer, "w13_bias", None)
if "w13_bias" not in layer._loaded_expert_biases:
layer.register_parameter("w13_bias", None)
w13_bias = None
w2_bias = getattr(layer, "w2_bias", None)
if "w2_bias" not in layer._loaded_expert_biases:
layer.register_parameter("w2_bias", None)
w2_bias = None
converted = convert_to_wna16_moe_kernel_format(
backend=self.wna16_moe_backend,
layer=layer,
quant_config=self.quant_config,
input_dtype=self.input_dtype,
w13=layer.w13_qweight,
w2=layer.w2_qweight,
w13_scale=layer.w13_scales,
w2_scale=layer.w2_scales,
w13_bias=w13_bias,
w2_bias=w2_bias,
w13_qzeros=getattr(layer, "w13_qzeros", None),
w2_qzeros=getattr(layer, "w2_qzeros", None),
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
replace_parameter(layer, "w13_scales", w13_scale)
replace_parameter(layer, "w2_scales", w2_scale)
replace_or_register("w13_input_global_scale", w13_input_global_scale)
replace_or_register("w2_input_global_scale", w2_input_global_scale)
replace_or_register("w13_bias", w13_bias)
replace_or_register("w2_bias", w2_bias)
replace_or_register("w13_qzeros", w13_qzeros)
replace_or_register("w2_qzeros", w2_qzeros)
# The modular kernel reads w13_weight/w2_weight; marlin keeps *_qweight.
layer.w13_weight = layer.w13_qweight
layer.w2_weight = layer.w2_qweight
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
from vllm.model_executor.layers.fused_moe.config import (
gptq_marlin_moe_quant_config,
)
# CPU fused_experts_cpu requires zero points even for symmetric quant
use_zp = (
not self.quant_config.is_sym
or self.wna16_moe_backend == WNA16MoEBackend.CPU
)
return gptq_marlin_moe_quant_config(
w1_scale=layer.w13_scales,
w2_scale=layer.w2_scales,
weight_bits=self.quant_config.weight_bits,
group_size=self.quant_config.group_size,
w1_zp=getattr(layer, "w13_qzeros", None) if use_zp else None,
w2_zp=getattr(layer, "w2_qzeros", None) if use_zp else None,
w1_bias=getattr(layer, "w13_bias", None),
w2_bias=getattr(layer, "w2_bias", None),
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
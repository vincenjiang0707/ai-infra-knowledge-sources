source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/moe_wna16/
lastmod: 2026-09-24

class MoeWNA16Method(FusedMoEMethodBase):
"""Linear method for MOE WNA16 (W8A16/W4A16) quantization.
Args:
quant_config: The MOE WNA16 (W8A16/W4A16) quantization config.
"""
def __init__(self, quant_config: MoeWNA16Config, moe: "FusedMoEConfig") -> None:
super().__init__(moe)
self.quant_config = quant_config
num_bits = self.quant_config.weight_bits
group_size = self.quant_config.group_size
if num_bits == 4:
quant_type = INT4_DTYPE
if group_size == 32:
scale = kInt4Static32GroupScale
else:
scale = kInt4StaticGroupScale
elif num_bits == 8:
quant_type = INT8_DTYPE
scale = kInt8StaticGroupScale
else:
raise ValueError("MoeWNA16Method only supports int4 and int8 now.")
weight_key = QuantKey(quant_type, scale)
# Select WNA16 MoE backend via oracle.
# handle ZP?
self.wna16_backend, self.experts_cls = select_wna16_moe_backend(
config=self.moe,
weight_key=weight_key,
quant_config=self.quant_config,
may_have_zp=self.quant_config.has_zp,
may_have_bias=False,
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
layer.quant_config = self.quant_config
bit8_pack_factor = self.quant_config.bit8_pack_factor
group_size = self.quant_config.group_size
group_size_div_factor = 1
# make intermediate_size and hidden_size divisible by group_size
# we reduce the group size to ensure that
# and we would repeat the loaded_weight later
while intermediate_size_per_partition % group_size or hidden_size % group_size:
group_size = group_size // 2
group_size_div_factor *= 2
assert group_size >= 32
layer.group_size = group_size
layer.group_size_div_factor = group_size_div_factor
strategy = FusedMoeWeightScaleSupported.GROUP.value
extra_weight_attrs.update({"quant_method": strategy, "is_transposed": False})
assert "weight_loader" in extra_weight_attrs
weight_loader = extra_weight_attrs["weight_loader"]
wrapped_weight_loader = MoeWNA16Method.get_weight_loader(layer, weight_loader)
extra_weight_attrs["weight_loader"] = wrapped_weight_loader
# Fused gate_up_proj (column parallel)
w13_qweight = torch.nn.Parameter(
torch.empty(
num_experts,
self.moe.w13_num_shards * intermediate_size_per_partition,
hidden_size // bit8_pack_factor,
dtype=torch.uint8,
),
requires_grad=False,
)
layer.register_parameter("w13_qweight", w13_qweight)
set_weight_attrs(w13_qweight, extra_weight_attrs)
# down_proj (row parallel)
w2_qweight = torch.nn.Parameter(
torch.empty(
num_experts,
hidden_size,
intermediate_size_per_partition // bit8_pack_factor,
dtype=torch.uint8,
),
requires_grad=False,
)
layer.register_parameter("w2_qweight", w2_qweight)
set_weight_attrs(w2_qweight, extra_weight_attrs)
w13_scales = torch.nn.Parameter(
torch.zeros(
num_experts,
self.moe.w13_num_shards * intermediate_size_per_partition,
hidden_size // group_size,
dtype=params_dtype,
),
requires_grad=False,
)
layer.register_parameter("w13_scales", w13_scales)
set_weight_attrs(w13_scales, extra_weight_attrs)
w2_scales = torch.nn.Parameter(
torch.zeros(
num_experts,
hidden_size,
intermediate_size_per_partition // group_size,
dtype=params_dtype,
),
requires_grad=False,
)
layer.register_parameter("w2_scales", w2_scales)
set_weight_attrs(w2_scales, extra_weight_attrs)
if self.quant_config.has_zp:
w13_qzeros = torch.nn.Parameter(
torch.zeros(
num_experts,
self.moe.w13_num_shards
* intermediate_size_per_partition
// bit8_pack_factor,
hidden_size // group_size,
dtype=torch.uint8,
),
requires_grad=False,
)
layer.register_parameter("w13_qzeros", w13_qzeros)
set_weight_attrs(w13_qzeros, extra_weight_attrs)
w2_qzeros = torch.nn.Parameter(
torch.zeros(
num_experts,
hidden_size // bit8_pack_factor,
intermediate_size_per_partition // group_size,
dtype=torch.uint8,
),
requires_grad=False,
)
layer.register_parameter("w2_qzeros", w2_qzeros)
set_weight_attrs(w2_qzeros, extra_weight_attrs)
if self.quant_config.linear_quant_method == "gptq":
# some param are unused, but we need to init them in order to
# load weights
invalid_param_keys: list[str] = []
if not self.quant_config.has_zp:
invalid_param_keys += ["w13_qzeros", "w2_qzeros"]
for key in invalid_param_keys:
param = torch.nn.Parameter(
torch.empty((0,), dtype=torch.int32), requires_grad=False
)
layer.register_parameter(key, param)
set_weight_attrs(param, extra_weight_attrs)
def get_fused_moe_quant_config(
self, layer: RoutedExperts
) -> FusedMoEQuantConfig | None:
if self.wna16_backend == WNA16MoEBackend.HUMMING:
from vllm.model_executor.layers.quantization.utils.humming import (
get_humming_moe_quant_config,
)
return get_humming_moe_quant_config(
layer,
gemm1_alpha=getattr(layer, "swiglu_alpha", None),
gemm1_beta=getattr(layer, "swiglu_beta", None),
gemm1_clamp_limit=getattr(layer, "swiglu_limit", None),
)
has_zp = self.quant_config.has_zp
return make_wna16_moe_quant_config(
w1_scale=layer.w13_scales,
w2_scale=layer.w2_scales,
w1_zp=layer.w13_qzeros if has_zp else None,
w2_zp=layer.w2_qzeros if has_zp else None,
group_size=layer.group_size,
num_bits=self.quant_config.weight_bits,
)
def _setup_kernel(self, layer: RoutedExperts):
assert self.experts_cls is not None
self.moe_quant_config = self.get_fused_moe_quant_config(layer)
assert self.moe_quant_config is not None
self.moe_kernel = make_wna16_moe_kernel(
moe_quant_config=self.moe_quant_config,
moe_config=self.moe,
experts_cls=self.experts_cls,
backend=self.wna16_backend,
routing_tables=layer._expert_routing_tables(),
)
def process_weights_after_loading(self, layer: RoutedExperts) -> None:
has_zp = self.quant_config.has_zp
converted = convert_to_wna16_moe_kernel_format(
backend=self.wna16_backend,
layer=layer,
quant_config=self.quant_config,
input_dtype=None,
w13=layer.w13_qweight,
w2=layer.w2_qweight,
w13_scale=layer.w13_scales,
w2_scale=layer.w2_scales,
w13_qzeros=layer.w13_qzeros if has_zp else None,
w2_qzeros=layer.w2_qzeros if has_zp else None,
)
if converted is None:
# Backend rewrote the layer's params in place (e.g. Humming).
self._setup_kernel(layer)
return
(
w13_qweight,
w2_qweight,
w13_scales,
w2_scales,
w13_qzeros,
w2_qzeros,
w13_input_global_scale,
w2_input_global_scale,
_, # w13_bias
_, # w2_bias
) = converted
# Replace common parameters
replace_parameter(layer, "w13_qweight", w13_qweight)
replace_parameter(layer, "w2_qweight", w2_qweight)
replace_parameter(layer, "w13_scales", w13_scales)
replace_parameter(layer, "w2_scales", w2_scales)
layer.w13_weight = layer.w13_qweight
layer.w2_weight = layer.w2_qweight
if has_zp:
assert w13_qzeros is not None and w2_qzeros is not None
replace_parameter(layer, "w13_qzeros", w13_qzeros)
replace_parameter(layer, "w2_qzeros", w2_qzeros)
# Marlin-specific parameters (not needed for Flashinfer)
if self.wna16_backend != WNA16MoEBackend.FLASHINFER_TRTLLM:
# Register input global scales if present
if w13_input_global_scale is not None:
layer.register_parameter(
"w13_input_global_scale",
torch.nn.Parameter(w13_input_global_scale, requires_grad=False),
)
if w2_input_global_scale is not None:
layer.register_parameter(
"w2_input_global_scale",
torch.nn.Parameter(w2_input_global_scale, requires_grad=False),
)
self._setup_kernel(layer)
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
x,
layer.w13_weight,
layer.w2_weight,
topk_weights=topk_weights,
topk_ids=topk_ids,
activation=layer.activation,
global_num_experts=layer.global_num_experts,
expert_map=layer.expert_map,
apply_router_weight_on_input=layer.apply_router_weight_on_input,
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
x,
layer.w13_weight,
layer.w2_weight,
router_logits,
activation=layer.activation,
global_num_experts=layer.global_num_experts,
expert_map=layer.expert_map,
apply_router_weight_on_input=layer.apply_router_weight_on_input,
num_expert_group=layer.num_expert_group,
topk_group=layer.topk_group,
e_score_correction_bias=layer.e_score_correction_bias,
routed_scaling_factor=layer.routed_scaling_factor,
)
@staticmethod
def get_weight_loader(layer, weight_loader):
def convert_awq_tensor(tensor, tensor_type):
# convert awq qweight/qzeros to a standard format (assume int4)
# qweight: (k, n // pack_factor_bit32) -> (n, k // pack_factor_bit8)
# qzeros: (k // group_size, n // pack_factor_bit32) ->
# (n // pack_factor_bit8, k // group_size)
# pack_factor_bit32 = 32 // weight_bits
# pack_factor_bit8 = 8 // weight_bits
# 0. suppose origin shape (a, b), dtype int32
# 1. convert to uint8, shape (a, b) -> (a, 4 * b)
size0 = tensor.size(0)
tensor = tensor.view(torch.uint8)
# 2. unpack to uint4 (only when weight_bits == 4)
# shape (a, 4 * b) -> (a, 4 * b, 2)
shifter = torch.tensor([0, 4], dtype=torch.uint8, device=tensor.device)
tensor = (tensor[:, :, None] >> shifter) & 0xF
# 3. change order, see
# https://github.com/casper-hansen/AutoAWQ/blob/v0.2.8/awq/utils/quant_utils.py
# shape -> (a, 4 * b * pack_factor_bit8)
reverse_awq_pack_order = [0, 4, 1, 5, 2, 6, 3, 7]
tensor = tensor.view(-1, 8)[:, reverse_awq_pack_order]
tensor = tensor.view(size0, -1)
# 4. transpose, shape -> (4 * b * pack_factor_bit8, a)
tensor = tensor.T.contiguous()
# 5. repack (only when weight_bits == 4)
# qweight shape -> (4 * b * pack_factor_bit8, a // pack_factor_bit8)
# qzeros shape -> (4 * b, a)
if tensor_type == "qweight":
tensor = tensor[:, 1::2] * 16 + tensor[:, ::2]
elif tensor_type == "qzeros":
tensor = tensor[1::2, :] * 16 + tensor[::2, :]
return tensor
def convert_gptq_int4_qzeros(tensor):
tensor = tensor.view(torch.uint8)
shifter = torch.tensor([0, 4], dtype=torch.uint8, device=tensor.device)
tensor = (tensor[:, :, None] >> shifter) & 0xF
tensor = tensor + 1
tensor = tensor[:, :, 0] + tensor[:, :, 1] * 16
return tensor
def moe_wna16_weight_loader(
param: torch.nn.Parameter,
loaded_weight: torch.Tensor,
weight_name: str,
shard_id: str,
expert_id: int,
return_success: bool = False,
):
if not layer.quant_config.has_zp and "qzeros" in weight_name:
return False if return_success else None
device = get_tp_group().device
tp_rank = get_tensor_model_parallel_rank()
loaded_weight = loaded_weight.to(device)
shard_size = layer.intermediate_size_per_partition
# convert gptq and awq weight to a standard format
# awq_marlin uses the same weight format as awq
if layer.quant_config.linear_quant_method in ("awq", "awq_marlin"):
assert layer.quant_config.weight_bits == 4
if "weight" in weight_name:
loaded_weight = convert_awq_tensor(loaded_weight, "qweight")
elif "zeros" in weight_name:
loaded_weight = convert_awq_tensor(loaded_weight, "qzeros")
else:
loaded_weight = loaded_weight.T
elif layer.quant_config.linear_quant_method == "gptq":
assert layer.quant_config.weight_bits in [4, 8]
if "weight" in weight_name:
loaded_weight = loaded_weight.T.contiguous().view(torch.uint8)
elif "zeros" in weight_name:
# add 1 to gptq qzeros to align with awq
loaded_weight = loaded_weight.view(torch.uint8)
if layer.quant_config.weight_bits == 4:
loaded_weight = convert_gptq_int4_qzeros(loaded_weight).T
else:
loaded_weight = loaded_weight.T + 1
else:
loaded_weight = loaded_weight.T
# repeat the qzeros/scales to fit new group size
if (
layer.group_size_div_factor > 1
and "qzeros" in weight_name
or "scales" in weight_name
):
loaded_weight = loaded_weight.repeat_interleave(
layer.group_size_div_factor, 1
)
if "w13_qzeros" in weight_name:
tensor = loaded_weight.view(
layer.moe_config.tp_size, -1, loaded_weight.size(1)
)[tp_rank]
if shard_id == "w1":
param.data[expert_id, : shard_size // 2] = tensor
else:
param.data[expert_id, shard_size // 2 :] = tensor
return True if return_success else None
elif "w2_qzeros" in weight_name:
param.data[expert_id] = loaded_weight.view(
loaded_weight.size(0), layer.moe_config.tp_size, -1
)[:, tp_rank]
return True if return_success else None
else:
# Delegate to the original loader, passing return_success
return weight_loader(
param,
loaded_weight,
weight_name,
shard_id,
expert_id,
return_success=return_success,
)
return moe_wna16_weight_loader
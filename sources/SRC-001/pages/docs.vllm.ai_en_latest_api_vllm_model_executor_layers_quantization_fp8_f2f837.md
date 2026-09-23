source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/fp8/
lastmod: 2026-09-23

class Fp8MoEMethod(FusedMoEMethodBase):
"""MoE method for FP8.
Supports loading FP8 checkpoints with static weight scale and
dynamic/static activation scale.
Also supports loading quantized FP16/BF16 model checkpoints with dynamic
activation scaling. The weight scaling factor will be initialized after
the model weights are loaded.
Args:
quant_config: The quantization config.
"""
supports_pre_processed_weights = True
def __init__(self, quant_config: Fp8Config, layer: RoutedExperts):
super().__init__(layer.moe_config)
self.quant_config = quant_config
self.weight_block_size = self.quant_config.weight_block_size
self.block_quant: bool = self.weight_block_size is not None
self.weight_scale_name = (
"weight_scale_inv" if self.block_quant else "weight_scale"
)
self.weight_scale_refine: tuple[int, int] | None = None
self.moe_block_shape = self.weight_block_size
# Set weight key and activation key for kernel compatibility
if self.block_quant:
assert self.weight_block_size is not None
# Adapt the checkpoint block shape to TP sharding before
# building the weight key.
self.moe_block_shape, self.weight_scale_refine = (
resolve_fp8_moe_weight_block_shape(
self.moe,
self.weight_block_size,
kFp8Dynamic128Sym,
self.quant_config.is_checkpoint_fp8_serialized,
)
)
weight_key = create_fp8_quant_key(
static=True, group_shape=GroupShape(*self.moe_block_shape)
)
activation_key = kFp8Dynamic128Sym
else:
weight_key = kFp8StaticTensorSym
activation_key = (
kFp8StaticTensorSym
if self.quant_config.activation_scheme == "static"
else kFp8DynamicTensorSym
)
# Select Fp8 MoE backend
self.fp8_backend, self.experts_cls = select_fp8_moe_backend(
config=self.moe,
weight_key=weight_key,
activation_key=activation_key,
allow_vllm_cutlass=False,
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
layer.num_experts = num_experts
layer.orig_dtype = params_dtype
layer.weight_block_size = None
assert self.quant_config.is_checkpoint_fp8_serialized
params_dtype = torch.float8_e4m3fn
if self.block_quant:
assert self.weight_block_size is not None
assert self.moe_block_shape is not None
moe_block_shape = self.moe_block_shape
layer.weight_block_size = self.weight_block_size
block_n, block_k = (
self.weight_block_size[0],
self.weight_block_size[1],
)
if self.weight_scale_refine is None:
validate_fp8_block_shape_moe(
intermediate_size_per_partition,
self.weight_block_size,
)
else:
# Use the refined block grid for the scale parameters; the
# loader upsamples the checkpoint scales accordingly.
tp_size = get_tensor_model_parallel_world_size()
if intermediate_size_per_partition % block_n != 0:
block_n, block_k = moe_block_shape
if tp_size > 1 and intermediate_size_per_partition % block_k != 0:
block_n, block_k = moe_block_shape
# WEIGHTS
w13_weight = torch.nn.Parameter(
torch.empty(
num_experts,
self.moe.w13_num_shards * intermediate_size_per_partition,
hidden_size,
dtype=params_dtype,
),
requires_grad=False,
)
layer.register_parameter("w13_weight", w13_weight)
set_weight_attrs(w13_weight, extra_weight_attrs)
w2_weight = torch.nn.Parameter(
torch.empty(
num_experts,
hidden_size,
intermediate_size_per_partition,
dtype=params_dtype,
),
requires_grad=False,
)
layer.register_parameter("w2_weight", w2_weight)
set_weight_attrs(w2_weight, extra_weight_attrs)
# BIASES (for models like GPT-OSS that have biased MoE)
if self.moe.has_bias:
w13_bias = torch.nn.Parameter(
torch.zeros(
num_experts,
self.moe.w13_num_shards * intermediate_size_per_partition,
dtype=layer.orig_dtype,
),
requires_grad=False,
)
layer.register_parameter("w13_bias", w13_bias)
set_weight_attrs(w13_bias, extra_weight_attrs)
w2_bias = torch.nn.Parameter(
torch.zeros(num_experts, hidden_size, dtype=layer.orig_dtype),
requires_grad=False,
)
layer.register_parameter("w2_bias", w2_bias)
set_weight_attrs(w2_bias, extra_weight_attrs)
# WEIGHT_SCALES
if not self.block_quant:
# For per-tensor quant, the scales are per expert and weight.
w13_scale_data = torch.ones(
num_experts, self.moe.w13_num_shards, dtype=torch.float32
)
w2_scale_data = torch.ones(num_experts, dtype=torch.float32)
else:
# For block quant, the scales are per block (typically 128x128).
w13_scale_data = torch.ones(
num_experts,
self.moe.w13_num_shards
* ((intermediate_size_per_partition + block_n - 1) // block_n),
(hidden_size + block_k - 1) // block_k,
dtype=torch.float32,
)
w2_scale_data = torch.ones(
num_experts,
(hidden_size + block_n - 1) // block_n,
(intermediate_size_per_partition + block_k - 1) // block_k,
dtype=torch.float32,
)
w13_weight_scale = torch.nn.Parameter(w13_scale_data, requires_grad=False)
w2_weight_scale = torch.nn.Parameter(w2_scale_data, requires_grad=False)
# Note: name is weight_scale for tensor, weight_scale_inv for block.
layer.register_parameter(f"w13_{self.weight_scale_name}", w13_weight_scale)
layer.register_parameter(f"w2_{self.weight_scale_name}", w2_weight_scale)
# Add the quantization method used (per tensor/grouped/channel)
# to ensure the weight scales are loaded in properly
extra_weight_attrs.update(
{"quant_method": FusedMoeWeightScaleSupported.BLOCK.value}
if self.block_quant
else {"quant_method": FusedMoeWeightScaleSupported.TENSOR.value}
)
set_weight_attrs(w13_weight_scale, extra_weight_attrs)
set_weight_attrs(w2_weight_scale, extra_weight_attrs)
# INPUT_SCALES
if self.quant_config.activation_scheme == "static":
assert not self.block_quant
w13_input_scale = torch.nn.Parameter(
torch.ones(num_experts, dtype=torch.float32), requires_grad=False
)
layer.register_parameter("w13_input_scale", w13_input_scale)
set_weight_attrs(w13_input_scale, extra_weight_attrs)
w2_input_scale = torch.nn.Parameter(
torch.ones(num_experts, dtype=torch.float32), requires_grad=False
)
layer.register_parameter("w2_input_scale", w2_input_scale)
set_weight_attrs(w2_input_scale, extra_weight_attrs)
else:
layer.w13_input_scale = None
layer.w2_input_scale = None
def _setup_kernel(
self,
layer: RoutedExperts,
w13: torch.Tensor,
w2: torch.Tensor,
w13_scale: torch.Tensor,
w2_scale: torch.Tensor,
w13_input_scale: torch.Tensor | None,
w2_input_scale: torch.Tensor | None,
) -> None:
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
# Replace parameters with updated versions. Note that this helper
# function ensures the replacement is compatible with RL weight reloads.
replace_parameter(layer, "w13_weight", w13)
replace_parameter(layer, "w2_weight", w2)
replace_parameter(layer, f"w13_{self.weight_scale_name}", w13_scale)
replace_parameter(layer, f"w2_{self.weight_scale_name}", w2_scale)
self._init_moe_kernel(layer)
def _init_moe_kernel(self, layer: RoutedExperts) -> None:
"""Build the MoE kernel from the layer's current (converted) weights."""
self.moe_quant_config = self.get_fused_moe_quant_config(layer)
assert self.moe_quant_config is not None
assert self.experts_cls is not None
self.moe_kernel = make_fp8_moe_kernel(
moe_quant_config=self.moe_quant_config,
moe_config=self.moe,
fp8_backend=self.fp8_backend,
experts_cls=self.experts_cls,
routing_tables=layer._expert_routing_tables(),
)
def process_weights_after_loading(self, layer: RoutedExperts) -> None:
if is_weights_pre_processed():
# Weights are already in kernel format; rebuild the kernel only.
self._init_moe_kernel(layer)
return
# Allow for accessing weights and scales in standard way.
w13 = layer.w13_weight
w2 = layer.w2_weight
w13_scale = getattr(layer, f"w13_{self.weight_scale_name}")
w2_scale = getattr(layer, f"w2_{self.weight_scale_name}")
w13_input_scale = layer.w13_input_scale
w2_input_scale = layer.w2_input_scale
# MI300x and MI325x use FNUZ format for FP8. Convert if needed.
if current_platform.is_fp8_fnuz():
w13, w13_scale, w13_input_scale = normalize_e4m3fn_to_e4m3fnuz(
w13,
w13_scale,
w13_input_scale,
)
w2, w2_scale, w2_input_scale = normalize_e4m3fn_to_e4m3fnuz(
w2,
w2_scale,
w2_input_scale,
)
# Per tensor kernels require single activation scale. Use the max.
if self.quant_config.activation_scheme == "static":
assert not self.block_quant
assert w13_input_scale is not None and w2_input_scale is not None
w13_input_scale, w2_input_scale = process_fp8_input_tensor_strategy_moe(
w13_input_scale,
w2_input_scale,
layer.moe_config.moe_parallel_config.enable_eplb,
)
replace_parameter(layer, "w13_input_scale", w13_input_scale)
replace_parameter(layer, "w2_input_scale", w2_input_scale)
# Per tensor kernels require single weight scale for w13 per expert, but
# on disk there is a scale for w1 and w3. Use the max to requantize.
if not self.block_quant:
shard_size = layer.intermediate_size_per_partition
w13, w13_scale = process_fp8_weight_tensor_strategy_moe(
w13,
w13_scale,
shard_size,
layer.local_num_experts,
is_act_and_mul=self.moe.is_act_and_mul,
)
# Shuffle weights to runtime format and setup kernel.
self._setup_kernel(
layer, w13, w2, w13_scale, w2_scale, w13_input_scale, w2_input_scale
)
def get_fused_moe_quant_config(self, layer: RoutedExperts) -> FusedMoEQuantConfig:
w1_scale = getattr(layer, f"w13_{self.weight_scale_name}")
w2_scale = getattr(layer, f"w2_{self.weight_scale_name}")
a1_scale = layer.w13_input_scale
a2_scale = layer.w2_input_scale
quant_config = make_fp8_moe_quant_config(
fp8_backend=self.fp8_backend,
w1_scale=w1_scale,
w2_scale=w2_scale,
a1_scale=a1_scale,
a2_scale=a2_scale,
block_shape=self.moe_block_shape,
swiglu_limit=getattr(layer, "swiglu_limit", None),
gemm1_alpha=getattr(layer, "swiglu_alpha", None),
gemm1_beta=getattr(layer, "swiglu_beta", None),
layer=layer,
)
# Inject biases into the quant config if the model has them
# (e.g. GPT-OSS biased MoE)
if quant_config is not None and self.moe.has_bias:
w13_bias = getattr(layer, "w13_bias", None)
w2_bias = getattr(layer, "w2_bias", None)
if w13_bias is not None:
quant_config._w1.bias = w13_bias
if w2_bias is not None:
quant_config._w2.bias = w2_bias
return quant_config
@property
def supports_eplb(self) -> bool:
return True
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
topk_weights,
topk_ids,
activation=layer.activation,
global_num_experts=layer.global_num_experts,
expert_map=layer.expert_map,
apply_router_weight_on_input=layer.apply_router_weight_on_input,
shared_experts=shared_experts,
shared_experts_input=shared_experts_input,
)
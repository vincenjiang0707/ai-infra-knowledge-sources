source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/quark/quark_moe/
lastmod: 2026-09-23

class QuarkOCP_MX_MoEMethod(QuarkMoEMethod):
supported_activation_quant_keys = [
*_ACTIVATION_QUANT_KEY_MAP.values(),
kFp8DynamicTensorSym,
kFp8StaticTensorSym,
None,
]
supported_weight_quant_keys = [*_WEIGHT_QUANT_KEY_MAP.values()]
def __init__(
self,
moe: FusedMoEConfig,
weight_quant_key: QuantKey,
activation_quant_key: QuantKey | None,
):
super().__init__(moe, weight_quant_key, activation_quant_key)
self.weight_dtype = next(
dtype
for dtype, quant_key in _WEIGHT_QUANT_KEY_MAP.items()
if quant_key == weight_quant_key
)
if activation_quant_key in {kFp8DynamicTensorSym, kFp8StaticTensorSym}:
self.input_dtype: str | None = "fp8"
elif activation_quant_key is None:
self.input_dtype = None
else:
self.input_dtype = next(
dtype
for dtype, quant_key in _ACTIVATION_QUANT_KEY_MAP.items()
if quant_key == activation_quant_key
)
self.ocp_mx_scheme = OCP_MX_Scheme.from_quant_dtype(
self.input_dtype, self.weight_dtype
)
if self.ocp_mx_scheme is None:
raise ValueError(
f"Unsupported OCP MX dtype combination for MoE: "
f"input_dtype={self.input_dtype}, weight_dtype={self.weight_dtype}. "
f"Please check that the combination is supported in OCP_MX_Scheme."
)
# TODO(bowenbao): refactor and introduce backends for other OCP MX schemes,
# use kernel abstraction for all OCP MX MOE implementations.
self.mxfp4_backend: Mxfp4MoeBackend = Mxfp4MoeBackend.NONE
self.experts_cls: type[mk.FusedMoEExperts] | None = None
self.moe_kernel: mk.FusedMoEKernel | None = None
# Used for triton kernel precision configs (W4A8, TRITON backends)
self.w13_precision_config = None
self.w2_precision_config = None
self.static_input_scales = activation_quant_key == kFp8StaticTensorSym
# Select backend based on OCP MX scheme
if self.ocp_mx_scheme == "w_mxfp4":
# W4A16: weight-only MXFP4
self.mxfp4_backend, self.experts_cls = select_mxfp4_moe_backend(moe)
elif self.ocp_mx_scheme == "w_mxfp4_a_fp8" and self.static_input_scales:
# W4A8: MXFP4 weights + static FP8 activations
self.mxfp4_backend, self.experts_cls = select_mxfp4_moe_backend(
moe, activation_key=kFp8StaticTensorSym
)
elif self.ocp_mx_scheme == "w_mxfp4_a_mxfp4":
# W4A4: MXFP4 weights + MXFP4 activations
self.mxfp4_backend, self.experts_cls = select_mxfp4_moe_backend(
moe, activation_key=kMxfp4Dynamic
)
# Validation for unsupported schemes
if any(
self.ocp_mx_scheme.endswith(a_scheme)
for a_scheme in ["a_mxfp4", "a_mxfp6_e3m2", "a_mxfp6_e2m3"]
):
if self.static_input_scales:
raise NotImplementedError(
"QuarkOCP_MX_MoEMethod with static input scales is currently "
f"not implemented for OCP MX scheme {self.ocp_mx_scheme}. "
"Please open an issue."
)
elif self.ocp_mx_scheme.endswith("a_fp8") and not self.static_input_scales:
raise NotImplementedError(
"QuarkOCP_MX_MoEMethod with dynamic input scales is currently "
f"not implemented for OCP MX scheme {self.ocp_mx_scheme}. "
"Please open an issue."
)
self.model_type = getattr(
get_current_vllm_config().model_config.hf_config, "model_type", None
)
# If no native backend available, use emulation.
if self.mxfp4_backend is Mxfp4MoeBackend.NONE:
self.mxfp4_backend = Mxfp4MoeBackend.EMULATION
self.experts_cls = backend_to_kernel_cls(self.mxfp4_backend)[0]
logger.info_once(
f"Using {self.mxfp4_backend.value} backend for {self.ocp_mx_scheme}"
)
def maybe_roundup_sizes(
self,
hidden_size: int,
intermediate_size_per_partition: int,
act_dtype: torch.dtype,
moe_parallel_config: FusedMoEParallelConfig,
) -> tuple[int, int]:
hidden_size, intermediate_size_per_partition = super().maybe_roundup_sizes(
hidden_size=hidden_size,
intermediate_size_per_partition=intermediate_size_per_partition,
act_dtype=act_dtype,
moe_parallel_config=moe_parallel_config,
)
# Round per-partition sizes up to each backend's requirement. Emulation is
# handled inside the helper too (OCP MX block alignment), so no special-case.
if self.mxfp4_backend is not None:
hidden_size, intermediate_size_per_partition = (
mxfp4_round_up_hidden_size_and_intermediate_size(
self.mxfp4_backend, hidden_size, intermediate_size_per_partition
)
)
return hidden_size, intermediate_size_per_partition
def get_packed_dim(self, dim: int, quant_dtype: str):
if quant_dtype == "mxfp4":
assert dim % 2 == 0
return dim // 2
else:
# FP6 packs 4 * 6 = 24 bits on 3 bytes.
assert (dim * 3) % 4 == 0
return (dim * 3) // 4
def create_weights(
self,
layer: RoutedExperts,
num_experts: int,
hidden_size: int,
intermediate_size_per_partition: int,
params_dtype: torch.dtype,
**extra_weight_attrs,
):
# Add the quantization method used (per tensor/grouped/channel)
# to ensure the weight scales are loaded in properly
extra_weight_attrs.update(
{"quant_method": FusedMoeWeightScaleSupported.BLOCK.value}
)
params_dtype = torch.uint8
# WEIGHTS
w13_weight = torch.nn.Parameter(
torch.zeros(
num_experts,
self.moe.w13_num_shards * intermediate_size_per_partition,
self.get_packed_dim(hidden_size, self.weight_dtype),
dtype=params_dtype,
),
requires_grad=False,
)
layer.register_parameter("w13_weight", w13_weight)
set_weight_attrs(w13_weight, extra_weight_attrs)
w2_weight = torch.nn.Parameter(
torch.zeros(
num_experts,
hidden_size,
self.get_packed_dim(intermediate_size_per_partition, self.weight_dtype),
dtype=params_dtype,
),
requires_grad=False,
)
layer.register_parameter("w2_weight", w2_weight)
set_weight_attrs(w2_weight, extra_weight_attrs)
# WEIGHT_SCALES
w13_weight_scale = torch.nn.Parameter(
torch.ones(
num_experts,
self.moe.w13_num_shards * intermediate_size_per_partition,
hidden_size // OCP_MX_BLOCK_SIZE,
dtype=params_dtype,
),
requires_grad=False,
)
w2_weight_scale = torch.nn.Parameter(
torch.ones(
num_experts,
hidden_size,
intermediate_size_per_partition // OCP_MX_BLOCK_SIZE,
dtype=params_dtype,
),
requires_grad=False,
)
set_weight_attrs(w2_weight_scale, extra_weight_attrs)
set_weight_attrs(w13_weight_scale, extra_weight_attrs)
layer.register_parameter("w13_weight_scale", w13_weight_scale)
layer.register_parameter("w2_weight_scale", w2_weight_scale)
if self.has_bias:
w13_bias = torch.nn.Parameter(
torch.zeros(
num_experts,
self.moe.w13_num_shards * intermediate_size_per_partition,
dtype=torch.float32,
),
requires_grad=False,
)
layer.register_parameter("w13_bias", w13_bias)
set_weight_attrs(w13_bias, extra_weight_attrs)
w2_bias = torch.nn.Parameter(
torch.zeros(num_experts, hidden_size, dtype=torch.float32),
requires_grad=False,
)
layer.register_parameter("w2_bias", w2_bias)
set_weight_attrs(w2_bias, extra_weight_attrs)
else:
layer.w13_bias, layer.w2_bias = None, None
# INPUT_SCALES
if self.static_input_scales:
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
def process_weights_after_loading(self, layer):
self._setup_kernel(layer)
def _setup_kernel(self, layer: RoutedExperts):
"""Setup kernel using oracle functions for MXFP4 schemes (W4A16, W4A8)."""
w13_bias = getattr(layer, "w13_bias", None)
w2_bias = getattr(layer, "w2_bias", None)
# Convert weights to kernel format (handles all backend-specific logic)
w13, w2, w13_scale, w2_scale, w13_bias, w2_bias = (
convert_gpt_oss_weight_to_mxfp4_moe_kernel_format(
mxfp4_backend=self.mxfp4_backend,
layer=layer,
w13_weight=layer.w13_weight,
w2_weight=layer.w2_weight,
w13_weight_scale=layer.w13_weight_scale,
w2_weight_scale=layer.w2_weight_scale,
w13_bias=w13_bias,
w2_bias=w2_bias,
w13_input_scale=layer.w13_input_scale,
w2_input_scale=layer.w2_input_scale,
)
)
# Handle weight/scale assignment based on backend type
if self.mxfp4_backend in TRITON_BACKENDS or self.mxfp4_backend in (
Mxfp4MoeBackend.AITER_MXFP4_FP8,
):
# Triton-based backends: w13/w2 are triton_kernels.tensor.Tensor
# Store on layer for apply(), scales are PrecisionConfig
layer.w13_weight = w13
layer.w2_weight = w2
self.w13_precision_config = w13_scale
self.w2_precision_config = w2_scale
else:
# Standard backends: replace parameters
replace_parameter(layer, "w13_weight", w13)
replace_parameter(layer, "w2_weight", w2)
replace_parameter(layer, "w13_weight_scale", w13_scale)
replace_parameter(layer, "w2_weight_scale", w2_scale)
if w13_bias is not None and w2_bias is not None:
replace_parameter(layer, "w13_bias", w13_bias)
replace_parameter(layer, "w2_bias", w2_bias)
torch.accelerator.empty_cache()
# Build quant config and kernel
self.moe_quant_config = self.get_fused_moe_quant_config(layer)
if self.moe_quant_config is not None and self.experts_cls is not None:
self.moe_kernel = make_mxfp4_moe_kernel(
moe_quant_config=self.moe_quant_config,
moe_config=self.moe,
mxfp4_backend=self.mxfp4_backend,
experts_cls=self.experts_cls,
routing_tables=layer._expert_routing_tables(),
)
self.moe_kernel.fused_experts.process_weights_after_loading(layer)
def get_fused_moe_quant_config(
self, layer: RoutedExperts
) -> FusedMoEQuantConfig | None:
# For oracle-based backends (W4A16, W4A8), use make_mxfp4_moe_quant_config
if self.mxfp4_backend not in (Mxfp4MoeBackend.NONE, Mxfp4MoeBackend.EMULATION):
# Determine scale source based on backend type
if self.mxfp4_backend in TRITON_BACKENDS or self.mxfp4_backend in (
Mxfp4MoeBackend.AITER_MXFP4_FP8,
):
w1_scale = self.w13_precision_config
w2_scale = self.w2_precision_config
else:
w1_scale = layer.w13_weight_scale
w2_scale = layer.w2_weight_scale
return make_mxfp4_moe_quant_config(
mxfp4_backend=self.mxfp4_backend,
w1_scale=w1_scale,
w2_scale=w2_scale,
w1_bias=getattr(layer, "w13_bias", None),
w2_bias=getattr(layer, "w2_bias", None),
a1_scale=getattr(layer, "w13_input_scale", None),
a2_scale=getattr(layer, "w2_input_scale", None),
gemm1_alpha=getattr(layer, "swiglu_alpha", None),
gemm1_beta=getattr(layer, "swiglu_beta", None),
swiglu_limit=getattr(layer, "swiglu_limit", None),
layer=layer,
)
# Emulation and other schemes
if self.ocp_mx_scheme == "w_mxfp4":
return mxfp4_w4a16_moe_quant_config(
w1_scale=layer.w13_weight_scale,
w2_scale=layer.w2_weight_scale,
w1_bias=layer.w13_bias,
w2_bias=layer.w2_bias,
)
elif self.ocp_mx_scheme == "w_mxfp4_a_fp8":
return mxfp4_w4a8_moe_quant_config(
w1_scale=layer.w13_weight_scale,
w2_scale=layer.w2_weight_scale,
a1_scale=layer.w13_input_scale,
a2_scale=layer.w2_input_scale,
w1_bias=layer.w13_bias,
w2_bias=layer.w2_bias,
block_shape=None,
)
elif self.ocp_mx_scheme in ["w_mxfp6_e3m2_a_fp8", "w_mxfp6_e2m3_a_fp8"]:
raise NotImplementedError(
"Currently there is no corresponding fused moe quant config configured "
f"in vLLM for OCP MX scheme {self.ocp_mx_scheme}. Please open an issue."
)
else:
assert self.input_dtype is not None
return ocp_mx_moe_quant_config(
quant_dtype=self.input_dtype,
weight_dtype=self.weight_dtype,
w1_scale=layer.w13_weight_scale,
w2_scale=layer.w2_weight_scale,
w1_bias=layer.w13_bias,
w2_bias=layer.w2_bias,
a1_scale=None,
a2_scale=None,
block_shape=None,
gemm1_alpha=getattr(layer, "swiglu_alpha", None),
gemm1_beta=getattr(layer, "swiglu_beta", None),
gemm1_clamp_limit=getattr(layer, "swiglu_limit", None),
)
@property
def supports_eplb(self) -> bool:
# AITER shuffle keeps expert dim outermost, so EPLB row moves are layout-safe.
return True
@property
def is_monolithic(self) -> bool:
if self.moe_kernel is not None:
return self.moe_kernel.is_monolithic
return False
def apply(
self,
layer: RoutedExperts,
x: torch.Tensor,
topk_weights: torch.Tensor,
topk_ids: torch.Tensor,
shared_experts: SharedExperts | None,
shared_experts_input: torch.Tensor | None,
) -> torch.Tensor:
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
shared_experts_input=shared_experts_input,
)
def apply_monolithic(
self,
layer: RoutedExperts,
x: torch.Tensor,
router_logits: torch.Tensor,
input_ids: torch.Tensor | None = None,
) -> torch.Tensor | UnfinalizedMoEOutput:
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
)
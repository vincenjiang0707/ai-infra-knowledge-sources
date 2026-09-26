source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/online/mxfp4/
lastmod: 2026-09-24

class Mxfp4OnlineMoEMethod(OnlineMoEMethodBase):
"""MoE method for online MXFP4 (block) quantization."""
mxfp4_backend: Mxfp4MoeBackend
experts_cls: "type[mk.FusedMoEExperts] | None"
activation_quant_key = kMxfp4Dynamic
def __init__(self, *, moe: FusedMoEConfig):
super().__init__(moe)
self.weight_block_size: list[int] = [1, MXFP4_BLOCK_SIZE]
self.weight_scale_name = "weight_scale"
self.mxfp4_backend, self.experts_cls = select_mxfp4_moe_backend(
config=self.moe, activation_key=self.activation_quant_key
)
def maybe_roundup_sizes(
self,
hidden_size: int,
intermediate_size_per_partition: int,
act_dtype: torch.dtype,
moe_parallel_config: "FusedMoEParallelConfig",
) -> tuple[int, int]:
hidden_size, intermediate_size_per_partition = super().maybe_roundup_sizes(
hidden_size=hidden_size,
intermediate_size_per_partition=intermediate_size_per_partition,
act_dtype=act_dtype,
moe_parallel_config=moe_parallel_config,
)
return mxfp4_round_up_hidden_size_and_intermediate_size(
self.mxfp4_backend, hidden_size, intermediate_size_per_partition
)
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
hidden_size % MXFP4_BLOCK_SIZE != 0
or intermediate_size_per_partition % MXFP4_BLOCK_SIZE != 0
):
raise ValueError(
"Online MXFP4 MoE requires hidden/intermediate sizes divisible "
f"by {MXFP4_BLOCK_SIZE}."
)
super().create_weights(
layer=layer,
num_experts=num_experts,
hidden_size=hidden_size,
intermediate_size_per_partition=intermediate_size_per_partition,
params_dtype=params_dtype,
**extra_weight_attrs,
)
layer.weight_block_size = [1, MXFP4_BLOCK_SIZE]
def _setup_kernel(
self,
layer: "RoutedExperts",
w13: torch.Tensor,
w2: torch.Tensor,
w13_scale: torch.Tensor,
w2_scale: torch.Tensor,
w13_bias: torch.Tensor | None,
w2_bias: torch.Tensor | None,
) -> None:
w13, w2, w13_scale, w2_scale, w13_bias, w2_bias = (
convert_weight_to_mxfp4_moe_kernel_format(
mxfp4_backend=self.mxfp4_backend,
layer=layer,
w13_weight=w13,
w2_weight=w2,
w13_weight_scale=w13_scale,
w2_weight_scale=w2_scale,
w13_bias=w13_bias,
w2_bias=w2_bias,
)
)
# Handle weight/scale assignment based on backend type
# Copied from `quark_moe.py`.
# TODO: This should not be here, replace_parameter should handle
# triton_kernels.tensor.Tensor.
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
self, layer: torch.nn.Module
) -> "FusedMoEQuantConfig | None":
# NOTE: unlike `QuarkOCP_MX_MoEMethod.get_fused_moe_quant_config`, this
# does not branch on `self.mxfp4_backend in TRITON_BACKENDS or
# AITER_MXFP4_FP8` to read `self.w13_precision_config`/
# `self.w2_precision_config` instead of `layer.w13_weight_scale`/
# `layer.w2_weight_scale`. For those backends,
# `convert_weight_to_mxfp4_moe_kernel_format` deletes the latter, so
# `getattr` below would raise `AttributeError`. This is currently
# unreachable because `activation_quant_key` is hardcoded to
# `kMxfp4Dynamic`
# TODO: When supporting online activation quant key override,
# fix this convert_weight_to_mxfp4_moe_kernel_format issue.
w1_scale = getattr(layer, f"w13_{self.weight_scale_name}")
w2_scale = getattr(layer, f"w2_{self.weight_scale_name}")
return make_mxfp4_moe_quant_config(
mxfp4_backend=self.mxfp4_backend,
w1_scale=w1_scale,
w2_scale=w2_scale,
w1_bias=getattr(layer, "w13_bias", None),
w2_bias=getattr(layer, "w2_bias", None),
a1_scale=layer.w13_input_scale,
a2_scale=layer.w2_input_scale,
swiglu_limit=getattr(layer, "swiglu_limit", None),
gemm1_alpha=getattr(layer, "swiglu_alpha", None),
gemm1_beta=getattr(layer, "swiglu_beta", None),
layer=layer,
)
def process_weights_after_loading(self, layer: Module) -> None:
if getattr(layer, "_already_called_process_weights_after_loading", False):
return
self._zero_padding(layer)
if self.mxfp4_backend == Mxfp4MoeBackend.NONE:
layer._already_called_process_weights_after_loading = True
return
layer.w13_input_scale = None
layer.w2_input_scale = None
w13, w13_scale = _quantize_mxfp4_moe_weight(layer.w13_weight)
w2, w2_scale = _quantize_mxfp4_moe_weight(layer.w2_weight)
self._setup_kernel(
layer,
w13,
w2,
w13_scale,
w2_scale,
getattr(layer, "w13_bias", None),
getattr(layer, "w2_bias", None),
)
layer._already_called_process_weights_after_loading = True
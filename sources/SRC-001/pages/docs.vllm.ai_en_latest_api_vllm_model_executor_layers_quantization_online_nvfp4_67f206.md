source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/online/nvfp4/
lastmod: 2026-09-24

class Nvfp4OnlineMoEMethod(OnlineMoEMethodBase):
"""Online NVFP4 MoE quantization with per-token activation scales.
Quantizes fp16/bf16 expert weights to NVFP4 at load time; the FlashInfer
TRTLLM kernel computes per-token activation scales at runtime. Blackwell
(SM100) only.
"""
def __init__(
self,
*,
moe: FusedMoEConfig,
):
if not current_platform.is_device_capability_family(100):
raise ValueError(
"nvfp4_per_token online quantization requires a Blackwell (SM100) GPU."
)
super().__init__(moe)
self.nvfp4_backend, self.experts_cls = select_nvfp4_moe_backend(
config=self.moe,
weight_key=kNvfp4Static,
activation_key=kNvfp4DynamicToken,
)
def process_weights_after_loading(self, layer: Module) -> None:
if getattr(layer, "_already_called_process_weights_after_loading", False):
return
self._quantize_weights(layer)
self._setup_kernel(layer)
layer._already_called_process_weights_after_loading = True
def _quantize_weights(self, layer: Module) -> None:
moe_tp_size = self.moe.tp_size
w13, w13_scale, w13_scale_2 = _quantize_moe_weight_to_nvfp4(
layer.w13_weight, moe_tp_size
)
w2, w2_scale, w2_scale_2 = _quantize_moe_weight_to_nvfp4(
layer.w2_weight, moe_tp_size
)
replace_parameter(layer, "w13_weight", w13)
replace_parameter(layer, "w13_weight_scale", w13_scale)
replace_parameter(layer, "w13_weight_scale_2", w13_scale_2)
replace_parameter(layer, "w2_weight", w2)
replace_parameter(layer, "w2_weight_scale", w2_scale)
replace_parameter(layer, "w2_weight_scale_2", w2_scale_2)
# Neutral (1.0) activation global scales: the kernel derives per-token
# scales at runtime, so the output scalars reduce to the weight scales.
ones = torch.ones(layer.num_experts, device=w13.device, dtype=torch.float32)
replace_parameter(layer, "w13_input_scale", ones)
replace_parameter(layer, "w2_input_scale", ones.clone())
def _setup_kernel(self, layer: RoutedExperts) -> None:
(
w13,
w13_scale,
w13_scale_2,
a13_scale,
w2,
w2_scale,
w2_scale_2,
a2_scale,
) = convert_to_nvfp4_moe_kernel_format(
nvfp4_backend=self.nvfp4_backend,
layer=layer,
w13=layer.w13_weight,
w13_scale=layer.w13_weight_scale,
w13_scale_2=layer.w13_weight_scale_2,
a13_scale=layer.w13_input_scale,
w2=layer.w2_weight,
w2_scale=layer.w2_weight_scale,
w2_scale_2=layer.w2_weight_scale_2,
a2_scale=layer.w2_input_scale,
is_act_and_mul=self.moe.is_act_and_mul,
)
replace_parameter(layer, "w13_weight", w13)
replace_parameter(layer, "w13_weight_scale", w13_scale)
replace_parameter(layer, "w13_weight_scale_2", w13_scale_2)
replace_parameter(layer, "w13_input_scale", a13_scale)
replace_parameter(layer, "w2_weight", w2)
replace_parameter(layer, "w2_weight_scale", w2_scale)
replace_parameter(layer, "w2_weight_scale_2", w2_scale_2)
replace_parameter(layer, "w2_input_scale", a2_scale)
if self.moe_kernel is None:
self.moe_quant_config = self.get_fused_moe_quant_config(layer)
assert self.experts_cls is not None
self.moe_kernel = make_nvfp4_moe_kernel(
moe_quant_config=self.moe_quant_config,
moe_config=self.moe,
experts_cls=self.experts_cls,
backend=self.nvfp4_backend,
routing_tables=layer._expert_routing_tables(),
per_token_activation=True,
)
self.moe_kernel.fused_experts.process_weights_after_loading(layer)
def get_fused_moe_quant_config(self, layer: torch.nn.Module) -> FusedMoEQuantConfig:
return make_nvfp4_moe_quant_config(
backend=self.nvfp4_backend,
w13_scale=layer.w13_weight_scale,
w2_scale=layer.w2_weight_scale,
w13_scale_2=layer.w13_weight_scale_2,
w2_scale_2=layer.w2_weight_scale_2,
a13_scale=layer.w13_input_scale,
a2_scale=layer.w2_input_scale,
swiglu_limit=getattr(layer, "swiglu_limit", None),
layer=layer,
)
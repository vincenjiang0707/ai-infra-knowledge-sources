source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe/
lastmod: 2026-09-23

def rocm_aiter_fused_experts(
hidden_states: torch.Tensor,
w1: torch.Tensor,
w2: torch.Tensor,
topk_weights: torch.Tensor,
topk_ids: torch.Tensor,
moe_config: FusedMoEConfig,
activation: MoEActivation = MoEActivation.SILU,
apply_router_weight_on_input: bool = False,
expert_mask: torch.Tensor | None = None,
quant_config: FusedMoEQuantConfig | None = None,
a1q_scale: torch.Tensor | None = None,
num_local_tokens: torch.Tensor | None = None,
output_dtype: torch.dtype | None = None,
moe_sorting_dispatch_policy: int = 0,
shared_w1: torch.Tensor | None = None,
shared_w2: torch.Tensor | None = None,
shared_w1_scale: torch.Tensor | None = None,
shared_w2_scale: torch.Tensor | None = None,
shared_expert_id: int = -1,
) -> torch.Tensor:
"""ROCm AITER fused MoE expert computation."""
if quant_config is None:
quant_config = FUSED_MOE_UNQUANTIZED_CONFIG
# Gate/up interleave hint; only the SWIGLUOAI activations override it.
activation_interleave = None
activation_method: ActivationMethod | ActivationType
if activation == MoEActivation.SILU:
activation_method = ActivationMethod.SILU
elif activation == MoEActivation.GELU:
activation_method = ActivationMethod.GELU
elif activation == MoEActivation.SWIGLUOAI:
activation_method = rocm_aiter_ops.get_aiter_activation_type("swiglu")
elif activation == MoEActivation.SWIGLUOAI_UNINTERLEAVE:
activation_method = rocm_aiter_ops.get_aiter_activation_type("swiglu")
activation_interleave = False
elif activation == MoEActivation.SITU:
activation_method = rocm_aiter_ops.get_aiter_activation_type("situ")
else:
raise ValueError(f"Unsupported activation: {activation}")
if activation_method is None:
raise ValueError(f"AITER does not support activation: {activation}")
# All AITER Fused MoE kernels are expecting the following datatypes
topk_weights = topk_weights.to(torch.float32)
topk_ids = topk_ids.to(torch.int32)
# w8a8 per-channel quantization
if (
quant_config.per_act_token_quant
and apply_router_weight_on_input
and quant_config.use_fp8_w8a8
):
# AITER tkw1 kernel for FP8 models with `apply_router_weight_on_input`
# This applies topk_weights on the GEMM output of the first FC layer
# rather than the second FC.
assert topk_weights.dim() == 2, (
"`topk_weights` should be in shape (num_tokens, topk)"
)
assert topk_weights.shape[-1] == 1, (
"Only support topk=1 when `apply_router_weight_on_input` is True"
)
assert num_local_tokens is None, (
"AITER tkw1 kernel does not support `num_local_tokens`"
)
return rocm_aiter_ops.asm_moe_tkw1(
hidden_states,
w1,
w2,
topk_weights,
topk_ids,
fc1_scale=quant_config.w1_scale,
fc2_scale=quant_config.w2_scale,
fc1_smooth_scale=None,
fc2_smooth_scale=None,
a16=False,
per_tensor_quant_scale=None,
expert_mask=expert_mask,
activation_method=activation_method,
)
else:
quant_method = QuantMethod.NO.value
# mxfp4 i.e. w4a4, w4a16 uses BLOCK_1X32
# mxfp6 and mxfp8 are unsupported in AITER currently and use emulation instead
if quant_config.use_mxfp4_w4a4 or quant_config.use_mxfp4_w4a16:
quant_method = QuantMethod.BLOCK_1X32.value
# w8a8 block-scaled
if quant_config.block_shape is not None and quant_config.use_fp8_w8a8:
assert not apply_router_weight_on_input, (
"apply_router_weight_on_input is not supported for block scaled moe"
)
assert quant_config.w1_scale is not None
assert quant_config.w2_scale is not None
quant_method = QuantMethod.BLOCK_128x128.value
elif quant_config.use_fp8_w8a8 and quant_config.per_out_ch_quant:
quant_method = QuantMethod.PER_TOKEN.value
elif quant_config.use_fp8_w8a8:
# Currently only per tensor quantization method is enabled.
quant_method = QuantMethod.PER_TENSOR.value
if apply_router_weight_on_input:
assert topk_weights.dim() == 2, (
"`topk_weights` should be in shape (num_tokens, topk)"
)
_, topk = topk_weights.shape
assert topk == 1, (
"Only support topk=1 when `apply_router_weight_on_input` is True"
)
# Compute padding on-the-fly for CK MXFP4 kernels
hidden_pad = 0
intermediate_pad = 0
assert moe_config.hidden_dim_unpadded is not None
assert moe_config.intermediate_size_per_partition_unpadded is not None
hidden_pad = hidden_states.shape[1] - moe_config.hidden_dim_unpadded
intermediate_pad = (
(
moe_config.intermediate_size_per_partition
- moe_config.intermediate_size_per_partition_unpadded
)
if moe_config.intermediate_pad is None
else moe_config.intermediate_pad
)
# Round hidden_pad/intermediate_pad to match AITER's CK/FlyDSL MoE
# dispatch (currently pinned to v0.1.13.post1):
# https://github.com/ROCm/aiter/blob/v0.1.13.post1/aiter/fused_moe.py#L1073
# https://github.com/ROCm/aiter/blob/v0.1.13.post1/aiter/fused_moe.py#L1099
# TODO: Revisit this once we bump AITER to 0.1.15 with padding fixes
# for CK/FlyDSL MoE GEMM e.g. https://github.com/ROCm/aiter/pull/3401
# SITU's A16W4 FlyDSL kernel pads per gate/up half; pass through unrounded.
if activation != MoEActivation.SITU:
hidden_pad = hidden_pad // 128 * 128
intermediate_pad = (
intermediate_pad // 64 * 64 * (2 if moe_config.tp_size == 1 else 1)
)
# https://github.com/ROCm/aiter/pull/3123 specialized the AITER stage1 GEMMs
# for interleaved vs separated gate and up weights.
# For gpt-oss i.e. use_mxfp4_w4a16=True, the weights are shuffled by
# `rocm_aiter_ops.shuffle_weight_a16w4` in `oracle/mxfp4.py`,
# which always sets `is_guinterleave=True`.
# Hence, we pass in GateMode.INTERLEAVE to match the weight shuffling.
from aiter.ops.flydsl.moe_common import GateMode
gate_mode = ""
if activation == MoEActivation.SITU:
# SiTUv2 flydsl (VLLM_ROCM_USE_AITER_MOE_SITUV2=1) uses a4w4
# fp4 activations with separated gate/up weights (AITER #4463);
# default a16w4 SiTU also stays separated.
gate_mode = GateMode.SEPARATED.value
elif quant_config.use_mxfp4_w4a16:
gate_mode = GateMode.INTERLEAVE.value
elif activation_interleave is not None:
gate_mode = (
GateMode.INTERLEAVE.value
if activation_interleave
else GateMode.SEPARATED.value
)
return rocm_aiter_ops.fused_moe(
hidden_states,
w1,
w2,
topk_weights,
topk_ids,
expert_mask=expert_mask,
quant_method=quant_method,
activation_method=activation_method,
w1_scale=quant_config.w1_scale,
w2_scale=quant_config.w2_scale,
a1_scale=quant_config.a1_scale if a1q_scale is None else a1q_scale,
a2_scale=quant_config.a2_scale,
doweight_stage1=apply_router_weight_on_input,
num_local_tokens=num_local_tokens,
output_dtype=output_dtype,
hidden_pad=hidden_pad,
intermediate_pad=intermediate_pad,
gate_mode=gate_mode,
bias1=quant_config.w1_bias if quant_config.use_mxfp4_w4a16 else None,
bias2=quant_config.w2_bias if quant_config.use_mxfp4_w4a16 else None,
moe_sorting_dispatch_policy=moe_sorting_dispatch_policy,
swiglu_limit=(
0.0
if moe_config.swiglu_limit is None
else float(moe_config.swiglu_limit)
),
beta=moe_config.activation_situ_beta,
linear_beta=moe_config.activation_situ_linear_beta,
shared_w1=shared_w1,
shared_w2=shared_w2,
shared_w1_scale=shared_w1_scale,
shared_w2_scale=shared_w2_scale,
shared_expert_id=shared_expert_id,
)
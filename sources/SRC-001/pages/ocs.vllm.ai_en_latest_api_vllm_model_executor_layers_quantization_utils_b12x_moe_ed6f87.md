source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/b12x_moe/
lastmod: 2026-09-23

def prepare_nvfp4_moe_layer_for_b12x(
w13: torch.Tensor,
w13_scale: torch.Tensor,
w13_scale_2: torch.Tensor,
a13_scale: torch.Tensor,
w2: torch.Tensor,
w2_scale: torch.Tensor,
w2_scale_2: torch.Tensor,
a2_scale: torch.Tensor,
is_act_and_mul: bool,
reorder_w13: bool = False,
) -> tuple[
torch.Tensor,
torch.Tensor,
torch.Tensor,
torch.Tensor,
torch.Tensor,
torch.Tensor,
torch.Tensor,
torch.Tensor,
]:
"""Prepare b12x NVFP4 MoE weights and scales."""
num_experts = w13.shape[0]
a13_scale = _per_expert_scale(a13_scale, num_experts, "a13_scale")
a2_scale = _per_expert_scale(a2_scale, num_experts, "a2_scale")
if reorder_w13 and is_act_and_mul:
w13 = swap_w13_to_w31(w13)
w13_scale = swap_w13_to_w31(w13_scale)
if is_act_and_mul:
w13, w13_scale, w2, w2_scale = _pad_gated_weights(w13, w13_scale, w2, w2_scale)
w13_scale = swizzle_blockscale(w13_scale)
pad_size = w13_scale.size(1) - w13.size(1)
if pad_size > 0:
if is_act_and_mul:
raise RuntimeError("gated NVFP4 MoE padding must precede scale swizzling")
w13 = F.pad(w13, (0, 0, 0, pad_size))
w2 = F.pad(w2, (0, pad_size // 2, 0, 0))
w2_scale = F.pad(w2_scale, (0, pad_size // 16))
w2_scale = swizzle_blockscale(w2_scale)
return w13, w13_scale, w13_scale_2, a13_scale, w2, w2_scale, w2_scale_2, a2_scale
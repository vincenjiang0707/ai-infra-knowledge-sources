source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/xpu_moe/
lastmod: 2026-09-23

Bases: `XPUExperts`


W4A16 INT4-symmetric MoE backed by `xpu_fused_moe(is_int4=True)`

.

Weight layout when `is_int4=True`

(per `xpu_fused_moe`

docstring): w13: [num_experts, 2*inter_size, hidden_size] contiguous int4-packed w13_scales: [num_experts, 2*inter_size, hidden_size // group_size] w2: [num_experts, hidden_size, inter_size] contiguous int4-packed w2_scales: [num_experts, hidden_size, inter_size // group_size]

Pairs with `INCXPULinearMethod`

for the linear layers; together they cover full-attn + MoE on Intel XPU end-to-end without IPEX.

## Source code in `vllm/model_executor/layers/fused_moe/experts/xpu_moe.py`


| class XPUExpertsWNA16(XPUExperts):
"""W4A16 INT4-symmetric MoE backed by `xpu_fused_moe(is_int4=True)`.
Weight layout when `is_int4=True` (per `xpu_fused_moe` docstring):
w13: [num_experts, 2*inter_size, hidden_size] contiguous int4-packed
w13_scales: [num_experts, 2*inter_size, hidden_size // group_size]
w2: [num_experts, hidden_size, inter_size] contiguous int4-packed
w2_scales: [num_experts, hidden_size, inter_size // group_size]
Pairs with `INCXPULinearMethod` for the linear layers; together they
cover full-attn + MoE on Intel XPU end-to-end without IPEX.
"""
def __init__(
self,
moe_config: FusedMoEConfig,
quant_config: FusedMoEQuantConfig,
max_num_tokens: int | None = None,
num_dispatchers: int | None = None,
):
super().__init__(
moe_config,
quant_config,
max_num_tokens,
num_dispatchers,
)
@staticmethod
def _supports_quant_scheme(
weight_key: QuantKey | None,
activation_key: QuantKey | None,
) -> bool:
return (weight_key, activation_key) in (
(kInt4Static, None),
(kInt4Static32, None),
)
|
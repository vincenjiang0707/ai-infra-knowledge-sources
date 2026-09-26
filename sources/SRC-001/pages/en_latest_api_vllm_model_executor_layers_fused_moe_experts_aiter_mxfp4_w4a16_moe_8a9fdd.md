source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/aiter_mxfp4_w4a16_moe/
lastmod: 2026-09-24

def _aiter_w4a16_silu_via_a8w4(
hidden_states: torch.Tensor,
w1_data,
w2_data,
w1_wscale,
w2_wscale,
w1_bias,
w2_bias,
routing_data,
gather_idx,
scatter_idx,
gammas,
apply_router_weight_on_input: bool,
swiglu_limit: float,
unpadded_N_w1,
unpadded_K_w1,
unpadded_N_w2,
unpadded_K_w2,
) -> torch.Tensor:
"""MXFP4 w4a16 MoE with a SILU (concatenated ``[gate | up]``) activation."""
from aiter.ops.triton.fusions.fused_clamp_act_mul import fused_clamp_act_mul
from aiter.ops.triton.quant import dynamic_mxfp8_quant
try:
from aiter.ops.triton.moe.moe_op_gemm_a8w4 import moe_gemm_a8w4
except ImportError:
from aiter.ops.triton.moe_op_gemm_a8w4 import moe_gemm_a8w4
from vllm.model_executor.layers.quantization.utils.mxfp4_utils import (
should_use_cdna4_mx_scale_swizzle,
)
swz = "CDNA4_SCALE" if should_use_cdna4_mx_scale_swizzle() else None
quant_dtype = torch.float8_e4m3fn
g1_gammas = gammas if apply_router_weight_on_input else None
g2_gammas = None if apply_router_weight_on_input else gammas
hidden_q, a1_scale = dynamic_mxfp8_quant(hidden_states, quant_dtype=quant_dtype)
raw_gate_up = moe_gemm_a8w4(
hidden_q,
w1_data,
a1_scale,
w1_wscale,
None,
None,
w1_bias,
routing_data,
gather_indx=gather_idx,
gammas=g1_gammas,
swizzle_mx_scale=swz,
out_dtype=torch.bfloat16,
apply_swiglu=False,
unpadded_N=unpadded_N_w1,
unpadded_K=unpadded_K_w1,
)
if unpadded_N_w1 is not None:
raw_gate_up = raw_gate_up[:, :unpadded_N_w1]
# convert interleaved -> chunked for kernel
gate, up = raw_gate_up[:, ::2], raw_gate_up[:, 1::2]
raw_gate_up = torch.cat((gate, up), dim=1).contiguous()
interim_fp8, a2_scale = fused_clamp_act_mul(
raw_gate_up,
swiglu_limit=swiglu_limit,
activation="silu",
dtype_quant=quant_dtype,
scale_dtype_fmt="ue8m0",
quant_block_size=32,
)
out = moe_gemm_a8w4(
interim_fp8,
w2_data,
a2_scale,
w2_wscale,
None,
None,
w2_bias,
routing_data,
scatter_indx=scatter_idx,
gammas=g2_gammas,
swizzle_mx_scale=swz,
unpadded_N=unpadded_N_w2,
unpadded_K=unpadded_K_w2,
)
return out
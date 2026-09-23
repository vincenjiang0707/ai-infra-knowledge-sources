source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/mxfp8_native_moe/
lastmod: 2026-09-23

Native MXFP8 (1x32 block, E8M0 scale) MoE for AMD CDNA4 (gfx950) via Triton `tl.dot_scaled`

(hardware microscaling matmul).

The expert GEMMs consume the FP8 E4M3 weights and their E8M0 block scales directly (no dequant-to-BF16), and activations are MXFP8-quantized per token. On CDNA4 `dot_scaled`

maps to the native MX matrix-core ops; on other archs Triton upcasts to BF16 (so this stays correct, just not faster) — but the oracle only selects this path on gfx950 and routes everything else to the BF16 `Mxfp8EmulationTritonExperts`

fallback.

Structure mirrors vLLM's `fused_moe_kernel`

: tokens are sorted by expert (`moe_align_block_size`

); each program computes a `[BLOCK_M, BLOCK_N]`

tile for one expert, accumulating over K with `dot_scaled`

. SwiGLU-OAI activation and the top-k weighted reduction run in PyTorch between/after the two GEMMs.

Classes:

##

`Mxfp8NativeTritonExperts`


Bases: [Mxfp8TritonExpertsBase](../mxfp8_emulation_moe/#vllm.model_executor.layers.fused_moe.experts.mxfp8_emulation_moe.Mxfp8TritonExpertsBase)


Native MXFP8 MoE (CDNA4 `dot_scaled`

) on gfx950.

## Source code in `vllm/model_executor/layers/fused_moe/experts/mxfp8_native_moe.py`


| class Mxfp8NativeTritonExperts(Mxfp8TritonExpertsBase):
"""Native MXFP8 MoE (CDNA4 ``dot_scaled``) on gfx950."""
@property
def quant_dtype(self) -> torch.dtype | str | None:
return self.quant_config.quant_dtype
@property
def block_shape(self) -> list[int] | None:
return self.quant_config.block_shape
@property
def expects_unquantized_inputs(self) -> bool:
# Activations are MXFP8-quantized inside ``fused_moe_mxfp8_native``.
return True
@staticmethod
def _supports_current_device() -> bool:
return current_platform.is_rocm() and current_platform.supports_mx()
def apply(
self,
output: torch.Tensor,
hidden_states: torch.Tensor,
w1: torch.Tensor,
w2: torch.Tensor,
topk_weights: torch.Tensor,
topk_ids: torch.Tensor,
activation,
global_num_experts: int,
expert_map: torch.Tensor | None,
a1q_scale: torch.Tensor | None,
a2_scale: torch.Tensor | None,
workspace13: torch.Tensor,
workspace2: torch.Tensor,
expert_tokens_meta: mk.ExpertTokensMetadata | None,
apply_router_weight_on_input: bool,
):
activation_config = self.activation_config
out = fused_moe_mxfp8_native(
hidden_states,
w1,
self.w1_scale_val,
w2,
self.w2_scale_val,
topk_weights,
topk_ids,
alpha=activation_config.alpha,
beta=activation_config.beta,
limit=activation_config.clamp_limit,
global_num_experts=global_num_experts,
expert_map=expert_map,
)
output.copy_(out)
|


##

`_select_cfg(M, N, K, block_m)`


Pick the launch config from host constants only (M=num_valid_tokens, N, K, block_m) — graph-capture safe (no GPU-scalar branch).

## Source code in `vllm/model_executor/layers/fused_moe/experts/mxfp8_native_moe.py`


| def _select_cfg(M, N, K, block_m):
"""Pick the launch config from host constants only (M=num_valid_tokens, N, K,
block_m) — graph-capture safe (no GPU-scalar branch)."""
# Per-regime winners (measured, isolated cuda-event A/B on gfx950, GPU 3):
# BLOCK_K=256 (fewer K-iters + bigger MX scale-load coalesced with the dot),
# num_stages=2 (software-pipeline overlaps the E8M0 scale-load with the scaled
# MFMA), GROUP_SIZE_M=4 (XCD-friendly swizzle that keeps each touched expert's
# A rows + B column-tiles L2/MALL-resident across its N-tiles -> kills the
# redundant A re-read). num_warps stays 8 (wave64 here did NOT spill: VGPR fits
# and 4 warps was neutral/worse in measurement). BLOCK_K must be a power of two
# and divide K (K=6144 and K=768 are both multiples of 256).
BLOCK_K = 256 if K % 256 == 0 else 128
return {
"BLOCK_N": 128,
"BLOCK_K": BLOCK_K,
"GROUP_SIZE_M": 4,
"num_warps": 8,
"num_stages": 2,
}
|
source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/determinism/batch_invariant_configs/
lastmod: 2026-09-24

Select a config for the XPU descriptor matmul from shape and dtype.

The default 128×128×64 config is optimized for large square-ish GEMMs but wastes resources on skinny shapes (small M during decode, or very tall/thin matrices during prefill). Shape-dependent tuning closes the gap with oneDNN.

Only BLOCK_SIZE_M/N and the launch parameters vary with M; dtype alone decides BLOCK_SIZE_K, so the K-reduction order never depends on batch size.

## Source code in `vllm/model_executor/determinism/batch_invariant_configs.py`


| def _get_descriptor_matmul_config(
M: int, N: int, K: int, dtype: torch.dtype
) -> dict[str, int]:
"""Select a config for the XPU descriptor matmul from shape and dtype.
The default 128×128×64 config is optimized for large square-ish GEMMs but
wastes resources on skinny shapes (small M during decode, or very tall/thin
matrices during prefill). Shape-dependent tuning closes the gap with oneDNN.
Only BLOCK_SIZE_M/N and the launch parameters vary with M; dtype alone
decides BLOCK_SIZE_K, so the K-reduction order never depends on batch size.
"""
# fp32 uses smaller BLOCK_SIZE_K due to register pressure
block_k = 32 if dtype == torch.float32 else 64
if M <= 16:
# Decode: M=1-16. Tiny M means most of a 128-row tile is wasted.
# Use small M-block, wide N-block to maximize useful work per tile.
return {
"BLOCK_SIZE_M": 16,
"BLOCK_SIZE_N": 256,
"BLOCK_SIZE_K": block_k,
"GROUP_SIZE_M": 1,
"num_stages": 4,
"num_warps": 8,
}
elif M <= 64:
# Small batch decode or very short prefill.
return {
"BLOCK_SIZE_M": 32,
"BLOCK_SIZE_N": 128,
"BLOCK_SIZE_K": block_k,
"GROUP_SIZE_M": 4,
"num_stages": 4,
"num_warps": 8,
}
else:
# Medium and large prefill (M > 64). 64×128 tiles provide the best
# balance of register pressure vs parallelism on Intel XPU.
# M=2048, N=4096 → 32×32 = 1024 tiles, well above ~160 compute units.
return {
"BLOCK_SIZE_M": 64,
"BLOCK_SIZE_N": 128,
"BLOCK_SIZE_K": block_k,
"GROUP_SIZE_M": 8,
"num_stages": 3,
"num_warps": 8,
}
|
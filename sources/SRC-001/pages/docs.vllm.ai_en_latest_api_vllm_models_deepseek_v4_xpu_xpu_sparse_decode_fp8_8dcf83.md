source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/xpu/xpu_sparse_decode_fp8/
lastmod: 2026-09-23

def xpu_sparse_decode_fp8(
q: torch.Tensor, # [num_tokens, num_heads, head_dim]
kv_cache: torch.Tensor | None, # [num_blocks, block_size, head_bytes] uint8
swa_kv_cache: torch.Tensor, # [num_blocks, swa_block_size, head_bytes] uint8
swa_only: bool,
topk_indices: torch.Tensor | None, # [num_tokens, 1, topk] global slot IDs
topk_lens: torch.Tensor | None,
swa_indices: torch.Tensor, # [num_tokens, 1, swa_k] global slot IDs
swa_lens: torch.Tensor,
attn_sink: torch.Tensor,
softmax_scale: float,
head_dim: int,
nope_head_dim: int,
rope_head_dim: int,
out: torch.Tensor, # [num_tokens, num_heads, head_dim]
) -> None:
"""XPU decode: dequant FP8 pages to BF16, then BF16 sparse MLA attention.
Keeps external FP8 KV cache layout identical to CUDA/ROCm.
Performance is slower due to on-the-fly dequant, but correctness is
guaranteed by reusing the validated BF16 attention kernel.
"""
num_tokens = q.shape[0]
device = q.device
# Determine max topk and swa widths
if not swa_only and topk_indices is not None:
topk_idx_2d = (
topk_indices.squeeze(1) if topk_indices.dim() == 3 else topk_indices
)
max_topk = topk_idx_2d.shape[1]
else:
topk_idx_2d = None
max_topk = 0
swa_idx_2d = swa_indices.squeeze(1) if swa_indices.dim() == 3 else swa_indices
max_swa = swa_idx_2d.shape[1]
K_total = max_topk + max_swa
# Allocate flat workspace: [num_tokens * K_total, 512] bf16
workspace = torch.empty(
(num_tokens * K_total, OUTPUT_DIM), dtype=torch.bfloat16, device=device
)
ws_3d = workspace.view(num_tokens, K_total, OUTPUT_DIM)
# Dequant+gather topk slots from compressed cache
if not swa_only and topk_idx_2d is not None and kv_cache is not None:
topk_flat = topk_idx_2d.reshape(-1).to(torch.int32)
topk_buf = torch.empty(
(num_tokens * max_topk, OUTPUT_DIM), dtype=torch.bfloat16, device=device
)
compressed_block_size = kv_cache.shape[1]
dequant_gather_slots(topk_buf, kv_cache, topk_flat, compressed_block_size)
ws_3d[:, :max_topk, :] = topk_buf.view(num_tokens, max_topk, OUTPUT_DIM)
# Dequant+gather SWA slots
swa_flat = swa_idx_2d.reshape(-1).to(torch.int32)
swa_buf = torch.empty(
(num_tokens * max_swa, OUTPUT_DIM), dtype=torch.bfloat16, device=device
)
swa_block_size = swa_kv_cache.shape[1]
dequant_gather_slots(swa_buf, swa_kv_cache, swa_flat, swa_block_size)
ws_3d[:, max_topk:, :] = swa_buf.view(num_tokens, max_swa, OUTPUT_DIM)
# Build combined indices into the flat workspace and combined lengths.
# Workspace layout per token t: [topk_0..topk_{max_topk-1}, swa_0..swa_{max_swa-1}]
# Flat index for token t, position p = t * K_total + p
#
# IMPORTANT: The attention kernel uses combined_lens as a position cutoff —
# it only reads indices[0..combined_lens-1]. So indices must be PACKED
# contiguously: [valid_topk_indices..., valid_swa_indices..., -1 padding...]
if not swa_only and topk_lens is not None:
combined_lens = (topk_lens + swa_lens).to(torch.int32)
else:
combined_lens = swa_lens.to(torch.int32)
max_combined = int(combined_lens.max().item()) if combined_lens.numel() > 0 else 0
# Round up to BLOCK_N=16 alignment for kernel efficiency
_BLOCK_N = 16
max_combined_padded = ((max_combined + _BLOCK_N - 1) // _BLOCK_N) * _BLOCK_N
# Build packed index table: [num_tokens, max_combined_padded]
# Each token t: [topk_0..topk_{tlen-1}, swa_0..swa_{slen-1}, -1 padding]
# Vectorized: for each token, topk indices are t*K_total + 0..tlen-1,
# swa indices are t*K_total + max_topk + 0..slen-1
combined_indices = torch.full(
(num_tokens, max_combined_padded),
fill_value=-1,
dtype=torch.int32,
device=device,
)
token_offsets = (
torch.arange(num_tokens, device=device, dtype=torch.int32) * K_total
) # [B]
if not swa_only and topk_lens is not None:
# Pack topk: for each token, write t*K_total + 0..tlen-1 at positions 0..tlen-1
max_tlen = int(topk_lens.max().item())
topk_range = torch.arange(max_tlen, device=device, dtype=torch.int32).unsqueeze(
0
)
topk_valid = topk_range < topk_lens.unsqueeze(1)
topk_ws_indices = token_offsets.unsqueeze(1) + topk_range
combined_indices[:, :max_tlen] = torch.where(
topk_valid,
topk_ws_indices,
torch.tensor(-1, dtype=torch.int32, device=device),
)
# Pack swa after topk: positions tlen..tlen+slen-1
# Since tlen varies per token, we need per-token offset
swa_range = torch.arange(max_swa, device=device, dtype=torch.int32).unsqueeze(0)
swa_valid = swa_range < swa_lens.unsqueeze(1)
swa_ws_indices = token_offsets.unsqueeze(1) + max_topk + swa_range
# Write at position topk_lens[t] + swa_pos for each token
for t_idx in range(num_tokens):
tlen = int(topk_lens[t_idx].item())
slen = int(swa_lens[t_idx].item())
combined_indices[t_idx, tlen : tlen + slen] = swa_ws_indices[t_idx, :slen]
else:
# SWA-only: pack swa indices at positions 0..slen-1
# Use min(max_swa, max_combined_padded) because combined_indices only
# has max_combined_padded columns, and all valid entries fit within it.
effective_swa = min(max_swa, max_combined_padded)
swa_range = torch.arange(
effective_swa, device=device, dtype=torch.int32
).unsqueeze(0)
swa_valid = swa_range < swa_lens.unsqueeze(1)
swa_ws_indices = token_offsets.unsqueeze(1) + swa_range # max_topk=0
combined_indices[:, :effective_swa] = torch.where(
swa_valid,
swa_ws_indices,
torch.tensor(-1, dtype=torch.int32, device=device),
)
# Call BF16 sparse MLA kernel
out_attn, _, _ = triton_bf16_mla_sparse_interface(
q=q,
kv=workspace.unsqueeze(1),
indices=combined_indices.unsqueeze(1),
sm_scale=softmax_scale,
d_v=q.shape[-1],
block_dpe=0,
)
out.copy_(out_attn)
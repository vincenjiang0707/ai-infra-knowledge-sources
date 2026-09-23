source: https://docs.vllm.ai/en/latest/api/vllm/models/minimax_m3/common/vision_tower/
lastmod: 2026-09-23

class MiniMaxVLVisionTransformer(nn.Module):
"""CLIP-based ViT with 3D RoPE (t/h/w decomposed).
Faithfully mirrors the reference ``MiniMaxVLVisionTransformer``.
FLASHINFER backend is not supported; standard flash-attn is used.
"""
def __init__(
self,
config: PretrainedConfig,
num_hidden_layers_override: int | None = None,
require_post_norm: bool | None = None,
quant_config: QuantizationConfig | None = None,
prefix: str = "",
) -> None:
super().__init__()
compression = config.img_token_compression_config
self.spatial_merge_size: int = compression.get("spatial_merge_size", 2)
self.temporal_patch_size: int = compression.get("temporal_patch_size", 2)
self.vision_segment_max_frames: int | None = getattr(
config, "vision_segment_max_frames", None
)
self.use_data_parallel = is_vit_use_data_parallel()
embed_dim = config.hidden_size
head_dim = embed_dim // config.num_attention_heads
# Backend selection + sharding info for building encoder metadata.
# Defaults to FLASH_ATTN on SM80+; --mm-encoder-attn-backend FLASHINFER
# selects the cuDNN ViT prefill path.
self.hidden_size = embed_dim
self.tp_size = (
1
if self.use_data_parallel
else parallel_state.get_tensor_model_parallel_world_size()
)
self.attn_backend = get_vit_attn_backend(
head_size=head_dim, dtype=torch.get_default_dtype()
)
rope_dims = 2 * (head_dim // 2)
# Split rope dims evenly across t/h/w (same formula as the reference)
self.t_dim = int(2 * ((rope_dims // 3) // 2))
self.h_dim = int(2 * ((rope_dims // 3) // 2))
self.w_dim = int(2 * ((rope_dims // 3) // 2))
# rot_dim = t_dim + h_dim + w_dim (may be < head_dim)
rope_theta: float = getattr(config, "rope_theta", 10000.0)
inv_freq_t = 1.0 / (
rope_theta
** (torch.arange(0, self.t_dim, 2, dtype=torch.float32) / self.t_dim)
)
inv_freq_h = 1.0 / (
rope_theta
** (torch.arange(0, self.h_dim, 2, dtype=torch.float32) / self.h_dim)
)
inv_freq_w = 1.0 / (
rope_theta
** (torch.arange(0, self.w_dim, 2, dtype=torch.float32) / self.w_dim)
)
self.register_buffer("inv_freq_t", inv_freq_t, persistent=False)
self.register_buffer("inv_freq_h", inv_freq_h, persistent=False)
self.register_buffer("inv_freq_w", inv_freq_w, persistent=False)
self.embeddings = MiniMaxVLPatchEmbed(config)
self.pre_layrnorm = nn.LayerNorm(embed_dim, eps=config.layer_norm_eps)
n_layers = config.num_hidden_layers
if num_hidden_layers_override is None:
num_hidden_layers_override = n_layers
self.encoder = MiniMaxVLEncoder(
config=config,
num_hidden_layers_override=num_hidden_layers_override,
quant_config=quant_config,
prefix=f"{prefix}.encoder",
)
if require_post_norm is None:
require_post_norm = num_hidden_layers_override == n_layers
self.post_layernorm = (
nn.LayerNorm(embed_dim, eps=config.layer_norm_eps)
if require_post_norm
else None
)
# out_hidden_size needed by run_dp_sharded_mrope_vision_model
self.out_hidden_size = embed_dim
# ── RoPE helpers ─────────────────────────────────────────────────────
def _get_3d_rope_embed(
self, grid_t: int, grid_h: int, grid_w: int, spatial_merge_size: int
) -> torch.Tensor:
"""Compute 3D RoPE frequencies for a single (T, H, W) grid.
Returns (T*H*W, half_rot_dim) on the same device as inv_freq buffers.
Mirrors the reference ``_get_3d_rope_embed`` exactly.
"""
tokens_per_frame = grid_h * grid_w
tpos_ids = (
torch.arange(grid_t, device=self.inv_freq_t.device)
.unsqueeze(1)
.expand(-1, tokens_per_frame)
.flatten()
)
hpos_ids = (
torch.arange(grid_h, device=self.inv_freq_h.device)
.unsqueeze(1)
.expand(-1, grid_w)
.reshape(
grid_h // spatial_merge_size,
spatial_merge_size,
grid_w // spatial_merge_size,
spatial_merge_size,
)
.permute(0, 2, 1, 3)
.unsqueeze(0)
.expand(grid_t, -1, -1, -1, -1)
.flatten()
)
wpos_ids = (
torch.arange(grid_w, device=self.inv_freq_w.device)
.unsqueeze(0)
.expand(grid_h, -1)
.reshape(
grid_h // spatial_merge_size,
spatial_merge_size,
grid_w // spatial_merge_size,
spatial_merge_size,
)
.permute(0, 2, 1, 3)
.unsqueeze(0)
.expand(grid_t, -1, -1, -1, -1)
.flatten()
)
max_t = max(grid_t, 1)
max_hw = max(grid_h, grid_w)
seq_t = torch.arange(
max_t, device=self.inv_freq_t.device, dtype=self.inv_freq_t.dtype
)
seq_hw = torch.arange(
max_hw, device=self.inv_freq_h.device, dtype=self.inv_freq_h.dtype
)
freqs_t = torch.outer(seq_t, self.inv_freq_t) # (max_t, t_dim/2)
freqs_h = torch.outer(seq_hw, self.inv_freq_h) # (max_hw, h_dim/2)
freqs_w = torch.outer(seq_hw, self.inv_freq_w) # (max_hw, w_dim/2)
return torch.cat(
[freqs_t[tpos_ids], freqs_h[hpos_ids], freqs_w[wpos_ids]], dim=-1
) # (T*H*W, half_rot_dim)
def _get_rope_embed_3d(
self, grid_thw: list[list[int]], spatial_merge_size: int
) -> torch.Tensor:
embeds = [
self._get_3d_rope_embed(t, h, w, spatial_merge_size) for t, h, w in grid_thw
]
return torch.cat(embeds, dim=0) # (total_N, half_rot_dim)
# ── Frame-limit helper (mirrors the reference) ───────────────────────
def _apply_max_frames_limit(self, grid_thw: list[list[int]]) -> list[list[int]]:
if self.vision_segment_max_frames is None:
return grid_thw
max_f = self.vision_segment_max_frames
out: list[list[int]] = []
for t, h, w in grid_thw:
if t <= max_f:
out.append([t, h, w])
else:
for i in range(0, t, max_f):
out.append([min(max_f, t - i), h, w])
return out
# ── Forward ──────────────────────────────────────────────────────────
def forward(
self,
pixel_values: torch.Tensor,
grid_thw: list[list[int]],
) -> torch.Tensor:
# pixel_values: (total_N, C * temporal_patch_size * patch_size²)
# Output: (total_N, hidden_size)
hidden = self.embeddings(pixel_values) # (total_N, hidden_size)
hidden = self.pre_layrnorm(hidden)
limited = self._apply_max_frames_limit(grid_thw)
# Token-level cumulative sequence lengths (one segment per limited grid).
lens = [t * h * w for t, h, w in limited]
cu_seqlens_np = np.zeros(len(lens) + 1, dtype=np.int32)
np.cumsum(np.array(lens, dtype=np.int32), out=cu_seqlens_np[1:])
# Backend-specific encoder metadata. For FLASH_ATTN this returns the raw
# token cu_seqlens, the max segment length, and sequence_lengths=None;
# for FLASHINFER (cuDNN) it repacks cu_seqlens into element-offset
# indptrs, buckets max_seqlen, and builds padded per-sequence lengths.
sequence_lengths = MMEncoderAttention.maybe_compute_seq_lens(
self.attn_backend, cu_seqlens_np, hidden.device
)
max_seqlen = torch.tensor(
MMEncoderAttention.compute_max_seqlen(self.attn_backend, cu_seqlens_np),
dtype=torch.int32,
)
cu_seqlens = MMEncoderAttention.maybe_recompute_cu_seqlens(
self.attn_backend,
cu_seqlens_np,
self.hidden_size,
self.tp_size,
hidden.device,
)
# 3D RoPE: (total_N, half_rot_dim); ApplyRotaryEmb expands internally
freqs = self._get_rope_embed_3d(limited, self.spatial_merge_size)
freqs = freqs.to(device=hidden.device)
# Keep cos/sin in fp32; ApplyRotaryEmb(enable_fp32_compute=True) runs the
# rotation in fp32 to match the reference precision.
rotary_cos, rotary_sin = freqs.cos(), freqs.sin()
# Encoder expects (N, 1, hidden_size) — add batch dim
hidden = hidden.unsqueeze(1)
# On ROCm, the flash_attn Triton rotary kernel can fail with
# hipErrorInvalidValue when seqlen is very large, e.g. 192k video
# tokens; pass per-segment lengths so RoPE can be applied in chunks.
# On other platforms leave it None -> single-kernel fast path, so the
# NVIDIA/CUDA code path is unchanged.
rotary_segment_lengths = lens if current_platform.is_rocm() else None
hidden = self.encoder(
hidden,
cu_seqlens,
rotary_cos,
rotary_sin,
max_seqlen,
rotary_segment_lengths,
sequence_lengths=sequence_lengths,
)
hidden = hidden.squeeze(1) # back to (total_N, hidden_size)
if self.post_layernorm is not None:
hidden = self.post_layernorm(hidden)
return hidden
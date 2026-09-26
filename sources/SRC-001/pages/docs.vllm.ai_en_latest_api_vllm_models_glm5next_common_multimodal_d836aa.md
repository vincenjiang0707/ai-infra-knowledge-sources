source: https://docs.vllm.ai/en/latest/api/vllm/models/glm5next/common/multimodal/
lastmod: 2026-09-24

class Glm5NextVisionTransformer(nn.Module):
# Stacked-weight remap for the GLM-OCR/GLM-4V vision checkpoint layout.
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_stacked={
".attn.q.": (".attn.qkv.", "q"),
".attn.k.": (".attn.qkv.", "k"),
".attn.v.": (".attn.qkv.", "v"),
".gate_proj": (".gate_up_proj", 0),
".up_proj": (".gate_up_proj", 1),
}
)
def __init__(
self,
text_config, # noqa: ANN001
vision_config,
norm_eps: float = 1e-6,
quant_config: QuantizationConfig | None = None,
prefix: str = "",
) -> None:
super().__init__()
use_data_parallel = is_vit_use_data_parallel()
self.tp_size = (
1 if use_data_parallel else get_tensor_model_parallel_world_size()
)
patch_size = vision_config.patch_size
temporal_patch_size = vision_config.temporal_patch_size
in_channels = vision_config.in_channels
depth = vision_config.depth
self.hidden_size = vision_config.hidden_size
self.num_heads = vision_config.num_heads
self.patch_size = vision_config.patch_size
self.spatial_merge_size = vision_config.spatial_merge_size
self.out_hidden_size = vision_config.out_hidden_size
swiglu_limit = vision_config.swiglu_limit
if swiglu_limit is None:
swiglu_limit = text_config.swiglu_limit
assert swiglu_limit is not None, (
"GLM-5.3-Flash vision requires swiglu_limit (vision_config or text_config)"
)
# Single construction pass — no abs-pos embeddings / post-conv norm (OCR delta).
self.patch_embed = Glm5NextVisionPatchEmbed(
patch_size=patch_size,
temporal_patch_size=temporal_patch_size,
in_channels=in_channels,
hidden_size=self.hidden_size,
)
norm_layer = partial(RMSNorm, eps=norm_eps)
head_dim = self.hidden_size // self.num_heads
self.rotary_pos_emb = get_rope(
head_size=head_dim,
max_position=8192,
is_neox_style=True,
rope_parameters={"partial_rotary_factor": 0.5},
)
self.blocks = nn.ModuleList(
[
Glm5NextVisionBlock(
dim=self.hidden_size,
num_heads=self.num_heads,
mlp_hidden_dim=vision_config.intermediate_size,
swiglu_limit=swiglu_limit,
norm_layer=norm_layer,
quant_config=quant_config,
prefix=f"{prefix}.blocks.{layer_idx}",
)
for layer_idx in range(depth)
]
)
# GLM-5.3-Flash merger bottleneck width.
self.merger = Glm5NextPatchMerger(
d_model=vision_config.out_hidden_size,
context_dim=vision_config.projection_intermediate_size,
swiglu_limit=swiglu_limit,
quant_config=quant_config,
bias=False,
prefix=f"{prefix}.merger",
)
self.downsample = Conv2dLayer(
in_channels=vision_config.hidden_size,
out_channels=vision_config.out_hidden_size,
kernel_size=vision_config.spatial_merge_size,
stride=vision_config.spatial_merge_size,
)
self.post_layernorm = RMSNorm(
vision_config.hidden_size, eps=vision_config.rms_norm_eps
)
self.attn_backend = get_vit_attn_backend(
head_size=head_dim,
dtype=torch.get_default_dtype(),
)
@property
def dtype(self) -> torch.dtype:
return self.patch_embed.proj.weight.dtype
@property
def device(self) -> torch.device:
return self.patch_embed.proj.weight.device
def rot_pos_emb(
self, grid_thw: list[list[int]]
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
pos_ids = []
for t, h, w in grid_thw:
hpos_ids = torch.arange(h).unsqueeze(1).expand(-1, w)
wpos_ids = torch.arange(w).unsqueeze(0).expand(h, -1)
hpos_ids = (
hpos_ids.reshape(
h // self.spatial_merge_size,
self.spatial_merge_size,
w // self.spatial_merge_size,
self.spatial_merge_size,
)
.permute(0, 2, 1, 3)
.flatten()
)
wpos_ids = (
wpos_ids.reshape(
h // self.spatial_merge_size,
self.spatial_merge_size,
w // self.spatial_merge_size,
self.spatial_merge_size,
)
.permute(0, 2, 1, 3)
.flatten()
)
pos_ids.append(torch.stack([hpos_ids, wpos_ids], dim=-1).repeat(t, 1))
pos_ids = torch.cat(pos_ids, dim=0)
max_grid_size = max(max(h, w) for _, h, w in grid_thw)
cos, sin = self.rotary_pos_emb.get_cos_sin(max_grid_size)
pos_ids = pos_ids.to(cos.device, non_blocking=True)
cos_combined = cos[pos_ids].flatten(1)
sin_combined = sin[pos_ids].flatten(1)
return cos_combined, sin_combined, pos_ids
def compute_attn_mask_seqlen(
self,
cu_seqlens: torch.Tensor,
) -> torch.Tensor | None:
max_seqlen = None
if self.attn_backend in {
AttentionBackendEnum.FLASH_ATTN,
AttentionBackendEnum.ROCM_AITER_FA,
AttentionBackendEnum.TRITON_ATTN,
}:
max_seqlen = (cu_seqlens[1:] - cu_seqlens[:-1]).max()
return max_seqlen
def prepare_encoder_metadata(
self,
grid_thw_list: list[list[int]],
*,
max_batch_size: int | None = None,
max_frames_per_batch: int | None = None,
max_seqlen_override: int | None = None,
device: torch.device | None = None,
) -> dict[str, torch.Tensor | None]:
"""Compute encoder metadata for eager and CUDA graph execution."""
if device is None:
device = self.device
metadata: dict[str, torch.Tensor | None] = {}
rotary_cos, rotary_sin, _ = self.rot_pos_emb(grid_thw_list)
metadata["rotary_pos_emb_cos"] = rotary_cos
metadata["rotary_pos_emb_sin"] = rotary_sin
grid_thw_np = np.array(grid_thw_list, dtype=np.int32)
patches_per_frame = grid_thw_np[:, 1] * grid_thw_np[:, 2]
cu_seqlens = np.repeat(patches_per_frame, grid_thw_np[:, 0]).cumsum(
dtype=np.int32
)
cu_seqlens = np.concatenate([np.zeros(1, dtype=np.int32), cu_seqlens])
pad_to = (
max_frames_per_batch if max_frames_per_batch is not None else max_batch_size
)
if pad_to is not None:
num_seqs = len(cu_seqlens) - 1
if num_seqs < pad_to:
cu_seqlens = np.concatenate(
[
cu_seqlens,
np.full(
pad_to - num_seqs,
cu_seqlens[-1],
dtype=np.int32,
),
]
)
metadata["sequence_lengths"] = MMEncoderAttention.maybe_compute_seq_lens(
self.attn_backend, cu_seqlens, device
)
if max_seqlen_override is not None:
max_seqlen_val = max_seqlen_override
else:
max_seqlen_val = MMEncoderAttention.compute_max_seqlen(
self.attn_backend, cu_seqlens
)
metadata["max_seqlen"] = torch.tensor(max_seqlen_val, dtype=torch.int32)
metadata["cu_seqlens"] = MMEncoderAttention.maybe_recompute_cu_seqlens(
self.attn_backend,
cu_seqlens,
self.hidden_size,
self.tp_size,
device,
)
return metadata
def forward(
self,
x: torch.Tensor,
grid_thw: torch.Tensor | list[list[int]],
*,
encoder_metadata: dict[str, torch.Tensor] | None = None,
) -> torch.Tensor:
# patchify
x = x.to(device=self.device, dtype=self.dtype)
x = self.patch_embed(x)
if encoder_metadata is not None:
# Encoder CUDA-graph path (PR #49852): rotary/cu_seqlens/max_seqlen are
# precomputed by prepare_encoder_metadata (which uses rot_pos_emb exactly
# as the eager rebuild does), so reuse them and skip the per-call CPU
# rebuild (the low-GPU-util culprit on multimodal workloads).
rotary_pos_emb_cos = encoder_metadata["rotary_pos_emb_cos"]
rotary_pos_emb_sin = encoder_metadata["rotary_pos_emb_sin"]
cu_seqlens = encoder_metadata["cu_seqlens"]
max_seqlen = encoder_metadata["max_seqlen"]
else:
if isinstance(grid_thw, list):
grid_thw = torch.tensor(grid_thw, dtype=torch.int32)
rotary_pos_emb_cos, rotary_pos_emb_sin, _ = self.rot_pos_emb(grid_thw)
cu_seqlens = torch.repeat_interleave(
grid_thw[:, 1] * grid_thw[:, 2], grid_thw[:, 0]
).cumsum(dim=0, dtype=torch.int32)
cu_seqlens = torch.cat([cu_seqlens.new_zeros(1), cu_seqlens])
cu_seqlens = cu_seqlens.to(self.device, non_blocking=True)
max_seqlen = self.compute_attn_mask_seqlen(cu_seqlens)
# transformers
x = x.unsqueeze(1)
for blk in self.blocks:
x = blk(
x,
cu_seqlens=cu_seqlens,
rotary_pos_emb_cos=rotary_pos_emb_cos,
rotary_pos_emb_sin=rotary_pos_emb_sin,
max_seqlen=max_seqlen,
)
# adapter
x = self.post_layernorm(x)
x = x.view(-1, self.spatial_merge_size, self.spatial_merge_size, x.shape[-1])
x = x.permute(0, 3, 1, 2)
x = self.downsample(x).view(-1, self.out_hidden_size)
x = self.merger(x)
return x
def load_weights(self, weights) -> set[str]:
loader = AutoWeightsLoader(self)
return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
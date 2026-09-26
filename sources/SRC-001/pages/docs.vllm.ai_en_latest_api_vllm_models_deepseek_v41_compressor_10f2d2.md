source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/compressor/
lastmod: 2026-09-24

class DeepseekCompressor(nn.Module):
"""DeepSeek V4.1 KV/score compressor.
Pools ``compress_ratio`` consecutive tokens into one KV latent with a
learned softmax gate (ratio 1 has no gate and no pooling). Owns the
linear, norm and state cache. State saving, compression and RMSNorm share
one Triton kernel. The emitted latent feeds independent main-cache and
indexer K kernels, which the attention layer can schedule concurrently.
"""
def __init__(
self,
vllm_config: VllmConfig,
compress_ratio: int,
hidden_size: int,
head_dim: int,
rotate: bool = False,
prefix: str = "",
k_cache_prefix="",
):
super().__init__()
if compress_ratio not in (1, 2):
raise NotImplementedError(
"DeepSeek V4.1 compressor supports compress_ratio 1 (full-length "
f"compressed cache) and 2; got {compress_ratio}. The ratio-4/128 "
"CuTe-DSL kernels are v4.0-specific and not wired here."
)
self.compress_ratio = compress_ratio
self.hidden_size = hidden_size
self.head_dim = head_dim
self.rotate = rotate
self.prefix = prefix
self.k_cache_prefix = k_cache_prefix
# Ratio 1 pools single tokens, so the checkpoint carries no gate.
self.has_gate = compress_ratio > 1
config = vllm_config.model_config.hf_config
self.rope_head_dim = config.qk_rope_head_dim
self.nope_head_dim = self.head_dim - self.rope_head_dim
assert self.head_dim == 512 and self.rope_head_dim == 64
self.rms_norm_eps = config.rms_norm_eps
self.device = current_platform.device_type
self.max_num_reqs = vllm_config.scheduler_config.max_num_seqs
self.max_model_len = vllm_config.model_config.max_model_len
wkv_wgate_sizes = (
[self.head_dim, self.head_dim] if self.has_gate else [self.head_dim]
)
self.fused_wkv_wgate = MergedColumnParallelLinear(
self.hidden_size,
wkv_wgate_sizes,
bias=False,
return_bias=False,
quant_config=None,
disable_tp=True,
prefix=f"{prefix}.fused_wkv_wgate",
)
self.norm = RMSNorm(self.head_dim, self.rms_norm_eps)
self.state_cache = (
CompressorStateCache(
state_dim=2 * self.head_dim, # kv_state + score_state
dtype=torch.float32,
prefix=f"{prefix}.state_cache",
)
if compress_ratio > 1
else None
)
# Save reference to static_forward_context for forward-time KV cache lookup.
# get_current_vllm_config() is only available during __init__, not forward.
self._static_forward_context = (
vllm_config.compilation_config.static_forward_context
)
def forward(
self,
# [num_tokens, (2 if has_gate else 1) * self.head_dim]
kv_score: torch.Tensor,
# [num_tokens]
positions: torch.Tensor,
) -> torch.Tensor | None:
"""Save states and return the BF16 latent for cache insertion and indexing.
Only valid group-boundary rows are written.
"""
attn_metadata = get_forward_context().attn_metadata
if not isinstance(attn_metadata, dict):
return None
if self.state_cache is None:
state_cache = query_start_loc = token_to_req_indices = None
slot_mapping = cast(Any, attn_metadata[self.k_cache_prefix]).slot_mapping
else:
state_metadata = cast(
CompressorMetadata, attn_metadata[self.state_cache.prefix]
)
state_cache = self.state_cache.kv_cache
slot_mapping = state_metadata.slot_mapping
query_start_loc = state_metadata.query_start_loc
token_to_req_indices = state_metadata.token_to_req_indices
latent = torch.empty(
kv_score.shape[0],
self.head_dim,
dtype=torch.bfloat16,
device=kv_score.device,
)
fused_save_compress_norm(
kv_score,
positions,
state_cache,
slot_mapping,
query_start_loc,
token_to_req_indices,
self.norm.weight,
self.rms_norm_eps,
self.compress_ratio,
latent,
)
return latent
def insert_cache(
self,
latent: torch.Tensor | None,
positions: torch.Tensor,
rotary_emb,
) -> None:
"""Publish compressed main-cache rows after the latent becomes ready."""
if latent is None:
return
attn_metadata = get_forward_context().attn_metadata
assert isinstance(attn_metadata, dict)
k_cache_metadata = cast(Any, attn_metadata[self.k_cache_prefix])
k_cache_layer = self._static_forward_context[self.k_cache_prefix]
kv_cache = k_cache_layer.kv_cache
# Plain-row per-tensor fp8 caches (FlashInfer) carry the layer's scale;
# fp8_ds_mla and bf16 rows need none.
fp8_scale = (
getattr(k_cache_layer, "_flashinfer_fp8_kv_scale", None)
if kv_cache.dtype == torch.float8_e4m3fn
else None
)
rope_quant_insert(
latent,
positions,
rotary_emb.cos_sin_cache,
kv_cache,
k_cache_metadata.slot_mapping,
self.compress_ratio,
fp8_scale=fp8_scale,
)
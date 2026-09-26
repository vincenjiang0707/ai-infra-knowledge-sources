source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/nvidia/flash_mla_mega_attn/
lastmod: 2026-09-24

class DeepseekV4MegaAttnAttention(DeepseekV4FlashMLAAttention):
"""FlashMLA mega-attention layer for DeepSeek V4.1 (SM100)."""
backend_cls = FlashMLAMegaAttnBackend
@classmethod
def is_available_for(cls, vllm_config: VllmConfig) -> bool:
"""Whether this layer can serve the configured model on this device.
The kernel is SM100-only and wants ``WV_GROUP_SIZE`` heads per ``wo_a``
group, which stops holding once TP divides the head count far enough
(TP16 on a 64-head model leaves 4). ``__init__`` raises on both, so the
default-backend selector asks here first rather than turning an
unsupported topology into a startup crash.
"""
if not is_flashmla_mega_attn_supported()[0]:
return False
config = vllm_config.model_config.hf_config
config = getattr(config, "text_config", config)
n_heads = getattr(config, "num_attention_heads", 0) or 0
n_groups = getattr(config, "o_groups", 0) or 0
tp_size = vllm_config.parallel_config.tensor_parallel_size
if n_heads % tp_size or n_groups % tp_size:
return False
n_local_heads, n_local_groups = n_heads // tp_size, n_groups // tp_size
if not n_local_groups or n_local_heads % WV_GROUP_SIZE:
return False
return n_local_heads // n_local_groups == WV_GROUP_SIZE
def __init__(self, vllm_config: VllmConfig, *args, **kwargs) -> None:
super().__init__(vllm_config, *args, **kwargs)
if self.n_local_heads % WV_GROUP_SIZE:
raise ValueError(
f"{self.prefix}: mega attention needs the local head count "
f"({self.n_local_heads}) to be a multiple of {WV_GROUP_SIZE}."
)
if self.n_local_heads // self.n_local_groups != WV_GROUP_SIZE:
raise ValueError(
f"{self.prefix}: mega attention needs {WV_GROUP_SIZE} heads per "
"wo_a group."
)
self.n_wv_group = self.padded_heads // WV_GROUP_SIZE
self._fused_layouts_ready = False
# ---- interface contract ------------------------------------------------
@property
def accepts_unnormed_unroped_query(self) -> bool:
return True
@property
def packed_kv_cache_dtype(self) -> CacheDType:
# This kernel is the only one that reads an NVFP4 compressed cache, so
# it is what an unspecific --kv-cache-dtype resolves to here.
return "nvfp4_ds_mla"
def _alloc_attn_out(
self, num_tokens: int, hidden_states: torch.Tensor
) -> QuantizedActivation:
return alloc_mega_attn_output(num_tokens, self.n_wv_group, hidden_states.device)
def _o_proj(
self, attn_out: QuantizedActivation, positions: torch.Tensor
) -> torch.Tensor:
"""Grouped ``wo_a`` then ``wo_b`` over the kernel's quantized output.
The inverse RoPE and the FP8 cast happened inside the attention
kernel, and ``wo_a`` is permuted for its output layout, so there is
nothing to rotate or quantize here and ``positions`` is unused. The
scale already is DeepGEMM's packed-ue8m0 MN-major layout, so the
einsum consumes the kernel's output with no repacking.
"""
groups = self.n_local_groups
z = torch.empty(
(attn_out.data.shape[0], groups, self.o_lora_rank),
dtype=torch.bfloat16,
device=attn_out.data.device,
)
fp8_einsum(
"bhr,hdr->bhd",
(attn_out.data[:, :groups], attn_out.scale[:, :groups]),
(self.wo_a.weight, self.wo_a.weight_scale),
z,
recipe=self._einsum_recipe,
)
return self._wo_b_proj(z.flatten(1))
# ---- weights -----------------------------------------------------------
def finalize_loaded_weights(self) -> None:
"""Permute wq_b rows / wo_a columns into the kernel's layouts.
Idempotent: a second post-load pass must not permute twice.
"""
if self._fused_layouts_ready:
return
permute_wq_b_(
self.wq_b.weight.data, self.wq_b.weight_scale.data, self.n_local_heads
)
permute_wo_a_(
self.wo_a.weight.data,
self.wo_a.weight_scale.data,
self.n_local_heads // self.n_local_groups,
)
self._fused_layouts_ready = True
# ---- forward -----------------------------------------------------------
def forward_mqa(
self,
q: torch.Tensor,
kv: torch.Tensor,
positions: torch.Tensor,
output: QuantizedActivation,
) -> None:
if not self._fused_layouts_ready:
raise RuntimeError(
f"{self.prefix}: wq_b / wo_a were never permuted for the mega "
"attention kernel; refusing to run with mismatched layouts."
)
attn_metadata = get_forward_context().attn_metadata
if attn_metadata is None:
# Warmup dummy run: reserve the prefill workspace, produce zeros.
self._reserve_prefill_workspace(q)
output.data.zero_()
output.scale.zero_()
return
assert isinstance(attn_metadata, dict)
# q was zero-padded to the kernel's head count by the fused KV insert.
assert q.shape[1] == self.padded_heads
flashmla_metadata = cast(
DeepseekV4FlashMLAMetadata | None,
attn_metadata.get(self.compressed_cache_prefix)
if self.compressed_cache_prefix is not None
else None,
)
swa_metadata = cast(
"DeepseekSparseSWAMetadata", attn_metadata[self.swa_cache_layer.prefix]
)
# The kernel takes int32 RoPE positions.
positions_int32 = positions.to(torch.int32)
num_decode_tokens = swa_metadata.num_decode_tokens
if swa_metadata.num_prefills > 0:
self._forward_prefill_mega(
q[num_decode_tokens:],
positions_int32[num_decode_tokens:],
flashmla_metadata,
swa_metadata,
output,
num_decode_tokens,
)
if swa_metadata.num_decodes > 0:
self._forward_decode_mega(
q[:num_decode_tokens],
positions_int32[:num_decode_tokens],
flashmla_metadata,
swa_metadata,
_token_slice(output, 0, num_decode_tokens),
)
def _reserve_prefill_workspace(self, q: torch.Tensor) -> None:
swa_only = self.compress_ratio == 0
n = 0 if swa_only else -(-self.max_model_len // self.compress_ratio)
m = n + self.window_size + self.max_num_batched_tokens
if swa_only:
top_k = 0
else:
assert self.topk_indices_buffer is not None
top_k = self.topk_indices_buffer.shape[-1]
combined_topk = round_up(top_k + self.window_size, 128)
current_workspace_manager().get_simultaneous(
((self.PREFILL_CHUNK_SIZE, m, q.shape[-1]), torch.bfloat16),
((self.max_num_batched_tokens, combined_topk), torch.int32),
((self.max_num_batched_tokens,), torch.int32),
)
def _decode_compressed_kv_and_topk(
self,
flashmla_metadata: DeepseekV4FlashMLAMetadata | None,
swa_metadata: "DeepseekSparseSWAMetadata",
) -> tuple[torch.Tensor | None, torch.Tensor | None, torch.Tensor | None]:
"""The compressed cache and its ``[n, topk]`` slot indices / lengths."""
if self.compress_ratio == 0:
return None, None, None
assert flashmla_metadata is not None
assert swa_metadata.is_valid_token is not None
assert self.topk_indices_buffer is not None
num_decode_tokens = swa_metadata.num_decode_tokens
indices, lens = compute_global_topk_indices_and_lens(
self.topk_indices_buffer[:num_decode_tokens],
swa_metadata.token_to_req_indices,
flashmla_metadata.block_table[: swa_metadata.num_decodes],
flashmla_metadata.block_size // self.compress_ratio,
swa_metadata.is_valid_token[:num_decode_tokens],
)
return self._compressed_kv_cache().unsqueeze(-2), indices, lens
def _forward_decode_mega(
self,
q: torch.Tensor,
positions_int32: torch.Tensor,
flashmla_metadata: DeepseekV4FlashMLAMetadata | None,
swa_metadata: "DeepseekSparseSWAMetadata",
out: QuantizedActivation,
) -> None:
"""Mega attention over the paged quantized caches, in place into ``out``.
The caches are ``[num_blocks, page, 1, bytes]``, the record taken from
``bytes`` (528 V4.1 fp8, 288 V4.1 NVFP4; NVFP4 only as the compressed
cache beside an fp8 SWA one), and the indices ``[s_q, topk]`` int32
slot ids (``block * page + offset``, ``-1`` invalid).
"""
extra_cache, extra_idx, extra_len = self._decode_compressed_kv_and_topk(
flashmla_metadata, swa_metadata
)
assert swa_metadata.decode_swa_indices is not None
torch.ops._flashmla_C.fused_norm_rope_attn_rope_cast_decode(
q,
self.swa_cache_layer.kv_cache.unsqueeze(-2),
swa_metadata.decode_swa_indices.view(q.shape[0], -1),
self.scale,
_HEAD_DIM_V,
self.attn_sink,
swa_metadata.decode_swa_lens,
extra_cache,
extra_idx,
extra_len,
False, # enable_q_norm
0.0, # rms_norm_eps
positions_int32,
*_ROPE_ARGS,
self.rotary_emb.cos_sin_cache,
self.n_wv_group,
*_SF_ARGS,
out.data,
out.scale,
)
def _forward_prefill_mega(
self,
q: torch.Tensor,
positions_int32: torch.Tensor,
flashmla_metadata: DeepseekV4FlashMLAMetadata | None,
swa_metadata: "DeepseekSparseSWAMetadata",
out: QuantizedActivation,
token_base: int,
) -> None:
swa_only = self.compress_ratio == 0
num_decodes = swa_metadata.num_decodes
num_decode_tokens = swa_metadata.num_decode_tokens
seq_lens = swa_metadata.prefill_seq_lens
gather_lens = swa_metadata.prefill_gather_lens
query_start_loc_cpu = swa_metadata.query_start_loc_cpu
query_start_loc = swa_metadata.query_start_loc
assert seq_lens is not None and gather_lens is not None
assert query_start_loc_cpu is not None and query_start_loc is not None
prefill_token_base = query_start_loc_cpu[num_decodes]
assert self.topk_indices_buffer is not None
topk_indices = self.topk_indices_buffer[num_decode_tokens:][
: swa_metadata.num_prefill_tokens
]
top_k = 0 if swa_only else topk_indices.shape[-1]
chunk_plan = swa_metadata.get_prefill_chunk_plan(
compress_ratio=self.compress_ratio,
prefill_chunk_size=self.PREFILL_CHUNK_SIZE,
has_compressed=not swa_only,
)
assert chunk_plan, "prefill chunk plan must be non-empty when num_prefills > 0"
workspace_manager = current_workspace_manager()
combined_topk = round_up(top_k + self.window_size, 128)
for chunk_start, chunk_end, chunk_n, chunk_m in chunk_plan:
chunk_size = chunk_end - chunk_start
kv_ws, idx_ws, lens_ws = workspace_manager.get_simultaneous(
((chunk_size, chunk_m, q.shape[-1]), torch.bfloat16),
((self.max_num_batched_tokens, combined_topk), torch.int32),
((self.max_num_batched_tokens,), torch.int32),
)
if not swa_only:
assert flashmla_metadata is not None
dequantize_and_gather_k_cache(
kv_ws[:chunk_size, :chunk_n],
self._compressed_kv_cache(),
seq_lens=seq_lens[chunk_start:chunk_end] // self.compress_ratio,
gather_lens=None,
block_table=flashmla_metadata.block_table[num_decodes:][
chunk_start:chunk_end
],
block_size=flashmla_metadata.block_size // self.compress_ratio,
offset=0,
)
dequantize_and_gather_k_cache(
kv_ws[:chunk_size],
self.swa_cache_layer.kv_cache,
seq_lens=seq_lens[chunk_start:chunk_end],
gather_lens=gather_lens[chunk_start:chunk_end],
block_table=swa_metadata.block_table[num_decodes:][
chunk_start:chunk_end
],
block_size=swa_metadata.block_size,
offset=chunk_n,
)
first, last = num_decodes + chunk_start, num_decodes + chunk_end
qs = int(query_start_loc_cpu[first] - prefill_token_base)
qe = int(query_start_loc_cpu[last] - prefill_token_base)
combined_indices, combined_lens = combine_topk_swa_indices(
topk_indices[qs:qe],
query_start_loc[first : last + 1],
seq_lens[chunk_start:chunk_end],
gather_lens[chunk_start:chunk_end],
self.window_size,
self.compress_ratio,
top_k,
chunk_m,
chunk_n,
out=(idx_ws[: qe - qs], lens_ws[: qe - qs]),
)
chunk_out = _token_slice(out, token_base + qs, token_base + qe)
# Mega attention over the gathered non-paged bf16 KV (RoPE already
# applied), in place into this chunk's token range. `indices`
# entries outside [0, s_kv) skip.
torch.ops._flashmla_C.fused_norm_rope_attn_rope_cast_fwd(
q[qs:qe],
kv_ws.view(-1, 1, q.shape[-1]),
combined_indices.unsqueeze(1),
self.scale,
_HEAD_DIM_V,
self.attn_sink,
combined_lens,
False, # enable_q_norm
0.0, # rms_norm_eps
positions_int32[qs:qe],
*_ROPE_ARGS,
self.rotary_emb.cos_sin_cache,
self.n_wv_group,
*_SF_ARGS,
chunk_out.data,
chunk_out.scale,
)
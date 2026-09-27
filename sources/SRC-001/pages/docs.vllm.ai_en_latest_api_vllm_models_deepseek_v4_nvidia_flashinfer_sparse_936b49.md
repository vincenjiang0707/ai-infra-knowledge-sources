source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/nvidia/flashinfer_sparse/
lastmod: 2026-09-27

class DeepseekV4FlashInferMLAAttention(DeepseekV4Attention):
"""FlashInfer TRTLLM-gen sparse MLA attention layer for SM100 DeepSeek V4."""
backend_cls = DeepseekV4FlashInferMLASparseBackend
swa_backend_cls = DeepseekSparseSWAFlashInferBackend
use_fp8_ds_mla_layout: ClassVar[bool] = False
@classmethod
def get_padded_num_q_heads(cls, num_heads: int) -> int:
return _pad_to_supported_q_heads(num_heads)
def _o_proj(
self, o: torch.Tensor | QuantizedActivation, positions: torch.Tensor
) -> torch.Tensor:
return deep_gemm_fp8_o_proj(
o,
positions,
self.rotary_emb.cos_sin_cache,
self.wo_a,
self.wo_b,
n_groups=self.n_local_groups,
heads_per_group=self.n_local_heads // self.n_local_groups,
nope_dim=self.nope_head_dim,
rope_dim=self.rope_head_dim,
o_lora_rank=self.o_lora_rank,
einsum_recipe=self._einsum_recipe,
tma_aligned_scales=self._tma_aligned_scales,
)
def _alloc_attn_out(
self, num_tokens: int, hidden_states: torch.Tensor
) -> torch.Tensor | QuantizedActivation:
if self._fuse_rope_quant:
return rope_quant_attn_out(num_tokens, hidden_states.device)
return super()._alloc_attn_out(num_tokens, hidden_states)
def __init__(self, vllm_config: VllmConfig, *args, **kwargs) -> None:
super().__init__(vllm_config, *args, **kwargs)
self._einsum_recipe, self._tma_aligned_scales = compute_fp8_einsum_recipe()
# RopeQuant derives each query's RoPE position as seq_len - q_len + i,
# which matches `positions` for DSpark's non-causal draft block too,
# since every call passes the real per-request seq_lens. The one
# exception is a draft block running past max_model_len, whose clamped
# positions it does not reproduce; that only costs those drafts.
reason = rope_quant_unsupported_reason(self)
self._fuse_rope_quant = reason is None
if reason is None:
logger.info_once(
"FLASHINFER_MLA_SPARSE_DSV4 fuses the inverse RoPE and FP8 "
"quant of the attention output."
)
else:
logger.debug_once("FLASHINFER_MLA_SPARSE_DSV4 RopeQuant off: %s", reason)
# Per-tensor FP8 scale buffers + precomputed scalar BMM scales. Only the
# per-tensor FP8 cache path consumes these; bf16 reads ``self.scale``.
if self.kv_cache_torch_dtype != torch.float8_e4m3fn:
return
fp8_q_scale = 1.0
fp8_kv_scale = 1.0
self.register_buffer(
"_flashinfer_fp8_q_scale",
torch.tensor([fp8_q_scale], dtype=torch.float32),
persistent=False,
)
self.register_buffer(
"_flashinfer_fp8_q_scale_inv",
torch.tensor([1.0 / fp8_q_scale], dtype=torch.float32),
persistent=False,
)
self.register_buffer(
"_flashinfer_fp8_kv_scale",
torch.tensor([fp8_kv_scale], dtype=torch.float32),
persistent=False,
)
# TRTLLM-gen takes scalar scale args on a distinct C++ path vs
# one-element tensors, so these are Python floats.
self._flashinfer_fp8_bmm1_scale = self.scale * fp8_q_scale * fp8_kv_scale
self._flashinfer_fp8_bmm2_scale = fp8_kv_scale
def forward_mqa(
self,
q: torch.Tensor,
kv: torch.Tensor,
positions: torch.Tensor,
output: torch.Tensor | QuantizedActivation,
) -> None:
if isinstance(output, QuantizedActivation):
assert output.data.shape[0] == q.shape[0]
else:
# The TRTLLM-gen kernel requires h_q in {64, 128}, so the output
# buffer is allocated at the padded head count while q arrives at
# the local head count; _forward pads q to match before the launcher.
assert output.shape[0] == q.shape[0] and output.shape[-1] == q.shape[-1], (
f"output buffer shape {output.shape} incompatible with q {q.shape}"
)
assert output.shape[1] >= q.shape[1], (
f"output heads {output.shape[1]} must be >= q heads {q.shape[1]}"
)
# Per-tensor FP8 q produces a bf16 attention output.
expected_output_dtype = (
torch.bfloat16 if q.dtype == torch.float8_e4m3fn else q.dtype
)
assert output.dtype == expected_output_dtype, (
f"output dtype {output.dtype} must match expected "
f"{expected_output_dtype} for q dtype {q.dtype}"
)
forward_context = get_forward_context()
attn_metadata = forward_context.attn_metadata
if attn_metadata is None:
# Warmup dummy run: FlashInfer reads the cache directly and lazily
# allocates its workspace, so nothing to reserve here.
if isinstance(output, QuantizedActivation):
output.data.zero_()
output.scale.zero_()
else:
output.zero_()
return
assert isinstance(attn_metadata, dict)
flashmla_metadata = cast(
DeepseekV4FlashMLAMetadata | None, attn_metadata.get(self.prefix)
)
swa_metadata = cast(
"DeepseekSparseSWAMetadata | None",
attn_metadata.get(self.swa_cache_layer.prefix),
)
assert swa_metadata is not None
swa_only = self.compress_ratio <= 1
# SWA-only layers don't allocate their own compressed KV cache.
self_kv_cache = self.kv_cache if not swa_only else None
swa_kv_cache = self.swa_cache_layer.kv_cache
self._forward(
q=q,
kv_cache=self_kv_cache,
swa_k_cache=swa_kv_cache,
swa_metadata=swa_metadata,
attn_metadata=flashmla_metadata,
swa_only=swa_only,
output=output,
)
def _build_sparse_index_metadata(
self,
kv_cache: torch.Tensor | None,
swa_k_cache: torch.Tensor,
swa_metadata: "DeepseekSparseSWAMetadata",
attn_metadata: DeepseekV4FlashMLAMetadata | None,
swa_only: bool,
num_rows: int | None = None,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
"""Build the combined sparse-index tensors for the mixed batch.
Returns ``(compressed_kv_cache, seq_lens, sparse_indices,
sparse_topk_lens)``, sized ``num_rows`` (default: the real tokens).
"""
num_decodes = swa_metadata.num_decodes
num_prefills = swa_metadata.num_prefills
num_decode_tokens = swa_metadata.num_decode_tokens
num_prefill_tokens = swa_metadata.num_prefill_tokens
num_reqs = num_decodes + num_prefills
num_tokens = num_decode_tokens + num_prefill_tokens
assert swa_metadata.seq_lens is not None
assert swa_metadata.query_start_loc is not None
assert swa_metadata.token_to_req_indices is not None
assert swa_metadata.decode_swa_indices is not None
assert swa_metadata.block_table is not None
decode_swa_indices = swa_metadata.decode_swa_indices.reshape(
num_decode_tokens, swa_metadata.decode_swa_width
)
decode_compressed_topk_lens = None
decode_compressed_indices_are_local = False
decode_is_valid_token = None
if swa_only:
assert self.topk_indices_buffer is not None
compressed_kv_cache = swa_k_cache
decode_compressed_indices = None
prefill_topk_indices = self.topk_indices_buffer[
num_decode_tokens:num_tokens, :0
]
compressed_block_table = None
compressed_block_size = swa_metadata.block_size
top_k = 0
else:
assert kv_cache is not None
assert attn_metadata is not None
compressed_kv_cache = kv_cache
compressed_block_table = attn_metadata.block_table[:num_reqs]
compressed_block_size = attn_metadata.block_size // self.compress_ratio
if self.compress_ratio == 4:
assert self.topk_indices_buffer is not None
if num_prefill_tokens > 0:
prefill_topk_indices = self.topk_indices_buffer[
num_decode_tokens:num_tokens
]
top_k = prefill_topk_indices.shape[-1]
else:
prefill_topk_indices = self.topk_indices_buffer[:0, :0]
top_k = 0
decode_compressed_indices_are_local = True
assert swa_metadata.is_valid_token is not None
decode_is_valid_token = swa_metadata.is_valid_token[:num_decode_tokens]
if num_decode_tokens > 0:
decode_compressed_indices = self.topk_indices_buffer[
:num_decode_tokens
]
else:
# Keep the logical width aligned with the mixed-batch case so
# pure-prefill steps reuse the same Triton specialization.
decode_compressed_indices = prefill_topk_indices[:0]
else:
if num_prefill_tokens > 0:
assert attn_metadata.c128a_prefill_topk_indices is not None
prefill_topk_indices = attn_metadata.c128a_prefill_topk_indices
top_k = prefill_topk_indices.shape[-1]
else:
prefill_topk_indices = decode_swa_indices[:0, :0]
top_k = 0
if num_decode_tokens > 0:
assert attn_metadata.c128a_global_decode_topk_indices is not None
assert attn_metadata.c128a_decode_topk_lens is not None
decode_compressed_indices = (
attn_metadata.c128a_global_decode_topk_indices.view(
num_decode_tokens, -1
)
)
decode_compressed_topk_lens = attn_metadata.c128a_decode_topk_lens
if num_prefill_tokens == 0:
prefill_topk_indices = decode_compressed_indices[:0, :0]
else:
decode_compressed_indices = prefill_topk_indices[:0]
decode_compressed_topk_lens = swa_metadata.seq_lens[:0]
query_start_loc = swa_metadata.query_start_loc[: num_reqs + 1]
seq_lens = swa_metadata.seq_lens[:num_reqs]
assert seq_lens.dtype == torch.int32
# cache for SWA-only and C128A that build the same mixed sparse indices
# C4A stays uncached.
cache_key = (
"swa_only"
if swa_only
else ("c128a" if self.compress_ratio == 128 else "c4a")
)
if num_rows is not None:
cache_key = f"{cache_key}:{num_rows}"
cached_sparse = swa_metadata.flashinfer_sparse_index_cache.get(cache_key, None)
if cached_sparse is None:
swa_block_span = _packed_block_span(swa_k_cache)
compressed_block_span = _packed_block_span(compressed_kv_cache)
sparse_indices, sparse_topk_lens = build_flashinfer_mixed_sparse_indices(
decode_swa_indices,
decode_compressed_indices,
decode_compressed_topk_lens,
prefill_topk_indices[:num_prefill_tokens],
query_start_loc,
seq_lens,
swa_metadata.token_to_req_indices[:num_tokens],
swa_metadata.block_table[:num_reqs],
swa_metadata.block_size,
compressed_block_table,
compressed_block_size,
self.window_size,
self.compress_ratio,
top_k,
decode_compressed_indices_are_local=decode_compressed_indices_are_local,
decode_is_valid_token=decode_is_valid_token,
swa_block_span=swa_block_span,
compressed_block_span=compressed_block_span,
prefill_left_visible=swa_metadata.prefill_left_visible,
prefill_right_visible=swa_metadata.prefill_right_visible,
# getattr for tests that bypass __init__ via object.__new__.
max_image_tokens=getattr(self, "max_image_tokens", 0),
num_rows=num_rows,
)
if not cache_key.startswith("c4a"):
swa_metadata.flashinfer_sparse_index_cache[cache_key] = (
sparse_indices,
sparse_topk_lens,
)
else:
sparse_indices, sparse_topk_lens = cached_sparse
return compressed_kv_cache, seq_lens, sparse_indices, sparse_topk_lens
def _forward(
self,
q: torch.Tensor,
kv_cache: torch.Tensor | None,
swa_k_cache: torch.Tensor,
swa_metadata: "DeepseekSparseSWAMetadata",
attn_metadata: DeepseekV4FlashMLAMetadata | None,
swa_only: bool,
output: torch.Tensor | QuantizedActivation,
) -> None:
assert self.kv_cache_torch_dtype in (torch.bfloat16, torch.float8_e4m3fn)
num_decodes = swa_metadata.num_decodes
num_prefills = swa_metadata.num_prefills
num_decode_tokens = swa_metadata.num_decode_tokens
num_prefill_tokens = swa_metadata.num_prefill_tokens
num_reqs = num_decodes + num_prefills
num_tokens = num_decode_tokens + num_prefill_tokens
if num_tokens == 0:
return
# RopeQuant's output is group-major with a group stride of exactly
# sum_q tokens, so both calls span every row of the (CUDA-graph
# padded) buffers and select their tokens through cum_seq_lens_q
# alone; the kernel never touches rows outside it.
rope_quant = isinstance(output, QuantizedActivation)
(
compressed_kv_cache,
seq_lens,
sparse_indices,
sparse_topk_lens,
) = self._build_sparse_index_metadata(
kv_cache=kv_cache,
swa_k_cache=swa_k_cache,
swa_metadata=swa_metadata,
attn_metadata=attn_metadata,
swa_only=swa_only,
num_rows=q.shape[0] if rope_quant else None,
)
# CUDA graph execution can pad q/output past the scheduled token count;
# restrict to the real tokens (the launcher validates sparse indices).
query = q if rope_quant else q[:num_tokens]
bmm1_scale: float | torch.Tensor = self.scale
bmm2_scale: float | torch.Tensor = 1.0
if self.kv_cache_torch_dtype == torch.float8_e4m3fn:
assert query.dtype == torch.float8_e4m3fn
bmm1_scale = self._flashinfer_fp8_bmm1_scale
bmm2_scale = self._flashinfer_fp8_bmm2_scale
else:
assert query.dtype == torch.bfloat16
query = query.contiguous()
# The TRTLLM-gen sparse-MLA kernel requires h_q in {64, 128}; zero-pad
# the query heads to the allocated output head count. Padded heads attend
# to the shared KV and are sliced off downstream (output is padded too).
padded_heads = (
output.shape[1] if isinstance(output, torch.Tensor) else self.padded_heads
)
if query.shape[1] < padded_heads:
padded_query = query.new_zeros(
(query.shape[0], padded_heads, query.shape[2])
)
padded_query[:, : query.shape[1], :] = query
query = padded_query
workspace = _get_flashinfer_dsv4_workspace(q.device)
query_start_loc = swa_metadata.query_start_loc
query_start_loc_cpu = swa_metadata.query_start_loc_cpu
assert query_start_loc is not None and query_start_loc_cpu is not None
def run(
rows: slice, reqs: slice, cum_seq_lens_q: torch.Tensor, max_q_len: int
) -> None:
if rope_quant:
assert isinstance(output, QuantizedActivation)
rows = slice(None)
out_kwargs = dict(
out=output.data,
dsv4_output_scale=output.scale,
dsv4_inv_rope_cos_sin_cache=self.rotary_emb.cos_sin_cache,
)
else:
assert isinstance(output, torch.Tensor)
out_kwargs = dict(out=output[rows])
flashinfer_trtllm_batch_decode_sparse_mla_dsv4(
query=query[rows],
swa_kv_cache=swa_k_cache,
workspace_buffer=workspace,
sparse_indices=sparse_indices[rows],
sparse_indices_are_storage_offsets=True,
compressed_kv_cache=compressed_kv_cache,
sparse_topk_lens=sparse_topk_lens[rows],
seq_lens=seq_lens[reqs],
bmm1_scale=bmm1_scale,
bmm2_scale=bmm2_scale,
sinks=self.attn_sink,
cum_seq_lens_q=cum_seq_lens_q,
max_q_len=max_q_len,
**out_kwargs,
)
# Keep the TRTLLM-gen decode/prefill split: the launcher is tuned for
# uniform-q batches, and this avoids flattening mixed batches into one call.
if num_decode_tokens > 0:
run(
slice(0, num_decode_tokens),
slice(0, num_decodes),
query_start_loc[: num_decodes + 1],
swa_metadata.max_decode_query_len,
)
if num_prefill_tokens > 0:
prefill_cu = query_start_loc[num_decodes : num_reqs + 1]
if not rope_quant:
# The prefill query view re-anchors at offset 0, so rebase the
# cumulative query offsets to start at 0.
prefill_cu = prefill_cu - query_start_loc[num_decodes]
prefill_cu_cpu = query_start_loc_cpu[num_decodes : num_reqs + 1]
prefill_lens_cpu = prefill_cu_cpu[1:] - prefill_cu_cpu[:-1]
run(
slice(num_decode_tokens, num_tokens),
slice(num_decodes, num_reqs),
prefill_cu,
int(prefill_lens_cpu.max().item()),
)
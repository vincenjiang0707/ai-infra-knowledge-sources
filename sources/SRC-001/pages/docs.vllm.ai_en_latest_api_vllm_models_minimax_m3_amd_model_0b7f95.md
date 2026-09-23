source: https://docs.vllm.ai/en/latest/api/vllm/models/minimax_m3/amd/model/
lastmod: 2026-09-23

class MiniMaxM3SparseAttention(nn.Module, AttentionLayerBase):
"""Block-sparse attention layer with the lightning-indexer branch.
This is a merged attention layer: it owns the projections (qkv + index
q/k), per-head QK norms and RoPE, *and* the attention-backend wiring that a
generic ``Attention`` layer would normally provide — it binds the
``MiniMaxM3SparseBackend`` + main impl, registers the main paged K/V cache,
and owns the lightning indexer (``MiniMaxM3Indexer``), which holds the
index-key side cache.
The index branch (index_{q,k}_proj + index_{q,k}_norm) feeds the sparse
top-k block selection. M3 always disables the index value/output
projections (``sparse_disable_index_value`` set for every sparse layer), so
``index_{v,o}_proj`` are never created.
"""
def __init__(
self,
config: PretrainedConfig,
layer_id: int,
quant_config: QuantizationConfig | None = None,
prefix: str = "",
cache_config: CacheConfig | None = None,
topk_indices_buffer: torch.Tensor | None = None,
sparse_table_buffers: tuple[torch.Tensor, torch.Tensor] | None = None,
) -> None:
super().__init__()
self.hidden_size = config.hidden_size
tp_size = get_tensor_model_parallel_world_size()
self.total_num_heads = config.num_attention_heads
assert self.total_num_heads % tp_size == 0
self.num_heads = self.total_num_heads // tp_size
self.total_num_kv_heads = config.num_key_value_heads
if self.total_num_kv_heads >= tp_size:
assert self.total_num_kv_heads % tp_size == 0
else:
assert tp_size % self.total_num_kv_heads == 0
self.num_kv_heads = max(1, self.total_num_kv_heads // tp_size)
self.head_dim = config.head_dim
self.q_size = self.num_heads * self.head_dim
self.kv_size = self.num_kv_heads * self.head_dim
self.scaling = self.head_dim**-0.5
# Cross-layer index sharing (ATOM index_topk_freq): when True this sparse
# layer reuses the previous compute layer's top-k block selection from the
# shared topk_indices_buffer instead of recomputing it. Static per layer
# -> cudagraph-capture-safe.
self.skip_index_topk = _should_skip_index_topk(config, layer_id)
# Sparse "index" branch dims. index_q has the same head count as the KV
# heads (sparse_num_index_heads == num_key_value_heads), so it shards
# identically -- including replication when tp_size > num_key_value_heads.
sparse_cfg = config.sparse_attention_config
self.total_idx_heads = sparse_cfg["sparse_num_index_heads"]
self.num_idx_heads = self.num_kv_heads
self.idx_head_dim = sparse_cfg["sparse_index_dim"]
self.index_q_size = self.num_idx_heads * self.idx_head_dim
# Single fused projection: q, k, v, index_q, index_k in one GEMM.
self.qkv_proj = MinimaxM3QKVParallelLinearWithIndexer(
self.hidden_size,
self.head_dim,
self.total_num_heads,
self.total_num_kv_heads,
self.total_idx_heads,
self.idx_head_dim,
bias=False,
quant_config=quant_config,
prefix=f"{prefix}.qkv_proj",
)
# reduce_results=False: the attention all-reduce is fused with the
# following post_attention_layernorm (GemmaRMSNorm) in the decoder layer
# via fused_allreduce_gemma_rms_norm.
self.o_proj = RowParallelLinear(
self.total_num_heads * self.head_dim,
self.hidden_size,
bias=False,
reduce_results=False,
quant_config=quant_config,
prefix=f"{prefix}.o_proj",
)
# Per-head QK norm (qk_norm_type == "per_head", use_gemma_norm == True).
self.q_norm = MiniMAXGemmaRMSNorm(self.head_dim, eps=config.rms_norm_eps)
self.k_norm = MiniMAXGemmaRMSNorm(self.head_dim, eps=config.rms_norm_eps)
# Partial RoPE: rotary_dim == head_dim * partial_rotary_factor. Honors
# config.rope_scaling (e.g. YaRN) so long-context positions are covered.
self.rotary_emb = _build_rotary_emb(config, self.head_dim)
self.index_q_norm = MiniMAXGemmaRMSNorm(
self.idx_head_dim, eps=config.rms_norm_eps
)
self.index_k_norm = MiniMAXGemmaRMSNorm(
self.idx_head_dim, eps=config.rms_norm_eps
)
self.index_rotary_emb = self.rotary_emb
# Attention-backend wiring.
vllm_config = get_current_vllm_config()
self.layer_name = f"{prefix}.attn"
self.kv_cache_dtype = (
cache_config.cache_dtype if cache_config is not None else "auto"
)
self.kv_cache_torch_dtype = kv_cache_dtype_str_to_dtype(
self.kv_cache_dtype, vllm_config.model_config
)
# MiniMax-M3 sparse attention owns its KV-cache insert/read path instead
# of wrapping the generic Attention module. Keep the same runtime scale
# attributes so FP8 KV reads can honor vLLM's per-layer descale contract.
set_default_quant_scales(self, register_buffer=True)
# Indexer side-cache dtype, mirroring --kv-cache-dtype for the main cache
# (--attention-config '{"indexer_kv_dtype": ...}'). fp8 e4m3 is what the
# AITER indexer needs; bf16 keeps the Triton indexer.
self.indexer_kv_dtype = vllm_config.attention_config.resolve_indexer_kv_dtype(
"bf16"
)
# Shared top-k buffer: the indexer writes the selected blocks into it and
# the attend impl reads them back (no Python value crosses the break).
self.topk_indices_buffer = topk_indices_buffer
# Indexer and main attention are separate impls. The AITER indexer is
# ROCm-only, so it is selected here rather than inside the neutral
# MiniMaxM3Indexer, which knows nothing about it and would pick Triton.
indexer_impl_cls = select_aiter_indexer_impl_cls(
topk_blocks=sparse_cfg["sparse_topk_blocks"],
sparse_block_size=sparse_cfg["sparse_block_size"],
num_index_heads=self.num_idx_heads,
index_head_dim=self.idx_head_dim,
indexer_kv_dtype=self.indexer_kv_dtype,
score_type=sparse_cfg.get("sparse_score_type", "max"),
)
# The attend gate below needs this: an emitted table is what lets it
# serve more than one KV head per rank. Buffers to write the table into
# only arrive when the model already resolved the attend to the AITER
# path the table addresses, so that is not rechecked here.
self.indexer_emits_table = (
indexer_impl_cls is not None and sparse_table_buffers is not None
)
# The backend names the metadata builder, which for the AITER path is
# the one that rebases the block table the indexer's top-k resolves
# through, so both have to come from the same selection.
self.attn_backend, main_impl_cls = select_main_backend_and_impl_cls(
topk_blocks=sparse_cfg["sparse_topk_blocks"],
kv_cache_dtype=self.kv_cache_dtype,
num_kv_heads=self.num_kv_heads,
emits_sparse_block_table=self.indexer_emits_table,
)
# impl is AttentionImplBase (broader than AttentionLayerBase's annotation).
self.impl: MiniMaxM3SparseImpl = main_impl_cls( # type: ignore[assignment]
self.num_heads,
self.head_dim,
self.scaling,
self.num_kv_heads,
kv_cache_dtype=self.kv_cache_dtype,
topk_blocks=sparse_cfg["sparse_topk_blocks"],
sparse_block_size=sparse_cfg["sparse_block_size"],
)
self.use_aiter_sparse_pa = minimax_m3_use_aiter_sparse_pa(
self.num_kv_heads, emits_sparse_block_table=self.indexer_emits_table
)
self.kv_cache_k = torch.tensor([])
self.kv_cache_v = torch.tensor([])
self._aiter_sparse_pa_cache_data_ptr = 0
self._aiter_sparse_pa_block_page_stride = 0
indexer_kwargs = dict(
num_kv_heads=self.num_kv_heads,
scale=self.scaling,
topk_blocks=sparse_cfg["sparse_topk_blocks"],
sparse_block_size=sparse_cfg["sparse_block_size"],
num_index_heads=self.num_idx_heads,
index_head_dim=self.idx_head_dim,
prefix=self.layer_name,
init_blocks=sparse_cfg.get("sparse_init_block", 0),
local_blocks=sparse_cfg.get("sparse_local_block", 0),
score_type=sparse_cfg.get("sparse_score_type", "max"),
cache_config=cache_config,
indexer_kv_dtype=self.indexer_kv_dtype,
topk_indices_buffer=topk_indices_buffer,
)
self.sparse_bt_buffer: torch.Tensor | None = None
self.sparse_ctx_buffer: torch.Tensor | None = None
if indexer_impl_cls is None:
# Self-contained nn.Module: owns its side cache, selects its impl.
self.indexer = MiniMaxM3Indexer(**indexer_kwargs)
else:
if self.indexer_emits_table:
assert sparse_table_buffers is not None
self.sparse_bt_buffer, self.sparse_ctx_buffer = sparse_table_buffers
self.indexer = MiniMaxM3AiterIndexer(
impl_cls=indexer_impl_cls,
sparse_bt_buffer=self.sparse_bt_buffer,
sparse_ctx_buffer=self.sparse_ctx_buffer,
**indexer_kwargs,
)
# Register the main K/V cache so the KV-cache manager allocates it.
compilation_config = vllm_config.compilation_config
if self.layer_name in compilation_config.static_forward_context:
raise ValueError(f"Duplicate layer name: {self.layer_name}")
compilation_config.static_forward_context[self.layer_name] = self
self.kv_cache = torch.tensor([]) # replaced by bind_kv_cache
def get_attn_backend(self) -> type[MiniMaxM3SparseBackend]:
return self.attn_backend
def get_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCacheSpec | None:
# Main GQA K/V cache. Block size may change after load, refresh it.
# AITER sparse PA wants K and V as two separate head groups
# (H folded into the content dim).
sparse_pa = self.use_aiter_sparse_pa
kv_bytes = (
self.num_kv_heads * self.head_dim * self.kv_cache_torch_dtype.itemsize
)
return FullAttentionSpec(
block_size=vllm_config.cache_config.block_size,
num_kv_heads=self.num_kv_heads,
head_size=self.head_dim,
head_size_v=self.head_dim,
dtype=self.kv_cache_torch_dtype,
kv_quant_mode=get_kv_quant_mode(self.kv_cache_dtype),
num_head_slots=2 if sparse_pa else None,
state_content_bytes=kv_bytes if sparse_pa else None,
)
def _ensure_aiter_sparse_pa_kv_cache(self) -> None:
if self.kv_cache.numel() == 0:
return
if self._aiter_sparse_pa_cache_data_ptr == self.kv_cache.data_ptr():
return
kv_cache = self.kv_cache
if is_quantized_kv_cache(self.kv_cache_dtype):
kv_cache = kv_cache.view(self.impl.kv_cache_fp8_dtype)
key_cache, value_cache = kv_cache.unbind(1)
x = 16 // kv_cache.element_size()
if self.head_dim % x != 0:
raise RuntimeError(
"MiniMax-M3 AITER sparse PA requires head_dim divisible by "
f"16 / dtype_size, got head_dim={self.head_dim}, x={x}"
)
num_blocks, _, block_size, _ = kv_cache.shape
pages_in_side = block_size // 16
if key_cache.is_contiguous() and value_cache.is_contiguous():
k_src, v_src = key_cache, value_cache
block_pages, v_page_offset = pages_in_side, 0
elif kv_cache.is_contiguous():
k_src = v_src = kv_cache
block_pages, v_page_offset = 2 * pages_in_side, pages_in_side
else:
raise RuntimeError(
"MiniMax-M3 AITER sparse PA needs each K/V head slot stored as "
"whole 16-token pages, but the resolved KV cache layout gives "
"neither dense planes nor block-contiguous pages."
)
num_phys16 = num_blocks * block_pages
self.kv_cache_k = k_src.view(
num_phys16,
self.num_kv_heads,
self.head_dim // x,
16,
x,
)
# Offsetting V by half a block lets both sides share one page id.
self.kv_cache_v = v_src.view(
num_phys16,
self.num_kv_heads,
16 // x,
self.head_dim,
x,
)[v_page_offset:]
self._aiter_sparse_pa_block_page_stride = minimax_m3_sparse_block_page_stride(
self.kv_cache_k, self.kv_cache_v
)
self._aiter_sparse_pa_cache_data_ptr = self.kv_cache.data_ptr()
def get_aiter_sparse_pa_kv_cache(self) -> tuple[torch.Tensor, torch.Tensor]:
self._ensure_aiter_sparse_pa_kv_cache()
return self.kv_cache_k, self.kv_cache_v
def _get_aiter_sparse_pa_slot_mapping(
self,
slot_mapping: torch.Tensor,
key_cache: torch.Tensor,
value_cache: torch.Tensor,
) -> torch.Tensor:
if value_cache.shape[0] == key_cache.shape[0]:
return slot_mapping
attn_metadata = get_forward_context().attn_metadata
page16_slot_mapping = None
if isinstance(attn_metadata, dict):
main_md = attn_metadata[self.layer_name]
assert isinstance(main_md, MiniMaxM3SparseMetadata)
page16_slot_mapping = main_md.page16_slot_mapping
if (
page16_slot_mapping is None
or page16_slot_mapping.shape != slot_mapping.shape
):
page16_slot_mapping = minimax_m3_rebase_slots_to_page16(
slot_mapping, self.kv_cache.shape[2]
)
return page16_slot_mapping
def _insert_aiter_sparse_pa_kv(
self,
k: torch.Tensor,
v: torch.Tensor,
index_k: torch.Tensor | None,
slot_mapping: torch.Tensor,
index_slot_mapping: torch.Tensor | None,
key_cache: torch.Tensor,
value_cache: torch.Tensor,
) -> None:
if self.kv_cache.numel() == 0:
return
from aiter import reshape_and_cache
from vllm.models.minimax_m3.amd.ops.sparse_pa import (
minimax_m3_insert_index_cache,
)
kv_cache_dtype = (
self.kv_cache_dtype
if is_quantized_kv_cache(self.kv_cache_dtype)
else "auto"
)
reshape_and_cache(
_kv_insert_operand(k),
_kv_insert_operand(v),
key_cache,
value_cache,
slot_mapping,
kv_cache_dtype=kv_cache_dtype,
k_scale=getattr(self, "_k_scale", None),
v_scale=getattr(self, "_v_scale", None),
asm_layout=True,
)
if index_k is None or index_slot_mapping is None:
return
index_cache = self.indexer.index_cache.kv_cache
if index_cache.numel() == 0:
return
minimax_m3_insert_index_cache(index_k, index_cache, index_slot_mapping)
def forward(
self,
positions: torch.Tensor,
hidden_states: torch.Tensor,
) -> torch.Tensor:
# Single fused projection emitting [q | k | v | index_q | index_k].
qkv, _ = self.qkv_proj(hidden_states)
# Horizontally-fused per-head Gemma QK-norm + partial NeoX RoPE on the
# main (q/k) and index (index_q/index_k) branches, all read straight out
# of the single fused ``qkv`` tensor. Once the paged caches are bound the
# kernel also inserts k/v and the index key into them (each with its own
# slot_mapping); the memory-profiling run (caches unbound, no slot_mapping)
# short-circuits to zeros below. The main and index slot mappings are read
# from the forward context's slot_mapping dict, matching the
# breakable-cudagraph path -- see nvidia/model.py.
cos_sin_cache = self.rotary_emb.cos_sin_cache
rotary_dim = self.rotary_emb.rotary_dim
eps = self.q_norm.variance_epsilon
num_tokens = qkv.shape[0]
fwd_slot_mapping = get_forward_context().slot_mapping
if (
not isinstance(fwd_slot_mapping, dict)
or self.layer_name not in fwd_slot_mapping
):
# Memory-profiling run: caches not yet bound, slot_mapping is empty.
return qkv.new_zeros((num_tokens, self.hidden_size))
main_slot_mapping = fwd_slot_mapping[self.layer_name]
q = qkv.new_empty((num_tokens, self.q_size))
key_cache = value_cache = page16_slot_mapping = None
k_scale = v_scale = None
use_fused_qknorm = False
if self.use_aiter_sparse_pa:
key_cache, value_cache = self.get_aiter_sparse_pa_kv_cache()
page16_slot_mapping = self._get_aiter_sparse_pa_slot_mapping(
main_slot_mapping, key_cache, value_cache
)
k_scale = getattr(self, "_k_scale", None)
v_scale = getattr(self, "_v_scale", None)
use_fused_qknorm = rocm_aiter_ops.fused_qknorm_idxrqknorm_enabled(
self.kv_cache_dtype, k_scale, v_scale
)
if self.skip_index_topk:
index_q = None
if self.use_aiter_sparse_pa:
assert key_cache is not None
assert value_cache is not None
assert page16_slot_mapping is not None
if use_fused_qknorm:
rocm_aiter_ops.fused_qknorm_idxrqknorm(
qkv,
self.q_norm.weight,
self.k_norm.weight,
cos_sin_cache,
positions,
self.num_heads,
self.num_kv_heads,
rotary_dim,
eps,
page16_slot_mapping,
key_cache,
value_cache,
q,
self.kv_cache_dtype,
k_scale,
v_scale,
num_index_heads=self.num_idx_heads,
skip_index_branch=True,
)
else:
ops.fused_minimax_m3_qknorm_rope_kv_insert(
qkv,
self.q_norm.weight,
self.k_norm.weight,
cos_sin_cache,
positions,
self.num_heads,
self.num_kv_heads,
rotary_dim,
eps,
num_index_heads=self.num_idx_heads,
q_out=q,
skip_index_branch=True,
)
k_start = self.q_size
v_start = k_start + self.kv_size
k = qkv[:, k_start:v_start].view(
num_tokens, self.num_kv_heads, self.head_dim
)
v = qkv[:, v_start : v_start + self.kv_size].view(
num_tokens, self.num_kv_heads, self.head_dim
)
self._insert_aiter_sparse_pa_kv(
k,
v,
None,
page16_slot_mapping,
None,
key_cache,
value_cache,
)
else:
ops.fused_minimax_m3_qknorm_rope_kv_insert(
qkv,
self.q_norm.weight,
self.k_norm.weight,
cos_sin_cache,
positions,
self.num_heads,
self.num_kv_heads,
rotary_dim,
eps,
num_index_heads=self.num_idx_heads,
slot_mapping=main_slot_mapping,
kv_cache=self.kv_cache,
block_size=self.kv_cache.size(2), # paged-cache block size
q_out=q,
kv_cache_dtype=self.kv_cache_dtype,
skip_index_branch=True,
)
else:
index_slot_mapping = fwd_slot_mapping[self.indexer.index_cache.prefix]
# index_q matches the index-K cache dtype (e4m3 for the AITER fp8
# score path); the fused kernel emits fp8 directly when this buffer
# is e4m3.
index_q = qkv.new_empty(
(num_tokens, self.index_q_size),
dtype=self.indexer.index_cache.dtype,
)
if self.use_aiter_sparse_pa:
assert key_cache is not None
assert value_cache is not None
assert page16_slot_mapping is not None
index_cache = self.indexer.index_cache.kv_cache
if use_fused_qknorm:
rocm_aiter_ops.fused_qknorm_idxrqknorm(
qkv,
self.q_norm.weight,
self.k_norm.weight,
cos_sin_cache,
positions,
self.num_heads,
self.num_kv_heads,
rotary_dim,
eps,
page16_slot_mapping,
key_cache,
value_cache,
q,
self.kv_cache_dtype,
k_scale,
v_scale,
self.index_q_norm.weight,
self.index_k_norm.weight,
self.num_idx_heads,
index_cache,
index_q,
index_slot_mapping,
)
else:
ops.fused_minimax_m3_qknorm_rope_kv_insert(
qkv,
self.q_norm.weight,
self.k_norm.weight,
cos_sin_cache,
positions,
self.num_heads,
self.num_kv_heads,
rotary_dim,
eps,
self.index_q_norm.weight,
self.index_k_norm.weight,
self.num_idx_heads,
q_out=q,
index_q_out=index_q,
kv_cache_dtype=self.kv_cache_dtype,
)
k_start = self.q_size
v_start = k_start + self.kv_size
index_k_start = v_start + self.kv_size + self.index_q_size
k = qkv[:, k_start:v_start].view(
num_tokens, self.num_kv_heads, self.head_dim
)
v = qkv[:, v_start : v_start + self.kv_size].view(
num_tokens, self.num_kv_heads, self.head_dim
)
index_k = qkv[
:, index_k_start : index_k_start + self.idx_head_dim
].view(num_tokens, self.idx_head_dim)
self._insert_aiter_sparse_pa_kv(
k,
v,
index_k,
page16_slot_mapping,
index_slot_mapping,
key_cache,
value_cache,
)
else:
ops.fused_minimax_m3_qknorm_rope_kv_insert(
qkv,
self.q_norm.weight,
self.k_norm.weight,
cos_sin_cache,
positions,
self.num_heads,
self.num_kv_heads,
rotary_dim,
eps,
self.index_q_norm.weight,
self.index_k_norm.weight,
self.num_idx_heads,
main_slot_mapping,
index_slot_mapping,
self.kv_cache,
self.indexer.index_cache.kv_cache,
self.kv_cache.size(2), # paged-cache block size
q,
index_q,
self.kv_cache_dtype,
)
output = torch.empty_like(q)
attn_output = self._run_attention(q, index_q, output)
output, _ = self.o_proj(attn_output)
return output
@eager_break_during_capture
def _run_attention(
self,
query: torch.Tensor,
index_query: torch.Tensor | None,
output: torch.Tensor,
) -> torch.Tensor:
# Single eager break around both: their split-K kernels read per-request
# metadata and can't be captured into a cudagraph. The indexer writes its
# top-k into the shared ``topk_indices_buffer``; the attend reads it back.
# When skip_index_topk is set (ATOM index_topk_freq), reuse the selection
# the preceding compute layer wrote into the shared buffer this forward.
decode_sparse_table: tuple[torch.Tensor, torch.Tensor] | None = None
if not self.skip_index_topk:
assert index_query is not None
# The AITER indexer emits the attend table into its persistent
# buffers, resolving its selection through the page-16 rebase of the
# attend's block table. The Triton indexer can instead fuse decode
# top-k with main's per-forward sparse-table allocation.
if self.indexer_emits_table:
attn_metadata = get_forward_context().attn_metadata
decode_page16 = prefill_page16 = None
if isinstance(attn_metadata, dict):
main_md = attn_metadata[self.layer_name]
assert isinstance(main_md, MiniMaxM3SparseMetadata)
# Rebased once per step by the AITER attend's builder, which
# this path selected along with the impl.
d, p = main_md.decode, main_md.prefill
if d is not None:
assert isinstance(d, MiniMaxM3SparseAiterPADecodeMetadata)
decode_page16 = d.page16_block_table
if p is not None:
assert isinstance(p, MiniMaxM3SparseAiterPAPrefillMetadata)
prefill_page16 = p.page16_block_table
self.indexer(
index_query,
decode_page16_block_table=decode_page16,
prefill_page16_block_table=prefill_page16,
)
else:
attn_metadata = get_forward_context().attn_metadata
if self.use_aiter_sparse_pa and isinstance(attn_metadata, dict):
main_md = attn_metadata[self.layer_name]
assert isinstance(main_md, MiniMaxM3SparseMetadata)
if main_md.num_decodes > 0:
d = main_md.decode
assert d is not None
topk = self.topk_indices_buffer
assert topk is not None
decode_sparse_table = minimax_m3_alloc_sparse_block_table(
topk[:, : main_md.num_decode_tokens, :]
)
block_page_stride = self._aiter_sparse_pa_block_page_stride
assert block_page_stride > 0
self.indexer(
index_query,
attention_block_table=d.block_table,
sparse_block_table_out=decode_sparse_table[0],
sparse_context_lens_out=decode_sparse_table[1],
block_page_stride=block_page_stride,
)
else:
self.indexer(index_query)
else:
self.indexer(index_query)
if self.use_aiter_sparse_pa:
assert isinstance(self.impl, MiniMaxM3SparseAiterPAImpl)
return self.impl.forward(
self,
query,
self.kv_cache,
output,
decode_sparse_table=decode_sparse_table,
)
return self.impl.forward(self, query, self.kv_cache, output)
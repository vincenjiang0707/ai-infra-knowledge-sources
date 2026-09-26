source: https://docs.vllm.ai/en/latest/api/vllm/models/minimax_m3/nvidia/model/
lastmod: 2026-09-24

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
config: PreTrainedConfig,
layer_id: int,
quant_config: QuantizationConfig | None = None,
prefix: str = "",
cache_config: CacheConfig | None = None,
topk_indices_buffer: torch.Tensor | None = None,
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
# Partial RoPE: rotary_dim == head_dim * partial_rotary_factor.
self.rotary_emb = get_rope(
self.head_dim,
max_position=config.max_position_embeddings,
rope_parameters={
"rope_theta": config.rope_theta,
"partial_rotary_factor": config.partial_rotary_factor,
},
)
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
# Indexer side-cache dtype, mirroring --kv-cache-dtype for the main
# cache (--attention-config '{"indexer_kv_dtype": ...}').
self.indexer_kv_dtype = vllm_config.attention_config.resolve_indexer_kv_dtype(
"bf16"
)
# Shared top-k buffer: the indexer writes the selected blocks into it and
# the attend impl reads them back (so nothing crosses the eager break as a
# Python value, which would freeze at capture).
self.topk_indices_buffer = topk_indices_buffer
# Indexer (top-k selection) and main attention are separate impls, each
# picking Triton vs MSA off its cache dtype. impl is AttentionImplBase
# (broader than the AttentionImpl that AttentionLayerBase annotates).
self.attn_backend, impl_cls = select_main_backend_and_impl_cls(
topk_blocks=sparse_cfg["sparse_topk_blocks"],
kv_cache_dtype=self.kv_cache_dtype,
num_kv_heads=self.num_kv_heads,
)
self.impl: MiniMaxM3SparseImpl = impl_cls( # type: ignore[assignment]
self.num_heads,
self.head_dim,
self.scaling,
self.num_kv_heads,
kv_cache_dtype=self.kv_cache_dtype,
topk_blocks=sparse_cfg["sparse_topk_blocks"],
sparse_block_size=sparse_cfg["sparse_block_size"],
msa_decode_backend=(
vllm_config.attention_config.minimax_m3_msa_decode_backend
),
)
# Self-contained nn.Module: owns its side cache, selects its impl in init.
self.indexer = MiniMaxM3Indexer(
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
return FullAttentionSpec(
block_size=vllm_config.cache_config.block_size,
num_kv_heads=self.num_kv_heads,
head_size=self.head_dim,
head_size_v=self.head_dim,
dtype=self.kv_cache_torch_dtype,
kv_quant_mode=get_kv_quant_mode(self.kv_cache_dtype),
)
def _allocate_query_fp8(self, qkv: torch.Tensor) -> torch.Tensor | None:
if not getattr(self.impl, "use_cutlass_decode", False):
return None
return torch.empty(
(qkv.shape[0], self.q_size),
dtype=torch.float8_e4m3fn,
device=qkv.device,
)
def forward(
self,
positions: torch.Tensor,
hidden_states: torch.Tensor,
) -> torch.Tensor:
# Single fused projection emitting [q | k | v | index_q | index_k].
qkv, _ = self.qkv_proj(hidden_states)
# Horizontally-fused per-head Gemma QK-norm + partial NeoX RoPE on the
# main (q/k) and index (index_q/index_k) branches, all read straight out
# of the single fused ``qkv`` tensor (the "5 results"). Once the paged
# caches are bound the kernel also inserts k/v and the index key into
# them; the initial memory-profiling run (caches unbound, no slot_mapping)
# short-circuits to zeros below. k/v and index_k are rewritten in place
# inside qkv (and scatter-inserted into the caches); q and index_q are
# de-interleaved
# straight into the dedicated contiguous ``q``/``index_q`` buffers below.
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
index_slot_mapping = fwd_slot_mapping[self.indexer.index_cache.prefix]
q = qkv.new_empty((num_tokens, self.q_size))
query_fp8 = self._allocate_query_fp8(qkv)
# index_q matches the index-K cache dtype (e4m3 for the fp8 score path);
# the fused kernel emits fp8 directly when this buffer is e4m3.
index_q = qkv.new_empty(
(num_tokens, self.index_q_size),
dtype=self.indexer.index_cache.dtype,
)
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
q_fp8_out=query_fp8,
q_fp8_scale=self._q_scale_float,
)
output = torch.empty_like(q)
attn_output = self._run_attention(q, query_fp8, index_q, output)
output, _ = self.o_proj(attn_output)
return output
@eager_break_during_capture
def _run_attention(
self,
query: torch.Tensor,
query_fp8: torch.Tensor | None,
index_query: torch.Tensor,
output: torch.Tensor,
) -> torch.Tensor:
# Single eager break around both: their split-K kernels read per-request
# metadata and can't be captured into a cudagraph. The indexer writes its
# top-k into the shared ``topk_indices_buffer``; the attend reads it back.
self.indexer(index_query)
return self.impl.forward(
self,
query,
self.kv_cache,
output,
query_fp8=query_fp8,
)
source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/attention/
lastmod: 2026-09-24

class DeepseekV4Attention(nn.Module, AttentionLayerBase, ABC):
"""DeepseekV4 MLA attention layer.
The platform-specific sparse-MLA forward (``forward_mqa`` /
``get_padded_num_q_heads`` / ``_o_proj`` / ``backend_cls``) is provided by a
subclass — ``DeepseekV4FlashMLAAttention`` /
``DeepseekV4FlashInferSM120Attention`` /
``DeepseekV4FlashInferMLAAttention`` (CUDA) or
``DeepseekV41ROCMAiterMLAAttention`` (ROCm) — selected by the platform-specific
deepseek_v41 model module. The base is never instantiated directly.
"""
# Provided by the platform subclass.
backend_cls: ClassVar[type[AttentionBackend]]
# Backend for the SWA cache layer; None uses the default SWA backend.
swa_backend_cls: ClassVar[type[AttentionBackend] | None] = None
# KV-cache per-token block format (both layouts are paged). True (default)
# = fp8_ds_mla (UE8M0 block-scaled fp8 packed as uint8); False = plain
# bf16 / per-tensor fp8 KV row. Backends can override the instance hook when
# a single attention class dispatches across arch-specific layouts.
use_fp8_ds_mla_layout: ClassVar[bool] = True
# Prefill is processed in fixed-size chunks; this bounds the bf16 kv-gather
# workspace allocated in _forward_prefill and is also read by the dummy-run
# path to pre-reserve that workspace.
PREFILL_CHUNK_SIZE: ClassVar[int] = 4
# ---- attention-interface contract, declared by the platform subclass ----
@property
def accepts_unnormed_unroped_query(self) -> bool:
"""Whether ``forward_mqa``'s ``q`` is the raw ``wq_b`` output.
True when the attention kernel applies the Q norm and RoPE itself, and
reads Q in its own chunk-interleaved layout, so the layer only
zero-pads Q to ``padded_heads`` and inserts KV before calling it.
"""
return False
@property
def packed_kv_cache_dtype(self) -> CacheDType:
"""The packed KV record this layer's kernel prefers.
What an unspecific ``--kv-cache-dtype`` (``auto`` / ``fp8``) resolves
to. Mega attention overrides it: its kernel is the one that can read
an NVFP4 compressed cache.
"""
return "fp8_ds_mla"
@classmethod
@abstractmethod
def get_padded_num_q_heads(cls, num_heads: int) -> int:
"""Q head count the q/output buffers are allocated at.
The layer allocates the q/output buffers at
``[N, get_padded_num_q_heads(n_local_heads), head_dim]``. Must satisfy
``result >= num_heads``. Backends with no padding constraint return
``num_heads``.
"""
raise NotImplementedError
@abstractmethod
def forward_mqa(
self,
q: torch.Tensor,
kv: torch.Tensor,
positions: torch.Tensor,
output: torch.Tensor,
) -> None:
"""Platform-specific sparse MLA forward; writes attention into ``output``."""
raise NotImplementedError
@abstractmethod
def _o_proj(
self,
attn_out: "torch.Tensor | QuantizedActivation",
positions: torch.Tensor,
) -> torch.Tensor:
"""Project whatever ``_alloc_attn_out`` produced through wo_a and wo_b.
Takes the buffer whole, so each layer owns the shape it allocated: the
bf16 layers slice off their padding heads and apply the inverse RoPE,
while a layer whose attention kernel already did the inverse RoPE and
the FP8 cast gets a QuantizedActivation and has only wo_a and wo_b
left.
"""
raise NotImplementedError
def _uses_fp8_ds_mla_layout(self) -> bool:
"""Return whether this instance stores fp8 KV in fp8_ds_mla layout."""
return self.use_fp8_ds_mla_layout
def __init__(
self,
vllm_config: VllmConfig,
prefix: str,
topk_indices_buffer: torch.Tensor | None = None,
aux_stream_list: list[torch.cuda.Stream] | None = None,
candidate_block_buffer: torch.Tensor | None = None,
) -> None:
super().__init__()
config = vllm_config.model_config.hf_config
quant_config = vllm_config.quant_config
cache_config = vllm_config.cache_config
tp_size = get_tensor_model_parallel_world_size()
layer_id = extract_layer_index(prefix)
self.layer_id = layer_id
self.prefix = prefix # Alias for compatibility with compressor
self.hidden_size = config.hidden_size
self.n_heads = config.num_attention_heads
assert self.n_heads % tp_size == 0
self.n_local_heads = self.n_heads // tp_size
self.q_lora_rank = config.q_lora_rank
self.o_lora_rank = config.o_lora_rank
self.head_dim = config.head_dim
self.rope_head_dim = config.qk_rope_head_dim
self.nope_head_dim = self.head_dim - self.rope_head_dim
self.n_groups = config.o_groups
self.n_local_groups = self.n_groups // tp_size
self.window_size = config.sliding_window
# ---- v4.1 sparse-attention topology ----
# compress_ratios has one entry per layer (MTP layers included):
# 0 = pure sliding window, 1 = full-length compressed cache,
# 2 = ratio-2 compressed. Compressors and compressed-KV caches live
# only on ``kv_source_layer_ids``; indexers only on
# ``index_source_layer_ids``. Consumers reuse the most recently
# published source below them.
compress_ratios = getattr(config, "compress_ratios", None)
if compress_ratios is not None and layer_id < len(compress_ratios):
self.compress_ratio = int(compress_ratios[layer_id])
else:
# MTP layers past the configured list are pure sliding-window.
self.compress_ratio = 0
if self.compress_ratio not in (0, 1, 2):
raise ValueError(
f"DeepSeek V4.1 layer {layer_id} has compress_ratio="
f"{self.compress_ratio}; only 0 (sliding window), 1 and 2 are "
"supported."
)
self.kv_source_layers = tuple(
getattr(config, "kv_source_layer_ids", None) or ()
)
self.index_source_layers = tuple(
getattr(config, "index_source_layer_ids", None) or ()
)
self.candidate_source_layer = getattr(config, "candidate_source_layer_id", -1)
self.candidate_topk_blocks = getattr(config, "candidate_topk_blocks", 0)
self.candidate_block_size = getattr(config, "candidate_block_size", 0)
is_backbone = layer_id < config.num_hidden_layers
self.is_kv_source = is_backbone and layer_id in self.kv_source_layers
self.is_index_source = is_backbone and layer_id in self.index_source_layers
if self.compress_ratio > 0:
if not self.kv_source_layers or not self.index_source_layers:
raise ValueError(
"DeepSeek V4.1 requires kv_source_layer_ids / "
"index_source_layer_ids in the config for compressed "
f"layers (layer {layer_id} has "
f"compress_ratio={self.compress_ratio})."
)
self.kv_source_layer_id = max(
s for s in self.kv_source_layers if s <= layer_id
)
self.index_source_layer_id = max(
s for s in self.index_source_layers if s <= layer_id
)
else:
self.kv_source_layer_id = None
self.index_source_layer_id = None
self.eps = config.rms_norm_eps
self.scale = self.head_dim**-0.5
# Padded Q head count is dictated by the platform subclass.
self.padded_heads = self.get_padded_num_q_heads(self.n_local_heads)
# Sink padded to the same head count, initialized to -inf (no sink
# effect). Weight loading fills the first n_local_heads slots.
self.attn_sink = nn.Parameter(
torch.full((self.padded_heads,), -float("inf"), dtype=torch.float32),
requires_grad=False,
)
self.fused_wqa_wkv = MergedColumnParallelLinear(
self.hidden_size,
[self.q_lora_rank, self.head_dim],
bias=False,
quant_config=quant_config,
prefix=f"{prefix}.fused_wqa_wkv",
disable_tp=True, # fused ReplicatedLinear
)
self.q_norm = RMSNorm(self.q_lora_rank, self.eps)
self.wq_b = ColumnParallelLinear(
self.q_lora_rank,
self.n_heads * self.head_dim,
bias=False,
quant_config=quant_config,
return_bias=False,
prefix=f"{prefix}.wq_b",
)
self.kv_norm = RMSNorm(self.head_dim, self.eps)
self.wo_a = ColumnParallelLinear(
self.n_heads * self.head_dim // self.n_groups,
self.n_groups * self.o_lora_rank,
bias=False,
quant_config=quant_config,
return_bias=False,
prefix=f"{prefix}.wo_a",
)
self.wo_a.is_bmm = True
self.wo_a.bmm_batch_size = self.n_local_groups
self._o_proj_block_size = (
32 if getattr(self.wo_a, "weight_block_size", None) == [1, 32] else 128
)
self.wo_b = RowParallelLinear(
self.n_groups * self.o_lora_rank,
self.hidden_size,
bias=False,
quant_config=quant_config,
return_bias=False,
prefix=f"{prefix}.wo_b",
)
# Set by ``bind_gemm_rs`` when the decoder layer runs sequence
# parallel and the fused GEMM + reduce-scatter kernel accepts wo_b.
self.gemm_rs: GemmRsAr | None = None
# Initialize rotary embedding before the indexer/compressor consume it.
self.rotary_emb = build_deepseek_v4_rope(
config,
head_dim=self.head_dim,
rope_head_dim=self.rope_head_dim,
max_position_embeddings=config.max_position_embeddings,
compress_ratio=self.compress_ratio,
)
self.indexer_rotary_emb = self.rotary_emb
self.topk_indices_buffer = topk_indices_buffer
self.candidate_block_buffer = candidate_block_buffer
# Register with compilation context for metadata lookup. Done before
# indexer/compressor creation so consumers can resolve their source
# layers through it.
compilation_config = vllm_config.compilation_config
if prefix and prefix in compilation_config.static_forward_context:
raise ValueError(f"Duplicate layer name: {prefix}")
if prefix:
compilation_config.static_forward_context[prefix] = self
self.kv_cache = torch.tensor([])
self._static_forward_context = compilation_config.static_forward_context
self.indexer = None
if self.is_index_source:
index_k_cache: DeepseekV4IndexerCache | None
# Index K cache: owned only by kv-source layers (their indexer has
# wk/k_norm); non-owning index sources share the K cache of the
# latest kv source below them (its indexer produces the keys).
if self.is_kv_source:
index_k_cache = DeepseekV4IndexerCache(
head_dim=_indexer_k_cache_head_dim(
config.index_head_dim, dsa_indexer_uses_fp4(vllm_config)
),
dtype=torch.uint8,
prefix=f"{prefix}.indexer.k_cache",
cache_config=cache_config,
compress_ratio=self.compress_ratio,
)
else:
assert self.kv_source_layer_id is not None
k_cache_prefix = (
f"{_replace_layer_index(prefix, self.kv_source_layer_id)}"
".indexer.k_cache"
)
index_k_cache = self._static_forward_context.get(k_cache_prefix)
if index_k_cache is None:
raise NotImplementedError(
f"Indexer K cache source {k_cache_prefix} not found on "
"this rank; PP splits inside a v4.1 kv-sharing group "
"are not supported."
)
is_candidate_source = layer_id == self.candidate_source_layer
uses_candidates = 0 <= self.candidate_source_layer < layer_id
self.indexer = DeepseekV4Indexer(
vllm_config,
config=config,
hidden_size=self.hidden_size,
q_lora_rank=self.q_lora_rank,
quant_config=quant_config,
cache_config=cache_config,
topk_indices_buffer=topk_indices_buffer,
compress_ratio=self.compress_ratio,
prefix=f"{prefix}.indexer",
owns_k=self.is_kv_source,
k_cache=index_k_cache,
main_head_dim=self.head_dim,
candidate_block_buffer=(
candidate_block_buffer
if (is_candidate_source or uses_candidates)
else None
),
candidate_block_size=self.candidate_block_size,
candidate_write=is_candidate_source,
)
self._prepare_and_attn_fn = self._prepare_and_attn
if not vllm_config.use_v2_model_runner:
# MRV1's piecewise capture only tolerates the wide eager region: with
# the narrow one the attention input preparation stays in the captured
# graph and MRV1 produces garbage (#51430).
self._prepare_and_attn_fn = self._prepare_and_attn_eager
# Will be None on ROCm for now.
self.aux_stream_list = aux_stream_list
# [0]: GEMM start / post-GEMM event0. [1..3]: GEMM done events;
# [1] doubles as post-GEMM event1. Reuse is safe: GEMM fully joins
# before post-GEMM starts.
self.ln_events = [torch.cuda.Event() for _ in range(4)]
assert cache_config is not None, "DeepseekV4 attention requires cache_config"
# ---- Attention / KV-cache setup ----
self.max_num_batched_tokens = (
vllm_config.scheduler_config.max_num_batched_tokens
)
self.max_model_len = vllm_config.model_config.max_model_len
# Resolve the kv-cache dtype from this backend's block format. The same
# resolution drives the SWA cache tensor dtype below.
self.kv_cache_dtype, self.kv_cache_torch_dtype = _resolve_dsv4_kv_cache_dtype(
self._uses_fp8_ds_mla_layout(),
cache_config.cache_dtype,
cache_config,
self.packed_kv_cache_dtype,
)
self.kv_mxfp8 = _use_v41_mxfp8_kv_record()
self.swa_bytes_per_token = 528 if self.kv_mxfp8 else 584
# nvfp4_ds_mla keeps the MXFP8 sliding-window record and stores the
# compressed cache as NVFP4 (256 B of e2m1 pairs + 32 e4m3 scales).
self.compressed_bytes_per_token = (
288 if self.kv_cache_dtype == "nvfp4_ds_mla" else self.swa_bytes_per_token
)
# One alignment for every page in the block: the block stride is their
# sum, and 512 satisfies both TMA strides in play (512 for the V4.1
# fp8 record, 256 for NVFP4).
self.kv_page_alignment = 512 if self.kv_mxfp8 else 576
if self.kv_cache_dtype == "nvfp4_ds_mla" and not self.kv_mxfp8:
raise ValueError(
"nvfp4_ds_mla needs the V4.1 KV records, which FlashMLA "
"decodes only on SM100."
)
swa_bounded_replay = cache_config.swa_bounded_replay
if swa_bounded_replay and not vllm_config.use_v2_model_runner:
logger.warning_once(
"SWA bounded replay needs model runner V2 (only it skips the "
"paged-KV writes of replayed tokens); the sliding-window cache "
"takes part in prefix caching instead."
)
swa_bounded_replay = False
if (
swa_bounded_replay
and vllm_config.parallel_config.prefill_context_parallel_size > 1
):
logger.warning_once(
"SWA bounded replay is off under prefill context parallelism "
"(the replayed tokens' slot padding knows the rank-local batch "
"only); the sliding-window cache takes part in prefix caching "
"instead."
)
swa_bounded_replay = False
if swa_bounded_replay and current_platform.is_rocm():
logger.warning_once(
"SWA bounded replay is off on ROCm (the sparse SWA metadata "
"builders forward replay_start, but the window clamp it relies "
"on lives in the FlashInfer and FlashMLA prefill kernels, so "
"the padded slots fault); the sliding-window cache takes part "
"in prefix caching instead."
)
swa_bounded_replay = False
self.swa_cache_layer = DeepseekV4SWACache(
head_dim=self.head_dim,
window_size=self.window_size,
dtype=self.kv_cache_torch_dtype,
prefix=f"{prefix}.swa_cache",
cache_config=cache_config,
backend_cls=self.swa_backend_cls,
block_size=32,
packed_bytes_per_token=self.swa_bytes_per_token,
packed_page_alignment=self.kv_page_alignment,
bounded_replay=swa_bounded_replay,
)
# The attention layer itself was already registered with the
# compilation context above (before indexer/compressor creation).
# Compressors live only on kv-source layers; consumers read the
# source's compressed cache through the forward context.
self.compressor = None
if self.is_kv_source:
self.compressor = DeepseekCompressor(
vllm_config=vllm_config,
compress_ratio=self.compress_ratio,
hidden_size=self.hidden_size,
head_dim=self.head_dim,
rotate=True,
prefix=f"{prefix}.compressor",
k_cache_prefix=self.prefix,
)
# Prefix of the attention layer owning this layer's compressed KV
# cache (self for kv sources).
if self.compress_ratio > 0:
assert self.kv_source_layer_id is not None
self.compressed_cache_prefix: str | None = _replace_layer_index(
prefix, self.kv_source_layer_id
)
if (
not self.is_kv_source
and self.compressed_cache_prefix not in self._static_forward_context
):
raise NotImplementedError(
f"Compressed-KV source {self.compressed_cache_prefix} not "
"found on this rank; PP splits inside a v4.1 kv-sharing "
"group are not supported."
)
else:
self.compressed_cache_prefix = None
if vllm_config.kernel_config.enable_jit_warmup:
from vllm.v1.attention.backends.mla.sparse_swa import (
_COMPUTE_PREFILL_METADATA_KERNEL,
_COMPUTE_SWA_INDICES_AND_LENS_KERNEL,
)
_COMPUTE_PREFILL_METADATA_KERNEL.register_warmup()
_COMPUTE_SWA_INDICES_AND_LENS_KERNEL.register_warmup(
window_size=self.window_size,
block_size=self.swa_cache_layer.block_size,
)
if self.compress_ratio > 1:
from vllm.v1.attention.backends.mla.compressor_utils import (
_COMPRESSED_SLOT_MAPPING_KERNEL,
)
_COMPRESSED_SLOT_MAPPING_KERNEL.register_warmup()
if self.indexer is not None:
from vllm.v1.attention.backends.mla.indexer import (
_BUILD_PREFILL_CHUNK_METADATA_KERNEL,
_PREPARE_UNIFORM_DECODE_KERNEL,
)
_PREPARE_UNIFORM_DECODE_KERNEL.register_warmup()
_BUILD_PREFILL_CHUNK_METADATA_KERNEL.register_warmup()
spec_config = vllm_config.speculative_config
if spec_config is not None and spec_config.use_dspark():
from vllm.v1.attention.backends.mla.sparse_swa import (
_COMPUTE_DSPARK_NONCAUSAL_SWA_INDICES_KERNEL,
)
_COMPUTE_DSPARK_NONCAUSAL_SWA_INDICES_KERNEL.register_warmup(
window_size=self.window_size,
num_speculative_tokens=spec_config.num_speculative_tokens,
block_size=self.swa_cache_layer.block_size,
)
# Every backend that gathers a chunk's KV through
# combine_topk_swa_indices needs its Triton kernel warmed, mega
# attention included -- it calls it from _forward_prefill_mega.
if self.backend_cls.get_name() in (
"FLASHMLA_SPARSE_DSV41",
"FLASHMLA_MEGA_ATTN_DSV41",
"ROCM_FLASHMLA_SPARSE_DSV4",
):
from vllm.models.deepseek_v41.common.ops.cache_utils import (
_COMBINE_TOPK_SWA_INDICES_KERNEL,
)
_COMBINE_TOPK_SWA_INDICES_KERNEL.register_warmup()
def forward(
self,
positions: torch.Tensor,
hidden_states: torch.Tensor,
llama_4_scaling: torch.Tensor | None = None,
) -> torch.Tensor:
# The eager attention region writes into a caller-owned buffer
# (breakable_cudagraph needs in-place outputs); its shape and how it is
# projected afterwards follow the interface contract above.
attn_out = self._alloc_attn_out(hidden_states.shape[0], hidden_states)
# Keep the attention input preparation in the captured graph. Only the
# sparse indexer and MLA attention run in the eager break below.
qr_kv, kv_score, indexer_weights = self._run_parallel_input_projections(
hidden_states
)
qr, qr_scale, kv = self._split_qkv_and_norm(qr_kv)
self._prepare_and_attn_fn(
hidden_states,
qr,
kv,
qr_scale,
kv_score,
indexer_weights,
positions,
attn_out,
)
return self._o_proj(attn_out, positions)
def bind_gemm_rs(self) -> None:
"""Fuse ``wo_b`` with the sequence-parallel TP reduce-scatter.
The decoder layer calls this after the model initialized the
process-wide GEMM-RS workspace and before weights load: the
eligibility check inspects the projection's linear kernel and weight
shape, which online quantization may later re-layout.
"""
from vllm.model_executor.kernels.linear.cute_dsl.gemm_rs_ar import (
get_gemm_rs_ar,
)
# The layer owns the reduction under sequence parallel.
assert not self.wo_b.reduce_results
gemm_rs = get_gemm_rs_ar()
if gemm_rs.can_run(self.wo_b):
self.gemm_rs = gemm_rs
else:
gemm_rs.warn_incompatible_projection()
def _wo_b_proj(self, z: torch.Tensor) -> torch.Tensor:
"""Apply ``wo_b``; with GEMM-RS bound, also reduce-scatter the result.
Every ``_o_proj`` implementation projects through this so the decoder
layer sees one contract: when ``gemm_rs`` is bound the output is
already the local sequence-parallel shard, otherwise it is the
unreduced TP partial.
"""
if self.gemm_rs is None:
return self.wo_b(z)
if self.gemm_rs.should_run(z):
return self.gemm_rs.apply(z, self.wo_b)
# Small batches stay on the unfused path, which is faster there.
return sp_reduce_scatter(self.wo_b(z))
def _alloc_attn_out(
self, num_tokens: int, hidden_states: torch.Tensor
) -> "torch.Tensor | QuantizedActivation":
"""The buffer ``forward_mqa`` fills, per the interface contract."""
return torch.empty(
(num_tokens, self.padded_heads, self.head_dim),
dtype=hidden_states.dtype,
device=hidden_states.device,
)
@cached_property
def _can_fuse_query_quant(self) -> bool:
from vllm.models.deepseek_v41.common.ops.query_quant import (
can_fuse_query_quant,
)
linears = [self.wq_b]
if self.indexer is not None:
linears.append(self.indexer.wq_b)
return can_fuse_query_quant(linears)
def _split_qkv_and_norm(
self, qr_kv: torch.Tensor
) -> tuple[torch.Tensor | QuantizedActivation, torch.Tensor | None, torch.Tensor]:
"""Split the fused q-lora / kv projection and RMSNorm both halves.
Compatible MXFP8 projections share the quantized Q and scales;
other projection backends consume the normalized Q directly.
"""
qr, kv = qr_kv.split([self.q_lora_rank, self.head_dim], dim=-1)
if self.q_lora_rank % 32 == 0 and self._can_fuse_query_quant:
from vllm.models.deepseek_v41.common.ops.query_quant import (
fused_q_kv_rmsnorm_quant,
)
qr_quant, kv = fused_q_kv_rmsnorm_quant(
qr,
kv,
self.q_norm.weight.data,
self.kv_norm.weight.data,
self.eps,
)
return qr_quant, None, kv
qr, kv = fused_q_kv_rmsnorm(
qr,
kv,
self.q_norm.weight.data,
self.kv_norm.weight.data,
self.eps,
)
return qr, None, kv
@eager_break_during_capture
def _prepare_and_attn_eager(
self,
hidden_states: torch.Tensor,
qr: torch.Tensor | QuantizedActivation,
kv: torch.Tensor,
qr_scale: torch.Tensor | None,
kv_score: torch.Tensor,
indexer_weights: torch.Tensor,
positions: torch.Tensor,
attn_out: "torch.Tensor | QuantizedActivation",
) -> None:
"""Wide eager region: the whole of ``_prepare_and_attn`` runs eagerly.
The nested ``_sparse_indexer_and_attn`` break runs inline, since
``add_eager`` clears ``_capturing`` before invoking this.
"""
self._prepare_and_attn(
hidden_states,
qr,
kv,
qr_scale,
kv_score,
indexer_weights,
positions,
attn_out,
)
def _prepare_and_attn(
self,
hidden_states: torch.Tensor,
qr: torch.Tensor | QuantizedActivation,
kv: torch.Tensor,
qr_scale: torch.Tensor | None,
kv_score: torch.Tensor,
indexer_weights: torch.Tensor,
positions: torch.Tensor,
attn_out: "torch.Tensor | QuantizedActivation",
) -> None:
"""Attention input preparation followed by the sparse indexer and MLA.
Only the latter runs in the eager break.
Q/SWA preparation overlaps state saving and compression. Once the
latent is ready, main-cache insertion overlaps indexer preparation;
both cache writes finish before sparse attention reads either cache.
"""
attn_metadata = get_forward_context().attn_metadata
indexer = self.indexer
compressor = self.compressor
aux_streams = self.aux_stream_list
def project_query_and_cache_kv() -> torch.Tensor:
q = self._wq_b_proj(qr, qr_scale).view(
-1, self.n_local_heads, self.head_dim
)
return self._fused_qnorm_rope_kv_insert(q, kv, positions, attn_metadata)
index_q: torch.Tensor | None = None
index_q_scale: torch.Tensor | None = None
index_weights_out: torch.Tensor | None = None
latent: torch.Tensor | None = None
aux_stream = aux_streams[0] if aux_streams is not None else None
if compressor is not None:
# Q projection / KV insertion on the default stream overlaps the
# compressor on aux stream 0 (sequential on ROCm).
q, latent = maybe_execute_in_parallel(
project_query_and_cache_kv,
lambda: compressor(kv_score, positions),
self.ln_events[0],
self.ln_events[1],
aux_stream,
)
else:
q = project_query_and_cache_kv()
def prepare_indexer():
if indexer is None:
return None, None, None
return indexer(
qr,
latent,
indexer_weights,
positions,
self.indexer_rotary_emb,
qr_scale,
)
if compressor is not None:
indexer_result, _ = maybe_execute_in_parallel(
prepare_indexer,
lambda: compressor.insert_cache(latent, positions, self.rotary_emb),
self.ln_events[0],
self.ln_events[1],
aux_stream,
)
else:
indexer_result = prepare_indexer()
index_q, index_q_scale, index_weights_out = indexer_result
self._sparse_indexer_and_attn(
hidden_states,
index_q,
index_q_scale,
index_weights_out,
q,
kv,
positions,
attn_out,
)
def _fused_wqa_wkv_gemm(self, hidden_states: torch.Tensor) -> torch.Tensor:
# Override point: the ROCm layer preshuffles this weight in place, so
# it cannot go through fused_wqa_wkv directly.
# MergedColumnParallelLinear returns (output, bias); bias is None.
qr_kv, _ = self.fused_wqa_wkv(hidden_states)
return qr_kv
def _wq_b_proj(
self,
qr: torch.Tensor | QuantizedActivation,
qr_scale: torch.Tensor | None = None,
) -> torch.Tensor:
"""Project normalized Q, bypassing quantization when already fused."""
assert qr_scale is None, "ROCm-only path"
return self.wq_b(qr)
def _run_parallel_input_projections(
self, hidden_states: torch.Tensor
) -> tuple[
torch.Tensor,
torch.Tensor | None,
torch.Tensor | None,
]:
aux_streams = self.aux_stream_list
if aux_streams is not None:
aux_streams = aux_streams[:2]
# fused_wqa_wkv (heaviest) on default; the two lighter input GEMMs on
# aux streams 0/1 when their owning module exists. ln_events[0] is the
# fan-out start event; ln_events[1..2] are per-aux done events. The
# v4.1 indexer derives K from the kv-source compressor's latent, so
# unlike v4.0 there is no indexer K GEMM over hidden_states here.
aux_fns: list[Callable[[], Any] | None] = [None, None]
if self.compressor is not None:
# Local ref so the closure keeps a non-None type for mypy.
compressor = self.compressor
def compressor_kv_score() -> torch.Tensor:
return torch.mm(
hidden_states,
compressor.fused_wkv_wgate.weight.T,
out_dtype=torch.float32,
)
aux_fns[0] = compressor_kv_score
if self.indexer is not None:
indexer = self.indexer
def indexer_weights_proj() -> torch.Tensor:
# ReplicatedLinear returns (output, bias); bias is None.
weights, _ = indexer.weights_proj(hidden_states)
return weights
aux_fns[1] = indexer_weights_proj
qr_kv, (kv_score, indexer_weights) = execute_in_parallel(
lambda: self._fused_wqa_wkv_gemm(hidden_states),
aux_fns,
self.ln_events[0],
self.ln_events[1:3],
aux_streams,
enable=hidden_states.shape[0]
<= envs.VLLM_MULTI_STREAM_GEMM_TOKEN_THRESHOLD,
)
return qr_kv, kv_score, indexer_weights
@eager_break_during_capture
def _sparse_indexer_and_attn(
self,
hidden_states: torch.Tensor,
index_q: torch.Tensor | None,
index_q_scale: torch.Tensor | None,
index_weights: torch.Tensor | None,
q: torch.Tensor,
kv: torch.Tensor,
positions: torch.Tensor,
out: torch.Tensor,
) -> None:
if self.indexer is not None and index_q is not None:
assert index_weights is not None
q_quant = (index_q, index_q_scale) if index_q_scale is not None else index_q
self.indexer.indexer_op(
hidden_states,
q_quant,
None,
index_weights,
)
# MLA attention writes into the pre-allocated `out` buffer
# ([num_tokens, padded_heads, head_dim]).
self.forward_mqa(q, kv, positions, out)
def _fused_qnorm_rope_kv_insert(
self,
q: torch.Tensor,
kv: torch.Tensor,
positions: torch.Tensor,
attn_metadata: (
dict[str, AttentionMetadata] | list[dict[str, AttentionMetadata]] | None
),
) -> torch.Tensor:
"""Ready ``q`` for the attention kernel and publish this step's KV.
One launch does both. With ``accepts_unnormed_unroped_query`` the
attention kernel norms and rotates Q itself and reads it in its own
chunk-interleaved layout, so the Q half of the launch is a zero-pad to
``padded_heads`` -- and nothing at all once the shard is that wide.
"""
if not isinstance(attn_metadata, dict):
# Profile run: kernel doesn't fire; produce a padded tensor so
# downstream FlashMLA gets the right shape.
if self.n_local_heads >= self.padded_heads:
return q
if self.accepts_unnormed_unroped_query:
# Padding heads sit at the tail of every head-dim chunk in
# that layout, so no head-major pad of `q` reproduces it --
# and nothing reads it on a profile run.
return q.new_zeros((q.shape[0], self.padded_heads, q.shape[2]))
return F.pad(
q,
(0, 0, 0, self.padded_heads - self.n_local_heads),
value=0.0,
)
swa_metadata = cast(
"DeepseekSparseSWAMetadata | None",
attn_metadata.get(self.swa_cache_layer.prefix),
)
assert swa_metadata is not None
swa_kv_cache = self.swa_cache_layer.kv_cache
# The fused insert ops require int64 position_ids; the runner's positions
# buffer is already int64, so no cast is needed.
assert positions.dtype == torch.int64
cos_sin_cache = self.rotary_emb.cos_sin_cache
cache_dtype = swa_kv_cache.dtype
# kv is unchanged; attention reads kv solely via swa_kv_cache.
if cache_dtype == torch.uint8:
# fp8_ds_mla UE8M0 paged path. Horizontally fused:
# Q side: GPT-J RoPE, zero-filling the padding head slots; the
# kernel allocates and returns the padded q tensor. An
# interleaved Q skips the RoPE its attention kernel owns
# and keeps only the pad, which q_head_padded=0 drops
# too once the shard is already padded_heads wide.
# KV side: GPT-J RoPE + UE8M0 FP8 quant + paged cache insert.
swa_kv_cache_2d = swa_kv_cache.view(swa_kv_cache.shape[0], -1)
pad_to = (
0
if self.accepts_unnormed_unroped_query
and self.n_local_heads == self.padded_heads
else self.padded_heads
)
q_padded = torch.ops._C.fused_deepseek_v4_qnorm_rope_kv_rope_quant_insert(
q,
kv,
swa_kv_cache_2d,
swa_metadata.slot_mapping,
positions,
cos_sin_cache,
pad_to,
self.eps,
swa_metadata.block_size,
False, # apply_q_norm: qr is normed before wq_b
self.kv_mxfp8,
not self.accepts_unnormed_unroped_query, # apply_q_rope
self.accepts_unnormed_unroped_query, # is_q_interleaved
)
return q if pad_to == 0 else q_padded
assert not self.accepts_unnormed_unroped_query, (
"the chunk-interleaved Q layout only pairs with a packed KV record"
)
# Plain-row path: the [num_blocks, block_size, 512] cache stores the KV
# row in its element dtype (no Q padding). bf16 rewrites q in place;
# per-tensor fp8 writes a separately-allocated fp8 q and quantizes the
# KV row.
block_size = swa_metadata.block_size
assert swa_kv_cache.shape[1:] == (block_size, self.head_dim)
swa_kv_cache_3d = swa_kv_cache
if cache_dtype == torch.bfloat16:
torch.ops._C.fused_deepseek_v4_qnorm_rope_kv_rope_full_cache_bf16_insert(
q,
kv,
swa_kv_cache_3d,
swa_metadata.slot_mapping,
positions,
cos_sin_cache,
self.eps,
block_size,
False,
)
return q
# per-tensor fp8 (torch.float8_e4m3fn)
q_fp8 = torch.empty_like(q, dtype=torch.float8_e4m3fn)
torch.ops._C.fused_deepseek_v4_qnorm_rope_kv_rope_full_cache_fp8_insert(
q,
kv,
q_fp8,
swa_kv_cache_3d,
swa_metadata.slot_mapping,
positions,
cos_sin_cache,
self._flashinfer_fp8_kv_scale,
self._flashinfer_fp8_q_scale_inv,
self.eps,
block_size,
False,
)
return q_fp8
def bind_kv_cache(self, kv_cache: torch.Tensor) -> None:
# [B, H=1, N, C] -> [B, N, C]
self.kv_cache = kv_cache.squeeze(1)
def get_attn_backend(self) -> type[AttentionBackend]:
return self.backend_cls
def get_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCacheSpec | None:
# Only kv-source layers own a compressed-KV cache; consumers read the
# source's cache through the forward context, and cr==0 layers are
# pure SWA. The SWA cache is allocated separately as
# DeepseekV4SWACache.
if not self.is_kv_source:
return None
# fp8_ds_mla is a UE8M0 block-scaled uint8 layout whose page rounds up
# to the decode kernel's TMA stride; plain bf16 / per-tensor fp8 rows
# use natural element-size pages.
uses_fp8_ds_mla_layout = self.kv_cache_dtype in ("fp8_ds_mla", "nvfp4_ds_mla")
return MLAAttentionSpec(
block_size=vllm_config.cache_config.block_size,
num_kv_heads=1,
head_size=self.head_dim,
dtype=torch.uint8 if uses_fp8_ds_mla_layout else self.kv_cache_torch_dtype,
tokens_per_state=self.compress_ratio,
cache_dtype_str=self.kv_cache_dtype,
alignment=self.kv_page_alignment if uses_fp8_ds_mla_layout else 512,
model_version="deepseek_v4",
kv_quant_mode=get_kv_quant_mode(self.kv_cache_dtype),
# Packed record width; head_size stays semantic (512).
state_content_bytes=(
self.compressed_bytes_per_token if uses_fp8_ds_mla_layout else None
),
)
def _compressed_kv_cache(self) -> torch.Tensor:
"""The compressed-KV cache tensor of this layer's kv source (own
cache for kv-source layers)."""
if self.is_kv_source:
return self.kv_cache
assert self.compressed_cache_prefix is not None
source = self._static_forward_context[self.compressed_cache_prefix]
return source.kv_cache
source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/sparse_attn_indexer/
lastmod: 2026-09-23

@CustomOp.register("sparse_attn_indexer")
class SparseAttnIndexer(CustomOp):
"""Sparse Attention Indexer Custom Op Layer. This layer is extracted as a
separate custom op since it involves heavy custom kernels like `mqa_logits`,
`paged_mqa_logits` and `top_k_per_row`, etc. Those kernels maybe requires
specific memory layout or implementation for different hardware backends to
achieve optimal performance.
For now, the default native path will use CUDA backend path. Other platform
may requires add the corresponding Custom Op name `sparse_attn_indexer` to
`custom_ops` in `CompilationConfig` to enable the platform specific path.
"""
def __init__(
self,
k_cache,
quant_block_size: int,
scale_fmt: str,
topk_tokens: int,
head_dim: int,
max_model_len: int,
max_total_seq_len: int,
topk_indices_buffer: torch.Tensor,
skip_k_cache_insert: bool = False,
use_fp4_cache: bool = False,
compress_ratio: int = 1,
candidate_blocks: torch.Tensor | None = None,
candidate_block_size: int = 0,
candidate_write: bool = False,
):
super().__init__()
self.k_cache = k_cache
self.quant_block_size = quant_block_size
self.scale_fmt = scale_fmt
self.topk_tokens = topk_tokens
self.head_dim = head_dim
self.max_model_len = max_model_len
self.max_total_seq_len = max_total_seq_len
self.topk_indices_buffer = topk_indices_buffer
self.skip_k_cache_insert = skip_k_cache_insert
self.use_fp4_cache = use_fp4_cache
self.compress_ratio = compress_ratio
# v4.1 two-level selection: the candidate source indexer writes the
# top candidate blocks here; later indexers mask their scores with it.
self.candidate_blocks = candidate_blocks
self.candidate_block_size = candidate_block_size
self.candidate_write = candidate_write
self.dense_mha_metadata_layer_name = ""
# DCP scalars are constant for the run; resolve them here (config is set
# during model construction) and pass them into the custom op, rather
# than threading them through per-step metadata.
vllm_config = get_current_vllm_config()
parallel_config = vllm_config.parallel_config
self.topk_backend = vllm_config.kernel_config.sparse_indexer_topk_backend
self._parallel_config = parallel_config
self.dcp_world_size = parallel_config.decode_context_parallel_size
self.dcp_rank = get_dcp_group().rank_in_group if self.dcp_world_size > 1 else 0
self.use_pcp = parallel_config.prefill_context_parallel_size > 1
self._cp_kv_cache_interleave_size: int | None = None
if current_platform.is_cuda() and not has_deep_gemm():
raise RuntimeError(
"Sparse Attention Indexer CUDA op requires DeepGEMM support in "
"the current vLLM environment."
)
if vllm_config.kernel_config.enable_jit_warmup:
from vllm.v1.attention.ops.common import (
_PACK_SEQ_TRITON_KERNEL,
_UNPACK_SEQ_TRITON_KERNEL,
)
pack_dtype = torch.uint8 if use_fp4_cache else current_platform.fp8_dtype()
_PACK_SEQ_TRITON_KERNEL.register_warmup(
dtype=pack_dtype,
pad_value=0 if use_fp4_cache else -float("inf"),
)
_UNPACK_SEQ_TRITON_KERNEL.register_warmup()
if self.dcp_world_size > 1 and current_platform.is_cuda() and has_cutedsl():
from vllm.model_executor.kernels.attention.dsa.dcp_indexer_cutedsl import ( # noqa: E501
_PACK_DCP_TOPK_CANDIDATES_KERNEL,
_STABLE_TOPK_FROM_GATHERED_CANDIDATES_KERNEL,
)
_PACK_DCP_TOPK_CANDIDATES_KERNEL.register_warmup()
_STABLE_TOPK_FROM_GATHERED_CANDIDATES_KERNEL.register_warmup()
@property
def cp_kv_cache_interleave_size(self) -> int:
"""With PD+DCP, the real value isn't known until block_size is finalized,
which happens after this layer is built. Safe to cache after the first access,
as long as the adjustment always runs before any forward pass
(it's set up in Worker.initialize_from_config, ahead of warmup/serving).
"""
if self._cp_kv_cache_interleave_size is None:
value = self._parallel_config.cp_kv_cache_interleave_size
if isinstance(get_forward_context().attn_metadata, dict):
self._cp_kv_cache_interleave_size = value
return value
return self._cp_kv_cache_interleave_size
def forward_native(
self,
hidden_states: torch.Tensor,
q_quant: torch.Tensor | tuple[torch.Tensor, torch.Tensor],
k: torch.Tensor | None,
weights: torch.Tensor,
):
if current_platform.is_cuda() or current_platform.is_xpu():
return self.forward_cuda(hidden_states, q_quant, k, weights)
elif current_platform.is_rocm():
if self.use_pcp and self.dcp_world_size > 1:
raise NotImplementedError(
"The ROCm sparse-indexer path does not support PCP+DCP."
)
return self.forward_hip(hidden_states, q_quant, k, weights)
elif current_platform.is_cpu():
return self.forward_cpu(hidden_states, q_quant, k, weights)
else:
raise NotImplementedError(
"SparseAttnIndexer native forward is only implemented for "
"CUDA, ROCm, XPU and CPU platforms."
)
def forward_cuda(
self,
hidden_states: torch.Tensor,
q_quant: torch.Tensor | tuple[torch.Tensor, torch.Tensor],
k: torch.Tensor | None,
weights: torch.Tensor,
):
# FP8 path: single tensor (per-token scale is folded into `weights`).
# FP4 path: (values, scales) tuple with scales required by the kernel.
if isinstance(q_quant, tuple):
q_values, q_scale = q_quant
else:
q_values, q_scale = q_quant, None
return torch.ops.vllm.sparse_attn_indexer(
hidden_states,
_encode_layer_name(self.k_cache.prefix),
self.k_cache.kv_cache,
q_values,
q_scale,
k,
weights,
self.quant_block_size,
self.scale_fmt,
self.topk_tokens,
self.head_dim,
self.max_model_len,
self.max_total_seq_len,
self.topk_indices_buffer,
self.skip_k_cache_insert,
self.use_pcp,
_encode_layer_name(self.dense_mha_metadata_layer_name),
self.use_fp4_cache,
self.dcp_rank,
self.dcp_world_size,
self.cp_kv_cache_interleave_size,
False,
candidate_blocks=self.candidate_blocks,
candidate_block_size=self.candidate_block_size,
candidate_write=self.candidate_write,
topk_backend=self.topk_backend,
)
def forward_xpu(
self,
hidden_states: torch.Tensor,
q_fp8: torch.Tensor,
k: torch.Tensor | None,
weights: torch.Tensor,
):
return self.forward_cuda(hidden_states, q_fp8, k, weights)
def forward_hip(
self,
hidden_states: torch.Tensor,
q_quant: torch.Tensor | tuple[torch.Tensor, torch.Tensor],
k: torch.Tensor | None,
weights: torch.Tensor,
):
assert not self.use_fp4_cache, "AMD platform doesn't support fp4 cache yet"
assert isinstance(q_quant, torch.Tensor), (
"AMD sparse_attn_indexer expects a single FP8 q_quant tensor"
)
from vllm.platforms.rocm import on_gfx11, on_gfx950
if (
rocm_aiter_ops.is_enabled()
or rocm_aiter_ops.is_rdna_aiter_enabled()
or on_gfx11()
# The so-called AITER sparse indexer op has a native gfx950 path:
# its cache insert, MQA logits, and top-k fallbacks are implemented
# by local Triton/C++ kernels and do not require the aiter package.
or on_gfx950()
):
return torch.ops.vllm.rocm_aiter_sparse_attn_indexer(
hidden_states,
_encode_layer_name(self.k_cache.prefix),
self.k_cache.kv_cache,
q_quant,
k,
weights,
self.quant_block_size,
self.scale_fmt,
self.topk_tokens,
self.head_dim,
self.max_model_len,
self.max_total_seq_len,
self.topk_indices_buffer,
skip_k_cache_insert=self.skip_k_cache_insert,
compress_ratio=self.compress_ratio,
candidate_blocks=self.candidate_blocks,
candidate_block_size=self.candidate_block_size,
candidate_write=self.candidate_write,
)
raise RuntimeError(
"Sparse attention indexer ROCm path requires AITER or a supported "
"native architecture (gfx950/gfx11)."
)
def forward_cpu(
self,
hidden_states: torch.Tensor,
q_quant: torch.Tensor | tuple[torch.Tensor, torch.Tensor],
k: torch.Tensor | None,
weights: torch.Tensor,
):
"""CPU sparse attention indexer: cache write stays eager Python glue
(own K-cache layout, not shared with the main attention cache
write). PREFILL and DECODE both call the ported
``fp8_paged_mqa_logits_cpu``/``topk_transform_512_cpu`` kernels,
which read the paged K-cache directly via ``page_table`` -- no
eager gather step, no per-request Python loop.
``prefill_metadata.chunks`` always has exactly one entry here:
``DeepseekV4CPUIndexerMetadataBuilder`` overrides the base chunk
split to always return the whole step's prefill batch as one
chunk, since the base chunking only bounds CUDA/XPU's dense M*N
logits tensor and flat K-gather workspace, neither of which this
paged kernel allocates.
"""
assert not self.use_fp4_cache, (
"CPU sparse indexer doesn't support fp4 cache yet"
)
assert isinstance(q_quant, torch.Tensor), (
"CPU sparse_attn_indexer expects a single FP8 q_quant tensor"
)
assert self.dcp_world_size <= 1 and not self.use_pcp, (
"CPU sparse indexer doesn't support decode/prefill context parallelism yet."
)
forward_context = get_forward_context()
attn_metadata = forward_context.attn_metadata
attn_metadata_narrowed: DeepseekV32IndexerMetadata | None = None
if isinstance(attn_metadata, dict):
metadata = attn_metadata[self.k_cache.prefix]
assert isinstance(metadata, DeepseekV32IndexerMetadata)
attn_metadata_narrowed = metadata
if attn_metadata_narrowed is None:
# Profiling/dummy run: no real metadata to act on.
return self.topk_indices_buffer
kv_cache = self.k_cache.kv_cache
topk_tokens = self.topk_tokens
topk_indices_buffer = self.topk_indices_buffer
slot_mapping = attn_metadata_narrowed.slot_mapping
has_decode = attn_metadata_narrowed.num_decodes > 0
has_prefill = attn_metadata_narrowed.num_prefills > 0
num_decode_tokens = attn_metadata_narrowed.num_decode_tokens
num_tokens = slot_mapping.shape[0]
if k is not None:
k = k[:num_tokens]
if not self.skip_k_cache_insert:
# Only reachable via DeepseekV32Attention with
# prefill_context_parallel_size > 1 on CPU -- set_k_cpu/set_s_cpu
# (the kernels this used to call) have been removed as unused/
# untested (csrc/cpu/sgl-kernels/store_cache.cpp).
raise NotImplementedError(
"SparseAttnIndexer.forward_cpu: skip_k_cache_insert=False "
"(prefill context parallel on CPU) is not supported."
)
topk_indices_buffer[: hidden_states.shape[0]] = -1
if has_prefill:
assert topk_tokens == 512, (
"topk_transform_512_cpu only supports index_topk == 512."
)
prefill_metadata = attn_metadata_narrowed.prefill
assert prefill_metadata is not None
assert len(prefill_metadata.chunks) == 1, (
"forward_cpu expects the prefill metadata builder to always "
"produce a single chunk -- see "
"DeepseekV4CPUIndexerMetadataBuilder._split_indexer_prefill_chunks."
)
chunk = prefill_metadata.chunks[0]
# kv_cache is a per-layer view into vLLM's shared multi-layer
# cache allocation, so its block stride generally exceeds
# block_size * page_width; fp8_paged_mqa_logits_cpu reads
# kv_view.stride(0) explicitly, so no copy is needed here.
kv_view = kv_cache.view(kv_cache.shape[0], -1)
block_size = kv_cache.shape[1]
q_slice = q_quant[chunk.token_start : chunk.token_end]
topk_indices = topk_indices_buffer[
chunk.token_start : chunk.token_end, :topk_tokens
]
if chunk.local_total_seq_lens == 0:
topk_indices.fill_(-1)
else:
assert chunk.local_cu_seq_lens is not None
# Each token's own (per-request, DCP-local) causal length.
local_seq_lens = chunk.cu_seqlen_ke - chunk.cu_seqlen_ks
# Recover each token's owning request from its row-start
# tag. Ties (from zero-length requests) are harmless: those
# tokens have local length 0 and never dereference
# page_table.
req_idx = (
torch.searchsorted(
chunk.local_cu_seq_lens, chunk.cu_seqlen_ks, right=True
)
- 1
)
page_table = chunk.block_table[req_idx]
# The true max over this chunk's own rows, NOT
# chunk.max_local_total_seq_lens (that field sums every
# request's length in the chunk, bounding the old
# flat-gather buffer this paged path no longer allocates).
max_seq_len = int(local_seq_lens.max().item())
logits = ops.fp8_paged_mqa_logits_cpu(
q_slice,
kv_view,
weights[chunk.token_start : chunk.token_end],
local_seq_lens,
page_table,
block_size,
max_seq_len,
)
out_page_scratch = torch.empty(
(q_slice.shape[0], topk_tokens),
dtype=torch.int32,
device=kv_cache.device,
)
ops.topk_transform_512_cpu(
logits,
local_seq_lens,
page_table,
out_page_scratch,
block_size,
topk_indices,
)
if has_decode:
decode_metadata = attn_metadata_narrowed.decode
assert decode_metadata is not None
assert not decode_metadata.requires_padding, (
"CPU sparse indexer decode path does not support speculative "
"decoding (native MTP) yet."
)
batch_size = decode_metadata.decode_lens.shape[0]
if batch_size > 0:
# No native MTP on CPU (asserted above) => exactly one
# query token per decode request, so the flat slice below
# is already the batch-major layout
# fp8_paged_mqa_logits_cpu wants.
assert num_decode_tokens == batch_size, (
"CPU sparse indexer decode path expects exactly one query "
"token per decode request."
)
assert topk_tokens == 512, (
"topk_transform_512_cpu only supports index_topk == 512."
)
seq_lens = decode_metadata.seq_lens
seq_lens = (
seq_lens[:, -1].contiguous() if seq_lens.ndim == 2 else seq_lens
)
block_table = decode_metadata.block_table[:batch_size]
block_size = kv_cache.shape[1]
kv_view = kv_cache.view(kv_cache.shape[0], -1)
logits = ops.fp8_paged_mqa_logits_cpu(
q_quant[:num_decode_tokens],
kv_view,
weights[:num_decode_tokens],
seq_lens,
block_table,
block_size,
attn_metadata_narrowed.max_seq_len,
)
# out_page_indices is a required kernel output but unused:
# the indexer's topk output must stay local/compressed-
# context positions (resolved later by
# DeepseekV4CPUAttention.forward_mqa via
# map_local_to_global_slots_cpu).
out_page_scratch = torch.empty(
(batch_size, topk_tokens),
dtype=torch.int32,
device=kv_cache.device,
)
ops.topk_transform_512_cpu(
logits,
seq_lens,
block_table,
out_page_scratch,
block_size,
topk_indices_buffer[:num_decode_tokens, :topk_tokens],
)
return topk_indices_buffer
source: https://docs.vllm.ai/en/latest/api/vllm/models/minimax_m3/amd/ops/index_topk/
lastmod: 2026-09-23

@torch.no_grad()
def minimax_m3_index_decode(
idx_q: torch.Tensor, # [total_q, num_idx_heads, head_dim]
index_kv_cache: torch.Tensor, # [num_blocks, 128, head_dim]
block_table: torch.Tensor, # [num_reqs, max_blocks]
seq_lens: torch.Tensor, # [num_reqs] int32
max_seq_len: int,
topk: int,
init_blocks: int,
local_blocks: int,
num_kv_heads: int,
decode_query_len: int,
max_decode_query_len: int,
out: torch.Tensor | None = None,
*,
attention_block_table: torch.Tensor | None = None,
sparse_block_table_out: torch.Tensor | None = None,
sparse_context_lens_out: torch.Tensor | None = None,
block_page_stride: int | None = None,
completion_counter: torch.Tensor | None = None,
) -> torch.Tensor:
"""Decode index block-score followed by fused adaptive top-k selection.
Returns topk_idx [num_kv_heads, total_q, topk] (0-indexed block ids, -1 pad).
When ``out`` ([num_kv_heads, >=total_q, topk]) is given, writes into
``out[:, :total_q, :]`` (stable address for cudagraph) instead of allocating.
The optional sparse-table arguments fuse current-layer table construction
into the selector. They must be provided together. ``completion_counter``
provides stable per-query synchronization storage for CUDA graphs. It must
be zero before its first launch and must not be shared by overlapping
selector invocations; every completed launch resets its active entries.
"""
total_q, num_idx_heads, head_dim = idx_q.shape
assert num_idx_heads == num_kv_heads, (
"M3 expects num_idx_heads == num_kv_heads (no topk index reduce)"
)
assert 0 < decode_query_len <= max_decode_query_len
assert total_q == seq_lens.shape[0] * decode_query_len
batch = total_q
emit_sparse_table = attention_block_table is not None
if emit_sparse_table and (
sparse_block_table_out is None
or sparse_context_lens_out is None
or block_page_stride is None
):
raise ValueError(
"MiniMax-M3 fused decode sparse-table arguments must be provided together"
)
if not emit_sparse_table and (
sparse_block_table_out is not None
or sparse_context_lens_out is not None
or block_page_stride is not None
):
raise ValueError(
"MiniMax-M3 fused decode sparse-table arguments must be provided together"
)
if emit_sparse_table:
assert attention_block_table is not None
assert sparse_block_table_out is not None
assert sparse_context_lens_out is not None
assert block_page_stride is not None
if num_idx_heads != 1:
raise ValueError(
"MiniMax-M3 fused decode sparse-table construction requires "
f"one index head, got {num_idx_heads}"
)
if block_page_stride not in (
PAGES_PER_SPARSE_BLOCK,
2 * PAGES_PER_SPARSE_BLOCK,
):
raise ValueError(
"MiniMax-M3 fused decode sparse-table page stride must be "
f"{PAGES_PER_SPARSE_BLOCK} or {2 * PAGES_PER_SPARSE_BLOCK}, "
f"got {block_page_stride}"
)
expected_sparse_shape = (total_q, topk * PAGES_PER_SPARSE_BLOCK)
if sparse_block_table_out.shape != expected_sparse_shape:
raise ValueError(
"MiniMax-M3 fused decode sparse block table has shape "
f"{tuple(sparse_block_table_out.shape)}, expected "
f"{expected_sparse_shape}"
)
if sparse_context_lens_out.shape != (total_q,):
raise ValueError(
"MiniMax-M3 fused decode sparse context lengths have shape "
f"{tuple(sparse_context_lens_out.shape)}, expected {(total_q,)}"
)
if (
attention_block_table.dim() != 2
or attention_block_table.shape[0] != seq_lens.shape[0]
):
raise ValueError(
"MiniMax-M3 fused decode attention block table must be "
"[num_requests, max_blocks]"
)
int32_tensors = (
attention_block_table,
sparse_block_table_out,
sparse_context_lens_out,
)
if any(tensor.dtype != torch.int32 for tensor in int32_tensors):
raise ValueError("MiniMax-M3 fused decode sparse tables require int32")
if any(tensor.device != idx_q.device for tensor in int32_tensors):
raise ValueError(
"MiniMax-M3 fused decode sparse tables must share the query device"
)
if (
attention_block_table.stride(1) != 1
or sparse_block_table_out.stride(1) != 1
or sparse_context_lens_out.stride(0) != 1
):
raise ValueError(
"MiniMax-M3 fused decode sparse tables require contiguous rows"
)
max_block = triton.cdiv(max_seq_len, SPARSE_BLOCK_SIZE)
if max_block >= 0xFFFF:
raise ValueError(
"MiniMax-M3 decode top-k supports fewer than 65535 sparse blocks"
)
if emit_sparse_table:
assert attention_block_table is not None
if attention_block_table.shape[1] < max_block:
raise ValueError(
"MiniMax-M3 fused decode attention block table is shorter "
f"than the required {max_block} sparse blocks"
)
use_pdl = current_platform.is_arch_support_pdl()
# `launch_pdl` is a Triton runtime kwarg only some backends accept (CUDA
# SM9+); this ROCm Triton rejects it even when False ("Keyword argument
# launch_pdl was specified but unrecognised"). Only pass it when PDL is
# actually supported -- on ROCm use_pdl is always False, so it's omitted.
pdl_kwargs: dict[str, bool | int] = {}
if use_pdl:
pdl_kwargs.update({"launch_pdl": True})
is_gfx950 = False
if current_platform.is_rocm():
from vllm.platforms.rocm import on_gfx950
is_gfx950 = on_gfx950()
# Multi-head spec decode scores a wider head-position tile per K block;
# reduce stages to ease memory/register pressure on the fallback path.
score_kwargs = pdl_kwargs.copy()
if num_idx_heads > 1 and max_decode_query_len > 1:
score_kwargs.update({"num_warps": 4, "num_stages": 2})
# Keep score strides 16-divisible to avoid Triton recompiles.
score_block_stride = round_up(max_block, 16)
score = torch.empty(
(num_idx_heads, total_q, score_block_stride),
dtype=torch.float32,
device=idx_q.device,
)
# Use the configured max decode length to avoid Triton recompiles when
# switching between qlen=1 and spec-decode verification batches.
BLOCK_SIZE_Q = triton.next_power_of_2(max_decode_query_len)
num_reqs = seq_lens.shape[0]
score_program_budget = _decode_score_program_budget(
num_reqs,
head_dim,
idx_q.dtype,
index_kv_cache.dtype,
is_gfx950=is_gfx950,
)
grid_score: tuple[int, ...]
if score_program_budget is not None:
grid_score = (score_program_budget + num_reqs - 1,)
_decode_index_score_balanced_kernel[grid_score](
idx_q,
index_kv_cache,
score,
block_table,
seq_lens,
num_idx_heads,
head_dim,
init_blocks,
local_blocks,
num_reqs,
score_program_budget,
decode_query_len,
idx_q.stride(0),
idx_q.stride(1),
idx_q.stride(2),
index_kv_cache.stride(0),
index_kv_cache.stride(1),
index_kv_cache.stride(2),
score.stride(0),
score.stride(1),
score.stride(2),
block_table.stride(0),
BLOCK_SIZE_K=SPARSE_BLOCK_SIZE,
BLOCK_SIZE_Q=BLOCK_SIZE_Q,
num_warps=2,
num_stages=1,
)
else:
# Increase independent work for the measured high-batch gfx950 decode
# range while preserving the deployed split for every other shape.
num_kv_chunks, use_high_batch_config = _decode_score_split_launch_policy(
num_reqs,
head_dim,
idx_q.dtype,
index_kv_cache.dtype,
is_gfx950=is_gfx950,
)
if use_high_batch_config and not (
num_idx_heads > 1 and max_decode_query_len > 1
):
score_kwargs.update({"num_warps": 2, "num_stages": 1})
grid_score = (num_reqs, num_kv_chunks)
_decode_index_score_kernel[grid_score](
idx_q,
index_kv_cache,
score,
block_table,
seq_lens,
num_idx_heads,
head_dim,
init_blocks,
local_blocks,
decode_query_len,
idx_q.stride(0),
idx_q.stride(1),
idx_q.stride(2),
index_kv_cache.stride(0),
index_kv_cache.stride(1),
index_kv_cache.stride(2),
score.stride(0),
score.stride(1),
score.stride(2),
block_table.stride(0),
BLOCK_SIZE_K=SPARSE_BLOCK_SIZE,
BLOCK_SIZE_Q=BLOCK_SIZE_Q,
num_kv_chunks=num_kv_chunks,
USE_PDL=use_pdl,
**score_kwargs,
)
if out is not None:
topk_idx = out[:, :total_q, :]
else:
topk_idx = torch.empty(
(num_idx_heads, total_q, topk),
dtype=torch.int32,
device=idx_q.device,
)
# The launch grid remains shape-constant for CUDA graphs. Each query uses
# only the number of chunks needed for its live context.
(
num_topk_chunks,
topk_block_size,
selector_num_warps,
selector_num_stages,
single_tile_guaranteed,
adaptive_final_merge,
) = _decode_topk_launch_policy(
max_block,
batch,
num_idx_heads,
topk,
is_gfx950=is_gfx950,
)
block_size_t = triton.next_power_of_2(topk)
topk_partial = torch.empty(
num_topk_chunks,
num_idx_heads,
batch,
block_size_t,
dtype=torch.int64,
device=idx_q.device,
)
if completion_counter is None:
active_counter = torch.zeros(
(num_idx_heads, batch),
dtype=torch.int32,
device=idx_q.device,
)
else:
if (
completion_counter.dim() != 2
or completion_counter.shape[0] != num_idx_heads
or completion_counter.shape[1] < batch
or completion_counter.dtype != torch.int32
or completion_counter.device != idx_q.device
or not completion_counter.is_contiguous()
):
raise ValueError(
"MiniMax-M3 completion counter must be contiguous int32 "
"[num_idx_heads, >=total_q] on the query device"
)
active_counter = completion_counter[:, :batch]
selector_attention_block_table = block_table
selector_sparse_block_table = topk_idx
selector_sparse_context_lens = seq_lens
selector_block_page_stride = PAGES_PER_SPARSE_BLOCK
selector_sparse_block_stride = topk_idx.stride(1)
if emit_sparse_table:
assert attention_block_table is not None
assert sparse_block_table_out is not None
assert sparse_context_lens_out is not None
assert block_page_stride is not None
selector_attention_block_table = attention_block_table
selector_sparse_block_table = sparse_block_table_out
selector_sparse_context_lens = sparse_context_lens_out
selector_block_page_stride = block_page_stride
selector_sparse_block_stride = sparse_block_table_out.stride(0)
_decode_topk_fused_kernel[(batch, num_idx_heads, num_topk_chunks)](
score,
topk_partial,
active_counter,
topk_idx,
seq_lens,
selector_attention_block_table,
selector_sparse_block_table,
selector_sparse_context_lens,
decode_query_len,
score.stride(0),
score.stride(1),
score.stride(2),
topk_partial.stride(0),
topk_partial.stride(1),
topk_partial.stride(2),
topk_partial.stride(3),
active_counter.stride(0),
active_counter.stride(1),
topk_idx.stride(0),
topk_idx.stride(1),
topk_idx.stride(2),
selector_attention_block_table.stride(0),
selector_sparse_block_stride,
topk=topk,
block_size=SPARSE_BLOCK_SIZE,
pages_per_sparse_block=PAGES_PER_SPARSE_BLOCK,
block_page_stride=selector_block_page_stride,
NUM_TOPK_CHUNKS=num_topk_chunks,
BLOCK_SIZE_K=topk_block_size,
BLOCK_SIZE_T=block_size_t,
EMIT_SPARSE_TABLE=emit_sparse_table,
SINGLE_TILE_GUARANTEED=single_tile_guaranteed,
ADAPTIVE_FINAL_MERGE=adaptive_final_merge,
num_warps=selector_num_warps,
num_stages=selector_num_stages,
)
return topk_idx
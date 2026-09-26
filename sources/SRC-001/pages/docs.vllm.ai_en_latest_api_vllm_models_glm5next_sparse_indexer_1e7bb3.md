source: https://docs.vllm.ai/en/latest/api/vllm/models/glm5next/sparse_indexer/
lastmod: 2026-09-24

@CustomOp.register("sparse_attn_indexer_kpool")
class SparseAttnIndexerKpool(CustomOp):
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
max_pool_len: int,
max_total_seq_len: int,
topk_indices_buffer: torch.Tensor,
skip_k_cache_insert: bool = False,
use_fp4_cache: bool = False,
tail_cache=None,
):
super().__init__()
self.k_cache = k_cache
self.tail_cache = tail_cache
self.quant_block_size = quant_block_size
self.scale_fmt = scale_fmt
self.topk_tokens = topk_tokens
self.head_dim = head_dim
self.max_pool_len = max_pool_len
self.max_total_seq_len = max_total_seq_len
self.topk_indices_buffer = topk_indices_buffer
self.skip_k_cache_insert = skip_k_cache_insert
self.use_fp4_cache = use_fp4_cache
if current_platform.is_cuda() and not has_deep_gemm():
raise RuntimeError(
"Sparse Attention Indexer CUDA op requires DeepGEMM to be installed."
)
_cfg = get_current_vllm_config_or_none()
self.topk_backend = (
_cfg.kernel_config.sparse_indexer_topk_backend
if _cfg is not None
else "auto"
)
_parallel = _cfg.parallel_config if _cfg is not None else None
if (
_parallel is not None
and _parallel.prefill_context_parallel_size > 1
and _parallel.decode_context_parallel_size > 1
):
raise NotImplementedError(
"SparseAttnIndexerKpool does not support PCP+DCP."
)
def forward_native(
self,
hidden_states: torch.Tensor,
q_quant: torch.Tensor | tuple[torch.Tensor, torch.Tensor],
k: torch.Tensor,
weights: torch.Tensor,
*,
gate_score: torch.Tensor | None = None,
compress_ape: torch.Tensor | None = None,
index_kpool: int = 1,
positions: torch.Tensor | None = None,
):
return self.forward_cuda(
hidden_states,
q_quant,
k,
weights,
gate_score=gate_score,
compress_ape=compress_ape,
index_kpool=index_kpool,
positions=positions,
)
def forward_cuda(
self,
hidden_states: torch.Tensor,
q_quant: torch.Tensor | tuple[torch.Tensor, torch.Tensor],
k: torch.Tensor,
weights: torch.Tensor,
*,
gate_score: torch.Tensor | None = None,
compress_ape: torch.Tensor | None = None,
index_kpool: int = 1,
positions: torch.Tensor | None = None,
):
# FP8 path: single tensor (per-token scale is folded into `weights`).
# FP4 path: (values, scales) tuple with scales required by the kernel.
if isinstance(q_quant, tuple):
q_values, q_scale = q_quant
else:
q_values, q_scale = q_quant, None
return sparse_attn_indexer_kpool(
hidden_states,
self.k_cache.prefix,
self.k_cache.kv_cache,
q_values,
q_scale,
k,
weights,
self.quant_block_size,
self.scale_fmt,
self.topk_tokens,
self.head_dim,
self.max_pool_len,
self.max_total_seq_len,
self.topk_indices_buffer,
self.skip_k_cache_insert,
self.use_fp4_cache,
gate_score,
compress_ape,
index_kpool,
positions,
self.tail_cache.kv_cache if self.tail_cache is not None else None,
self.tail_cache.prefix if self.tail_cache is not None else None,
self.topk_backend,
)
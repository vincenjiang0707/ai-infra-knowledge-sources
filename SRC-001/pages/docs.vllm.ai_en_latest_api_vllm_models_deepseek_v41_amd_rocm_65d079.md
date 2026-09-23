source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/amd/rocm/
lastmod: 2026-09-23

class DeepseekV41ROCMAiterMLAAttention(DeepseekV4Attention):
"""ROCm sparse MLA attention layer for DeepSeek V4.1."""
backend_cls = DeepseekV4ROCMAiterMLASparseBackend
swa_backend_cls = DeepseekV41ROCMAiterSparseSWABackend
def __init__(self, *args, **kwargs):
vllm_config = args[0] if args else kwargs["vllm_config"]
super().__init__(*args, **kwargs)
# CUDA executes WO_A with a quantized grouped-BMM kernel. ROCm's
# correctness path below dequantizes WO_A once and uses torch.einsum,
# so retain the ordinary MXFP8 linear kernel for post-load processing
# instead of asking for the CUDA-only BMM kernel.
self.wo_a.is_bmm = False
self._has_kv_transfer = vllm_config.kv_transfer_config is not None
# Block scale for the preshuffled weight; None = not preshuffled.
self._wqa_wkv_scale: torch.Tensor | None = None
self._wo_b_scale: torch.Tensor | None = None
self._fused_compressor_weight: torch.Tensor | None
self.register_buffer("_fused_compressor_weight", None, persistent=False)
self._fused_compressor_split_sizes: tuple[int, int] | None = None
# Decode ragged topk metadata is a pure function of the indices its
# index source published, so every consumer of a source rebuilds the
# same thing. The source owns one cache per compress ratio, refreshed
# when it runs; consumers below it read through.
self._topk_ragged_cache: dict[int, _TopkRagged] = {}
self._index_source_prefix: str | None = None
if self.compress_ratio > 0:
assert self.index_source_layer_id is not None
self._index_source_prefix = _replace_layer_index(
self.prefix, self.index_source_layer_id
)
if self._index_source_prefix not in self._static_forward_context:
raise NotImplementedError(
f"Index source {self._index_source_prefix} not found on "
"this rank; PP splits inside a v4.1 index-sharing group "
"are not supported."
)
@classmethod
def get_padded_num_q_heads(cls, num_heads: int) -> int:
return num_heads
def prepare_attn_preshuffle(self) -> None:
from vllm._aiter_ops import rocm_aiter_ops
if not rocm_aiter_ops.is_enabled():
return
from vllm.model_executor.layers.quantization.utils.fp8_utils import (
_upcast_e8m0_to_fp32,
)
from vllm.model_executor.utils import replace_parameter
def _prep(linear) -> torch.Tensor | None:
w = getattr(linear, "weight", None)
if w is None or w.dim() != 2:
return None
# K % 128 (group-128 quant) and N % 16 (shuffle_weight) must hold.
if w.shape[-1] % 128 != 0 or w.shape[0] % 16 != 0:
return None
ws = getattr(linear, "weight_scale_inv", None) # per-block scale
if ws is None:
return None
if ws.dtype == torch.float8_e8m0fnu:
ws = _upcast_e8m0_to_fp32(ws).contiguous()
# Shuffle the weight in place (single weight, no unshuffled copy).
replace_parameter(
linear,
"weight",
rocm_aiter_ops.shuffle_weight(w.data, layout=(16, 16)),
)
return ws
self._wqa_wkv_scale = _prep(self.fused_wqa_wkv)
self._wo_b_scale = _prep(self.wo_b)
def prepare_compressor_gemm_fusion(self) -> bool:
# V4.1 derives index keys from the source compressor's emitted latent
# and has no nested ``indexer.compressor``. Keep the projections
# separate and use the shared linear/PyTorch correctness path.
return False
def _bpre_attn_gemm(
self,
weight: torch.Tensor,
scale: torch.Tensor,
x: torch.Tensor,
reduce_tp: bool,
) -> torch.Tensor:
from vllm._aiter_ops import rocm_aiter_ops
x_fp8, x_scale = rocm_aiter_ops.group_fp8_quant(x, transpose_scale=True)
out = rocm_aiter_ops.gemm_a8w8_blockscale_bpreshuffle(
x_fp8, weight, x_scale, scale, output_dtype=x.dtype
)
if reduce_tp and get_tensor_model_parallel_world_size() > 1:
out = tensor_model_parallel_all_reduce(out)
return out
def _fused_wqa_wkv_gemm(self, hidden_states: torch.Tensor) -> torch.Tensor:
if self._wqa_wkv_scale is not None and hidden_states.dim() == 2:
return self._bpre_attn_gemm(
self.fused_wqa_wkv.weight, self._wqa_wkv_scale, hidden_states, False
)
return super()._fused_wqa_wkv_gemm(hidden_states)
def _run_parallel_input_projections(
self, hidden_states: torch.Tensor
) -> tuple[torch.Tensor, torch.Tensor | None, torch.Tensor | None]:
return super()._run_parallel_input_projections(hidden_states)
@functools.cached_property
def _wq_b_uses_aiter_block_scaled(self) -> bool:
"""True when both wq_b GEMMs run the aiter block-scaled fp8 kernel.
Cached: the linear kernels and the aiter env gates are fixed once
the model is built, so this is evaluated at the first forward
only.
The fused norm+quant path is only valid if the quant and GEMM it
replaces are exactly the aiter ones; otherwise fall back to the
shared path.
"""
from vllm._aiter_ops import rocm_aiter_ops
from vllm.model_executor.kernels.linear.scaled_mm import (
Fp8BlockScaledMMLinearKernel,
)
if not rocm_aiter_ops.is_linear_fp8_enabled():
return False
linears = [self.wq_b]
if self.indexer is not None:
linears.append(self.indexer.wq_b)
for linear in linears:
kernel = getattr(getattr(linear, "quant_method", None), "fp8_linear", None)
if not isinstance(kernel, Fp8BlockScaledMMLinearKernel):
return False
return True
def _split_qkv_and_norm(
self, qr_kv: torch.Tensor
) -> tuple[torch.Tensor, torch.Tensor | None, torch.Tensor]:
"""Fuse q/kv RMSNorm + per-1x128 fp8 q quant into one aiter kernel.
The shared path norms q and kv in one triton kernel and the wq_b
linears then re-read the bf16 qr to quantize it. The aiter kernel
computes both RMSNorms (fp32 accumulate) and the fp8 group quant
in a single pass, writing fp8 qr + group scales directly; both
wq_b GEMMs (attention and indexer) then consume that pair and
skip their own input quant. kv stays bf16: the fused insert
kernel RoPE/quantizes it itself. Falls back to the shared path
when the aiter linear path is not active.
"""
qr, kv = qr_kv.split([self.q_lora_rank, self.head_dim], dim=-1)
if not (
qr.dim() == 2
and qr.shape[0] > 0
and self.q_lora_rank % 128 == 0
and self._wq_b_uses_aiter_block_scaled
):
return super()._split_qkv_and_norm(qr_kv)
from vllm._aiter_ops import rocm_aiter_ops
return rocm_aiter_ops.fused_qk_rmsnorm_group_quant(
q=qr,
q_weight=self.q_norm.weight.data,
q_epsilon=self.eps,
kv=kv,
kv_weight=self.kv_norm.weight.data,
kv_epsilon=self.eps,
group_size=128,
transpose_scale=False,
)
def _o_proj(self, attn_out: torch.Tensor, positions: torch.Tensor) -> torch.Tensor:
o = attn_out[:, : self.n_local_heads, :]
# ROCm BF16 reference wo_a path (inverse RoPE + einsum) + wo_b.
z = rocm_inv_rope_einsum(
self.rotary_emb,
o,
positions,
self.rope_head_dim,
self.n_local_groups,
self.o_lora_rank,
self.wo_a,
inverse_rope=False,
)
zf = z.flatten(1)
if self._wo_b_scale is not None and zf.dim() == 2:
result = self._bpre_attn_gemm(self.wo_b.weight, self._wo_b_scale, zf, True)
else:
result = self.wo_b(zf)
return result
def forward_mqa(
self,
q: torch.Tensor,
kv: torch.Tensor,
positions: torch.Tensor,
output: torch.Tensor,
) -> None:
assert output.shape == q.shape, (
f"output buffer shape {output.shape} must match q shape {q.shape}"
)
assert output.dtype == q.dtype, (
f"output buffer dtype {output.dtype} must match q dtype {q.dtype}"
)
forward_context = get_forward_context()
attn_metadata = forward_context.attn_metadata
if attn_metadata is None:
# Warmup dummy run: no real metadata. Reserve the same bf16
# gather workspace _forward_prefill would; the dequantize / topk
# / sparse_fwd kernels are skipped this step.
swa_only = self.compress_ratio == 0
N = (
0
if swa_only
else (self.max_model_len + self.compress_ratio - 1)
// self.compress_ratio
)
M = N + self.window_size + self.max_num_batched_tokens
current_workspace_manager().get_simultaneous(
((self.PREFILL_CHUNK_SIZE, M, q.shape[-1]), torch.bfloat16),
)
output.zero_()
return
assert isinstance(attn_metadata, dict)
rocm_metadata = cast(
DeepseekV4FlashMLAMetadata | None,
attn_metadata.get(self.compressed_cache_prefix)
if self.compressed_cache_prefix is not None
else None,
)
swa_metadata = cast(
DeepseekV4ROCMAiterSparseSWAMetadata | None,
attn_metadata.get(self.swa_cache_layer.prefix),
)
assert swa_metadata is not None
swa_only = self.compress_ratio == 0
self_kv_cache = None if swa_only else self._compressed_kv_cache()
swa_kv_cache = self.swa_cache_layer.kv_cache
num_decodes = swa_metadata.num_decodes
num_prefills = swa_metadata.num_prefills
num_decode_tokens = swa_metadata.num_decode_tokens
if num_prefills > 0:
self._forward_prefill(
q=q[num_decode_tokens:],
positions=positions[num_decode_tokens:],
compressed_k_cache=self_kv_cache,
swa_k_cache=swa_kv_cache,
output=output[num_decode_tokens:],
attn_metadata=rocm_metadata,
swa_metadata=swa_metadata,
)
rotated = 0
if num_decodes > 0:
rotated = self._forward_decode(
q=q[:num_decode_tokens],
positions=positions[:num_decode_tokens],
kv_cache=self_kv_cache,
swa_metadata=swa_metadata,
attn_metadata=rocm_metadata,
swa_only=swa_only,
output=output[:num_decode_tokens],
)
# Only the decode reduce rotates its own rows, and only the leading
# `rotated` of them; prefill rows and any decode path that did not
# fuse still owe the standalone pass. Settle that here rather than in
# _o_proj: the split is batch-dependent and _o_proj runs compiled,
# where such a value freezes at its trace-time value.
rocm_inverse_rope_rows_(
output[rotated:, : self.n_local_heads, :],
positions[rotated:],
self.rotary_emb.cos_sin_cache,
self.rope_head_dim,
)
def _decode_topk_ragged(
self,
swa_metadata: DeepseekV4ROCMAiterSparseSWAMetadata,
attn_metadata: DeepseekV4FlashMLAMetadata | None,
num_decodes: int,
num_decode_tokens: int,
) -> _TopkRagged:
"""Ragged form of the topk indices this layer's index source published.
The packing depends only on the shared ``topk_indices_buffer`` and
per-step metadata, apart from the layer's own compress ratio, so the
source memoizes one result per ratio for all the layers below it.
"""
assert attn_metadata is not None
assert swa_metadata.is_valid_token is not None
assert self.topk_indices_buffer is not None
assert self._index_source_prefix is not None
source = self._static_forward_context[self._index_source_prefix]
if source is self:
# Fresh indices as of this layer; drop what the last step cached.
source._topk_ragged_cache = {}
cached = source._topk_ragged_cache.get(self.compress_ratio)
if cached is not None:
return cached
built = compute_global_topk_ragged_indices_and_indptr(
self.topk_indices_buffer[:num_decode_tokens],
swa_metadata.token_to_req_indices,
attn_metadata.block_table[:num_decodes],
attn_metadata.block_size // self.compress_ratio,
swa_metadata.is_valid_token[:num_decode_tokens],
)
source._topk_ragged_cache[self.compress_ratio] = built
return built
def _forward_decode(
self,
q: torch.Tensor,
positions: torch.Tensor,
kv_cache: torch.Tensor | None,
swa_metadata: DeepseekV4ROCMAiterSparseSWAMetadata,
attn_metadata: DeepseekV4FlashMLAMetadata | None,
swa_only: bool,
output: torch.Tensor,
) -> int:
"""Returns how many leading rows the decode epilogue inverse-RoPE'd."""
num_decodes = swa_metadata.num_decodes
num_decode_tokens = swa_metadata.num_decode_tokens
topk_lens = None
topk_ragged_indices = None
topk_ragged_indptr = None
if not swa_only:
(
topk_ragged_indices,
topk_ragged_indptr,
topk_lens,
) = self._decode_topk_ragged(
swa_metadata=swa_metadata,
attn_metadata=attn_metadata,
num_decodes=num_decodes,
num_decode_tokens=num_decode_tokens,
)
return rocm_sparse_attn_decode(
q=q,
kv_cache=kv_cache,
swa_k_cache=self.swa_cache_layer.kv_cache,
swa_only=swa_only,
topk_indices=None,
topk_lens=topk_lens,
swa_indices=swa_metadata.decode_swa_indices,
swa_lens=swa_metadata.decode_swa_lens,
swa_ragged_indices=swa_metadata.decode_swa_ragged_indices,
swa_ragged_indptr=swa_metadata.decode_swa_ragged_indptr,
topk_ragged_indices=topk_ragged_indices,
topk_ragged_indptr=topk_ragged_indptr,
attn_sink=self.attn_sink,
scale=self.scale,
head_dim=self.head_dim,
nope_head_dim=self.nope_head_dim,
rope_head_dim=self.rope_head_dim,
output=output,
inv_rope_positions=positions,
inv_rope_cos_sin_cache=self.rotary_emb.cos_sin_cache,
extra_cache_nan_free=_trust_dsv4_extra_cache_nan_free(
self.kv_cache_dtype,
self._has_kv_transfer,
not swa_only and kv_cache is not None,
),
)
def _forward_prefill(
self,
q: torch.Tensor,
positions: torch.Tensor,
compressed_k_cache: torch.Tensor | None,
swa_k_cache: torch.Tensor,
output: torch.Tensor,
attn_metadata: DeepseekV4FlashMLAMetadata | None,
swa_metadata: DeepseekV4ROCMAiterSparseSWAMetadata,
) -> None:
swa_only = attn_metadata is None
num_prefills = swa_metadata.num_prefills
num_prefill_tokens = swa_metadata.num_prefill_tokens
num_decodes = swa_metadata.num_decodes
num_decode_tokens = swa_metadata.num_decode_tokens
seq_lens = swa_metadata.prefill_seq_lens
gather_lens = swa_metadata.prefill_gather_lens
assert seq_lens is not None
assert gather_lens is not None
query_start_loc_cpu = swa_metadata.query_start_loc_cpu
query_start_loc = swa_metadata.query_start_loc
assert query_start_loc_cpu is not None
assert query_start_loc is not None
prefill_token_base = query_start_loc_cpu[num_decodes]
# Local indices filled by the index source; SWA-only layers pass
# top_k=0 and never read them.
assert self.topk_indices_buffer is not None
topk_indices = self.topk_indices_buffer[num_decode_tokens:]
topk_indices = topk_indices[:num_prefill_tokens]
if not swa_only:
top_k = topk_indices.shape[-1]
N = (self.max_model_len + self.compress_ratio - 1) // self.compress_ratio
else:
top_k = 0
N = 0
M = N + self.window_size + self.max_num_batched_tokens
num_chunks = (num_prefills + self.PREFILL_CHUNK_SIZE - 1) // (
self.PREFILL_CHUNK_SIZE
)
workspace_manager = current_workspace_manager()
kv = workspace_manager.get_simultaneous(
((self.PREFILL_CHUNK_SIZE, M, q.shape[-1]), torch.bfloat16),
)[0]
for chunk_idx in range(num_chunks):
chunk_start = chunk_idx * self.PREFILL_CHUNK_SIZE
chunk_end = min(chunk_start + self.PREFILL_CHUNK_SIZE, num_prefills)
chunk_size = chunk_end - chunk_start
if not swa_only:
assert attn_metadata is not None
assert compressed_k_cache is not None
block_table = attn_metadata.block_table[num_decodes:]
# compressed_k_cache is OCP on every platform (Triton encoder).
dequantize_and_gather_k_cache(
kv[:chunk_size],
compressed_k_cache,
seq_lens=seq_lens[chunk_start:chunk_end] // self.compress_ratio,
gather_lens=None,
block_table=block_table[chunk_start:chunk_end],
block_size=attn_metadata.block_size // self.compress_ratio,
offset=0,
use_fnuz=False,
)
swa_block_table = swa_metadata.block_table[num_decodes:]
dequantize_and_gather_k_cache(
kv[:chunk_size],
swa_k_cache,
seq_lens=seq_lens[chunk_start:chunk_end],
gather_lens=gather_lens[chunk_start:chunk_end],
block_table=swa_block_table[chunk_start:chunk_end],
block_size=swa_metadata.block_size,
offset=N,
use_fnuz=current_platform.is_fp8_fnuz(),
)
query_start = (
query_start_loc_cpu[num_decodes + chunk_start] - prefill_token_base
)
query_end = (
query_start_loc_cpu[num_decodes + chunk_end] - prefill_token_base
)
combined_indices, combined_lens = combine_topk_swa_indices(
topk_indices[query_start:query_end],
query_start_loc[
num_decodes + chunk_start : num_decodes + chunk_end + 1
],
seq_lens[chunk_start:chunk_end],
gather_lens[chunk_start:chunk_end],
self.window_size,
self.compress_ratio,
top_k,
M,
N,
)
rocm_sparse_attn_prefill(
q=q[query_start:query_end],
kv=kv.view(-1, 1, q.shape[-1]),
indices=combined_indices,
topk_length=combined_lens,
scale=self.scale,
head_dim=self.head_dim,
nope_head_dim=self.nope_head_dim,
rope_head_dim=self.rope_head_dim,
attn_sink=self.attn_sink,
output=output[query_start:query_end],
)
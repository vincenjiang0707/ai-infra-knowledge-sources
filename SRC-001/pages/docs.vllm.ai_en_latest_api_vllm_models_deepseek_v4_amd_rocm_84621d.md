source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/amd/rocm/
lastmod: 2026-09-23

class DeepseekV4ROCMAiterMLAAttention(DeepseekV4Attention):
"""ROCm sparse MLA attention layer for DeepSeek V4."""
backend_cls = DeepseekV4ROCMAiterMLASparseBackend
def __init__(self, *args, **kwargs):
vllm_config = args[0] if args else kwargs["vllm_config"]
super().__init__(*args, **kwargs)
self._has_kv_transfer = vllm_config.kv_transfer_config is not None
# Block scale for the preshuffled weight; None = not preshuffled.
self._wqa_wkv_scale: torch.Tensor | None = None
self._wo_b_scale: torch.Tensor | None = None
self._wo_a_fp8_weight: torch.Tensor | None = None
self._wo_a_e8m0_scale: torch.Tensor | None = None
self._wo_a_cos_cache: torch.Tensor | None = None
self._wo_a_sin_cache: torch.Tensor | None = None
self._fused_compressor_weight: torch.Tensor | None
self.register_buffer("_fused_compressor_weight", None, persistent=False)
self._fused_compressor_split_sizes: tuple[int, int] | None = None
if self.indexer is None:
# Dense layers have no compressor work to overlap; HCA layers
# (compressor, no indexer) keep the streams for the dual-stream
# fork below.
if self.compressor is None:
self.aux_stream_list = None
else:
# Disable indexer inner overlap.
self.indexer.aux_stream = None
def _enable_multi_stream_overlap(self) -> bool:
"""ROCm multi-stream gates: streams and capture region.
Dict metadata marks piecewise cudagraph, whose eager breaks rebuild
the attention inputs on the owning stream. Forking side streams
there would rely on runtime HIP event sync, which is unreliable in
this overlap on ROCm (event waits can hang), so multi-stream only
runs where the fork/join becomes static graph edges: inside capture,
or with non-dict metadata (full cudagraph or the profile run), which
has no eager breaks. Covers both the HCA and CSA forks.
"""
attn_metadata = get_forward_context().attn_metadata
return self.aux_stream_list is not None and (
torch.cuda.is_current_stream_capturing()
or not isinstance(attn_metadata, dict)
)
def _run_sequential_pipeline(
self,
hidden_states: torch.Tensor,
positions: torch.Tensor,
o_padded: torch.Tensor,
) -> None:
"""Disable ROCm streams when the current execution region cannot overlap."""
aux_streams = self.aux_stream_list
self.aux_stream_list = None
try:
qr_kv, kv_score, indexer_kv_score, indexer_weights = (
self._run_parallel_input_projections(hidden_states)
)
qr, qr_scale, kv = self._split_qkv_and_norm(qr_kv)
self._prepare_and_attn_fn(
hidden_states,
qr,
kv,
qr_scale,
kv_score,
indexer_kv_score,
indexer_weights,
positions,
o_padded,
)
finally:
self.aux_stream_list = aux_streams
def forward(
self,
positions: torch.Tensor,
hidden_states: torch.Tensor,
llama_4_scaling: torch.Tensor | None = None,
) -> torch.Tensor:
# Pre-allocate attention output with FlashMLA-padded head count.
# The op writes into `o_padded`; we slice to n_local_heads after.
num_tokens = hidden_states.shape[0]
o_padded = torch.empty(
(num_tokens, self.padded_heads, self.head_dim),
dtype=hidden_states.dtype,
device=hidden_states.device,
)
if self._enable_multi_stream_overlap():
# The ROCm override consumes these sentinels inside the capture
# boundary, moving the stream fan-out ahead of the projections.
self._prepare_and_attn_fn(
hidden_states,
None,
None,
None,
None,
None,
None,
positions,
o_padded,
)
else:
self._run_sequential_pipeline(hidden_states, positions, o_padded)
o = o_padded[:, : self.n_local_heads, :]
# Inverse-RoPE + wo_a + wo_b output projection (platform-specific).
return self._o_proj(o, positions)
def _prepare_and_attn(
self,
hidden_states: torch.Tensor,
qr: torch.Tensor | None,
kv: torch.Tensor | None,
qr_scale: torch.Tensor | None,
kv_score: torch.Tensor | None,
indexer_kv_score: torch.Tensor | None,
indexer_weights: torch.Tensor | None,
positions: torch.Tensor,
o_padded: torch.Tensor,
) -> None:
"""Run the ROCm fork/join (HCA or CSA) inside the capture boundary."""
aux_streams = self.aux_stream_list
# The sequential pipeline disables aux_stream_list before calling
# back with real projection inputs; aux_streams is None ends that
# recursion here.
if aux_streams is None:
saved_streams = self.aux_stream_list
self.aux_stream_list = None
try:
super()._prepare_and_attn(
hidden_states,
cast(torch.Tensor, qr),
cast(torch.Tensor, kv),
qr_scale,
cast(torch.Tensor, kv_score),
cast(torch.Tensor, indexer_kv_score),
cast(torch.Tensor, indexer_weights),
positions,
o_padded,
)
finally:
self.aux_stream_list = saved_streams
return
# Re-check: forward's gate ran inside a captured segment that
# _prepare_and_attn_eager (MRV1) then broke, making this region eager.
if not self._enable_multi_stream_overlap():
self._run_sequential_pipeline(hidden_states, positions, o_padded)
return
indexer = self.indexer
compressor = self.compressor
assert compressor is not None
def default_chain():
qr_kv = self._fused_wqa_wkv_gemm(hidden_states)
qr_out, qr_scale_out, kv_out = self._split_qkv_and_norm(qr_kv)
q = self._wq_b_proj(qr_out, qr_scale_out).view(
-1, self.n_local_heads, self.head_dim
)
attn_metadata = get_forward_context().attn_metadata
q = self._fused_qnorm_rope_kv_insert(q, kv_out, positions, attn_metadata)
return q, qr_out, qr_scale_out, kv_out
def main_compressor_chain() -> None:
score = torch.mm(
hidden_states,
compressor.fused_wkv_wgate.weight.T,
out_dtype=torch.float32,
)
compressor(score, positions, self.rotary_emb)
if indexer is None:
# HCA dual-stream: the main compressor runs on aux stream 0 while
# the default stream produces q and inserts KV into the SWA cache.
# Both branches only read hidden_states, so the join merely has to
# precede the sparse attention that consumes the compressed KV.
(q, _qr_out, _qr_scale_out, kv_out), _ = execute_in_parallel(
default_chain,
[main_compressor_chain],
self.ln_events[0],
[self.ln_events[1]],
aux_streams[:1],
enable=True,
)
self._sparse_indexer_and_attn(
hidden_states, None, None, None, q, kv_out, positions, o_padded
)
return
def indexer_compressor_chain() -> None:
score = torch.mm(
hidden_states,
indexer.compressor.fused_wkv_wgate.weight.T,
out_dtype=torch.float32,
)
indexer.compressor(score, positions, self.indexer_rotary_emb)
# CSA three-stream: the main and indexer compressors run on aux
# streams 0 and 1 while the default stream produces q and inserts KV
# into the SWA cache. Every branch only reads hidden_states plus its
# own state, so the join merely has to precede the indexer op and the
# sparse attention, which consume the compressed KV caches.
(q, qr_out, qr_scale_out, kv_out), _ = execute_in_parallel(
default_chain,
[main_compressor_chain, indexer_compressor_chain],
self.ln_events[0],
self.ln_events[1:3],
aux_streams[:2],
enable=True,
)
indexer_weights_out, _ = indexer.weights_proj(hidden_states)
# The indexer compressor already ran on aux stream 1; build queries only.
index_q, index_q_scale, weights = indexer(
hidden_states,
qr_out,
None,
indexer_weights_out,
positions,
self.indexer_rotary_emb,
qr_scale_out,
skip_compressor=True,
)
self._sparse_indexer_and_attn(
hidden_states,
index_q,
index_q_scale,
weights,
q,
kv_out,
positions,
o_padded,
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
get_fp8_block_weight_scale,
)
from vllm.model_executor.utils import replace_parameter
def _prep(linear) -> torch.Tensor | None:
w = getattr(linear, "weight", None)
if w is None or w.dim() != 2:
return None
# K % 128 (group-128 quant) and N % 16 (shuffle_weight) must hold.
if w.shape[-1] % 128 != 0 or w.shape[0] % 16 != 0:
return None
ws = get_fp8_block_weight_scale(linear)
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
if _ON_GFX950 and envs.VLLM_ROCM_USE_AITER_FP8BMM:
self._prepare_fp8_wo_a()
def _prepare_fp8_wo_a(self) -> None:
try:
from aiter.ops.batched_gemm_op_a8w8 import (
batched_gemm_a8w8_mxscale as mxscale_op,
)
from aiter.ops.inverse_rope_group_quant import (
inverse_rope_group_quant as inverse_quant_op,
)
except ImportError:
logger.warning_once(
"The DeepSeek V4 FP8 WO_A path requires AITER >= 0.1.20; "
"falling back to BF16 WO_A."
)
return
del mxscale_op, inverse_quant_op
from vllm.model_executor.layers.quantization.utils.fp8_utils import (
get_fp8_block_weight_scale,
is_fp8,
)
weight = getattr(self.wo_a, "weight", None)
scale = get_fp8_block_weight_scale(self.wo_a)
if scale is None:
# ModelOpt MXFP8 stores the multiplicative E8M0 scale without the
# historical ``_inv`` suffix.
scale = getattr(self.wo_a, "weight_scale", None)
if weight is None or scale is None:
logger.warning_once(
"DeepSeek V4 FP8 WO_A needs a block-scaled FP8 wo_a weight; "
"the layer exposes no weight/weight scale. Falling back to "
"BF16 WO_A."
)
return
if weight.dim() != 2 or scale.dim() != 2 or not is_fp8(weight.dtype):
logger.warning_once(
"DeepSeek V4 FP8 WO_A needs a 2-D FP8 wo_a weight with a 2-D "
"block scale, got weight %s%s and scale %s. Falling back to "
"BF16 WO_A.",
weight.dtype,
tuple(weight.shape),
tuple(scale.shape),
)
return
groups = self.n_local_groups
out_per_group = self.o_lora_rank
out_features, in_features = weight.shape
if (
out_features != groups * out_per_group
or out_per_group % 128 != 0
or in_features % 128 != 0
or scale.shape != (out_features // 128, in_features // 128)
):
logger.warning_once(
"DeepSeek V4 FP8 WO_A needs group-128 blocks for %d groups of "
"%d outputs, got weight %s and scale %s. Falling back to BF16 "
"WO_A.",
groups,
out_per_group,
tuple(weight.shape),
tuple(scale.shape),
)
return
e8m0_scale = _wo_a_block_scale_to_e8m0(scale)
if e8m0_scale is None:
logger.warning_once(
"DeepSeek V4 FP8 WO_A could not losslessly encode the %s wo_a "
"block scale as OCP E8M0. Falling back to BF16 WO_A.",
scale.dtype,
)
return
self._wo_a_fp8_weight = weight.view(groups, out_per_group, in_features)
self._wo_a_e8m0_scale = e8m0_scale.view(
groups, out_per_group // 128, in_features // 128
)
cache = getattr(self.rotary_emb, "cos_sin_cache_bf16", None)
if cache is None:
cache = self.rotary_emb.cos_sin_cache.to(dtype=torch.bfloat16)
cos_cache, sin_cache = cache.chunk(2, dim=-1)
self._wo_a_cos_cache = cos_cache.contiguous()
self._wo_a_sin_cache = sin_cache.contiguous()
def prepare_compressor_gemm_fusion(self) -> bool:
if self._fused_compressor_weight is not None:
return False
from vllm.model_executor.offloader import NoopOffloader, get_offloader
if not isinstance(get_offloader(), NoopOffloader):
logger.warning_once(
"DeepSeek V4 compressor GEMM fusion is incompatible with "
"weight offloading and will remain disabled."
)
return False
compressor = self.compressor
indexer = self.indexer
if compressor is None or indexer is None:
return False
main_weight = compressor.fused_wkv_wgate.weight
indexer_weight = indexer.compressor.fused_wkv_wgate.weight
if main_weight.ndim != 2 or indexer_weight.ndim != 2:
raise ValueError("DeepSeek V4 compressor weights must be matrices")
if main_weight.shape[1] != indexer_weight.shape[1]:
raise ValueError("DeepSeek V4 compressor weights must share K")
if main_weight.dtype != indexer_weight.dtype:
raise ValueError("DeepSeek V4 compressor weights must share dtype")
if main_weight.device != indexer_weight.device:
raise ValueError("DeepSeek V4 compressor weights must share device")
main_size = main_weight.shape[0]
indexer_size = indexer_weight.shape[0]
fused_weight = torch.cat((main_weight, indexer_weight), dim=0)
with torch.no_grad():
main_weight.set_(fused_weight[:main_size])
indexer_weight.set_(fused_weight[main_size:])
self._fused_compressor_weight = fused_weight
self._fused_compressor_split_sizes = (main_size, indexer_size)
return True
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
) -> tuple[
torch.Tensor,
torch.Tensor | None,
torch.Tensor | None,
torch.Tensor | None,
]:
fused_weight = self._fused_compressor_weight
split_sizes = self._fused_compressor_split_sizes
if fused_weight is None or split_sizes is None:
return super()._run_parallel_input_projections(hidden_states)
indexer = self.indexer
if indexer is None:
raise RuntimeError("Fused compressor weight requires a C4 indexer")
qr_kv = self._fused_wqa_wkv_gemm(hidden_states)
fused_scores = torch.mm(
hidden_states,
fused_weight.T,
out_dtype=torch.float32,
)
kv_score, indexer_kv_score = fused_scores.split(split_sizes, dim=-1)
indexer_weights, _ = indexer.weights_proj(hidden_states)
return qr_kv, kv_score, indexer_kv_score, indexer_weights
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
def _o_proj(self, o: torch.Tensor, positions: torch.Tensor) -> torch.Tensor:
if self._wo_a_fp8_weight is not None:
from aiter.ops.batched_gemm_op_a8w8 import (
batched_gemm_a8w8_mxscale,
)
from aiter.ops.inverse_rope_group_quant import (
inverse_rope_group_quant,
)
assert self._wo_a_cos_cache is not None
assert self._wo_a_sin_cache is not None
o_fp8, o_scale = inverse_rope_group_quant(
o.view(o.shape[0], self.n_local_heads, self.head_dim),
positions.to(torch.int64),
self._wo_a_cos_cache,
self._wo_a_sin_cache,
num_groups=self.n_local_groups,
quant_group_size=128,
)
assert self._wo_a_e8m0_scale is not None
zf = batched_gemm_a8w8_mxscale(
o_fp8,
self._wo_a_fp8_weight,
o_scale,
self._wo_a_e8m0_scale,
dtype=o.dtype,
).flatten(1)
else:
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
return self._bpre_attn_gemm(self.wo_b.weight, self._wo_b_scale, zf, True)
return self.wo_b(zf)
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
swa_only = self.compress_ratio <= 1
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
DeepseekV4ROCMAiterMLASparseMetadata | None,
attn_metadata.get(self.prefix),
)
swa_metadata = cast(
DeepseekV4ROCMAiterSparseSWAMetadata | None,
attn_metadata.get(self.swa_cache_layer.prefix),
)
assert swa_metadata is not None
swa_only = self.compress_ratio <= 1
self_kv_cache = self.kv_cache if not swa_only else None
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
# The fp8 wo_a path rotates inside inverse_rope_group_quant, so folding
# the rotation into the decode reduce would apply it twice. Only the
# BF16 einsum path hands its rotation off to the decode.
fuse_inv_rope = self._wo_a_fp8_weight is None
rotated = 0
if num_decodes > 0:
rotated = self._forward_decode(
q=q[:num_decode_tokens],
positions=positions[:num_decode_tokens] if fuse_inv_rope else None,
kv_cache=self_kv_cache,
swa_metadata=swa_metadata,
attn_metadata=rocm_metadata,
swa_only=swa_only,
output=output[:num_decode_tokens],
adaptive_splits=(
_ON_GFX950
and not swa_only
and self.compress_ratio == 128
and rocm_metadata is not None
and rocm_metadata.for_cudagraph_capture
),
)
if fuse_inv_rope:
# Only the decode reduce rotates its own rows, and only the leading
# `rotated` of them; prefill rows and any decode path that did not
# fuse still owe the standalone pass. Settle that here rather than
# in _o_proj: the split is batch-dependent and _o_proj runs
# compiled, where such a value freezes at its trace-time value.
rocm_inverse_rope_rows_(
output[rotated:, : self.n_local_heads, :],
positions[rotated:],
self.rotary_emb.cos_sin_cache,
self.rope_head_dim,
)
def _forward_decode(
self,
q: torch.Tensor,
positions: torch.Tensor | None,
kv_cache: torch.Tensor | None,
swa_metadata: DeepseekV4ROCMAiterSparseSWAMetadata,
attn_metadata: DeepseekV4ROCMAiterMLASparseMetadata | None,
swa_only: bool,
output: torch.Tensor,
adaptive_splits: bool,
) -> int:
"""Returns how many leading rows the decode epilogue inverse-RoPE'd."""
num_decodes = swa_metadata.num_decodes
num_decode_tokens = swa_metadata.num_decode_tokens
topk_indices = None
topk_lens = None
topk_ragged_indices = None
topk_ragged_indptr = None
if not swa_only:
assert attn_metadata is not None
assert swa_metadata.is_valid_token is not None
block_size = attn_metadata.block_size // self.compress_ratio
is_valid = swa_metadata.is_valid_token[:num_decode_tokens]
if self.compress_ratio == 4:
assert self.topk_indices_buffer is not None
(
topk_ragged_indices,
topk_ragged_indptr,
topk_lens,
) = compute_global_topk_ragged_indices_and_indptr(
self.topk_indices_buffer[:num_decode_tokens],
swa_metadata.token_to_req_indices,
attn_metadata.block_table[:num_decodes],
block_size,
is_valid,
)
else:
topk_indices = attn_metadata.c128a_global_decode_topk_indices
topk_lens = attn_metadata.c128a_decode_topk_lens
topk_ragged_indices = attn_metadata.c128a_decode_topk_ragged_indices
topk_ragged_indptr = attn_metadata.c128a_decode_topk_ragged_indptr
return rocm_sparse_attn_decode(
q=q,
kv_cache=kv_cache,
swa_k_cache=self.swa_cache_layer.kv_cache,
swa_only=swa_only,
topk_indices=topk_indices,
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
adaptive_splits=adaptive_splits,
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
attn_metadata: DeepseekV4ROCMAiterMLASparseMetadata | None,
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
left_visible = swa_metadata.prefill_left_visible
right_visible = swa_metadata.prefill_right_visible
if left_visible is not None:
left_visible = left_visible[num_decode_tokens:]
assert right_visible is not None
right_visible = right_visible[num_decode_tokens:]
if not swa_only:
if self.compress_ratio == 4:
assert self.topk_indices_buffer is not None
topk_indices = self.topk_indices_buffer[num_decode_tokens:]
topk_indices = topk_indices[:num_prefill_tokens]
else:
assert attn_metadata is not None
topk_indices = attn_metadata.c128a_prefill_topk_indices
assert topk_indices is not None
top_k = topk_indices.shape[-1]
N = (self.max_model_len + self.compress_ratio - 1) // self.compress_ratio
else:
assert self.topk_indices_buffer is not None
topk_indices = self.topk_indices_buffer[num_decode_tokens:]
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
max_image_tokens=self.max_image_tokens,
left_visible=(
left_visible[query_start:query_end]
if left_visible is not None
else None
),
right_visible=(
right_visible[query_start:query_end]
if right_visible is not None
else None
),
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
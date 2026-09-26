source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention/
lastmod: 2026-09-24

class MLAAttention(nn.Module, AttentionLayerBase):
"""Multi-Head Latent Attention layer.
NOTE: Please read the comment at the top of the file before trying to
understand this class
This class takes query, and compressed key/value tensors as input.
The class does the following:
1. Store the input key and value tensors in the KV cache.
2. Perform (multi-head/multi-query/grouped-query) attention.
3. Return the output tensor.
"""
supports_dense_mha_prefill: ClassVar[bool] = True
# Under PCP+DCP only the decode rows carry an LSE; the base forward
# merges a full-batch LSE, so subclasses opt in with their own forward.
supports_pcp_dcp: ClassVar[bool] = False
def __init__(
self,
num_heads: int,
scale: float,
qk_nope_head_dim: int,
qk_rope_head_dim: int,
v_head_dim: int,
q_lora_rank: int | None,
kv_lora_rank: int,
kv_b_proj: ColumnParallelLinear,
dcp_q_replicate: bool = False,
cache_config: CacheConfig | None = None,
quant_config: QuantizationConfig | None = None,
prefix: str = "",
attn_backend: type[AttentionBackend] | None = None,
use_sparse: bool = False,
indexer: object | None = None,
topk_indices_buffer: torch.Tensor | None = None,
index_group_builder: "SparseMLAIndexGroupBuilder | None" = None,
non_causal_multi_token_decode: bool = False,
sliding_window: int | None = None,
prefill_backend_cls: type[MLAPrefillBackend] | None = None,
**extra_impl_args,
):
super().__init__()
self.num_heads = num_heads
self.scale = scale
self.qk_nope_head_dim = qk_nope_head_dim
self.qk_rope_head_dim = qk_rope_head_dim
self.v_head_dim = v_head_dim
self.q_lora_rank = q_lora_rank
self.kv_lora_rank = kv_lora_rank
self.kv_b_proj = kv_b_proj
self.dcp_q_replicate = dcp_q_replicate
self.W_UK_T_dcp_qrep: torch.Tensor | None = None
self.head_size = kv_lora_rank + qk_rope_head_dim
self.layer_name = prefix
self.indexer = indexer
self.non_causal_multi_token_decode = non_causal_multi_token_decode
self.sliding_window = sliding_window
self.num_kv_heads = 1
self.qk_head_dim = self.qk_nope_head_dim + self.qk_rope_head_dim
if cache_config is not None:
kv_cache_dtype: CacheDType = cache_config.cache_dtype
else:
kv_cache_dtype = "auto"
self.quant_config = quant_config
if cache_config is not None and cache_config.kv_cache_dtype_skip_layers:
from vllm.model_executor.models.utils import extract_layer_index
layer_idx = extract_layer_index(prefix)
if str(layer_idx) in cache_config.kv_cache_dtype_skip_layers:
kv_cache_dtype = "auto"
logger.debug(
"Layer %s: kv_cache_dtype=%s",
prefix,
kv_cache_dtype,
)
dtype = torch.get_default_dtype()
if attn_backend is not None:
assert attn_backend.is_mla(), (
f"MLAAttention: attn_backend must be an MLA backend, "
f"got {attn_backend.get_name()} instead"
)
self.attn_backend = attn_backend
else:
self.attn_backend = get_attn_backend(
self.head_size,
dtype,
kv_cache_dtype,
use_mla=True,
use_sparse=use_sparse,
num_heads=self.num_heads,
)
normalized_kv_cache_dtype = _canonicalize_sparse_mla_kv_cache_dtype(
self.attn_backend, kv_cache_dtype
)
if normalized_kv_cache_dtype != kv_cache_dtype:
if cache_config is not None:
cache_config.cache_dtype = normalized_kv_cache_dtype
kv_cache_dtype = normalized_kv_cache_dtype
logger.info_once(
"Using %s KV cache format for %s backend.",
kv_cache_dtype,
self.attn_backend.get_name(),
)
if (
self.attn_backend.get_name() == "FLASHINFER_MLA_SPARSE"
and kv_cache_dtype != "fp8_ds_mla"
and is_quantized_kv_cache(kv_cache_dtype)
):
logger.info_once(
"Using standard fp8 KV cache format. To use DeepSeek's fp8_ds_mla "
"KV cache format, please set `--attention-backend FLASHMLA_SPARSE`"
)
# Initialize KV cache quantization attributes
self.kv_cache_dtype = kv_cache_dtype
_init_kv_cache_quant(self, quant_config, prefix)
if (
cache_config is not None
and cache_config.enable_prefix_caching
and envs.VLLM_BATCH_INVARIANT
and (
self.attn_backend.get_name() == "TRITON_MLA"
or self.attn_backend.get_name() == "FLASHINFER"
)
):
logger.warning_once(
"Disabling prefix caching for TRITON_MLA / FLASHINFER "
"with batch invariance, as it is not yet supported.",
)
cache_config.enable_prefix_caching = False
# Sparse MLA reads top-k indices from a shared buffer. Pass it
# explicitly so backbone "skip" layers (indexer=None) still find it.
if use_sparse:
extra_impl_args["topk_indices_buffer"] = topk_indices_buffer
if index_group_builder is not None:
extra_impl_args["index_group_builder"] = index_group_builder
impl_cls = cast(type[MLAAttentionImpl], self.attn_backend.get_impl_cls())
impl = impl_cls(
num_heads=self.num_heads,
head_size=self.head_size,
scale=self.scale,
num_kv_heads=1,
alibi_slopes=None,
sliding_window=sliding_window,
kv_cache_dtype=self.kv_cache_dtype,
logits_soft_cap=None,
attn_type=AttentionType.DECODER,
kv_sharing_target_layer_name=None,
# MLA Args
q_lora_rank=self.q_lora_rank,
kv_lora_rank=self.kv_lora_rank,
qk_nope_head_dim=self.qk_nope_head_dim,
qk_rope_head_dim=self.qk_rope_head_dim,
qk_head_dim=self.qk_nope_head_dim + self.qk_rope_head_dim,
v_head_dim=self.v_head_dim,
kv_b_proj=kv_b_proj,
indexer=indexer,
**extra_impl_args,
)
self.impl = impl # type: ignore[assignment]
index_group = getattr(impl, "index_group", None)
self.hisparse_cache = (
index_group.cache(cast(Any, impl).index_group_index)
if isinstance(index_group, HiSparseMLAIndexGroup)
else None
)
self.q_pad_num_heads = getattr(self.impl, "q_pad_num_heads", None)
self.is_amx_bmm_enabled = getattr(self.impl, "uses_amx_bmm", False)
# AMX reads kv_b_proj's weight directly and never calls it live; the
# reference CPU MLA backend calls it but isn't perf-critical. Skip
# the packed-kernel dispatch either way.
kv_b_proj._cpu_skip_gemm_dispatch = True
self.use_direct_call = not current_platform.opaque_attention_op()
vllm_config = get_current_vllm_config()
parallel_config = vllm_config.parallel_config
self.use_pcp = parallel_config.prefill_context_parallel_size > 1
compilation_config = vllm_config.compilation_config
if prefix in compilation_config.static_forward_context:
raise ValueError(f"Duplicate layer name: {prefix}")
compilation_config.static_forward_context[prefix] = self
self.prefill_backend: MLAPrefillBackend | None
if self.impl.is_sparse and not (
self.impl.supports_dense_mha_prefill and self.supports_dense_mha_prefill
):
logger.warning_once(
"Sparse MLA layer has no dense-MHA prefill path; using the top-k "
"MQA path only."
)
self.prefill_backend = None
else:
try:
prefill_backend_cls = prefill_backend_cls or get_mla_prefill_backend(
vllm_config
)
except ValueError:
if (
not self.impl.is_sparse
or vllm_config.attention_config.mla_prefill_backend is not None
):
raise
logger.warning_once(
"No MLA prefill backend supports this model; sparse MLA will "
"use the top-k MQA path only (no dense-MHA prefill)."
)
self.prefill_backend = None
else:
self.prefill_backend = prefill_backend_cls(
num_heads=self.num_heads,
scale=self.scale,
kv_lora_rank=self.kv_lora_rank,
qk_nope_head_dim=self.qk_nope_head_dim,
qk_rope_head_dim=self.qk_rope_head_dim,
v_head_dim=self.v_head_dim,
vllm_config=vllm_config,
)
self.kv_cache = torch.tensor([])
self.use_sparse = use_sparse
if vllm_config.kernel_config.enable_jit_warmup:
backend_name = self.attn_backend.get_name()
if backend_name in (
"FLASHMLA_SPARSE",
"FLASHINFER_MLA_SPARSE",
"FLASHINFER_MLA_SPARSE_SM120",
"DEEPSEEK_V32_INDEXER",
):
from vllm.v1.attention.backends.mla.compressor_utils import (
_COMPRESSED_SLOT_MAPPING_KERNEL,
)
from vllm.v1.attention.backends.mla.indexer import (
_BUILD_PREFILL_CHUNK_METADATA_KERNEL,
_PREPARE_UNIFORM_DECODE_KERNEL,
)
_COMPRESSED_SLOT_MAPPING_KERNEL.register_warmup()
_PREPARE_UNIFORM_DECODE_KERNEL.register_warmup()
_BUILD_PREFILL_CHUNK_METADATA_KERNEL.register_warmup()
if backend_name != "DEEPSEEK_V32_INDEXER":
from vllm.v1.attention.backends.mla.sparse_swa import (
_COMPUTE_PREFILL_METADATA_KERNEL,
)
_COMPUTE_PREFILL_METADATA_KERNEL.register_warmup()
if self.use_pcp and self.impl.dcp_world_size > 1 and not self.supports_pcp_dcp:
raise NotImplementedError(
f"{type(self).__name__} does not support PCP+DCP."
)
self.dcp_manager: MLADCPManager | None = None
if self.impl.dcp_world_size > 1:
query_dtype = (
current_platform.fp8_dtype()
if is_quantized_kv_cache(self.kv_cache_dtype)
and self.kv_cache_dtype != "fp8_ds_mla"
and self.impl.supports_quant_query_input
else dtype
)
self.dcp_manager = MLADCPManager(
vllm_config=vllm_config,
device=next(kv_b_proj.parameters()).device,
num_heads=self.num_heads,
query_head_dim=self.kv_lora_rank + self.qk_rope_head_dim,
output_head_dim=self.kv_lora_rank,
query_dtype=query_dtype,
output_dtype=dtype,
padded_num_heads=self.q_pad_num_heads,
is_lse_base_on_e=self.impl.lse_base_on_e,
use_pcp=self.use_pcp,
)
self.is_aiter_triton_fp8_bmm_enabled = rocm_aiter_ops.is_fp8bmm_enabled()
# If kv_b_proj_weight is unquantized, quantize it to mxfp4 if supported
self.is_aiter_triton_fp4_bmm_enabled = (
rocm_aiter_ops.is_fp4bmm_enabled()
and hasattr(self.kv_b_proj, "weight")
and self.kv_b_proj.weight.dtype == torch.bfloat16
)
# Attributes for forward_impl method
self._vllm_config = get_current_vllm_config()
self._chunked_prefill_workspace_size: int | None = None
self._decode_concat_quant_fp8_op = _DecodeConcatQuantFP8(
static=True,
group_shape=GroupShape.PER_TENSOR,
compile_native=True,
)
self._quant_fp8_op = QuantFP8(
static=True,
group_shape=GroupShape.PER_TENSOR,
compile_native=True,
)
def bind_kv_cache(self, kv_cache: torch.Tensor) -> None:
# [B, H=1, N, C] -> [B, N, C]
self.kv_cache = kv_cache.squeeze(1)
if (
self._vllm_config.kernel_config.enable_jit_warmup
and self.attn_backend.get_name()
in (
"FLASHMLA_SPARSE",
"FLASHINFER_MLA_SPARSE",
"FLASHINFER_MLA_SPARSE_SM120",
"DEEPSEEK_V32_INDEXER",
)
):
from vllm.v1.attention.backends.mla.sparse_utils import (
_CONVERT_REQ_INDEX_TO_GLOBAL_INDEX_KERNEL,
)
row_width = self.kv_cache.shape[-1]
assert self.kv_cache.stride(0) % row_width == 0
_CONVERT_REQ_INDEX_TO_GLOBAL_INDEX_KERNEL.register_warmup(
self._vllm_config,
block_stride_rows=self.kv_cache.stride(0) // row_width,
)
@property
def chunked_prefill_workspace_size(self) -> int:
if self._chunked_prefill_workspace_size is None:
self._chunked_prefill_workspace_size = (
MLACommonMetadataBuilder.determine_chunked_prefill_workspace_size(
self._vllm_config
)
)
return self._chunked_prefill_workspace_size
def update_kv_cache(
self,
kv_c_normed: torch.Tensor,
k_pe: torch.Tensor,
kv_cache: torch.Tensor,
slot_mapping: torch.Tensor | None,
attn_metadata: "MLACommonMetadata | None",
kv_cache_dtype: str,
k_scale: torch.Tensor,
) -> None:
cache = self.hisparse_cache
if slot_mapping is None or (cache is not None and cache.dummy_batch):
return
kv_c_normed, k_pe, slot_mapping = maybe_gather_mla_latent_cache_inputs(
kv_c_normed,
k_pe,
slot_mapping,
attn_metadata.num_decode_tokens if attn_metadata is not None else None,
self.use_pcp,
)
assert slot_mapping is not None
if cache is not None:
kv_cache, slot_mapping, num_rows = cache.write_target(
kv_c_normed.shape[0], slot_mapping.numel()
)
kv_c_normed = kv_c_normed[:num_rows]
k_pe = k_pe[:num_rows]
self.impl.do_kv_cache_update( # type: ignore[attr-defined]
kv_c_normed,
k_pe,
kv_cache,
slot_mapping,
kv_cache_dtype,
k_scale,
)
if cache is not None:
mirror_target = cache.mirror_write_target(kv_c_normed.shape[0])
if mirror_target is not None:
mirror_cache, mirror_slots = mirror_target
self.impl.do_kv_cache_update( # type: ignore[attr-defined]
kv_c_normed,
k_pe,
mirror_cache,
mirror_slots,
kv_cache_dtype,
k_scale,
)
def prepare_kv_cache_update(
self, attn_metadata: "MLACommonMetadata | None"
) -> None:
cache = self.hisparse_cache
if cache is not None and cache.runtime.is_group_leader:
cache.prepare_group_for_batch(attn_metadata)
def forward(
self,
q: torch.Tensor,
kv_c_normed: torch.Tensor,
k_pe: torch.Tensor,
output_shape: torch.Size | None = None,
q_dcp_replicated: torch.Tensor | None = None,
) -> torch.Tensor:
if self.use_direct_call:
forward_context: ForwardContext = get_forward_context()
attn_metadata_raw = forward_context.attn_metadata
attn_metadata: MLACommonMetadata
if isinstance(attn_metadata_raw, dict):
attn_metadata = attn_metadata_raw[self.layer_name] # type: ignore[assignment]
elif isinstance(attn_metadata_raw, list):
# list[dict[str, AttentionMetadata]]: used in speculative decoding
# where [0] is the base-model (non-speculative) metadata dict.
attn_metadata = attn_metadata_raw[0][self.layer_name] # type: ignore[assignment]
else:
attn_metadata = attn_metadata_raw
self_kv_cache = self.kv_cache
slot_mapping = forward_context.slot_mapping
assert isinstance(slot_mapping, dict), (
f"Expected slot_mapping to be a dict, got {type(slot_mapping)}. "
)
layer_slot_mapping = slot_mapping.get(self.layer_name)
self.prepare_kv_cache_update(attn_metadata)
self.update_kv_cache(
kv_c_normed,
k_pe,
self_kv_cache,
layer_slot_mapping,
attn_metadata,
self.kv_cache_dtype,
self._k_scale,
)
if self.hisparse_cache is not None:
self.hisparse_cache.finish_kv_update()
output = torch.empty(output_shape, dtype=q.dtype, device=q.device)
self.forward_impl(
q,
kv_c_normed,
k_pe,
self_kv_cache,
attn_metadata,
output=output,
q_dcp_replicated=q_dcp_replicated,
)
return output
else:
encoded = _encode_layer_name(self.layer_name)
kv_cache_dummy_dep = torch.ops.vllm.unified_mla_kv_cache_update(
kv_c_normed,
k_pe,
encoded,
self.kv_cache_dtype,
self._k_scale,
)
output = torch.empty(output_shape, dtype=q.dtype, device=q.device)
torch.ops.vllm.unified_mla_attention_with_output(
q,
kv_c_normed,
k_pe,
output,
encoded,
kv_cache_dummy_dep=kv_cache_dummy_dep,
q_dcp_replicated=q_dcp_replicated,
)
return output
def forward_impl(
self,
q: torch.Tensor,
k_c_normed: torch.Tensor, # key in unified attn
k_pe: torch.Tensor, # value in unified attn
kv_cache: torch.Tensor,
attn_metadata: "MLACommonMetadata",
output: torch.Tensor,
output_scale: torch.Tensor | None = None,
output_block_scale: torch.Tensor | None = None,
quant_group_size: int | None = None,
quant_scale_ue8m0: bool | None = None,
quant_col_major: bool | None = None,
quant_tma_aligned: bool | None = None,
q_dcp_replicated: torch.Tensor | None = None,
) -> torch.Tensor:
assert output is not None, "Output tensor must be provided."
quant_key = _detect_output_quant_key(
output, output_scale, output_block_scale, self.num_heads * self.v_head_dim
)
if quant_key is not None:
# The fusion pass has allocated output with quantized dtype
# (FP8 or uint8 for FP4). We can't write into it directly,
# so we swap in a temp buffer for computation, then quantize
# into the real output at the end.
# NOTE(carlyou): this is temporary until kernels support fp8 output
quant_output = output
output = torch.empty(
output.shape[0],
self.num_heads * self.v_head_dim,
dtype=q.dtype,
device=output.device,
)
if attn_metadata is None:
# During the profile run try to simulate to worse case output size
# for `self.kv_b_proj(kv_c_normed)` in `_compute_prefill_context`
# since this can be large
_ = torch.empty(
(
self.chunked_prefill_workspace_size,
self.num_heads,
self.qk_nope_head_dim + self.v_head_dim,
),
device=k_c_normed.device,
dtype=k_c_normed.dtype,
)
# The zero fill is required when used with DP + EP
# to ensure all ranks within a DP group compute the
# same expert outputs.
if quant_key is not None:
return quant_output.fill_(0)
return output.fill_(0)
fp8_attention = is_quantized_kv_cache(self.kv_cache_dtype)
num_actual_toks = attn_metadata.num_actual_tokens
if self.use_pcp and self.impl.dcp_world_size > 1 and quant_key is not None:
raise NotImplementedError(
"MRV2 MLA PCP+DCP does not support fused output quantization yet."
)
# Inputs and outputs may be padded for CUDA graphs
output_padded = output
output = output[:num_actual_toks, ...]
q = q[:num_actual_toks, ...]
if q_dcp_replicated is not None:
q_dcp_replicated = q_dcp_replicated[:num_actual_toks, ...]
k_c_normed = k_c_normed[:num_actual_toks, ...]
k_pe = k_pe[:num_actual_toks, ...]
if fp8_attention and self.kv_cache_dtype not in (
# Opaque per-token byte formats stay as raw uint8
"fp8_ds_mla",
"nvfp4_ds_mla",
):
kv_cache = kv_cache.view(current_platform.fp8_dtype())
assert (
attn_metadata.num_decodes is not None
and attn_metadata.num_prefills is not None
and attn_metadata.num_decode_tokens is not None
)
num_mqa_tokens = attn_metadata.num_decode_tokens
num_mha_tokens = q.size(0) - num_mqa_tokens
use_mha = True
if self.impl.is_sparse and num_mha_tokens > 0:
use_mha = self._use_sparse_mha(attn_metadata)
if not use_mha:
num_mqa_tokens = q.size(0)
num_mha_tokens = 0
mha_use_quant_output = (
quant_key is not None
and self.prefill_backend is not None
and self.prefill_backend.supports_quant_output(quant_key)
and (
not self.impl.is_sparse
or attn_metadata.prefill_max_seq_len # type: ignore[attr-defined]
<= attn_metadata.topk_tokens # type: ignore[attr-defined]
)
and attn_metadata is not None
and attn_metadata.prefill is not None
and attn_metadata.prefill.chunked_context is None
and self.impl.dcp_world_size <= 1
)
if num_mha_tokens > 0:
if mha_use_quant_output:
mha_output = quant_output
mha_output_scale = output_scale
else:
mha_output = output
mha_output_scale = None
self.impl.forward_mha( # type: ignore[attr-defined]
q[num_mqa_tokens:],
k_c_normed[num_mqa_tokens:],
k_pe[num_mqa_tokens:],
kv_cache,
attn_metadata,
self._k_scale,
output=mha_output[num_mqa_tokens:num_actual_toks],
output_scale=mha_output_scale,
)
if num_mqa_tokens > 0:
if q_dcp_replicated is not None:
mqa_q = q_dcp_replicated[:num_mqa_tokens]
qrep_decode = True
else:
mqa_q = q[:num_mqa_tokens]
qrep_decode = False
mqa_output_slice = output[:num_mqa_tokens]
mqa_q_nope, mqa_q_pe = mqa_q.split(
[self.qk_nope_head_dim, self.qk_rope_head_dim], dim=-1
)
# Convert from (B, N, P) to (N, B, P)
mqa_q_nope = mqa_q_nope.transpose(0, 1)
if self.q_pad_num_heads is not None:
B, N, L = mqa_q_pe.shape
mqa_pe_padded = mqa_q_pe.new_empty((B, self.q_pad_num_heads, L))
mqa_pe_padded.resize_((B, N, L))
mqa_pe_padded.copy_(mqa_q_pe)
mqa_q_pe = mqa_pe_padded
if self.is_aiter_triton_fp4_bmm_enabled:
mqa_ql_nope = rocm_aiter_ops.batched_gemm_a16wfp4(
mqa_q_nope,
self.W_K,
self.W_K_scale,
transpose_bm=True,
prequant=True,
y_scale=self._q_scale if fp8_attention else None,
)
elif self.is_aiter_triton_fp8_bmm_enabled:
# Multiply+Transpose (N, B, P)x(N, P, L)->(N, B, L)->(B, N, L)
mqa_ql_nope = rocm_aiter_ops.triton_fp8_bmm(
mqa_q_nope,
self.W_K,
self.W_K_scale,
group_size=128,
transpose_bm=True,
)
elif self.is_amx_bmm_enabled:
# bmm_cpu computes out[n] = mat1[n] @ mat2[n]^T against
# AMXMLAImpl's own (N, L, P) packed W_UK -- same as prefill.
N, B, P = mqa_q_nope.shape
L = self.kv_lora_rank
mqa_ql_nope = mqa_q_nope.new_empty((N, B, L))
ops.bmm_cpu(
mqa_ql_nope,
mqa_q_nope,
self.impl._w_uk_packed, # type: ignore[attr-defined]
True,
self.impl._w_scale, # type: ignore[attr-defined]
)
mqa_ql_nope = mqa_ql_nope.transpose(0, 1)
else:
# Pads the head_dim if necessary (for the underlying kernel)
N, B, P = mqa_q_nope.shape
W_UK_T = self.W_UK_T_dcp_qrep if qrep_decode else self.W_UK_T
assert W_UK_T is not None
_, _, L = W_UK_T.shape
if self.q_pad_num_heads is not None:
mqa_ql_nope = mqa_q_nope.new_empty((self.q_pad_num_heads, B, L))
mqa_ql_nope.resize_((N, B, L))
# Multiply (N, B, P) x (N, P, L) -> (N, B, L)
torch.bmm(mqa_q_nope, W_UK_T, out=mqa_ql_nope)
# Convert from (N, B, L) to (B, N, L)
mqa_ql_nope = mqa_ql_nope.transpose(0, 1)
else:
# Write the (N, B, L) bmm result straight into a
# token-major (B, N, L) buffer so the MQA query is already
# contiguous; a NoPE model (qk_rope_head_dim == 0) then
# needs no concat at all.
mqa_ql_nope = mqa_q_nope.new_empty((B, N, L))
torch.bmm(mqa_q_nope, W_UK_T, out=mqa_ql_nope.transpose(0, 1))
if fp8_attention and self.impl.supports_quant_query_input:
assert mqa_ql_nope.shape[0] == mqa_q_pe.shape[0]
assert mqa_ql_nope.shape[1] == mqa_q_pe.shape[1]
mqa_q = self._decode_concat_quant_fp8_op(
mqa_ql_nope, mqa_q_pe, self._q_scale
)
else:
mqa_q = (mqa_ql_nope, mqa_q_pe)
# concatenate nope + pe -> (B, N, L + P) (fp8 op above may have fused)
if self.impl.dcp_world_size > 1:
assert self.dcp_manager is not None
if self.use_pcp:
if self.impl.dcp_world_size > self.impl.pcp_world_size:
if isinstance(mqa_q, tuple):
mqa_q = torch.cat(mqa_q, dim=-1)
mqa_q = get_tp_group().all_gather(mqa_q, dim=1)
else:
if isinstance(mqa_q, tuple):
# concatenate mqa_ql_nope and mqa_q_pe -> (B, N, L + P)
mqa_q = torch.cat(mqa_q, dim=-1)
if not qrep_decode:
assert self.dcp_manager.query_gather is not None
mqa_q = self.dcp_manager.query_gather(mqa_q)
# call decode attn
if not self.impl.is_sparse:
assert attn_metadata.decode is not None
attn_out, lse = self.impl.forward_mqa(mqa_q, kv_cache, attn_metadata, self) # type: ignore[attr-defined]
# correct dcp attn_out with lse.
if self.impl.dcp_world_size > 1:
assert lse is not None
assert self.dcp_manager is not None
decode_metadata = getattr(attn_metadata, "decode", None)
if not use_mha:
seq_lens = cast(torch.Tensor, attn_metadata.seq_lens) # type: ignore[attr-defined]
query_start_loc = attn_metadata.query_start_loc
else:
seq_lens = (
decode_metadata.seq_lens
if decode_metadata is not None
else cast(torch.Tensor, attn_metadata.seq_lens)[ # type: ignore[attr-defined]
: attn_metadata.num_decodes
]
)
query_start_loc = attn_metadata.query_start_loc[
: attn_metadata.num_decodes + 1
]
attn_out = self.dcp_manager.combine(
attn_out,
lse,
seq_lens=seq_lens,
query_start_loc=query_start_loc,
)
if self.use_pcp:
attn_out = finalize_mla_pcp_decode(attn_out, self.num_heads)
# v_up projection
self._v_up_proj(attn_out, out=mqa_output_slice)
if quant_key is not None:
quant_idx = num_mqa_tokens if mha_use_quant_output else num_actual_toks
if quant_idx == 0:
return quant_output
actual = output[:quant_idx]
if quant_key == kNvfp4Dynamic:
# NVFP4: two FP4 values packed into one uint8
assert output_block_scale is not None
fp4_data, fp4_scales = ops.scaled_fp4_quant(actual, output_scale)
quant_output[:quant_idx].copy_(fp4_data)
output_block_scale[: fp4_scales.shape[0]].copy_(fp4_scales)
elif quant_key in (kFp8Dynamic128Sym, kFp8Dynamic64Sym):
# Per-group FP8
assert output_block_scale is not None
assert quant_group_size is not None, (
"Group FP8 output quant requested but "
"quant_group_size not passed through custom op"
)
finfo = torch.finfo(_FP8_DTYPE)
torch.ops._C.per_token_group_fp8_quant(
actual,
quant_output[:quant_idx],
output_block_scale[:quant_idx],
quant_group_size,
1e-10, # eps
finfo.min,
finfo.max,
quant_scale_ue8m0,
quant_col_major,
quant_tma_aligned,
)
elif quant_key == kFp8StaticTensorSym:
# Static FP8 quantization
fp8_data, _ = self._quant_fp8_op(actual, output_scale)
quant_output[:quant_idx].copy_(fp8_data)
else:
raise ValueError(f"Unsupported quant_key: {quant_key}")
return quant_output
if self.use_pcp and output_padded.shape[0] > num_actual_toks:
output_padded[num_actual_toks:].zero_()
return output_padded
def _use_sparse_mha(self, attn_metadata: "MLACommonMetadata") -> bool:
if self.hisparse_cache is not None:
return False
prefill = attn_metadata.prefill
if prefill is None:
return False
use_masked_mha = (
self.prefill_backend is not None
and self.impl.masked_mha_available # type: ignore[attr-defined]
and self.impl.dcp_world_size <= 1
and _use_masked_mha(
backend_name=self.attn_backend.get_name(),
tensor_parallel_size=(
self._vllm_config.parallel_config.tensor_parallel_size
),
qk_head_dim=self.qk_nope_head_dim + self.qk_rope_head_dim,
v_head_dim=self.v_head_dim,
query_len=prefill.max_query_len,
seq_len=attn_metadata.prefill_max_seq_len, # type: ignore[attr-defined]
has_context=prefill.chunked_context is not None,
)
and self.impl.masked_mha_workspace_fits(prefill) # type: ignore[attr-defined]
)
return (prefill.use_dense_mha or use_masked_mha) and not (
self._vllm_config.attention_config.sparse_mla_force_mqa
)
def process_weights_after_loading(self, act_dtype: torch.dtype):
# Let per-backend impls do their own weight packing first (no-op
# unless overridden), mirroring Attention.process_weights_after_loading.
self.impl.process_weights_after_loading(act_dtype)
if self.is_amx_bmm_enabled:
# AMXMLAImpl already packed its own W_UK/W_UV above, for both
# prefill and decode. Release the now-unused raw weight.
self.kv_b_proj.weight = torch.nn.Parameter(
torch.empty(0), requires_grad=False
)
return
if self.dcp_q_replicate:
# qrep wired here: validate unsupported decode backends once.
assert self.q_pad_num_heads in (None, self.num_heads), (
"DCP query replication is unsupported on head-padding MLA "
"backends (q_pad_num_heads)."
)
if (
self.is_aiter_triton_fp4_bmm_enabled
or self.is_aiter_triton_fp8_bmm_enabled
):
raise NotImplementedError(
"DCP query replication is not implemented for the aiter "
"FP4/FP8 MLA BMM paths."
)
W_UK, W_UV = split_kv_b_proj(
self.kv_b_proj,
act_dtype,
self.kv_lora_rank,
self.num_heads,
self.qk_nope_head_dim,
self.v_head_dim,
)
# If kv_b_proj_weight is unquantized, quantize it to mxfp4 if supported
if self.is_aiter_triton_fp4_bmm_enabled:
from vllm.model_executor.layers.quantization.quark.utils import (
quark_quantize_weight_to_mxfp4,
)
self.W_K, self.W_K_scale = quark_quantize_weight_to_mxfp4(W_UK)
# Convert from (L, N, P) to (N, L, P)
self.W_K = self.W_K.transpose(0, 1)
self.W_K_scale = self.W_K_scale.transpose(0, 1)
self.W_V, self.W_V_scale = quark_quantize_weight_to_mxfp4(
W_UV.permute(1, 2, 0)
)
elif self.is_aiter_triton_fp8_bmm_enabled:
W_K = W_UK.transpose(0, 1) # 16 512 128
W_V = W_UV.permute(1, 2, 0) # 16 128 512
self.W_K, self.W_K_scale = dynamic_per_batched_tensor_quant(
W_K, dtype=current_platform.fp8_dtype()
)
self.W_V, self.W_V_scale = dynamic_per_batched_tensor_quant(
W_V, dtype=current_platform.fp8_dtype()
)
# The kernel operates on non-padded inputs. Hence, pre-compiling
# triton kernel to avoid runtime compilation for unseen batch sizes
# Pre-compile for batch sizes 1 to 1024 to cover most use-cases.
# On DS-R1, this step adds roughly 50s to the model loading time.
max_batch_size = 1024 # [ToDo] Find the optimal upper limit
pre_compilation_list = list(range(1, max_batch_size + 1))
if is_global_first_rank():
pre_compilation_list = tqdm(
pre_compilation_list,
desc="[Aiter Triton] Pre-compiling fp8 BMM kernel",
total=max_batch_size,
)
for m in pre_compilation_list:
x = torch.empty(
(self.W_K.shape[0], m, self.W_K.shape[2]),
dtype=torch.bfloat16,
device=self.W_K.device,
)
rocm_aiter_ops.triton_fp8_bmm(
x, self.W_K, self.W_K_scale, group_size=128, transpose_bm=True
)
x = torch.empty(
(self.W_V.shape[0], m, self.W_V.shape[2]),
dtype=torch.bfloat16,
device=self.W_V.device,
)
rocm_aiter_ops.triton_fp8_bmm(
x, self.W_V, self.W_V_scale, group_size=128, transpose_bm=True
)
else:
# Convert from (L, N, V) to (N, L, V)
replace_parameter(self, "W_UV", W_UV.transpose(0, 1), prefer_copy=True)
# Convert from (L, N, P) to (N, P, L)
replace_parameter(self, "W_UK_T", W_UK.permute(1, 2, 0), prefer_copy=True)
if self.dcp_q_replicate:
self.W_UK_T_dcp_qrep = get_dcp_group().all_gather(
self.W_UK_T.contiguous(), dim=0
)
# If we should not load quant weights, we initialize the scales to 1.0
# as the default value. See [Note: Register q/k/v/prob scales in state dict]
# for more details.
quant_method = (
resolve_quant_method(self.quant_config, self, prefix=self.layer_name)
if self.quant_config
else None
)
if not should_load_quant_weights(quant_method):
set_default_quant_scales(self, register_buffer=False)
def get_attn_backend(self) -> type[AttentionBackend]:
return self.attn_backend
def get_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCacheSpec:
kv_cache_dtype = kv_cache_dtype_str_to_dtype(
self.kv_cache_dtype, vllm_config.model_config
)
common_kwargs = dict(
block_size=vllm_config.cache_config.block_size,
num_kv_heads=1,
head_size=self.head_size,
dtype=kv_cache_dtype,
cache_dtype_str=self.kv_cache_dtype,
kv_quant_mode=get_kv_quant_mode(self.kv_cache_dtype),
# ds_mla layouts pack NoPE + RoPE + scales into one opaque per-token
# blob, so the size is not derivable from head_size.
# See flashmla_sparse.py.
state_content_bytes={"fp8_ds_mla": 656, "nvfp4_ds_mla": 352}.get(
self.kv_cache_dtype
),
)
if self.sliding_window is not None:
return SlidingWindowMLASpec(
**common_kwargs,
sliding_window=self.sliding_window,
)
return MLAAttentionSpec(
**common_kwargs,
is_index_group_leader=self.indexer is not None,
non_causal_multi_token_decode=self.non_causal_multi_token_decode,
)
def _v_up_proj(self, x: torch.Tensor, out: torch.Tensor):
# Convert from (B, N, L) to (N, B, L)
x = x.view(-1, self.num_heads, self.kv_lora_rank).transpose(0, 1)
out = out.view(-1, self.num_heads, self.v_head_dim)
if self.is_aiter_triton_fp4_bmm_enabled:
out = rocm_aiter_ops.batched_gemm_a16wfp4(
x,
self.W_V,
self.W_V_scale,
out,
transpose_bm=True,
prequant=True,
y_scale=None,
)
x = out.view(-1, self.num_heads * self.v_head_dim)
elif self.is_aiter_triton_fp8_bmm_enabled:
# Multiply + Transpose (N, B, L) x (N, L, V)->(N, B, V)->(B, N, V)
x = rocm_aiter_ops.triton_fp8_bmm(
x, self.W_V, self.W_V_scale, group_size=128, transpose_bm=True, YQ=out
)
elif self.is_amx_bmm_enabled:
# bmm_cpu computes out[n] = mat1[n] @ mat2[n]^T against
# AMXMLAImpl's own (N, V, L) packed W_UV -- same as prefill.
ops.bmm_cpu(
out.transpose(0, 1),
x,
self.impl._w_uv_packed, # type: ignore[attr-defined]
True,
self.impl._w_scale, # type: ignore[attr-defined]
)
else:
# Multiply + Transpose (N, B, L) x (N, L, V)->(N, B, V)->(B, N, V)
torch.bmm(x, self.W_UV, out=out.transpose(0, 1))
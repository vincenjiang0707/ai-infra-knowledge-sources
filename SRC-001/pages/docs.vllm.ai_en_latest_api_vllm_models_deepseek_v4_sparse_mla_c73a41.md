source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/sparse_mla/
lastmod: 2026-09-23

class DeepseekV4SparseMLAMetadataBuilder(
AttentionMetadataBuilder[DeepseekV4FlashMLAMetadata]
):
_cudagraph_support: ClassVar[AttentionCGSupport] = AttentionCGSupport.UNIFORM_BATCH
def __init__(
self,
kv_cache_spec: AttentionSpec,
layer_names: list[str],
vllm_config: VllmConfig,
device: torch.device,
) -> None:
super().__init__(kv_cache_spec, layer_names, vllm_config, device)
self.model_config = vllm_config.model_config
# Classify single-token queries (plus num_speculative_tokens via
# supports_spec_as_decode=True) as decodes; longer queries go to prefill.
self._init_reorder_batch_threshold(1, supports_spec_as_decode=True)
self.topk_tokens = self.model_config.hf_config.index_topk
max_num_batched_tokens = vllm_config.scheduler_config.max_num_batched_tokens
self.req_id_per_token_buffer = torch.empty(
(max_num_batched_tokens,), dtype=torch.int32, device=device
)
assert isinstance(self.kv_cache_spec.tokens_per_state, int)
self.compress_ratio = self.kv_cache_spec.tokens_per_state
# Pre-allocate compressed slot mapping buffer for CUDA graph address
# stability when compress_ratio > 1.
if self.compress_ratio > 1:
self.compressed_slot_mapping_buffer = torch.empty(
max_num_batched_tokens, dtype=torch.int64, device=device
)
# Pre-allocate C128A topk buffers for CUDA graph address stability.
if self.compress_ratio == 128:
c128a_max_compressed = cdiv(
self.model_config.max_model_len, self.compress_ratio
)
c128a_max_compressed = (
cdiv(c128a_max_compressed, _C128A_TOPK_ALIGNMENT)
* _C128A_TOPK_ALIGNMENT
)
# Stored so _build_c128a_metadata passes it as the kernel's
# max_compressed_tokens, matching the buffer stride. Otherwise the
# kernel's default 8192 iterates past row width and spills writes
# into adjacent rows (present in both decode and prefill branches of
# _build_c128a_topk_metadata_kernel).
self.c128a_max_compressed = c128a_max_compressed
self.c128a_global_decode_buffer = torch.empty(
(max_num_batched_tokens, c128a_max_compressed),
dtype=torch.int32,
device=device,
)
self.c128a_decode_lens_buffer = torch.empty(
max_num_batched_tokens, dtype=torch.int32, device=device
)
self.c128a_prefill_buffer = torch.empty(
(max_num_batched_tokens, c128a_max_compressed),
dtype=torch.int32,
device=device,
)
def build(
self,
common_prefix_len: int,
common_attn_metadata: CommonAttentionMetadata,
fast_build: bool = False,
) -> DeepseekV4FlashMLAMetadata:
cm = common_attn_metadata
req_id_per_token = cm.token_to_req_indices(self.req_id_per_token_buffer)
slot_mapping = cm.slot_mapping
if self.compress_ratio > 1:
slot_mapping = get_compressed_slot_mapping(
cm.num_actual_tokens,
cm.slot_mapping,
cm.query_start_loc,
cm.seq_lens,
cm.block_table_tensor.clamp_(min=0),
int(self.kv_cache_spec.num_states),
self.compress_ratio,
out=self.compressed_slot_mapping_buffer,
)
c128a_fields: dict[str, torch.Tensor | None] = {}
if self.compress_ratio == 128:
c128a_fields = self._build_c128a_metadata(cm, req_id_per_token)
return DeepseekV4FlashMLAMetadata(
num_reqs=cm.num_reqs,
max_query_len=cm.max_query_len,
max_seq_len=cm.max_seq_len,
num_actual_tokens=cm.num_actual_tokens,
query_start_loc=cm.query_start_loc,
slot_mapping=slot_mapping,
block_table=cm.block_table_tensor,
req_id_per_token=req_id_per_token,
block_size=self.kv_cache_spec.block_size,
topk_tokens=self.topk_tokens,
c128a_global_decode_topk_indices=c128a_fields.get(
"c128a_global_decode_topk_indices"
),
c128a_decode_topk_lens=c128a_fields.get("c128a_decode_topk_lens"),
c128a_prefill_topk_indices=c128a_fields.get("c128a_prefill_topk_indices"),
)
def _build_c128a_metadata(
self,
cm: CommonAttentionMetadata,
req_id_per_token: torch.Tensor,
) -> dict[str, torch.Tensor | None]:
"""Pre-compute C128A topk indices for DeepseekV4 (compress_ratio >= 128)."""
# Must match SWA's decode split (no `require_uniform=True`) so
# `c128a_global_decode_topk_indices.shape[0]` lines up with q in
# `_forward_decode`. The per-token C128A kernel handles non-uniform
# query lengths.
(num_decodes, _, num_decode_tokens, num_prefill_tokens) = (
split_decodes_and_prefills(
cm,
decode_threshold=self.reorder_batch_threshold or 1,
)
)
num_total = num_decode_tokens + num_prefill_tokens
if num_total == 0:
return {}
assert cm.positions is not None, (
"positions is required for C128A metadata build"
)
active_topk_width = min(
max(
triton.next_power_of_2(max(cm.max_seq_len // self.compress_ratio, 1)),
_C128A_TOPK_ALIGNMENT,
),
self.c128a_max_compressed,
)
assert active_topk_width >= cm.max_seq_len // self.compress_ratio
assert active_topk_width % _C128A_TOPK_ALIGNMENT == 0
block_size = self.kv_cache_spec.block_size // self.compress_ratio
global_decode, decode_lens, prefill_local = build_c128a_topk_metadata(
cm.positions[:num_total],
self.compress_ratio,
num_decode_tokens,
req_id_per_token,
cm.block_table_tensor[:num_decodes],
block_size,
cm.slot_mapping,
self.c128a_global_decode_buffer,
self.c128a_decode_lens_buffer,
self.c128a_prefill_buffer,
max_compressed_tokens=active_topk_width,
)
result: dict[str, torch.Tensor | None] = {}
if num_decode_tokens > 0:
result["c128a_global_decode_topk_indices"] = global_decode.view(
num_decode_tokens, 1, -1
)
result["c128a_decode_topk_lens"] = decode_lens
if num_prefill_tokens > 0:
result["c128a_prefill_topk_indices"] = prefill_local
return result
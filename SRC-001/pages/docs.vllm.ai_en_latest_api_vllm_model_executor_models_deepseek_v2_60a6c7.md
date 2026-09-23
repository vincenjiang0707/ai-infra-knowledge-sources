source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/deepseek_v2/
lastmod: 2026-09-23

class DeepseekV2MLAAttention(nn.Module):
"""Main reference: DeepseekV2 paper, and FlashInfer Implementation
(https://arxiv.org/abs/2405.04434 and https://github.com/flashinfer-ai/flashinfer/pull/551).
For more info see MLACommonImpl in:
vllm/v1/attention/backends/mla/utils.py
"""
def __init__(
self,
vllm_config: VllmConfig,
config: DeepseekV2Config | DeepseekV3Config,
hidden_size: int,
num_heads: int,
qk_nope_head_dim: int,
qk_rope_head_dim: int,
v_head_dim: int,
q_lora_rank: int | None,
kv_lora_rank: int,
max_position_embeddings: int = 8192,
cache_config: CacheConfig | None = None,
quant_config: QuantizationConfig | None = None,
prefix: str = "",
topk_indices_buffer: torch.Tensor | None = None,
index_group_builder: SparseMLAIndexGroupBuilder | None = None,
input_size: int | None = None,
reduce_results: bool = True,
non_causal_multi_token_decode: bool = False,
) -> None:
super().__init__()
self.hidden_size = hidden_size
self.qk_nope_head_dim = qk_nope_head_dim
self.qk_rope_head_dim = qk_rope_head_dim
self.qk_head_dim = qk_nope_head_dim + qk_rope_head_dim
self.v_head_dim = v_head_dim
self.q_lora_rank = q_lora_rank
self.kv_lora_rank = kv_lora_rank
self.num_heads = num_heads
tp_size = get_tensor_model_parallel_world_size()
assert num_heads % tp_size == 0
self.num_local_heads = num_heads // tp_size
self.scaling = self.qk_head_dim**-0.5
self.max_position_embeddings = max_position_embeddings
# Use input_size for projection input dimensions if provided,
# otherwise default to hidden_size (used in Eagle3 Deepseek with MLA)
proj_input_size = input_size if input_size is not None else self.hidden_size
if self.q_lora_rank is not None:
self.fused_qkv_a_proj = DeepSeekV2FusedQkvAProjLinear(
proj_input_size,
[self.q_lora_rank, self.kv_lora_rank + self.qk_rope_head_dim],
quant_config=quant_config,
prefix=f"{prefix}.fused_qkv_a_proj",
)
else:
self.kv_a_proj_with_mqa = ReplicatedLinear(
proj_input_size,
self.kv_lora_rank + self.qk_rope_head_dim,
bias=False,
quant_config=quant_config,
prefix=f"{prefix}.kv_a_proj_with_mqa",
)
# The env var predates the config field and still wins if set explicitly.
qrep_requested = (
envs.VLLM_DCP_Q_REPLICATE
if envs.is_set("VLLM_DCP_Q_REPLICATE")
else bool(vllm_config.parallel_config.dcp_q_replicate)
)
qrep_enabled = (
qrep_requested
and vllm_config.parallel_config.decode_context_parallel_size > 1
and vllm_config.parallel_config.prefill_context_parallel_size <= 1
)
q_proj_cls = (
DCPGroupColumnParallelLinear if qrep_enabled else ColumnParallelLinear
)
if self.q_lora_rank is not None:
self.q_a_layernorm = RMSNorm(self.q_lora_rank, eps=config.rms_norm_eps)
self.q_b_proj = q_proj_cls(
self.q_lora_rank,
self.num_heads * self.qk_head_dim,
bias=False,
quant_config=quant_config,
prefix=f"{prefix}.q_b_proj",
)
else:
self.q_proj = q_proj_cls(
proj_input_size,
self.num_heads * self.qk_head_dim,
bias=False,
quant_config=quant_config,
prefix=f"{prefix}.q_proj",
)
self.kv_a_layernorm = RMSNorm(self.kv_lora_rank, eps=config.rms_norm_eps)
self.kv_b_proj = ColumnParallelLinear(
self.kv_lora_rank,
self.num_heads * (self.qk_nope_head_dim + self.v_head_dim),
bias=False,
quant_config=quant_config,
prefix=f"{prefix}.kv_b_proj",
)
self.o_proj = RowParallelLinear(
self.num_heads * self.v_head_dim,
self.hidden_size,
bias=False,
reduce_results=reduce_results,
quant_config=quant_config,
prefix=f"{prefix}.o_proj",
)
if config.rope_parameters["rope_type"] != "default":
config.rope_parameters["rope_type"] = (
"deepseek_llama_scaling"
if config.rope_parameters.get("attention_factor") == 1.0
else "deepseek_yarn"
)
self.rotary_emb = get_rope(
qk_rope_head_dim,
max_position=max_position_embeddings,
rope_parameters=config.rope_parameters,
is_neox_style=False,
)
if (
config.rope_parameters["rope_type"] != "default"
and config.rope_parameters["rope_type"] == "deepseek_yarn"
):
mscale_all_dim = config.rope_parameters.get("mscale_all_dim", False)
scaling_factor = config.rope_parameters["factor"]
mscale = yarn_get_mscale(scaling_factor, float(mscale_all_dim))
self.scaling = self.scaling * mscale * mscale
self.is_v32 = hasattr(config, "index_topk")
# IndexCache config
# Refer: https://arxiv.org/abs/2603.12201 for more details.
_skip_topk = False
is_mtp_layer = False
if self.is_v32:
_index_topk_freq = getattr(config, "index_topk_freq", 1)
_index_topk_pattern = getattr(config, "index_topk_pattern", None)
_index_skip_topk_offset = getattr(config, "index_skip_topk_offset", 2)
layer_id = extract_layer_index(prefix)
if _index_topk_pattern is None:
_skip_topk = (
max(layer_id - _index_skip_topk_offset + 1, 0) % _index_topk_freq
!= 0
)
elif 0 <= layer_id < len(_index_topk_pattern):
_skip_topk = _index_topk_pattern[layer_id] == "S"
# The skip pattern only governs backbone layers. MTP/nextn
# layers (layer_id >= num_hidden_layers) always build a full
# indexer: they compute indices at draft step 0 and toggle
# at runtime via set_skip_topk
# (index_share_for_mtp_iteration).
_num_hidden_layers = getattr(config, "num_hidden_layers", None)
is_mtp_layer = (
_num_hidden_layers is not None and layer_id >= _num_hidden_layers
)
if self.is_v32 and (not _skip_topk or is_mtp_layer):
assert q_lora_rank is not None
assert cache_config is not None
self.indexer_rope_emb: nn.Module | None
self.indexer: Indexer | None
self.indexer_rope_emb = get_rope(
qk_rope_head_dim,
max_position=max_position_embeddings,
rope_parameters=config.rope_parameters,
is_neox_style=not getattr(config, "indexer_rope_interleave", False),
)
self.indexer = Indexer(
vllm_config,
config,
hidden_size,
q_lora_rank,
quant_config,
cache_config,
topk_indices_buffer,
f"{prefix}.indexer",
is_inplace_rope=self.indexer_rope_emb.enabled(),
)
else:
self.indexer_rope_emb = None
self.indexer = None
mla_modules = MLAModules(
kv_a_layernorm=self.kv_a_layernorm,
kv_b_proj=self.kv_b_proj,
rotary_emb=self.rotary_emb,
o_proj=self.o_proj,
fused_qkv_a_proj=self.fused_qkv_a_proj
if self.q_lora_rank is not None
else None,
kv_a_proj_with_mqa=self.kv_a_proj_with_mqa
if self.q_lora_rank is None
else None,
q_a_layernorm=self.q_a_layernorm if self.q_lora_rank is not None else None,
q_b_proj=self.q_b_proj if self.q_lora_rank is not None else None,
q_proj=self.q_proj if self.q_lora_rank is None else None,
indexer=self.indexer,
indexer_rotary_emb=self.indexer_rope_emb,
is_sparse=self.is_v32,
topk_indices_buffer=topk_indices_buffer,
index_group_builder=index_group_builder,
)
self.mla_attn = MultiHeadLatentAttentionWrapper(
self.hidden_size,
self.num_local_heads,
self.scaling,
self.qk_nope_head_dim,
self.qk_rope_head_dim,
self.v_head_dim,
self.q_lora_rank,
self.kv_lora_rank,
mla_modules,
cache_config,
quant_config,
prefix,
# MTP layers must never start with skip_topk=True: their indexer
# computes indices at draft step 0, and the runtime toggle
# (set_skip_topk, index_share_for_mtp_iteration) only exists in
# the V1 proposer. A frozen True would leave the draft reading a
# never-written topk buffer.
skip_topk=_skip_topk and not is_mtp_layer,
non_causal_multi_token_decode=non_causal_multi_token_decode,
# Do not skip scoring for MTP layers: their top-k buffer may be
# reused by later draft iterations through index sharing.
allow_short_prefill_indexer_scoring_skip=not is_mtp_layer,
)
def forward(
self,
positions: torch.Tensor,
hidden_states: torch.Tensor,
llama_4_scaling: torch.Tensor | None,
) -> torch.Tensor:
return self.mla_attn(positions, hidden_states, llama_4_scaling)
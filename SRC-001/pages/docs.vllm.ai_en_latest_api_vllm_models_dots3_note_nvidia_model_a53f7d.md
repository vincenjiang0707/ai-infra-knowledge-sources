source: https://docs.vllm.ai/en/latest/api/vllm/models/dots3_note/nvidia/model/
lastmod: 2026-09-23

class Dots3NoteSlidingAttention(nn.Module):
"""NOTE SWA constructed directly as dense sliding-window MLA."""
def __init__(
self,
vllm_config: VllmConfig,
config,
prefix: str,
topk_indices_buffer: torch.Tensor | None = None,
) -> None:
super().__init__()
del topk_indices_buffer
num_heads = config.swa_num_attention_heads
qk_nope_head_dim = config.swa_qk_nope_head_dim
qk_rope_head_dim = config.swa_qk_rope_head_dim
v_head_dim = config.swa_v_head_dim
q_lora_rank = config.swa_q_lora_rank
kv_lora_rank = config.swa_kv_lora_rank
qk_head_dim = qk_nope_head_dim + qk_rope_head_dim
tp_size = get_tensor_model_parallel_world_size()
assert num_heads % tp_size == 0
quant_config = vllm_config.quant_config
fused_qkv_a_proj = DeepSeekV2FusedQkvAProjLinear(
config.hidden_size,
[q_lora_rank, kv_lora_rank + qk_rope_head_dim],
quant_config=quant_config,
prefix=f"{prefix}.fused_qkv_a_proj",
)
qrep_enabled = (
envs.VLLM_DCP_Q_REPLICATE
and vllm_config.parallel_config.decode_context_parallel_size > 1
and vllm_config.parallel_config.prefill_context_parallel_size <= 1
)
q_proj_cls = (
DCPGroupColumnParallelLinear if qrep_enabled else ColumnParallelLinear
)
q_a_layernorm = RMSNorm(q_lora_rank, eps=config.rms_norm_eps)
q_b_proj = q_proj_cls(
q_lora_rank,
num_heads * qk_head_dim,
bias=False,
quant_config=quant_config,
prefix=f"{prefix}.q_b_proj",
)
kv_a_layernorm = RMSNorm(kv_lora_rank, eps=config.rms_norm_eps)
kv_b_proj = ColumnParallelLinear(
kv_lora_rank,
num_heads * (qk_nope_head_dim + v_head_dim),
bias=False,
quant_config=quant_config,
prefix=f"{prefix}.kv_b_proj",
)
o_proj = RowParallelLinear(
num_heads * v_head_dim,
config.hidden_size,
bias=False,
reduce_results=False,
quant_config=quant_config,
prefix=f"{prefix}.o_proj",
)
gate_type = config.swa_attention_gate_type
gate_cls = ReplicatedLinear if gate_type == "headwise" else ColumnParallelLinear
gate_size = num_heads if gate_type == "headwise" else num_heads * v_head_dim
g_proj = gate_cls(
config.hidden_size,
gate_size,
bias=False,
quant_config=quant_config,
prefix=f"{prefix}.g_proj",
)
k_rope_only_layernorm = RMSNorm(qk_rope_head_dim, eps=config.rms_norm_eps)
rotary_emb = get_rope(
qk_rope_head_dim,
max_position=config.max_position_embeddings,
rope_parameters={
"rope_type": "default",
"rope_theta": config.swa_rope_theta,
},
is_neox_style=False,
)
cache_config = vllm_config.cache_config
if cache_config.cache_dtype == "fp8_ds_mla":
cache_config = copy.copy(cache_config)
cache_config.cache_dtype = "fp8"
apply_rescale = config.apply_mla_qkv_lora_rescale
self.hidden_size = config.hidden_size
self.num_heads = num_heads // tp_size
self.qk_nope_head_dim = qk_nope_head_dim
self.qk_rope_head_dim = qk_rope_head_dim
self.qk_head_dim = qk_head_dim
self.v_head_dim = v_head_dim
self.q_lora_rank = q_lora_rank
self.kv_lora_rank = kv_lora_rank
self.fused_qkv_a_proj = fused_qkv_a_proj
self.q_a_layernorm = q_a_layernorm
self.q_b_proj = q_b_proj
self.kv_a_layernorm = kv_a_layernorm
self.kv_b_proj = kv_b_proj
self.rotary_emb = rotary_emb
self.o_proj = o_proj
self.g_proj = g_proj
self.k_rope_only_layernorm = k_rope_only_layernorm
self.indexer = None
self.indexer_rope_emb = None
self.is_sparse = False
self.skip_topk = False
self.dcp_q_replicate = getattr(q_b_proj, "qrep_active", False)
self.attention_gate_type = gate_type
self.q_lora_scale = (
(config.hidden_size / q_lora_rank) ** 0.5 if apply_rescale else 1.0
)
self.kv_lora_scale = (
(config.hidden_size / kv_lora_rank) ** 0.5 if apply_rescale else 1.0
)
self.mla_attn = MLAAttention(
num_heads=self.num_heads,
scale=qk_head_dim**-0.5,
qk_nope_head_dim=qk_nope_head_dim,
qk_rope_head_dim=qk_rope_head_dim,
v_head_dim=v_head_dim,
q_lora_rank=q_lora_rank,
kv_lora_rank=kv_lora_rank,
kv_b_proj=kv_b_proj,
dcp_q_replicate=self.dcp_q_replicate,
cache_config=cache_config,
quant_config=quant_config,
prefix=f"{prefix}.attn",
sliding_window=config.sliding_window_size,
attn_backend=Dots3NoteTritonMLABackend,
prefill_backend_cls=Dots3NoteFlashAttnPrefillBackend,
)
def forward(
self,
positions: torch.Tensor,
hidden_states: torch.Tensor,
llama_4_scaling: torch.Tensor | None = None,
) -> torch.Tensor:
return _forward_note_mla(
self,
positions,
hidden_states,
g_proj=self.g_proj,
k_rope_only_layernorm=self.k_rope_only_layernorm,
attention_gate_type=self.attention_gate_type,
q_lora_scale=self.q_lora_scale,
kv_lora_scale=self.kv_lora_scale,
llama_4_scaling=llama_4_scaling,
)
source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/amd/linear/
lastmod: 2026-09-24

class KimiMLAAttention(nn.Module):
"""Main reference: DeepseekV2 vllm Implementation."""
def __init__(
self,
config: KimiLinearConfig,
hidden_size: int,
num_heads: int,
qk_nope_head_dim: int,
qk_rope_head_dim: int,
v_head_dim: int,
q_lora_rank: int | None,
kv_lora_rank: int,
use_nope: bool = False,
cache_config: CacheConfig | None = None,
quant_config: QuantizationConfig | None = None,
prefix: str = "",
**kwargs,
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
self.num_local_heads = num_heads // tp_size
self.scaling = self.qk_head_dim**-0.5
self.use_nope = use_nope
assert self.use_nope is True
assert num_heads % tp_size == 0
if self.q_lora_rank is not None:
self.fused_qkv_a_proj = MergedColumnParallelLinear(
self.hidden_size,
[self.q_lora_rank, self.kv_lora_rank + self.qk_rope_head_dim],
bias=False,
quant_config=quant_config,
prefix=f"{prefix}.fused_qkv_a_proj",
disable_tp=True,
)
else:
self.kv_a_proj_with_mqa = ReplicatedLinear(
self.hidden_size,
self.kv_lora_rank + self.qk_rope_head_dim,
bias=False,
quant_config=quant_config,
prefix=f"{prefix}.kv_a_proj_with_mqa",
)
if self.q_lora_rank is not None:
self.q_a_layernorm = RMSNorm(
self.q_lora_rank,
eps=config.rms_norm_eps,
)
self.q_b_proj = ColumnParallelLinear(
self.q_lora_rank,
self.num_heads * self.qk_head_dim,
bias=False,
quant_config=quant_config,
prefix=f"{prefix}.q_b_proj",
)
else:
self.q_proj = ColumnParallelLinear(
self.hidden_size,
self.num_heads * self.qk_head_dim,
bias=False,
quant_config=quant_config,
prefix=f"{prefix}.q_proj",
)
self.kv_a_layernorm = RMSNorm(
self.kv_lora_rank,
eps=config.rms_norm_eps,
)
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
quant_config=quant_config,
prefix=f"{prefix}.o_proj",
)
self.use_output_gate = config.mla_use_output_gate
if self.use_output_gate:
projection_size = self.num_heads * self.v_head_dim
self.g_proj = ColumnParallelLinear(
self.hidden_size,
projection_size,
bias=False,
quant_config=quant_config,
prefix=f"{prefix}.g_proj",
)
# TODO: Remove this mypy workaround once the K3 PR is fully merged.
mla_modules = MLAModules( # type: ignore[call-arg]
kv_a_layernorm=self.kv_a_layernorm,
kv_b_proj=self.kv_b_proj,
rotary_emb=None,
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
indexer=None,
is_sparse=False,
topk_indices_buffer=None,
g_proj=getattr(self, "g_proj", None),
)
self.mla_attn = KimiK3MultiHeadLatentAttentionWrapper(
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
)
def forward(
self,
positions: torch.Tensor,
hidden_states: torch.Tensor,
) -> torch.Tensor:
return self.mla_attn(positions, hidden_states)
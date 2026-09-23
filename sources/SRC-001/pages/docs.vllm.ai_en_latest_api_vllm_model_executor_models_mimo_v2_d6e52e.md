source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/mimo_v2/
lastmod: 2026-09-23

@support_torch_compile
class MiMoV2Model(nn.Module, EagleModelMixin):
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
config = vllm_config.model_config.hf_config.get_text_config()
quant_config = vllm_config.quant_config
eplb_config = vllm_config.parallel_config.eplb_config
self.config = config
self.quant_config = quant_config
self.vocab_size = config.vocab_size
self.num_redundant_experts = eplb_config.num_redundant_experts
if get_pp_group().is_first_rank or (
config.tie_word_embeddings and get_pp_group().is_last_rank
):
self.embed_tokens = VocabParallelEmbedding(
config.vocab_size,
config.hidden_size,
quant_config=quant_config,
prefix=f"{prefix}.embed_tokens",
)
else:
self.embed_tokens = PPMissingLayer()
self.start_layer, self.end_layer, self.layers = make_layers(
config.num_hidden_layers,
lambda prefix: MiMoV2FlashDecoderLayer(
vllm_config=vllm_config,
prefix=prefix,
),
prefix=f"{prefix}.layers",
)
self.make_empty_intermediate_tensors = make_empty_intermediate_tensors_factory(
["hidden_states", "residual"], config.hidden_size
)
if get_pp_group().is_last_rank:
self.norm = RMSNorm(config.hidden_size, eps=config.layernorm_epsilon)
else:
self.norm = PPMissingLayer()
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.embed_tokens(input_ids)
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
) -> torch.Tensor | IntermediateTensors:
if get_pp_group().is_first_rank:
if inputs_embeds is not None:
hidden_states = inputs_embeds
else:
hidden_states = self.embed_input_ids(input_ids)
residual = None
else:
assert intermediate_tensors is not None
hidden_states = intermediate_tensors["hidden_states"]
residual = intermediate_tensors["residual"]
aux_hidden_states = self._maybe_add_hidden_state(
[], self.start_layer, hidden_states, residual
)
for idx, layer in enumerate(
islice(self.layers, self.start_layer, self.end_layer)
):
hidden_states, residual = layer(positions, hidden_states, residual)
self._maybe_add_hidden_state(
aux_hidden_states, idx + 1, hidden_states, residual
)
if not get_pp_group().is_last_rank:
return IntermediateTensors(
{"hidden_states": hidden_states, "residual": residual}
)
hidden_states, _ = self.norm(hidden_states, residual)
if len(aux_hidden_states) > 0:
return hidden_states, aux_hidden_states
return hidden_states
def get_expert_mapping(self) -> list[tuple[str, str, int, str]]:
# Params for weights, fp8 weight scales, fp8 activation scales
# (param_name, weight_name, expert_id, shard_id)
return fused_moe_make_expert_params_mapping(
self,
ckpt_gate_proj_name="gate_proj",
ckpt_down_proj_name="down_proj",
ckpt_up_proj_name="up_proj",
num_experts=self.config.n_routed_experts,
num_redundant_experts=self.num_redundant_experts,
)
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
stacked_params_mapping: list[tuple[str, str, str | int]] = [
# (param_name, shard_name, shard_id)
("qkv_proj", "q_proj", "q"),
("qkv_proj", "k_proj", "k"),
("qkv_proj", "v_proj", "v"),
("gate_up_proj", "gate_proj", 0),
("gate_up_proj", "up_proj", 1),
]
tp_rank = get_tensor_model_parallel_rank()
tp_size = get_tensor_model_parallel_world_size()
params_dict = dict(self.named_parameters(remove_duplicate=False))
loaded_params: set[str] = set()
expert_params_mapping = self.get_expert_mapping()
# Pro-format fused qkv_proj arrives as two tensors (weight and
# weight_scale_inv). Store them per-layer so that they can be
# sharded together.
pending_fp8_qkv_proj: dict[str, dict[str, torch.Tensor]] = {}
for name, loaded_weight in weights:
if "rotary_emb.inv_freq" in name:
continue
if "rotary_emb.cos_cached" in name or "rotary_emb.sin_cached" in name:
continue
if "mtp" in name:
continue
expert_matched = False
for param_name, weight_name, expert_id, shard_id in expert_params_mapping:
if weight_name not in name:
continue
name_rewritten = name.replace(weight_name, param_name)
if is_pp_missing_parameter(name_rewritten, self):
continue
if (
name_rewritten.endswith(".bias") or name_rewritten.endswith("_bias")
) and name_rewritten not in params_dict:
continue
if name_rewritten not in params_dict:
continue
param = params_dict[name_rewritten]
weight_loader = param.weight_loader
weight_loader(
param,
loaded_weight,
name_rewritten,
shard_id=shard_id,
expert_id=expert_id,
)
loaded_params.add(name_rewritten)
expert_matched = True
break
if expert_matched:
continue
# Support fused qkv_proj checkpoint (Pro format)
if self._try_load_fp8_qkv_proj(
name,
loaded_weight,
pending_fp8_qkv_proj,
params_dict,
loaded_params,
tp_rank,
tp_size,
):
continue
stacked_matched = False
for param_name, weight_name, stacked_shard_id in stacked_params_mapping:
if weight_name not in name:
continue
name_rewritten = name.replace(weight_name, param_name)
if (
name_rewritten.endswith(".bias")
and name_rewritten not in params_dict
):
continue
if is_pp_missing_parameter(name_rewritten, self):
continue
if name_rewritten not in params_dict:
continue
param = params_dict[name_rewritten]
weight_loader = getattr(param, "weight_loader", default_weight_loader)
weight_loader(param, loaded_weight, stacked_shard_id)
loaded_params.add(name_rewritten)
stacked_matched = True
break
if stacked_matched:
continue
if name.endswith(".bias") and name not in params_dict:
continue
orig_name = name
mapped_name = maybe_remap_kv_scale_name(name, params_dict)
name = mapped_name if mapped_name is not None else orig_name
if name not in params_dict:
continue
param = params_dict[name]
if "attention_sink_bias" in name:
total_heads = loaded_weight.shape[0]
heads_per_rank = total_heads // tp_size
head_start = tp_rank * heads_per_rank
narrow_weight = loaded_weight.narrow(0, head_start, heads_per_rank)
param.data.copy_(narrow_weight)
loaded_params.add(name)
else:
weight_loader = getattr(param, "weight_loader", default_weight_loader)
weight_loader(param, loaded_weight)
loaded_params.add(name)
return loaded_params
def _try_load_fp8_qkv_proj(
self,
name: str,
tensor: torch.Tensor,
fp8_qkv_proj_dict: dict[str, dict[str, torch.Tensor]],
params_dict: dict[str, torch.nn.Parameter],
loaded_params: set[str],
tp_rank: int,
tp_size: int,
) -> bool:
"""The fused fp8 QKV projection weights and scale are stored separately.
Special care must be taken while sharding these tensors across TP ranks.
See _shard_fp8_qkv_proj for more details.
Returns:
True if ``tensor`` was an fp8 qkv_proj weight/scale and was consumed
(caller should skip it); False otherwise, so the caller falls
through to its normal loading path.
"""
is_weight = (
name.endswith("qkv_proj.weight") and tensor.dtype == torch.float8_e4m3fn
)
is_scale = name.endswith("qkv_proj.weight_scale_inv")
if not is_weight and not is_scale:
# Weight is not in FP8 format. Ignore.
return False
if is_pp_missing_parameter(name, self):
# This qkv_proj is for a layer not on this PP rank.
return True
prefix, qkv_kind = name.rsplit(".", 1)
entry = fp8_qkv_proj_dict.setdefault(prefix, {})
entry[qkv_kind] = tensor
if "weight" not in entry or "weight_scale_inv" not in entry:
# Still waiting for the other param.
return True
del fp8_qkv_proj_dict[prefix]
# Get self_attn module, which is a parent of qkv_proj.
attn = self.get_submodule(prefix.rsplit(".", 1)[0])
# Shard the qkv_proj per-rank.
w_rank, s_rank = _shard_fp8_qkv_proj(
entry["weight"],
entry["weight_scale_inv"],
num_heads=attn.total_num_heads,
num_kv_heads=attn.total_num_kv_heads,
head_dim=attn.head_dim,
v_head_dim=attn.v_head_dim,
tp_rank=tp_rank,
tp_size=tp_size,
# The fused qkv_proj is pre-sharded for this many ranks.
ckpt_tp=self.config.num_key_value_heads,
)
sharded = {"weight": w_rank, "weight_scale_inv": s_rank}
for kind, tensor in sharded.items():
param_name = f"{prefix}.{kind}"
param = params_dict[param_name]
if tensor.shape[0] > param.shape[0]:
tensor = tensor[: param.shape[0]]
default_weight_loader(param, tensor)
loaded_params.add(param_name)
return True
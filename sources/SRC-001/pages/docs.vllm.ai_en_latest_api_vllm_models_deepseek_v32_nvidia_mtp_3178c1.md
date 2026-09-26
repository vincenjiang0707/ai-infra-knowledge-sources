source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v32/nvidia/mtp/
lastmod: 2026-09-24

class DeepseekV32MTP(nn.Module, DeepseekV2MixtureOfExperts, SupportsPP):
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
self.config = vllm_config.model_config.hf_config
self.quant_config = vllm_config.quant_config
self.model = DeepseekV32MultiTokenPredictor(
vllm_config=vllm_config, prefix=maybe_prefix(prefix, "model")
)
if self.config.model_type == "glm_moe_dsa":
enable_glm52_low_latency_gemm(self, vllm_config.model_config.dtype)
self.set_moe_parameters()
self.make_empty_intermediate_tensors = make_empty_intermediate_tensors_factory(
["hidden_states", "residual"], self.config.hidden_size
)
def set_moe_parameters(self):
self.num_moe_layers = self.config.num_nextn_predict_layers
self.num_expert_groups = self.config.n_group
self.moe_layers = []
self.moe_mlp_layers = []
example_moe = None
for layer in self.model.layers.values():
mlp = layer.mtp_block.mlp
if isinstance(mlp, DeepseekV2MoE):
example_moe = mlp
self.moe_mlp_layers.append(mlp)
self.moe_layers.append(mlp.experts)
self.extract_moe_parameters(example_moe)
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.model.embed_input_ids(input_ids)
def forward( # type: ignore[override]
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
hidden_states: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
spec_step_idx: int = 0,
) -> torch.Tensor:
return self.model(
input_ids, positions, hidden_states, inputs_embeds, spec_step_idx
)
def compute_logits(
self,
hidden_states: torch.Tensor,
spec_step_idx: int = 0,
) -> torch.Tensor | None:
return self.model.compute_logits(hidden_states, spec_step_idx)
def get_top_tokens(
self,
hidden_states: torch.Tensor,
spec_step_idx: int = 0,
) -> torch.Tensor:
"""See ``DeepseekV32MultiTokenPredictor.get_top_tokens``."""
return self.model.get_top_tokens(hidden_states, spec_step_idx)
def _rewrite_spec_layer_name(self, spec_layer: int, name: str) -> str:
spec_layer_weight_names = [
"embed_tokens",
"enorm",
"hnorm",
"eh_proj",
"shared_head",
]
shared_weight_names = ["embed_tokens"]
spec_layer_weight = False
shared_weight = False
for weight_name in spec_layer_weight_names:
if weight_name in name:
spec_layer_weight = True
if weight_name in shared_weight_names:
shared_weight = True
break
if not spec_layer_weight:
name = name.replace(
f"model.layers.{spec_layer}.", f"model.layers.{spec_layer}.mtp_block."
)
elif shared_weight:
name = name.replace(f"model.layers.{spec_layer}.", "model.")
return name
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
stacked_params_mapping = [
("gate_up_proj", "gate_proj", 0),
("gate_up_proj", "up_proj", 1),
("fused_qkv_a_proj", "q_a_proj", 0),
("fused_qkv_a_proj", "kv_a_proj_with_mqa", 1),
("wk_weights_proj", "wk", 0),
("wk_weights_proj", "weights_proj", 1),
]
expert_params_mapping = fused_moe_make_expert_params_mapping(
self,
ckpt_gate_proj_name="gate_proj",
ckpt_down_proj_name="down_proj",
ckpt_up_proj_name="up_proj",
num_experts=self.config.n_routed_experts,
)
pp_missing_layer_names = get_pp_missing_layer_names(self)
params_dict = dict(self.named_parameters())
loaded_params: set[str] = set()
_pending_wk_fp8: dict = {}
for name, loaded_weight in weights:
if "rotary_emb.inv_freq" in name:
continue
spec_layer = get_spec_layer_idx_from_weight_name(self.config, name)
if spec_layer is None:
# A tied top-level embed_tokens has no spec layer to rewrite
# from; the draft needs its own copy under PP.
param = params_dict.get(name) if "embed_tokens" in name else None
if param is not None:
weight_loader = getattr(
param, "weight_loader", default_weight_loader
)
weight_loader(param, loaded_weight)
loaded_params.add(name)
continue
name = self._rewrite_spec_layer_name(spec_layer, name)
if _try_load_fp8_indexer_wk(
name,
loaded_weight,
_pending_wk_fp8,
params_dict,
loaded_params,
pp_missing_layer_names,
):
continue
for param_name, weight_name, shard_id in stacked_params_mapping:
if weight_name not in name:
continue
if ("mlp.experts." in name) and name not in params_dict:
continue
name_mapped = name.replace(weight_name, param_name)
if (
param_name == "fused_qkv_a_proj"
) and name_mapped not in params_dict:
continue
else:
name = name_mapped
if name.endswith(".bias") and name not in params_dict:
continue
param = params_dict[name]
weight_loader = param.weight_loader
weight_loader(param, loaded_weight, shard_id)
break
else:
num_chunks = 1
for j in range(num_chunks):
chunk_name = name
weight_to_load = loaded_weight
is_expert_weight = False
for mapping in expert_params_mapping:
param_name, weight_name, expert_id, shard_id = mapping # type: ignore[assignment]
if weight_name not in chunk_name:
continue
is_expert_weight = True
name_mapped = chunk_name.replace(weight_name, param_name)
param = params_dict[name_mapped]
weight_loader = typing.cast(
Callable[..., bool], param.weight_loader
)
success = weight_loader(
param,
weight_to_load,
name_mapped,
shard_id=shard_id,
expert_id=expert_id,
return_success=True,
)
if success:
name = name_mapped
break
else:
if is_expert_weight:
continue
if name.endswith(".bias") and name not in params_dict:
continue
name = maybe_remap_kv_scale_name(name, params_dict) # type: ignore[assignment]
if name is None:
continue
if (
spec_layer != self.model.mtp_start_layer_idx
and ".layers" not in name
):
continue
param = params_dict[name]
weight_loader = getattr(
param, "weight_loader", default_weight_loader
)
weight_loader(param, loaded_weight)
loaded_params.add(name)
loaded_layers: set[int] = set()
for param_name in loaded_params:
spec_layer = get_spec_layer_idx_from_weight_name(self.config, param_name)
if spec_layer is not None:
loaded_layers.add(spec_layer)
for layer_idx in range(
self.model.mtp_start_layer_idx,
self.model.mtp_start_layer_idx + self.model.num_mtp_layers,
):
if layer_idx not in loaded_layers and is_mtp_completeness_check_enabled():
raise ValueError(
f"MTP speculative decoding layer {layer_idx} weights "
f"missing from checkpoint."
)
return loaded_params
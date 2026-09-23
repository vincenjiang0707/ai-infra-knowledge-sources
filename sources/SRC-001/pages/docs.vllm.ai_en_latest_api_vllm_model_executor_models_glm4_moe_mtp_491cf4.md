source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/glm4_moe_mtp/
lastmod: 2026-09-23

class Glm4MoeMTP(nn.Module, Glm4MixtureOfExperts):
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
self.config = vllm_config.model_config.hf_config
self.model = Glm4MoeMultiTokenPredictor(
vllm_config=vllm_config, prefix=maybe_prefix(prefix, "model")
)
# Set MoE hyperparameters
self.num_moe_layers = self.config.num_nextn_predict_layers
self.num_expert_groups = self.config.n_group
self.moe_layers: list[MoERunner] = []
self.moe_mlp_layers: list[Glm4MoE] = []
example_moe = None
for layer in self.model.layers.values():
assert isinstance(layer, Glm4MoeMultiTokenPredictorLayer)
layer = layer.mtp_block
assert isinstance(layer, Glm4MoeDecoderLayer)
if isinstance(layer.mlp, Glm4MoE):
example_moe = layer.mlp
self.moe_mlp_layers.append(layer.mlp)
self.moe_layers.append(layer.mlp.experts)
self.extract_moe_parameters(example_moe)
self.is_fused_shared_expert_enabled = is_model_fused_shared_expert_compatible(
self.model.layers.values(),
Glm4MoE,
"mtp_block.mlp",
)
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.model.embed_input_ids(input_ids)
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
hidden_states: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
spec_step_idx: int = 0,
) -> torch.Tensor:
hidden_states = self.model(
input_ids, positions, hidden_states, inputs_embeds, spec_step_idx
)
return hidden_states
def compute_logits(
self,
hidden_states: torch.Tensor,
spec_step_idx: int = 0,
) -> torch.Tensor | None:
return self.model.compute_logits(hidden_states, spec_step_idx)
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
stacked_params_mapping = [
# (param_name, shard_name, shard_id)
("qkv_proj", "q_proj", "q"),
("qkv_proj", "k_proj", "k"),
("qkv_proj", "v_proj", "v"),
("gate_up_proj", "gate_proj", 0),
("gate_up_proj", "up_proj", 1),
]
# Params for weights, fp8 weight scales, fp8 activation scales
# (param_name, weight_name, expert_id, shard_id)
num_experts = self.config.n_routed_experts
if self.is_fused_shared_expert_enabled and self.config.n_shared_experts:
num_experts += self.config.n_shared_experts
expert_params_mapping = fused_moe_make_expert_params_mapping(
self,
ckpt_gate_proj_name="gate_proj",
ckpt_down_proj_name="down_proj",
ckpt_up_proj_name="up_proj",
num_experts=num_experts,
)
params_dict = dict(self.named_parameters())
loaded_params: set[str] = set()
for name, loaded_weight in weights:
if name == "lm_head.weight":
spec_layer = self.model.mtp_start_layer_idx
name = f"model.layers.{spec_layer}.shared_head.head.weight"
elif name == "model.embed_tokens.weight":
spec_layer = self.model.mtp_start_layer_idx
else:
spec_layer = get_spec_layer_idx_from_weight_name(self.config, name)
if spec_layer is None:
continue
name = self._rewrite_spec_layer_name(spec_layer, name)
is_fusion_moe_shared_experts_layer = (
self.is_fused_shared_expert_enabled and ("mlp.shared_experts" in name)
)
for param_name, weight_name, shard_id in stacked_params_mapping:
# Skip non-stacked layers and experts (experts handled below).
if weight_name not in name:
continue
# We have mlp.experts[0].gate_proj in the checkpoint.
# Since we handle the experts below in expert_params_mapping,
# we need to skip here BEFORE we update the name, otherwise
# name will be updated to mlp.experts[0].gate_up_proj, which
# will then be updated below in expert_params_mapping
# for mlp.experts[0].gate_gate_up_proj, which breaks load.
if ("mlp.experts." in name) and name not in params_dict:
continue
if is_fusion_moe_shared_experts_layer:
continue
name = name.replace(weight_name, param_name)
# Skip loading extra bias for GPTQ models.
if name.endswith(".bias") and name not in params_dict:
continue
param = params_dict[name]
weight_loader = param.weight_loader
weight_loader(param, loaded_weight, shard_id)
break
else:
# FSE: split a widened mlp.shared_experts tensor into
# n_shared_experts chunks; see deepseek_v2.py for details.
num_chunks = 1
split_dim = 0
chunk_size = 0
if is_fusion_moe_shared_experts_layer:
num_chunks = getattr(self.config, "n_shared_experts", 1) or 1
split_dim = (
1
if ("down_proj.weight" in name and loaded_weight.ndim > 1)
else 0
)
total = loaded_weight.shape[split_dim]
if total % num_chunks != 0:
raise ValueError(
f"FSE shared-expert weight {name} has dim "
f"{total} along axis {split_dim} which is "
f"not divisible by "
f"n_shared_experts={num_chunks}."
)
chunk_size = total // num_chunks
for j in range(num_chunks):
chunk_name = name
weight_to_load = loaded_weight
if is_fusion_moe_shared_experts_layer:
chunk_slice = slice(j * chunk_size, (j + 1) * chunk_size)
if loaded_weight.ndim == 1:
weight_to_load = loaded_weight[chunk_slice]
elif split_dim == 0:
weight_to_load = loaded_weight[chunk_slice, :]
else:
weight_to_load = loaded_weight[:, chunk_slice]
chunk_name = name.replace(
"mlp.shared_experts",
f"mlp.experts.{self.config.n_routed_experts + j}",
)
is_expert_weight = False
for mapping in expert_params_mapping:
param_name, weight_name, expert_id, shard_id = mapping
if weight_name not in chunk_name:
continue
is_expert_weight = True
name_mapped = chunk_name.replace(weight_name, param_name)
param = params_dict[name_mapped]
# Use return_success so we don't blindly mark
# remote-expert replicas as loaded on this rank.
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
if not is_fusion_moe_shared_experts_layer:
name = name_mapped
else:
loaded_params.add(name_mapped)
break
else:
if is_expert_weight:
# Expert weight not local to this rank; skip.
continue
# Skip loading extra bias for GPTQ models.
if name.endswith(".bias") and name not in params_dict:
continue
# Some checkpoints include weight scale tensors for
# the LM head even when the quantized head isn't
# built. Skip them if the model does not expose a
# matching parameter to avoid KeyError during load.
if name.endswith(".weight_scale") and name not in params_dict:
continue
# According to DeepSeek-V3 Technical Report, MTP
# modules share the embedding layer. We only load
# the first weights.
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
if not is_fusion_moe_shared_experts_layer:
loaded_params.add(name)
return loaded_params
def _rewrite_spec_layer_name(self, spec_layer: int, name: str) -> str:
"""Rewrite the weight name to match the format of the original model.
Add .mtp_block for modules in transformer layer block for spec layer
and rename shared layer weights to be top level.
"""
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
# treat rest weights as weights for transformer layer block
name = name.replace(
f"model.layers.{spec_layer}.", f"model.layers.{spec_layer}.mtp_block."
)
elif shared_weight:
# treat shared weights as top level weights
name = name.replace(f"model.layers.{spec_layer}.", "model.")
return name
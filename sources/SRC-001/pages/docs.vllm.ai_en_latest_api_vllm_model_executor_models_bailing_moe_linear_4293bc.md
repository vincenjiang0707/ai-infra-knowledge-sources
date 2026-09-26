source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/bailing_moe_linear/
lastmod: 2026-09-24

@support_torch_compile(
dynamic_arg_dims={
"input_ids": 0,
"positions": -1,
"intermediate_tensors": 0,
"inputs_embeds": 0,
}
)
class BailingMoeV25Model(nn.Module):
"""Bailing MoE v2.5 Model with hybrid attention support."""
def __init__(
self,
*,
vllm_config: VllmConfig,
prefix: str = "",
):
super().__init__()
config = vllm_config.model_config.hf_config
self.config = config
self.vocab_size = config.vocab_size
self.embed_dim = config.hidden_size
# Determine layer types based on layer_group_size
self.layer_group_size = getattr(config, "layer_group_size", 1)
self.num_layers = config.num_hidden_layers
# decoder_attention_types: 0 = linear, 1 = full
self.decoder_attention_types = [
0 if is_linear_layer(i, self.layer_group_size) else 1
for i in range(self.num_layers)
]
# Embeddings
if get_pp_group().is_first_rank:
self.word_embeddings = VocabParallelEmbedding(
self.vocab_size,
self.embed_dim,
org_num_embeddings=self.vocab_size,
)
else:
from vllm.model_executor.models.utils import PPMissingLayer
self.word_embeddings = PPMissingLayer()
# Layers
def layer_fn(prefix):
layer_idx = int(prefix.split(".")[-1])
layer_config = copy.deepcopy(config)
layer_config.attention_type = self.decoder_attention_types[layer_idx]
return BailingMoeV25DecoderLayer(
config=layer_config,
vllm_config=vllm_config,
prefix=prefix,
layer_id=layer_idx,
)
self.start_layer, self.end_layer, self.layers = make_layers(
self.num_layers, layer_fn, prefix=f"{prefix}.layers"
)
# Final norm
norm_kwargs = {}
if hasattr(config, "rms_norm_eps"):
norm_kwargs["eps"] = config.rms_norm_eps
if get_pp_group().is_last_rank:
self.norm = RMSNorm(config.hidden_size, **norm_kwargs)
else:
from vllm.model_executor.models.utils import PPMissingLayer
self.norm = PPMissingLayer()
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.word_embeddings(input_ids)
@property
def embed_tokens(self) -> nn.Module:
return self.word_embeddings
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
) -> torch.Tensor:
forward_context = get_forward_context()
attn_metadata = forward_context.attn_metadata
if get_pp_group().is_first_rank:
if inputs_embeds is None:
hidden_states = self.word_embeddings(input_ids)
else:
hidden_states = inputs_embeds
residual = None
else:
assert intermediate_tensors is not None
hidden_states = intermediate_tensors["hidden_states"]
residual = intermediate_tensors["residual"]
for layer in self.layers[self.start_layer : self.end_layer]:
hidden_states, residual = layer(
hidden_states=hidden_states,
positions=positions,
attn_metadata=attn_metadata,
residual=residual,
)
if not get_pp_group().is_last_rank:
return IntermediateTensors(
{"hidden_states": hidden_states, "residual": residual}
)
else:
if residual is not None:
hidden_states, _ = self.norm(hidden_states, residual)
else:
hidden_states = self.norm(hidden_states)
return hidden_states
def get_expert_mapping(self) -> list[tuple[str, str, int, str]]:
"""Get expert parameter mapping for MoE layers."""
return fused_moe_make_expert_params_mapping(
self,
ckpt_gate_proj_name="gate_proj",
ckpt_down_proj_name="down_proj",
ckpt_up_proj_name="up_proj",
num_experts=self.config.num_experts,
num_redundant_experts=0,
)
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
"""Load checkpoint weights with simplified mapping."""
params_dict = dict(self.named_parameters(remove_duplicate=False))
loaded_params: set[str] = set()
# Stacked parameter mappings (fused projections)
stacked_mappings = [
(".fused_qkv_a_proj", ".q_a_proj", 0),
(".fused_qkv_a_proj", ".kv_a_proj_with_mqa", 1),
(".gate_up_proj", ".gate_proj", 0),
(".gate_up_proj", ".up_proj", 1),
]
# Expert parameter mappings from FusedMoEFactory
expert_mappings = list(self.get_expert_mapping())
def load_param(name: str, tensor: torch.Tensor, shard_id=None) -> bool:
"""Load a single parameter."""
if name not in params_dict or is_pp_missing_parameter(name, self):
return False
if name.endswith(".bias") and name not in params_dict:
return False
param = params_dict[name]
weight_loader: Callable[..., None] = getattr(
param, "weight_loader", default_weight_loader
)
if shard_id is None:
weight_loader(param, tensor)
elif isinstance(shard_id, int):
weight_loader(param, tensor, shard_id)
else:
# Expert param: (expert_id, shard_id)
weight_loader(
param, tensor, name, expert_id=shard_id[0], shard_id=shard_id[1]
)
loaded_params.add(name)
return True
def normalize_name(name: str) -> str | None:
"""Normalize checkpoint name to model parameter name."""
# Skip special weights
if name.startswith("model.mtp"):
return None
# Remove 'model.' prefix if present
# (e.g., 'model.layers.0...' -> 'layers.0...')
name = name.removeprefix("model.")
# Map attention.dense based on layer type
if "attention.dense" in name:
layer_idx = (
int(name.split("layers.")[1].split(".")[0])
if "layers." in name
else 0
)
attn_name = (
"self_attn.dense"
if is_linear_layer(layer_idx, self.config.layer_group_size)
else "self_attn.o_proj"
)
name = name.replace("attention.dense", attn_name)
# Standard mappings
name = name.replace("attention.", "self_attn.")
name = name.replace(
"mlp.gate.e_score_correction_bias", "mlp.gate.expert_bias"
)
return maybe_remap_kv_scale_name(name, params_dict)
for orig_name, weight in weights:
norm_name = normalize_name(orig_name)
if norm_name is None:
continue
# Try stacked mappings
loaded = False
for param_suf, weight_suf, shard_id in stacked_mappings:
if weight_suf not in norm_name:
continue
mapped = norm_name.replace(weight_suf, param_suf).replace(
"attention.", "self_attn."
)
if load_param(mapped, weight, shard_id):
loaded = True
break
if loaded:
continue
# Handle expert weights
if "mlp.experts" in norm_name:
# Expert bias
if (
"mlp.experts.e_score_correction_bias" in norm_name
or "mlp.experts.expert_bias" in norm_name
):
alt = norm_name.replace(
"mlp.experts.e_score_correction_bias", "mlp.gate.expert_bias"
).replace("mlp.experts.expert_bias", "mlp.gate.expert_bias")
if load_param(alt, weight) or load_param(norm_name, weight):
continue
# Routed experts
for (
param_name,
weight_name,
expert_id,
expert_shard_id,
) in expert_mappings:
if weight_name not in norm_name:
continue
mapped = norm_name.replace(weight_name, param_name)
if load_param(mapped, weight, (expert_id, expert_shard_id)):
break
continue
# General parameters
load_param(norm_name, weight)
return loaded_params
source: https://docs.vllm.ai/en/latest/api/vllm/models/hy_v4/nvidia/model/
lastmod: 2026-09-24

class HYV4Model(nn.Module):
"""HY V4 backbone."""
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
config = _normalize_hyv4_config(vllm_config.model_config.hf_config)
cache_config = vllm_config.cache_config
quant_config = vllm_config.quant_config
parallel_config = vllm_config.parallel_config
eplb_config = parallel_config.eplb_config
self.num_redundant_experts = eplb_config.num_redundant_experts
self.device = current_platform.device_type
self.vocab_size = config.vocab_size
self.is_sparse = hasattr(config, "index_topk")
if self.is_sparse:
self.topk_indices_buffer = torch.empty(
vllm_config.scheduler_config.max_num_batched_tokens,
config.index_topk,
dtype=torch.int32,
device=self.device,
)
else:
self.topk_indices_buffer = None
self.config = config
self.quant_config = quant_config
self.enable_ihc = getattr(config, "enable_ihc", False)
if get_pp_group().is_first_rank or (
self.config.tie_word_embeddings and get_pp_group().is_last_rank
):
self.embed_tokens = VocabParallelEmbedding(
config.vocab_size,
config.hidden_size,
)
else:
self.embed_tokens = PPMissingLayer()
self.start_layer, self.end_layer, self.layers = make_layers(
config.num_hidden_layers,
lambda prefix: HYV4DecoderLayer(
config=config,
vllm_config=vllm_config,
cache_config=cache_config,
quant_config=quant_config,
prefix=prefix,
topk_indices_buffer=self.topk_indices_buffer,
),
prefix=f"{prefix}.layers",
)
if get_pp_group().is_last_rank:
self.norm = RMSNorm(config.hidden_size, config.rms_norm_eps)
else:
self.norm = PPMissingLayer()
if self.enable_ihc:
# iHC head layer: merge the residual channels into one stream.
if get_pp_group().is_last_rank:
self.hc_head = HYV4HCHeadLayer(
config,
hidden_size=config.hidden_size,
hc_mult=config.hc_mult,
hc_eps=config.hc_eps,
prefix=f"{prefix}.hc_head",
)
else:
self.hc_head = PPMissingLayer()
self.make_empty_intermediate_tensors = (
make_empty_intermediate_tensors_factory(
["hidden_states"], config.hc_mult * config.hidden_size
)
)
else:
self.make_empty_intermediate_tensors = (
make_empty_intermediate_tensors_factory(
["hidden_states", "residual"], config.hidden_size
)
)
# MoE hyperparameters (consumed by EPLB).
self.expert_weights: MutableSequence[Sequence[torch.Tensor]] = []
self.num_expert_groups = 1
self.moe_layers: list[nn.Module] = []
example_layer: HYV4MoEFused | None = None
for layer in self.layers:
if isinstance(layer, PPMissingLayer):
continue
assert isinstance(layer, HYV4DecoderLayer)
if layer.block_type == "moe":
assert isinstance(layer.mlp, HYV4MoEFused)
example_layer = layer.mlp
self.moe_layers.append(layer.mlp.experts)
if example_layer is None:
self.num_moe_layers = 0
self.num_logical_experts = 0
self.num_physical_experts = 0
self.num_local_physical_experts = 0
self.num_routed_experts = 0
self.num_redundant_experts = 0
return
self.num_moe_layers = len(self.moe_layers)
self.num_logical_experts = example_layer.n_logical_experts
self.num_physical_experts = example_layer.n_physical_experts
self.num_local_physical_experts = example_layer.n_local_physical_experts
self.num_routed_experts = example_layer.n_routed_experts
self.num_redundant_experts = example_layer.n_redundant_experts
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.embed_tokens(input_ids)
def update_physical_experts_metadata(
self,
num_physical_experts: int,
num_local_physical_experts: int,
) -> None:
assert self.num_local_physical_experts == num_local_physical_experts
self.num_physical_experts = num_physical_experts
self.num_local_physical_experts = num_local_physical_experts
self.num_redundant_experts = num_physical_experts - self.num_logical_experts
for layer in self.layers:
if isinstance(layer, PPMissingLayer):
continue
if isinstance(layer.mlp, HYV4MoEFused):
moe = layer.mlp
moe.n_local_physical_experts = num_local_physical_experts
moe.n_physical_experts = num_physical_experts
moe.n_redundant_experts = self.num_redundant_experts
moe.experts.update_expert_map()
def get_expert_mapping(self) -> list[tuple[str, str, int, str]]:
# (param_name, weight_name, expert_id, shard_id) for weights, fp8
# weight scales and fp8 activation scales.
if not hasattr(self, "_cached_expert_params_mapping"):
self._cached_expert_params_mapping = fused_moe_make_expert_params_mapping(
self,
ckpt_gate_proj_name="gate_proj",
ckpt_down_proj_name="down_proj",
ckpt_up_proj_name="up_proj",
num_experts=self.config.num_experts,
num_redundant_experts=self.num_redundant_experts,
)
return self._cached_expert_params_mapping
def forward(
self,
input_ids: torch.Tensor,
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
# In iHC mode the flattened [num_tokens, hc*h] tensor from the
# previous PP stage is reshaped back to 3D by the first layer's
# prepare_input, and residual is unused.
residual = None if self.enable_ihc else intermediate_tensors["residual"]
for layer in islice(self.layers, self.start_layer, self.end_layer):
hidden_states, residual = layer(positions, hidden_states, residual)
if not get_pp_group().is_last_rank:
if self.enable_ihc:
# hidden_states is [num_tokens, hc, h]; flatten the channel dim
# for PP transfer (matches the 2D receive buffer).
return IntermediateTensors({"hidden_states": hidden_states.flatten(1)})
return IntermediateTensors(
{"hidden_states": hidden_states, "residual": residual}
)
if self.enable_ihc:
hidden_states = self.hc_head(hidden_states)
else:
hidden_states = hidden_states + residual
return self.norm(hidden_states)
def load_fused_expert_weights(
self,
name: str,
params_dict: dict,
loaded_weight: torch.Tensor,
shard_id: str,
num_experts: int,
) -> bool:
param = params_dict[name]
weight_loader = typing.cast(Callable[..., bool], param.weight_loader)
loaded_local_expert = False
for expert_id in range(num_experts):
curr_expert_weight = loaded_weight[expert_id]
success = weight_loader(
param,
curr_expert_weight,
name,
shard_id,
expert_id,
return_success=True,
)
if success:
loaded_local_expert = True
return loaded_local_expert
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
# FP8 indexer wk dequant buffer (weight and scale arrive separately).
pending_wk_fp8: dict[str, dict[str, torch.Tensor]] = {}
pp_missing_layer_names = get_pp_missing_layer_names(self)
skip_topk_layers = compute_skip_topk_layers(self.config)
# Must not be cached on `self`: `process_weights_after_loading` swaps in
# kernel-specific expert weights via `replace_parameter`, and a cache
# outliving this call would pin the pre-shuffle storage (OOM on large
# MoE) and make a later reload target orphaned tensors.
params_dict = dict(self.named_parameters())
# Split per-expert mapping (V3 style): experts.0.gate_proj.weight
split_expert_params_mapping = self.get_expert_mapping()
loaded_params: set[str] = set()
# Sink weights are sharded like the q/k/v linears.
sink_tp_size = get_tensor_model_parallel_world_size()
sink_tp_rank = get_tensor_model_parallel_rank()
n_local_head = self.config.num_attention_heads // sink_tp_size
head_rank_start = n_local_head * sink_tp_rank
head_rank_end = n_local_head * (sink_tp_rank + 1)
base_layer = (
"base_layer." if any(".base_layer." in name for name in params_dict) else ""
)
# Fused expert mapping: experts.gate_up_proj (all experts in one tensor).
# The packed weights are owned by the RoutedExperts submodule, so the
# targets are experts.routed_experts.[base_layer.]w{13,2}_weight.
fused_expert_prefix = f".experts.routed_experts.{base_layer}"
fused_expert_params_mapping = [
(f"{fused_expert_prefix}w13_weight", ".experts.gate_up_proj", 0, "w1"),
(f"{fused_expert_prefix}w2_weight", ".experts.down_proj", 0, "w2"),
]
num_experts = getattr(self.config, "num_experts", 0)
def _should_skip_missing_param(param_name: str) -> bool:
# Sparse checkpoints may contain indexer weights for layers that
# fall back to dense MLA on unsupported GPUs.
return ".indexer." in param_name
def _is_split_expert_weight(weight_name: str) -> bool:
"""Whether this weight is in split (per-expert) format."""
# Split format: mlp.experts.<id>.gate_proj.weight
return bool(re.search(r"\.experts\.\d+\.", weight_name))
def _is_fused_expert_weight(weight_name: str) -> bool:
"""Whether this weight is in fused (all-experts-packed) format."""
return ".experts.gate_up_proj" in weight_name or (
".experts.down_proj" in weight_name
and not _is_split_expert_weight(weight_name)
)
for name, loaded_weight in weights:
if is_skip_topk_indexer_weight(name, skip_topk_layers):
continue
if _try_load_fp8_indexer_wk(
name,
loaded_weight,
pending_wk_fp8,
params_dict,
loaded_params,
pp_missing_layer_names,
):
continue
if self.config.tie_word_embeddings and "lm_head.weight" in name:
continue
# Names and stacked shard ids are normalized upstream by
# AutoWeightsLoader, through quant_config.get_cache_scale_mapper()
# and hf_to_vllm_mapper.
stacked_shard_id = getattr(loaded_weight, "shard_id", None)
if ".indexer.wk." in name:
name = name.replace(".indexer.wk.", ".indexer.wk_weights_proj.")
stacked_shard_id = 0
# Skip loading extra bias for GPTQ models.
if name.endswith(".bias") and name not in params_dict:
continue
# Determine per-weight whether this is fused or split format.
is_fused_expert = _is_fused_expert_weight(name)
expert_params_mapping = (
fused_expert_params_mapping
if is_fused_expert
else split_expert_params_mapping
)
is_expert_weight = False
loaded_expert_param_names: set[str] = set()
for mapping in expert_params_mapping:
param_name, weight_name, expert_id, shard_id = mapping
if weight_name not in name:
continue
# This is an expert weight and must not be attempted as any
# other kind of weight later on.
is_expert_weight = True
# Do not modify `name`: the loop may continue past this point.
name_mapped = name.replace(weight_name, param_name)
if is_pp_missing_parameter(name_mapped, self):
continue
if is_fused_expert:
if "experts.gate_up_proj" in name:
chunks = loaded_weight.chunk(2, dim=-2)
success_w1 = self.load_fused_expert_weights(
name_mapped, params_dict, chunks[0], "w1", num_experts
)
success_w3 = self.load_fused_expert_weights(
name_mapped, params_dict, chunks[1], "w3", num_experts
)
success = success_w1 and success_w3
else:
success = self.load_fused_expert_weights(
name_mapped,
params_dict,
loaded_weight,
shard_id,
num_experts,
)
if success:
name = name_mapped
break
else:
# Split per-expert format (V3 style).
if name_mapped not in params_dict:
if _should_skip_missing_param(name_mapped):
continue
logger.warning_once(
"Skipping unknown checkpoint weight: %s",
name_mapped,
)
continue
param = params_dict[name_mapped]
# Ask the weight loader whether it succeeded, otherwise we
# may skip experts that have other available replicas.
weight_loader: Callable[..., typing.Any] = param.weight_loader
success = weight_loader(
param,
loaded_weight,
name_mapped,
shard_id=shard_id,
expert_id=expert_id,
return_success=True,
)
if success:
if not is_fused_expert:
loaded_expert_param_names.add(name_mapped)
continue
name = name_mapped
break
else:
if loaded_expert_param_names:
loaded_params.update(loaded_expert_param_names)
continue
if "learnable_sink_param" in name:
if is_pp_missing_parameter(name, self):
continue
narrow_weight = loaded_weight[head_rank_start:head_rank_end]
n = narrow_weight.shape[0]
with torch.no_grad():
params_dict[name][:n].copy_(narrow_weight)
else:
if is_expert_weight:
# An expert weight that is not mapped to this rank.
continue
if "gate.e_score_correction_bias" in name:
name = name.replace(
"gate.e_score_correction_bias", "expert_bias"
)
if "router.gate." in name:
name = name.replace("router.", "")
if "hc_fn" in name:
name = name.replace("hc_fn", "hc_fn.weight")
if "hc_head_fn" in name:
name = name.replace("hc_head_fn", "hc_head_fn.weight")
if is_pp_missing_parameter(name, self):
continue
if name not in params_dict:
if _should_skip_missing_param(name):
continue
logger.warning_once(
"Skipping unknown checkpoint weight: %s",
name,
)
continue
param = params_dict[name]
weight_loader = getattr(
param, "weight_loader", default_weight_loader
)
if stacked_shard_id is None:
weight_loader(param, loaded_weight)
else:
weight_loader(param, loaded_weight, stacked_shard_id)
loaded_params.add(name)
return loaded_params
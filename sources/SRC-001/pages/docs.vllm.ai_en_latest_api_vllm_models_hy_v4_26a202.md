source: https://docs.vllm.ai/en/latest/api/vllm/models/hy_v4/
lastmod: 2026-09-24

class HYV4MTP(nn.Module):
"""HY V4 MTP draft head.
Not a pipeline-parallel stage: the draft head always runs on a single rank,
matching `DeepseekV32MTP` / `KimiK3MTP` / `HYV3MTP`.
"""
packed_modules_mapping = {
"gate_up_proj": ["gate_proj", "up_proj"],
# MLA runs both latent down-projections as one GEMM.
"fused_qkv_a_proj": ["q_a_proj", "kv_a_proj_with_mqa"],
# The indexer fuses wk and weights_proj into one GEMM.
"wk_weights_proj": ["wk", "weights_proj"],
}
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
self.config = vllm_config.model_config.hf_config
self.model = HYV4MultiTokenPredictor(
vllm_config=vllm_config, prefix=maybe_prefix(prefix, "model")
)
self.quant_config = self.model.quant_config
self.sampler = Sampler()
def set_topk_indices_buffer(self, topk_indices_buffer: torch.Tensor) -> None:
"""Share the target sparse-index buffer with every draft consumer.
Proposers that walk ``named_modules()`` instead of calling this reach
the same consumers via ``HYV4MLAAttention.topk_indices_buffer``.
"""
self.model.topk_indices_buffer = topk_indices_buffer
for layer in self.model.layers.values():
self_attn = layer.mtp_block.self_attn
if not self_attn.is_sparse:
continue
indexer = self_attn.indexer
assert indexer is not None, "Sparse HYV4 MTP attention requires an indexer"
indexer.topk_indices_buffer = topk_indices_buffer
indexer.indexer_op.topk_indices_buffer = topk_indices_buffer
attn_impl = self_attn.mla_attn.impl
assert hasattr(attn_impl, "topk_indices_buffer"), (
"Sparse HYV4 MTP attention backend requires a top-k indices buffer"
)
attn_impl.topk_indices_buffer = topk_indices_buffer
def forward(
self,
input_ids: torch.Tensor,
positions: torch.Tensor,
hidden_states: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
spec_step_idx: int = 0,
) -> torch.Tensor:
del intermediate_tensors # the MTP head is single-stage
if (
self.model.requires_topk_indices_buffer
and self.model.topk_indices_buffer is None
):
raise RuntimeError(
"HYV4 sparse MTP requires the target model's top-k indices buffer. "
"The proposer must call HYV4MTP.set_topk_indices_buffer() before "
"the first draft forward."
)
self.model.spec_step_idx = spec_step_idx
return self.model(input_ids, positions, hidden_states, inputs_embeds)
def compute_logits(
self,
hidden_states: torch.Tensor,
spec_step_idx: int = 0,
) -> torch.Tensor | None:
self.model.spec_step_idx = spec_step_idx
return self.model.compute_logits(hidden_states)
def sample(
self,
logits: torch.Tensor,
sampling_metadata: SamplingMetadata,
) -> SamplerOutput | None:
return self.sampler(logits, sampling_metadata)
def _rewrite_spec_layer_name(self, spec_layer: int, name: str) -> str:
if f"model.layers.{spec_layer}.embed_tokens" in name:
return "__skip__"
if f"model.layers.{spec_layer}.shared_head" in name:
return "__skip__"
spec_layer_weight_names = ["enorm", "hnorm", "eh_proj", "final_layernorm"]
spec_layer_weight = any(
weight_name in name for weight_name in spec_layer_weight_names
)
if not spec_layer_weight:
name = name.replace(
f"model.layers.{spec_layer}.",
f"model.layers.{spec_layer}.mtp_block.",
)
return name
def _load_fused_expert_weights(
self,
name: str,
params_dict: dict,
loaded_weight: torch.Tensor,
shard_id: str,
num_experts: int,
) -> bool:
if name not in params_dict:
return False
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
def _load_expert_weight(
self,
name: str,
loaded_weight: torch.Tensor,
params_dict: dict,
loaded_params: set[str],
split_expert_params_mapping: list[tuple[str, str, int, str]],
fused_expert_param_names: dict[tuple[str, str], str],
num_experts: int,
) -> bool:
"""Load one routed-expert weight in either checkpoint layout.
Args:
name: Weight name already rewritten to draft-module naming.
loaded_weight: The checkpoint tensor.
params_dict: The draft model's named parameters.
loaded_params: Set updated with the parameters that received a value.
split_expert_params_mapping: Mapping for the per-expert layout.
fused_expert_param_names: ``(mlp_prefix, tag) -> param name`` for the
all-experts-packed layout.
num_experts: Total number of routed experts.
Returns:
True when the weight was consumed (even if this rank holds none of
the addressed experts).
"""
base = name.split(".experts.")[0]
for ckpt_proj, tag in (
(".experts.gate_up_proj", "w13_weight"),
(".experts.down_proj", "w2_weight"),
):
if ckpt_proj not in name:
continue
param_base = fused_expert_param_names.get((base, tag))
if param_base is None:
return False
# Keep the checkpoint suffix (e.g. `_scale_inv`) so block-scale
# tensors land in the scale parameter, not in the weight.
target = _resolve_fused_expert_param(
param_base, name.split(ckpt_proj, 1)[1], params_dict
)
if target is None:
return False
if tag == "w13_weight":
chunks = loaded_weight.chunk(2, dim=-2)
loaded_w1 = self._load_fused_expert_weights(
target, params_dict, chunks[0], "w1", num_experts
)
loaded_w3 = self._load_fused_expert_weights(
target, params_dict, chunks[1], "w3", num_experts
)
loaded = loaded_w1 and loaded_w3
else:
loaded = self._load_fused_expert_weights(
target, params_dict, loaded_weight, "w2", num_experts
)
if loaded:
loaded_params.add(target)
# The weight belongs to the experts either way; never fall through.
return True
consumed = False
for param_name, weight_name, expert_id, shard_id in split_expert_params_mapping:
if weight_name not in name:
continue
consumed = True
name_mapped = name.replace(weight_name, param_name)
if name_mapped not in params_dict:
continue
param = params_dict[name_mapped]
weight_loader = typing.cast(Callable[..., bool], param.weight_loader)
if weight_loader(
param,
loaded_weight,
name_mapped,
shard_id=shard_id,
expert_id=expert_id,
return_success=True,
):
loaded_params.add(name_mapped)
return consumed
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
params_dict = dict(self.named_parameters())
pp_missing_layer_names = get_pp_missing_layer_names(self)
loaded_params: set[str] = set()
mtp_start = self.config.num_hidden_layers
shared_weights = {
"model.embed_tokens.weight": "model.embed_tokens.weight",
"lm_head.weight": f"model.layers.{mtp_start}.shared_head.head.weight",
}
num_experts = getattr(self.config, "n_routed_experts", 0)
sink_tp_size = get_tensor_model_parallel_world_size()
sink_tp_rank = get_tensor_model_parallel_rank()
n_local_head = self.config.num_attention_heads // sink_tp_size
head_rank_start = n_local_head * sink_tp_rank
head_rank_end = n_local_head * (sink_tp_rank + 1)
# Routed-expert weights come in two checkpoint layouts:
# split: mlp.experts.<id>.gate_proj.weight
# fused: mlp.experts.gate_up_proj (all experts in one tensor)
# The split layout is resolved through the shared EPLB helper so the
# target param names stay in sync with the RoutedExperts module layout;
# the fused layout is resolved from the live parameter names.
split_expert_params_mapping = fused_moe_make_expert_params_mapping(
self,
ckpt_gate_proj_name="gate_proj",
ckpt_down_proj_name="down_proj",
ckpt_up_proj_name="up_proj",
num_experts=num_experts,
)
fused_expert_param_names: dict[tuple[str, str], str] = {}
for param_name in params_dict:
for tag in ("w13_weight", "w2_weight"):
if param_name.endswith(tag) and ".experts." in param_name:
base = param_name.split(".experts.")[0]
fused_expert_param_names[base, tag] = param_name
stacked_mapping = [
(".gate_up_proj", ".gate_proj", 0),
(".gate_up_proj", ".up_proj", 1),
# MLA runs both latent down-projections as one GEMM.
(".fused_qkv_a_proj", ".q_a_proj", 0),
(".fused_qkv_a_proj", ".kv_a_proj_with_mqa", 1),
]
# Sparse DSA draft blocks build an Indexer whose wk / weights_proj are
# fused into a single MergedColumnParallelLinear (wk_weights_proj).
indexer_stacked_mapping = [
(".wk_weights_proj", ".wk", 0),
(".wk_weights_proj", ".weights_proj", 1),
]
# FP8 indexer wk dequant buffer (weight and scale arrive separately).
pending_wk_fp8: dict[str, dict[str, torch.Tensor]] = {}
for name, loaded_weight in weights:
if name in shared_weights:
target_name = shared_weights[name]
if target_name in params_dict:
param = params_dict[target_name]
weight_loader = getattr(
param, "weight_loader", default_weight_loader
)
weight_loader(param, loaded_weight)
loaded_params.add(target_name)
continue
spec_layer = None
if name.startswith("model.mtp_layers."):
parts = name.split(".")
if len(parts) > 3 and parts[2].isdigit():
spec_layer = mtp_start + int(parts[2])
name = name.replace(
f"model.mtp_layers.{parts[2]}.",
f"model.layers.{spec_layer}.",
)
else:
spec_layer = _get_spec_layer_idx_from_weight_name(self.config, name)
if spec_layer is None:
continue
name = self._rewrite_spec_layer_name(spec_layer, name)
if name == "__skip__":
continue
name, loaded_weight = _prepare_mtp_fp8_expert_scale(
self.quant_config, name, loaded_weight
)
if "mlp.gate.e_score_correction_bias" in name:
name = name.replace("gate.e_score_correction_bias", "expert_bias")
is_loaded = False
for param_name, weight_name, shard_id in stacked_mapping:
if weight_name not in name or ".experts." in name:
continue
name_mapped = name.replace(weight_name, param_name)
if name_mapped not in params_dict:
if is_pp_missing_parameter(name_mapped, self):
is_loaded = True
break
param = params_dict[name_mapped]
param.weight_loader(param, loaded_weight, shard_id)
loaded_params.add(name_mapped)
is_loaded = True
break
if is_loaded:
continue
# FP8 indexer wk: dequantize to BF16 and load into the fused
# wk_weights_proj. PP-aware (skips layers not held by this rank).
if _try_load_fp8_indexer_wk(
name,
loaded_weight,
pending_wk_fp8,
params_dict,
loaded_params,
pp_missing_layer_names,
):
continue
# BF16 indexer wk / weights_proj: merge into the fused param.
is_loaded = False
for param_name, weight_name, shard_id in indexer_stacked_mapping:
if weight_name not in name or "wk_weights" in name:
continue
name_mapped = name.replace(weight_name, param_name)
if name_mapped not in params_dict:
if is_pp_missing_parameter(name_mapped, self):
is_loaded = True
break
param = params_dict[name_mapped]
param.weight_loader(param, loaded_weight, shard_id)
loaded_params.add(name_mapped)
is_loaded = True
break
if is_loaded:
continue
is_loaded = False
if ".experts." in name:
is_loaded = self._load_expert_weight(
name,
loaded_weight,
params_dict,
loaded_params,
split_expert_params_mapping,
fused_expert_param_names,
num_experts,
)
if is_loaded:
continue
if "learnable_sink_param" in name:
if name in params_dict:
narrow_weight = loaded_weight[head_rank_start:head_rank_end]
n = narrow_weight.shape[0]
with torch.no_grad():
params_dict[name][:n].copy_(narrow_weight)
loaded_params.add(name)
continue
remapped_name = maybe_remap_kv_scale_name(name, params_dict)
if remapped_name is None:
continue
name = remapped_name
if name not in params_dict:
if is_pp_missing_parameter(name, self):
continue
if _should_skip_missing_mtp_scale_param(self.quant_config, name):
continue
logger.warning_once("Skipping unknown MTP weight: %s", name)
continue
param = params_dict[name]
weight_loader = getattr(param, "weight_loader", default_weight_loader)
weight_loader(param, loaded_weight)
loaded_params.add(name)
logger.info_once("HYV4 MTP draft model loaded: %d params", len(loaded_params))
unassigned_all = sorted(set(params_dict) - loaded_params)
# KVCacheScaleParameter (``k_scale`` / ``v_scale`` / ``q_scale`` /
# ``prob_scale``) is created by ``BaseKVCacheMethod.create_weights`` for
# every Attention layer that runs on an fp8-family quant method, and
# its -1.0 sentinel is replaced by the runtime default (1.0) in
# ``process_weights_after_loading`` -- which runs *after* this method.
# HY V4 checkpoints intentionally omit these (``kv_cache_quant_algo:
# null``); silence them only when the parameter is actually the
# sentinel type so a genuine mismatch on a same-named tensor still
# reaches the warning.
from vllm.model_executor.layers.quantization.kv_cache import (
KVCacheScaleParameter,
)
unassigned = [
name
for name in unassigned_all
if not isinstance(params_dict.get(name), KVCacheScaleParameter)
]
if unassigned:
# A draft parameter with no checkpoint source keeps its sentinel
# init value (FP8 scales start at finfo(float32).min), which
# silently destroys draft quality instead of failing the load.
logger.warning(
"HYV4 MTP draft model: %d parameters received no checkpoint value: %s",
len(unassigned),
", ".join(unassigned),
)
return loaded_params
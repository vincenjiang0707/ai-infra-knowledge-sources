source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/xpu/dspark/
lastmod: 2026-09-24

class DSparkDeepseekV4ForCausalLM(nn.Module):
"""XPU DSpark draft model entry point for DeepSeek-V4."""
has_own_embed_tokens = False
has_own_lm_head = False
def __init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
super().__init__()
assert vllm_config.speculative_config is not None
self.draft_model_config = vllm_config.speculative_config.draft_model_config
self.config = self.draft_model_config.hf_config
self.model = DSparkDeepseekV4Model(
vllm_config=vllm_config, prefix=maybe_prefix(prefix, "model")
)
# Shared with the target (aliased by the speculator's load utility).
self.lm_head = ParallelLMHead(
self.config.vocab_size,
self.config.hidden_size,
prefix=maybe_prefix(prefix, "lm_head"),
)
self.logits_processor = LogitsProcessor(self.config.vocab_size)
# --- Hooks used by the speculator ---
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.model.embed_input_ids(input_ids)
def combine_hidden_states(self, aux_hidden_states: torch.Tensor) -> torch.Tensor:
return self.model.combine_hidden_states(aux_hidden_states)
def get_draft_kv_cache_layer_names(self) -> list[str]:
return [layer.attn.swa_cache_layer.prefix for layer in self.model.layers]
def precompute_and_store_context_kv(
self,
context_states: torch.Tensor,
context_positions: torch.Tensor,
context_slot_mappings: list[torch.Tensor | None] | None = None,
) -> None:
self.model.precompute_and_store_context_kv(
context_states, context_positions, context_slot_mappings
)
def forward(
self,
input_ids: torch.Tensor,
positions: torch.Tensor,
inputs_embeds: torch.Tensor | None = None,
) -> torch.Tensor:
return self.model(input_ids, positions, inputs_embeds)
def compute_logits(self, hidden_states: torch.Tensor) -> torch.Tensor:
"""Base logits U_k = lm_head(norm(head_hidden))."""
return self.logits_processor(self.lm_head, self.model.norm(hidden_states))
def compute_draft_logits(self, hidden_states: torch.Tensor) -> torch.Tensor:
return self.compute_logits(hidden_states)
def map_draft_to_target(self, draft_ids: torch.Tensor) -> torch.Tensor:
return draft_ids # full-vocab: draft ids are target ids
def markov_embed(self, token_ids: torch.Tensor) -> torch.Tensor:
return self.model.markov_head.embed(token_ids)
def markov_bias(self, markov_embed: torch.Tensor) -> torch.Tensor:
return self.model.markov_head.bias(markov_embed, self.logits_processor)
# --- Weight loading ---
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
"""Load ``mtp.{0,1,2}.*`` draft weights from the target checkpoint."""
first_layer = self.model.layers[0]
use_mega_moe = first_layer.ffn.use_mega_moe
if use_mega_moe:
expert_mapping = make_deepseek_v4_expert_params_mapping(
self.config.n_routed_experts
)
else:
expert_mapping = fused_moe_make_expert_params_mapping(
self,
ckpt_gate_proj_name="w1",
ckpt_down_proj_name="w2",
ckpt_up_proj_name="w3",
num_experts=self.config.n_routed_experts,
)
expert_scale_suffix = (
".weight_scale"
if getattr(self.config, "expert_dtype", "fp4") == "fp4"
else ".weight_scale_inv"
)
stacked_params_mapping = [
("gate_up_proj", "w1", 0),
("gate_up_proj", "w3", 1),
("attn.fused_wqa_wkv", "attn.wq_a", 0),
("attn.fused_wqa_wkv", "attn.wkv", 1),
]
params_dict = dict(self.named_parameters())
loaded_params: set[str] = set()
tp_size = get_tensor_model_parallel_world_size()
tp_rank = get_tensor_model_parallel_rank()
n_local_head = self.config.num_attention_heads // tp_size
head_start = n_local_head * tp_rank
head_end = n_local_head * (tp_rank + 1)
for name, loaded_weight in weights:
mapped = self._remap_dspark_name(name)
if mapped is None:
continue
name = mapped
# .scale -> per-method scale suffix
if name.endswith(".scale"):
suffix = (
expert_scale_suffix
if _EXPERT_SCALE_RE.search(name)
else ".weight_scale_inv"
)
name = name.removesuffix(".scale") + suffix
# Expert weights
if ".experts." in name:
if (
"weight_scale" in name
and loaded_weight.dtype == torch.float8_e8m0fnu
):
loaded_weight = loaded_weight.view(torch.uint8)
for param_name, weight_name, expert_id, shard_id in expert_mapping:
if weight_name not in name:
continue
name_mapped = name.replace(weight_name, param_name)
if name_mapped not in params_dict:
continue
param = params_dict[name_mapped]
success = param.weight_loader(
param,
loaded_weight,
name_mapped,
shard_id=shard_id,
expert_id=expert_id,
return_success=True,
)
if success:
loaded_params.add(name_mapped)
break
continue
# Stacked params (decoder-layer only)
is_layer_param = name.startswith("model.layers.")
for param_name, weight_name, stacked_shard_id in stacked_params_mapping:
if not is_layer_param or weight_name not in name:
continue
name = name.replace(weight_name, param_name)
if name not in params_dict:
break
param = params_dict[name]
param.weight_loader(param, loaded_weight, stacked_shard_id)
loaded_params.add(name)
break
else:
if "attn_sink" in name:
if name not in params_dict:
continue
narrow = loaded_weight[head_start:head_end]
params_dict[name][: narrow.shape[0]].copy_(narrow)
loaded_params.add(name)
continue
if ".shared_experts.w2" in name:
name = name.replace(
".shared_experts.w2", ".shared_experts.down_proj"
)
if name.endswith(".ffn.gate.bias"):
name = name.replace(
".ffn.gate.bias", ".ffn.gate.e_score_correction_bias"
)
if name not in params_dict:
continue
param = params_dict[name]
weight_loader = getattr(param, "weight_loader", default_weight_loader)
weight_loader(param, loaded_weight)
loaded_params.add(name)
self._finalize_moe()
logger.info_once("DSpark XPU draft model loaded: %d params", len(loaded_params))
return loaded_params
def _finalize_moe(self) -> None:
for layer in self.model.layers:
layer.ffn.finalize_mega_moe_weights()
def _remap_dspark_name(self, name: str) -> str | None:
"""Map checkpoint ``mtp.{i}.*`` name to this model's parameter path."""
m = re.match(r"mtp\.(\d+)\.(.*)", name)
if m is None:
return None
stage = int(m.group(1))
rest = m.group(2)
if rest.startswith("confidence_head."):
return None
head_prefixes = (
"norm.",
"hc_head_fn",
"hc_head_base",
"hc_head_scale",
"markov_head.",
)
if rest.startswith(("main_proj.", "main_norm.")) or rest.startswith(
head_prefixes
):
return f"model.{rest}"
return f"model.layers.{stage}.{rest}"
source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/nvidia/dspark/
lastmod: 2026-09-24

class DSparkDeepseekV4ForCausalLM(nn.Module):
# Draft weights ship in the target checkpoint (mtp.*) without embed/head, so
# load_dspark_model always aliases the target's.
has_own_embed_tokens = False
has_own_lm_head = False
# Full-vocab draft: draft ids are target ids, no remapping needed.
draft_id_to_target_id = None
def __init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
super().__init__()
assert vllm_config.speculative_config is not None
self.draft_model_config = vllm_config.speculative_config.draft_model_config
self.config = self.draft_model_config.hf_config
self.quant_config = vllm_config.quant_config
self.linear_scale_name = _linear_scale_param_name(
vllm_config, getattr(self.config, "expert_dtype", "fp4")
)
self.pad_shared_expert = getattr(
self.quant_config, "weight_block_size", None
) is not None and not _use_sequence_parallel(vllm_config)
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
# --- Hooks used by the speculator -------------------------------------
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.model.embed_input_ids(input_ids)
def combine_hidden_states(self, aux_hidden_states: torch.Tensor) -> torch.Tensor:
return self.model.combine_hidden_states(aux_hidden_states)
def get_draft_kv_cache_layer_names(self) -> list[str]:
# DSV4 MLA path: each draft layer's sliding-window cache is a separate
# layer, named by its prefix.
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
# Returns the pre-norm collapsed head hidden ([T, hidden_size]).
return self.model(input_ids, positions, inputs_embeds)
def compute_logits(self, hidden_states: torch.Tensor) -> torch.Tensor:
"""Base logits U_k = lm_head(norm(head_hidden))."""
return self.logits_processor(self.lm_head, self.model.norm(hidden_states))
def compute_draft_logits(self, hidden_states: torch.Tensor) -> torch.Tensor:
# Full-vocab draft: base logits, no d2t scatter.
return self.compute_logits(hidden_states)
def map_draft_to_target(self, draft_ids: torch.Tensor) -> torch.Tensor:
return draft_ids # full-vocab: draft ids are target ids
def markov_embed(self, token_ids: torch.Tensor) -> torch.Tensor:
return self.model.markov_head.embed(token_ids)
def markov_bias(self, markov_embed: torch.Tensor) -> torch.Tensor:
return self.model.markov_head.bias(markov_embed, self.logits_processor)
def compute_confidence(
self, head_hidden: torch.Tensor, markov_embed: torch.Tensor
) -> torch.Tensor:
"""Per-position acceptance probability for each drafted token."""
assert self.model.confidence_head is not None
return torch.sigmoid(self.model.confidence_head(head_hidden, markov_embed))
# --- Weight loading ----------------------------------------------------
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
"""Load the ``mtp.{0,1,2}.*`` draft weights from the target checkpoint.
Non-mtp weights (embed/head/main layers) belong to the target model and
are skipped here. ``embed_tokens``/``lm_head`` are aliased from the target.
"""
first_layer = self.model.layers[0]
use_mega_moe = first_layer.ffn.use_mega_moe
# Draft MoE layers use the dspark_* expert counts, not the
# backbone's (see DeepseekV4MoE and the reference
# ModelArgs.get_moe_config).
n_draft_experts = (
getattr(self.config, "dspark_n_routed_experts", 0)
or self.config.n_routed_experts
)
if use_mega_moe:
expert_mapping = make_deepseek_v4_expert_params_mapping(n_draft_experts)
else:
expert_mapping = fused_moe_make_expert_params_mapping(
self,
ckpt_gate_proj_name="w1",
ckpt_down_proj_name="w2",
ckpt_up_proj_name="w3",
num_experts=n_draft_experts,
)
expert_scale_suffix = (
".weight_scale"
if getattr(self.config, "expert_dtype", "fp4") == "fp4"
else ".weight_scale_inv"
)
# (param_name, ckpt_shard_name, shard_id) for non-expert stacked params.
stacked_params_mapping = [
("gate_up_proj", "w1", 0),
("gate_up_proj", "w3", 1),
("attn.fused_wqa_wkv", "attn.wq_a", 0),
("attn.fused_wqa_wkv", "attn.wkv", 1),
]
params_dict = dict(self.named_parameters())
loaded_params: set[str] = set()
loaded_confidence_head = False
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
if "confidence_head." in name:
loaded_confidence_head = True
# ``.scale`` -> per-method scale suffix.
if name.endswith(".scale"):
suffix = (
expert_scale_suffix
if _EXPERT_SCALE_RE.search(name)
else f".{self.linear_scale_name}"
)
name = name.removesuffix(".scale") + suffix
if ".shared_experts.w2" in name:
name = name.replace(".shared_experts.w2", ".shared_experts.down_proj")
if self.pad_shared_expert and ".shared_experts." in name:
loaded_weight = DeepseekV4Model._pad_shared_expert_weight(
self.quant_config, name, loaded_weight
)
# E8M0 expert scales: keep raw exponent bytes.
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
# Stacked rules only apply to decoder-layer weights. Head-stack params
# (main_proj/norm/markov_head/confidence_head) load directly —
# otherwise e.g. "markov_w1" would collide with the "w1" shard rule.
is_layer_param = name.startswith("model.layers.")
for param_name, weight_name, stacked_shard_id in stacked_params_mapping:
if not is_layer_param or weight_name not in name:
continue
name = name.replace(weight_name, param_name)
param = params_dict[name]
param.weight_loader(param, loaded_weight, stacked_shard_id)
loaded_params.add(name)
break
else:
if "attn_sink" in name:
narrow = loaded_weight[head_start:head_end]
params_dict[name][: narrow.shape[0]].copy_(narrow)
loaded_params.add(name)
continue
if name.endswith(".ffn.gate.bias"):
name = name.replace(
".ffn.gate.bias", ".ffn.gate.e_score_correction_bias"
)
param = params_dict[name]
weight_loader = getattr(param, "weight_loader", default_weight_loader)
weight_loader(param, loaded_weight)
loaded_params.add(name)
if self.model.confidence_head is not None and not loaded_confidence_head:
self.model.confidence_head = None
self.process_weights_after_loading()
logger.info_once("DSpark draft model loaded: %d params", len(loaded_params))
return loaded_params
def _finalize_moe(self) -> None:
for layer in self.model.layers:
layer.ffn.finalize_mega_moe_weights()
def _finalize_attn(self) -> None:
"""Run the attention backend's post-load weight step on the draft layers.
They are ordinary DeepseekV4DecoderLayers, so they take the engine-wide
attention backend and owe it whatever the target model owes it -- mega
attention permutes wq_b / wo_a here and refuses to run without it.
Idempotent, like the target's.
"""
for layer in self.model.layers:
finalize = getattr(layer.attn, "finalize_loaded_weights", None)
if finalize is not None:
finalize()
def process_weights_after_loading(self) -> None:
self._finalize_moe()
self._finalize_attn()
def _remap_dspark_name(self, name: str) -> str | None:
"""Map a checkpoint ``mtp.{i}.*`` name to this model's parameter path.
Returns None for non-mtp weights (owned by the target model).
"""
m = re.match(r"mtp\.(\d+)\.(.*)", name)
if m is None:
return None
stage = int(m.group(1))
rest = m.group(2)
if rest.startswith("confidence_head.") and self.model.confidence_head is None:
return None
# The checkpoint calls the Markov head's factors ``embed``/``head``;
# DSparkMarkovHead registers them as ``markov_w1``/``markov_w2``.
if rest.startswith("markov_head.embed."):
return "model.markov_head.markov_w1." + rest.removeprefix(
"markov_head.embed."
)
if rest.startswith("markov_head.head."):
return "model.markov_head.markov_w2." + rest.removeprefix(
"markov_head.head."
)
# Head-stack params live at model level (mtp.last), context combiner at
# model level (mtp.0); everything else is a per-layer decoder block.
head_prefixes = (
"norm.",
"markov_head.",
"confidence_head.",
)
if rest.startswith(("main_proj.", "main_norm.")) or rest.startswith(
head_prefixes
):
return f"model.{rest}"
return f"model.layers.{stage}.{rest}"
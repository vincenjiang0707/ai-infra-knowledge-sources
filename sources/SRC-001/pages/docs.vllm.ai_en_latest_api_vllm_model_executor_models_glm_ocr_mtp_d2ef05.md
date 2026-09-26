source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/glm_ocr_mtp/
lastmod: 2026-09-24

class GlmOcrMTP(nn.Module, SupportsPP):
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
self.config = vllm_config.model_config.hf_config.text_config
quant_config = vllm_config.quant_config
self.quant_config = quant_config
self.model = GlmOcrMultiTokenPredictor(
vllm_config=vllm_config, prefix=maybe_prefix(prefix, "model")
)
self.num_layers = self.config.num_nextn_predict_layers
for layer in self.model.layers.values():
assert isinstance(layer, GlmOcrMultiTokenPredictorLayer)
layer = layer.mtp_block
assert isinstance(layer, Glm4DecoderLayer)
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.model.embed_input_ids(input_ids)
def forward( # type: ignore[override]
self,
input_ids: torch.Tensor,
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
if self.quant_config is not None and (
cache_scale_mapper := self.quant_config.get_cache_scale_mapper()
):
weights = cache_scale_mapper.apply(weights)
stacked_params_mapping = [
# (param_name, shard_name, shard_id)
(".qkv_proj", ".q_proj", "q"),
(".qkv_proj", ".k_proj", "k"),
(".qkv_proj", ".v_proj", "v"),
(".gate_up_proj", ".gate_proj", 0),
(".gate_up_proj", ".up_proj", 1),
]
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
if "scale" in name or "zero_point" in name:
# Remapping the name of FP8 kv-scale or zero point.
remapped_name = maybe_remap_kv_scale_name(name, params_dict)
if remapped_name is None:
continue
name = remapped_name
for param_name, weight_name, shard_id in stacked_params_mapping:
if weight_name not in name:
continue
name = name.replace(weight_name, param_name)
# Skip loading extra bias for GPTQ models.
if name.endswith(".bias") and name not in params_dict:
continue
if is_pp_missing_parameter(name, self):
continue
param = params_dict[name]
weight_loader = param.weight_loader
weight_loader(param, loaded_weight, shard_id)
break
else:
# Skip loading extra bias for GPTQ models.
if name.endswith(".bias") and name not in params_dict:
continue
# Some checkpoints include weight scale tensors for the
# LM head even when the quantized head isn't built. Skip
# them if the model does not expose a matching parameter
# to avoid KeyError during load.
if name.endswith(".weight_scale") and name not in params_dict:
continue
# According to DeepSeek-V3 Technical Report, MTP modules
# shares embedding layer. We only load the first weights.
if (
spec_layer != self.model.mtp_start_layer_idx
and ".layers" not in name
):
continue
if is_pp_missing_parameter(name, self):
continue
param = params_dict[name]
weight_loader = getattr(param, "weight_loader", default_weight_loader)
weight_loader(param, loaded_weight)
loaded_params.add(name)
return loaded_params
def _rewrite_spec_layer_name(self, spec_layer: int, name: str) -> str:
"""Rewrite the weight name to match the format of the original model.
Add .mtp_block for modules in transformer layer block for spec layer
and rename shared layer weights to be top level.
"""
name = name.replace("model.language_model.layers", "model.layers")
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
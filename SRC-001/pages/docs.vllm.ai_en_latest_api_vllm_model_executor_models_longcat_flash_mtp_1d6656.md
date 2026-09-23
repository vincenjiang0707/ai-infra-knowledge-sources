source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/longcat_flash_mtp/
lastmod: 2026-09-23

class LongCatFlashMTP(nn.Module):
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
# LongCat MTP has no MoE layers: clear n_routed_experts so the predictor
# builds a dense MLP. object.__setattr__ bypasses the ngram remote
# config's strict validation (it rejects setting the int field to None).
object.__setattr__(vllm_config.model_config.hf_config, "n_routed_experts", None)
self.config = FlashConfig(**vllm_config.model_config.hf_config.__dict__)
self.quant_config = (
None
if "mtp" in getattr(self.config, "disable_quant_module", [])
else vllm_config.quant_config
)
self.model = LongCatMultiTokenPredictor(
vllm_config=vllm_config,
quant_config=self.quant_config,
prefix=maybe_prefix(prefix, "model"),
)
self.lm_head = ParallelLMHead(
self.config.vocab_size,
self.config.hidden_size,
quant_config=self.quant_config,
prefix=maybe_prefix(prefix, "lm_head"),
)
self.logits_processor = LogitsProcessor(self.config.vocab_size)
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
logits = self.logits_processor(self.lm_head, hidden_states)
return logits
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
stacked_params_mapping = [
("gate_up_proj", "gate_proj", 0),
("gate_up_proj", "up_proj", 1),
("fused_qkv_a_proj", "q_a_proj", 0),
("fused_qkv_a_proj", "kv_a_proj_with_mqa", 1),
]
new_to_old_names_mapping = {
"model.mtp.embed_tokens.weight": "model.layers.0.embed_tokens.weight",
"model.mtp.layers.0.eh_proj.weight": "eh_proj.weight",
"model.mtp.layers.0.eh_proj.weight_scale_inv": "eh_proj.weight_scale_inv",
"model.mtp.layers.0.enorm.m.weight": "enorm.weight",
"model.mtp.layers.0.hnorm.m.weight": "hnorm.weight",
"model.mtp.layers.0.input_layernorm.weight": "model.layers.0.input_layernorm.weight", # noqa: E501
"model.mtp.layers.0.post_attention_layernorm.weight": "model.layers.0.post_attention_layernorm.weight", # noqa: E501
"model.mtp.layers.0.self_attn.kv_a_layernorm.weight": "model.layers.0.self_attn.kv_a_layernorm.weight", # noqa: E501
"model.mtp.layers.0.self_attn.kv_a_proj_with_mqa.weight": "model.layers.0.self_attn.kv_a_proj_with_mqa.weight", # noqa: E501
"model.mtp.layers.0.self_attn.kv_a_proj_with_mqa.weight_scale_inv": "model.layers.0.self_attn.kv_a_proj_with_mqa.weight_scale_inv", # noqa: E501
"model.mtp.layers.0.self_attn.kv_b_proj.weight": "model.layers.0.self_attn.kv_b_proj.weight", # noqa: E501
"model.mtp.layers.0.self_attn.kv_b_proj.weight_scale_inv": "model.layers.0.self_attn.kv_b_proj.weight_scale_inv", # noqa: E501
"model.mtp.layers.0.self_attn.o_proj.weight": "model.layers.0.self_attn.o_proj.weight", # noqa: E501
"model.mtp.layers.0.self_attn.o_proj.weight_scale_inv": "model.layers.0.self_attn.o_proj.weight_scale_inv", # noqa: E501
"model.mtp.layers.0.self_attn.q_a_layernorm.weight": "model.layers.0.self_attn.q_a_layernorm.weight", # noqa: E501
"model.mtp.layers.0.self_attn.q_a_proj.weight": "model.layers.0.self_attn.q_a_proj.weight", # noqa: E501
"model.mtp.layers.0.self_attn.q_a_proj.weight_scale_inv": "model.layers.0.self_attn.q_a_proj.weight_scale_inv", # noqa: E501
"model.mtp.layers.0.self_attn.q_b_proj.weight": "model.layers.0.self_attn.q_b_proj.weight", # noqa: E501
"model.mtp.layers.0.self_attn.q_b_proj.weight_scale_inv": "model.layers.0.self_attn.q_b_proj.weight_scale_inv", # noqa: E501
"model.mtp.layers.0.transformer_layer.mlp.down_proj.weight": "model.layers.0.mlp.down_proj.weight", # noqa: E501
"model.mtp.layers.0.transformer_layer.mlp.down_proj.weight_scale_inv": "model.layers.0.mlp.down_proj.weight_scale_inv", # noqa: E501
"model.mtp.layers.0.transformer_layer.mlp.gate_proj.weight": "model.layers.0.mlp.gate_proj.weight", # noqa: E501
"model.mtp.layers.0.transformer_layer.mlp.gate_proj.weight_scale_inv": "model.layers.0.mlp.gate_proj.weight_scale_inv", # noqa: E501
"model.mtp.layers.0.transformer_layer.mlp.up_proj.weight": "model.layers.0.mlp.up_proj.weight", # noqa: E501
"model.mtp.layers.0.transformer_layer.mlp.up_proj.weight_scale_inv": "model.layers.0.mlp.up_proj.weight_scale_inv", # noqa: E501
"model.mtp.norm.weight": "final_layernorm.weight",
}
params_dict = dict(self.named_parameters())
loaded_params: set[str] = set()
for name, loaded_weight in weights:
if "rotary_emb.inv_freq" in name:
continue
spec_layer = self.get_spec_layer_idx_from_weight_name(self.config, name)
if spec_layer is None:
continue
name = self._rewrite_spec_layer_name(
spec_layer, name, new_to_old_names_mapping
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
name = name.replace(weight_name, param_name)
# QKV fusion is optional, fall back to normal
# weight loading if it's not enabled
if (param_name == "fused_qkv_a_proj") and name not in params_dict:
continue
# Skip loading extra bias for GPTQ models.
if name.endswith(".bias") and name not in params_dict:
continue
param = params_dict[name]
weight_loader = param.weight_loader
weight_loader(param, loaded_weight, shard_id)
break
else:
# Skip loading extra bias for GPTQ models.
if name.endswith(".bias") and name not in params_dict:
continue
# According to DeepSeek-V3 Technical Report, MTP modules
# shares embedding layer. We only load the first weights.
if (
spec_layer != self.model.mtp_start_layer_idx
and ".layers" not in name
):
continue
param = params_dict[name]
weight_loader = getattr(param, "weight_loader", default_weight_loader)
weight_loader(param, loaded_weight)
loaded_params.add(name)
spec_layer_id = self.config.num_hidden_layers * 2
self_attn = self.model.layers[str(spec_layer_id)].mtp_block.self_attn
if (
self.quant_config is not None
and hasattr(self.quant_config, "weight_block_size")
and self_attn.kv_b_proj.weight.dtype
in (
torch.float8_e4m3fn,
torch.float8_e4m3fnuz,
)
):
weight_block_size = self.quant_config.weight_block_size
if weight_block_size is not None:
dtype = torch.get_default_dtype()
w = block_dequant(
self_attn.kv_b_proj.weight,
self_attn.kv_b_proj.weight_scale_inv,
weight_block_size,
).to(dtype)
else:
w = self_attn.kv_b_proj.weight
else:
w = self_attn.kv_b_proj.weight
w_kc, w_vc = w.unflatten(
0, (-1, self_attn.qk_nope_head_dim + self_attn.v_head_dim)
).split([self_attn.qk_nope_head_dim, self_attn.v_head_dim], dim=1)
self_attn.w_kc = w_kc.transpose(1, 2).contiguous().transpose(1, 2)
self_attn.w_vc = w_vc.contiguous().transpose(1, 2)
# Guard against compounding on incremental load_weights calls (the
# in-place *= would otherwise double-apply the LoRA scaling).
if self.config.mla_scale_q_lora and not getattr(
self_attn, "_mla_q_lora_scaled", False
):
self_attn.q_a_layernorm.weight.data *= (
self.config.hidden_size / self.config.q_lora_rank
) ** 0.5
self_attn._mla_q_lora_scaled = True
if self.config.mla_scale_kv_lora and not getattr(
self_attn, "_mla_kv_lora_scaled", False
):
self_attn.kv_a_layernorm.weight.data *= (
self.config.hidden_size / self.config.kv_lora_rank
) ** 0.5
self_attn._mla_kv_lora_scaled = True
return loaded_params
def _rewrite_spec_layer_name(
self, spec_layer: int, name: str, new_to_old_names_mapping: dict
) -> str:
"""Rewrite the weight name to match the format of the original model.
Add .mtp_block for modules in transformer layer block for spec layer
and rename shared layer weights to be top level.
"""
if name in new_to_old_names_mapping:
name = new_to_old_names_mapping[name]
spec_layer_weight_names = [
"embed_tokens",
"enorm",
"hnorm",
"eh_proj",
"shared_head",
]
if (
name.startswith("enorm")
or name.startswith("hnorm")
or name.startswith("eh_proj")
or name.startswith("final_layernorm")
):
name = "model.layers." + str(spec_layer) + "." + name
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
"model.layers.0.", f"model.layers.{spec_layer}.mtp_block."
)
elif shared_weight:
# treat shared weights as top level weights
name = name.replace("model.layers.0.", "model.")
return name
def get_spec_layer_idx_from_weight_name(
self, config: PretrainedConfig, weight_name: str
) -> int | None:
if "model.mtp" in weight_name:
return config.num_hidden_layers * 2
return None
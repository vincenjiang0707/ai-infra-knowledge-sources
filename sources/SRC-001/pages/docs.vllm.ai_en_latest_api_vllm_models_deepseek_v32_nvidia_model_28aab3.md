source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v32/nvidia/model/
lastmod: 2026-09-23

Bases: `DeepseekV2ForCausalLM`


DSA causal LM — DeepSeek V2/V3 orchestration with the DSA backbone.

Serves DeepSeek V3.2 and any architecture reusing DSA (e.g. GLM-5.2).

## Source code in `vllm/models/deepseek_v32/nvidia/model.py`


| class DeepseekV32ForCausalLM(DeepseekV2ForCausalLM):
"""DSA causal LM — DeepSeek V2/V3 orchestration with the DSA backbone.
Serves DeepSeek V3.2 and any architecture reusing DSA (e.g. GLM-5.2).
"""
model_cls = DeepseekV32Model
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__(vllm_config=vllm_config, prefix=prefix)
if self.config.model_type == "glm_moe_dsa":
enable_glm52_low_latency_gemm(self, vllm_config.model_config.dtype)
def set_moe_parameters(self):
# Same as the base, but keyed on the MoE block type rather than the
# decoder-layer type (DeepseekV32DecoderLayer is a plain nn.Module).
self.num_expert_groups = getattr(self.config, "n_group", 1)
self.moe_layers = []
self.moe_mlp_layers = []
example_moe = None
for layer in self.model.layers:
if isinstance(layer, PPMissingLayer):
continue
if isinstance(layer.mlp, DeepseekV2MoE):
example_moe = layer.mlp
self.moe_mlp_layers.append(layer.mlp)
self.moe_layers.append(layer.mlp.experts)
self.extract_moe_parameters(example_moe)
|
source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/voyage/
lastmod: 2026-09-24

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsLoRA](../interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)


Qwen3Model + Voyage embedding head + bidirectional attention.

Checkpoint conventions (HF): - MLP: gate_proj + up_proj (unfused) - Attn: q_proj + k_proj + v_proj (unfused) - Linear head: linear.weight - Weights prefixed with "model." (e.g., model.layers.0...)

## vLLM Qwen3Model expects

- mlp.gate_up_proj (fused)
- self_attn.qkv_proj (fused)
- No "model." prefix

## Source code in `vllm/model_executor/models/voyage.py`


| class VoyageQwen3BidirectionalEmbedModel(nn.Module, SupportsLoRA):
"""Qwen3Model + Voyage embedding head + bidirectional attention.
Checkpoint conventions (HF):
- MLP: gate_proj + up_proj (unfused)
- Attn: q_proj + k_proj + v_proj (unfused)
- Linear head: linear.weight
- Weights prefixed with "model." (e.g., model.layers.0...)
vLLM Qwen3Model expects:
- mlp.gate_up_proj (fused)
- self_attn.qkv_proj (fused)
- No "model." prefix
"""
packed_modules_mapping = {
"qkv_proj": ["q_proj", "k_proj", "v_proj"],
"gate_up_proj": ["gate_proj", "up_proj"],
}
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
self.config = vllm_config.model_config.hf_config
self.model = Qwen3Model(
vllm_config=vllm_config, prefix=maybe_prefix(prefix, "model")
)
# Embedding head (hidden_size -> num_labels, bias=False)
self.linear = nn.Linear(
self.config.hidden_size,
self.config.num_labels,
bias=False,
)
self.make_empty_intermediate_tensors = (
self.model.make_empty_intermediate_tensors
)
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.model.embed_input_ids(input_ids)
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
) -> torch.Tensor:
out = self.model(input_ids, positions, intermediate_tensors, inputs_embeds)
return self.linear(out)
def load_weights(self, weights: Iterable[WeightItem]) -> set[str]:
loader = AutoWeightsLoader(self)
return loader.load_weights(weights)
|
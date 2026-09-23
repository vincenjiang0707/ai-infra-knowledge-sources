source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/granitemoehybrid/
lastmod: 2026-09-23

class GraniteMoeHybridForCausalLM(
nn.Module,
HasInnerState,
SupportsLoRA,
SupportsPP,
IsHybrid,
SupportsQuant,
SupportsMambaPrefixCaching,
):
packed_modules_mapping: dict[str, list[str]] = {
"qkv_proj": [
"q_proj",
"k_proj",
"v_proj",
],
"conv1d": ["conv1d"],
"in_proj": ["in_proj"],
"input_linear": ["input_linear"],
}
embedding_modules = {
"embed_tokens": "input_embeddings",
"lm_head": "output_embeddings",
}
@classmethod
def get_mamba_state_dtype_from_config(
cls,
vllm_config: "VllmConfig",
) -> tuple[torch.dtype, torch.dtype]:
return MambaStateDtypeCalculator.mamba2_state_dtype(
vllm_config.model_config.dtype,
vllm_config.cache_config.mamba_cache_dtype,
vllm_config.cache_config.mamba_ssm_cache_dtype,
)
@classmethod
def get_mamba_state_shape_from_config(
cls,
vllm_config: "VllmConfig",
) -> tuple[tuple[int, int], tuple[int, int, int]]:
"""Calculate shapes for Mamba's convolutional and state caches.
Args:
vllm_config: vLLM config
Returns:
Tuple containing:
- conv_state_shape: Shape for convolutional state cache
- temporal_state_shape: Shape for state space model cache
"""
parallel_config = vllm_config.parallel_config
hf_config = vllm_config.model_config.hf_config
intermediate_size = hf_config.mamba_expand * hf_config.hidden_size
return MambaStateShapeCalculator.mamba2_state_shape(
intermediate_size=intermediate_size,
tp_world_size=parallel_config.tensor_parallel_size,
n_groups=hf_config.mamba_n_groups,
num_heads=hf_config.mamba_n_heads,
head_dim=hf_config.mamba_d_head,
state_size=hf_config.mamba_d_state,
conv_kernel=hf_config.mamba_d_conv,
)
@classmethod
def get_mamba_state_copy_func(cls) -> tuple[MambaStateCopyFunc, MambaStateCopyFunc]:
return MambaStateCopyFuncCalculator.mamba2_state_copy_func()
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
config = vllm_config.model_config.hf_config
self.vllm_config = vllm_config
self.model_config = vllm_config.model_config
scheduler_config = vllm_config.scheduler_config
self.quant_config = vllm_config.quant_config
self.config = config
self.scheduler_config = scheduler_config
self.model = GraniteMoeHybridModel(
vllm_config=vllm_config, prefix=maybe_prefix(prefix, "model")
)
self.lm_head = ParallelLMHead(
config.vocab_size,
config.hidden_size,
quant_config=self.quant_config,
prefix=maybe_prefix(prefix, "lm_head"),
)
if config.tie_word_embeddings:
self.lm_head = self.lm_head.tie_weights(self.model.embed_tokens)
self.logits_processor = LogitsProcessor(
config.vocab_size,
config.vocab_size,
scale=1 / self.config.logits_scaling,
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
**kwargs,
):
hidden_states = self.model(
input_ids, positions, intermediate_tensors, inputs_embeds
)
return hidden_states
def compute_logits(
self,
hidden_states: torch.Tensor,
) -> torch.Tensor | None:
logits = self.logits_processor(self.lm_head, hidden_states)
return logits
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
loader = AutoWeightsLoader(self)
return loader.load_weights(weights)
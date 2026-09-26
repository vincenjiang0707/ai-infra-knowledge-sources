source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/lfm2/
lastmod: 2026-09-24

class Lfm2ForCausalLM(
nn.Module, HasInnerState, SupportsLoRA, SupportsPP, IsHybrid, SupportsQuant
):
packed_modules_mapping = {
"qkv_proj": [
"q_proj",
"k_proj",
"v_proj",
],
"w13": [
"w1",
"w3",
],
"in_proj": ["in_proj"],
}
# Reuse the backbone mapper so LoRA/quantization see the same name mapping.
hf_to_vllm_mapper = Lfm2Model.hf_to_vllm_mapper
# LoRA specific attributes
embedding_modules = {
"embed_tokens": "input_embeddings",
"lm_head": "output_embeddings",
}
@classmethod
def get_mamba_state_dtype_from_config(
cls,
vllm_config: "VllmConfig",
) -> tuple[torch.dtype, ...]:
return MambaStateDtypeCalculator.short_conv_state_dtype(
vllm_config.model_config.dtype,
vllm_config.cache_config.mamba_cache_dtype,
)
@classmethod
def get_mamba_state_shape_from_config(
cls,
vllm_config: "VllmConfig",
) -> tuple[tuple[int, int]]:
"""Calculate shapes for LFM2's convolutional cache.
Args:
vllm_config: vLLM config
Returns:
Tuple containing:
- conv_state_shape: Shape for convolutional state cache
"""
parallel_config = vllm_config.parallel_config
hf_config = vllm_config.model_config.hf_config
return MambaStateShapeCalculator.short_conv_state_shape(
tp_world_size=parallel_config.tensor_parallel_size,
intermediate_size=hf_config.conv_dim,
conv_kernel=hf_config.conv_L_cache,
)
@classmethod
def get_mamba_state_copy_func(cls) -> tuple[MambaStateCopyFunc]:
return MambaStateCopyFuncCalculator.short_conv_state_copy_func()
def __init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
config = vllm_config.model_config.hf_config
quant_config = vllm_config.quant_config
cache_config = vllm_config.cache_config
if cache_config.mamba_cache_mode == "all":
raise NotImplementedError(
"Lfm2 currently does not support 'all' prefix caching, "
"please use '--mamba-cache-mode=align' instead"
)
super().__init__()
self.config = config
self.model = Lfm2Model(
vllm_config=vllm_config, prefix=maybe_prefix(prefix, "model")
)
if get_pp_group().is_last_rank:
self.lm_head = ParallelLMHead(
config.vocab_size,
config.hidden_size,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "lm_head"),
)
self.lm_head = self.lm_head.tie_weights(self.model.embed_tokens)
else:
self.lm_head = PPMissingLayer()
self.logits_processor = LogitsProcessor(config.vocab_size)
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
) -> torch.Tensor:
hidden_states = self.model(
input_ids, positions, intermediate_tensors, inputs_embeds
)
return hidden_states
def compute_logits(self, hidden_states: torch.Tensor) -> torch.Tensor:
logits = self.logits_processor(self.lm_head, hidden_states)
return logits
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
loader = AutoWeightsLoader(self)
return loader.load_weights(weights)
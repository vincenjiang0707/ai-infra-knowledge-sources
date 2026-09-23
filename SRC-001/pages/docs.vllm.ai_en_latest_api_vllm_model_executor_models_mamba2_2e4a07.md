source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/mamba2/
lastmod: 2026-09-23

class Mamba2ForCausalLM(
nn.Module, HasInnerState, IsAttentionFree, SupportsMambaPrefixCaching
):
hf_to_vllm_mapper = WeightsMapper(orig_to_new_substr={".A_log": ".A"})
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
intermediate_size = hf_config.expand * hf_config.hidden_size
return MambaStateShapeCalculator.mamba2_state_shape(
intermediate_size=intermediate_size,
tp_world_size=parallel_config.tensor_parallel_size,
n_groups=hf_config.n_groups,
num_heads=hf_config.num_heads,
head_dim=hf_config.head_dim,
state_size=hf_config.state_size,
conv_kernel=hf_config.conv_kernel,
num_spec=vllm_config.num_speculative_tokens,
)
@classmethod
def get_mamba_state_copy_func(cls) -> tuple[MambaStateCopyFunc, MambaStateCopyFunc]:
return MambaStateCopyFuncCalculator.mamba2_state_copy_func()
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
config = vllm_config.model_config.hf_config
scheduler_config = vllm_config.scheduler_config
super().__init__()
self.config = config
self.vllm_config = vllm_config
self.scheduler_config = scheduler_config
self.model_config = vllm_config.model_config
self.backbone = Mamba2Model(
vllm_config=vllm_config, prefix=maybe_prefix(prefix, "backbone")
)
self.lm_head = ParallelLMHead(
config.vocab_size,
config.hidden_size,
prefix=maybe_prefix(prefix, "lm_head"),
)
if config.tie_word_embeddings:
self.lm_head = self.lm_head.tie_weights(self.backbone.embeddings)
self.logits_processor = LogitsProcessor(config.vocab_size)
self.make_empty_intermediate_tensors = (
self.backbone.make_empty_intermediate_tensors
)
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.backbone.embed_input_ids(input_ids)
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
**kwargs,
):
hidden_states = self.backbone(
input_ids, positions, intermediate_tensors, inputs_embeds
)
return hidden_states
def copy_inputs_before_cuda_graphs(self, input_buffers, **kwargs):
return self.mamba_cache.copy_inputs_before_cuda_graphs(input_buffers, **kwargs)
def get_seqlen_agnostic_capture_inputs(self, batch_size: int):
return self.mamba_cache.get_seqlen_agnostic_capture_inputs(batch_size)
def compute_logits(self, hidden_states: torch.Tensor) -> torch.Tensor:
logits = self.logits_processor(self.lm_head, hidden_states)
return logits
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
loader = AutoWeightsLoader(self)
return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
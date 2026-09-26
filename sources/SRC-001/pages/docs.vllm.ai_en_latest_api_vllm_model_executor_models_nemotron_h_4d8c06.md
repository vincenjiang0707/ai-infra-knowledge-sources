source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/nemotron_h/
lastmod: 2026-09-24

class NemotronHForCausalLM(
nn.Module,
HasInnerState,
SupportsLoRA,
SupportsPP,
SupportsEagle,
SupportsEagle3,
IsHybrid,
SupportsQuant,
MixtureOfExperts,
SupportsMambaPrefixCaching,
SupportsReplaySSM,
):
# Relevant only if self.has_moe is True
is_non_gated_moe = True
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_prefix={"backbone": "model", "mtp": None},
orig_to_new_substr={"A_log": "A", "embeddings": "embed_tokens"},
orig_to_new_stacked={
".q_proj": (".qkv_proj", "q"),
".k_proj": (".qkv_proj", "k"),
".v_proj": (".qkv_proj", "v"),
},
)
packed_modules_mapping = {
"qkv_proj": [
"q_proj",
"k_proj",
"v_proj",
],
}
# LoRA specific attributes
embedding_modules = {
"embed_tokens": "input_embeddings",
"lm_head": "output_embeddings",
}
# Skip MTP (Multi-Token Prediction) layers during LoRA loading
lora_skip_prefixes = ["mtp."]
@classmethod
def get_mamba_state_dtype_from_config(
cls,
vllm_config: "VllmConfig",
) -> tuple[torch.dtype, ...]:
cache_config = vllm_config.cache_config
base_dtype = MambaStateDtypeCalculator.mamba2_state_dtype(
vllm_config.model_config.dtype,
cache_config.mamba_cache_dtype,
cache_config.mamba_ssm_cache_dtype,
)
if cache_config.use_replayssm:
return MambaStateDtypeCalculator.append_replayssm_ring(
base_dtype,
vllm_config.model_config.dtype,
)
return base_dtype
@classmethod
def get_mamba_state_shape_from_config(
cls,
vllm_config: "VllmConfig",
) -> MambaStateShapes:
"""Calculate shapes for Mamba's convolutional and state caches.
Args:
vllm_config: vLLM config
Returns:
Tuple containing:
- conv_state_shape: Shape for convolutional state cache
- temporal_state_shape: Shape for state space model cache
- x_cache/dt_cache/B_cache ring-buffer shapes (use_replayssm only)
"""
parallel_config = vllm_config.parallel_config
cache_config = vllm_config.cache_config
hf_config = vllm_config.model_config.hf_config
intermediate_size = hf_config.mamba_num_heads * hf_config.mamba_head_dim
base_shape = MambaStateShapeCalculator.mamba2_state_shape(
intermediate_size=intermediate_size,
tp_world_size=parallel_config.tensor_parallel_size,
n_groups=hf_config.n_groups,
num_heads=hf_config.mamba_num_heads,
head_dim=hf_config.mamba_head_dim,
state_size=hf_config.ssm_state_size,
conv_kernel=hf_config.conv_kernel,
num_spec=vllm_config.num_speculative_tokens,
)
if cache_config.use_replayssm:
return MambaStateShapeCalculator.append_replayssm_ring(
base_shapes=base_shape,
n_groups=hf_config.n_groups,
tp_world_size=parallel_config.tensor_parallel_size,
logical_window=cache_config.replayssm_buffer_len,
backend=vllm_config.mamba_config.backend,
)
return base_shape
@classmethod
def get_mamba_state_copy_func(cls) -> tuple[MambaStateCopyFunc, MambaStateCopyFunc]:
return MambaStateCopyFuncCalculator.mamba2_state_copy_func()
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
config = vllm_config.model_config.hf_config
self.vllm_config = vllm_config
self.model_config = vllm_config.model_config
scheduler_config = vllm_config.scheduler_config
self.quant_config = vllm_config.quant_config
super().__init__()
self.config = config
self.scheduler_config = scheduler_config
self.model = NemotronHModel(
vllm_config=vllm_config, prefix=maybe_prefix(prefix, "model")
)
self.lm_head = ParallelLMHead(
config.vocab_size,
config.hidden_size,
quant_config=self.quant_config,
prefix=maybe_prefix(prefix, "lm_head"),
)
self.logits_processor = LogitsProcessor(config.vocab_size)
self.make_empty_intermediate_tensors = (
self.model.make_empty_intermediate_tensors
)
# Set MoE hyperparameters
if self.model.has_moe:
self.num_expert_groups = config.n_group
self.moe_layers = []
example_moe = None
for layer in self.model.layers:
if isinstance(layer, NemotronHMoEDecoderLayer):
# Pick last one layer since the first ones
# may be dense layers.
example_moe = layer.mixer
self.moe_layers.append(layer.mixer.experts)
self.num_moe_layers = len(self.moe_layers)
assert example_moe is not None
self.num_logical_experts = example_moe.n_logical_experts
self.num_physical_experts = example_moe.n_physical_experts
self.num_local_physical_experts = example_moe.n_local_physical_experts # noqa: E501
self.num_routed_experts = example_moe.n_routed_experts
self.num_shared_experts = example_moe.n_shared_experts
self.num_redundant_experts = example_moe.n_redundant_experts
def update_physical_experts_metadata(
self,
num_physical_experts: int,
num_local_physical_experts: int,
) -> None:
assert self.num_local_physical_experts == num_local_physical_experts
self.num_physical_experts = num_physical_experts
self.num_local_physical_experts = num_local_physical_experts
self.num_redundant_experts = num_physical_experts - self.num_logical_experts
for layer in self.model.layers:
if isinstance(layer, NemotronHMoEDecoderLayer):
moe = layer.mixer
moe.n_local_physical_experts = num_local_physical_experts
moe.n_physical_experts = num_physical_experts
moe.n_redundant_experts = self.num_redundant_experts
moe.experts.update_expert_map()
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
return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
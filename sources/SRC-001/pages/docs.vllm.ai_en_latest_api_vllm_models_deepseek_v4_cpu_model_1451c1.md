source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/cpu/model/
lastmod: 2026-09-23

class DeepseekV4ForCausalLM(nn.Module, SupportsPP, SupportsEagle3):
model_cls = DeepseekV4Model
# Default mapper assumes the original FP4-expert checkpoint layout.
# Overridden per-instance in __init__ when expert_dtype != "fp4".
hf_to_vllm_mapper = _make_deepseek_v4_weights_mapper("fp4")
packed_modules_mapping = {
"gate_up_proj": ["w1", "w3"],
"fused_wqa_wkv": ["wq_a", "wkv"],
}
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
config = vllm_config.model_config.hf_config
self.config = config
expert_dtype = getattr(config, "expert_dtype", "fp4")
self.model = self.model_cls(
vllm_config=vllm_config, prefix=maybe_prefix(prefix, "model")
)
if expert_dtype != "fp4" or self.model.is_fused_shared_expert_enabled:
self.hf_to_vllm_mapper = _make_deepseek_v4_weights_mapper(
expert_dtype,
fuse_shared_experts=self.model.is_fused_shared_expert_enabled,
)
if get_pp_group().is_last_rank:
self.lm_head = ParallelLMHead(
config.vocab_size,
config.hidden_size,
prefix=maybe_prefix(prefix, "lm_head"),
)
else:
self.lm_head = PPMissingLayer()
self.logits_processor = LogitsProcessor(config.vocab_size)
self.make_empty_intermediate_tensors = ( # type: ignore[method-assign]
self.model.make_empty_intermediate_tensors
)
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.model.embed_input_ids(input_ids)
def compute_logits(
self,
hidden_states: torch.Tensor,
) -> torch.Tensor | None:
logits = self.logits_processor(self.lm_head, hidden_states)
return logits
def forward(
self,
input_ids: torch.Tensor,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
) -> torch.Tensor | IntermediateTensors:
hidden_states = self.model(
input_ids, positions, intermediate_tensors, inputs_embeds
)
return hidden_states
def get_mtp_target_hidden_states(self) -> torch.Tensor | None:
"""Pre-hc_head residual stream buffer (max_num_batched_tokens,
hc_mult * hidden_size) for the MTP draft model. Populated by
forward(); valid after each target step."""
return getattr(self.model, "_mtp_hidden_buffer", None)
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
loader = AutoWeightsLoader(self)
return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
def process_weights_after_loading(self) -> None:
# No CPU AMX weight-packing hook yet.
pass
def get_expert_mapping(self) -> list[tuple[str, str, int, str]]:
return self.model.get_expert_mapping()
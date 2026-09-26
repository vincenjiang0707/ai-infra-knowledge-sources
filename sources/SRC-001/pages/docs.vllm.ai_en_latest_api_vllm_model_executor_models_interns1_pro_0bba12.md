source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interns1_pro/
lastmod: 2026-09-24

@MULTIMODAL_REGISTRY.register_processor(
Qwen3VLMultiModalProcessor,
info=InternS1ProProcessingInfo,
dummy_inputs=Qwen3VLDummyInputsBuilder,
)
class InternS1ProForConditionalGeneration(
Qwen3VLForConditionalGeneration, InternS1ProMoeMixtureOfExperts
):
is_3d_moe_weight: ClassVar[bool] = True
packed_modules_mapping: dict[str, list[str]] = {
"qkv_proj": [
"q_proj",
"k_proj",
"v_proj",
],
}
# To ensure correct weight loading and mapping.
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_prefix={
"model.visual.": "visual.",
"lm_head.": "language_model.lm_head.",
"model.language_model.": "language_model.model.",
},
)
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super(Qwen3VLForConditionalGeneration, self).__init__()
config: PreTrainedConfig = vllm_config.model_config.hf_config
multimodal_config = vllm_config.model_config.get_multimodal_config()
self.config = config
self.multimodal_config = multimodal_config
self.use_data_parallel = multimodal_config.mm_encoder_tp_mode == "data"
self._init_video_pruning(multimodal_config)
with self._mark_tower_model(vllm_config, {"image", "video"}):
self.visual = Qwen3_VisionTransformer(
config.vision_config,
norm_eps=getattr(config, "rms_norm_eps", 1e-6),
prefix=maybe_prefix(prefix, "visual"),
)
with self._mark_language_model(vllm_config):
self.language_model = InternS1ProMoeLLMForCausalLM(
vllm_config=vllm_config,
prefix=maybe_prefix(prefix, "language_model"),
)
# Whether to include the gate_up_proj mapping is determined by
# the language model.
self.packed_modules_mapping = (
self.packed_modules_mapping | self.language_model.packed_modules_mapping
)
self.make_empty_intermediate_tensors = (
self.language_model.make_empty_intermediate_tensors
)
self.use_deepstack = hasattr(config.vision_config, "deepstack_visual_indexes")
self.deepstack_num_level = (
len(config.vision_config.deepstack_visual_indexes)
if self.use_deepstack
else 0
)
self.visual_dim = config.vision_config.out_hidden_size
self.multiscale_dim = self.visual_dim * self.deepstack_num_level
# Set MoE hyperparameters
self.set_moe_parameters()
def get_frope_params_map(self) -> dict[str, str]:
mapper: dict[str, str] = {}
for name, params in self.language_model.model.named_parameters():
if "rotary_emb.sin_coef" in name:
mapper["language_model.model.rotary_emb.sin_coef"] = (
f"language_model.model.{name}"
)
if "rotary_emb.cos_coef" in name:
mapper["language_model.model.rotary_emb.cos_coef"] = (
f"language_model.model.{name}"
)
return mapper
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]):
"""Load weights"""
orig_to_new_prefix: dict[str, str | None] = {
"model.visual.": "visual.",
"lm_head.": "language_model.lm_head.",
"model.language_model.": "language_model.model.",
"model.time_series.": None,
}
if self.visual is None:
orig_to_new_prefix["visual."] = None
# FIXME(Isotr0py): See if we can avoid tighing FoPE to PP layers
weights_mapper = WeightsMapper(
orig_to_new_prefix=orig_to_new_prefix,
orig_to_new_suffix=self.get_frope_params_map(),
)
loader = AutoWeightsLoader(self)
return loader.load_weights(weights, mapper=weights_mapper)
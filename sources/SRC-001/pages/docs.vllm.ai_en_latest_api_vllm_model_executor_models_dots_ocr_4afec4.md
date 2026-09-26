source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/dots_ocr/
lastmod: 2026-09-24

@MULTIMODAL_REGISTRY.register_processor(
Qwen2VLMultiModalProcessor,
info=DotsOCRProcessingInfo,
dummy_inputs=DotsOCRDummyInputsBuilder,
)
class DotsOCRForCausalLM(nn.Module, SupportsMultiModal, SupportsPP, SupportsLoRA):
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_substr={
".attn.qkv_proj.": ".attn.qkv.",
".attn.out_proj.": ".attn.proj.",
},
orig_to_new_stacked={
".fc1.": (".fc13.", 0),
".fc3.": (".fc13.", 1),
},
orig_to_new_prefix={
"lm_head.": "language_model.lm_head.",
"model.": "language_model.model.",
},
)
packed_modules_mapping = {
"qkv_proj": [
"q_proj",
"k_proj",
"v_proj",
],
"gate_up_proj": [
"gate_proj",
"up_proj",
],
".attn.qkv": [".attn.qkv"],
"fc13": ["fc1", "fc3"],
}
supports_encoder_tp_data = True
supports_tower_connector_lora = True
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("image"):
return "<|img|><|imgpad|><|endofimg|>"
return None
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
self.config: DotsOCRConfig = vllm_config.model_config.hf_config
self.quant_config = vllm_config.quant_config
multimodal_config = vllm_config.model_config.multimodal_config
assert multimodal_config is not None
self.use_data_parallel = multimodal_config.mm_encoder_tp_mode == "data"
if isinstance(self.config.vision_config, dict):
vision_config = DotsVisionConfig(**self.config.vision_config)
self.config.vision_config = vision_config
else:
vision_config = self.config.vision_config
with self._mark_tower_model(vllm_config, "image"):
self.vision_tower = DotsVisionTransformer(
vision_config,
quant_config=self.quant_config,
prefix=maybe_prefix(prefix, "vision_tower"),
)
with self._mark_language_model(vllm_config):
self.language_model: Qwen2ForCausalLM = init_vllm_registered_model(
vllm_config=vllm_config,
hf_config=self.config,
prefix=maybe_prefix(prefix, "language_model"),
architectures=["Qwen2ForCausalLM"],
)
self.make_empty_intermediate_tensors = (
self.language_model.make_empty_intermediate_tensors
)
def _parse_and_validate_image_input(
self, **kwargs: object
) -> DotsOCRImageInputs | None:
pixel_values = kwargs.pop("pixel_values", None)
image_embeds = kwargs.pop("image_embeds", None)
image_grid_thw = kwargs.pop("image_grid_thw", None)
if pixel_values is None and image_embeds is None:
return None
if pixel_values is not None:
return DotsOCRImagePixelInputs(
type="pixel_values",
pixel_values=pixel_values,
image_grid_thw=image_grid_thw,
)
if image_embeds is not None:
return DotsOCRImageEmbeddingInputs(
type="image_embeds",
image_embeds=image_embeds,
image_grid_thw=image_grid_thw,
)
raise AssertionError
def _process_image_input(
self, image_input: DotsOCRImageInputs
) -> tuple[torch.Tensor, ...]:
grid_thw = image_input["image_grid_thw"]
assert grid_thw.ndim == 2
grid_thw_list = grid_thw.tolist()
if image_input["type"] == "image_embeds":
image_embeds = image_input["image_embeds"].type(self.vision_tower.dtype)
else:
pixel_values = image_input["pixel_values"].type(self.vision_tower.dtype)
if self.use_data_parallel:
return run_dp_sharded_mrope_vision_model(
self.vision_tower,
pixel_values,
grid_thw_list,
rope_type="rope_3d",
)
else:
image_embeds = self.vision_tower(pixel_values, grid_thw_list)[
:, : self.config.hidden_size
]
# Split concatenated embeddings for each image item.
merge_size = self.vision_tower.spatial_merge_size
sizes = (
torch.tensor(grid_thw_list, dtype=torch.long).prod(-1)
// (merge_size * merge_size)
).tolist()
return image_embeds.split(sizes)
def get_mm_lora_token_counts(
self,
*,
modality: str,
mm_kwargs: MultiModalKwargsItem | None,
num_mm_embeds: int,
) -> tuple[int, int | None]:
del modality, mm_kwargs
merge_size = self.vision_tower.spatial_merge_size
return num_mm_embeds * (merge_size**2), num_mm_embeds
def embed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
image_input = self._parse_and_validate_image_input(**kwargs)
if image_input is None:
return []
vision_embeddings = self._process_image_input(image_input)
return vision_embeddings
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
**kwargs,
) -> torch.Tensor | IntermediateTensors:
if intermediate_tensors is not None:
inputs_embeds = None
hidden_states = self.language_model(
input_ids=input_ids,
positions=positions,
intermediate_tensors=intermediate_tensors,
inputs_embeds=inputs_embeds,
)
return hidden_states
def compute_logits(
self,
hidden_states: torch.Tensor,
) -> torch.Tensor | None:
return self.language_model.compute_logits(hidden_states)
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
loader = AutoWeightsLoader(self)
return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
def get_mm_mapping(self) -> MultiModelKeys:
"""Get the module prefix in multimodal models."""
return MultiModelKeys.from_string_field(
language_model="language_model",
connector="vision_tower.merger",
tower_model="vision_tower.",
)
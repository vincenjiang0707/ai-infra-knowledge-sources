source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/cosmos3_edge/
lastmod: 2026-09-23

@MULTIMODAL_REGISTRY.register_processor(
Cosmos3EdgeMultiModalProcessor,
info=Cosmos3EdgeProcessingInfo,
dummy_inputs=Cosmos3EdgeDummyInputsBuilder,
)
class Cosmos3EdgeForConditionalGeneration(
nn.Module,
SupportsMultiModal,
SupportsPP,
SupportsMRoPE,
):
"""Cosmos3 Edge model with a SigLIP2 vision encoder.
Architecture:
- self.visual: SigLIP2 encoder + patch merger + projector
- self.language_model: Cosmos3EdgeForCausalLM (pure attention + RoPE)
"""
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_stacked={
".self_attn.q_proj": (".self_attn.qkv_proj", "q"),
".self_attn.k_proj": (".self_attn.qkv_proj", "k"),
".self_attn.v_proj": (".self_attn.qkv_proj", "v"),
},
orig_to_new_prefix={
**_cosmos3_edge_diffusers_prefix_map(),
"proj_in.": None,
"proj_out.": None,
"time_embedder.": None,
"action_proj_in.": None,
"action_proj_out.": None,
"audio_modality_embed": None,
"action_modality_embed": None,
"model.visual.": "visual.encoder.",
"model.projector.": "visual.projector.",
"lm_head.": "language_model.lm_head.",
"model.language_model.": "language_model.model.",
},
orig_to_new_substr={
"_moe_gen": None,
"k_norm_und_for_gen": None,
".add_q_proj.": None,
".add_k_proj.": None,
".add_v_proj.": None,
".to_add_out.": None,
".norm_added_q.": None,
".norm_added_k.": None,
".self_attn.to_q.": ".self_attn.q_proj.",
".self_attn.to_k.": ".self_attn.k_proj.",
".self_attn.to_v.": ".self_attn.v_proj.",
".self_attn.to_out.": ".self_attn.o_proj.",
"language_model.embeddings": "language_model.embed_tokens",
},
)
packed_modules_mapping = {
"qkv_proj": ["q_proj", "k_proj", "v_proj"],
}
# Cosmos3 Edge unified Diffusers checkpoints store reasoner weights across
# transformer/ and vision_encoder/. Match both while excluding VAE weights.
allow_patterns_overrides = ["[tv]*er/*.safetensors"]
supports_encoder_tp_data = True
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("image"):
return "<|vision_start|><|image_pad|><|vision_end|>"
if modality.startswith("video"):
return "<|vision_start|><|video_pad|><|vision_end|>"
raise ValueError(f"Unsupported modality: {modality}")
def __init__(self, *, vllm_config: VllmConfig, prefix: str = "model"):
super().__init__()
config = vllm_config.model_config.hf_config
quant_config = vllm_config.quant_config
multimodal_config = vllm_config.model_config.multimodal_config
assert multimodal_config is not None
self.config = config
self.multimodal_config = multimodal_config
self.use_data_parallel = multimodal_config.mm_encoder_tp_mode == "data"
with self._mark_tower_model(vllm_config, {"image", "video"}):
self.visual = Cosmos3EdgeVisionModel(
vision_config=config.vision_config,
projector_config=config.projector_config,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "visual"),
)
with self._mark_language_model(vllm_config):
self.language_model = Cosmos3EdgeForCausalLM(
vllm_config=vllm_config.with_hf_config(
config.text_config, architectures=["NemotronHForCausalLM"]
),
prefix=maybe_prefix(prefix, "language_model"),
)
self.make_empty_intermediate_tensors = (
self.language_model.make_empty_intermediate_tensors
)
def _get_image_features(
self,
pixel_values: torch.Tensor,
grid_thw: torch.Tensor,
) -> tuple[torch.Tensor, ...]:
"""Run the complete vision tower and split by media item."""
image_embeds = self.visual(pixel_values, grid_thw=grid_thw)
sizes = (grid_thw.prod(-1) // self.visual.spatial_merge_size**2).tolist()
return image_embeds.split(sizes)
def _parse_and_validate_image_input(
self, **kwargs: object
) -> Qwen2_5_VLImageInputs | None:
pixel_values = kwargs.pop("pixel_values", None)
image_embeds = kwargs.pop("image_embeds", None)
image_grid_thw = kwargs.pop("image_grid_thw", None)
if pixel_values is None and image_embeds is None:
return None
if pixel_values is not None:
return Qwen2_5_VLImagePixelInputs(
type="pixel_values",
pixel_values=pixel_values,
image_grid_thw=image_grid_thw,
)
if image_embeds is not None:
return Qwen2_5_VLImageEmbeddingInputs(
type="image_embeds",
image_embeds=image_embeds,
image_grid_thw=image_grid_thw,
)
raise AssertionError
def _parse_and_validate_video_input(
self, **kwargs: object
) -> Qwen2_5_VLVideoInputs | None:
pixel_values_videos = kwargs.pop("pixel_values_videos", None)
video_embeds = kwargs.pop("video_embeds", None)
video_grid_thw = kwargs.pop("video_grid_thw", None)
second_per_grid_ts = kwargs.pop("second_per_grid_ts", None)
if pixel_values_videos is None and video_embeds is None:
return None
if pixel_values_videos is not None:
return Qwen2_5_VLVideoPixelInputs(
type="pixel_values_videos",
pixel_values_videos=pixel_values_videos,
video_grid_thw=video_grid_thw,
second_per_grid_ts=second_per_grid_ts,
)
if video_embeds is not None:
return Qwen2_5_VLVideoEmbeddingInputs(
type="video_embeds",
video_embeds=video_embeds,
video_grid_thw=video_grid_thw,
)
raise AssertionError
def _process_image_input(
self, image_input: Qwen2_5_VLImageInputs
) -> tuple[torch.Tensor, ...]:
grid_thw = image_input["image_grid_thw"]
assert grid_thw.ndim == 2
if image_input["type"] == "image_embeds":
image_embeds = image_input["image_embeds"].type(self.visual.dtype)
merge_size = self.visual.spatial_merge_size
sizes = (grid_thw.prod(-1) // merge_size // merge_size).tolist()
return image_embeds.split(sizes)
pixel_values = image_input["pixel_values"].type(self.visual.dtype)
if self.use_data_parallel:
return run_dp_sharded_mrope_vision_model(
self.visual, pixel_values, grid_thw.tolist(), rope_type="rope_3d"
)
return self._get_image_features(pixel_values, grid_thw)
def _process_video_input(
self, video_input: Qwen2_5_VLVideoInputs
) -> tuple[torch.Tensor, ...]:
grid_thw = video_input["video_grid_thw"]
assert grid_thw.ndim == 2
if video_input["type"] == "video_embeds":
video_embeds = video_input["video_embeds"].type(self.visual.dtype)
merge_size = self.visual.spatial_merge_size
sizes = (grid_thw.prod(-1) // merge_size // merge_size).tolist()
return video_embeds.split(sizes)
pixel_values_videos = video_input["pixel_values_videos"].type(self.visual.dtype)
if self.use_data_parallel:
return run_dp_sharded_mrope_vision_model(
self.visual, pixel_values_videos, grid_thw.tolist(), rope_type="rope_3d"
)
return self._get_image_features(pixel_values_videos, grid_thw)
def _parse_and_validate_multimodal_inputs(self, **kwargs: object) -> dict:
modalities: dict = {}
image_input = self._parse_and_validate_image_input(**kwargs)
if image_input is not None:
modalities["image"] = image_input
video_input = self._parse_and_validate_video_input(**kwargs)
if video_input is not None:
modalities["video"] = video_input
return modalities
def embed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings | None:
mm_input_by_modality = self._parse_and_validate_multimodal_inputs(**kwargs)
if not mm_input_by_modality:
return None
multimodal_embeddings: tuple[torch.Tensor, ...] = ()
for modality in mm_input_by_modality:
multimodal_input = mm_input_by_modality[modality]
if modality == "image":
image_embeddings = self._process_image_input(multimodal_input)
multimodal_embeddings += tuple(image_embeddings)
if modality == "video":
video_embeddings = self._process_video_input(multimodal_input)
multimodal_embeddings += tuple(video_embeddings)
return multimodal_embeddings
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
**kwargs: object,
) -> torch.Tensor | IntermediateTensors:
if intermediate_tensors is not None:
inputs_embeds = None
return self.language_model.model(
input_ids=input_ids,
positions=positions,
intermediate_tensors=intermediate_tensors,
inputs_embeds=inputs_embeds,
)
def compute_logits(
self,
hidden_states: torch.Tensor,
) -> torch.Tensor | None:
return self.language_model.compute_logits(hidden_states)
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
loader = AutoWeightsLoader(self)
return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
def get_mm_mapping(self) -> MultiModelKeys:
return MultiModelKeys.from_string_field(
language_model="language_model",
connector="visual.projector",
tower_model="visual.",
)
def get_mrope_input_positions(
self,
input_tokens: list[int],
mm_features: list[MultiModalFeatureSpec],
) -> tuple[torch.Tensor, int]:
return Qwen3VLForConditionalGeneration._get_mrope_input_positions(
input_tokens=input_tokens,
mm_features=mm_features,
config=self.config,
)
source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/bailing_moe_v3_vl/
lastmod: 2026-09-24

@MULTIMODAL_REGISTRY.register_processor(
BailingMoeV3VLMultiModalProcessor,
info=BailingMoeV3VLProcessingInfo,
dummy_inputs=BailingMoeV3VLDummyInputsBuilder,
)
class BailingMoeV3VLForConditionalGeneration(
nn.Module,
HasInnerState,
IsHybrid,
SupportsMultiModal,
SupportsPP,
SupportsMRoPE,
):
"""Native vLLM wrapper for ``BailingMoeV3VLConfig`` checkpoints."""
packed_modules_mapping = {
**BailingMoeV3ForCausalLM.packed_modules_mapping,
# The vision checkpoint already stores Q/K/V in one tensor.
"qkv": ["qkv"],
}
hf_to_vllm_mapper = BailingMoeV3ForCausalLM.hf_to_vllm_mapper | WeightsMapper(
orig_to_new_prefix={
# Match module names as well as parameter names for quantization.
"model.visual": "visual",
"model.linear_proj": "linear_proj",
"linear_proj.0": "linear_proj.linear_fc1",
"linear_proj.2": "linear_proj.linear_fc2",
"lm_head": "language_model.lm_head",
"model.": "language_model.model.",
}
)
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("image"):
return IMAGE_PLACEHOLDER
raise ValueError("Only image modality is supported")
@classmethod
def get_mamba_state_shape_from_config(
cls, vllm_config: VllmConfig
) -> tuple[tuple[int, int], tuple[int, int, int]]:
text_config = vllm_config.model_config.hf_config.text_config
return BailingMoeV3ForCausalLM.get_mamba_state_shape_from_config(
vllm_config.with_hf_config(text_config)
)
@classmethod
def get_mamba_state_dtype_from_config(
cls, vllm_config: VllmConfig
) -> tuple[torch.dtype, torch.dtype]:
text_config = vllm_config.model_config.hf_config.text_config
return BailingMoeV3ForCausalLM.get_mamba_state_dtype_from_config(
vllm_config.with_hf_config(text_config)
)
@classmethod
def get_mamba_state_copy_func(cls) -> tuple:
return BailingMoeV3ForCausalLM.get_mamba_state_copy_func()
def __init__(self, *, vllm_config: VllmConfig, prefix: str = "model") -> None:
super().__init__()
config = vllm_config.model_config.hf_config
vision_config = config.vision_config
text_config = config.text_config
quant_config = vllm_config.quant_config
self.config = config
self.model_config = vllm_config.model_config
merged_vision_size = vision_config.hidden_size * (
vision_config.spatial_merge_size**2
)
with self._mark_tower_model(vllm_config, "image"):
self.visual = BailingMoeV3VisionTransformer(
vision_config,
norm_eps=getattr(config, "rms_norm_eps", 1e-6),
quant_config=quant_config,
prefix=maybe_prefix(prefix, "visual"),
)
self.linear_proj = BailingMoeV3VLProjector(
vision_hidden_size=merged_vision_size,
text_hidden_size=text_config.hidden_size,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "linear_proj"),
)
with self._mark_language_model(vllm_config):
self.language_model = BailingMoeV3ForCausalLM(
vllm_config=vllm_config.with_hf_config(text_config),
prefix=maybe_prefix(prefix, "language_model"),
)
self.make_empty_intermediate_tensors = (
self.language_model.make_empty_intermediate_tensors
)
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
return Qwen2_5_VLImageEmbeddingInputs(
type="image_embeds",
image_embeds=image_embeds,
image_grid_thw=image_grid_thw,
)
def _process_image_input(
self, image_input: Qwen2_5_VLImageInputs
) -> tuple[torch.Tensor, ...]:
image_grid_thw = image_input["image_grid_thw"]
assert image_grid_thw.ndim == 2
if image_input["type"] == "image_embeds":
image_embeds = image_input["image_embeds"]
else:
pixel_values = image_input["pixel_values"].type(self.visual.dtype)
vision_features = self.visual(
pixel_values,
grid_thw=image_grid_thw,
)
image_embeds = self.linear_proj(vision_features)
image_embeds = image_embeds.to(dtype=self.visual.dtype)
merge_unit = self.visual.spatial_merge_size**2
sizes = (image_grid_thw.prod(-1) // merge_unit).tolist()
return image_embeds.split(sizes)
def embed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
image_input = self._parse_and_validate_image_input(**kwargs)
if image_input is None:
return []
return self._process_image_input(image_input)
def embed_input_ids(
self,
input_ids: torch.Tensor,
multimodal_embeddings: MultiModalEmbeddings | None = None,
*,
is_multimodal: torch.Tensor | None = None,
) -> torch.Tensor:
inputs_embeds = self._embed_text_input_ids(
input_ids,
self.language_model.embed_input_ids,
is_multimodal=is_multimodal,
)
if multimodal_embeddings is None or len(multimodal_embeddings) == 0:
return inputs_embeds
return _merge_multimodal_embeddings(
inputs_embeds=inputs_embeds,
multimodal_embeddings=multimodal_embeddings,
is_multimodal=_require_is_multimodal(is_multimodal),
)
def get_mrope_input_positions(
self,
input_tokens: list[int],
mm_features: list[MultiModalFeatureSpec],
) -> tuple[torch.Tensor, int]:
position_blocks: list[np.ndarray] = []
consumed = 0
merge_size = self.config.vision_config.spatial_merge_size
for mm_feature in sorted(mm_features, key=lambda f: f.mm_position.offset):
if mm_feature.modality != "image":
raise ValueError(f"Unsupported modality: {mm_feature.modality}")
offset = mm_feature.mm_position.offset
text_len = offset - consumed
start = position_blocks[-1].max() + 1 if position_blocks else 0
position_blocks.append(
np.broadcast_to(np.arange(text_len), (3, text_len)) + start
)
assert mm_feature.data is not None
image_grid_thw = mm_feature.data["image_grid_thw"].data
assert isinstance(image_grid_thw, torch.Tensor)
t, h, w = image_grid_thw.tolist()
assert t == 1, f"Image must have one temporal grid, got {t}"
grid = np.indices((t, h // merge_size, w // merge_size))
position_blocks.append(grid.reshape(3, -1) + text_len + start)
consumed = offset + t * (h // merge_size) * (w // merge_size)
if consumed < len(input_tokens):
start = position_blocks[-1].max() + 1 if position_blocks else 0
text_len = len(input_tokens) - consumed
position_blocks.append(
np.broadcast_to(np.arange(text_len), (3, text_len)) + start
)
if not position_blocks:
positions = np.empty((3, 0), dtype=np.int64)
return torch.from_numpy(positions), 0
positions = np.concatenate(position_blocks, axis=1).reshape(3, -1)
position_delta = int(positions.max() + 1 - len(input_tokens))
return torch.from_numpy(positions), position_delta
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
return self.language_model(
input_ids=input_ids,
positions=positions,
intermediate_tensors=intermediate_tensors,
inputs_embeds=inputs_embeds,
)
def compute_logits(self, hidden_states: torch.Tensor) -> torch.Tensor:
return self.language_model.compute_logits(hidden_states)
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
loader = AutoWeightsLoader(self)
return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
def get_mm_mapping(self) -> MultiModelKeys:
return MultiModelKeys.from_string_field(
language_model="language_model",
connector="linear_proj",
tower_model="visual.",
)
def get_num_mm_encoder_tokens(self, num_image_tokens: int) -> int:
return num_image_tokens * self.visual.spatial_merge_size**2
def get_num_mm_connector_tokens(self, num_vision_tokens: int) -> int:
return num_vision_tokens // self.visual.spatial_merge_size**2
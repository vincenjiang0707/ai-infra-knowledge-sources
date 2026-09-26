source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/glm4_1v/
lastmod: 2026-09-24

@MULTIMODAL_REGISTRY.register_processor(
Glm4vMultiModalProcessor,
info=Glm4vProcessingInfo,
dummy_inputs=Glm4vDummyInputsBuilder,
)
class Glm4vForConditionalGeneration(
nn.Module,
SupportsMultiModal,
SupportsEncoderCudaGraph,
SupportsLoRA,
SupportsPP,
SupportsMRoPE,
):
packed_modules_mapping = {
"qkv_proj": [
"q_proj",
"k_proj",
"v_proj",
],
"gate_up_proj": ["gate_up_proj"],
}
# To ensure correct weight loading and mapping.
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_prefix={
"lm_head.": "language_model.lm_head.",
"model.language_model.": "language_model.model.",
"model.visual.": "visual.",
}
)
supports_encoder_tp_data = True
supports_tower_connector_lora = True
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("image"):
return "<|begin_of_image|><|image|><|end_of_image|>"
if modality.startswith("video"):
return "<|begin_of_video|><|video|><|end_of_video|>"
raise ValueError("Only image or video modality is supported")
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
config = vllm_config.model_config.hf_config
quant_config = vllm_config.quant_config
multimodal_config = vllm_config.model_config.multimodal_config
self.config = config
self.model_config = vllm_config.model_config
self.multimodal_config = multimodal_config
assert multimodal_config is not None
self.use_data_parallel = multimodal_config.mm_encoder_tp_mode == "data"
self.is_multimodal_pruning_enabled = (
multimodal_config.is_multimodal_pruning_enabled()
)
with self._mark_tower_model(vllm_config, {"image", "video"}):
self.visual = Glm4vVisionTransformer(
config.text_config,
config.vision_config,
norm_eps=getattr(config, "rms_norm_eps", 1e-5),
quant_config=quant_config,
prefix=maybe_prefix(prefix, "visual"),
)
if config.model_type in ("glm4v", "glm_ocr", "glmga"):
architectures = ["Glm4ForCausalLM"]
elif config.model_type == "glm4v_moe":
architectures = ["Glm4MoeForCausalLM"]
else:
architectures = None
with self._mark_language_model(vllm_config):
self.language_model = init_vllm_registered_model(
vllm_config=vllm_config,
hf_config=config.text_config,
prefix=maybe_prefix(prefix, "language_model"),
architectures=architectures,
)
self.make_empty_intermediate_tensors = (
self.language_model.make_empty_intermediate_tensors
)
def _parse_and_validate_image_input(
self, **kwargs: object
) -> Glm4vImageInputs | None:
pixel_values = kwargs.pop("pixel_values", None)
image_embeds = kwargs.pop("image_embeds", None)
image_grid_thw = kwargs.pop("image_grid_thw", None)
if pixel_values is None and image_embeds is None:
return None
if pixel_values is not None:
return Glm4vImagePixelInputs(
type="pixel_values",
pixel_values=pixel_values,
image_grid_thw=image_grid_thw,
)
if image_embeds is not None:
return Glm4vImageEmbeddingInputs(
type="image_embeds",
image_embeds=image_embeds,
image_grid_thw=image_grid_thw,
)
raise AssertionError("image input must contain pixels or embeddings")
def _parse_and_validate_video_input(
self, **kwargs: object
) -> Glm4vVideoInputs | None:
pixel_values_videos = kwargs.pop("pixel_values_videos", None)
video_embeds = kwargs.pop("video_embeds", None)
video_grid_thw = kwargs.pop("video_grid_thw", None)
if pixel_values_videos is None and video_embeds is None:
return None
if pixel_values_videos is not None:
return Glm4vVideoPixelInputs(
type="pixel_values_videos",
pixel_values_videos=pixel_values_videos,
video_grid_thw=video_grid_thw,
)
if video_embeds is not None:
return Glm4vVideoEmbeddingInputs(
type="video_embeds",
video_embeds=video_embeds,
video_grid_thw=video_grid_thw,
)
raise AssertionError("video input must contain pixels or embeddings")
def _process_image_input(
self, image_input: Glm4vImageInputs
) -> tuple[torch.Tensor, ...]:
grid_thw = image_input["image_grid_thw"]
assert grid_thw.ndim == 2
if image_input["type"] == "image_embeds":
image_embeds = image_input["image_embeds"].type(self.visual.dtype)
else:
pixel_values = image_input["pixel_values"].type(self.visual.dtype)
if self.use_data_parallel:
return run_dp_sharded_mrope_vision_model(
self.visual, pixel_values, grid_thw.tolist(), rope_type="rope_3d"
)
else:
image_embeds = self.visual(pixel_values, grid_thw=grid_thw)
merge_size = self.visual.spatial_merge_size
sizes = (grid_thw.prod(-1) // merge_size // merge_size).tolist()
return image_embeds.split(sizes)
def _process_video_input(
self, video_input: Glm4vVideoInputs
) -> tuple[torch.Tensor, ...]:
grid_thw = video_input["video_grid_thw"]
assert grid_thw.ndim == 2
if video_input["type"] == "video_embeds":
video_embeds = video_input["video_embeds"].type(self.visual.dtype)
else:
pixel_values_videos = video_input["pixel_values_videos"].type(
self.visual.dtype
)
if self.use_data_parallel:
return run_dp_sharded_mrope_vision_model(
self.visual,
pixel_values_videos,
grid_thw.tolist(),
rope_type="rope_3d",
)
else:
video_embeds = self.visual(pixel_values_videos, grid_thw=grid_thw)
# Split concatenated embeddings for each video item.
merge_size = self.visual.spatial_merge_size
sizes = (grid_thw.prod(-1) // merge_size // merge_size).tolist()
return video_embeds.split(sizes)
# -- SupportsEncoderCudaGraph protocol methods --
def get_encoder_cudagraph_config(self):
from vllm.v1.worker.encoder_cudagraph_defs import (
EncoderCudaGraphConfig,
)
# When EVS pruning is enabled, embed_multimodal post-processes both
# image and video embeddings (mrope positions are appended for image,
# prune+append for video). The encoder CUDA graph path bypasses that
# post-process, producing inconsistent embedding formats vs eager. So
# disable CUDA graph for all modalities when pruning is on.
modalities = [] if self.is_multimodal_pruning_enabled else ["image", "video"]
# Compute max_frames_per_video for budget sizing.
max_frames = self.get_max_frames_per_video() if "video" in modalities else 1
return EncoderCudaGraphConfig(
modalities=modalities,
buffer_keys=[
"pixel_values",
"pos_embeds",
"rotary_pos_emb_cos",
"rotary_pos_emb_sin",
"cu_seqlens",
"max_seqlen",
"sequence_lengths",
],
out_hidden_size=self.visual.out_hidden_size,
max_frames_per_video=max_frames,
)
def get_input_modality(
self,
mm_kwargs: dict[str, Any],
) -> str:
if "image_grid_thw" in mm_kwargs:
return "image"
elif "video_grid_thw" in mm_kwargs:
return "video"
raise AssertionError("This line should be unreachable.")
def get_max_frames_per_video(self) -> int:
return _MAX_FRAMES_PER_VIDEO
def get_encoder_cudagraph_budget_range(
self,
vllm_config,
) -> tuple[int, int]:
# Min: estimated smallest possible encoder input.
# 224x224 image → 16x16 patches (patch_size=14)
# spatial_merge_size=2 → 8x8 = 64 tokens
min_budget = 64
# Max: capped by max_num_batched_tokens
max_budget = min(
vllm_config.scheduler_config.max_num_batched_tokens,
vllm_config.model_config.max_model_len,
)
return (min_budget, max_budget)
def _get_pixel_values_by_modality(
self,
mm_kwargs: dict[str, Any],
) -> torch.Tensor:
if self.get_input_modality(mm_kwargs) == "image":
pixel_values = mm_kwargs["pixel_values"]
else:
pixel_values = mm_kwargs["pixel_values_videos"]
return pixel_values
def _get_grid_thw_by_modality(
self,
mm_kwargs: dict[str, Any],
) -> list[list[int]]:
grid_thw_key = f"{self.get_input_modality(mm_kwargs)}_grid_thw"
grid_thw = mm_kwargs[grid_thw_key]
if not isinstance(grid_thw, list):
grid_thw = grid_thw.tolist()
return [list(row) for row in grid_thw]
def get_encoder_cudagraph_item_specs(
self,
mm_kwargs: dict[str, Any],
):
from vllm.v1.worker.encoder_cudagraph_defs import EncoderItemSpec
m = self.visual.spatial_merge_size
grid_thw = self._get_grid_thw_by_modality(mm_kwargs)
return [
EncoderItemSpec(
input_size=t * h * w,
output_tokens=t * (h // m) * (w // m),
)
for t, h, w in grid_thw
]
def select_encoder_cudagraph_items(
self,
mm_kwargs: dict[str, Any],
indices: list[int],
) -> dict[str, Any]:
grid_thw = self._get_grid_thw_by_modality(mm_kwargs)
pixel_values = self._get_pixel_values_by_modality(mm_kwargs)
if len(indices) == 0:
if self.get_input_modality(mm_kwargs) == "image":
return {
"pixel_values": pixel_values[:0],
"image_grid_thw": [],
}
else:
return {
"pixel_values_videos": pixel_values[:0],
"video_grid_thw": [],
}
# Compute cumulative patch offsets for slicing pixel_values
patches_per_item = [t * h * w for t, h, w in grid_thw]
cum_patches = [0]
for p in patches_per_item:
cum_patches.append(cum_patches[-1] + p)
selected_pv = torch.cat(
[pixel_values[cum_patches[i] : cum_patches[i + 1]] for i in indices]
)
selected_grid = [grid_thw[i] for i in indices]
if self.get_input_modality(mm_kwargs) == "image":
return {
"pixel_values": selected_pv,
"image_grid_thw": selected_grid,
}
else:
return {
"pixel_values_videos": selected_pv,
"video_grid_thw": selected_grid,
}
def prepare_encoder_cudagraph_capture_inputs(
self,
token_budget: int,
max_batch_size: int,
max_frames_per_batch: int,
device: torch.device,
dtype: torch.dtype,
path: str = "default",
axis_keys: tuple[Hashable, ...] | None = None,
):
from vllm.v1.worker.encoder_cudagraph_defs import (
EncoderCudaGraphCaptureInputs,
)
spatial_merge_size = self.visual.spatial_merge_size
per_mm_item_output = token_budget // max_batch_size
frames_per_item = max_frames_per_batch // max_batch_size
if frames_per_item > 1:
# Build the capture grid using a video-format layout so that
# cu_seqlens is sized for video replays from the start.
# cu_seqlens has one entry per attention sequence (one per frame),
# so using T > 1 per item makes the buffer large enough without
# relying solely on padding.
# Ceiling ensures frames_per_item * tokens_per_frame >= per_mm_item_output
# so the pixel_values buffer covers any valid single-item replay.
tokens_per_frame = (
per_mm_item_output + frames_per_item - 1
) // frames_per_item
# Video-format grid_config (T=frames_per_item).
grid_config = [
[
frames_per_item,
spatial_merge_size,
tokens_per_frame * spatial_merge_size,
]
for _ in range(max_batch_size)
]
else:
# Image-format grid_config (T=1).
grid_config = [
[1, spatial_merge_size, per_mm_item_output * spatial_merge_size]
for _ in range(max_batch_size)
]
# Create dummy pixel_values
patch_embed = self.visual.patch_embed
in_channels = patch_embed.proj.in_channels
patch_size = patch_embed.patch_size
temporal_patch_size = patch_embed.temporal_patch_size
total_patches = sum(t * h * w for t, h, w in grid_config)
flattened_patch_size = (
in_channels * temporal_patch_size * patch_size * patch_size
)
dummy_pixel_values = torch.randn(
total_patches, flattened_patch_size, device=device, dtype=dtype
)
# Override max_seqlen with a safe upper bound for capture.
# max_seqlen.item() gets baked into the CUDA graph (not replayed),
# so the capture value must cover any replay scenario.
# Worst case: 1 item consuming the full budget ->
# seq_len = token_budget * spatial_merge_size^2.
metadata = self.visual.prepare_encoder_metadata(
grid_config,
max_batch_size=max_batch_size,
max_frames_per_batch=max_frames_per_batch,
max_seqlen_override=token_budget * (spatial_merge_size**2),
device=device,
)
# Just use image-modality dummy input_buffer for capturing, since it's also
# compatible for video inputs (has the same shape: [num_patches, C*T*P*P]).
values = metadata | {
"pixel_values": dummy_pixel_values,
}
return EncoderCudaGraphCaptureInputs(
values=values,
)
def prepare_encoder_cudagraph_replay_buffers(
self,
mm_kwargs: dict[str, Any],
max_batch_size: int,
max_frames_per_batch: int,
path: str = "default",
):
modality = self.get_input_modality(mm_kwargs)
grid_thw_list = self._get_grid_thw_by_modality(mm_kwargs)
if modality == "image":
metadata = self.visual.prepare_encoder_metadata(
grid_thw_list,
max_batch_size=max_batch_size,
)
elif modality == "video":
metadata = self.visual.prepare_encoder_metadata(
grid_thw_list,
max_frames_per_batch=max_frames_per_batch,
)
else:
raise AssertionError("This line should be unreachable.")
values = metadata | {
"pixel_values": self._get_pixel_values_by_modality(mm_kwargs),
}
return EncoderCudaGraphReplayBuffers(values=values)
def encoder_cudagraph_forward(
self,
values: dict[str, torch.Tensor],
path: str = "default",
) -> torch.Tensor:
pixel_values = values.pop("pixel_values")
metadata = values
return self.visual(pixel_values, None, encoder_metadata=metadata)
def encoder_eager_forward(
self,
mm_kwargs: dict[str, Any],
path: str = "default",
) -> torch.Tensor:
pixel_values = self._get_pixel_values_by_modality(mm_kwargs)
grid_thw = self._get_grid_thw_by_modality(mm_kwargs)
return self.visual(pixel_values, grid_thw)
def _parse_and_validate_multimodal_inputs(self, **kwargs: object) -> dict:
mm_input_by_modality: dict[str, Glm4vImageInputs | Glm4vVideoInputs | None] = {}
# Preserve the order of modalities if there are multiple of them
# from the order of kwargs.
for input_key in kwargs:
if (
input_key in ("pixel_values", "image_embeds")
and "image" not in mm_input_by_modality
):
mm_input_by_modality["image"] = self._parse_and_validate_image_input(
**kwargs
)
if (
input_key in ("pixel_values_videos", "video_embeds")
and "video" not in mm_input_by_modality
):
mm_input_by_modality["video"] = self._parse_and_validate_video_input(
**kwargs
)
return mm_input_by_modality
def embed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings | None:
mm_input_by_modality = self._parse_and_validate_multimodal_inputs(**kwargs)
if not mm_input_by_modality:
return None
# The result multimodal_embeddings is tuple of tensors, with each
# tensor corresponding to a multimodal data item (image or video).
multimodal_embeddings: tuple[torch.Tensor, ...] = ()
# NOTE: It is important to iterate over the keys in this dictionary
# to preserve the order of the modalities.
for modality in mm_input_by_modality:
multimodal_input = mm_input_by_modality[modality]
if modality == "image":
assert isinstance(
multimodal_input,
(Glm4vImagePixelInputs, Glm4vImageEmbeddingInputs),
)
image_embeddings = self._process_image_input(multimodal_input)
multimodal_embeddings += tuple(image_embeddings)
if modality == "video":
assert isinstance(
multimodal_input,
(Glm4vVideoPixelInputs, Glm4vVideoEmbeddingInputs),
)
video_embeddings = self._process_video_input(multimodal_input)
multimodal_embeddings += tuple(video_embeddings)
return multimodal_embeddings
def iter_mm_grid_thw(
self, mm_features: list[MultiModalFeatureSpec]
) -> Iterator[tuple[int, int, int, int]]:
hf_config = self.config
spatial_merge_size = hf_config.vision_config.spatial_merge_size
for mm_feature in sorted(mm_features, key=lambda f: f.mm_position.offset):
embed_ranges = mm_feature.mm_position.extract_embeds_range()
if mm_feature.modality == "image":
feature_data = mm_feature.data
assert feature_data is not None
grid_item = feature_data.get("image_grid_thw")
assert grid_item is not None
grid_data = grid_item.data
assert isinstance(grid_data, torch.Tensor)
t, h, w = grid_data.tolist()
assert t == 1, f"Image must have 1 frame, got {t}"
assert len(embed_ranges) == 1
offset, end = embed_ranges[0]
assert end - offset + 1 == h * w // spatial_merge_size**2
yield offset, t, h // spatial_merge_size, w // spatial_merge_size
elif mm_feature.modality == "video":
feature_data = mm_feature.data
assert feature_data is not None
grid_item = feature_data.get("video_grid_thw")
assert grid_item is not None
grid_data = grid_item.data
assert isinstance(grid_data, torch.Tensor)
t, h, w = grid_data.tolist()
llm_grid_h = h // spatial_merge_size
llm_grid_w = w // spatial_merge_size
num_tokens_per_frame = llm_grid_h * llm_grid_w
if len(embed_ranges) == t:
for offset, end in embed_ranges:
assert end - offset + 1 == num_tokens_per_frame
yield offset, 1, llm_grid_h, llm_grid_w
else:
offset = mm_feature.mm_position.offset
yield offset, t, llm_grid_h, llm_grid_w
else:
raise ValueError(f"Unsupported modality: {mm_feature.modality}")
def get_mrope_input_positions(
self,
input_tokens: list[int],
mm_features: list[MultiModalFeatureSpec],
) -> tuple[torch.Tensor, int]:
llm_pos_ids_list: list = []
st = 0
for (
offset,
llm_grid_t,
llm_grid_h,
llm_grid_w,
) in self.iter_mm_grid_thw(mm_features):
text_len = offset - st
st_idx = llm_pos_ids_list[-1].max() + 1 if len(llm_pos_ids_list) > 0 else 0
llm_pos_ids_list.append(
np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
)
grid_indices = np.indices((llm_grid_t, llm_grid_h, llm_grid_w)).reshape(
3, -1
)
llm_pos_ids_list.append(grid_indices + text_len + st_idx)
st = offset + llm_grid_t * llm_grid_h * llm_grid_w
if st < len(input_tokens):
text_len = len(input_tokens) - st
st_idx = llm_pos_ids_list[-1].max() + 1 if len(llm_pos_ids_list) > 0 else 0
llm_pos_ids_list.append(
np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
)
llm_positions = np.concatenate(llm_pos_ids_list, axis=1).reshape(3, -1)
mrope_position_delta = (llm_positions.max() + 1 - len(input_tokens)).item()
return torch.from_numpy(llm_positions), mrope_position_delta
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
**kwargs: object,
) -> torch.Tensor | IntermediateTensors:
"""Run forward pass for GLM-4V.
Args:
input_ids: Flattened (concatenated) input_ids corresponding to a
batch.
positions: Flattened (concatenated) position ids corresponding to a
batch.
**NOTE**: If mrope is enabled (default setting for GLM-4V
opensource models), the shape will be `(3, seq_len)`,
otherwise it will be `(seq_len,).
intermediate_tensors: Optional intermediate tensors for pipeline
parallelism.
inputs_embeds: Optional pre-computed input embeddings.
**kwargs: Additional keyword arguments.
"""
if intermediate_tensors is not None:
inputs_embeds = None
hidden_states = self.language_model.model(
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
language_model="language_model.model",
connector="visual.merger.",
tower_model="visual.",
)
def get_mm_lora_token_counts(
self,
*,
modality: str,
mm_kwargs: MultiModalKwargsItem | None,
num_mm_embeds: int,
) -> tuple[int, int | None]:
del modality, mm_kwargs
merge_size = self.config.vision_config.spatial_merge_size
return num_mm_embeds * (merge_size**2), num_mm_embeds
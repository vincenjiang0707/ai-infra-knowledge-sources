source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/ernie45_vl/
lastmod: 2026-09-24

@MULTIMODAL_REGISTRY.register_processor(
Ernie4_5VLMultiModalProcessor,
info=Ernie4_5_VLProcessingInfo,
dummy_inputs=Ernie4_5_VLDummyInputsBuilder,
)
class Ernie4_5_VLMoeForConditionalGeneration(
nn.Module,
SupportsMultiModal,
SupportsLoRA,
SupportsPP,
SupportsMRoPE,
SupportsEncoderCudaGraph,
):
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
}
# To ensure correct weight loading and mapping.
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_prefix={
"lm_head.": "language_model.lm_head.",
"model.": "language_model.model.",
# model.resampler_model.-> language_model.model.resampler_model.
# language_model.model.resampler_model. -> resampler_model.
"language_model.model.resampler_model.": "resampler_model.",
},
# resampler_weight_mappings
orig_to_new_substr={
"spatial_linear.0.": "spatial_linear1.",
"spatial_linear.2.": "spatial_linear2.",
"spatial_linear.3.": "spatial_norm.",
"temporal_linear.0.": "temporal_linear1.",
"temporal_linear.2.": "temporal_linear2.",
"temporal_linear.3.": "temporal_norm.",
},
)
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("image"):
return "<|IMAGE_START|><|image@placeholder|><|IMAGE_END|>"
if modality.startswith("video"):
return "<|VIDEO_START|><|video@placeholder|><|VIDEO_END|>"
raise ValueError("Only image or video modality is supported")
def __init__(self, vllm_config: VllmConfig, prefix: str = "") -> None:
super().__init__()
config = vllm_config.model_config.hf_config
quant_config = vllm_config.quant_config
multimodal_config = vllm_config.model_config.multimodal_config
self.config = config
self.multimodal_config = multimodal_config
with self._mark_tower_model(vllm_config, {"image", "video"}):
self.vision_model = Ernie4_5_VisionTransformer(
config.vision_config,
norm_eps=getattr(config, "rms_norm_eps", 1e-6),
quant_config=quant_config,
prefix=maybe_prefix(prefix, "vision_model"),
)
self.resampler_model = VariableResolutionResamplerModel(
self.config.pixel_hidden_size,
self.config.hidden_size,
self.config.spatial_conv_size,
self.config.temporal_conv_size,
config=self.config,
prefix=maybe_prefix(prefix, "resampler_model"),
)
with self._mark_language_model(vllm_config):
self.language_model = Ernie4_5_VLMoeForCausalLM(
vllm_config=vllm_config,
prefix=maybe_prefix(prefix, "language_model"),
)
self.visual_token_mask = None
self.make_empty_intermediate_tensors = (
self.language_model.make_empty_intermediate_tensors
)
if getattr(self.config, "im_patch_id", None):
visual_token_ids = [
token_id
for token_id in [
self.config.im_patch_id,
getattr(self.config, "image_start_token_id", None),
getattr(self.config, "image_end_token_id", None),
getattr(self.config, "video_start_token_id", None),
getattr(self.config, "video_end_token_id", None),
]
if token_id is not None
]
visual_token_ids_tensor_cache = torch.tensor(
visual_token_ids, dtype=torch.long
)
else:
visual_token_ids_tensor_cache = None
self.register_buffer(
"_visual_token_ids_tensor_cache",
visual_token_ids_tensor_cache,
persistent=False,
)
def compute_logits(
self,
hidden_states: torch.Tensor,
) -> torch.Tensor | None:
return self.language_model.compute_logits(hidden_states)
def _vision_forward(
self,
pixel_values: torch.Tensor,
grid_thw: torch.Tensor,
) -> torch.Tensor:
if grid_thw is not None:
grid_thw = grid_thw[grid_thw > 0]
if grid_thw.numel() % 3 != 0:
raise ValueError(
f"grid_thw has {grid_thw.numel()} elements after filtering,"
"which is not divisible by 3."
)
grid_thw = grid_thw.reshape(-1, 3)
# example: [[1,64,64],[2,80,80]] -> [[1,64,64],[1,80,80],[1,80,80]]
grid_thw = F.pad(
torch.repeat_interleave(grid_thw[:, 1:], grid_thw[:, 0], 0),
[1, 0, 0, 0],
value=1,
)
image_features = self.vision_model(pixel_values, grid_thw)
return image_features
def _set_visual_token_mask(self, input_ids: torch.Tensor) -> None:
"""Set mask for visual tokens (image/video patches and delimiters)."""
if self._visual_token_ids_tensor_cache is None:
self.visual_token_mask = None
return
# Create tensor on the correct device
visual_token_ids_tensor = self._visual_token_ids_tensor_cache.to(
device=input_ids.device,
dtype=input_ids.dtype,
)
self.visual_token_mask = torch.isin(input_ids, visual_token_ids_tensor).reshape(
-1, 1
)
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
def iter_mm_grid_thw(
self, mm_features: list[MultiModalFeatureSpec]
) -> Iterator[tuple[int, int, int, int]]:
spatial_conv_size = self.config.spatial_conv_size
temporal_conv_size = self.config.temporal_conv_size
for mm_feature in sorted(mm_features, key=lambda f: f.mm_position.offset):
if mm_feature.data is None:
raise ValueError("M-RoPE calculation requires multimodal feature data")
offset = mm_feature.mm_position.offset
if mm_feature.modality == "image":
grid_thw = mm_feature.data["image_grid_thw"].data
assert isinstance(grid_thw, torch.Tensor)
t, h, w = grid_thw.tolist()
yield offset, t, h // spatial_conv_size, w // spatial_conv_size
elif mm_feature.modality == "video":
grid_thw = mm_feature.data["video_grid_thw"].data
assert isinstance(grid_thw, torch.Tensor)
t, h, w = grid_thw.tolist()
yield (
offset,
t // temporal_conv_size,
h // spatial_conv_size,
w // spatial_conv_size,
)
else:
raise ValueError(f"Unsupported modality: {mm_feature.modality}")
def _parse_and_validate_image_input(
self, **kwargs: object
) -> Ernie4_5_VLImageInputs | None:
pixel_values = kwargs.pop("pixel_values", None)
image_grid_thw = kwargs.pop("image_grid_thw", None)
if pixel_values is None:
return None
return Ernie4_5_VLImagePixelInputs(
type="pixel_values",
pixel_values=pixel_values,
image_grid_thw=image_grid_thw,
)
def _parse_and_validate_video_input(
self, **kwargs: object
) -> Ernie4_5_VLVideoInputs | None:
pixel_values_videos = kwargs.pop("pixel_values_videos", None)
video_grid_thw = kwargs.pop("video_grid_thw", None)
if pixel_values_videos is None:
return None
return Ernie4_5_VLVideoPixelInputs(
type="pixel_values_videos",
pixel_values_videos=pixel_values_videos,
video_grid_thw=video_grid_thw,
)
# -- SupportsEncoderCudaGraph protocol methods --
#
# Only the vision transformer (self.vision_model) is captured into the
# CUDA graph. The VariableResolutionResamplerModel (spatial merge +
# projection) runs eagerly in encoder_eager_forward / postprocess_
# encoder_output because its temporal path performs host-side (numpy)
# indexing that cannot be captured. Image only: video uses a temporal
# conv that changes the output token count, so it falls back to the
# eager multimodal path for now.
def get_encoder_cudagraph_config(self):
from vllm.v1.worker.encoder_cudagraph_defs import EncoderCudaGraphConfig
return EncoderCudaGraphConfig(
modalities=["image"],
# Ernie consumes a single rotary freqs tensor (not cos/sin)
buffer_keys=[
"pixel_values",
"rotary_pos_emb",
"cu_seqlens",
"max_seqlen",
],
# Post-merge embeddings, produced in postprocess_encoder_output,
# are at the LM hidden dim, used only for DP gather sizing.
out_hidden_size=self.config.hidden_size,
)
def get_encoder_cudagraph_budget_range(self, vllm_config) -> tuple[int, int]:
# Min: a 224x224 image -> 16x16 patches (patch_size=14),
# spatial_merge_size=2 -> 8x8 = 64 output tokens.
min_budget = 64
max_budget = min(
vllm_config.scheduler_config.max_num_batched_tokens,
vllm_config.model_config.max_model_len,
)
return (min_budget, max_budget)
def get_encoder_cudagraph_item_specs(self, mm_kwargs: dict[str, Any]):
from vllm.v1.worker.encoder_cudagraph_defs import EncoderItemSpec
m = self.vision_model.spatial_merge_size
grid_thw = mm_kwargs["image_grid_thw"].tolist()
return [
EncoderItemSpec(
input_size=t * h * w,
output_tokens=(t * h * w) // m // m,
)
for t, h, w in grid_thw
]
def select_encoder_cudagraph_items(
self, mm_kwargs: dict[str, Any], indices: list[int]
) -> dict[str, Any]:
grid_thw = mm_kwargs["image_grid_thw"]
pixel_values = mm_kwargs["pixel_values"]
if len(indices) == 0:
return {"pixel_values": pixel_values[:0], "image_grid_thw": grid_thw[:0]}
# Cumulative patch offsets for slicing the concatenated pixel_values.
patches_per_item = (grid_thw[:, 0] * grid_thw[:, 1] * grid_thw[:, 2]).tolist()
cum_patches = [0]
for p in patches_per_item:
cum_patches.append(cum_patches[-1] + p)
selected_pv = torch.cat(
[pixel_values[cum_patches[i] : cum_patches[i + 1]] for i in indices]
)
return {"pixel_values": selected_pv, "image_grid_thw": grid_thw[indices]}
def prepare_encoder_cudagraph_capture_inputs(
self,
token_budget,
max_batch_size,
max_frames_per_batch,
device,
dtype,
path: str = "default",
axis_keys: tuple[Hashable, ...] | None = None,
):
from vllm.v1.worker.encoder_cudagraph_defs import (
EncoderCudaGraphCaptureInputs,
)
m = self.vision_model.spatial_merge_size
# Ceil so the buffer fits the worst case of one item using the full
# budget.
per_mm_item_output = (token_budget + max_batch_size - 1) // max_batch_size
# Image-format grid (T=1): h=m, w=per_mm_item_output*m, so the merged
# token count per item equals per_mm_item_output.
grid_config = [[1, m, per_mm_item_output * m] for _ in range(max_batch_size)]
patch_embed = self.vision_model.patch_embed
in_channels = patch_embed.in_channels
patch_size = patch_embed.patch_size
total_patches = sum(t * h * w for t, h, w in grid_config)
flattened_patch_size = in_channels * patch_size * patch_size
dummy_pixel_values = torch.randn(
total_patches, flattened_patch_size, device=device, dtype=dtype
)
# max_seqlen is baked at capture: worst case is one item consuming the
# full budget - seq_len = token_budget * spatial_merge_size**2.
metadata = self.vision_model.prepare_encoder_metadata(
grid_config,
max_batch_size=max_batch_size,
max_seqlen_override=token_budget * (m**2),
device=device,
)
values = metadata | {"pixel_values": dummy_pixel_values}
return EncoderCudaGraphCaptureInputs(values=values)
def prepare_encoder_cudagraph_replay_buffers(
self, mm_kwargs, max_batch_size, max_frames_per_batch, path: str = "default"
):
from vllm.v1.worker.encoder_cudagraph_defs import (
EncoderCudaGraphReplayBuffers,
)
# The per-image grids are needed as Python ints to size the buffers.
with gpu_sync_allowed():
grid_thw_list = mm_kwargs["image_grid_thw"].tolist()
metadata = self.vision_model.prepare_encoder_metadata(
grid_thw_list, max_batch_size=max_batch_size
)
values = metadata | {
"pixel_values": mm_kwargs["pixel_values"],
}
return EncoderCudaGraphReplayBuffers(values=values)
def encoder_cudagraph_forward(
self, values: dict[str, torch.Tensor], path: str = "default"
) -> torch.Tensor:
# Graph captures the ViT only, and the resampler runs in
# postprocess_encoder_output.
pixel_values = values.pop("pixel_values")
return self.vision_model(pixel_values, encoder_metadata=values)
def encoder_eager_forward(
self, mm_kwargs: dict[str, Any], path: str = "default"
) -> torch.Tensor:
# Eager fallback: run the full pipeline (ViT + resampler). The result
# is scattered directly, so it must be the post-merge embeddings.
pixel_values = mm_kwargs["pixel_values"].type(self.vision_model.dtype)
grid_thw = async_tensor_h2d(
mm_kwargs["image_grid_thw"], self.vision_model.device
)
image_features = self.vision_model(pixel_values, grid_thw)
return self.resampler_model(image_features, grid_thw)
def postprocess_encoder_output(
self,
outputs: dict[str, torch.Tensor],
indices: list[int],
per_item_out_tokens: list[int],
dest,
clone: bool = False,
batch_mm_kwargs: dict[str, Any] | None = None,
) -> None:
# The graph output is the raw ViT features (pre-merge), padded to the
# token budget. Run the resampler eagerly on the valid portion using
# the actual batch grid_thw, then scatter the post-merge embeddings.
# Ernie only uses the single "default" encoder path.
output = outputs["default"]
assert batch_mm_kwargs is not None
grid_thw_cpu = batch_mm_kwargs["image_grid_thw"]
grid_thw = async_tensor_h2d(grid_thw_cpu, output.device)
# The valid token count slices the graph output for the eager
# resampler call, so it has to come back to the host.
num_valid = int(
(grid_thw_cpu[:, 0] * grid_thw_cpu[:, 1] * grid_thw_cpu[:, 2]).sum()
)
image_embeds = self.resampler_model(output[:num_valid], grid_thw)
scatter_output_slices(image_embeds, indices, per_item_out_tokens, dest, clone)
def _process_image_input(
self, image_input: Ernie4_5_VLImageInputs
) -> tuple[torch.Tensor, ...]:
grid_thw = image_input["image_grid_thw"]
assert grid_thw.ndim == 2
pixel_values = image_input["pixel_values"].type(self.vision_model.dtype)
image_features = self._vision_forward(
pixel_values=pixel_values, grid_thw=grid_thw
)
image_embeds = self.resampler_model(image_features, grid_thw)
merge_size = self.vision_model.spatial_merge_size
sizes = grid_thw.prod(-1) // merge_size // merge_size
return image_embeds.split(sizes.tolist())
def _process_video_input(
self, video_input: Ernie4_5_VLVideoInputs
) -> tuple[torch.Tensor, ...]:
grid_thw = video_input["video_grid_thw"]
assert grid_thw.ndim == 2
pixel_values_videos = video_input["pixel_values_videos"].type(
self.vision_model.dtype
)
video_features = self._vision_forward(
pixel_values=pixel_values_videos, grid_thw=grid_thw
)
video_embeds = self.resampler_model(video_features, grid_thw)
merge_size = self.vision_model.spatial_merge_size
sizes = (
(grid_thw.prod(-1) // self.config.temporal_conv_size)
// merge_size
// merge_size
)
return video_embeds.split(sizes.tolist())
def _parse_and_validate_multimodal_inputs(self, **kwargs: object) -> dict:
modalities: dict[
str, Ernie4_5_VLImageInputs | Ernie4_5_VLVideoInputs | None
] = {}
# Preserve the order of modalities if there are multiple of them
# from the order of kwargs.
for input_key in kwargs:
if (
input_key in ("pixel_values", "image_embeds")
and "images" not in modalities
):
modalities["images"] = self._parse_and_validate_image_input(**kwargs)
if (
input_key in ("pixel_values_videos", "video_embeds")
and "videos" not in modalities
):
modalities["videos"] = self._parse_and_validate_video_input(**kwargs)
return modalities
def embed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings | None:
modalities = self._parse_and_validate_multimodal_inputs(**kwargs)
if not modalities:
return None
# The result multimodal_embeddings is tuple of tensors, with each
# tensor corresponding to a multimodal data item (image or video).
multimodal_embeddings: tuple[torch.Tensor, ...] = ()
# NOTE: It is important to iterate over the keys in this dictionary
# to preserve the order of the modalities.
for modality in modalities:
if modality == "images":
image_input = modalities["images"]
image_embeddings = self._process_image_input(image_input)
multimodal_embeddings += tuple(image_embeddings)
if modality == "videos":
video_input = modalities["videos"]
video_embeddings = self._process_video_input(video_input)
multimodal_embeddings += tuple(video_embeddings)
return multimodal_embeddings
def embed_input_ids(
self,
input_ids: torch.Tensor,
multimodal_embeddings: MultiModalEmbeddings | None = None,
*,
is_multimodal: torch.Tensor | None = None,
) -> torch.Tensor:
if multimodal_embeddings is not None and len(multimodal_embeddings) > 0:
self._set_visual_token_mask(input_ids)
# This is to satisfy the type checker for each overload
if multimodal_embeddings is None or is_multimodal is None:
return super().embed_input_ids(input_ids)
return super().embed_input_ids(
input_ids,
multimodal_embeddings=multimodal_embeddings,
is_multimodal=is_multimodal,
)
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
**kwargs,
):
forward_kwargs = {
"input_ids": input_ids,
"positions": positions,
"intermediate_tensors": intermediate_tensors,
"inputs_embeds": inputs_embeds,
}
if self.visual_token_mask is not None:
if self.visual_token_mask.shape[0] != inputs_embeds.shape[0]:
padding_len = inputs_embeds.shape[0] - self.visual_token_mask.shape[0]
# right pad False
pad = torch.zeros(
(padding_len, self.visual_token_mask.shape[1]),
dtype=self.visual_token_mask.dtype,
device=self.visual_token_mask.device,
)
self.visual_token_mask = torch.cat([self.visual_token_mask, pad], dim=0)
forward_kwargs.update({"visual_token_mask": self.visual_token_mask})
self.visual_token_mask = None
hidden_states = self.language_model.model(
**forward_kwargs,
**kwargs,
)
return hidden_states
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
loader = AutoWeightsLoader(self)
return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
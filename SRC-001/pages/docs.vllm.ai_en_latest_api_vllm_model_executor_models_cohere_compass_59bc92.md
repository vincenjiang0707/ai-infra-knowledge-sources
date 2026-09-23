source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/cohere_compass/
lastmod: 2026-09-23

@MULTIMODAL_REGISTRY.register_processor(
CohereCompassMultiModalProcessor,
info=CohereCompassProcessingInfo,
dummy_inputs=CohereCompassDummyInputsBuilder,
)
class CohereCompassForConditionalGeneration(
nn.Module,
SupportsMultiModal,
SupportsEncoderCudaGraph,
SupportsLoRA,
SupportsPP,
SupportsMRoPE,
SupportsEagle,
SupportsEagle3,
SupportsMultiModalPruning,
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
"qkv": ["qkv"], # For vision tower's already-packed QKV
}
supports_encoder_tp_data = True
# To ensure correct weight loading and mapping.
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_prefix={
"model.visual.": "visual.",
"lm_head.": "language_model.lm_head.",
"model.language_model.": "language_model.model.",
}
)
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("image"):
return "<|VISION_START|><|IMAGE_PAD|><|VISION_END|>"
raise ValueError("Only image modality is supported")
def __init__(self, *, vllm_config: VllmConfig, prefix: str = "model"):
nn.Module.__init__(self)
config = vllm_config.model_config.hf_config
quant_config = vllm_config.quant_config
multimodal_config = vllm_config.model_config.multimodal_config
self.config = config
self.model_config = vllm_config.model_config
self._tokenizer = cached_tokenizer_from_config(vllm_config.model_config)
self.multimodal_config = multimodal_config
assert multimodal_config is not None
self.use_data_parallel = multimodal_config.mm_encoder_tp_mode == "data"
self.is_multimodal_pruning_enabled = (
multimodal_config.is_multimodal_pruning_enabled()
)
self.use_deepstack = bool(config.vision_config.deepstack_visual_indexes)
self.deepstack_num_level = len(config.vision_config.deepstack_visual_indexes)
self.visual_dim = config.vision_config.out_hidden_size
self.multiscale_dim = self.visual_dim * self.deepstack_num_level
with self._mark_tower_model(vllm_config, {"image"}):
self.visual = Cohere_VisionTransformer(
config.vision_config,
norm_eps=1e-6,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "visual"),
)
if self.use_deepstack:
self.deepstack_input_embeds = [
torch.zeros(
vllm_config.scheduler_config.max_num_batched_tokens,
config.text_config.hidden_size,
)
for _ in range(self.deepstack_num_level)
]
self.deepstack_input_embeds_num_tokens = 0
with self._mark_language_model(vllm_config):
self.language_model = CohereCompassForCausalLM(
vllm_config=vllm_config.with_hf_config(config.text_config),
prefix=maybe_prefix(prefix, "language_model"),
)
if not get_pp_group().is_first_rank and self.use_deepstack:
assert self.language_model.model.start_layer >= self.deepstack_num_level
self.make_empty_intermediate_tensors = (
self.language_model.make_empty_intermediate_tensors
)
def iter_mm_grid_thw(
self, mm_features: list[MultiModalFeatureSpec]
) -> Iterator[tuple[int, int, int, int, float]]:
spatial_merge_size = self.config.vision_config.spatial_merge_size
for mm_feature in sorted(mm_features, key=lambda f: f.mm_position.offset):
if mm_feature.modality != "image":
raise ValueError(f"Unsupported modality: {mm_feature.modality}")
offset = mm_feature.mm_position.offset
feature_data = mm_feature.data
assert feature_data is not None
grid_item = feature_data.get("image_grid_thw")
assert grid_item is not None
grid_data = grid_item.data
assert isinstance(grid_data, torch.Tensor)
t, h, w = grid_data.tolist()
assert t == 1, f"Image must have 1 frame, got {t}"
yield offset, 1, h // spatial_merge_size, w // spatial_merge_size, 1.0
def _get_deepstack_input_embeds(
self,
num_tokens: int,
) -> IntermediateTensors | None:
if not getattr(self, "deepstack_input_embeds", None):
return None # If vision tower is skipped
if num_tokens > self.deepstack_input_embeds[0].size(0):
self._resize_deepstack_input_embeds(num_tokens)
# get deepstack_input_embeds from buffer, and clear the buffer
return IntermediateTensors(
{
f"deepstack_input_embeds_{idx}": self.deepstack_input_embeds[idx][
:num_tokens
]
for idx in range(self.deepstack_num_level)
}
)
def _resize_deepstack_input_embeds(self, num_tokens: int) -> None:
self.deepstack_input_embeds = [
torch.zeros(
num_tokens,
self.config.text_config.hidden_size,
device=self.deepstack_input_embeds[0].device,
dtype=self.deepstack_input_embeds[0].dtype,
)
for _ in range(self.deepstack_num_level)
]
def _set_deepstack_input_embeds(self, deepstack_input_embeds: torch.Tensor) -> None:
if not getattr(self, "deepstack_input_embeds", None):
return
# set deepstack_input_embeds to buffer
num_tokens = deepstack_input_embeds.size(1)
if num_tokens > self.deepstack_input_embeds[0].size(0):
self._resize_deepstack_input_embeds(num_tokens)
for idx in range(self.deepstack_num_level):
self.deepstack_input_embeds[idx][:num_tokens].copy_(
deepstack_input_embeds[idx]
)
self.deepstack_input_embeds_num_tokens = num_tokens
def _clear_deepstack_input_embeds(self, num_tokens: int) -> None:
if not getattr(self, "deepstack_input_embeds", None):
return
if getattr(self, "deepstack_input_embeds_num_tokens", 0) == 0:
return
# clear deepstack_input_embeds in buffer
if num_tokens > 0:
for idx in range(self.deepstack_num_level):
self.deepstack_input_embeds[idx][:num_tokens].zero_()
self.deepstack_input_embeds_num_tokens = 0
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
modalities = [] if self.is_multimodal_pruning_enabled else ["image"]
# Compute max_frames_per_video for budget sizing.
max_frames = 1
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
raise AssertionError("This line should be unreachable.")
def get_encoder_cudagraph_budget_range(
self,
vllm_config,
) -> tuple[int, int]:
# Min: estimated smallest possible encoder input.
# 224x224 image → 16x16 patches (patch_size=14)
# spatial_merge_size=2 → 8x8 = 64 tokens
min_budget = 64
# Max: capped by max_num_batched_tokens
# TODO(shen-shanshan): the max_budget auto-infer needs to be optimized later.
max_budget = min(
vllm_config.scheduler_config.max_num_batched_tokens,
self.model_config.max_model_len,
)
return (min_budget, max_budget)
def _get_pixel_values_by_modality(
self,
mm_kwargs: dict[str, Any],
) -> torch.Tensor:
modality = self.get_input_modality(mm_kwargs)
if modality == "image":
return mm_kwargs["pixel_values"]
raise AssertionError("This line should be unreachable.")
def _get_grid_thw_by_modality(
self,
mm_kwargs: dict[str, Any],
) -> list[list[int]]:
grid_thw_key = f"{self.get_input_modality(mm_kwargs)}_grid_thw"
grid_thw = mm_kwargs[grid_thw_key]
if not isinstance(grid_thw, list):
grid_thw = grid_thw.tolist()
return grid_thw
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
return {
"pixel_values": pixel_values[:0],
"image_grid_thw": [],
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
return {
"pixel_values": selected_pv,
"image_grid_thw": selected_grid,
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
# Ceil so the buffer fits the worst case of one item using the full
# budget. Floor under-allocates when budget is not a multiple of
# max_batch_size.
per_mm_item_output = (token_budget + max_batch_size - 1) // max_batch_size
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
# Just use image-modality dummy input_buffer for capturing
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
) -> EncoderCudaGraphReplayBuffers:
modality = self.get_input_modality(mm_kwargs)
grid_thw_list = self._get_grid_thw_by_modality(mm_kwargs)
if modality == "image":
metadata = self.visual.prepare_encoder_metadata(
grid_thw_list,
max_batch_size=max_batch_size,
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
def _parse_and_validate_image_input(
self, **kwargs: object
) -> Cohere_VLImageInputs | None:
pixel_values = kwargs.pop("pixel_values", None)
image_embeds = kwargs.pop("image_embeds", None)
image_grid_thw = kwargs.pop("image_grid_thw", None)
if pixel_values is None and image_embeds is None:
return None
if pixel_values is not None:
return Cohere_VLImagePixelInputs(
type="pixel_values",
pixel_values=pixel_values,
image_grid_thw=image_grid_thw,
)
if image_embeds is not None:
return Cohere_VLImageEmbeddingInputs(
type="image_embeds",
image_embeds=image_embeds,
image_grid_thw=image_grid_thw,
)
raise AssertionError("image input must contain pixels or embeddings")
def _process_image_input(
self, image_input: Cohere_VLImageInputs
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
# Split concatenated embeddings for each image item.
merge_size = self.visual.spatial_merge_size
sizes = (grid_thw.prod(-1) // merge_size // merge_size).tolist()
return image_embeds.split(sizes)
def _postprocess_image_embeds_evs(
self,
image_embeds_split: tuple[torch.Tensor, ...],
image_input: Cohere_VLImageInputs,
) -> tuple[torch.Tensor, ...]:
"""Append mrope positions for each for images.
This is necessary to recover correct mrope positions
Args:
image_embeds_split: Tuple of image embeddings for
each image item.
image_input: Image input data.
Returns:
Tuple of image embeddings for each image item.
Resulting embeddings will have extra 5 channels for
computed mrope positions, consistent with video embeddings.
"""
if self.is_multimodal_pruning_enabled:
merge_size = self.visual.spatial_merge_size
grid_thw = image_input["image_grid_thw"]
grid_thw_list = grid_thw.tolist()
image_embeds_out = []
for emb, size in zip(image_embeds_split, grid_thw_list):
positions = compute_mrope_for_media(size, merge_size).to(
emb.device, non_blocking=True
)
positions = torch.cat(
[
positions,
torch.zeros_like(
positions[:, 0:1]
), # Dummy extra fifth channel
],
dim=1,
)
emb = torch.cat([emb, positions], dim=1)
image_embeds_out.append(emb)
image_embeds_split = tuple(image_embeds_out)
return image_embeds_split
def _parse_and_validate_multimodal_inputs(self, **kwargs: object) -> dict:
mm_input_by_modality = {}
for input_key in kwargs:
if (
input_key in ("pixel_values", "image_embeds")
and "image" not in mm_input_by_modality
):
mm_input_by_modality["image"] = self._parse_and_validate_image_input(
**kwargs
)
return mm_input_by_modality
def get_mrope_input_positions(
self,
input_tokens: list[int],
mm_features: list[MultiModalFeatureSpec],
) -> tuple[torch.Tensor, int]:
llm_pos_ids_list: list[np.ndarray] = []
st = 0
for (
offset,
llm_grid_t,
llm_grid_h,
llm_grid_w,
_,
) in self.iter_mm_grid_thw(mm_features):
text_len = offset - st
st_idx = llm_pos_ids_list[-1].max() + 1 if llm_pos_ids_list else 0
llm_pos_ids_list.append(
np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
)
grid_indices = np.indices((llm_grid_t, llm_grid_h, llm_grid_w)).reshape(
3, -1
)
llm_pos_ids_list.append(grid_indices + text_len + st_idx)
st = offset + llm_grid_t * llm_grid_h * llm_grid_w
if st < len(input_tokens):
st_idx = llm_pos_ids_list[-1].max() + 1 if llm_pos_ids_list else 0
text_len = len(input_tokens) - st
llm_pos_ids_list.append(
np.broadcast_to(np.arange(text_len), (3, text_len)) + st_idx
)
llm_positions = np.concatenate(llm_pos_ids_list, axis=1).reshape(3, -1)
mrope_position_delta = (llm_positions.max() + 1 - len(input_tokens)).item()
return torch.from_numpy(llm_positions), mrope_position_delta
def recompute_mrope_positions(
self,
input_ids: list[int],
multimodal_embeddings: MultiModalEmbeddings,
mrope_positions: torch.LongTensor,
num_computed_tokens: int,
) -> tuple[MultiModalEmbeddings, torch.Tensor, int]:
"""Update part of input mrope positions (starting with
num_computed_tokens index). Original mrope_positions are computed
for unpruned sequence and becomes incorrect once pruning occurs,
so once we prune media tokens we should reflect this in the
mrope_positions before we feed it to LLM.
Args:
input_ids: (N,) All input tokens of the prompt containing
entire sequence.
multimodal_embeddings: Tuple of multimodal embeddings that
fits into the prefill chunk that is being processed.
mrope_positions: Existing mrope positions (3, N) for entire
sequence
num_computed_tokens: A number of computed tokens so far.
Returns:
Tuple of (multimodal_embeddings, mrope_positions,
mrope_position_delta).
"""
return self._recompute_mrope_positions(
input_ids=input_ids,
multimodal_embeddings=multimodal_embeddings,
mrope_positions=mrope_positions,
num_computed_tokens=num_computed_tokens,
image_token_id=self.config.image_token_id,
video_token_id=self.config.video_token_id,
vision_start_token_id=self.config.vision_start_token_id,
)
@staticmethod
def _recompute_mrope_positions(
input_ids: list[int],
multimodal_embeddings: MultiModalEmbeddings,
mrope_positions: torch.LongTensor,
num_computed_tokens: int,
vision_start_token_id: int,
image_token_id: int,
video_token_id: int,
) -> tuple[MultiModalEmbeddings, torch.Tensor, int]:
# Device
device = (
multimodal_embeddings[0].device
if len(multimodal_embeddings)
else mrope_positions.device
)
# Tensors
input_ids_t = async_tensor_h2d(input_ids, device=device, dtype=torch.long)
mm_embeddings_out = []
mm_embeddings_pos = []
# Strip position information from embeddings (last 5 channels)
# For Cohere VL, handle potentially empty frames (from unpacking)
for mm in multimodal_embeddings:
if mm.shape[0] > 0: # Only process non-empty frames
mm_embeddings_out.append(mm[:, :-5])
mm_embeddings_pos.append(mm[:, -5:].permute(1, 0).long())
else:
# Empty frame - keep as is
mm_embeddings_out.append(mm)
# Create empty position tensor with correct shape
mm_embeddings_pos.append(
torch.empty(5, 0, device=device, dtype=torch.long)
)
positions, mrope_positions_delta = recompute_mrope_positions(
input_ids_t,
mm_embeddings_pos,
mrope_positions,
num_computed_tokens,
vision_start_token_id,
image_token_id,
video_token_id,
)
return tuple(mm_embeddings_out), positions, mrope_positions_delta
def embed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings | None:
mm_input_by_modality = self._parse_and_validate_multimodal_inputs(**kwargs)
if not mm_input_by_modality:
return None
# The result multimodal_embeddings is tuple of tensors, with each
# tensor corresponding to a multimodal data item (image).
multimodal_embeddings: list[torch.Tensor] = []
# NOTE: It is important to iterate over the keys in this dictionary
# to preserve the order of the modalities.
for modality in mm_input_by_modality:
multimodal_input = mm_input_by_modality[modality]
if modality == "image":
image_embeddings = self._process_image_input(multimodal_input)
image_embeddings = self._postprocess_image_embeds_evs(
image_embeddings, multimodal_input
)
multimodal_embeddings.extend(image_embeddings)
embeddings_tuple = tuple(multimodal_embeddings)
return embeddings_tuple
def _compute_deepstack_embeds(
self,
inputs_embeds: torch.Tensor,
multimodal_embeddings: MultiModalEmbeddings,
is_multimodal: torch.Tensor,
) -> tuple[torch.Tensor, MultiModalEmbeddings]:
visual_lens = [len(x) for x in multimodal_embeddings]
multimodal_embeddings_cat = torch.cat(multimodal_embeddings, dim=0)
(
multimodal_embeddings_main,
multimodal_embeddings_multiscale,
) = torch.split(
multimodal_embeddings_cat,
[self.visual_dim, self.multiscale_dim],
dim=-1,
)
multimodal_embeddings = torch.split(
multimodal_embeddings_main, visual_lens, dim=0
)
multimodal_embeddings_multiscale = torch.split(
multimodal_embeddings_multiscale, visual_lens, dim=0
)
deepstack_input_embeds = inputs_embeds.new_zeros(
inputs_embeds.size(0), self.deepstack_num_level * inputs_embeds.size(1)
)
deepstack_input_embeds = _merge_multimodal_embeddings(
inputs_embeds=deepstack_input_embeds,
multimodal_embeddings=multimodal_embeddings_multiscale,
is_multimodal=is_multimodal,
)
deepstack_input_embeds = deepstack_input_embeds.view(
inputs_embeds.shape[0], self.deepstack_num_level, self.visual_dim
)
deepstack_input_embeds = deepstack_input_embeds.permute(1, 0, 2)
return deepstack_input_embeds, multimodal_embeddings
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
is_multimodal = _require_is_multimodal(is_multimodal)
if self.use_deepstack:
(
deepstack_input_embeds,
multimodal_embeddings,
) = self._compute_deepstack_embeds(
inputs_embeds=inputs_embeds,
multimodal_embeddings=multimodal_embeddings,
is_multimodal=is_multimodal,
)
else:
deepstack_input_embeds = None
inputs_embeds = _merge_multimodal_embeddings(
inputs_embeds=inputs_embeds,
multimodal_embeddings=multimodal_embeddings,
is_multimodal=is_multimodal,
)
if deepstack_input_embeds is not None:
self._set_deepstack_input_embeds(deepstack_input_embeds)
return inputs_embeds
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
**kwargs: object,
) -> torch.Tensor | IntermediateTensors:
"""Run forward pass for Cohere Compass.
Args:
input_ids: Flattened (concatenated) input_ids corresponding to a
batch.
positions: Flattened (concatenated) position ids corresponding to a
batch.
**NOTE**: If mrope is enabled (default setting for Cohere Compass
opensource models), the shape will be `(3, seq_len)`,
otherwise it will be `(seq_len,).
intermediate_tensors: Intermediate tensors from previous pipeline
stages.
inputs_embeds: Pre-computed input embeddings.
**kwargs: Additional keyword arguments including:
- pixel_values: Pixel values to be fed to a model.
`None` if no images are passed.
- image_grid_thw: Tensor `(n_images, 3)` of image 3D grid in
LLM. `None` if no images are passed.
"""
if intermediate_tensors is not None:
inputs_embeds = None
if inputs_embeds is not None and get_pp_group().is_first_rank:
deepstack_input_embeds = self._get_deepstack_input_embeds(
inputs_embeds.size(0)
)
else:
deepstack_input_embeds = None
hidden_states = self.language_model.model(
input_ids=input_ids,
positions=positions,
intermediate_tensors=intermediate_tensors,
inputs_embeds=inputs_embeds,
# args for deepstack
deepstack_input_embeds=deepstack_input_embeds,
)
if inputs_embeds is not None and get_pp_group().is_first_rank:
self._clear_deepstack_input_embeds(inputs_embeds.size(0))
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
"""Get the module prefix in multimodal models"""
return MultiModelKeys.from_string_field(
language_model="language_model",
connector=["visual.merger", "visual.deepstack_merger_list"],
tower_model="visual.",
)
def get_num_mm_encoder_tokens(
self,
num_image_tokens: int,
) -> int:
hf_config = self.config
vision_config = hf_config.vision_config
merge_size = vision_config.spatial_merge_size
return num_image_tokens * merge_size**2
def get_num_mm_connector_tokens(
self,
num_vision_tokens: int,
) -> int:
hf_config = self.config
vision_config = hf_config.vision_config
merge_size = vision_config.spatial_merge_size
return num_vision_tokens // merge_size**2
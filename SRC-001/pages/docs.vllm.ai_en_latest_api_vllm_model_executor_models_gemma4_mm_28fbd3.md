source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gemma4_mm/
lastmod: 2026-09-23

@MULTIMODAL_REGISTRY.register_processor(
Gemma4MultiModalProcessor,
info=Gemma4ProcessingInfo,
dummy_inputs=Gemma4DummyInputsBuilder,
)
class Gemma4ForConditionalGeneration(
nn.Module,
SupportsMultiModal,
SupportsQuant,
SupportsPP,
SupportsLoRA,
SupportsEagle3,
SupportsEncoderCudaGraph,
):
supports_encoder_cudagraph: ClassVar[Literal[True]] = True
# Gemma4 clamps mm_prefix bidirectional ranges to the sliding window
# in-kernel (HF's (causal OR blockwise) AND sliding_window). The model
# runner reads this to keep image bidirectional ranges that exceed the
# window instead of dropping them (which would make image attention
# causal-only for images larger than the sliding window).
mm_prefix_clamp_sliding_window: bool = True
supports_tower_connector_lora = True
packed_modules_mapping: dict[str, list[str]] = {
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
# Maps checkpoint prefixes to vLLM module paths.
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_prefix={
# vision tower
"model.vision_tower": "vision_tower",
"model.embed_vision": "embed_vision",
# audio tower
"model.audio_tower.": "audio_tower.",
"model.embed_audio.": "embed_audio.",
# backbone
"model.language_model.": "language_model.model.",
"lm_head.": "language_model.lm_head.",
"model": "language_model.model",
},
)
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
config = vllm_config.model_config.hf_config
quant_config = vllm_config.quant_config
multimodal_config = vllm_config.model_config.multimodal_config
self.config = config
self.quant_config = quant_config
self.multimodal_config = multimodal_config
self.model_dtype = vllm_config.model_config.dtype
self.vllm_config = vllm_config
lora_config = vllm_config.lora_config
self._enable_mm_lora = bool(
lora_config is not None and lora_config.enable_tower_connector_lora
)
# Only quantize towers when the quant method supports their
# dimensions. BNB/torchao handle arbitrary sizes; other methods
# (Marlin, FP8, …) require dimensions divisible by 64, which
# the vision tower (intermediate_size=4304) does not satisfy.
# TODO(mgoin): remove this by fixing kernel padding.
tower_quant: QuantizationConfig | None
if quant_config and quant_config.get_name() in [
"bitsandbytes",
"torchao",
"compressed-tensors",
]:
tower_quant = quant_config
else:
vision_cfg = config.vision_config
quantizable = (
vision_cfg.hidden_size % 64 == 0
and vision_cfg.intermediate_size % 64 == 0
)
tower_quant = quant_config if quantizable else None
# ---- Vision tower (shared by image and video) ----
with self._mark_tower_model(vllm_config, {"image", "video"}):
self.vision_tower = AutoModel.from_config(config=config.vision_config)
self.embed_vision = Gemma4MultimodalEmbedder(
config.vision_config,
config.text_config,
quant_config=tower_quant,
prefix=maybe_prefix(prefix, "embed_vision"),
)
recursive_replace_linear(
self.vision_tower,
tower_quant,
prefix=maybe_prefix(prefix, "vision_tower"),
)
# ---- Audio tower (variants with audio_config) ----
self.embed_audio: Gemma4MultimodalEmbedder | None
if config.audio_config is not None:
with self._mark_tower_model(vllm_config, "audio"):
self.audio_tower = AutoModel.from_config(config=config.audio_config)
# AutoModel.from_config does NOT call post_init(),
# which is needed to initialize buffers that are absent
# from the checkpoint (e.g. inv_timescales for relative
# position embeddings, softcap, gradient_clipping).
self.audio_tower.post_init()
self.embed_audio = Gemma4MultimodalEmbedder(
config.audio_config,
config.text_config,
quant_config=tower_quant,
prefix=maybe_prefix(prefix, "embed_audio"),
)
recursive_replace_linear(
self.audio_tower,
tower_quant,
prefix=maybe_prefix(prefix, "audio_tower"),
)
else:
self.audio_tower = None
self.embed_audio = None
# ---- Language model (vLLM optimised) ----
with self._mark_language_model(vllm_config):
self.language_model: Gemma4ForCausalLM = init_vllm_registered_model(
vllm_config=vllm_config,
hf_config=config.text_config,
prefix=maybe_prefix(prefix, "language_model"),
architectures=["Gemma4ForCausalLM"],
)
# Pre-allocate PLE buffer for CUDA graph compatibility.
# Some variants have hidden_size_per_layer_input=None (no PLE).
ple_dim = config.text_config.hidden_size_per_layer_input
if ple_dim is not None and ple_dim > 0:
embed = self.language_model.model.embed_tokens
self.per_layer_embeddings = torch.zeros(
vllm_config.scheduler_config.max_num_batched_tokens,
config.text_config.num_hidden_layers,
ple_dim,
device=next(embed.parameters()).device,
dtype=vllm_config.model_config.dtype,
)
else:
self.per_layer_embeddings = None
self.make_empty_intermediate_tensors = (
self.language_model.make_empty_intermediate_tensors
)
# --- Precompute full-attention layer indices for bidi clearing ---
self._full_attn_layer_idxs: frozenset[int] = frozenset()
text_config = config.text_config
if getattr(text_config, "use_bidirectional_attention", None) == "vision":
layer_types = getattr(text_config, "layer_types", None)
if layer_types:
self._full_attn_layer_idxs = frozenset(
i for i, lt in enumerate(layer_types) if lt != "sliding_attention"
)
# --- MixtureOfExperts delegation to language_model ---
self.moe_layers = self.language_model.moe_layers
self.num_moe_layers = self.language_model.num_moe_layers
self.num_logical_experts = self.language_model.num_logical_experts
self.num_physical_experts = self.language_model.num_physical_experts
self.num_local_physical_experts = self.language_model.num_local_physical_experts
self.num_routed_experts = self.language_model.num_routed_experts
self.num_expert_groups = self.language_model.num_expert_groups
self.num_shared_experts = self.language_model.num_shared_experts
self.num_redundant_experts = self.language_model.num_redundant_experts
gen_cfg = vllm_config.model_config.try_get_generation_config()
self._suppress_token_ids = gen_cfg.get("suppress_tokens") if gen_cfg else None
# ------------------------------------------------------------------ #
# Input parsing
# ------------------------------------------------------------------ #
def _parse_and_validate_image_input(
self, **kwargs: object
) -> Gemma4ImageInputs | None:
pixel_values = kwargs.pop("pixel_values", None)
pixel_position_ids = kwargs.pop("pixel_position_ids", None)
image_embeds = kwargs.pop("image_embeds", None)
assert image_embeds is None, "Gemma4 does not support image_embeds."
if pixel_values is None:
return None
return Gemma4ImagePixelInputs(
pixel_values=pixel_values,
pixel_position_ids=pixel_position_ids,
)
def _parse_and_validate_audio_input(
self, **kwargs: object
) -> Gemma4AudioInputs | None:
input_features_padded = kwargs.pop("input_features_padded", None)
if input_features_padded is None:
return None
input_features_mask = kwargs.pop("input_features_mask", None)
if input_features_mask is None:
return None
return Gemma4AudioInputs(
input_features_padded=input_features_padded,
input_features_mask=input_features_mask,
)
def _parse_and_validate_video_input(
self, **kwargs: object
) -> Gemma4VideoInputs | None:
pixel_values_videos = kwargs.pop("pixel_values_videos", None)
pixel_position_ids_videos = kwargs.pop("pixel_position_ids_videos", None)
video_frame_counts = kwargs.pop("video_frame_counts", None)
if pixel_values_videos is None:
return None
return Gemma4VideoInputs(
pixel_values_videos=pixel_values_videos,
pixel_position_ids_videos=pixel_position_ids_videos,
video_frame_counts=video_frame_counts,
)
def _parse_and_validate_multimodal_inputs(
self, **kwargs: object
) -> dict[str, Gemma4ImageInputs | Gemma4AudioInputs | Gemma4VideoInputs | None]:
mm_input_by_modality: dict[
str, Gemma4ImageInputs | Gemma4AudioInputs | Gemma4VideoInputs | None
] = {}
for input_key in list(kwargs):
if (
input_key in ("pixel_values", "image_embeds")
and "image" not in mm_input_by_modality
):
mm_input_by_modality["image"] = self._parse_and_validate_image_input(
**kwargs
)
if (
input_key == "pixel_values_videos"
and "video" not in mm_input_by_modality
):
mm_input_by_modality["video"] = self._parse_and_validate_video_input(
**kwargs
)
if (
input_key == "input_features_padded"
and "audio" not in mm_input_by_modality
):
mm_input_by_modality["audio"] = self._parse_and_validate_audio_input(
**kwargs
)
return mm_input_by_modality
@staticmethod
def _encoder_chunk(
patches_per_item: int,
free_bytes: int,
total_bytes: int,
position_embedding_size: int,
) -> int:
"""Max chunk size whose F.one_hot transient fits in the budget.
The dominant transient inside HF's ``Gemma4VisionPatchEmbedder.
_position_embeddings`` is
``F.one_hot(clamped_positions, num_classes=position_embedding_size)``
with shape ``(chunk, patches, 2, position_embedding_size)``,
int64, plus its simultaneous cast to the position embedding
table dtype. That, not the encoder residual stream, sets peak
memory.
"""
if patches_per_item <= 0:
return 1
# Half of currently-free, capped at 10% of total so we leave room
# for the rest of profile_run / the subsequent encoder + pooler.
budget = min(free_bytes // 2, total_bytes // 10)
if budget <= 0:
return 1
# F.one_hot allocates (chunk, patches, 2, pos_emb_size) int64
# (the inner 2 is the (x, y) coordinate axis, 8 is sizeof(int64)).
# Outer 2x covers the int64 buffer and its concurrent bf16 cast
# plus the matmul output that live alongside it at peak.
cost = patches_per_item * 4 * position_embedding_size * 8
return max(1, budget // cost) if cost > 0 else 1
# ------------------------------------------------------------------ #
# Image processing
# ------------------------------------------------------------------ #
def _process_image_input(
self,
image_input: Gemma4ImageInputs,
) -> list[torch.Tensor]:
"""Batch-encode images through the vision tower.
Groups images by patch count (resolution bucket) so each
encoder call processes a uniform-shape batch with no
cross-resolution padding. With MM LoRA enabled, all images are
padded into one batch so the encoder call matches the tower mapping.
"""
pixel_values = image_input["pixel_values"]
pixel_position_ids = image_input["pixel_position_ids"]
vt = self.vision_tower
vision_cfg = self.config.vision_config
pooling_k2 = vision_cfg.pooling_kernel_size**2
# Concurrent requests with different image resolutions may
# arrive as a list of per-image tensors, while same-resolution
# batches may arrive as a stacked tensor.
buckets: dict[int, list[tuple[int, torch.Tensor, torch.Tensor]]] = {}
total_images = (
len(pixel_values)
if isinstance(pixel_values, list)
else pixel_values.shape[0]
)
pool_position_ids = pixel_position_ids
if self._enable_mm_lora:
max_soft_tokens = vision_cfg.default_output_length
mm_processor_kwargs = getattr(
getattr(self, "multimodal_config", None),
"mm_processor_kwargs",
None,
)
if isinstance(mm_processor_kwargs, Mapping):
value, _ = _get_max_soft_tokens(mm_processor_kwargs)
if isinstance(value, int) and value in _SUPPORTED_SOFT_TOKENS:
max_soft_tokens = value
max_patches = max_soft_tokens * pooling_k2
padded_position_ids: list[torch.Tensor] = []
for idx in range(total_images):
pv = pixel_values[idx]
pp = pixel_position_ids[idx]
num_patches = pv.shape[0]
if num_patches > max_patches:
raise ValueError(
f"Image {idx} has {num_patches} patches, which exceeds "
f"the MM LoRA patch limit of {max_patches}."
)
pad_len = max_patches - num_patches
pv = torch.cat(
(pv, pv.new_zeros((pad_len, *pv.shape[1:]))),
dim=0,
)
pp = torch.cat(
(pp, pp.new_full((pad_len, *pp.shape[1:]), -1)),
dim=0,
)
buckets.setdefault(max_patches, []).append((idx, pv, pp))
padded_position_ids.append(pp)
pool_position_ids = padded_position_ids
else:
for idx in range(total_images):
pv = pixel_values[idx]
pp = pixel_position_ids[idx]
buckets.setdefault(pv.shape[0], []).append((idx, pv, pp))
# Encode each resolution bucket in memory-safe chunks. Re-read
# free memory per bucket because the previous bucket's encoder
# pass has already allocated activations we should account for.
last_hidden_states_map: dict[int, torch.Tensor] = {}
for patches, items in buckets.items():
if self._enable_mm_lora:
max_batch_size = len(items)
else:
free, total = torch.accelerator.get_memory_info()
max_batch_size = min(
len(items),
self._encoder_chunk(
patches, free, total, vision_cfg.position_embedding_size
),
)
for chunk_idx in range(0, len(items), max_batch_size):
chunk_items = items[chunk_idx : chunk_idx + max_batch_size]
pv_tensor = torch.cat(
[item[1].unsqueeze(0) for item in chunk_items], dim=0
)
pp_tensor = torch.cat(
[item[2].unsqueeze(0) for item in chunk_items], dim=0
)
pad_tensor = (pp_tensor == -1).all(dim=-1)
inputs_embeds = vt.patch_embedder(
pv_tensor,
pp_tensor,
pad_tensor,
).to(self.model_dtype)
# HuggingFace's mask builder probes `padding_mask.all()` to
# decide whether the mask can be skipped, which syncs.
with gpu_sync_allowed():
encoder_outputs = vt.encoder(
inputs_embeds=inputs_embeds,
attention_mask=~pad_tensor,
pixel_position_ids=pp_tensor,
)
hidden_states = encoder_outputs.last_hidden_state
for i, (orig_idx, _, _) in enumerate(chunk_items):
last_hidden_states_map[orig_idx] = hidden_states[i]
# Pool per image to strip padding and reduce spatial resolution.
all_valid_states: list[torch.Tensor] = [None] * total_images # type: ignore[list-item]
valid_lens = [0] * total_images
for orig_idx in range(total_images):
chunk_hidden = last_hidden_states_map[orig_idx]
output_length = chunk_hidden.shape[0] // pooling_k2
single_hidden = chunk_hidden.unsqueeze(0)
single_pos_ids = pool_position_ids[orig_idx].unsqueeze(0)
padding_positions = (single_pos_ids == -1).all(dim=-1)
# The pooler goes through HuggingFace's mask builder, which probes
# `padding_mask.all()`, and the mask indexing below needs the
# selected count on the host.
with gpu_sync_allowed():
pooled_states, valid_mask = vt.pooler(
hidden_states=single_hidden,
pixel_position_ids=single_pos_ids,
padding_positions=padding_positions,
output_length=output_length,
)
valid_states = pooled_states[valid_mask]
if getattr(vt.config, "standardize", False):
valid_states = (valid_states - vt.std_bias) * vt.std_scale
all_valid_states[orig_idx] = valid_states
valid_lens[orig_idx] = valid_states.shape[0]
# Project all images in a single batched call.
flat_valid_states = torch.cat(all_valid_states, dim=0).to(self.model_dtype)
flat_proj_embs = self.embed_vision(
inputs_embeds=flat_valid_states.unsqueeze(0)
).squeeze(0)
# Split back into per-image tensors (slicing returns views).
per_image_embeddings: list[torch.Tensor] = []
offset = 0
for length in valid_lens:
per_image_embeddings.append(flat_proj_embs[offset : offset + length])
offset += length
return per_image_embeddings
# ------------------------------------------------------------------ #
# Video processing (frames through vision tower)
# ------------------------------------------------------------------ #
def _process_video_input(
self,
video_input: Gemma4VideoInputs,
) -> list[torch.Tensor]:
"""Batch-encode video frames through the vision tower.
Gemma4 has no separate video tower; video frames are images at
lower resolution (max_soft_tokens=70). All frames across all
videos in the batch are encoded together in chunks, then pooled
and projected in a single batched call.
Returns one concatenated embedding tensor per video (not per
frame), matching the flat_from_sizes grouping that vLLM expects
for embed_multimodal.
"""
pixel_values = video_input["pixel_values_videos"]
pixel_position_ids = video_input["pixel_position_ids_videos"]
frame_counts = video_input["video_frame_counts"]
vt = self.vision_tower
vision_cfg = self.config.vision_config
pooling_k2 = vision_cfg.pooling_kernel_size**2
if isinstance(frame_counts, torch.Tensor):
# Per-video frame counts drive the Python-level batching below.
with gpu_sync_allowed():
fc_list = frame_counts.tolist()
else:
fc_list = list(frame_counts)
total_frames = pixel_values.shape[0]
free, total = torch.accelerator.get_memory_info()
max_batch_size = min(
total_frames,
self._encoder_chunk(
pixel_values.shape[1],
free,
total,
vision_cfg.position_embedding_size,
),
)
padding_positions = (pixel_position_ids == -1).all(dim=-1)
# Encode frames in chunks bounded by _encoder_chunk.
last_hidden_states_list: list[torch.Tensor] = []
for i in range(0, total_frames, max_batch_size):
pv_chunk = pixel_values[i : i + max_batch_size]
pp_chunk = pixel_position_ids[i : i + max_batch_size]
pad_chunk = padding_positions[i : i + max_batch_size]
inputs_embeds = vt.patch_embedder(
pv_chunk,
pp_chunk,
pad_chunk,
).to(self.model_dtype)
# HuggingFace's mask builder probes `padding_mask.all()`.
with gpu_sync_allowed():
encoder_outputs = vt.encoder(
inputs_embeds=inputs_embeds,
attention_mask=~pad_chunk,
pixel_position_ids=pp_chunk,
)
last_hidden_states_list.append(encoder_outputs.last_hidden_state)
last_hidden_states = torch.cat(last_hidden_states_list, dim=0)
# Pool per frame to strip padding and reduce spatial resolution.
output_length = pixel_values.shape[1] // pooling_k2
all_frame_valid_states: list[torch.Tensor] = []
frame_valid_lens: list[int] = []
for i in range(total_frames):
single_hidden = last_hidden_states[i].unsqueeze(0)
single_pos_ids = pixel_position_ids[i].unsqueeze(0)
single_pad_pos = padding_positions[i].unsqueeze(0)
# As above, plus mask indexing that needs the count on the host.
with gpu_sync_allowed():
pooled_states, valid_mask = vt.pooler(
hidden_states=single_hidden,
pixel_position_ids=single_pos_ids,
padding_positions=single_pad_pos,
output_length=output_length,
)
valid_states = pooled_states[valid_mask]
if getattr(vt.config, "standardize", False):
valid_states = (valid_states - vt.std_bias) * vt.std_scale
all_frame_valid_states.append(valid_states)
frame_valid_lens.append(valid_states.shape[0])
# Project all frames in a single batched call.
flat_valid_states = torch.cat(all_frame_valid_states, dim=0).to(
self.model_dtype
)
flat_proj_embs = self.embed_vision(
inputs_embeds=flat_valid_states.unsqueeze(0)
).squeeze(0)
# Regroup into per-video tensors (slicing returns views).
per_video_embeddings: list[torch.Tensor] = []
frame_idx = 0
offset = 0
for count in fc_list:
video_tokens = sum(frame_valid_lens[frame_idx : frame_idx + count])
per_video_embeddings.append(flat_proj_embs[offset : offset + video_tokens])
offset += video_tokens
frame_idx += count
return per_video_embeddings
# ------------------------------------------------------------------ #
# Audio processing
# ------------------------------------------------------------------ #
def _process_audio_input(
self,
audio_input: Gemma4AudioInputs,
) -> list[torch.Tensor]:
input_features, input_features_mask = batch_audio_features(
audio_input["input_features_padded"],
audio_input["input_features_mask"],
)
assert self.audio_tower is not None
assert self.embed_audio is not None
# Run audio tower — mask convention: True=valid, False=padding.
audio_outputs = self.audio_tower(input_features, input_features_mask)
if isinstance(audio_outputs, tuple):
audio_encodings, audio_mask = audio_outputs
else:
audio_encodings = audio_outputs.last_hidden_state
audio_mask = audio_outputs.attention_mask
# Project into LM embedding space.
audio_features = self.embed_audio(inputs_embeds=audio_encodings)
# Strip padding per-batch element: only keep valid (non-padding)
# tokens.
# Boolean-mask indexing needs the selected count on the host.
per_audio = []
with gpu_sync_allowed():
for enc, mask in zip(audio_features, audio_mask, strict=True):
per_audio.append(enc[mask]) # [num_real, hidden_size]
return per_audio
# ------------------------------------------------------------------ #
# MultiModalEmbeddings interface
# ------------------------------------------------------------------ #
def embed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
mm_input_by_modality = self._parse_and_validate_multimodal_inputs(**kwargs)
multimodal_embeddings: list[torch.Tensor] = []
for modality, multimodal_input in mm_input_by_modality.items():
if multimodal_input is None:
continue
if modality == "image":
assert isinstance(multimodal_input, Gemma4ImageInputs)
multimodal_embeddings.extend(
self._process_image_input(multimodal_input)
)
elif modality == "video":
assert isinstance(multimodal_input, Gemma4VideoInputs)
multimodal_embeddings.extend(
self._process_video_input(multimodal_input)
)
elif modality == "audio":
assert isinstance(multimodal_input, Gemma4AudioInputs)
multimodal_embeddings.extend(
self._process_audio_input(multimodal_input)
)
return multimodal_embeddings
# ------------------------------------------------------------------ #
# EncoderCudaGraph protocol methods
# ------------------------------------------------------------------ #
def get_encoder_cudagraph_config(self) -> "EncoderCudaGraphConfig":
from vllm.v1.worker.encoder_cudagraph_defs import EncoderCudaGraphConfig
def pad_pixel_values(dst: torch.Tensor, src: torch.Tensor) -> None:
dst.zero_()
batch_size, num_patches = src.shape[0], src.shape[1]
dst[:batch_size, :num_patches].copy_(src)
def pad_pixel_position_ids(dst: torch.Tensor, src: torch.Tensor) -> None:
dst.fill_(-1)
batch_size, num_patches = src.shape[0], src.shape[1]
dst[:batch_size, :num_patches].copy_(src)
return EncoderCudaGraphConfig(
modalities=["image", "video"],
buffer_keys=[
"pixel_values",
"pixel_position_ids",
"gather_indices",
],
out_hidden_size=self.config.text_config.hidden_size,
max_frames_per_video=_VIDEO_MAX_FRAMES,
padding_logics={
"pixel_values": pad_pixel_values,
"pixel_position_ids": pad_pixel_position_ids,
},
)
def get_encoder_cudagraph_budget_range(
self,
vllm_config: VllmConfig,
) -> tuple[int, int]:
min_budget = _SUPPORTED_SOFT_TOKENS[0]
max_budget = min(
vllm_config.scheduler_config.max_num_batched_tokens,
vllm_config.model_config.max_model_len,
)
return (min_budget, max_budget)
def get_input_modality(self, mm_kwargs: dict[str, Any]) -> str:
if "pixel_values" in mm_kwargs:
return "image"
elif "pixel_values_videos" in mm_kwargs:
return "video"
raise ValueError("Unsupported modality in mm_kwargs")
def get_max_frames_per_video(self) -> int:
return _VIDEO_MAX_FRAMES
def get_encoder_cudagraph_item_specs(
self,
mm_kwargs: dict[str, Any],
) -> list["EncoderItemSpec"]:
from vllm.v1.worker.encoder_cudagraph_defs import EncoderItemSpec
vision_cfg = self.vision_tower.config
pool_ratio = getattr(vision_cfg, "pooling_kernel_size", 2) ** 2
modality = self.get_input_modality(mm_kwargs)
if modality == "image":
pixel_values = mm_kwargs["pixel_values"]
if isinstance(pixel_values, list):
return [
EncoderItemSpec(
input_size=pv.shape[0],
output_tokens=pv.shape[0] // pool_ratio,
)
for pv in pixel_values
]
else:
return [
EncoderItemSpec(
input_size=pixel_values.shape[1],
output_tokens=pixel_values.shape[1] // pool_ratio,
)
for _ in range(pixel_values.shape[0])
]
elif modality == "video":
pixel_values_videos = mm_kwargs["pixel_values_videos"]
video_frame_counts = mm_kwargs["video_frame_counts"]
fc_list = (
video_frame_counts.tolist()
if isinstance(video_frame_counts, torch.Tensor)
else list(video_frame_counts)
)
np_patches = pixel_values_videos.shape[1]
return [
EncoderItemSpec(
input_size=fc * np_patches,
output_tokens=fc * (np_patches // pool_ratio),
)
for fc in fc_list
]
raise ValueError(f"Unknown modality: {modality}")
def select_encoder_cudagraph_items(
self,
mm_kwargs: dict[str, Any],
indices: list[int],
) -> dict[str, Any]:
modality = self.get_input_modality(mm_kwargs)
if modality == "image":
pixel_values = mm_kwargs["pixel_values"]
pixel_position_ids = mm_kwargs["pixel_position_ids"]
if len(indices) == 0:
is_pv_list = isinstance(pixel_values, list)
is_pp_list = isinstance(pixel_position_ids, list)
return {
"pixel_values": ([] if is_pv_list else pixel_values[:0]),
"pixel_position_ids": (
[] if is_pp_list else pixel_position_ids[:0]
),
}
if isinstance(pixel_values, list):
return {
"pixel_values": [pixel_values[i] for i in indices],
"pixel_position_ids": [pixel_position_ids[i] for i in indices],
}
return {
"pixel_values": pixel_values[indices],
"pixel_position_ids": pixel_position_ids[indices],
}
elif modality == "video":
pixel_values_videos = mm_kwargs["pixel_values_videos"]
pixel_position_ids_videos = mm_kwargs["pixel_position_ids_videos"]
video_frame_counts = mm_kwargs["video_frame_counts"]
if len(indices) == 0:
is_fc_tensor = isinstance(video_frame_counts, torch.Tensor)
return {
"pixel_values_videos": pixel_values_videos[:0],
"pixel_position_ids_videos": pixel_position_ids_videos[:0],
"video_frame_counts": (
video_frame_counts[:0] if is_fc_tensor else []
),
}
fc_list = (
video_frame_counts.tolist()
if isinstance(video_frame_counts, torch.Tensor)
else list(video_frame_counts)
)
cum_frames = [0]
for fc in fc_list:
cum_frames.append(cum_frames[-1] + fc)
selected_pv = torch.cat(
[
pixel_values_videos[cum_frames[i] : cum_frames[i + 1]]
for i in indices
],
dim=0,
)
selected_pp = torch.cat(
[
pixel_position_ids_videos[cum_frames[i] : cum_frames[i + 1]]
for i in indices
],
dim=0,
)
selected_fc = (
video_frame_counts[indices]
if isinstance(video_frame_counts, torch.Tensor)
else [video_frame_counts[i] for i in indices]
)
return {
"pixel_values_videos": selected_pv,
"pixel_position_ids_videos": selected_pp,
"video_frame_counts": selected_fc,
}
raise ValueError(f"Unknown modality: {modality}")
def prepare_encoder_cudagraph_capture_inputs(
self,
token_budget: int = 256,
max_batch_size: int = 4,
max_frames_per_batch: int = 1,
device: torch.device | str = "cpu",
dtype: torch.dtype | None = None,
path: str = "default",
axis_keys: tuple[Hashable, ...] | None = None,
**kwargs: Any,
) -> "EncoderCudaGraphCaptureInputs":
from vllm.v1.worker.encoder_cudagraph_defs import (
EncoderCudaGraphCaptureInputs,
)
dtype = dtype or torch.float32
max_size = max(max_batch_size, max_frames_per_batch)
vision_cfg = self.vision_tower.config
pool_ratio = getattr(vision_cfg, "pooling_kernel_size", 2) ** 2
# Retrieve the model's actual configured maximum tokens:
configured_max_tokens = getattr(
self.config.vision_config,
"num_soft_tokens",
_SUPPORTED_SOFT_TOKENS[2],
)
# Dynamically compute the slot capacity per item bounded by both the
# current graph budget and the user's maximum config:
per_item_output = min(token_budget, configured_max_tokens)
# Satisfy k^2 * per_item_output = per_item_patches
per_item_patches = per_item_output * pool_ratio
patch_size = self.vision_tower.config.patch_size
num_channels = getattr(self.vision_tower.config, "num_channels", 3)
patch_pixels = (patch_size**2) * num_channels
dummy_pixel_values = torch.zeros(
(max_size, per_item_patches, patch_pixels),
device=device,
dtype=dtype,
)
dummy_pixel_position_ids = torch.full(
(max_size, per_item_patches, 2),
-1,
device=device,
dtype=torch.long,
)
dummy_gather_indices = torch.zeros(
(token_budget,),
device=device,
dtype=torch.long,
)
return EncoderCudaGraphCaptureInputs(
values={
"pixel_values": dummy_pixel_values,
"pixel_position_ids": dummy_pixel_position_ids,
"gather_indices": dummy_gather_indices,
}
)
def prepare_encoder_cudagraph_replay_buffers(
self,
mm_kwargs: dict[str, Any],
max_batch_size: int = 4,
max_frames_per_batch: int = 1,
path: str = "default",
**kwargs: Any,
) -> "EncoderCudaGraphReplayBuffers":
from vllm.v1.worker.encoder_cudagraph_defs import (
EncoderCudaGraphReplayBuffers,
)
modality = self.get_input_modality(mm_kwargs)
if modality == "image":
pixel_values = mm_kwargs["pixel_values"]
pixel_position_ids = mm_kwargs["pixel_position_ids"]
elif modality == "video":
pixel_values = mm_kwargs["pixel_values_videos"]
pixel_position_ids = mm_kwargs["pixel_position_ids_videos"]
else:
raise ValueError(f"Unsupported modality: {modality}")
if isinstance(pixel_values, list):
max_patches = max(pv.shape[0] for pv in pixel_values)
batch_size = len(pixel_values)
pv_tensor = torch.zeros(
(batch_size, max_patches, pixel_values[0].shape[1]),
dtype=pixel_values[0].dtype,
device=pixel_values[0].device,
)
pp_tensor = torch.full(
(batch_size, max_patches, 2),
-1,
dtype=pixel_position_ids[0].dtype,
device=pixel_position_ids[0].device,
)
for i, (pv, pp) in enumerate(zip(pixel_values, pixel_position_ids)):
pv_tensor[i, : pv.shape[0]].copy_(pv)
pp_tensor[i, : pp.shape[0]].copy_(pp)
pixel_values = pv_tensor
pixel_position_ids = pp_tensor
item_specs = self.get_encoder_cudagraph_item_specs(mm_kwargs)
per_item_out_tokens = [spec.output_tokens for spec in item_specs]
total_tokens = sum(per_item_out_tokens)
device = pixel_values.device
vision_cfg = self.vision_tower.config
pool_ratio = getattr(vision_cfg, "pooling_kernel_size", 2) ** 2
per_item_output = pixel_values.shape[1] // pool_ratio
# ONLY allocate an array of exact size `total_tokens`.
# DO NOT pad it. The upstream Graph Manager handles the padding securely.
gather_indices = torch.zeros((total_tokens,), dtype=torch.long, device=device)
if modality == "image":
dst_offset = 0
for i, n_tok in enumerate(per_item_out_tokens):
safe_n_tok = min(n_tok, per_item_output)
src_start = i * per_item_output
src_end = src_start + safe_n_tok
gather_indices[dst_offset : dst_offset + safe_n_tok] = torch.arange(
src_start, src_end, dtype=torch.long, device=device
)
dst_offset += safe_n_tok
elif modality == "video":
video_frame_counts = mm_kwargs["video_frame_counts"]
fc_list = (
video_frame_counts.tolist()
if isinstance(video_frame_counts, torch.Tensor)
else list(video_frame_counts)
)
vision_cfg = self.vision_tower.config
pool_ratio = getattr(vision_cfg, "pooling_kernel_size", 2) ** 2
np_patches = pixel_values.shape[1]
frame_output_tokens = np_patches // pool_ratio
safe_frame_output_tokens = min(frame_output_tokens, per_item_output)
dst_offset = 0
frame_idx = 0
for fc in fc_list:
for f in range(fc):
src_start = (frame_idx + f) * per_item_output
src_end = src_start + safe_frame_output_tokens
gather_indices[
dst_offset : dst_offset + safe_frame_output_tokens
] = torch.arange(
src_start, src_end, dtype=torch.long, device=device
)
dst_offset += safe_frame_output_tokens
frame_idx += fc
return EncoderCudaGraphReplayBuffers(
values={
"pixel_values": pixel_values,
"pixel_position_ids": pixel_position_ids,
"gather_indices": gather_indices,
}
)
def encoder_cudagraph_forward(
self,
inputs: dict[str, torch.Tensor],
path: str = "default",
**kwargs: Any,
) -> torch.Tensor:
pixel_values = inputs["pixel_values"]
pixel_position_ids = inputs["pixel_position_ids"]
gather_indices = inputs["gather_indices"]
pad_tensor = (pixel_position_ids == -1).all(dim=-1)
vt = self.vision_tower
inputs_embeds = vt.patch_embedder(
pixel_values,
pixel_position_ids,
pad_tensor,
).to(self.model_dtype)
encoder_outputs = vt.encoder(
inputs_embeds=inputs_embeds,
attention_mask=~pad_tensor,
pixel_position_ids=pixel_position_ids,
)
hidden_states = encoder_outputs.last_hidden_state
pool_ratio = getattr(vt.config, "pooling_kernel_size", 2) ** 2
per_item_output = pixel_values.shape[1] // pool_ratio
pooled_states, _ = vt.pooler(
hidden_states=hidden_states,
pixel_position_ids=pixel_position_ids,
padding_positions=pad_tensor,
output_length=per_item_output,
)
if getattr(vt.config, "standardize", False):
pooled_states = (pooled_states - vt.std_bias) * vt.std_scale
flat_pooled = pooled_states.reshape(-1, pooled_states.shape[-1])
gathered_states = flat_pooled[gather_indices]
# Cast to the projection layer's dtype to resolve mixed-precision crash
target_dtype = self.embed_vision.embedding_projection.weight.dtype
gathered_states = gathered_states.to(target_dtype)
flat_proj_embs = self.embed_vision(
inputs_embeds=gathered_states.unsqueeze(0)
).squeeze(0)
return flat_proj_embs
def encoder_eager_forward(
self,
mm_kwargs: dict[str, Any],
path: str = "default",
**kwargs: Any,
) -> torch.Tensor:
modality = self.get_input_modality(mm_kwargs)
if modality == "image":
image_input = self._parse_and_validate_image_input(**mm_kwargs)
assert image_input is not None
embeddings = self._process_image_input(image_input)
elif modality == "video":
video_input = self._parse_and_validate_video_input(**mm_kwargs)
assert video_input is not None
embeddings = self._process_video_input(video_input)
else:
raise ValueError(f"Unsupported modality: {modality}")
return torch.cat(embeddings, dim=0)
def embed_input_ids(
self,
input_ids: torch.Tensor,
multimodal_embeddings: MultiModalEmbeddings | None = None,
*,
is_multimodal: torch.Tensor | None = None,
) -> torch.Tensor:
# Cache per-layer embeddings (PLE) for the language model's
# forward pass. During profiling embed_input_ids is not called,
# so the pre-allocated zeros are used instead.
if self.per_layer_embeddings is not None:
# Mask multimodal tokens (image/audio) to 0 for PLE
# computation (using token_type_ids == 0 as text_mask).
# Replicate this: map image token positions to token 0.
if is_multimodal is not None:
ple_input_ids = torch.where(
is_multimodal.to(input_ids.device, non_blocking=True),
torch.zeros_like(input_ids),
input_ids,
)
else:
ple_input_ids = input_ids
per_layer_inputs = self.language_model.model.get_per_layer_inputs(
ple_input_ids
)
if per_layer_inputs is not None:
per_layer_inputs = per_layer_inputs.reshape(
-1,
self.config.text_config.num_hidden_layers,
self.config.text_config.hidden_size_per_layer_input,
)
self.per_layer_embeddings[: per_layer_inputs.shape[0]].copy_(
per_layer_inputs
)
if multimodal_embeddings is None or is_multimodal is None:
return super().embed_input_ids(input_ids)
return super().embed_input_ids(
input_ids,
multimodal_embeddings=multimodal_embeddings,
is_multimodal=is_multimodal,
)
# ------------------------------------------------------------------ #
# Forward
# ------------------------------------------------------------------ #
def forward(
self,
input_ids: torch.Tensor,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
**kwargs: object,
) -> IntermediateTensors:
if intermediate_tensors is not None:
inputs_embeds = None
# Select the pre-cached PLEs for this batch (None when PLE
# is disabled for variants without PLE).
per_layer_inputs = (
self.per_layer_embeddings[: inputs_embeds.shape[0]]
if self.per_layer_embeddings is not None and inputs_embeds is not None
else None
)
# Gemma4 bidi: clear mm_prefix_range for full_attention layers.
# Must run here (outside @support_torch_compile boundary) because
# _run_decoder_layers is inside a compiled graph where Python
# side effects are eliminated.
self._clear_mm_prefix_for_full_attn_layers()
hidden_states = self.language_model.model(
input_ids,
positions,
per_layer_inputs=per_layer_inputs,
intermediate_tensors=intermediate_tensors,
inputs_embeds=inputs_embeds,
**kwargs,
)
return hidden_states
def compute_logits(
self,
hidden_states: torch.Tensor,
) -> torch.Tensor | None:
logits = self.language_model.compute_logits(hidden_states)
if logits is not None and self._suppress_token_ids:
# Cache a per-device index tensor for the (static) suppressed-token
# set and use `index_fill_`, so neither the Python-list indices nor
# the scalar fill value take a host roundtrip per call.
cache = getattr(self, "_suppress_token_ids_cache", None)
if cache is None:
cache = {}
self._suppress_token_ids_cache = cache
suppress_idx = cache.get(logits.device)
if suppress_idx is None:
suppress_idx = async_tensor_h2d(
self._suppress_token_ids, dtype=torch.long, device=logits.device
)
cache[logits.device] = suppress_idx
logits.index_fill_(1, suppress_idx, -float("inf"))
return logits
# ------------------------------------------------------------------ #
# Bidirectional attention helpers
# ------------------------------------------------------------------ #
def _clear_mm_prefix_for_full_attn_layers(self) -> None:
"""Clear mm_prefix_range for non-sliding layers.
Gemma4 with use_bidirectional_attention='vision' applies
bidirectional attention only to sliding_attention layers.
Full attention layers use plain causal masking.
Uses _full_attn_layer_idxs (precomputed in __init__) for O(1)
lookup instead of per-call regex parsing.
"""
if not self._full_attn_layer_idxs:
return
from vllm.forward_context import get_forward_context
attn_metadata = get_forward_context().attn_metadata
if attn_metadata is None:
return
def _process(metadata_dict: dict) -> None:
for layer_name, metadata in metadata_dict.items():
if ".layers." not in layer_name:
continue
try:
layer_idx = int(layer_name.split(".layers.")[1].split(".")[0])
except (ValueError, IndexError):
continue
if layer_idx in self._full_attn_layer_idxs:
if hasattr(metadata, "mm_prefix_range"):
metadata.mm_prefix_range = None
if hasattr(metadata, "mm_prefix_range_tensor"):
metadata.mm_prefix_range_tensor = None
if hasattr(metadata, "mm_prefix_query_range_tensor"):
metadata.mm_prefix_query_range_tensor = None
if isinstance(attn_metadata, list):
for ub_metadata in attn_metadata:
_process(ub_metadata)
elif isinstance(attn_metadata, dict):
_process(attn_metadata)
# ------------------------------------------------------------------ #
# Weight loading
# ------------------------------------------------------------------ #
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
# Some checkpoints have vestigial embed_vision.embedding and
# embed_audio.embedding weights from the Gemma3n architecture
# that are not used by Gemma4's MultimodalEmbedder (which only
# has embedding_projection + embedding_post_projection_norm).
ignore_prefixes = [
"embed_vision.embedding.",
"embed_audio.embedding.",
]
# Models without audio tower should skip audio weights entirely.
if self.audio_tower is None:
ignore_prefixes.extend(
[
"audio_tower.",
"embed_audio.",
]
)
loader = AutoWeightsLoader(
self,
ignore_unexpected_prefixes=ignore_prefixes,
)
return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
# ------------------------------------------------------------------ #
# LoRA / multimodal mapping
# ------------------------------------------------------------------ #
def get_mm_mapping(self) -> MultiModelKeys:
"""Get the module prefix mapping for multimodal models."""
connectors = ["embed_vision"]
tower_models = ["vision_tower"]
if self.audio_tower is not None:
connectors.append("embed_audio")
tower_models.append("audio_tower")
return MultiModelKeys.from_string_field(
language_model="language_model",
connector=connectors,
tower_model=tower_models,
)
def get_mm_lora_token_counts(
self,
*,
modality: str,
mm_kwargs: MultiModalKwargsItem | None,
num_mm_embeds: int,
) -> tuple[int, int | None]:
tower_tokens: int | None = None
connector_tokens: int | None = None
if modality in ("image", "video"):
vision_config = self.config.vision_config
pooling_k2 = vision_config.pooling_kernel_size**2
if modality == "image":
pixel_values_key = "pixel_values"
max_soft_tokens = int(vision_config.default_output_length)
mm_processor_kwargs = getattr(
getattr(self, "multimodal_config", None),
"mm_processor_kwargs",
None,
)
if isinstance(mm_processor_kwargs, Mapping):
val, _ = _get_max_soft_tokens(mm_processor_kwargs)
if isinstance(val, int) and val in _SUPPORTED_SOFT_TOKENS:
max_soft_tokens = val
else:
pixel_values_key = "pixel_values_videos"
max_soft_tokens = _VIDEO_MAX_SOFT_TOKENS
tower_tokens = max_soft_tokens * pooling_k2 if modality == "image" else None
connector_tokens = num_mm_embeds
if tower_tokens is None and mm_kwargs is not None:
field = mm_kwargs.get(pixel_values_key)
if field is not None:
data = field.data
if isinstance(data, torch.Tensor) and data.ndim >= 2:
tower_tokens = int(math.prod(data.shape[:-1]))
if tower_tokens is None:
min_soft_tokens = min(_SUPPORTED_SOFT_TOKENS)
tower_tokens = (
math.ceil(num_mm_embeds / min_soft_tokens)
* max_soft_tokens
* pooling_k2
)
elif modality == "audio":
tower_tokens = num_mm_embeds
connector_tokens = num_mm_embeds
if mm_kwargs is not None:
field = mm_kwargs.get("input_features_padded")
if field is not None:
data = field.data
if isinstance(data, torch.Tensor) and data.ndim >= 2:
batch_size = math.prod(data.shape[:-2])
audio_tokens = batch_size * math.ceil(data.shape[-2] / 4)
tower_tokens = audio_tokens
connector_tokens = audio_tokens
else:
raise ValueError(f"Unsupported modality: {modality}")
assert tower_tokens is not None
return tower_tokens, connector_tokens
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality == "image":
return "<image_soft_token>"
if modality == "audio":
return "<audio_soft_token>"
if modality == "video":
return "<|video|>"
raise ValueError(f"Unsupported modality: {modality}")
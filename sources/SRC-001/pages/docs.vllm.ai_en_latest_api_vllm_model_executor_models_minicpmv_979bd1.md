source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/minicpmv/
lastmod: 2026-09-24

class _MiniCPMVEncoderCudaGraphMixin(MiniCPMVBaseModel, SupportsEncoderCudaGraph):
"""SupportsEncoderCudaGraph for MiniCPM-V Idefics2 + resampler (not 2.0)."""
supports_encoder_cudagraph: ClassVar[Literal[True]] = True
def _mcpmv_slice_pixel_size(self) -> tuple[int, int]:
image_size = int(self.vpm.embeddings.image_size)
return image_size, image_size
def _mcpmv_patch_grid_pixel_hw(
self, patch_grid_key: tuple[int, int]
) -> tuple[int, int]:
patch_size = int(self.vpm.embeddings.patch_size)
th, tw = patch_grid_key
return th * patch_size, tw * patch_size
def _mcpmv_patch_grid_num_patches(self, patch_grid_key: tuple[int, int]) -> int:
th, tw = patch_grid_key
return th * tw
def _mcpmv_patch_grid_keys(self) -> tuple[tuple[int, int], ...]:
"""Ordered patch-grid keys ``(nb_h, nb_w)`` for the capture axis."""
max_side = int(self.vpm.embeddings.image_size) // int(
self.vpm.embeddings.patch_size
)
keys: list[tuple[int, int]] = []
seen: set[tuple[int, int]] = set()
for th, tw in _MINICPMV_BASE_PATCH_BUCKETS:
if th <= max_side and tw <= max_side:
keys.append((th, tw))
seen.add((th, tw))
full = (max_side, max_side)
if full not in seen:
keys.append(full)
return tuple(keys)
def _mcpmv_resolve_patch_grid(
self,
tgt_sizes: torch.Tensor,
slice_counts: list[int],
indices: list[int],
) -> tuple[int, int]:
"""Smallest patch-grid key covering all selected items."""
keys = self._mcpmv_patch_grid_keys()
if not indices:
return keys[0]
tgt_groups = torch.split(tgt_sizes, slice_counts)
selected = torch.cat([tgt_groups[i] for i in indices], dim=0)
need_h = int(selected[:, 0].max().item())
need_w = int(selected[:, 1].max().item())
for th, tw in keys:
if th >= need_h and tw >= need_w:
return (th, tw)
return keys[-1]
def _mcpmv_max_slices_cap(
self,
token_budget: int,
max_batch_size: int,
max_frames_per_batch: int,
) -> int:
max_slice_num = int(getattr(self.config, "max_slice_num", 9))
query_num = max(1, int(self.config.query_num))
max_slices_by_token_budget = max(1, token_budget // query_num)
max_slices_by_content = max_batch_size * (max_slice_num + 1)
if self.version in {(2, 6), (4, 0)} and max_frames_per_batch > 0:
max_slices_by_content = max(
max_slices_by_content,
max_frames_per_batch * (max_slice_num + 1),
)
return max(1, min(max_slices_by_token_budget, max_slices_by_content))
def get_encoder_cudagraph_config(self) -> EncoderCudaGraphConfig:
buffer_keys = [
_MINICPMV_CUDAGRAPH_BUF_KEY_PIXEL,
_MINICPMV_CUDAGRAPH_BUF_KEY_TGT_SIZES,
_MINICPMV_CUDAGRAPH_BUF_KEY_PATCH_MASK,
]
# Video is only supported from 2.6 onward.
modalities = ["image"]
if self.version in {(2, 6), (4, 0)}:
modalities.append("video")
max_frames = self.get_max_frames_per_video() if "video" in modalities else 1
return EncoderCudaGraphConfig(
modalities=modalities,
buffer_keys=buffer_keys,
out_hidden_size=int(self.embed_dim),
max_frames_per_video=max_frames,
capture_axes=(self._mcpmv_patch_grid_keys(),),
)
def get_input_modality(self, mm_kwargs: dict[str, Any]) -> str:
if "video_pixel_values" in mm_kwargs:
return "video"
return "image"
def get_max_frames_per_video(self) -> int:
info = MULTIMODAL_REGISTRY.get_processing_info(self.vllm_config.model_config)
assert isinstance(info, MiniCPMVProcessingInfo)
return int(
info.get_num_frames_with_most_features(
seq_len=self.vllm_config.model_config.max_model_len,
mm_counts={
"video": self.multimodal_config.get_limit_per_prompt("video")
},
)
)
def get_encoder_cudagraph_budget_range(
self, vllm_config: VllmConfig
) -> tuple[int, int]:
# Each slice produces exactly query_num resampler output tokens.
# A thumbnail-only image has 1 slice, so query_num is the smallest
# possible encoder output and the natural minimum budget.
min_budget = int(self.config.query_num)
max_budget = min(
vllm_config.scheduler_config.max_num_batched_tokens,
vllm_config.model_config.max_model_len,
)
return (min_budget, max_budget)
def get_encoder_cudagraph_item_specs(
self, mm_kwargs: dict[str, Any]
) -> list[EncoderItemSpec]:
video = self.get_input_modality(mm_kwargs) == "video"
pixel_values_key = "video_pixel_values" if video else "pixel_values"
pixel_values: list[list[torch.Tensor]] = mm_kwargs[pixel_values_key]
slice_counts = [len(img) for img in pixel_values]
tgt_sizes = _mcpmv_tgt_sizes_tensor(mm_kwargs, video=video)
tgt_sizes = _mcpmv_normalize_tgt_sizes(tgt_sizes, slice_counts)
patch_sums = tgt_sizes.prod(-1)
input_sizes = [
int(group.sum().item()) for group in torch.split(patch_sums, slice_counts)
]
query_num = int(self.config.query_num)
return [
EncoderItemSpec(
input_size=input_sizes[i],
output_tokens=slice_counts[i] * query_num,
)
for i in range(len(pixel_values))
]
def select_encoder_cudagraph_items(
self,
mm_kwargs: dict[str, Any],
indices: list[int],
) -> dict[str, Any]:
subset, patch_grid = self._mcpmv_select_items(mm_kwargs, indices)
subset[ENCODER_CUDAGRAPH_AXIS_KEYS_KWARG] = (patch_grid,)
return subset
def _mcpmv_select_items(
self, mm_kwargs: dict[str, Any], indices: list[int]
) -> tuple[dict[str, Any], tuple[int, int]]:
"""Slice mm_kwargs for `indices`; also returns the patch-grid key."""
video = self.get_input_modality(mm_kwargs) == "video"
pixel_values_key = "video_pixel_values" if video else "pixel_values"
tgt_key = "video_tgt_sizes" if video else "tgt_sizes"
flat_key = (
_MINICPMV_CUDAGRAPH_FLAT_KEY_VIDEO
if video
else _MINICPMV_CUDAGRAPH_FLAT_KEY_IMAGE
)
device = next(self.vpm.parameters()).device
pixel_values: list[list[torch.Tensor]] = mm_kwargs[pixel_values_key]
tgt_sizes = _mcpmv_tgt_sizes_tensor(mm_kwargs, video=video)
subset = {
k: v
for k, v in mm_kwargs.items()
if k not in _ENCODER_CUDAGRAPH_MM_KWARGS_SKIP_KEYS
}
if not indices:
pixel_h, pixel_w = self._mcpmv_slice_pixel_size()
vpm_dtype = next(self.vpm.parameters()).dtype
subset.update(
{
pixel_values_key: [],
tgt_key: torch.zeros((0, 2), dtype=torch.long, device=device),
flat_key: torch.zeros(
(0, 3 * pixel_h * pixel_w), device=device, dtype=vpm_dtype
),
}
)
return subset, self._mcpmv_patch_grid_keys()[0]
slice_counts = [len(item_slices) for item_slices in pixel_values]
tgt_sizes = _mcpmv_normalize_tgt_sizes(tgt_sizes, slice_counts)
tgt_groups = torch.split(tgt_sizes, slice_counts)
patch_grid = self._mcpmv_resolve_patch_grid(tgt_sizes, slice_counts, indices)
pixel_h, pixel_w = self._mcpmv_patch_grid_pixel_hw(patch_grid)
selected_pixel_values = [pixel_values[i] for i in indices]
selected_tgt_sizes_list = [tgt_groups[i] for i in indices]
selected_tgt_sizes = torch.cat(selected_tgt_sizes_list, dim=0)
selected_slices = flatten_2d_lists(selected_pixel_values)
packed_flat_pixels = _mcpmv_pack_flat_pixels(
selected_slices,
pixel_height=pixel_h,
pixel_width=pixel_w,
max_num_slices=len(selected_slices),
device=selected_slices[0].device,
dtype=selected_slices[0].dtype,
patch_size=int(self.vpm.embeddings.patch_size),
tgt_sizes=selected_tgt_sizes,
)
subset.update(
{
pixel_values_key: selected_pixel_values,
tgt_key: selected_tgt_sizes_list,
flat_key: packed_flat_pixels,
_MINICPMV_CUDAGRAPH_PATCH_GRID_KEY: patch_grid,
}
)
return subset, patch_grid
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
patch_grid = (
cast("tuple[int, int]", axis_keys[0])
if axis_keys
# Without capture-axis context, use the largest (full-resolution)
# patch grid.
else self._mcpmv_patch_grid_keys()[-1]
)
return self._mcpmv_capture_inputs(
token_budget,
max_batch_size,
max_frames_per_batch,
device,
dtype,
patch_grid=patch_grid,
)
def _mcpmv_capture_inputs(
self,
token_budget: int,
max_batch_size: int,
max_frames_per_batch: int,
device: torch.device,
dtype: torch.dtype,
patch_grid: tuple[int, int],
):
th, tw = patch_grid
pixel_h, pixel_w = self._mcpmv_patch_grid_pixel_hw(patch_grid)
max_patches = self._mcpmv_patch_grid_num_patches(patch_grid)
max_num_slices = self._mcpmv_max_slices_cap(
token_budget,
max_batch_size,
max_frames_per_batch,
)
pixel_buffer = torch.zeros(
(max_num_slices, 3, pixel_h, pixel_w), device=device, dtype=dtype
)
dummy_tgt_sizes = torch.zeros(
(max_num_slices, 2), dtype=torch.long, device=device
)
dummy_tgt_sizes[:, 0] = th
dummy_tgt_sizes[:, 1] = tw
dummy_patch_mask = torch.ones(
(max_num_slices, max_patches), dtype=torch.bool, device=device
)
values: dict[str, torch.Tensor] = {
_MINICPMV_CUDAGRAPH_BUF_KEY_PIXEL: pixel_buffer,
_MINICPMV_CUDAGRAPH_BUF_KEY_TGT_SIZES: dummy_tgt_sizes,
_MINICPMV_CUDAGRAPH_BUF_KEY_PATCH_MASK: dummy_patch_mask,
}
return EncoderCudaGraphCaptureInputs(values=values)
def prepare_encoder_cudagraph_replay_buffers(
self,
mm_kwargs: dict[str, Any],
max_batch_size: int,
max_frames_per_batch: int,
path: str = "default",
):
_ = max_batch_size
_ = max_frames_per_batch
video = self.get_input_modality(mm_kwargs) == "video"
flat_key = (
_MINICPMV_CUDAGRAPH_FLAT_KEY_VIDEO
if video
else _MINICPMV_CUDAGRAPH_FLAT_KEY_IMAGE
)
flat_pixels = mm_kwargs[flat_key] # (num_actual_slices, 3*pixel_h*pixel_w)
patch_grid = mm_kwargs[_MINICPMV_CUDAGRAPH_PATCH_GRID_KEY]
pixel_h, pixel_w = self._mcpmv_patch_grid_pixel_hw(patch_grid)
max_patches = self._mcpmv_patch_grid_num_patches(patch_grid)
pixel_buffer = flat_pixels.reshape(-1, 3, pixel_h, pixel_w)
device = next(self.vpm.parameters()).device
tgt_sizes_raw = _mcpmv_tgt_sizes_tensor(mm_kwargs, video=video)
if isinstance(tgt_sizes_raw, list):
tgt_sizes_raw = torch.cat(tgt_sizes_raw, dim=0)
# tgt_sizes arrives from CPU-side mm_kwargs; use a pinned async copy
# to stay clean under VLLM_GPU_SYNC_CHECK.
tgt_sizes = async_tensor_h2d(tgt_sizes_raw, device, dtype=torch.long)
patches_per_slice = tgt_sizes.prod(-1).clamp(max=max_patches)
col_idx = torch.arange(max_patches, device=device)
patch_attention_mask = col_idx.unsqueeze(0) < patches_per_slice.unsqueeze(1)
values: dict[str, torch.Tensor] = {
_MINICPMV_CUDAGRAPH_BUF_KEY_PIXEL: pixel_buffer,
_MINICPMV_CUDAGRAPH_BUF_KEY_TGT_SIZES: tgt_sizes,
_MINICPMV_CUDAGRAPH_BUF_KEY_PATCH_MASK: patch_attention_mask,
}
return EncoderCudaGraphReplayBuffers(values=values)
def encoder_cudagraph_forward(
self,
values: dict[str, torch.Tensor],
path: str = "default",
) -> torch.Tensor:
all_pixel_values = values[_MINICPMV_CUDAGRAPH_BUF_KEY_PIXEL]
tgt_sizes = values[_MINICPMV_CUDAGRAPH_BUF_KEY_TGT_SIZES]
patch_mask = values[_MINICPMV_CUDAGRAPH_BUF_KEY_PATCH_MASK]
patch_attention_mask = patch_mask.unsqueeze(1)
max_num_slices = all_pixel_values.shape[0]
# v2.5 infers patch layout from the attention mask; pass tgt_sizes=None.
vpm_tgt_sizes = None if self.version == (2, 5) else tgt_sizes
vision_embedding = self.vpm(
all_pixel_values,
patch_attention_mask=patch_attention_mask,
tgt_sizes=vpm_tgt_sizes,
)
resampler_out = self.resampler(vision_embedding, tgt_sizes)
query_num = int(self.config.query_num)
return resampler_out.reshape(max_num_slices * query_num, int(self.embed_dim))
def encoder_eager_forward(
self,
mm_kwargs: dict[str, Any],
path: str = "default",
) -> torch.Tensor:
"""Eager encoder path; returns ``(total_tokens, embed_dim)`` like
``encoder_cudagraph_forward``.
"""
mm_kwargs_no_flat = {
k: v
for k, v in mm_kwargs.items()
if k not in _ENCODER_CUDAGRAPH_MM_KWARGS_SKIP_KEYS
}
modalities = self._parse_and_validate_multimodal_inputs(**mm_kwargs_no_flat)
segments: list[torch.Tensor] = []
embed_dim = self.embed_dim
for modality in modalities:
if modality == "images":
image_input = modalities["images"]
assert isinstance(image_input, MiniCPMVImagePixelInputs)
image_embeddings = self.get_vision_hidden_states(image_input)
segments.append(image_embeddings.reshape(-1, embed_dim))
elif modality == "videos":
video_input = modalities["videos"]
assert isinstance(video_input, MiniCPMVImagePixelInputs)
video_embeddings = self.get_vision_hidden_states(video_input)
segments.append(video_embeddings.reshape(-1, embed_dim))
if not segments:
raise RuntimeError(
"MiniCPM-V encoder cudagraph eager path expects pixel_values "
"or video_pixel_values"
)
return torch.cat(segments, dim=0)
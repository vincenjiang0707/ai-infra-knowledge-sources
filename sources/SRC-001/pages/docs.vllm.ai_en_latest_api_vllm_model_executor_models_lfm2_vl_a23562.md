source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/lfm2_vl/
lastmod: 2026-09-24

@MULTIMODAL_REGISTRY.register_processor(
Lfm2VLMultiModalProcessor,
info=Lfm2VLProcessingInfo,
dummy_inputs=Lfm2VLDummyInputsBuilder,
)
class Lfm2VLForConditionalGeneration(
nn.Module,
SupportsMultiModal,
SupportsEncoderCudaGraph,
SupportsLoRA,
SupportsPP,
IsHybrid,
):
supports_tower_connector_lora = True
merge_by_field_config = True
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_prefix={
"lm_head.": "language_model.lm_head.",
"model.language_model.": "language_model.model.",
"model.vision_tower.": "vision_tower.",
"model.multi_modal_projector.": "multi_modal_projector.",
}
)
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("image"):
return "<image>"
raise ValueError("Only image modality is supported")
@classmethod
def get_mamba_state_dtype_from_config(
cls,
vllm_config: "VllmConfig",
) -> tuple[torch.dtype, ...]:
return MambaStateDtypeCalculator.short_conv_state_dtype(
vllm_config.model_config.dtype,
vllm_config.cache_config.mamba_cache_dtype,
)
@classmethod
def get_mamba_state_shape_from_config(
cls,
vllm_config: "VllmConfig",
) -> tuple[tuple[int, int]]:
"""Calculate shapes for LFM2's convolutional cache.
Args:
vllm_config: vLLM config
Returns:
Tuple containing:
- conv_state_shape: Shape for convolutional state cache
"""
parallel_config = vllm_config.parallel_config
hf_language_config = vllm_config.model_config.hf_config.text_config
return MambaStateShapeCalculator.short_conv_state_shape(
tp_world_size=parallel_config.tensor_parallel_size,
intermediate_size=hf_language_config.hidden_size,
conv_kernel=hf_language_config.conv_L_cache,
)
@classmethod
def get_mamba_state_copy_func(cls) -> tuple[MambaStateCopyFunc]:
return MambaStateCopyFuncCalculator.short_conv_state_copy_func()
def __init__(self, *, vllm_config: VllmConfig, prefix: str = "model"):
super().__init__()
config: Lfm2VlConfig = vllm_config.model_config.hf_config
multimodal_config = vllm_config.model_config.multimodal_config
assert multimodal_config is not None
vision_config = config.vision_config
quant_config = vllm_config.quant_config
self.config = config
self.vllm_config = vllm_config
self.model_config = vllm_config.model_config
self.multimodal_config = multimodal_config
self.use_data_parallel = multimodal_config.mm_encoder_tp_mode == "data"
with self._mark_tower_model(vllm_config, "image"):
if vision_config.model_type == "siglip2_vision_model":
self.vision_tower = Siglip2Model(
config=vision_config,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "vision_tower"),
)
else:
raise ValueError(
f"Unsupported visual tokenizer type: {vision_config.model_type}"
)
self.multi_modal_projector = Lfm2VLMultiModalProjector(
config=config,
prefix=maybe_prefix(prefix, "multi_modal_projector"),
)
with self._mark_language_model(vllm_config):
self.language_model = init_vllm_registered_model(
vllm_config=vllm_config,
hf_config=config.text_config,
prefix=maybe_prefix(prefix, "language"),
architectures=config.text_config.architectures,
)
self.make_empty_intermediate_tensors = (
self.language_model.make_empty_intermediate_tensors
)
def _parse_and_validate_image_input(
self, **kwargs: object
) -> LFM2VLImageInputs | None:
pixel_values = kwargs.pop("pixel_values", None)
spatial_shapes = kwargs.pop("spatial_shapes", None)
num_patches = kwargs.pop("num_patches", None)
if pixel_values is None:
return None
return LFM2VLImageInputs(
type="pixel_values",
pixel_values=pixel_values,
spatial_shapes=spatial_shapes,
num_patches=num_patches,
)
def image_pixels_to_features(
self,
pixel_values: torch.FloatTensor,
spatial_shapes: torch.Tensor,
) -> list[torch.Tensor]:
assert spatial_shapes.device.type == "cpu", (
"Expected `spatial_shapes` on CPU to avoid device-to-host sync in "
"variable-length packing."
)
pixel_values = pixel_values.to(
dtype=self.vision_tower.vision_model.embeddings.patch_embedding.weight.dtype
) # fp16 compatibility
# LFM2-VL's HF processor pads patch sequences with trailing zeros.
# Pack patch tokens upfront so the vision tower runs entirely unpadded.
spatial_shapes_list: list[list[int]] = spatial_shapes.tolist()
lengths_list = [h * w for h, w in spatial_shapes_list]
total_tokens = int(sum(lengths_list))
lengths_cpu = (spatial_shapes[:, 0] * spatial_shapes[:, 1]).to(
dtype=torch.int32
)
max_seqlen = (
lengths_cpu.max().reshape(1)
if lengths_cpu.numel()
else torch.tensor([0], dtype=torch.int32)
)
if total_tokens == 0:
return []
packed_pixel_values = pixel_values.new_empty(
(total_tokens, pixel_values.shape[-1])
)
offset = 0
for i, length in enumerate(lengths_list):
if length <= 0:
continue
packed_pixel_values[offset : offset + length].copy_(
pixel_values[i, :length]
)
offset += length
packed_pixel_values = packed_pixel_values.unsqueeze(0)
lengths = torch.tensor(
lengths_list, dtype=torch.int32, device=pixel_values.device
)
cu_seqlens = torch.zeros(
lengths.shape[0] + 1,
dtype=torch.int32,
device=pixel_values.device,
)
cu_seqlens[1:] = torch.cumsum(lengths, dim=0)
with set_forward_context(None, self.vllm_config):
vision_outputs = self.vision_tower(
pixel_values_packed=packed_pixel_values,
spatial_shapes=spatial_shapes,
cu_seqlens=cu_seqlens,
max_seqlen=max_seqlen,
)
image_outputs_packed = getattr(
vision_outputs, "last_hidden_state", vision_outputs
)
vision_features_packed = image_outputs_packed[0]
projected_packed = self.multi_modal_projector(
vision_features_packed=vision_features_packed,
spatial_shapes=spatial_shapes,
)
projected_lengths_list = self._get_lfm2vl_tile_output_lengths(
spatial_shapes_list
)
image_features: list[torch.Tensor] = []
offset = 0
for out_len in projected_lengths_list:
image_features.append(projected_packed[offset : offset + out_len])
offset += out_len
return image_features
def _process_image_input(
self,
image_input: LFM2VLImageInputs,
) -> torch.Tensor | list[torch.Tensor]:
pixel_values = image_input["pixel_values"]
spatial_shapes = image_input["spatial_shapes"]
num_patches = image_input["num_patches"]
image_features = self.image_pixels_to_features(
pixel_values,
spatial_shapes=spatial_shapes,
)
# Group patches by image - num_patches is on CPU (keep_on_cpu=True)
# so .tolist() is instant with no DtoH sync
num_patches_list = num_patches.tolist()
batched_features: list[torch.Tensor] = []
patch_idx = 0
for count in num_patches_list:
# Slice the list of patch tensors for this image
image_patches = image_features[patch_idx : patch_idx + count]
# Concatenate patches for this image
batched_features.append(torch.cat(image_patches, dim=0))
patch_idx += count
return batched_features
def embed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
image_input = self._parse_and_validate_image_input(**kwargs)
if image_input is None:
return []
return self._process_image_input(image_input)
def get_encoder_cudagraph_config(self):
from vllm.v1.worker.encoder_cudagraph_defs import (
EncoderCudaGraphConfig,
)
return EncoderCudaGraphConfig(
modalities=["image"],
buffer_keys=[
"pixel_values_packed",
"pos_embeds",
"cu_seqlens",
"max_seqlen",
"gather_idx",
],
out_hidden_size=self.config.text_config.hidden_size,
padding_logics={
"cu_seqlens": _pad_cumulative_seqlens_buffer,
},
)
def get_max_frames_per_video(self) -> int:
return 0
def get_encoder_cudagraph_budget_range(
self,
vllm_config: VllmConfig,
) -> tuple[int, int]:
min_budget = self._get_lfm2vl_min_image_tokens()
max_budget = min(
vllm_config.scheduler_config.max_num_batched_tokens,
self.model_config.max_model_len,
)
return min_budget, max_budget
def _get_spatial_shapes_list(
self,
spatial_shapes: torch.Tensor,
) -> list[list[int]]:
assert spatial_shapes.device.type == "cpu", (
"Expected `spatial_shapes` on CPU to avoid device-to-host sync in "
"variable-length packing."
)
return spatial_shapes.tolist()
@staticmethod
def _get_lfm2vl_tile_input_lengths(
spatial_shapes_list: list[list[int]],
) -> list[int]:
return [height * width for height, width in spatial_shapes_list]
def _get_lfm2vl_tile_output_lengths(
self,
spatial_shapes_list: list[list[int]],
) -> list[int]:
factor = self.multi_modal_projector.factor
output_lengths: list[int] = []
for height, width in spatial_shapes_list:
if height % factor != 0 or width % factor != 0:
raise ValueError(
"spatial_shapes must be divisible by downsample_factor: "
f"got ({height}, {width}) with factor={factor}."
)
output_lengths.append((height // factor) * (width // factor))
return output_lengths
def _get_lfm2vl_mm_processor_kwargs(self) -> Mapping[str, object]:
return self.multimodal_config.mm_processor_kwargs or {}
def _get_lfm2vl_min_image_tokens(self) -> int:
value = self._get_lfm2vl_mm_processor_kwargs().get(
"min_image_tokens",
getattr(self.config, "min_image_tokens", None) or 64,
)
if not isinstance(
value,
(str, Buffer, typing.SupportsInt, typing.SupportsIndex),
):
raise TypeError(
"int() argument must be a string, a bytes-like object "
f"or a real number, not '{type(value).__name__}'"
)
return max(1, int(value))
def _get_lfm2vl_item_tile_slices(
self,
num_patches: torch.Tensor,
) -> list[tuple[int, int]]:
num_patches_list = [int(x) for x in num_patches.tolist()]
starts = [0]
for count in num_patches_list:
starts.append(starts[-1] + count)
return list(zip(starts[:-1], starts[1:]))
def get_encoder_cudagraph_item_specs(
self,
mm_kwargs: dict[str, Any],
):
from vllm.v1.worker.encoder_cudagraph_defs import EncoderItemSpec
spatial_shapes = mm_kwargs["spatial_shapes"]
num_patches = mm_kwargs["num_patches"]
spatial_shapes_list = self._get_spatial_shapes_list(spatial_shapes)
input_lengths = self._get_lfm2vl_tile_input_lengths(spatial_shapes_list)
output_lengths = self._get_lfm2vl_tile_output_lengths(spatial_shapes_list)
return [
EncoderItemSpec(
input_size=sum(input_lengths[start:end]),
output_tokens=sum(output_lengths[start:end]),
)
for start, end in self._get_lfm2vl_item_tile_slices(num_patches)
]
def select_encoder_cudagraph_items(
self,
mm_kwargs: dict[str, Any],
indices: list[int],
) -> dict[str, Any]:
pixel_values = mm_kwargs["pixel_values"]
spatial_shapes = mm_kwargs["spatial_shapes"]
num_patches = mm_kwargs["num_patches"]
tile_slices = self._get_lfm2vl_item_tile_slices(num_patches)
if len(indices) == 0:
return {
"pixel_values": pixel_values[:0],
"spatial_shapes": spatial_shapes[:0],
"num_patches": num_patches[:0],
}
tile_indices: list[int] = []
for image_idx in indices:
start, end = tile_slices[image_idx]
tile_indices.extend(range(start, end))
return {
"pixel_values": pixel_values[tile_indices],
"spatial_shapes": spatial_shapes[tile_indices],
"num_patches": num_patches[indices],
}
def _pack_lfm2vl_pixel_values(
self,
pixel_values: torch.Tensor,
spatial_shapes_list: list[list[int]],
) -> torch.Tensor:
input_lengths = self._get_lfm2vl_tile_input_lengths(spatial_shapes_list)
total_tokens = sum(input_lengths)
packed = pixel_values.new_empty((total_tokens, pixel_values.shape[-1]))
offset = 0
for i, length in enumerate(input_lengths):
if length <= 0:
continue
packed[offset : offset + length].copy_(pixel_values[i, :length])
offset += length
return packed
def _get_lfm2vl_pos_embeds(
self,
spatial_shapes: torch.Tensor,
spatial_shapes_list: list[list[int]],
) -> torch.Tensor:
embeddings = self.vision_tower.vision_model.embeddings
positional_embeddings = embeddings.position_embedding.weight.reshape(
embeddings.position_embedding_size,
embeddings.position_embedding_size,
-1,
)
lengths_list = self._get_lfm2vl_tile_input_lengths(spatial_shapes_list)
return embeddings.resize_positional_embeddings_packed(
positional_embeddings,
spatial_shapes,
lengths_list=lengths_list,
)
def _get_lfm2vl_cu_seqlens(
self,
spatial_shapes_list: list[list[int]],
device: torch.device,
) -> torch.Tensor:
lengths = torch.tensor(
self._get_lfm2vl_tile_input_lengths(spatial_shapes_list),
dtype=torch.int32,
device=device,
)
cu_seqlens = torch.zeros(
lengths.shape[0] + 1,
dtype=torch.int32,
device=device,
)
if lengths.numel() > 0:
cu_seqlens[1:] = torch.cumsum(lengths, dim=0)
return cu_seqlens
def _get_lfm2vl_max_seqlen(
self,
spatial_shapes_list: list[list[int]],
) -> torch.Tensor:
input_lengths = self._get_lfm2vl_tile_input_lengths(spatial_shapes_list)
max_seqlen = max(input_lengths) if input_lengths else 0
return torch.tensor(max_seqlen, dtype=torch.int32)
def _get_lfm2vl_projector_gather_idx(
self,
spatial_shapes_list: list[list[int]],
device: torch.device,
) -> torch.Tensor:
factor = self.multi_modal_projector.factor
dh = torch.arange(factor, dtype=torch.int64)
dw = torch.arange(factor, dtype=torch.int64)
dh_grid, dw_grid = torch.meshgrid(dh, dw, indexing="ij")
dh_flat = dh_grid.reshape(-1)
dw_flat = dw_grid.reshape(-1)
gather_idx_parts: list[torch.Tensor] = []
offset = 0
for height, width in spatial_shapes_list:
length = height * width
if length <= 0:
continue
if height % factor != 0 or width % factor != 0:
raise ValueError(
"spatial_shapes must be divisible by downsample_factor: "
f"got ({height}, {width}) with factor={factor}."
)
rows_out = torch.arange(height // factor, dtype=torch.int64)
cols_out = torch.arange(width // factor, dtype=torch.int64)
rr, cc = torch.meshgrid(rows_out, cols_out, indexing="ij")
rr = rr.reshape(-1)
cc = cc.reshape(-1)
token_idx = (rr[:, None] * factor + dh_flat[None, :]) * width + (
cc[:, None] * factor + dw_flat[None, :]
)
gather_idx_parts.append(token_idx.reshape(-1) + offset)
offset += length
if not gather_idx_parts:
return torch.empty(0, dtype=torch.int64, device=device)
return torch.cat(gather_idx_parts).to(device=device)
def _prepare_lfm2vl_cudagraph_values(
self,
pixel_values: torch.Tensor,
spatial_shapes: torch.Tensor,
) -> dict[str, torch.Tensor]:
spatial_shapes_list = self._get_spatial_shapes_list(spatial_shapes)
pixel_values_packed = self._pack_lfm2vl_pixel_values(
pixel_values,
spatial_shapes_list,
)
pos_embeds = self._get_lfm2vl_pos_embeds(spatial_shapes, spatial_shapes_list)
device = pixel_values.device
return {
"pixel_values_packed": pixel_values_packed,
"pos_embeds": pos_embeds,
"cu_seqlens": self._get_lfm2vl_cu_seqlens(spatial_shapes_list, device),
"max_seqlen": self._get_lfm2vl_max_seqlen(spatial_shapes_list),
"gather_idx": self._get_lfm2vl_projector_gather_idx(
spatial_shapes_list,
device,
),
}
def _get_lfm2vl_capture_spatial_shapes(
self,
token_budget: int,
) -> torch.Tensor:
factor = self.multi_modal_projector.factor
min_image_tokens = self._get_lfm2vl_min_image_tokens()
remaining = token_budget
shapes: list[list[int]] = []
while remaining > 0:
out_tokens = min(remaining, min_image_tokens)
shapes.append([factor, out_tokens * factor])
remaining -= out_tokens
return torch.tensor(shapes, dtype=torch.int64)
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
spatial_shapes = self._get_lfm2vl_capture_spatial_shapes(token_budget)
spatial_shapes_list = self._get_spatial_shapes_list(spatial_shapes)
input_lengths = self._get_lfm2vl_tile_input_lengths(spatial_shapes_list)
total_input_tokens = sum(input_lengths)
patch_dim = (
self.vision_tower.vision_model.embeddings.patch_embedding.weight.shape[1]
)
dummy_pixel_values = torch.randn(
total_input_tokens,
patch_dim,
device=device,
dtype=dtype,
)
pos_embeds = self._get_lfm2vl_pos_embeds(
spatial_shapes,
spatial_shapes_list,
).to(device=device, dtype=dtype)
# max_seqlen.item() is baked into the captured ViT attention graph, so
# capture with a budget-level upper bound that covers any replay item.
max_tile_input_tokens = token_budget * self.multi_modal_projector.factor**2
values = {
"pixel_values_packed": dummy_pixel_values,
"pos_embeds": pos_embeds,
"cu_seqlens": self._get_lfm2vl_cu_seqlens(spatial_shapes_list, device),
"max_seqlen": torch.tensor(max_tile_input_tokens, dtype=torch.int32),
"gather_idx": self._get_lfm2vl_projector_gather_idx(
spatial_shapes_list,
device,
),
}
return EncoderCudaGraphCaptureInputs(values=values)
def prepare_encoder_cudagraph_replay_buffers(
self,
mm_kwargs: dict[str, Any],
max_batch_size: int,
max_frames_per_batch: int,
path: str = "default",
):
from vllm.v1.worker.encoder_cudagraph_defs import (
EncoderCudaGraphReplayBuffers,
)
values = self._prepare_lfm2vl_cudagraph_values(
mm_kwargs["pixel_values"],
mm_kwargs["spatial_shapes"],
)
return EncoderCudaGraphReplayBuffers(values=values)
def encoder_cudagraph_forward(
self,
values: dict[str, torch.Tensor],
path: str = "default",
) -> torch.Tensor:
embeddings = self.vision_tower.vision_model.embeddings
pixel_values = values["pixel_values_packed"].to(
dtype=embeddings.patch_embedding.weight.dtype
)
patch_embeds = embeddings.patch_embedding(pixel_values)
hidden_states = (patch_embeds + values["pos_embeds"]).unsqueeze(0)
with set_forward_context(None, self.vllm_config):
encoder_outputs = self.vision_tower.vision_model.encoder(
inputs_embeds=hidden_states,
cu_seqlens=values["cu_seqlens"],
max_seqlen=values["max_seqlen"],
)
post_layernorm = self.vision_tower.vision_model.post_layernorm
if post_layernorm is not None:
encoder_outputs = post_layernorm(encoder_outputs)
return self.multi_modal_projector.forward_with_gather_idx(
vision_features_packed=encoder_outputs[0],
gather_idx=values["gather_idx"],
)
def encoder_eager_forward(
self,
mm_kwargs: dict[str, Any],
path: str = "default",
) -> torch.Tensor:
image_input = LFM2VLImageInputs(
type="pixel_values",
pixel_values=mm_kwargs["pixel_values"],
spatial_shapes=mm_kwargs["spatial_shapes"],
num_patches=mm_kwargs["num_patches"],
)
return torch.cat(self._process_image_input(image_input), dim=0)
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
connector="multi_modal_projector",
tower_model="vision_tower",
)
def get_mm_lora_token_counts(
self,
*,
modality: str,
mm_kwargs: MultiModalKwargsItem | None,
num_mm_embeds: int,
) -> tuple[int, int | None]:
del modality, mm_kwargs
downsample_factor = self.config.downsample_factor
return num_mm_embeds * downsample_factor**2, num_mm_embeds
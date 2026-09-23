source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/internvl/
lastmod: 2026-09-23

@MULTIMODAL_REGISTRY.register_processor(
InternVLMultiModalProcessor,
info=InternVLProcessingInfo,
dummy_inputs=InternVLDummyInputsBuilder,
)
class InternVLChatModel(
nn.Module,
SupportsMultiModal,
SupportsPP,
SupportsLoRA,
SupportsEncoderCudaGraph,
):
supports_encoder_tp_data = True
supports_tower_connector_lora = True
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_prefix=dict.fromkeys(
[
"action_embed",
"temporal_embed",
"track_embed",
"track_embed_decoder",
"box_token",
"cg_criterion",
"cg_model",
"loc_encoder",
"loc_decoder",
"sam",
"temporal_token",
"track_token",
]
)
)
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("image"):
return "<image>"
if modality.startswith("video"):
return "<video>"
raise ValueError("Only image or video modality is supported")
def __init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
super().__init__()
config = vllm_config.model_config.hf_config
quant_config = vllm_config.quant_config
multimodal_config = vllm_config.model_config.get_multimodal_config()
self.config = config
self.multimodal_config = multimodal_config
self.use_data_parallel = multimodal_config.mm_encoder_tp_mode == "data"
self._patch_quant_config(config, quant_config)
image_size = config.force_image_size or config.vision_config.image_size
patch_size = config.vision_config.patch_size
self.patch_size = patch_size
self.patch_tokens = (image_size // patch_size) ** 2
self.num_image_token = int(self.patch_tokens * (config.downsample_ratio**2))
self.downsample_ratio = config.downsample_ratio
self.ps_version = config.ps_version
with self._mark_tower_model(vllm_config, {"image", "video"}):
self.vision_model = self._init_vision_model(
config,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "vision_model"),
)
self.mlp1 = self._init_mlp1(config)
with self._mark_language_model(vllm_config):
self.language_model = init_vllm_registered_model(
vllm_config=vllm_config,
hf_config=config.text_config,
prefix=maybe_prefix(prefix, "language_model"),
)
self.img_context_token_id: int | None = None
self.video_context_token_id: int | None = None
self.make_empty_intermediate_tensors = (
self.language_model.make_empty_intermediate_tensors
)
def _patch_quant_config(
self, config: PretrainedConfig, quant_config: QuantizationConfig | None
):
# the awq models from OpenGVLab missing `modules_to_not_convert`
# patch the quant_config to add `modules_to_not_convert` back
if isinstance(quant_config, AutoAWQConfig):
text_config = config.text_config
llm_quant_config = getattr(text_config, "quantization_config", None)
if (not quant_config.modules_to_not_convert) and (
llm_quant_config is not None
):
quant_config.modules_to_not_convert.append("vision_model")
def _init_vision_model(
self,
config: PretrainedConfig,
quant_config: QuantizationConfig | None,
*,
prefix: str,
):
vision_feature_layer = config.select_layer
if vision_feature_layer < 0:
num_hidden_layers = (
config.vision_config.num_hidden_layers + vision_feature_layer + 1
)
else:
num_hidden_layers = vision_feature_layer + 1
return InternVisionModel(
config.vision_config,
quant_config=quant_config,
num_hidden_layers_override=num_hidden_layers,
prefix=prefix,
)
def _init_mlp1(self, config: PretrainedConfig) -> nn.Module:
vit_hidden_size = config.vision_config.hidden_size
llm_hidden_size = config.text_config.hidden_size
return nn.Sequential(
nn.LayerNorm(vit_hidden_size * int(1 / self.downsample_ratio) ** 2),
nn.Linear(
vit_hidden_size * int(1 / self.downsample_ratio) ** 2, llm_hidden_size
),
nn.GELU(),
nn.Linear(llm_hidden_size, llm_hidden_size),
)
def pixel_shuffle(self, x, scale_factor=0.5):
n, w, h, c = x.size()
# N, W, H, C --> N, W, H * scale, C // scale
x = x.view(n, w, int(h * scale_factor), int(c / scale_factor))
# N, W, H * scale, C // scale --> N, H * scale, W, C // scale
x = x.permute(0, 2, 1, 3).contiguous()
x = x.view(
n,
int(h * scale_factor),
int(w * scale_factor),
int(c / (scale_factor * scale_factor)),
)
if self.ps_version == "v1":
pass
else:
x = x.permute(0, 2, 1, 3).contiguous()
return x
def extract_feature(self, pixel_values: torch.Tensor) -> torch.Tensor:
vit_embeds = self.vision_model(pixel_values=pixel_values)
vit_embeds = vit_embeds[:, 1:, :]
h = w = int(vit_embeds.shape[1] ** 0.5)
vit_embeds = vit_embeds.reshape(vit_embeds.shape[0], h, w, -1)
vit_embeds = self.pixel_shuffle(vit_embeds, scale_factor=self.downsample_ratio)
vit_embeds = vit_embeds.reshape(vit_embeds.shape[0], -1, vit_embeds.shape[-1])
vit_embeds = self.mlp1(vit_embeds)
return vit_embeds
def _parse_and_validate_image_input(
self, **kwargs: object
) -> InternVLImageInputs | None:
pixel_values_flat = kwargs.pop("pixel_values_flat", None)
image_num_patches = kwargs.pop("image_num_patches", None)
image_embeds = kwargs.pop("image_embeds", None)
if pixel_values_flat is None and image_embeds is None:
return None
if image_embeds is not None:
return InternVLImageEmbeddingInputs(
type="image_embeds",
data=image_embeds,
)
image_token_id = kwargs["image_token_id"]
if isinstance(image_token_id, torch.Tensor):
image_token_id = image_token_id.flatten().unique().item()
assert isinstance(image_token_id, int)
self.img_context_token_id = image_token_id
if pixel_values_flat is not None:
expected_h = expected_w = self.config.vision_config.image_size
resolve_bindings = {"h": expected_h, "w": expected_w}
return InternVLImagePixelInputs(
type="pixel_values",
pixel_values_flat=pixel_values_flat,
num_patches=image_num_patches,
resolve_bindings=resolve_bindings,
)
raise AssertionError("This line should be unreachable.")
def _parse_and_validate_video_input(
self, **kwargs: object
) -> InternVLVideoInputs | None:
pixel_values_flat_video = kwargs.pop("pixel_values_flat_video", None)
video_num_patches = kwargs.pop("video_num_patches", None)
video_embeds = kwargs.pop("video_embeds", None)
if pixel_values_flat_video is None and video_embeds is None:
return None
if video_embeds is not None:
return InternVLVideoEmbeddingInputs(
type="video_embeds",
data=video_embeds,
)
video_token_id = kwargs["video_token_id"]
if isinstance(video_token_id, torch.Tensor):
video_token_id = video_token_id.flatten().unique().item()
assert isinstance(video_token_id, int)
self.video_context_token_id = video_token_id
if pixel_values_flat_video is not None:
expected_h = expected_w = self.config.vision_config.image_size
resolve_bindings = {"h": expected_h, "w": expected_w}
return InternVLVideoPixelInputs(
type="pixel_values_videos",
pixel_values_flat=pixel_values_flat_video,
num_patches=video_num_patches,
resolve_bindings=resolve_bindings,
)
raise AssertionError("This line should be unreachable.")
def _process_vision_input(
self,
image_input: InternVLImageInputs | InternVLVideoInputs,
) -> tuple[torch.Tensor, ...]:
if (
image_input["type"] == "image_embeds"
or image_input["type"] == "video_embeds"
):
return image_input["data"]
image_embeds = self.extract_feature(image_input["pixel_values_flat"])
num_patches = image_input["num_patches"]
# Only one image in the current batch
if len(num_patches) == 1:
return (image_embeds.view(-1, self.config.text_config.hidden_size),)
# NOTE: Image embeddings are split into separate tensors for each image
# by the size of each embedding.
feature_size = image_embeds.shape[1]
image_embeds = image_embeds.view(-1, self.config.text_config.hidden_size)
image_feature_sizes = [
num_patches * feature_size for num_patches in num_patches
]
return image_embeds.split(image_feature_sizes)
def _parse_and_validate_multimodal_inputs(
self, **kwargs: object
) -> InternVLMultiModalInputs:
modalities: InternVLMultiModalInputs = {}
# Preserve the order of modalities if there are multiple of them
# from the order of kwargs.
for input_key in kwargs:
if (
input_key in ("pixel_values_flat", "image_embeds")
and "images" not in modalities
):
modalities["images"] = self._parse_and_validate_image_input(**kwargs)
if input_key in ("pixel_values_flat_video",) and "videos" not in modalities:
modalities["videos"] = self._parse_and_validate_video_input(**kwargs)
return modalities
def embed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
modalities = self._parse_and_validate_multimodal_inputs(**kwargs)
if not modalities:
return []
# The result multimodal_embeddings is tuple of tensors, with each
# tensor correspoending to a multimodal data item (image or video).
multimodal_embeddings: tuple[torch.Tensor, ...] = ()
# NOTE: It is important to iterate over the keys in this dictionary
# to preserve the order of the modalities.
for modality in modalities:
if modality == "images":
image_input = modalities["images"]
if image_input is not None:
image_embeddings = self._process_vision_input(image_input)
multimodal_embeddings += tuple(image_embeddings)
if modality == "videos":
video_input = modalities["videos"]
if video_input is not None:
video_embeddings = self._process_vision_input(video_input)
multimodal_embeddings += tuple(video_embeddings)
return multimodal_embeddings
def embed_input_ids(
self,
input_ids: torch.Tensor,
multimodal_embeddings: MultiModalEmbeddings | None = None,
*,
is_multimodal: torch.Tensor | None = None,
) -> torch.Tensor:
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
**kwargs: object,
) -> IntermediateTensors:
if intermediate_tensors is not None:
inputs_embeds = None
forward_kwargs = {
"input_ids": input_ids,
"positions": positions,
"intermediate_tensors": intermediate_tensors,
"inputs_embeds": inputs_embeds,
}
hidden_states = self.language_model.model(**forward_kwargs)
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
connector="mlp1",
tower_model="vision_model",
)
def get_mm_lora_token_counts(
self,
*,
modality: str,
mm_kwargs: MultiModalKwargsItem | None,
num_mm_embeds: int,
) -> tuple[int, int | None]:
del modality, mm_kwargs
if num_mm_embeds <= 0 or self.num_image_token <= 0:
return 0, 0
num_patches = num_mm_embeds // self.num_image_token
tower_tokens = num_patches * (self.patch_tokens + 1)
return tower_tokens, num_patches * self.num_image_token
# -- SupportsEncoderCudaGraph protocol methods --
def get_encoder_cudagraph_config(self):
from vllm.v1.worker.encoder_cudagraph_defs import EncoderCudaGraphConfig
return EncoderCudaGraphConfig(
modalities=["image", "video"],
# InternVision uses standard ViT attention (no rotary embeddings,
# no variable-length sequence metadata), so the only graph-recorded
# buffer is pixel_values_flat itself.
buffer_keys=["pixel_values_flat"],
out_hidden_size=self.config.text_config.hidden_size,
)
def get_input_modality(
self,
mm_kwargs: dict[str, Any],
) -> str:
if "pixel_values_flat" in mm_kwargs:
return "image"
return "video"
def get_encoder_cudagraph_budget_range(
self,
vllm_config: "VllmConfig",
) -> tuple[int, int]:
# Min: 1 tile → num_image_token output tokens.
min_budget = self.num_image_token
max_budget = min(
vllm_config.scheduler_config.max_num_batched_tokens,
vllm_config.model_config.max_model_len,
)
return (min_budget, max_budget)
def _get_internvl_patches_list(
self,
mm_kwargs: dict[str, Any],
) -> list[int]:
"""Return per-item tile counts as a plain list of ints."""
if self.get_input_modality(mm_kwargs) == "image":
patches = mm_kwargs.get("image_num_patches", [])
else:
patches = mm_kwargs.get("video_num_patches", [])
if isinstance(patches, torch.Tensor):
return patches.tolist()
return [int(n) for n in patches]
def get_encoder_cudagraph_item_specs(
self,
mm_kwargs: dict[str, Any],
):
from vllm.v1.worker.encoder_cudagraph_defs import EncoderItemSpec
return [
EncoderItemSpec(
input_size=n,
output_tokens=n * self.num_image_token,
)
for n in self._get_internvl_patches_list(mm_kwargs)
]
def select_encoder_cudagraph_items(
self,
mm_kwargs: dict[str, Any],
indices: list[int],
) -> dict[str, Any]:
modality = self.get_input_modality(mm_kwargs)
pv_key = (
"pixel_values_flat" if modality == "image" else "pixel_values_flat_video"
)
patches_key = (
"image_num_patches" if modality == "image" else "video_num_patches"
)
pixel_values = mm_kwargs[pv_key]
patches_list = self._get_internvl_patches_list(mm_kwargs)
if len(indices) == 0:
return {pv_key: pixel_values[:0], patches_key: []}
# Compute cumulative tile offsets for slicing pixel_values.
cum_patches = [0]
for n in patches_list:
cum_patches.append(cum_patches[-1] + n)
selected_pv = torch.cat(
[pixel_values[cum_patches[i] : cum_patches[i + 1]] for i in indices]
)
selected_patches = [patches_list[i] for i in indices]
return {pv_key: selected_pv, patches_key: selected_patches}
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
# Size the buffer to hold the maximum possible tiles for this budget.
total_tiles = max(token_budget // self.num_image_token, 1)
image_size = self.config.vision_config.image_size
dummy_pixel_values = torch.randn(
total_tiles, 3, image_size, image_size, device=device, dtype=dtype
)
return EncoderCudaGraphCaptureInputs(
values={"pixel_values_flat": dummy_pixel_values},
)
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
modality = self.get_input_modality(mm_kwargs)
pv_key = (
"pixel_values_flat" if modality == "image" else "pixel_values_flat_video"
)
return EncoderCudaGraphReplayBuffers(
values={"pixel_values_flat": mm_kwargs[pv_key]},
)
def encoder_cudagraph_forward(
self,
values: dict[str, torch.Tensor],
path: str = "default",
) -> torch.Tensor:
# The graph is always captured with pixel_values_flat as the input
# buffer. During video replay the manager copies video tiles into
# this same buffer before calling graph.replay(), so we always read
# from pixel_values_flat here.
pixel_values = values["pixel_values_flat"]
out = self.extract_feature(pixel_values) # [N, num_image_token, H]
return out.view(-1, self.config.text_config.hidden_size)
def encoder_eager_forward(
self,
mm_kwargs: dict[str, Any],
path: str = "default",
) -> torch.Tensor:
if self.get_input_modality(mm_kwargs) == "image":
pixel_values = mm_kwargs["pixel_values_flat"]
else:
pixel_values = mm_kwargs["pixel_values_flat_video"]
out = self.extract_feature(pixel_values) # [N, num_image_token, H]
return out.view(-1, self.config.text_config.hidden_size)
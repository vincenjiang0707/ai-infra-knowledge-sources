source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/keye/
lastmod: 2026-09-24

class BaseKeyeModule(nn.Module, SupportsMultiModal):
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
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_prefix={
"lm_head.": "language_model.lm_head.",
"model.": "language_model.model.",
}
)
supports_tower_connector_lora = True
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("image"):
return "<|vision_start|><|image_pad|><|vision_end|>"
if modality.startswith("video"):
return "<|vision_start|><|video_pad|><|vision_end|>"
raise ValueError("Only image or video modality is supported")
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
config: PreTrainedConfig = vllm_config.model_config.hf_config
quant_config = vllm_config.quant_config
self.config = config
with self._mark_tower_model(vllm_config, {"image", "video"}):
self.visual = KeyeSiglipVisionModel(
config.vision_config,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "visual"),
)
self.mlp_AR = self._build_projector(
config,
config.vision_config,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "mlp_AR"),
)
with self._mark_language_model(vllm_config):
self.language_model = init_vllm_registered_model(
vllm_config=vllm_config,
prefix=maybe_prefix(prefix, "language_model"),
architectures=["Qwen3ForCausalLM"],
)
self.make_empty_intermediate_tensors = (
self.language_model.make_empty_intermediate_tensors
)
@abstractmethod
def _build_projector(
self,
text_config: PreTrainedConfig,
vision_config: PreTrainedConfig,
quant_config: QuantizationConfig | None = None,
prefix: str = "",
) -> nn.Module:
raise NotImplementedError("Need projector")
def _process_image_input(self, image_input: Any) -> tuple[torch.Tensor, ...]:
siglip_position_ids = list()
image_grid_hws = list()
sample_indices = list()
cu_seqlens = [0]
image_grid_thw = image_input["image_grid_thw"]
assert image_grid_thw.ndim == 2
image_grid_thw_list = image_grid_thw.tolist()
for idx, thw in enumerate(image_grid_thw_list):
thw_tuple = tuple(thw)
numel = np.prod(thw_tuple)
image_grid_hws.append(thw_tuple)
image_position_ids = torch.arange(numel) % np.prod(thw_tuple[1:])
siglip_position_ids.append(image_position_ids)
sample_indices.append(torch.full((numel,), idx, dtype=torch.int64))
cu_seqlens.append(cu_seqlens[-1] + numel)
if image_input["type"] == "image_embeds":
raise ValueError(
"Image embeddings are not supported for this processing path."
)
else:
pixel_values = image_input["pixel_values"].type(self.visual.dtype)
# These are all built on the host; concat straight into pinned
# buffers so the H2D copies stay non-blocking.
siglip_position_ids = torch.concat(
siglip_position_ids,
dim=0,
out=torch.empty(
sum(t.numel() for t in siglip_position_ids),
dtype=torch.int64,
pin_memory=PIN_MEMORY,
),
).to(pixel_values.device, non_blocking=True)
cu_seqlens = async_tensor_h2d(
cu_seqlens, dtype=torch.int32, device=pixel_values.device
)
sample_indices = torch.concat(
sample_indices,
dim=0,
out=torch.empty(
sum(t.numel() for t in sample_indices),
dtype=torch.int64,
pin_memory=PIN_MEMORY,
),
).to(pixel_values.device, non_blocking=True)
image_embeds = self.visual(
pixel_values=pixel_values,
image_grid_thw=image_grid_hws,
position_ids=siglip_position_ids,
vision_return_embed_list=False,
interpolate_pos_encoding=True,
sample_indices=sample_indices,
cu_seqlens=cu_seqlens,
use_rope=True,
window_size=-1,
)
image_embeds = tuple(self.mlp_AR(image_embeds, image_grid_thw))
return image_embeds
def _process_video_embeds(
self,
video_type: Literal["video_embeds", "pixel_values_videos"],
video_grid_thw: list[torch.Tensor],
pixel_values_videos: torch.Tensor | None = None,
) -> torch.Tensor | list[torch.Tensor]:
siglip_position_ids = list()
video_grid_hws = list()
sample_indices = list()
cu_seqlens = [0]
assert video_grid_thw.ndim == 2
for idx, sub_thw in enumerate(video_grid_thw):
thw_tuple = tuple(sub_thw.detach().cpu().numpy().tolist())
numel = np.prod(thw_tuple)
video_grid_hws.append(thw_tuple)
video_position_ids = torch.arange(numel) % np.prod(thw_tuple[1:])
siglip_position_ids.append(video_position_ids)
sample_indices.append(torch.full((numel,), idx, dtype=torch.int64))
cu_seqlens.append(cu_seqlens[-1] + numel)
if video_type == "video_embeds":
raise ValueError(
"Video embeddings are not supported for this processing path."
)
else:
pixel_values_videos = pixel_values_videos.type(self.visual.dtype)
# These are host-built; concat straight into pinned buffers so
# the H2D copies stay non-blocking.
siglip_position_ids = torch.concat(
siglip_position_ids,
dim=0,
out=torch.empty(
sum(t.numel() for t in siglip_position_ids),
dtype=torch.int64,
pin_memory=PIN_MEMORY,
),
).to(pixel_values_videos.device, non_blocking=True)
cu_seqlens = async_tensor_h2d(
cu_seqlens, dtype=torch.int32, device=pixel_values_videos.device
)
sample_indices = torch.concat(
sample_indices,
dim=0,
out=torch.empty(
sum(t.numel() for t in sample_indices),
dtype=torch.int64,
pin_memory=PIN_MEMORY,
),
).to(pixel_values_videos.device, non_blocking=True)
video_embeds = self.visual(
pixel_values=pixel_values_videos,
image_grid_thw=video_grid_hws,
position_ids=siglip_position_ids,
vision_return_embed_list=True,
interpolate_pos_encoding=True,
sample_indices=sample_indices,
cu_seqlens=cu_seqlens,
use_rope=True,
window_size=-1,
)
video_embeds = self.mlp_AR(video_embeds, video_grid_thw)
return video_embeds
def _parse_and_validate_multimodal_inputs(self, **kwargs: object) -> dict:
modalities = {}
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
multimodal_embeddings: tuple[torch.Tensor, ...] = ()
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
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
**kwargs: object,
) -> torch.Tensor | IntermediateTensors:
"""Run forward pass for Keye-VL.
Args:
input_ids: Flattened (concatenated) input_ids corresponding to a
batch.
positions: Flattened (concatenated) position ids corresponding to a
batch.
**NOTE**: If mrope is enabled (default setting for Qwen2-VL
opensource models), the shape will be `(3, seq_len)`,
otherwise it will be `(seq_len,)`.
intermediate_tensors: Intermediate tensors from prior forward pass.
inputs_embeds: Optional tensor of input embeddings.
**kwargs: Multimodal inputs for this batch, forwarded to the
multimodal embedding path.
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
language_model="language_model",
connector="mlp_AR.",
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
return num_mm_embeds * merge_size**2, num_mm_embeds
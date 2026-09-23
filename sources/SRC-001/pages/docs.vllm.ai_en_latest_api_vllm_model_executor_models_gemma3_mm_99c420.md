source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gemma3_mm/
lastmod: 2026-09-23

@MULTIMODAL_REGISTRY.register_processor(
Gemma3MultiModalProcessor,
info=Gemma3ProcessingInfo,
dummy_inputs=Gemma3DummyInputsBuilder,
)
class Gemma3ForConditionalGeneration(
nn.Module, SupportsMultiModal, SupportsPP, SupportsLoRA, SupportsEncoderCudaGraph
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
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_prefix={
# mapping for new names in checkpoint saved after transformers v4.52
"model.language_model.": "language_model.model.",
"model.vision_tower.": "vision_tower.",
"model.multi_modal_projector.": "multi_modal_projector.",
"lm_head.": "language_model.lm_head.",
}
)
supports_tower_connector_lora = True
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("image"):
return "<start_of_image>"
raise ValueError("Only image modality is supported")
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
config = vllm_config.model_config.hf_config
quant_config = vllm_config.quant_config
multimodal_config = vllm_config.model_config.multimodal_config
self.config = config
self.model_config = vllm_config.model_config
self.quant_config = quant_config
self.multimodal_config = multimodal_config
self.vit_positions_per_patch = (
self.config.vision_config.image_size // self.config.vision_config.patch_size
) ** 2
self.configure_mm_token_handling(
vocab_size=config.text_config.vocab_size,
mm_token_ids=[config.image_token_index],
)
with self._mark_tower_model(vllm_config, "image"):
self.vision_tower = SiglipVisionModel(
config.vision_config,
quant_config,
prefix=maybe_prefix(prefix, "vision_tower"),
)
self.multi_modal_projector = Gemma3MultiModalProjector(config)
with self._mark_language_model(vllm_config):
self.language_model = init_vllm_registered_model(
vllm_config=vllm_config,
hf_config=config.text_config,
prefix=maybe_prefix(prefix, "language_model"),
architectures=["Gemma3ForCausalLM"],
)
logit_scale = getattr(config, "logit_scale", 1.0)
self.language_model.logits_processor.scale *= logit_scale
self.make_empty_intermediate_tensors = (
self.language_model.make_empty_intermediate_tensors
)
@property
def dtype(self):
return next(self.parameters()).dtype
def _parse_and_validate_image_input(
self, **kwargs: object
) -> Gemma3ImageInputs | None:
pixel_values = kwargs.pop("pixel_values", None)
num_patches = kwargs.pop("num_patches", None)
image_embeds = kwargs.pop("image_embeds", None)
assert image_embeds is None, "Gemma3 does not support image_embeds."
if pixel_values is None:
return None
image_size = self.config.vision_config.image_size
return Gemma3ImagePixelInputs(
pixel_values=pixel_values,
num_patches=num_patches,
resolve_bindings={"h": image_size, "w": image_size},
)
def _image_pixels_to_features(
self,
vision_tower: SiglipVisionModel,
pixel_values: torch.Tensor,
) -> torch.Tensor:
return vision_tower(pixel_values)
def _process_image_input(
self,
image_input: Gemma3ImageInputs,
) -> list[torch.Tensor]:
pixel_values = image_input["pixel_values"]
num_patches = image_input["num_patches"]
image_features = self._image_pixels_to_features(
self.vision_tower,
pixel_values,
)
image_embeds = self.multi_modal_projector(image_features)
return [e.flatten(0, 1) for e in image_embeds.split(num_patches.tolist())]
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
# Early return for text-only inference (no multimodal data)
if multimodal_embeddings is None or is_multimodal is None:
return super().embed_input_ids(input_ids)
# Use interface default with OOV handling enabled
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
hidden_states = self.language_model.model(
input_ids,
positions,
intermediate_tensors,
inputs_embeds=inputs_embeds,
**kwargs,
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
"""Get the module prefix in multimodal models"""
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
tower_tokens = num_mm_embeds * 16
return tower_tokens, tower_tokens
def get_encoder_cudagraph_config(self):
from vllm.v1.worker.encoder_cudagraph_defs import (
EncoderCudaGraphConfig,
)
return EncoderCudaGraphConfig(
modalities=["image"],
buffer_keys=["pixel_values"],
out_hidden_size=self.config.text_config.hidden_size,
)
def get_encoder_cudagraph_budget_range(
self,
vllm_config: VllmConfig,
) -> tuple[int, int]:
min_budget = self.config.mm_tokens_per_image
max_budget = min(
vllm_config.scheduler_config.max_num_batched_tokens,
self.model_config.max_model_len,
)
return (min_budget, max_budget)
def get_encoder_cudagraph_item_specs(
self,
mm_kwargs: dict[str, Any],
):
from vllm.v1.worker.encoder_cudagraph_defs import EncoderItemSpec
num_patches = mm_kwargs["num_patches"]
mm_tokens_per_image = self.config.mm_tokens_per_image
return [
EncoderItemSpec(
input_size=int(np) * self.vit_positions_per_patch,
output_tokens=int(np) * mm_tokens_per_image,
)
for np in num_patches
]
def select_encoder_cudagraph_items(
self,
mm_kwargs: dict[str, Any],
indices: list[int],
) -> dict[str, Any]:
pixel_values = mm_kwargs["pixel_values"]
num_patches = mm_kwargs["num_patches"]
if len(indices) == 0:
return {
"pixel_values": pixel_values[:0],
"num_patches": num_patches[:0],
}
cum_patches = [0]
for p in num_patches:
cum_patches.append(cum_patches[-1] + int(p))
selected_pv = torch.cat(
[pixel_values[cum_patches[i] : cum_patches[i + 1]] for i in indices]
)
selected_np = num_patches[indices]
return {
"pixel_values": selected_pv,
"num_patches": selected_np,
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
mm_tokens_per_image = self.config.mm_tokens_per_image
num_images = min(
token_budget // mm_tokens_per_image,
max_batch_size,
)
image_size = self.config.vision_config.image_size
dummy_pixel_values = torch.randn(
num_images,
3,
image_size,
image_size,
device=device,
dtype=dtype,
)
values = {"pixel_values": dummy_pixel_values}
return EncoderCudaGraphCaptureInputs(
values,
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
return EncoderCudaGraphReplayBuffers(
values={"pixel_values": mm_kwargs["pixel_values"]},
)
def encoder_cudagraph_forward(
self,
values: dict[str, torch.Tensor],
path: str = "default",
) -> torch.Tensor:
pixel_values = values["pixel_values"]
image_features = self.vision_tower(pixel_values)
image_features = self.multi_modal_projector(image_features)
return image_features.flatten(end_dim=1)
def encoder_eager_forward(
self,
mm_kwargs: dict[str, Any],
path: str = "default",
) -> torch.Tensor:
image_input = self._parse_and_validate_image_input(**mm_kwargs)
assert image_input is not None
results = self._process_image_input(image_input)
return torch.cat(results, dim=0)
source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/idefics3/
lastmod: 2026-09-24

@MULTIMODAL_REGISTRY.register_processor(
Idefics3MultiModalProcessor,
info=Idefics3ProcessingInfo,
dummy_inputs=Idefics3DummyInputsBuilder,
)
class Idefics3ForConditionalGeneration(
nn.Module, SupportsMultiModal, SupportsLoRA, SupportsEncoderCudaGraph
):
supports_encoder_cudagraph = True
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
supports_tower_connector_lora = True
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("image"):
return "<image>"
raise ValueError("Only image modality is supported")
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
config = vllm_config.model_config.hf_config
quant_config = vllm_config.quant_config
multimodal_config = vllm_config.model_config.multimodal_config
self.config = config
self.multimodal_config = multimodal_config
with self._mark_composite_model(
vllm_config,
language_targets=LlamaModel,
tower_targets={"image": (Idefics3VisionTransformer, Idefics3Connector)},
):
self.model = Idefics3Model(
vllm_config=vllm_config,
prefix=maybe_prefix(prefix, "model"),
)
self.image_token_id = self.config.image_token_id
self.lm_head = ParallelLMHead(
config.text_config.vocab_size,
config.text_config.hidden_size,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "lm_head"),
)
if self.config.text_config.tie_word_embeddings:
self.lm_head = self.lm_head.tie_weights(self.model.text_model.embed_tokens)
self.logits_processor = LogitsProcessor(config.text_config.vocab_size)
def _parse_and_validate_image_input(self, **kwargs: object) -> ImageInputs | None:
pixel_values = kwargs.pop("pixel_values", None)
image_embeds = kwargs.pop("image_embeds", None)
if pixel_values is None and image_embeds is None:
return None
if image_embeds is not None:
return Idefics3ImageEmbeddingInputs(
type="image_embeds",
data=image_embeds,
)
if pixel_values is not None:
pixel_attention_mask = kwargs.pop("pixel_attention_mask")
num_patches = kwargs.pop("num_patches")
expected_h = expected_w = self.config.vision_config.image_size
return Idefics3ImagePixelInputs(
type="pixel_values",
pixel_values=pixel_values,
pixel_attention_mask=pixel_attention_mask,
num_patches=num_patches,
resolve_bindings={"h": expected_h, "w": expected_w},
)
raise AssertionError("This line should be unreachable.")
def _process_image_pixels(self, inputs: Idefics3ImagePixelInputs) -> torch.Tensor:
pixel_values = inputs["pixel_values"]
pixel_attention_mask = inputs["pixel_attention_mask"]
return self.model.image_pixels_to_features(
pixel_values,
pixel_attention_mask=pixel_attention_mask,
)
def _process_image_input(
self,
image_input: ImageInputs,
) -> torch.Tensor | list[torch.Tensor]:
if image_input["type"] == "image_embeds":
return image_input["data"]
assert isinstance(image_input, Idefics3ImagePixelInputs)
image_features = self._process_image_pixels(image_input)
image_features = self.model.connector(image_features)
num_patches = image_input["num_patches"]
return [e.flatten(0, 1) for e in image_features.split(num_patches.tolist())]
# -- SupportsEncoderCudaGraph protocol methods --
def get_encoder_cudagraph_config(self):
from vllm.v1.worker.encoder_cudagraph_defs import EncoderCudaGraphConfig
return EncoderCudaGraphConfig(
modalities=["image"],
buffer_keys=["pixel_values", "pixel_attention_mask", "position_ids"],
out_hidden_size=self.config.text_config.hidden_size,
)
def get_encoder_cudagraph_budget_range(
self,
vllm_config: VllmConfig,
) -> tuple[int, int]:
min_budget = self.model.image_seq_len
max_budget = min(
vllm_config.scheduler_config.max_num_batched_tokens,
vllm_config.model_config.max_model_len,
)
return (min_budget, max_budget)
def _get_num_patches_list(self, mm_kwargs: dict[str, Any]) -> list[int]:
num_patches = mm_kwargs["num_patches"]
if isinstance(num_patches, torch.Tensor):
return num_patches.tolist()
return [int(n) for n in num_patches]
def get_encoder_cudagraph_item_specs(
self,
mm_kwargs: dict[str, Any],
):
from vllm.v1.worker.encoder_cudagraph_defs import EncoderItemSpec
return [
EncoderItemSpec(
input_size=num_patches,
output_tokens=num_patches * self.model.image_seq_len,
)
for num_patches in self._get_num_patches_list(mm_kwargs)
]
def select_encoder_cudagraph_items(
self,
mm_kwargs: dict[str, Any],
indices: list[int],
) -> dict[str, Any]:
pixel_values = mm_kwargs["pixel_values"]
pixel_attention_mask = mm_kwargs["pixel_attention_mask"]
num_patches_list = self._get_num_patches_list(mm_kwargs)
if len(indices) == 0:
return {
"pixel_values": pixel_values[:0],
"pixel_attention_mask": pixel_attention_mask[:0],
"num_patches": torch.empty(
(0,), dtype=torch.long, device=pixel_values.device
),
}
cum_patches = [0]
for num_patches in num_patches_list:
cum_patches.append(cum_patches[-1] + num_patches)
selected_pixel_values = torch.cat(
[pixel_values[cum_patches[i] : cum_patches[i + 1]] for i in indices]
)
selected_attention_mask = torch.cat(
[pixel_attention_mask[cum_patches[i] : cum_patches[i + 1]] for i in indices]
)
selected_num_patches = torch.tensor(
[num_patches_list[i] for i in indices],
dtype=torch.long,
device=pixel_values.device,
)
return {
"pixel_values": selected_pixel_values,
"pixel_attention_mask": selected_attention_mask,
"num_patches": selected_num_patches,
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
image_size = self.config.vision_config.image_size
num_tiles = max(
(token_budget + self.model.image_seq_len - 1) // self.model.image_seq_len,
1,
)
dummy_pixel_values = torch.randn(
num_tiles, 3, image_size, image_size, device=device, dtype=dtype
)
dummy_pixel_attention_mask = torch.ones(
num_tiles, image_size, image_size, device=device, dtype=torch.bool
)
dummy_position_ids = self.model.get_position_ids(dummy_pixel_attention_mask)
return EncoderCudaGraphCaptureInputs(
values={
"pixel_values": dummy_pixel_values,
"pixel_attention_mask": dummy_pixel_attention_mask,
"position_ids": dummy_position_ids,
}
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
values={
"pixel_values": mm_kwargs["pixel_values"],
"pixel_attention_mask": mm_kwargs["pixel_attention_mask"],
"position_ids": self.model.get_position_ids(
mm_kwargs["pixel_attention_mask"]
),
}
)
def encoder_cudagraph_forward(
self,
inputs: dict[str, torch.Tensor],
path: str = "default",
) -> torch.Tensor:
image_features = self.model.image_pixels_to_features(
inputs["pixel_values"],
pixel_attention_mask=inputs["pixel_attention_mask"],
remove_padding=False,
position_ids=inputs["position_ids"],
)
image_features = self.model.connector(image_features)
return image_features.flatten(0, 1)
def encoder_eager_forward(
self,
mm_kwargs: dict[str, Any],
path: str = "default",
) -> torch.Tensor:
image_input = self._parse_and_validate_image_input(**mm_kwargs)
assert isinstance(image_input, Idefics3ImagePixelInputs)
image_features = self._process_image_pixels(image_input)
image_features = self.model.connector(image_features)
return image_features.flatten(0, 1)
def embed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
image_input = self._parse_and_validate_image_input(**kwargs)
if image_input is None:
return []
return self._process_image_input(image_input)
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
hidden_states = self.model.text_model(
input_ids, positions, intermediate_tensors, inputs_embeds=inputs_embeds
)
return hidden_states
def compute_logits(self, hidden_states: torch.Tensor) -> torch.Tensor:
logits = self.logits_processor(self.lm_head, hidden_states)
return logits
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
loader = AutoWeightsLoader(self)
return loader.load_weights(weights)
def get_mm_mapping(self) -> MultiModelKeys:
"""Get the module prefix in multimodal models."""
return MultiModelKeys.from_string_field(
language_model="model.text_model",
connector="model.connector",
tower_model="model.vision_model",
)
def get_mm_lora_token_counts(
self,
*,
modality: str,
mm_kwargs: MultiModalKwargsItem | None,
num_mm_embeds: int,
) -> tuple[int, int | None]:
del modality, mm_kwargs
hf_config = self.config
scale_factor = hf_config.scale_factor
return num_mm_embeds * scale_factor**2, num_mm_embeds
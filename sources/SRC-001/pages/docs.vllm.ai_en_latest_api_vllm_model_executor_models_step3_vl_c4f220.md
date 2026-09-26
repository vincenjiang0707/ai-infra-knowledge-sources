source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/step3_vl/
lastmod: 2026-09-24

@MULTIMODAL_REGISTRY.register_processor(
Step3VLMultiModalProcessor,
info=Step3VLProcessingInfo,
dummy_inputs=Step3VLDummyInputsBuilder,
)
class Step3VLForConditionalGeneration(
nn.Module, SupportsMultiModal, SupportsPP, SupportsEncoderCudaGraph
):
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_prefix={
"model.": "language_model.model.",
"lm_head.": "language_model.lm_head.",
}
)
supports_encoder_tp_data = True
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("image"):
return "<im_patch>"
raise ValueError("Only image modality is supported")
def __init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
super().__init__()
config = vllm_config.model_config.hf_config
multimodal_config = vllm_config.model_config.get_multimodal_config()
self.config = config
self.model_config = vllm_config.model_config
self.multimodal_config = multimodal_config
self.use_data_parallel = multimodal_config.mm_encoder_tp_mode == "data"
# NOTE: This behavior is consistent with the previous OOV handling,
# but does not currently handle the start/stop toks around the
# image features (<patch_start> <patch_end> <im_start> <im_end>)
# See: https://huggingface.co/stepfun-ai/step3/blob/main/processing_step3v.py#L323
#
# If this becomes an issue or we refactor to handle this using the
# processor info in the future, it would probably be best to handle
# those too.
self.configure_mm_token_handling(
self.config.text_config.vocab_size,
[self.config.image_token_id],
)
with self._mark_tower_model(vllm_config, "image"):
self.vision_model = Step3VisionTransformer(
config.vision_config,
None,
prefix=maybe_prefix(prefix, "vision_model"),
)
self.vit_downsampler = Conv2dLayer(
config.vision_config.hidden_size,
config.vision_config.output_hidden_size,
kernel_size=2,
stride=config.understand_projector_stride,
)
self.vit_downsampler2 = Conv2dLayer(
config.vision_config.output_hidden_size,
config.vision_config.output_hidden_size * 2,
kernel_size=3,
stride=2,
padding=1,
)
self.vit_large_projector = nn.Linear(
config.vision_config.output_hidden_size * 2,
config.hidden_size,
bias=config.projector_bias,
)
with self._mark_language_model(vllm_config):
language_model = init_vllm_registered_model(
vllm_config=vllm_config,
hf_config=config.text_config,
prefix=maybe_prefix(prefix, "language_model"),
)
self.language_model = language_model
assert supports_pp(language_model)
self.make_empty_intermediate_tensors = (
language_model.make_empty_intermediate_tensors
)
@property
def device(self):
return next(self.parameters()).device
@property
def dtype(self):
return next(self.parameters()).dtype
@staticmethod
def _compute_spatial_tokens(size, patch_size, stride):
# Compute the number of spatial tokens after two rounds of
# downsampling with given patch size and stride.
grid = size // patch_size
vit_tokens = grid * grid
spatial = int(math.sqrt(vit_tokens))
h1 = (spatial - 2) // stride + 1
h2 = (h1 - 1) // 2 + 1
return h2 * h2
@property
def img_output_tokens(self) -> int:
return self._compute_spatial_tokens(
self.config.vision_config.image_size,
self.config.vision_config.patch_size,
self.config.understand_projector_stride,
)
@property
def patch_output_tokens(self) -> int:
return self._compute_spatial_tokens(
504,
self.config.vision_config.patch_size,
self.config.understand_projector_stride,
)
def _batched_encoder_forward(
self,
pixel_values: torch.Tensor,
) -> torch.Tensor:
image_features = self._process_image_features(
self._get_vision_model_output(pixel_values)
)
return image_features.reshape(-1, image_features.shape[-1])
def _parse_and_validate_image_input(
self, **kwargs: object
) -> Step3VLImageInputs | None:
pixel_values = kwargs.pop("pixel_values", None)
patch_pixel_values = kwargs.pop("patch_pixel_values", None)
num_patches = kwargs.pop("num_patches", None)
image_embeds = kwargs.pop("image_embeds", None)
if pixel_values is None and image_embeds is None:
return None
if pixel_values is not None and patch_pixel_values is not None:
assert isinstance(pixel_values, torch.Tensor)
assert isinstance(patch_pixel_values, torch.Tensor)
assert isinstance(num_patches, torch.Tensor)
return Step3VLImagePixelInputs(
type="pixel_values",
pixel_values=pixel_values.to(self.dtype),
patch_pixel_values=patch_pixel_values.to(self.dtype),
num_patches=num_patches,
)
if image_embeds is not None:
assert isinstance(image_embeds, torch.Tensor)
return Step3VLImageEmbeddingInputs(
type="image_embeds",
data=image_embeds.to(self.dtype),
)
raise AssertionError("This line should be unreachable.")
def _process_image_features(self, image_features: torch.Tensor) -> torch.Tensor:
B, P = image_features.shape[:2]
HW = int(sqrt(P))
image_features = image_features.permute(0, 2, 1).view(B, -1, HW, HW)
image_features = self.vit_downsampler(image_features)
image_features = self.vit_downsampler2(image_features)
n_dim = image_features.size(1)
image_features = image_features.view(B, n_dim, -1).permute(0, 2, 1)
image_features = self.vit_large_projector(image_features)
return image_features
def _get_vision_model_output(self, input_tensor: torch.Tensor) -> torch.Tensor:
return self.vision_model(input_tensor)[:, 4:]
def _process_image_input(
self, image_input: Step3VLImageInputs
) -> list[torch.Tensor]:
if image_input["type"] == "image_embeds":
image_features = image_input["data"]
return [
image_features[i].view(-1, image_features.shape[-1])
for i in range(image_features.shape[0])
]
image_features = self._get_vision_model_output(image_input["pixel_values"])
patch_image_features = (
self._get_vision_model_output(image_input["patch_pixel_values"])
if len(image_input["patch_pixel_values"]) > 0
else None
)
num_patches = image_input["num_patches"]
image_features = self._process_image_features(image_features)
patch_image_features = (
self._process_image_features(patch_image_features)
if patch_image_features is not None
else None
)
merged_image_features = []
cur_patch_idx = 0
num_patches_list = num_patches.tolist()
for i, num_patch in enumerate(num_patches_list):
cur_feature = []
if num_patch > 0:
assert patch_image_features is not None
patch_slice = patch_image_features[
cur_patch_idx : cur_patch_idx + num_patch
]
cur_feature.append(patch_slice.view(-1, patch_slice.shape[-1]))
cur_feature.append(image_features[i].view(-1, image_features.shape[-1]))
cur_patch_idx += num_patch
merged_image_features.append(
torch.cat(cur_feature) if len(cur_feature) > 1 else cur_feature[0]
)
return merged_image_features
def embed_multimodal(self, **kwargs) -> MultiModalEmbeddings:
image_input = self._parse_and_validate_image_input(**kwargs)
if image_input is None:
return []
vision_embeddings = self._process_image_input(image_input)
return vision_embeddings
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
# -- SupportsEncoderCudaGraph protocol methods --
def get_encoder_cudagraph_config(self):
from vllm.v1.worker.encoder_cudagraph_defs import (
EncoderCudaGraphConfig,
EncoderCudaGraphPathConfig,
)
return EncoderCudaGraphConfig(
modalities=["image"],
buffer_keys=[
"pixel_values",
"patch_pixel_values",
],
out_hidden_size=self.config.hidden_size,
paths={
"global": EncoderCudaGraphPathConfig(
min_token_budget=self.img_output_tokens
),
"local": EncoderCudaGraphPathConfig(
min_token_budget=self.patch_output_tokens,
allow_zero_tokens=True,
),
},
)
def get_encoder_cudagraph_budget_range(
self,
vllm_config: "VllmConfig",
) -> tuple[int, int]:
min_budget = self.img_output_tokens
max_budget = min(
vllm_config.scheduler_config.max_num_batched_tokens,
self.model_config.max_model_len,
)
return min_budget, max_budget
def get_encoder_cudagraph_item_specs(
self,
mm_kwargs: dict[str, Any],
):
from vllm.v1.worker.encoder_cudagraph_defs import EncoderItemSpec
num_patches = mm_kwargs.get("num_patches")
assert isinstance(num_patches, torch.Tensor)
img_grid = (
self.config.vision_config.image_size // self.config.vision_config.patch_size
)
patch_grid = 504 // self.config.vision_config.patch_size
total_image_pixel = img_grid * img_grid
total_patch_pixel = patch_grid * patch_grid
return [
EncoderItemSpec(
input_size=(total_image_pixel + num_patch * total_patch_pixel),
output_tokens=(
self.img_output_tokens + num_patch * self.patch_output_tokens
),
path_output_tokens={
"global": self.img_output_tokens,
"local": num_patch * self.patch_output_tokens,
},
)
for num_patch in num_patches
]
def select_encoder_cudagraph_items(
self,
mm_kwargs: dict[str, Any],
indices: list[int],
) -> dict[str, Any]:
pixel_values = mm_kwargs["pixel_values"]
patch_pixel_values = mm_kwargs["patch_pixel_values"]
num_patches = mm_kwargs["num_patches"]
# calcute the accumulated patch counts
cum_patches = [0]
for p in num_patches:
cum_patches.append(cum_patches[-1] + p)
if len(indices) == 0:
return {
"pixel_values": pixel_values[:0],
"patch_pixel_values": patch_pixel_values[:0],
"num_patches": num_patches[:0],
}
selected_pv = pixel_values[indices]
selected_np = num_patches[indices]
selected_ppv = torch.cat(
[patch_pixel_values[cum_patches[i] : cum_patches[i + 1]] for i in indices]
)
return {
"pixel_values": selected_pv,
"patch_pixel_values": selected_ppv,
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
assert path in ("global", "local")
if path == "global":
max_num_images = token_budget // self.img_output_tokens
max_batch_size = min(max_batch_size, max_num_images)
dummy_pixel_values = torch.randn(
max_batch_size,
3,
self.config.vision_config.image_size,
self.config.vision_config.image_size,
device=device,
dtype=dtype,
)
values = {"pixel_values": dummy_pixel_values}
else:
max_num_patches = token_budget // self.patch_output_tokens
dummy_patch_pixel_values = torch.randn(
max_num_patches,
3,
504,
504,
device=device,
dtype=dtype,
)
values = {"patch_pixel_values": dummy_patch_pixel_values}
return EncoderCudaGraphCaptureInputs(
values=values,
)
def encoder_cudagraph_forward(
self,
values: dict[str, torch.Tensor],
path: str = "default",
) -> torch.Tensor:
assert path in ("global", "local")
if path == "global":
return self._batched_encoder_forward(values["pixel_values"])
else:
return self._batched_encoder_forward(values["patch_pixel_values"])
def encoder_eager_forward(
self,
mm_kwargs: dict[str, Any],
path: str = "default",
) -> torch.Tensor:
assert path in ("global", "local")
if path == "global":
return self._batched_encoder_forward(mm_kwargs["pixel_values"])
else:
return self._batched_encoder_forward(mm_kwargs["patch_pixel_values"])
def postprocess_encoder_output(
self,
outputs: dict[str, torch.Tensor],
indices: list[int],
per_item_out_tokens: list[int],
dest: dict[int, torch.Tensor] | list[torch.Tensor | None],
clone: bool = False,
batch_mm_kwargs: dict[str, Any] | None = None,
):
"""CPU-side per-item merge after dual-path graph replay.
``outputs['global']`` contains global-image features and ``outputs['local']``
contains local-patch features (or ``None`` when there are no patches).
"""
output = outputs["global"]
local_output = outputs.get("local")
assert batch_mm_kwargs is not None
num_patches = batch_mm_kwargs["num_patches"]
hidden = output.shape[-1]
bsz = len(indices)
actual_np = [int(np) for np in num_patches]
total_patches = sum(actual_np)
img_tokens = bsz * self.img_output_tokens
patch_tokens = total_patches * self.patch_output_tokens
global_part = output[:img_tokens].reshape(bsz, self.img_output_tokens, hidden)
if total_patches > 0 and local_output is not None:
patch_part = local_output[:patch_tokens].reshape(
-1, self.patch_output_tokens, hidden
)
else:
patch_part = None
merged: dict[int, torch.Tensor] = {}
cur_patch = 0
for i, idx in enumerate(indices):
np = actual_np[i]
parts: list[torch.Tensor] = []
if patch_part is not None and np > 0:
parts.append(patch_part[cur_patch : cur_patch + np].reshape(-1, hidden))
cur_patch += np
parts.append(global_part[i].reshape(-1, hidden))
merged[idx] = torch.cat(parts, dim=0) if len(parts) > 1 else parts[0]
out = [merged[i] for i in indices]
for i, idx in enumerate(indices):
dest[idx] = out[i]
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
assert path in ("global", "local")
if path == "global":
values = {"pixel_values": mm_kwargs["pixel_values"]}
else:
values = {"patch_pixel_values": mm_kwargs["patch_pixel_values"]}
return EncoderCudaGraphReplayBuffers(values=values)
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
input_ids, positions, intermediate_tensors, inputs_embeds=inputs_embeds
)
return hidden_states
def compute_logits(
self,
hidden_states: torch.Tensor,
) -> torch.Tensor | None:
return self.language_model.compute_logits(hidden_states)
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]):
loader = AutoWeightsLoader(self)
return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
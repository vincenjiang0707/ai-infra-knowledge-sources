source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/amd/model/
lastmod: 2026-09-23

@MULTIMODAL_REGISTRY.register_processor(
KimiK3MultiModalProcessor,
info=KimiK3ProcessingInfo,
dummy_inputs=KimiK3DummyInputsBuilder,
)
class KimiK3ForConditionalGeneration(
nn.Module,
SupportsMultiModal,
SupportsPP,
SupportsQuant,
SupportsEagle3,
HasInnerState,
IsHybrid,
):
"""Kimi-K3 model with Kimi-K2.5 vision and KimiLinear text."""
supports_encoder_tp_data = True
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_prefix={
"language_model.layers.": "language_model.model.layers.",
"mm_projector.proj.0": "mm_projector.linear_1",
"mm_projector.proj.2": "mm_projector.linear_2",
}
)
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality == "image":
return "<|kimi_image_placeholder|>"
raise ValueError(f"Unsupported modality: {modality}")
def __init__(
self,
vllm_config: VllmConfig,
prefix: str = "",
) -> None:
super().__init__()
model_config = vllm_config.model_config
config: KimiK3Config = model_config.hf_config
self.config = config
quant_config = vllm_config.quant_config
multimodal_config = model_config.multimodal_config
assert multimodal_config is not None
self.use_data_parallel = is_vit_use_data_parallel(
config.vision_config.num_attention_heads
)
self.hidden_size = config.text_config.hidden_size
self.device = current_platform.current_device()
with self._mark_tower_model(vllm_config, "image"):
self.vision_tower = MoonViT3dPretrainedModel(
config.vision_config,
quant_config=self._maybe_ignore_quant_config(quant_config),
prefix=maybe_prefix(prefix, "vision_tower"),
)
if self._maybe_ignore_quant_config(quant_config) is not None:
self.vision_tower = self.vision_tower.to(device=self.device)
else:
self.vision_tower = self.vision_tower.to(
device=self.device, dtype=model_config.dtype
)
self.mm_projector = KimiK25MultiModalProjector(
config=config.vision_config,
use_data_parallel=self.use_data_parallel,
quant_config=self._maybe_ignore_quant_config(quant_config),
prefix=maybe_prefix(prefix, "mm_projector"),
)
self.mm_projector = self.mm_projector.to(
device=self.device, dtype=model_config.dtype
)
self.quant_config = quant_config
with self._mark_language_model(vllm_config):
self.language_model = init_vllm_registered_model(
vllm_config=vllm_config,
hf_config=config.text_config,
prefix=maybe_prefix(prefix, "language_model"),
architectures=["KimiLinearForCausalLM"],
)
self.make_empty_intermediate_tensors = ( # type: ignore[method-assign]
self.language_model.make_empty_intermediate_tensors
)
self.media_placeholder: int = self.config.media_placeholder_token_id
def _maybe_ignore_quant_config(
self, quant_config: QuantizationConfig | None
) -> QuantizationConfig | None:
if isinstance(quant_config, compressed_tensors.CompressedTensorsConfig):
return None
return quant_config
def _parse_and_validate_media_input(
self, **kwargs: object
) -> KimiK25MediaPixelInputs | None:
pixel_values = kwargs.pop("pixel_values", None)
grid_thws = kwargs.pop("grid_thws", None)
if pixel_values is None:
return None
if isinstance(pixel_values, list):
pixel_values = torch.cat(cast(list[torch.Tensor], pixel_values), dim=0)
if not isinstance(pixel_values, torch.Tensor):
raise TypeError(
"pixel_values must be a tensor or a list of tensors, "
f"got {type(pixel_values)}"
)
if len(pixel_values.shape) == 5 or len(pixel_values.shape) == 3:
pixel_values = pixel_values.reshape(
pixel_values.shape[0] * pixel_values.shape[1], *pixel_values.shape[2:]
)
target_dtype = next(self.vision_tower.parameters()).dtype
pixel_values = pixel_values.to(target_dtype)
assert isinstance(grid_thws, torch.Tensor), (
f"expect grid_thws to be a tensor, got {type(grid_thws)}"
)
grid_thws = grid_thws.reshape(-1, grid_thws.shape[-1])
assert grid_thws.ndim == 2 and grid_thws.size(1) == 3, (
f"unexpected shape for grid_thws: {grid_thws.shape}"
)
return KimiK25MediaPixelInputs(
type="pixel_values",
pixel_values=pixel_values,
grid_thws=grid_thws,
)
def _process_media_input(
self, media_input: KimiK25MediaPixelInputs
) -> list[torch.Tensor]:
media_features = vision_tower_forward(
self.vision_tower,
media_input["pixel_values"],
media_input["grid_thws"],
mm_projector=self.mm_projector,
use_data_parallel=self.use_data_parallel,
)
return media_features
def embed_multimodal(self, **kwargs: object) -> NestedTensors | None:
media_input = self._parse_and_validate_media_input(**kwargs)
if media_input is None:
return None
return self._process_media_input(media_input)
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
hidden_states = self.language_model(
input_ids=input_ids,
positions=positions,
intermediate_tensors=intermediate_tensors,
inputs_embeds=inputs_embeds,
)
return hidden_states
def compute_logits(self, hidden_states: torch.Tensor, **kwargs) -> torch.Tensor:
return self.language_model.compute_logits(hidden_states)
def copy_inputs_before_cuda_graphs(self, input_buffers, **kwargs):
return self.language_model.mamba_cache.copy_inputs_before_cuda_graphs(
input_buffers, **kwargs
)
def get_seqlen_agnostic_capture_inputs(self, batch_size: int):
return self.language_model.mamba_cache.get_seqlen_agnostic_capture_inputs(
batch_size
)
@classmethod
def get_mamba_state_dtype_from_config(cls, vllm_config: VllmConfig):
text_config = vllm_config.model_config.hf_config.text_config
temp_vllm_config = vllm_config.with_hf_config(text_config)
return KimiLinearForCausalLM.get_mamba_state_dtype_from_config(temp_vllm_config)
@classmethod
def get_mamba_state_shape_from_config(cls, vllm_config: VllmConfig):
text_config = vllm_config.model_config.hf_config.text_config
temp_vllm_config = vllm_config.with_hf_config(text_config)
return KimiLinearForCausalLM.get_mamba_state_shape_from_config(temp_vllm_config)
@classmethod
def get_mamba_state_copy_func(cls):
return KimiLinearForCausalLM.get_mamba_state_copy_func()
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]):
loader = AutoWeightsLoader(self)
return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
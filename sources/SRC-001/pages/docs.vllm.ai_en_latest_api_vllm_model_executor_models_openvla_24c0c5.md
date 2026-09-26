source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/openvla/
lastmod: 2026-09-24

@MULTIMODAL_REGISTRY.register_processor(
OpenVLAMultiModalProcessor,
info=OpenVLAProcessingInfo,
dummy_inputs=OpenVLADummyInputsBuilder,
)
class OpenVLAForActionPrediction(nn.Module, SupportsMultiModal, SupportsPP):
"""OpenVLA wrapper with vLLM language-model execution wired in."""
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("image"):
return None
raise ValueError("Only image modality is supported")
def __init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
super().__init__()
config = vllm_config.model_config.hf_config
quant_config = vllm_config.quant_config
self.config = config
self.multimodal_config = vllm_config.model_config.multimodal_config
self.image_token_id = config.image_token_index
self.n_action_bins = config.n_action_bins
self.num_patches = _get_num_image_tokens(config.image_sizes[0])
with self._mark_tower_model(vllm_config, "image"):
self.vision_backbone = PrismaticVisionBackbone(
image_sizes=config.image_sizes,
timm_model_ids=config.timm_model_ids,
timm_override_act_layers=config.timm_override_act_layers,
use_fused_vision_backbone=config.use_fused_vision_backbone,
)
self.projector = PrismaticProjector(
vision_dim=self.vision_backbone.embed_dim,
text_dim=config.text_config.hidden_size,
use_fused_vision_backbone=config.use_fused_vision_backbone,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "projector"),
)
with self._mark_language_model(vllm_config):
self.language_model = init_vllm_registered_model(
vllm_config=vllm_config,
hf_config=config.text_config,
prefix=maybe_prefix(prefix, "language_model"),
)
self.make_empty_intermediate_tensors = (
self.language_model.make_empty_intermediate_tensors
)
def get_language_model(self) -> nn.Module:
return self.language_model
def _parse_and_validate_image_input(
self,
**kwargs: object,
) -> OpenVLAImagePixelInputs | None:
pixel_values = kwargs.pop("pixel_values", None)
if pixel_values is None:
return None
return OpenVLAImagePixelInputs(
type="pixel_values",
data=pixel_values,
resolve_bindings={
"h": self.config.image_sizes[0],
"w": self.config.image_sizes[0],
},
)
def _process_image_input(
self,
image_input: OpenVLAImagePixelInputs,
) -> torch.Tensor:
if self.vision_backbone.dinov2_featurizer is None:
raise RuntimeError("OpenVLA vision backbone is not initialized.")
pixel_values = image_input["data"].to(
dtype=self.vision_backbone.dinov2_featurizer.patch_embed.proj.weight.dtype
)
vision_features = self.vision_backbone(pixel_values)
return self.projector(vision_features)
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
return self.language_model.model(
input_ids,
positions,
intermediate_tensors,
inputs_embeds=inputs_embeds,
)
def compute_logits(self, hidden_states: torch.Tensor) -> torch.Tensor | None:
return self.language_model.compute_logits(hidden_states)
def get_mm_mapping(self) -> MultiModelKeys:
return MultiModelKeys.from_string_field(
language_model="language_model",
connector="projector",
tower_model="vision_backbone",
)
def get_mm_lora_token_counts(
self,
*,
modality: str,
mm_kwargs: MultiModalKwargsItem | None,
num_mm_embeds: int,
) -> tuple[int, int | None]:
del modality, mm_kwargs
return num_mm_embeds, num_mm_embeds
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
def maybe_rename_vision_weights(
weights: Iterable[tuple[str, torch.Tensor]],
) -> Iterable[tuple[str, torch.Tensor]]:
for name, weight in weights:
if name.startswith("vision_backbone.featurizer."):
name = name.replace(
"vision_backbone.featurizer.",
"vision_backbone.dinov2_featurizer.",
1,
)
elif name.startswith("vision_backbone.fused_featurizer."):
name = name.replace(
"vision_backbone.fused_featurizer.",
"vision_backbone.siglip_featurizer.",
1,
)
# HF uses .scale_factor, timm uses .gamma
if ".ls1.scale_factor" in name or ".ls2.scale_factor" in name:
name = name.replace(".scale_factor", ".gamma")
yield name, weight
loader = AutoWeightsLoader(self)
return loader.load_weights(maybe_rename_vision_weights(weights))
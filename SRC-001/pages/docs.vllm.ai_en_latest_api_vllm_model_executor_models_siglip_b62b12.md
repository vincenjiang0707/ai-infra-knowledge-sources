source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/siglip/
lastmod: 2026-09-23

@default_pooling_type(seq_pooling_type="CLS")
@MULTIMODAL_REGISTRY.register_processor(
SiglipMultiModalProcessor,
info=SiglipProcessingInfo,
dummy_inputs=SiglipDummyInputsBuilder,
)
class SiglipEmbeddingModel(nn.Module, SupportsMultiModal, SupportsQuant):
is_pooling_model = True
hf_to_vllm_mapper = WeightsMapper(orig_to_new_substr={".position_ids": None})
packed_modules_mapping = {"qkv_proj": ["q_proj", "k_proj", "v_proj"]}
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("image"):
return None
raise ValueError("Only image modality is supported")
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
config: SiglipConfig = vllm_config.model_config.hf_config
quant_config = vllm_config.quant_config
self.config = config
if hasattr(config, "num_labels"):
config.num_labels = 0
text_config = config.text_config
vision_config = config.vision_config
self.text_embed_dim = text_config.hidden_size
self.vision_embed_dim = vision_config.hidden_size
self.text_projection_size = text_config.projection_size
with self._mark_language_model(vllm_config):
self.text_model = SiglipTextTransformer(
text_config,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "text_model"),
)
with self._mark_tower_model(vllm_config, "image"):
self.vision_model = SiglipVisionTransformer(
vision_config,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "vision_model"),
use_head=None, # Allows potential pooling head
)
pooler_config = vllm_config.model_config.pooler_config
assert pooler_config is not None
self.pooler_config = pooler_config
self.pooler = DispatchPooler.for_embedding(pooler_config)
# Set in embed_input_ids; consumed by forward.
self._has_text_tokens = True
self._mm_token_mask: torch.Tensor | None = None
def get_text_features(
self,
input_ids: torch.Tensor | None,
position_ids: torch.Tensor,
inputs_embeds: torch.Tensor | None = None,
) -> torch.Tensor:
last_hidden_state = self.text_model(
input_ids=input_ids,
position_ids=position_ids,
inputs_embeds=inputs_embeds,
)
text_features = self.text_model.head(last_hidden_state)
# SigLIP uses reversed position_ids;
# flip sequences to move EOS token to first position
text_features = self._flip_sequences_by_position_ids(
text_features, position_ids
)
return text_features
def _flip_sequences_by_position_ids(
self,
features: torch.Tensor,
position_ids: torch.Tensor,
) -> torch.Tensor:
"""Flip sequences so EOS token moves to first position for CLS pooling.
SigLIP position_ids are reversed within each sequence. This method detects
sequence boundaries and flips each sequence individually.
"""
if len(features) == 1:
return features
# Detect sequence boundaries where position_ids decrease
position_diffs = position_ids[1:] - position_ids[:-1]
boundary_mask = position_diffs <= 0
with gpu_sync_allowed():
boundary_mid_cpu = torch.where(boundary_mask.cpu())[0] + 1
zero = torch.zeros(1, dtype=boundary_mid_cpu.dtype)
end = torch.full((1,), len(features), dtype=boundary_mid_cpu.dtype)
boundary_indices_cpu = torch.cat([zero, boundary_mid_cpu, end])
# For each sequence [start, end), position i flips to: start + end - 1 - i
lengths_cpu = boundary_indices_cpu[1:] - boundary_indices_cpu[:-1]
starts_cpu = boundary_indices_cpu[:-1]
ends_cpu = boundary_indices_cpu[1:]
# Assign sequence ID to each element
sequence_ids_cpu = torch.arange(
len(lengths_cpu), dtype=boundary_mid_cpu.dtype
).repeat_interleave(lengths_cpu)
# Calculate flipped indices for all positions at once
current_positions_cpu = torch.arange(
len(features), dtype=boundary_mid_cpu.dtype
)
flip_indices_cpu = (
starts_cpu[sequence_ids_cpu] + ends_cpu[sequence_ids_cpu]
) - (1 + current_positions_cpu)
flip_indices = async_tensor_h2d(flip_indices_cpu, features.device)
return features[flip_indices]
def get_image_features(
self,
pixel_values: torch.Tensor,
feature_select_strategy: VisionFeatureSelectStrategy | None = None,
) -> torch.Tensor:
if feature_select_strategy is None:
pooling_type = self.pooler_config.seq_pooling_type
assert pooling_type is not None
feature_select_strategy = _get_vision_feature_select_strategy(pooling_type)
pooled_output = self.vision_model(
pixel_values=pixel_values,
select_layers=None,
feature_select_strategy=feature_select_strategy,
)
return pooled_output
def _parse_and_validate_image_input(
self, **kwargs: object
) -> SiglipImagePixelInputs | None:
pixel_values = kwargs.pop("pixel_values", None)
if pixel_values is None:
return None
expected_h = expected_w = self.config.vision_config.image_size
return SiglipImagePixelInputs(
type="pixel_values",
data=pixel_values,
resolve_bindings={"h": expected_h, "w": expected_w},
)
def _process_image_inputs(self, inputs: SiglipImagePixelInputs) -> torch.Tensor:
pixel_values = inputs["data"]
return self.get_image_features(pixel_values)
def _embed_text_input_ids(
self,
input_ids: torch.Tensor,
embed_input_ids: Callable[[torch.Tensor], torch.Tensor],
*,
is_multimodal: torch.Tensor | None,
) -> torch.Tensor:
inputs_embeds = super()._embed_text_input_ids(
input_ids,
embed_input_ids,
is_multimodal=is_multimodal,
)
# NOTE: inputs_embeds in model runner has size text_config.projection_size
# (instead of text_config.hidden_size) to accommodate image embeddings
inputs_embeds_size = self.text_projection_size
if inputs_embeds.shape[1] < inputs_embeds_size:
inputs_embeds = torch.cat(
[
inputs_embeds,
inputs_embeds.new_empty(
inputs_embeds.shape[0],
inputs_embeds_size - inputs_embeds.shape[1],
),
],
dim=1,
)
elif inputs_embeds.shape[1] > inputs_embeds_size:
# No need to handle this case for now
raise NotImplementedError
return inputs_embeds
def embed_input_ids(
self,
input_ids: torch.Tensor,
multimodal_embeddings: MultiModalEmbeddings | None = None,
*,
is_multimodal: torch.Tensor | None = None,
) -> torch.Tensor:
has_mm_embeddings = (
multimodal_embeddings is not None and len(multimodal_embeddings) > 0
)
self._mm_token_mask = is_multimodal
self._has_text_tokens = dual_encoder_has_text_tokens(
has_mm_embeddings, is_multimodal
)
if multimodal_embeddings is None or is_multimodal is None:
return super().embed_input_ids(input_ids)
return super().embed_input_ids(
input_ids,
multimodal_embeddings=multimodal_embeddings,
is_multimodal=is_multimodal,
)
def embed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
image_input = self._parse_and_validate_image_input(**kwargs)
if image_input is None:
return []
vision_embeddings = self._process_image_inputs(image_input)
return vision_embeddings
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
**kwargs: object,
) -> torch.Tensor:
if intermediate_tensors is not None:
raise RuntimeError("PP is not supported for this model")
# Multimodal inputs (image embeddings)
assert inputs_embeds is not None
if not self._has_text_tokens:
return inputs_embeds
vision_embeds = inputs_embeds
# NOTE: inputs_embeds in model runner has size text_config.projection_size
# (instead of text_config.hidden_size) to accommodate image embeddings
hidden_size = self.text_embed_dim
if inputs_embeds.shape[1] > hidden_size:
inputs_embeds = inputs_embeds[:, :hidden_size]
elif inputs_embeds.shape[1] < hidden_size:
# No need to handle this case for now
raise NotImplementedError
text_features = self.get_text_features(input_ids, positions, inputs_embeds)
return merge_dual_encoder_text_and_vision(
text_features, vision_embeds, self._mm_token_mask
)
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]):
loader = AutoWeightsLoader(
self,
ignore_unexpected_prefixes=["logit_scale.", "logit_bias."],
)
return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
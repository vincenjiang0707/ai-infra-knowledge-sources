source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/
lastmod: 2026-09-23

@MULTIMODAL_REGISTRY.register_processor(
InklingMultiModalProcessor,
info=InklingProcessingInfo,
dummy_inputs=InklingDummyInputsBuilder,
)
class InklingForConditionalGeneration(_TmlForCausalLMBase, SupportsMultiModal):
"""Top-level (multimodal) entry point.
Builds the vision + audio towers on top of the shared text backbone. Inkling has
NO cross-modal fusion (the vision tower emits one token per patch, the audio
tower one token per frame), so generation reuses the inherited backbone
``forward`` / ``compute_logits`` (the latter already applies muP) and this
class only adds multimodal embedding + merge.
"""
hf_to_vllm_mapper = _TmlForCausalLMBase.hf_to_vllm_mapper | WeightsMapper(
orig_to_new_prefix={
"model.audio.": "audio.",
"model.visual.": "visual.vision_encoder.",
},
)
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("image"):
return "<|content_image|>"
if modality.startswith("audio"):
return "<|content_audio_input|>"
raise ValueError("Only image or audio modality is supported")
def __init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
super().__init__()
config: InklingMMConfig = vllm_config.model_config.hf_config
self.visual = (
InklingVision(config.vision_config, prefix=maybe_prefix(prefix, "visual"))
if inkling_vision_enabled(config)
else None
)
self.audio = (
InklingAudio(config.audio_config, prefix=maybe_prefix(prefix, "audio"))
if inkling_audio_enabled(config)
else None
)
self._build(vllm_config, config.text_config, prefix)
# -- multimodal embedding -------------------------------------------
def _process_image_input(
self, pixel_values: Any, num_patches: Any
) -> tuple[torch.Tensor, ...]:
assert self.visual is not None
# pixel_values is a list (per item) of [P_i, 2, P, P, 3] tensors,
# or a single concatenated tensor. Normalize to a flat batch, run the
# tower once, then split back per item.
if isinstance(pixel_values, (list, tuple)):
if not pixel_values:
return ()
sizes = [int(p.shape[0]) for p in pixel_values]
patches = torch.cat(list(pixel_values), dim=0)
else:
patches = pixel_values
sizes = self._sizes_from(num_patches, patches.shape[0])
patches = patches.to(device=self.visual.device, dtype=self.visual.dtype)
embeds = self.visual(patches) # [total_patches, D]
return tuple(embeds.split(sizes))
def _process_audio_input(
self, input_audio_features: Any, num_audio_tokens: Any
) -> tuple[torch.Tensor, ...]:
assert self.audio is not None
if isinstance(input_audio_features, (list, tuple)):
if not input_audio_features:
return ()
sizes = [int(d.shape[0]) for d in input_audio_features]
dmel = torch.cat(list(input_audio_features), dim=0)
else:
dmel = input_audio_features
sizes = self._sizes_from(num_audio_tokens, dmel.shape[0])
dmel = dmel.to(device=self.audio.device)
embeds = self.audio(dmel) # [total_frames, D]
return tuple(embeds.split(sizes))
@staticmethod
def _sizes_from(counts: Any, total: int) -> list[int]:
if counts is None:
return [total]
if isinstance(counts, torch.Tensor):
return [int(c) for c in counts.flatten().tolist()]
if isinstance(counts, (list, tuple)):
flat: list[int] = []
for c in counts:
flat.append(int(c.item()) if isinstance(c, torch.Tensor) else int(c))
return flat
return [int(counts)]
def embed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
# Iterate modalities in a stable order so the returned per-item tensors
# line up with their appearance order; the positional merge in
# embed_input_ids handles actual placement.
pixel_values = kwargs.get("pixel_values")
num_patches = kwargs.get("num_patches")
input_audio_features = kwargs.get("input_audio_features")
num_audio_tokens = kwargs.get("num_audio_tokens")
embeddings: tuple[torch.Tensor, ...] = ()
if pixel_values is not None and self.visual is not None:
embeddings += self._process_image_input(pixel_values, num_patches)
if input_audio_features is not None and self.audio is not None:
embeddings += self._process_audio_input(
input_audio_features, num_audio_tokens
)
return embeddings
def embed_input_ids(
self,
input_ids: torch.Tensor,
multimodal_embeddings: MultiModalEmbeddings | None = None,
*,
is_multimodal: torch.Tensor | None = None,
) -> torch.Tensor:
# Override the base's 1-arg embed_input_ids: the runner calls this 3-arg
# signature for multimodal models. Text embeddings come from the shared
# backbone (which applies embed_norm); MM embeddings are scattered in.
from vllm.model_executor.models.utils import _merge_multimodal_embeddings
# Placeholder ids use unused vocabulary slots and these positions are
# overwritten by MM embeds below.
inputs_embeds = self.model.embed_input_ids(input_ids)
if multimodal_embeddings is None or len(multimodal_embeddings) == 0:
return inputs_embeds
assert is_multimodal is not None
return _merge_multimodal_embeddings(
inputs_embeds=inputs_embeds,
multimodal_embeddings=multimodal_embeddings,
is_multimodal=is_multimodal,
)
def get_language_model(self) -> nn.Module:
# This class IS the causal LM (the towers are side branches), so the
# language model is self — callers expect a module exposing ``.model``
# and ``.lm_head``.
return self
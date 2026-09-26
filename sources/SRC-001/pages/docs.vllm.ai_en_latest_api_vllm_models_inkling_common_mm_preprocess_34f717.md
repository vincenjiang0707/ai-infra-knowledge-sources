source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/common/mm_preprocess/
lastmod: 2026-09-24

class InklingMultiModalProcessor(BaseMultiModalProcessor[InklingProcessingInfo]):
def _apply_hf_processor_main(
self,
mm_items: MultiModalDataItems,
hf_kwargs: Mapping[str, object],
) -> BatchFeature:
mm_data, hf_kwargs, passthrough_data = self._get_hf_mm_inputs(
mm_items, hf_kwargs
)
prompt_text = self.dummy_inputs.get_dummy_text(mm_items.get_all_counts())
processor = self.info.get_hf_processor(**hf_kwargs)
tokenizer = self.info.get_tokenizer()
images = mm_data.get("images") or []
audios = mm_data.get("audio") or []
if not isinstance(images, list):
images = list(cast(Iterable[Any], images))
if not isinstance(audios, list):
audios = list(cast(Iterable[Any], audios))
prompt_ids = self._tokenize_with_placeholders(
prompt_text, tokenizer, len(images), len(audios)
)
data: dict[str, Any] = {"input_ids": [prompt_ids]}
if images:
img_feat = processor.process_images(images)
data["pixel_values"] = img_feat["vision_patches_bthwc"]
data["num_patches"] = torch.tensor(
img_feat["num_patches"], dtype=torch.int64
)
if audios:
aud_feat = processor.process_audios(audios)
per_clip = aud_feat["dmel_bins"]
num_audio_tokens = aud_feat["num_audio_tokens"]
for i, n in enumerate(num_audio_tokens):
if int(n) > MAX_AUDIO_TOKENS:
raise ValueError(
f"Audio clip {i} produces {int(n)} tokens, exceeding the "
f"maximum of {MAX_AUDIO_TOKENS} (~10 min at 20 tokens/s). "
"Provide a shorter clip."
)
if per_clip:
input_audio_features = torch.cat(
[torch.as_tensor(c) for c in per_clip], dim=0
)
else:
input_audio_features = torch.empty(0)
data["input_audio_features"] = input_audio_features
data["num_audio_tokens"] = torch.tensor(num_audio_tokens, dtype=torch.int64)
processed_data = BatchFeature(data=data, tensor_type=None)
return self._finalize_hf_mm_data(
mm_data, hf_kwargs, passthrough_data, processed_data
)
def _tokenize_with_placeholders(
self,
prompt: str,
tokenizer: Any,
num_images: int,
num_audios: int,
) -> list[int]:
"""Tokenize `prompt`, emitting the block-start marker id per media item.
Each marker (kept verbatim) is later expanded by ``_get_prompt_updates``
into ``<marker> + <placeholder> * N``.
"""
image_marker = "<|content_image|>"
audio_marker = "<|content_audio_input|>"
pattern = f"({re.escape(image_marker)}|{re.escape(audio_marker)})"
chunks = re.split(pattern, prompt)
ids: list[int] = []
seen_img = seen_aud = 0
for chunk in chunks:
if chunk == image_marker:
ids.append(IMAGE_MARKER_ID)
seen_img += 1
elif chunk == audio_marker:
ids.append(AUDIO_MARKER_ID)
seen_aud += 1
elif chunk:
ids.extend(tokenizer.encode(chunk, add_special_tokens=False))
# Reconcile against the declared media counts only when media is
# present. With no media items, emit the markers verbatim; the
# marker<->item correspondence is enforced later by
# ``_get_prompt_updates`` once the media features are available.
if num_images or num_audios:
# Fail clearly on a placeholder/media-count mismatch instead of
# crashing with an IndexError deep in the per-item replacement logic.
if num_images and seen_img != num_images:
raise ValueError(
f"Prompt contains {seen_img} image placeholder(s), but only "
f"{num_images} image(s) were provided."
)
if num_audios and seen_aud != num_audios:
raise ValueError(
f"Prompt contains {seen_aud} audio placeholder(s), but only "
f"{num_audios} audio input(s) were provided."
)
return ids
def _get_mm_fields_config(
self,
hf_inputs: BatchFeature,
hf_processor_mm_kwargs: Mapping[str, object],
) -> Mapping[str, MultiModalFieldConfig]:
num_patches = hf_inputs.get("num_patches", torch.empty(0, dtype=torch.int64))
num_audio_tokens = hf_inputs.get(
"num_audio_tokens", torch.empty(0, dtype=torch.int64)
)
return dict(
# Ragged per-image patches, grouped by num_patches.
pixel_values=MultiModalFieldConfig.flat_from_sizes("image", num_patches),
num_patches=MultiModalFieldConfig.batched("image", keep_on_cpu=True),
# Ragged per-audio frames, grouped by num_audio_tokens.
input_audio_features=MultiModalFieldConfig.flat_from_sizes(
"audio", num_audio_tokens
),
num_audio_tokens=MultiModalFieldConfig.batched("audio", keep_on_cpu=True),
)
def _get_prompt_updates(
self,
mm_items: Any,
hf_processor_mm_kwargs: Mapping[str, Any],
out_mm_kwargs: MultiModalKwargsItems,
) -> Sequence[PromptUpdate]:
out_mm_data = out_mm_kwargs.get_data()
num_patches: Any = out_mm_data.get("num_patches")
num_audio_tokens: Any = out_mm_data.get("num_audio_tokens")
# Keep the block-start marker and append N placeholder tokens after it;
# only the placeholder positions are flagged as embeddings (is_embed), so
# the marker stays a normal text token while the tower features scatter
# into the placeholders.
def image_replacement(item_idx: int) -> PromptUpdateDetails:
n = int(num_patches[item_idx])
return PromptUpdateDetails.select_token_id(
[IMAGE_MARKER_ID] + [IMAGE_TOKEN_ID] * n, IMAGE_TOKEN_ID
)
def audio_replacement(item_idx: int) -> PromptUpdateDetails:
n = int(num_audio_tokens[item_idx])
return PromptUpdateDetails.select_token_id(
[AUDIO_MARKER_ID] + [AUDIO_TOKEN_ID] * n, AUDIO_TOKEN_ID
)
updates: list[PromptUpdate] = []
if num_patches is not None and len(num_patches) > 0:
updates.append(
PromptReplacement(
modality="image",
target=[IMAGE_MARKER_ID],
replacement=image_replacement,
)
)
if num_audio_tokens is not None and len(num_audio_tokens) > 0:
updates.append(
PromptReplacement(
modality="audio",
target=[AUDIO_MARKER_ID],
replacement=audio_replacement,
)
)
return updates
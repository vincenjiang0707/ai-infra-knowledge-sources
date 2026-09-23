source: https://docs.vllm.ai/en/latest/api/vllm/models/dots3_note/common/processor/
lastmod: 2026-09-23

class Dots3NoteProcessor:
"""Small HF-like processor used by vLLM's multimodal frontend."""
def __init__(
self,
tokenizer,
image_processor: Dots3NoteImageProcessor | None,
*,
max_model_len: int,
video_audio_enabled: bool,
audio_token_stride: int,
) -> None:
self.tokenizer = tokenizer
self.image_processor = image_processor
self.max_model_len = max_model_len
self.video_audio_enabled = video_audio_enabled
self.audio_token_stride = audio_token_stride
def _token_ids(self, text: str) -> list[int]:
if hasattr(self.tokenizer, "encode"):
return self.tokenizer.encode(text, add_special_tokens=False)
token_ids = self.tokenizer(text, add_special_tokens=False)["input_ids"]
if token_ids and isinstance(token_ids[0], list):
return token_ids[0]
return token_ids
def _process_video(
self,
video,
*,
detail: str,
size_overrides: Mapping[str, int | None],
seq: int,
output_reserve: int | None,
audio_cap: float,
audio_sample_rate: int,
k_mode: str,
max_new_tokens: int,
question: str,
) -> dict[str, torch.Tensor]:
if self.image_processor is None:
raise ValueError("This NOTE checkpoint has no vision encoder")
if not self.video_audio_enabled:
audio_cap = 0.0
parts = preprocess_dots3_note_video(
video,
tokenizer=self.tokenizer,
question=question,
seq=seq,
output_reserve=output_reserve,
audio_cap=audio_cap,
audio_sample_rate=audio_sample_rate,
k_mode=k_mode,
max_new_tokens=max_new_tokens,
)
fragments: list[str] = []
pixel_values: list[torch.Tensor] = []
image_grids: list[torch.Tensor] = []
audio_values: list[torch.Tensor] = []
modalities: list[int] = []
image_pad_count = 0
audio_pad_count = 0
for part in parts:
if part.kind == "text":
fragments.append(cast(str, part.value))
continue
if part.kind == "image":
pixels, grid = self.image_processor.preprocess(
cast(Image.Image, part.value),
detail=detail,
min_pixels=size_overrides.get("min_pixels"),
max_pixels=size_overrides.get("max_pixels"),
target_height=size_overrides.get("target_height"),
target_width=size_overrides.get("target_width"),
)
num_tokens = int(grid.prod()) // self.image_processor.merge_size**2
fragments.append(f"{IMAGE_START}{IMAGE_PAD * num_tokens}{IMAGE_END}")
pixel_values.append(pixels)
image_grids.append(grid)
modalities.append(0)
image_pad_count += num_tokens
continue
waveform = torch.from_numpy(
np.ascontiguousarray(part.value, dtype=np.float32)
).view(torch.int32)
num_tokens = math.ceil(waveform.numel() / self.audio_token_stride)
fragments.append(f"{AUDIO_START}{AUDIO_PAD * num_tokens}{AUDIO_END}")
audio_values.append(waveform)
modalities.append(1)
audio_pad_count += num_tokens
if not pixel_values:
raise ValueError("NOTE video preprocessing produced no frames")
fragment_ids = self._token_ids("".join(fragments))
vocab = self.tokenizer.get_vocab()
embed_mask = torch.isin(
torch.tensor(fragment_ids, dtype=torch.long),
torch.tensor([vocab[IMAGE_PAD], vocab[AUDIO_PAD]], dtype=torch.long),
)
expected_embeds = image_pad_count + audio_pad_count
if int(embed_mask.sum()) != expected_embeds:
raise ValueError(
"NOTE video placeholder expansion produced an invalid embedding mask: "
f"expected={expected_embeds}, actual={int(embed_mask.sum())}"
)
empty_audio = torch.empty(0, dtype=torch.int32)
return {
"video_pixel_values": torch.cat(pixel_values),
"video_image_grid_thw": torch.stack(image_grids),
"video_audio_values": (
torch.cat(audio_values) if audio_values else empty_audio
),
"video_audio_lengths": torch.tensor(
[value.numel() for value in audio_values],
dtype=torch.long,
),
"video_modalities": torch.tensor(modalities, dtype=torch.uint8),
"video_input_ids": torch.tensor(fragment_ids, dtype=torch.long),
"video_embed_mask": embed_mask,
"video_frame_counts": torch.tensor([len(image_grids)], dtype=torch.long),
"video_audio_counts": torch.tensor([len(audio_values)], dtype=torch.long),
"video_emission_counts": torch.tensor([len(modalities)], dtype=torch.long),
"video_prompt_lengths": torch.tensor([len(fragment_ids)], dtype=torch.long),
"video_patch_counts": torch.tensor(
[sum(int(grid.prod()) for grid in image_grids)], dtype=torch.long
),
"video_audio_sample_counts": torch.tensor(
[sum(value.numel() for value in audio_values)], dtype=torch.long
),
}
def __call__(self, text: str, **kwargs: object) -> BatchFeature:
modality_order = [
key for key in kwargs if key in ("images", "audios", "videos")
]
raw_images = kwargs.pop("images", None)
raw_audios = kwargs.pop("audios", None)
raw_videos = kwargs.pop("videos", None)
images = (
list(cast(Sequence[Image.Image], raw_images))
if raw_images is not None
else []
)
audios = (
list(cast(Sequence[np.ndarray], raw_audios))
if raw_audios is not None
else []
)
videos = (
list(cast(Sequence[object], raw_videos)) if raw_videos is not None else []
)
if videos and (images or audios):
raise ValueError(
"Dots3Note does not support mixing a native video with "
"separate image/audio inputs"
)
if len(videos) > 1:
raise ValueError("Dots3Note supports one video per request")
detail = kwargs.pop("image_detail", "auto")
details = list(detail) if isinstance(detail, (list, tuple)) else None
size_overrides: dict[str, int | None] = {}
for key in ("min_pixels", "max_pixels", "target_height", "target_width"):
if key in kwargs:
value = kwargs.pop(key)
size_overrides[key] = None if value is None else int(cast(Any, value))
video_seq = int(cast(Any, kwargs.pop("seq", self.max_model_len)))
reserve_value = kwargs.pop("output_reserve", None)
output_reserve = (
None if reserve_value is None else int(cast(Any, reserve_value))
)
audio_cap = float(cast(Any, kwargs.pop("audio_cap", 1.0)))
audio_sample_rate = int(cast(Any, kwargs.pop("audio_sr", _DEFAULT_SAMPLE_RATE)))
k_mode = str(kwargs.pop("k_mode", "eval_ek"))
max_new_tokens = int(cast(Any, kwargs.pop("max_new_tokens", 0)))
question = str(kwargs.pop("video_question", text))
tokenized = self.tokenizer(text, **kwargs)
input_ids = tokenized["input_ids"]
if isinstance(input_ids, torch.Tensor):
if input_ids.ndim == 1:
input_ids = input_ids.unsqueeze(0)
elif input_ids and isinstance(input_ids[0], int):
input_ids = [input_ids]
data: dict[str, object] = {"input_ids": input_ids}
for modality in modality_order:
if modality == "images" and images:
if self.image_processor is None:
raise ValueError("This NOTE checkpoint has no vision encoder")
pixel_values = []
grids = []
for idx, image in enumerate(images):
image_detail = details[idx] if details is not None else str(detail)
pixels, grid = self.image_processor.preprocess(
image,
detail=image_detail,
min_pixels=size_overrides.get("min_pixels"),
max_pixels=size_overrides.get("max_pixels"),
target_height=size_overrides.get("target_height"),
target_width=size_overrides.get("target_width"),
)
pixel_values.append(pixels)
grids.append(grid)
data["pixel_values"] = torch.cat(pixel_values)
data["image_grid_thw"] = torch.stack(grids)
elif modality == "audios" and audios:
waveforms = [
torch.from_numpy(
np.ascontiguousarray(audio, dtype=np.float32)
).view(torch.int32)
for audio in audios
]
data["audio_values"] = torch.cat(waveforms)
data["audio_lengths"] = torch.tensor(
[waveform.numel() for waveform in waveforms],
dtype=torch.long,
)
elif modality == "videos" and videos:
video_detail = details[0] if details is not None else str(detail)
data.update(
self._process_video(
videos[0],
detail=video_detail,
size_overrides=size_overrides,
seq=video_seq,
output_reserve=output_reserve,
audio_cap=audio_cap,
audio_sample_rate=audio_sample_rate,
k_mode=k_mode,
max_new_tokens=max_new_tokens,
question=question,
)
)
return BatchFeature(data=data)
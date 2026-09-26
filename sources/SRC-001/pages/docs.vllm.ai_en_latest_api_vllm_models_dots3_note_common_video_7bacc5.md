source: https://docs.vllm.ai/en/latest/api/vllm/models/dots3_note/common/video/
lastmod: 2026-09-24

def preprocess_dots3_note_video(
video,
*,
tokenizer,
question: str,
seq: int,
output_reserve: int | None = None,
audio_cap: float = 1.0,
audio_sample_rate: int = _AUDIO_SAMPLE_RATE,
k_mode: str = "eval_ek",
max_new_tokens: int = 0,
) -> list[Dots3NoteVideoPart]:
"""Expand one video into timestamped, interleaved image/audio parts."""
if seq <= 0:
raise ValueError(f"seq must be positive, got {seq}")
configured_reserve = seq // 4 if output_reserve is None else output_reserve
effective_reserve = max(configured_reserve, max_new_tokens)
if effective_reserve >= seq:
raise ValueError(
"output_reserve/max_new_tokens must leave room for video input"
)
if audio_cap < 0:
raise ValueError(f"audio_cap must be non-negative, got {audio_cap}")
if audio_sample_rate <= 0:
raise ValueError(f"audio_sample_rate must be positive, got {audio_sample_rate}")
seq_length = seq - effective_reserve
jpeg_quality = int(os.environ.get("XHS_VIDEO_JPEG_QUALITY", "85"))
pcm: np.ndarray | None = None
audio_duration = 0.0
if isinstance(video, bytes) and audio_cap > 0:
pcm, audio_duration = _decode_audio(video, audio_sample_rate)
audio_token_count = (
_audio_tokens(audio_duration, audio_sample_rate) if pcm is not None else 0
)
estimated_frames = max(1, int(audio_duration * _FPS_CAP))
max_groups = min(
estimated_frames,
max(1, int(audio_duration // _INTERLEAVE_MIN_SECONDS)),
)
reserved_audio_tokens = audio_token_count + 3 * max_groups
min_visual_tokens = _MIN_FRAMES * (_PF_FLOOR + _FRAME_OVERHEAD)
if (
audio_token_count > audio_cap * seq_length
or reserved_audio_tokens + min_visual_tokens + _BUDGET_OVERHEAD > seq_length
):
pcm = None
audio_duration = 0.0
reserved_audio_tokens = 0
overhead = (
_token_len(
tokenizer,
"<|system|>You are a helpful assistant.<|endofsystem|>\n",
)
+ 2
+ _token_len(tokenizer, "<video_0>")
+ 64
)
visual_budget = max(
_PF_FLOOR + _FRAME_OVERHEAD,
seq_length - overhead - reserved_audio_tokens,
)
if isinstance(video, bytes):
frames, video_duration = _decode_frames(
video,
visual_budget,
seq_length,
jpeg_quality,
)
else:
frames, video_duration = _prepare_decoded_frames(
video,
visual_budget,
seq_length,
jpeg_quality,
)
if pcm is None:
parts: list[Dots3NoteVideoPart] = []
for timestamp, image in frames:
parts.append(
Dots3NoteVideoPart("text", f"<{_format_timestamp(timestamp)}>")
)
parts.append(Dots3NoteVideoPart("image", image))
return parts
video_id = hashlib.sha1(video).hexdigest()
record_key = hashlib.sha1(f"{video_id}|{question}".encode()).hexdigest()
seed_hex = hashlib.sha1(f"42|flatten|{record_key}".encode()).hexdigest()
rng = random.Random(int(seed_hex[:8], 16))
bounds = _group_bounds(len(frames), audio_duration, k_mode, rng)
parts = []
for group in range(len(bounds) - 1):
start, end = bounds[group], bounds[group + 1]
if end <= start:
continue
start_time = 0.0 if group == 0 else frames[start][0]
end_time = audio_duration if group == len(bounds) - 2 else frames[end][0]
if end_time <= start_time:
end_time = start_time + audio_duration / max(1, len(bounds) - 1)
for timestamp, image in frames[start:end]:
parts.append(
Dots3NoteVideoPart("text", f"<{_format_timestamp(timestamp)}>")
)
parts.append(Dots3NoteVideoPart("image", image))
sample_start = max(0, int(round(start_time * audio_sample_rate)))
sample_end = min(len(pcm), int(round(end_time * audio_sample_rate)))
if sample_end > sample_start:
segment = np.ascontiguousarray(
pcm[sample_start:sample_end].astype(np.float32) / 32768.0
)
parts.append(Dots3NoteVideoPart("audio", segment))
return parts
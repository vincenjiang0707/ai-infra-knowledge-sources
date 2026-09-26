source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/moss_transcribe_diarize/
lastmod: 2026-09-24

@MULTIMODAL_REGISTRY.register_processor(
MossTranscribeDiarizeMultiModalProcessor,
info=MossTranscribeDiarizeProcessingInfo,
dummy_inputs=MossTranscribeDiarizeDummyInputsBuilder,
)
class MossTranscribeDiarizeForConditionalGeneration(
nn.Module,
SupportsMultiModal,
SupportsPP,
SupportsTranscription,
):
supports_transcription = True
supports_transcription_only = True
supports_segment_timestamp = False
supports_diarized_transcription = True
supported_languages = ISO639_1_SUPPORTED_LANGS
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_prefix={
"language_model.layers.": "language_model.model.layers.",
"language_model.embed_tokens.": "language_model.model.embed_tokens.",
"language_model.norm.": "language_model.model.norm.",
"model.language_model.model.": "language_model.model.",
"model.language_model.lm_head.": "language_model.lm_head.",
"model.language_model.": "language_model.model.",
"model.whisper_encoder.": "whisper_encoder.",
"model.vq_adaptor.": "vq_adaptor.",
"model.": None,
},
)
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
return AUDIO_PLACEHOLDER if modality.startswith("audio") else None
@classmethod
def get_speech_to_text_config(
cls,
model_config: ModelConfig,
task_type: str,
) -> SpeechToTextConfig:
processor = cached_processor_from_config(model_config)
return SpeechToTextConfig(
max_audio_clip_s=None,
sample_rate=processor.feature_extractor.sampling_rate,
min_energy_split_window_size=None,
)
@classmethod
def get_num_audio_tokens(
cls,
audio_duration_s: float,
stt_config: SpeechToTextConfig,
model_config: ModelConfig,
) -> int | None:
processor = cached_processor_from_config(model_config)
num_samples = math.ceil(audio_duration_s * stt_config.sample_rate)
return _compute_total_audio_tokens(
num_samples,
processor.feature_extractor,
processor.audio_merge_size,
)
@classmethod
def get_generation_prompt(cls, stt_params: SpeechToTextParams) -> PromptType:
stt_config = stt_params.stt_config
question = stt_params.request_prompt or DEFAULT_MOSS_TRANSCRIBE_DIARIZE_PROMPT
question = question.strip() or DEFAULT_MOSS_TRANSCRIBE_DIARIZE_PROMPT
prompt = (
"<|im_start|>system\n"
"You are a helpful assistant.<|im_end|>\n"
f"<|im_start|>user\n{AUDIO_PLACEHOLDER}\n"
f"{question}<|im_end|>\n"
"<|im_start|>assistant\n"
)
return TextPrompt(
prompt=prompt,
multi_modal_data={"audio": (stt_params.audio, stt_config.sample_rate)},
)
@classmethod
def post_process_output(cls, text: str) -> str:
return text.strip()
@classmethod
def parse_diarized_transcript(cls, text: str) -> list[DiarizedTranscriptionSegment]:
"""Parse MOSS's canonical ``[start][Sxx]text[end]`` transcript."""
headers: list[tuple[re.Match[str], float, str]] = []
for match in _MOSS_DIARIZED_HEADER_RE.finditer(text):
start = parse_diarized_timestamp(match["start"])
speaker = parse_diarized_speaker(match["speaker"])
if start is not None and speaker is not None:
headers.append((match, start, speaker))
if not headers:
return []
segments: list[DiarizedTranscriptionSegment] = []
for index, (header, start, speaker) in enumerate(headers):
next_header_start = (
headers[index + 1][0].start() if index + 1 < len(headers) else len(text)
)
body = text[header.end() : next_header_start]
end_match = _MOSS_DIARIZED_END_RE.search(body)
if end_match is None:
return []
end = parse_diarized_timestamp(end_match["end"])
if end is None or end < start:
return []
segment_text = body[: end_match.start()].strip()
if segment_text:
segments.append(
DiarizedTranscriptionSegment(
start=start,
end=end,
speaker=speaker,
text=segment_text,
)
)
return segments
def __init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
super().__init__()
self.config = vllm_config.model_config.hf_config
self.dtype = vllm_config.model_config.dtype
with self._mark_tower_model(vllm_config, "audio"):
self.whisper_encoder = MossTranscribeDiarizeWhisperEncoder(
vllm_config=vllm_config,
prefix=maybe_prefix(prefix, "whisper_encoder"),
)
self.vq_adaptor = MossTranscribeDiarizeVQAdaptor(
input_dim=int(self.config.adaptor_input_dim),
hidden_size=int(self.config.text_config.hidden_size),
eps=float(self.config.text_config.rms_norm_eps),
)
with self._mark_language_model(vllm_config):
self.language_model = init_vllm_registered_model(
vllm_config=vllm_config,
hf_config=self.config.text_config,
prefix=maybe_prefix(prefix, "language_model"),
architectures=["Qwen3ForCausalLM"],
)
self.make_empty_intermediate_tensors = (
self.language_model.make_empty_intermediate_tensors
)
def _time_merge(self, features: torch.Tensor) -> torch.Tensor:
batch, seq_len, dim = features.shape
merge_size = int(self.config.audio_merge_size)
seq_len_trim = (seq_len // merge_size) * merge_size
return features[:, :seq_len_trim, :].reshape(
batch,
seq_len_trim // merge_size,
dim * merge_size,
)
def _parse_and_validate_audio_input(
self,
**kwargs: object,
) -> MossTranscribeDiarizeInputs | None:
input_features = kwargs.pop("input_features", None)
audio_embeds = kwargs.pop("audio_embeds", None)
audio_feature_lengths = kwargs.pop("audio_feature_lengths", None)
audio_chunk_counts = kwargs.pop("audio_chunk_counts", None)
if input_features is None and audio_embeds is None:
return None
if audio_embeds is not None:
return MossTranscribeDiarizeEmbeddingInputs(
type="audio_embeds",
audio_embeds=_as_audio_embedding_list(audio_embeds),
)
return MossTranscribeDiarizeAudioInputs(
type="audio_features",
input_features=input_features,
audio_feature_lengths=audio_feature_lengths,
audio_chunk_counts=audio_chunk_counts,
)
def _process_audio_input(
self, audio_input: MossTranscribeDiarizeInputs
) -> list[torch.Tensor]:
if audio_input["type"] == "audio_embeds":
return list(audio_input["audio_embeds"])
input_features = audio_input["input_features"]
audio_feature_lengths = audio_input["audio_feature_lengths"]
audio_chunk_counts = audio_input["audio_chunk_counts"]
if input_features is None or audio_feature_lengths is None:
raise ValueError(
"MOSS-Transcribe-Diarize audio inputs require both "
"`input_features` and `audio_feature_lengths`."
)
if audio_feature_lengths.numel() != input_features.shape[0]:
raise ValueError(
"`audio_feature_lengths` must contain one length per "
"`input_features` chunk: got "
f"{audio_feature_lengths.numel()} lengths for "
f"{input_features.shape[0]} chunks."
)
if audio_chunk_counts is None:
audio_chunk_counts = audio_feature_lengths.new_tensor(
[input_features.shape[0]],
dtype=torch.long,
)
else:
audio_chunk_counts = audio_chunk_counts.to(dtype=torch.long)
if audio_chunk_counts.numel() == 0:
raise ValueError("`audio_chunk_counts` must contain at least one item.")
if torch.any(audio_chunk_counts <= 0):
raise ValueError("`audio_chunk_counts` must contain positive counts.")
num_audio_chunks = int(audio_chunk_counts.sum().item())
if num_audio_chunks != input_features.shape[0]:
raise ValueError(
"`audio_chunk_counts` must sum to the number of input feature chunks: "
f"got {num_audio_chunks} chunks for "
f"{input_features.shape[0]} input chunks."
)
features = self.whisper_encoder(input_features, audio_feature_lengths)
merged = self._time_merge(features.to(dtype=self.dtype))
projected = self.vq_adaptor(merged).squeeze(0)
audio_chunk_offsets = torch.cumsum(audio_chunk_counts, dim=0)
audio_chunk_offsets = torch.cat(
[audio_chunk_offsets.new_zeros(1), audio_chunk_offsets]
)
tokens_per_item = [
int(audio_feature_lengths[start:end].sum().item())
for start, end in zip(
audio_chunk_offsets[:-1].tolist(),
audio_chunk_offsets[1:].tolist(),
)
]
if any(num_tokens <= 0 for num_tokens in tokens_per_item):
raise ValueError("Audio input is too short to produce any tokens.")
return list(projected.split(tokens_per_item, dim=0))
def embed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
audio_input = self._parse_and_validate_audio_input(**kwargs)
if audio_input is None:
return []
return self._process_audio_input(audio_input)
def embed_input_ids(
self,
input_ids: torch.Tensor,
multimodal_embeddings: MultiModalEmbeddings | None = None,
*,
is_multimodal: torch.Tensor | None = None,
) -> torch.Tensor:
inputs_embeds = self.language_model.embed_input_ids(input_ids)
if not multimodal_embeddings:
return inputs_embeds
return _merge_multimodal_embeddings(
inputs_embeds=inputs_embeds,
multimodal_embeddings=multimodal_embeddings,
is_multimodal=_require_is_multimodal(is_multimodal),
)
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
return self.language_model(
input_ids=input_ids,
positions=positions,
intermediate_tensors=intermediate_tensors,
inputs_embeds=inputs_embeds,
)
def compute_logits(self, hidden_states: torch.Tensor) -> torch.Tensor | None:
return self.language_model.compute_logits(hidden_states)
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
loader = AutoWeightsLoader(self)
return loader.load_weights(
weights,
mapper=self.hf_to_vllm_mapper,
)
source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/qwen3_asr/
lastmod: 2026-09-23

@MULTIMODAL_REGISTRY.register_processor(
Qwen3ASRMultiModalProcessor,
info=Qwen3ASRProcessingInfo,
dummy_inputs=Qwen3ASRDummyInputsBuilder,
)
class Qwen3ASRForConditionalGeneration(
nn.Module,
SupportsMultiModal,
SupportsPP,
SupportsMRoPE,
SupportsTranscription,
SupportsLoRA,
):
# LoRA support
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
supported_languages = ISO639_1_SUPPORTED_LANGS
supports_tower_connector_lora = True
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_prefix={
"thinker.lm_head.": "language_model.lm_head.",
"thinker.model.": "language_model.model.",
"thinker.": "",
# HF format mapper
"model.audio_tower.": "audio_tower.",
"model.language_model.": "language_model.model.",
"model.multi_modal_projector.linear_1.": "audio_tower.proj1.",
"model.multi_modal_projector.linear_2.": "audio_tower.proj2.",
"talker.": None,
"code2wav.": None,
}
)
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("audio"):
return "<|audio_start|><|audio_pad|><|audio_end|>"
raise ValueError("Only audio modality is supported")
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
self.vllm_config = vllm_config # needed for torch compile forward context
thinker_config: Qwen3ASRThinkerConfig = (
vllm_config.model_config.hf_config.thinker_config
)
quant_config = vllm_config.quant_config
multimodal_config = vllm_config.model_config.multimodal_config
self.config = thinker_config
self.multimodal_config = multimodal_config
self.quant_config = quant_config
with self._mark_tower_model(vllm_config, "audio"):
self.audio_tower = Qwen3OmniMoeAudioEncoder(
thinker_config.audio_config,
prefix=maybe_prefix(prefix, "audio_tower"),
)
with self._mark_language_model(vllm_config):
self.language_model = Qwen3ForCausalLM(
vllm_config=vllm_config.with_hf_config(
thinker_config.text_config, architectures=["Qwen3ForCausalLM"]
),
prefix=maybe_prefix(prefix, "language_model"),
)
self.make_empty_intermediate_tensors = (
self.language_model.make_empty_intermediate_tensors
)
def _parse_and_validate_audio_input(
self, **kwargs: object
) -> Qwen2_5OmniAudioFeatureInputs | None:
input_audio_features = kwargs.pop("input_audio_features", None)
audio_feature_lengths = kwargs.pop("audio_feature_lengths", None)
feature_attention_mask = kwargs.pop("feature_attention_mask", None)
if input_audio_features is None:
return None
# inputs features from rust frontend is batched and padded
# with shape [batch_size, n_mels, padded_seq_len], different
# from python's shape [n_mels, batch_size * seq_len]
if (
isinstance(input_audio_features, torch.Tensor)
and input_audio_features.dim() == 3
):
input_audio_features = unpad_and_flat_audio_features(
input_audio_features, audio_feature_lengths
)
return Qwen2_5OmniAudioFeatureInputs(
type="audio_features",
input_features=input_audio_features,
audio_feature_lengths=audio_feature_lengths,
feature_attention_mask=feature_attention_mask,
)
def _parse_and_validate_multimodal_inputs(self, **kwargs: object) -> dict:
mm_input_by_modality = {}
# Preserve the order of modalities if there are multiple of them
# from the order of kwargs.
for input_key in kwargs:
if (
input_key in ("input_audio_features")
and "audio" not in mm_input_by_modality
):
mm_input_by_modality["audio"] = self._parse_and_validate_audio_input(
**kwargs
)
return mm_input_by_modality
def _process_audio_input(
self,
audio_input: Qwen2_5OmniAudioFeatureInputs,
) -> torch.Tensor:
input_features = audio_input["input_features"]
# audio_feature_lengths is keep_on_cpu; the audio tower derives
# device placement from feature_lens, so move it explicitly.
audio_feature_lengths = async_tensor_h2d(
audio_input["audio_feature_lengths"], input_features.device
)
audio_output_lengths = _get_feat_extract_output_lengths(audio_feature_lengths)
audio_features = self.audio_tower(
input_features.to(self.audio_tower.dtype),
feature_lens=audio_feature_lengths,
aftercnn_lens=audio_output_lengths,
)
with gpu_sync_allowed():
split_sizes = audio_output_lengths.tolist()
return audio_features.split(split_sizes)
def embed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings | None:
mm_input_by_modality = self._parse_and_validate_multimodal_inputs(**kwargs)
if not mm_input_by_modality:
return []
# The result multimodal_embeddings is tuple of tensors, with each
# tensor correspoending to a multimodal data item (image or video).
multimodal_embeddings: tuple[torch.Tensor, ...] = ()
# NOTE: It is important to iterate over the keys in this dictionary
# to preserve the order of the modalities.
for modality in mm_input_by_modality:
multimodal_input = mm_input_by_modality[modality]
if modality == "audio":
audio_embeddings = self._process_audio_input(multimodal_input)
multimodal_embeddings += tuple(audio_embeddings)
return multimodal_embeddings
def embed_input_ids(
self,
input_ids: torch.Tensor,
multimodal_embeddings: MultiModalEmbeddings | None = None,
*,
is_multimodal: torch.Tensor | None = None,
) -> torch.Tensor:
inputs_embeds = self._embed_text_input_ids(
input_ids,
self.language_model.embed_input_ids,
is_multimodal=is_multimodal,
)
if multimodal_embeddings is None or len(multimodal_embeddings) == 0:
return inputs_embeds
inputs_embeds = _merge_multimodal_embeddings(
inputs_embeds=inputs_embeds,
multimodal_embeddings=multimodal_embeddings,
is_multimodal=is_multimodal,
)
return inputs_embeds
def forward(
self,
input_ids: torch.Tensor,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
**kwargs: object,
) -> torch.Tensor | IntermediateTensors:
if intermediate_tensors is not None:
inputs_embeds = None
hidden_states = self.language_model.model(
input_ids,
positions,
intermediate_tensors,
inputs_embeds=inputs_embeds,
)
return hidden_states
def compute_logits(
self,
hidden_states: torch.Tensor,
) -> torch.Tensor | None:
return self.language_model.compute_logits(hidden_states)
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
loader = AutoWeightsLoader(self)
loaded_weights = loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
return loaded_weights
def get_mrope_input_positions(
self,
input_tokens: list[int],
mm_features: list[MultiModalFeatureSpec],
) -> tuple[torch.Tensor, int]:
seq_len = len(input_tokens)
if not mm_features:
# No audio features, just return linear positions
llm_positions = (
torch.arange(seq_len, dtype=torch.long).view(1, -1).expand(3, -1)
)
return llm_positions.clone(), 0
llm_pos_ids_list: list[torch.Tensor] = []
st = 0
for mm_feature in sorted(mm_features, key=lambda f: f.mm_position.offset):
offset = mm_feature.mm_position.offset
# The placeholder already contains one token per audio embedding.
# Use its length so M-RoPE can be reconstructed even when a covered
# prefix no longer carries the audio processor tensors.
audio_len = mm_feature.mm_position.length
# Text segment before audio (includes audio_start token)
text_len = offset - st
st_idx = llm_pos_ids_list[-1].max() + 1 if llm_pos_ids_list else 0
text_positions = (
torch.arange(text_len, dtype=torch.long).view(1, -1).expand(3, -1)
+ st_idx
)
llm_pos_ids_list.append(text_positions)
st_idx = st_idx + text_len
# Audio token segment
audio_positions = (
torch.arange(audio_len, dtype=torch.long).view(1, -1).expand(3, -1)
+ st_idx
)
llm_pos_ids_list.append(audio_positions)
st = offset + audio_len
# Handle remaining text (includes audio_end and any trailing text)
if st < seq_len:
st_idx = llm_pos_ids_list[-1].max() + 1 if llm_pos_ids_list else 0
text_len = seq_len - st
final_text_positions = (
torch.arange(text_len, dtype=torch.long).view(1, -1).expand(3, -1)
+ st_idx
)
llm_pos_ids_list.append(final_text_positions)
llm_positions = torch.cat(llm_pos_ids_list, dim=1).reshape(3, -1)
if llm_positions.shape[1] != seq_len:
raise RuntimeError("Position ids length mismatch with input ids length")
mrope_position_delta = (llm_positions.max() + 1 - seq_len).item()
return llm_positions, mrope_position_delta
def get_mm_mapping(self) -> MultiModelKeys:
"""Get the module prefix in multimodal models."""
return MultiModelKeys.from_string_field(
language_model="language_model",
tower_model=["audio_tower."],
)
def get_mm_lora_token_counts(
self,
*,
modality: str,
mm_kwargs: MultiModalKwargsItem | None,
num_mm_embeds: int,
) -> tuple[int, int | None]:
del modality, mm_kwargs
# For Qwen3-ASR, the audio tower produces one embedding per audio
# placeholder token inserted into the prompt (no additional
# merge/downsample step like vision towers). Therefore, the encoder
# token budget is identity.
return num_mm_embeds, None
@classmethod
def get_speech_to_text_config(
cls, model_config: ModelConfig, task_type: str
) -> SpeechToTextConfig:
processor = cached_processor_from_config(model_config)
feature_extractor: WhisperFeatureExtractor = processor.feature_extractor
return SpeechToTextConfig(
max_audio_clip_s=feature_extractor.chunk_length,
sample_rate=feature_extractor.sampling_rate,
)
@classmethod
def get_generation_prompt(cls, stt_params: SpeechToTextParams) -> PromptType:
"""Get the generation prompt to be used for transcription requests.
Matches the official Qwen3-ASR SDK prompt format. The ``system`` turn
is only emitted when the caller supplied a ``prompt``, mirroring the
SDK's ``_build_messages`` (which omits the system role when context is
empty) and preserving the prior no-prompt behavior:
[system: {context}] # only when prompt given
user: {audio}
assistant: [language {Lang}<asr_text>] # when language is forced
"""
audio = stt_params.audio
model_config = stt_params.model_config
language = stt_params.language
task_type = stt_params.task_type
request_prompt = stt_params.request_prompt
to_language = stt_params.to_language
tokenizer = cached_tokenizer_from_config(model_config)
audio_placeholder = cls.get_placeholder_str("audio", 0)
if task_type not in ("transcribe", "translate"):
raise ValueError(
f"Unsupported task_type '{task_type}'. "
"Supported task types are 'transcribe' and 'translate'."
)
context = _sanitize_transcription_user_text(request_prompt)
system_turn = f"<|im_start|>system\n{context}<|im_end|>\n" if context else ""
prompt = (
f"{system_turn}"
f"<|im_start|>user\n{audio_placeholder}<|im_end|>\n"
f"<|im_start|>assistant\n"
)
lang_code = to_language if task_type == "translate" else language
if lang_code is not None:
full_lang_name = cls.supported_languages.get(lang_code, lang_code)
prompt += f"language {full_lang_name}{_ASR_TEXT_TAG}"
prompt_token_ids = cached_encode(tokenizer, prompt)
return TokensPrompt(
prompt_token_ids=prompt_token_ids,
multi_modal_data={"audio": audio},
)
@classmethod
def post_process_output(cls, text: str) -> str:
"""Post-process Qwen3-ASR raw output to extract clean transcription.
The model outputs in format: "language {lang}<asr_text>{transcription}"
This method strips the language prefix and asr_text tags.
"""
return _post_process_qwen3_asr_output(text)
@classmethod
def get_streaming_post_processor_cls(
cls,
) -> type[StreamingTranscriptionPostProcessor]:
return Qwen3ASRStreamingPostProcessor
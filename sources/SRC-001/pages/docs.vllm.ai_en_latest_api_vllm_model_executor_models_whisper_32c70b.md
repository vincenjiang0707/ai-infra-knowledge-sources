source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/whisper/
lastmod: 2026-09-24

@MULTIMODAL_REGISTRY.register_processor(
WhisperMultiModalProcessor,
info=WhisperProcessingInfo,
dummy_inputs=WhisperDummyInputsBuilder,
)
class WhisperForConditionalGeneration(
nn.Module,
SupportsTranscription,
SupportsMultiModal,
SupportsLoRA,
):
# LoRA-specific attributes
packed_modules_mapping = {
"qkv_proj": ["q_proj", "k_proj", "v_proj"],
"kv_proj": ["k_proj", "v_proj"],
}
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_substr={".fc1.": ".mlp.fc1.", ".fc2.": ".mlp.fc2."},
orig_to_new_stacked={
# weight_name: (param_name, shard_id)
".self_attn.q_proj": (".self_attn.qkv_proj", "q"),
".self_attn.k_proj": (".self_attn.qkv_proj", "k"),
".self_attn.v_proj": (".self_attn.qkv_proj", "v"),
".encoder_attn.k_proj": (".encoder_attn.kv_proj", 0),
".encoder_attn.v_proj": (".encoder_attn.kv_proj", 1),
},
orig_to_new_prefix={"proj_out.": None},
)
# Whisper only supports audio-conditioned generation.
supports_transcription_only = True
supports_segment_timestamp = True
supports_explicit_language_detection = True
supported_languages = ISO639_1_SUPPORTED_LANGS
@classmethod
def validate_language(cls, language: str | None) -> str | None:
if language is None:
logger.debug(
"No language specified. Language will be auto-detected "
"from audio. To skip detection, pass the `language` field "
"in the TranscriptionRequest."
)
return None
return super().validate_language(language)
@classmethod
def get_generation_prompt(
cls,
stt_params: SpeechToTextParams,
) -> PromptType:
audio = stt_params.audio
stt_config = stt_params.stt_config
language = stt_params.language
task_type = stt_params.task_type
request_prompt = stt_params.request_prompt
if language is None:
raise ValueError(
"Language must be specified when creating the Whisper prompt"
)
decoder_text = (
f"<|prev|>{request_prompt}" if request_prompt else ""
) + f"<|startoftranscript|><|{language}|><|{task_type}|><|notimestamps|>"
return ExplicitEncoderDecoderPrompt(
encoder_prompt=TextPrompt(
prompt="", # Whisper does not support encoder prompt.
multi_modal_data={"audio": (audio, stt_config.sample_rate)},
),
decoder_prompt=TextPrompt(prompt=decoder_text),
)
@classmethod
def get_language_token_ids(
cls,
tokenizer: object,
) -> list[int]:
"""Return token IDs for all supported language tokens.
Used with ``SamplingParams.allowed_token_ids`` to constrain
language detection to only produce valid language tokens.
"""
token_ids = [
tokenizer.convert_tokens_to_ids(f"<|{lang_code}|>")
for lang_code in cls.supported_languages
]
return token_ids
@classmethod
def get_language_detection_prompt(
cls,
audio: np.ndarray,
stt_config: SpeechToTextConfig,
) -> PromptType:
"""Return a prompt that elicits a single language token from Whisper.
Feed only ``<|startoftranscript|>`` as the decoder input so the model
predicts the most likely language token (e.g. ``<|de|>``).
"""
return ExplicitEncoderDecoderPrompt(
encoder_prompt=TextPrompt(
prompt="",
multi_modal_data={"audio": (audio, stt_config.sample_rate)},
),
decoder_prompt=TextPrompt(prompt="<|startoftranscript|>"),
)
@classmethod
def parse_language_detection_output(
cls,
token_ids: list[int],
tokenizer: object,
) -> str | None:
"""Parse the language token predicted by Whisper.
Decodes the first token ID and extracts the language code from the
``<|xx|>`` format. Expects a valid language token from constrained generation.
"""
decoded = tokenizer.decode(
[token_ids[0]],
skip_special_tokens=False,
)
# Whisper language tokens have the form <|xx|>
assert decoded.startswith("<|") and decoded.endswith("|>")
lang_code = decoded[2:-2]
assert lang_code in cls.supported_languages
return lang_code
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("audio"):
return None
raise ValueError("Only audio modality is supported")
@classmethod
def get_speech_to_text_config(
cls, model_config: ModelConfig, task_type: str
) -> SpeechToTextConfig:
processor = cached_processor_from_config(model_config)
return SpeechToTextConfig(
max_audio_clip_s=processor.feature_extractor.chunk_length,
sample_rate=processor.feature_extractor.sampling_rate,
)
@classmethod
def get_num_audio_tokens(
cls,
audio_duration_s: float,
stt_config: SpeechToTextConfig,
model_config: ModelConfig,
) -> int | None:
processor = cached_processor_from_config(model_config)
hop_length = processor.feature_extractor.hop_length
assert hop_length is not None
# NOTE(NickLucche) user can't pass encoder
# prompts directly at least not to Whisper.
# One indicator of the encoder amount of processing
# is the log-mel spectogram length.
return math.ceil(audio_duration_s * stt_config.sample_rate / hop_length)
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
config = vllm_config.model_config.hf_config
quant_config = vllm_config.quant_config
self.config = config
self.dtype = vllm_config.model_config.dtype
with self._mark_composite_model(
vllm_config,
language_targets=WhisperDecoder,
tower_targets={"audio": WhisperEncoder},
):
self.model = WhisperModel(vllm_config=vllm_config, prefix=prefix)
self.proj_out = ParallelLMHead(
config.vocab_size,
config.d_model,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "proj_out"),
)
self.proj_out = self.proj_out.tie_weights(self.model.decoder.embed_tokens)
logit_scale = getattr(config, "logit_scale", 1.0)
self.logits_processor = LogitsProcessor(config.vocab_size, scale=logit_scale)
def forward(
self,
input_ids: torch.Tensor,
positions: torch.Tensor,
encoder_outputs: list[torch.Tensor] | None = None,
**kwargs,
) -> torch.Tensor:
if encoder_outputs is None:
encoder_outputs = []
decoder_outputs = self.model(
input_ids=input_ids,
positions=positions,
encoder_outputs=encoder_outputs,
)
return decoder_outputs
def embed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
# Required as part of SupportsMultiModal interface.
audio_input = self._parse_and_validate_audio_input(**kwargs)
# Split concatenated encoder outputs into one tensor per audio input
enc_output = self.model.get_encoder_outputs(audio_input["input_features"])
# The assumption is we can only process whole mm items (audios)
return enc_output.unbind(dim=0)
def embed_input_ids(
self,
input_ids: torch.Tensor,
multimodal_embeddings: MultiModalEmbeddings | None = None,
*,
is_multimodal: torch.Tensor | None = None,
) -> torch.Tensor:
# This method just returns the decoder sequence embeddings since
# Whisper does not have encoder text tokens.
return self.model.decoder.embed_input_ids(input_ids)
def _parse_and_validate_audio_input(self, **kwargs: object) -> WhisperAudioInputs:
input_features = kwargs.pop("input_features", None)
if input_features is not None:
input_features = json_map_leaves(lambda x: x.to(self.dtype), input_features)
return WhisperAudioInputs(input_features=input_features)
def compute_logits(self, hidden_states: torch.Tensor) -> torch.Tensor:
logits = self.logits_processor(self.proj_out, hidden_states)
return logits
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
loader = AutoWeightsLoader(self)
# add fake zeros bias for k_proj to state_dict
weights = _create_fake_bias_for_k_proj(weights, ".k_proj.weight")
return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
source: https://docs.vllm.ai/en/latest/contributing/model/transcription/
lastmod: 2026-09-23

# Speech-to-Text (Transcription/Translation) Support[¶](https://docs.vllm.ai#speech-to-text-transcriptiontranslation-support)

This document walks you through the steps to add support for speech-to-text (ASR) models to vLLM’s transcription and translation APIs by implementing [SupportsTranscription](https://docs.vllm.ai/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription). Please refer to the [supported models](https://docs.vllm.ai/models/supported_models/#transcription) for further guidance.

## Update the base vLLM model[¶](https://docs.vllm.ai#update-the-base-vllm-model)

It is assumed you have already implemented your model in vLLM according to the basic model guide. Extend your model with the [SupportsTranscription](https://docs.vllm.ai/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription) interface and implement the following class attributes and methods.

`supported_languages`

and `supports_transcription_only`

[¶](https://docs.vllm.ai#supported_languages-and-supports_transcription_only)

Declare supported languages and capabilities:

- The
`supported_languages`

mapping is validated at init time. - Set
`supports_transcription_only=True`

if the model should not serve text generation (eg Whisper).

## supported_languages and supports_transcription_only

from typing import ClassVar, Mapping, Literal
import numpy as np
import torch
from torch import nn
from vllm.config import ModelConfig, SpeechToTextConfig
from vllm.inputs import PromptType
from vllm.model_executor.models.interfaces import SupportsTranscription
class YourASRModel(nn.Module, SupportsTranscription):
# Map of ISO 639-1 language codes to language names
supported_languages: ClassVar[Mapping[str, str]] = {
"en": "English",
"it": "Italian",
# ... add more as needed
}
# If your model only supports audio-conditioned generation
# (no text-only generation), enable this flag.
supports_transcription_only: ClassVar[bool] = True


Provide an ASR configuration via [get_speech_to_text_config](https://docs.vllm.ai/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription.get_speech_to_text_config).

This is for controlling general behavior of the API when serving your model:

## get_speech_to_text_config()

class YourASRModel(nn.Module, SupportsTranscription):
...
@classmethod
def get_speech_to_text_config(
cls,
model_config: ModelConfig,
task_type: Literal["transcribe", "translate"],
) -> SpeechToTextConfig:
return SpeechToTextConfig(
sample_rate=16_000,
max_audio_clip_s=30,
# Set to None to disable server-side chunking if your
# model/processor handles it already
min_energy_split_window_size=None,
)


See [Audio preprocessing and chunking](https://docs.vllm.ai#audio-preprocessing-and-chunking) for what each field controls.

Implement the prompt construction via [get_generation_prompt](https://docs.vllm.ai/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription.get_generation_prompt). The server builds a [SpeechToTextParams](https://docs.vllm.ai/api/vllm/config/speech_to_text/#vllm.config.speech_to_text.SpeechToTextParams) object that bundles the resampled waveform, task parameters, and request-specific options. Your model receives this single object and returns a valid [PromptType](https://docs.vllm.ai/api/vllm/inputs/llm/#vllm.inputs.llm.PromptType). There are two common patterns:

#### Multimodal LLM with audio embeddings (e.g., Voxtral, Gemma3n)[¶](https://docs.vllm.ai#multimodal-llm-with-audio-embeddings-eg-voxtral-gemma3n)

Return a dict containing `multi_modal_data`

with the audio, and either a `prompt`

string or `prompt_token_ids`

:

## get_generation_prompt()

from vllm.config.speech_to_text import SpeechToTextParams
class YourASRModel(nn.Module, SupportsTranscription):
...
@classmethod
def get_generation_prompt(
cls,
stt_params: SpeechToTextParams,
) -> PromptType:
audio = stt_params.audio
stt_config = stt_params.stt_config
task_type = stt_params.task_type
task_word = "Transcribe" if task_type == "transcribe" else "Translate"
prompt = (
"<start_of_turn>user\n"
f"{task_word} this audio: <audio_soft_token>"
"<end_of_turn>\n<start_of_turn>model\n"
)
return {
"multi_modal_data": {"audio": (audio, stt_config.sample_rate)},
"prompt": prompt,
}


For further clarification on multi modal inputs, please refer to [Multi-Modal Inputs](https://docs.vllm.ai/features/multimodal_inputs/).

#### Encoder–decoder audio-only (e.g., Whisper)[¶](https://docs.vllm.ai#encoderdecoder-audio-only-eg-whisper)

Return a dict with separate `encoder_prompt`

and `decoder_prompt`

entries:

## get_generation_prompt()

from vllm.config.speech_to_text import SpeechToTextParams
class YourASRModel(nn.Module, SupportsTranscription):
...
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
raise ValueError("Language must be specified")
prompt = {
"encoder_prompt": {
"prompt": "",
"multi_modal_data": {
"audio": (audio, stt_config.sample_rate),
},
},
"decoder_prompt": (
(f"<|prev|>{request_prompt}" if request_prompt else "")
+ f"<|startoftranscript|><|{language}|>"
+ f"<|{task_type}|><|notimestamps|>"
),
}
return cast(PromptType, prompt)


`validate_language`

(optional)[¶](https://docs.vllm.ai#validate_language-optional)

Language validation via [validate_language](https://docs.vllm.ai/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription.validate_language)

If your model requires a language and you want a default, override this method (see Whisper):

## validate_language()

@classmethod
def validate_language(cls, language: str | None) -> str | None:
if language is None:
logger.warning(
"Defaulting to language='en'. If you wish to transcribe "
"audio in a different language, pass the `language` field "
"in the TranscriptionRequest."
)
language = "en"
return super().validate_language(language)


`get_num_audio_tokens`

(optional)[¶](https://docs.vllm.ai#get_num_audio_tokens-optional)

Token accounting for streaming via [get_num_audio_tokens](https://docs.vllm.ai/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription.get_num_audio_tokens)

Provide a fast duration→token estimate to improve streaming usage statistics:

## get_num_audio_tokens()

class YourASRModel(nn.Module, SupportsTranscription):
...
@classmethod
def get_num_audio_tokens(
cls,
audio_duration_s: float,
stt_config: SpeechToTextConfig,
model_config: ModelConfig,
) -> int | None:
# Return None if unknown; otherwise return an estimate.
return int(audio_duration_s * stt_config.sample_rate // 320) # example


## Audio preprocessing and chunking[¶](https://docs.vllm.ai#audio-preprocessing-and-chunking)

The API server takes care of basic audio I/O and optional chunking before building prompts:

- Resampling: Input audio is resampled to
`SpeechToTextConfig.sample_rate`

using.`AudioResampler`

- Chunking: If
`SpeechToTextConfig.allow_audio_chunking`

is True and the duration exceeds`max_audio_clip_s`

, the server splits the audio into chunks and generates a prompt per chunk. There is no overlap between chunks, overlap_chunk_second controls the size of the search window used to find the split point. - Energy-aware splitting: When
`min_energy_split_window_size`

is set, the server finds low-energy regions to minimize cutting within words.

Relevant server logic:

## _preprocess_speech_to_text()

# vllm/entrypoints/openai/speech_to_text.py
async def _preprocess_speech_to_text(...):
language = self.model_cls.validate_language(request.language)
...
y, sr = load_audio(bytes_, sr=self.asr_config.sample_rate)
duration = get_audio_duration(y=y, sr=sr)
do_split_audio = (self.asr_config.allow_audio_chunking
and duration > self.asr_config.max_audio_clip_s)
chunks = [y] if not do_split_audio else self._split_audio(y, int(sr))
prompts = []
for chunk in chunks:
stt_params = request.build_stt_params(
audio=chunk,
stt_config=self.asr_config,
model_config=self.model_config,
task_type=self.task_type,
)
prompt = self.model_cls.get_generation_prompt(stt_params)
prompts.append(prompt)
return prompts, duration


## Exposing tasks automatically[¶](https://docs.vllm.ai#exposing-tasks-automatically)

vLLM automatically advertises transcription support if your model implements the interface:

if supports_transcription(model):
if model.supports_transcription_only:
return ["transcription"]
supported_tasks.append("transcription")


When enabled, the server initializes the transcription and translation handlers:

state.openai_serving_transcription = OpenAIServingTranscription(...) if "transcription" in supported_tasks else None
state.openai_serving_translation = OpenAIServingTranslation(...) if "transcription" in supported_tasks else None


No extra registration is required beyond having your model class available via the model registry and implementing [ SupportsTranscription](https://docs.vllm.ai/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription).

## Examples in-tree[¶](https://docs.vllm.ai#examples-in-tree)

- Whisper encoder–decoder (audio-only):
[vllm/model_executor/models/whisper.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/whisper.py) - Voxtral decoder-only (audio embeddings + LLM):
[vllm/model_executor/models/voxtral.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/voxtral.py). Make sure to have installed`mistral-common[audio]`

. - Gemma3n decoder-only with fixed instruction prompt:
[vllm/model_executor/models/gemma3n_mm.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/gemma3n_mm.py) - Qwen3-Omni multimodal with audio embeddings:
[vllm/model_executor/models/qwen3_omni_moe_thinker.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/qwen3_omni_moe_thinker.py)

## Test with the API[¶](https://docs.vllm.ai#test-with-the-api)

Once your model implements [ SupportsTranscription](https://docs.vllm.ai/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription), you can test the endpoints (API mimics OpenAI):

-
Transcription (ASR):

-
Translation (source → English unless otherwise supported):


Or check out more examples in [ examples/speech_to_text](https://github.com/vllm-project/vllm/tree/main/examples/speech_to_text).

Note

- If your model handles chunking internally (e.g., via its processor or encoder), set
`min_energy_split_window_size=None`

in the returnedto disable server-side chunking.`SpeechToTextConfig`

- Implementing
`get_num_audio_tokens`

improves accuracy of streaming usage metrics (`prompt_tokens`

) without an extra forward pass. - For multilingual behavior, keep
`supported_languages`

aligned with actual model capabilities.
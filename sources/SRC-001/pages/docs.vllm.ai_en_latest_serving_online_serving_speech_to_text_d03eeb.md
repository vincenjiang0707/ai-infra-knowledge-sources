source: https://docs.vllm.ai/en/latest/serving/online_serving/speech_to_text/
lastmod: 2026-09-24

# Speech to Text APIs[¶](https://docs.vllm.ai#speech-to-text-apis)

## Transcriptions API[¶](https://docs.vllm.ai#transcriptions-api)

Our Transcriptions API is compatible with [OpenAI's Transcriptions API](https://platform.openai.com/docs/api-reference/audio/createTranscription); you can use the [official OpenAI Python client](https://github.com/openai/openai-python) to interact with it.

Note

To use the Transcriptions API, please install with extra audio dependencies using `pip install vllm[audio]`

.

Code example: [ examples/speech_to_text/openai/openai_transcription_client.py](https://github.com/vllm-project/vllm/blob/main/examples/speech_to_text/openai/openai_transcription_client.py)

NOTE: beam search is currently supported in the transcriptions endpoint for encoder-decoder multimodal models, e.g., whisper, but highly inefficient as work for handling the encoder/decoder cache is actively ongoing. This is an active point of ongoing optimization and will be handled properly in the very near future.

### API Enforced Limits[¶](https://docs.vllm.ai#api-enforced-limits)

Set the maximum audio file size (in MB) that VLLM will accept, via the `VLLM_MAX_AUDIO_CLIP_FILESIZE_MB`

environment variable. Default is 25 MB.

### Uploading Audio Files[¶](https://docs.vllm.ai#uploading-audio-files)

The Transcriptions API supports uploading audio files in various formats including FLAC, MP3, MP4, MPEG, MPGA, M4A, OGG, WAV, and WEBM.

**Using OpenAI Python Client:**

## Code

from openai import OpenAI
client = OpenAI(
base_url="http://localhost:8000/v1",
api_key="token-abc123",
)
# Upload audio file from disk
with open("audio.mp3", "rb") as audio_file:
transcription = client.audio.transcriptions.create(
model="openai/whisper-large-v3-turbo",
file=audio_file,
language="en",
response_format="verbose_json",
)
print(transcription.text)


**Using curl with multipart/form-data:**

## Code

```bash
curl -X POST "http://localhost:8000/v1/audio/transcriptions" \
-H "Authorization: Bearer token-abc123" \
-F "[[email protected]](https://docs.vllm.ai/cdn-cgi/l/email-protection)" \
-F "model=openai/whisper-large-v3-turbo" \
-F "language=en" \
-F "response_format=verbose_json"
```


**Supported Parameters:**

`file`

: The audio file to transcribe (required)`model`

: The model to use for transcription (required)`language`

: The language code (e.g., "en", "zh") (optional)`prompt`

: Optional text to guide the transcription style (optional)`response_format`

: Format of the response ("json", "text", "verbose_json", or "diarized_json") (optional)`temperature`

: Sampling temperature between 0 and 1 (optional)

For the complete list of supported parameters including sampling parameters and vLLM extensions, see the [protocol definitions](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/speech_to_text/transcription/protocol.py).

**Response Format:**

For `verbose_json`

response format:

## Code

```json
{
"text": "Hello, this is a transcription of the audio file.",
"language": "en",
"duration": 5.42,
"segments": [
{
"id": 0,
"seek": 0,
"start": 0.0,
"end": 2.5,
"text": "Hello, this is a transcription",
"tokens": [50364, 938, 428, 307, 275, 28347],
"temperature": 0.0,
"avg_logprob": -0.245,
"compression_ratio": 1.235,
"no_speech_prob": 0.012
}
]
}
```


Currently “verbose_json” response format doesn’t support no_speech_prob.

For models with diarization support, `diarized_json`

returns OpenAI-compatible speaker segments. Currently, this is supported by `OpenMOSS-Team/MOSS-Transcribe-Diarize`

.

```json
{
"task": "transcribe",
"duration": 6.1,
"text": "Hello. Hi, how are you?",
"segments": [
{
"type": "transcript.text.segment",
"id": "segment_0",
"start": 0.0,
"end": 2.8,
"text": "Hello.",
"speaker": "S01"
}
],
"usage": {"type": "duration", "seconds": 7}
}
```


### Extra Parameters[¶](https://docs.vllm.ai#extra-parameters)

The following [sampling parameters](https://docs.vllm.ai/api/#inference-parameters) are supported.

## Code

use_beam_search: bool = False
"""Whether or not beam search should be used."""
n: int = 1
"""The number of beams to be used in beam search."""
length_penalty: float = 1.0
"""Length penalty to be used for beam search."""
include_stop_str_in_output: bool = False
"""Whether to include the stop strings in output text."""
temperature: float = Field(default=0.0)
"""The sampling temperature, between 0 and 1.
Higher values like 0.8 will make the output more random, while lower values
like 0.2 will make it more focused / deterministic. If set to 0, the model
will use [log probability](https://en.wikipedia.org/wiki/Log_probability)
to automatically increase the temperature until certain thresholds are hit.
"""
top_p: float | None = None
"""Enables nucleus (top-p) sampling, where tokens are selected from the
smallest possible set whose cumulative probability exceeds `p`.
"""
top_k: int | None = None
"""Limits sampling to the `k` most probable tokens at each step."""
min_p: float | None = None
"""Filters out tokens with a probability lower than `min_p`, ensuring a
minimum likelihood threshold during sampling.
"""
seed: int | None = Field(None, ge=_LONG_INFO.min, le=_LONG_INFO.max)
"""The seed to use for sampling."""
frequency_penalty: float | None = 0.0
"""The frequency penalty to use for sampling."""
repetition_penalty: float | None = None
"""The repetition penalty to use for sampling."""
presence_penalty: float | None = 0.0
"""The presence penalty to use for sampling."""
max_completion_tokens: int | None = None
"""The maximum number of tokens to generate."""


The following extra parameters are supported:

## Code

# Flattened stream option to simplify form data.
stream_include_usage: bool | None = False
stream_continuous_usage_stats: bool | None = False
vllm_xargs: dict[str, str | int | float | list[str | int | float]] | None = Field(
default=None,
description=(
"Additional request parameters with (list of) string or "
"numeric values, used by custom extensions."
),
)


## Translations API[¶](https://docs.vllm.ai#translations-api)

Our Translation API is compatible with [OpenAI's Translations API](https://platform.openai.com/docs/api-reference/audio/createTranslation); you can use the [official OpenAI Python client](https://github.com/openai/openai-python) to interact with it. Whisper models can translate audio from one of the 55 non-English supported languages into English. Please mind that the popular `openai/whisper-large-v3-turbo`

model does not support translating.

Note

To use the Translation API, please install with extra audio dependencies using `pip install vllm[audio]`

.

Code example: [ examples/speech_to_text/openai/openai_translation_client.py](https://github.com/vllm-project/vllm/blob/main/examples/speech_to_text/openai/openai_translation_client.py)

### Extra Parameters[¶](https://docs.vllm.ai#extra-parameters_1)

The following [sampling parameters](https://docs.vllm.ai/api/#inference-parameters) are supported.

use_beam_search: bool = False
"""Whether or not beam search should be used."""
n: int = 1
"""The number of beams to be used in beam search."""
length_penalty: float = 1.0
"""Length penalty to be used for beam search."""
include_stop_str_in_output: bool = False
"""Whether to include the stop strings in output text."""
seed: int | None = Field(None, ge=_LONG_INFO.min, le=_LONG_INFO.max)
"""The seed to use for sampling."""
temperature: float = Field(default=0.0)
"""The sampling temperature, between 0 and 1.
Higher values like 0.8 will make the output more random, while lower values
like 0.2 will make it more focused / deterministic. If set to 0, the model
will use [log probability](https://en.wikipedia.org/wiki/Log_probability)
to automatically increase the temperature until certain thresholds are hit.
"""
top_p: float | None = None
"""Enables nucleus (top-p) sampling, where tokens are selected from the
smallest possible set whose cumulative probability exceeds `p`.
"""
top_k: int | None = None
"""Limits sampling to the `k` most probable tokens at each step."""
min_p: float | None = None
"""Filters out tokens with a probability lower than `min_p`, ensuring a
minimum likelihood threshold during sampling.
"""
frequency_penalty: float | None = 0.0
"""The frequency penalty to use for sampling."""
repetition_penalty: float | None = None
"""The repetition penalty to use for sampling."""
presence_penalty: float | None = 0.0
"""The presence penalty to use for sampling."""


The following extra parameters are supported:

language: str | None = None
"""The language of the input audio we translate from.
Supplying the input language in
[ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format
will improve accuracy.
"""
hotwords: str | None = None
"""
hotwords refers to a list of important words or phrases that the model
should pay extra attention to during transcription.
"""
to_language: str | None = None
"""The language of the input audio we translate to.
Please note that this is not supported by all models, refer to the specific
model documentation for more details.
For instance, Whisper only supports `to_language=en`.
"""
stream: bool | None = False
"""Custom field not present in the original OpenAI definition. When set,
it will enable output to be streamed in a similar fashion as the Chat
Completion endpoint.
"""
# Flattened stream option to simplify form data.
stream_include_usage: bool | None = False
stream_continuous_usage_stats: bool | None = False
max_completion_tokens: int | None = None
"""The maximum number of tokens to generate."""
vllm_xargs: dict[str, str | int | float | list[str | int | float]] | None = Field(
default=None,
description=(
"Additional request parameters with (list of) string or "
"numeric values, used by custom extensions."
),
)


## Realtime API[¶](https://docs.vllm.ai#realtime-api)

The Realtime API provides WebSocket-based streaming audio transcription, allowing real-time speech-to-text as audio is being recorded.

Note

To use the Realtime API, please install with extra audio dependencies using `uv pip install vllm[audio]`

.

### Audio Format[¶](https://docs.vllm.ai#audio-format)

Audio must be sent as base64-encoded PCM16 audio at 16kHz sample rate, mono channel.

### Protocol Overview[¶](https://docs.vllm.ai#protocol-overview)

- Client connects to
`ws://host/v1/realtime`

- Server sends
`session.created`

event - Client optionally sends
`session.update`

with model/params - Client sends
`input_audio_buffer.commit`

when ready - Client sends
`input_audio_buffer.append`

events with base64 PCM16 chunks - Server sends
`transcription.delta`

events with incremental text - Server sends
`transcription.done`

with final text + usage - Repeat from step 5 for next utterance
- Optionally, client sends input_audio_buffer.commit with final=True to signal audio input is finished. Useful when streaming audio files

### Client → Server Events[¶](https://docs.vllm.ai#client-server-events)

| Event | Description |
|---|---|
`input_audio_buffer.append` | Send base64-encoded audio chunk: `{"type": "input_audio_buffer.append", "audio": "<base64>"}` |
`input_audio_buffer.commit` | Trigger transcription processing or end: `{"type": "input_audio_buffer.commit", "final": bool}` |
`session.update` | Configure session: `{"type": "session.update", "model": "model-name"}` |

### Server → Client Events[¶](https://docs.vllm.ai#server-client-events)

| Event | Description |
|---|---|
`session.created` | Connection established with session ID and timestamp |
`transcription.delta` | Incremental transcription text: `{"type": "transcription.delta", "delta": "text"}` |
`transcription.done` | Final transcription with usage stats |
`error` | Error notification with message and optional code |

#### Example Clients[¶](https://docs.vllm.ai#example-clients)

[openai_realtime_client.py](https://github.com/vllm-project/vllm/tree/main/examples/speech_to_text/realtime/openai_realtime_client.py)- Upload and transcribe an audio file[openai_realtime_microphone_client.py](https://github.com/vllm-project/vllm/tree/main/examples/speech_to_text/realtime/openai_realtime_microphone_client.py)- Gradio demo for live microphone transcription
source: https://github.com/vllm-project/guidellm/issues/984

## Bug Description

GuideLLM persists complete backend request arguments in each request statistic. For transcription and translation requests, those arguments include the multipart file tuple containing the full encoded audio byte payload.

Pydantic serializes the bytes as Base64, after which the resulting string is retained as `request_args`

and written to JSON/YAML reports. HTML output also embeds sampled `request_args`

directly into its generated JavaScript.

For a benchmark containing 75 minutes of 16 kHz mono WAV audio:

```
75 x 60 x 16,000 x 2 bytes = 144,000,000 bytes
Base64 size ~= 192,000,000 characters ~= 183 MiB
```


This produces JSON and HTML reports around 185 MB. The bulk of the report is therefore recoverable input audio, not transcription text.

This causes:

- Extremely large JSON, YAML, and HTML artifacts.
- Large transient memory allocations during Base64 and report serialization.
- Slow or failed artifact transfers.
- Browser parsing and rendering problems for HTML reports.
- An unexpected privacy/data-retention risk because reports contain source media.
- Similar exposure for other multimodal endpoints when raw media is present in persisted request bodies.

## Expected Behavior

Transport payloads should not be retained in benchmark reports.

Persisted request metadata should retain useful reproducibility information, such as:

- Filename
- MIME type
- Payload byte count
- Model and ordinary request parameters

The actual file bytes and embedded Base64 media should be omitted or replaced by bounded metadata before assigning `request_args`

.

HTML output should additionally limit the size of displayed request samples.

## Steps to Reproduce

from guidellm.backends.openai.request_handlers import AudioRequestHandler
from guidellm.schemas import GenerationRequest
audio = b"\x00" * (1024 * 1024)
request = GenerationRequest(
columns={
"audio_column": [
{
"audio": audio,
"file_name": "audio.wav",
"mimetype": "audio/wav",
}
]
}
)
arguments = AudioRequestHandler().format(request)
serialized = arguments.model_dump_json()
print(len(audio))
print(len(serialized))

The approximately 1 MiB binary input produces roughly 1.33 MiB of Base64 data inside `serialized`

. Response compilation stores this string as `request_args`

, and serialized benchmark reports retain it.

For workloads with five or fewer requests, HTML's five-request sample can include every audio payload.

## Operating System

Not OS-specific; observed in a Linux-hosted benchmark environment.

## Python Version

Not Python-version-specific.

## GuideLLM Version

`main`

at `39383552962841086d05e25c37b58a83ef06c758`

.

## Installation Method

Source checkout.

## Additional Context

This is related to closed issue [#38](https://github.com/vllm-project/guidellm/issues/38), but request sampling does not adequately address binary payloads:

- A selected request still retains its complete media.
- Long-form workloads may contain fewer requests than the sample limit.
`sample_size=0`

also removes useful generated outputs such as transcriptions.
- The privacy issue exists regardless of total report size.

## Bug Description

GuideLLM persists complete backend request arguments in each request statistic. For transcription and translation requests, those arguments include the multipart file tuple containing the full encoded audio byte payload.

Pydantic serializes the bytes as Base64, after which the resulting string is retained as

`request_args`

and written to JSON/YAML reports. HTML output also embeds sampled`request_args`

directly into its generated JavaScript.For a benchmark containing 75 minutes of 16 kHz mono WAV audio:

This produces JSON and HTML reports around 185 MB. The bulk of the report is therefore recoverable input audio, not transcription text.

This causes:

## Expected Behavior

Transport payloads should not be retained in benchmark reports.

Persisted request metadata should retain useful reproducibility information, such as:

The actual file bytes and embedded Base64 media should be omitted or replaced by bounded metadata before assigning

`request_args`

.HTML output should additionally limit the size of displayed request samples.

## Steps to Reproduce

The approximately 1 MiB binary input produces roughly 1.33 MiB of Base64 data inside

`serialized`

. Response compilation stores this string as`request_args`

, and serialized benchmark reports retain it.For workloads with five or fewer requests, HTML's five-request sample can include every audio payload.

## Operating System

Not OS-specific; observed in a Linux-hosted benchmark environment.

## Python Version

Not Python-version-specific.

## GuideLLM Version

`main`

at`39383552962841086d05e25c37b58a83ef06c758`

.## Installation Method

Source checkout.

## Additional Context

This is related to closed issue #38, but request sampling does not adequately address binary payloads:

`sample_size=0`

also removes useful generated outputs such as transcriptions.
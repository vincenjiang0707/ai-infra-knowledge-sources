source: https://github.com/vllm-project/guidellm/issues/833

### Problem Statement

When benchmarking audio transcription one of the more common metrics that's used is the Real-Time-Factor ([RTF](https://openvoice-tech.net/index.php/Real-time-factor)), or its inverse RTFx.

Currently, GuideLLM doesn't provide any insight into this when benchmarking audio, while it's very simple to calculate - E2E latency divided by audio duration (RTF) or the other way around (RTFx).

### Proposed Solution

When using the `audio_transcription`

or the `realtime_transcription`

request types, automatically report RTF and RTFx.

### Alternatives Considered

We could accept that RTF and RTFx won't be available when benchmarking audio transcription.

### Usage Examples

```bash
python3 -m vllm.entrypoints.openai.api_server \
--model mistralai/Voxtral-Mini-4B-Realtime-2602 \
--tokenizer-mode mistral \
--config-format mistral \
--load-format mistral \
--trust-remote-code \
--compilation-config '{"cudagraph_mode":"PIECEWISE"}' \
--tensor-parallel-size 1 \
--max-model-len 45000 \
--max-num-batched-tokens 8192 \
--max-num-seqs 16 \
--gpu-memory-utilization 0.90 \
--host 0.0.0.0 --port 8000
guidellm benchmark \
--target http://localhost:8000/v1 \
--request-type realtime_transcription \
--backend openai_realtime_ws \
--data /workspace/custom-audio-dataset/hf_dataset \
--profile synchronous \
--max-requests 10 \
--output-dir /workspace/repo/runs/2026-04-23T13-41-41 \
--outputs json,html,csv
# RTF & RTFx always reported when `request-type=realtime_transcription` or `request-type=audio_transcription`
```

### Additional Context

[#713](https://github.com/vllm-project/guidellm/pull/713)

[https://openvoice-tech.net/index.php/Real-time-factor](https://openvoice-tech.net/index.php/Real-time-factor)

I am interested in creating a PR for this 😄

## Problem Statement

When benchmarking audio transcription one of the more common metrics that's used is the Real-Time-Factor (RTF), or its inverse RTFx.

Currently, GuideLLM doesn't provide any insight into this when benchmarking audio, while it's very simple to calculate - E2E latency divided by audio duration (RTF) or the other way around (RTFx).

## Proposed Solution

When using the

`audio_transcription`

or the`realtime_transcription`

request types, automatically report RTF and RTFx.## Alternatives Considered

We could accept that RTF and RTFx won't be available when benchmarking audio transcription.

## Usage Examples

## Additional Context

#713

https://openvoice-tech.net/index.php/Real-time-factor

I am interested in creating a PR for this 😄
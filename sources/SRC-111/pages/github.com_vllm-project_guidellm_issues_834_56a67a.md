source: https://github.com/vllm-project/guidellm/issues/834

### Problem Statement

When benchmarking realtime transcription a user might want to simulate a realistic workload, where the input is not sent as fast as possible, but sent packet by packet as if in real time, waiting the appropriate durations between packets to simulate a live stream of audio.

Currently, there is no throttling or timing or scheduling mechanism for sending individual audio packets, and so they are sent as fast as possible, creating a load which could be unrealistic for many scenarios.

### Proposed Solution

Add a configurable `websocket_backend_RTF`

argument that will allow a user to decide the max speed at which they wish the packets to be sent. `websocket_backend_RTF=1`

would mean to send one second worth of packets every one second, and `websocket_backend_RTF=2`

would mean sending one second worth of packets every two seconds, and `websocket_backend_RTF=0.5`

would mean sending one second worth of packets every half second. `websocket_backend_RTF=0`

means that packets will be sent as fast as possible, and it should be the default behavior.

### Alternatives Considered

The user could try to increase the parallelism and reduce the benchmarking CPU to make GuideLLM reduce the speed to something closer to a realistic live stream, but that's very finicky.

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
--websocket-backend-rtf 1.0 \
--data /workspace/custom-audio-dataset/hf_dataset \
--profile synchronous \
--max-requests 10 \
--output-dir /workspace/repo/runs/2026-04-23T13-41-41 \
--outputs json,html,csv
```

### Additional Context

[#713](https://github.com/vllm-project/guidellm/pull/713)

[https://openvoice-tech.net/index.php/Real-time-factor](https://openvoice-tech.net/index.php/Real-time-factor)

I am interested in creating a PR for this 😄

## Problem Statement

When benchmarking realtime transcription a user might want to simulate a realistic workload, where the input is not sent as fast as possible, but sent packet by packet as if in real time, waiting the appropriate durations between packets to simulate a live stream of audio.

Currently, there is no throttling or timing or scheduling mechanism for sending individual audio packets, and so they are sent as fast as possible, creating a load which could be unrealistic for many scenarios.

## Proposed Solution

Add a configurable

`websocket_backend_RTF`

argument that will allow a user to decide the max speed at which they wish the packets to be sent.`websocket_backend_RTF=1`

would mean to send one second worth of packets every one second, and`websocket_backend_RTF=2`

would mean sending one second worth of packets every two seconds, and`websocket_backend_RTF=0.5`

would mean sending one second worth of packets every half second.`websocket_backend_RTF=0`

means that packets will be sent as fast as possible, and it should be the default behavior.## Alternatives Considered

The user could try to increase the parallelism and reduce the benchmarking CPU to make GuideLLM reduce the speed to something closer to a realistic live stream, but that's very finicky.

## Usage Examples

## Additional Context

#713

https://openvoice-tech.net/index.php/Real-time-factor

I am interested in creating a PR for this 😄
# [Issue #832] Websocket backend metrics

source: https://github.com/vllm-project/guidellm/issues/832
state: closed | updated: 2026-08-12T17:40:39Z
labels: 

## 正文

### Problem Statement

When using the websocket backend for a task which has some sort of correspondence between input packets and output tokens (e.g realtime transcription), we might want more metrics than just the classical LLM metrics such as TTFT, TPOT, E2E etc, but might want to know things like the Round-Trip Time ([RTT](https://en.wikipedia.org/wiki/Round-trip_delay)), which is essentially the user experienced system lag.

Without exact alignment between input packets and output tokens and their timings - we cannot know the exact RTT, but we can estimate it in 3 different ways:

1. TTFT - Time between the first sent packet time and the first received token time (`T_recv[0] - T_sent[0]`). Basically the RTT of the first token, which is already an OK proxy
2. TTLT (Time To Last Token) - Time between the last sent packet time and the last received token time  (`T_recv[-1] - T_sent[-1]`). The RTT of the last token, also an OK proxy
3. Avg RTT (approximate) - The time between the average sent packet time and the average received packet time  (`T_recv.mean() - T_sent.mean()`). This is a much more stable metric, because like TPOT it averages over all tokens instead of measuring just once per request. However, this is an approximate estimation of the true RTT, because it assumes that the sent packets and received tokens match each other uniformly in time, which is never exactly true.

### Proposed Solution

When the websocket backend is used, report TTLT and Avg RTT in addition to the rest of the metrics. They are always simple to calculate with the websocket backend regardless of modality and endpoint, they provide useful information for all websocket use cases, and they will provide a unique advantage for realtime transcription benchmarking by approximating the experienced system lag.

### Alternatives Considered

We could just accept TTFT as the only proxy, but it's very different from actual system lag in actual streaming applications.

We could also try to measure the true RTT, but that requires having a dataset with accurate timestamp labels, and to use some forced alignment to align predicted tokens with input audio packets, and accommodate for prediction errors, and it requires a different solution for each future websocket modality. It's an overly complicated solution that will create a fragile benchmark that can't generalize to other datasets.

### Usage Examples

```markdown
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

# TTLT & Avg RTT always reported when `backend=openai_realtime_ws`
```

### Additional Context

https://github.com/vllm-project/guidellm/pull/713
https://en.wikipedia.org/wiki/Round-trip_delay

I am interested in creating a PR for this 😄 

## 评论 (4)

### dreamer-89 · 2026-06-23

Hi @AlonKellner-RedHat, thanks for creating this issue. It looks interesting work to me, do you mind if I take this one? I would add the TTLT and Avg RTT to the websocket backend metrics, computed from the sent/received timestamps along with the unit tests. Could you assign it to me?

### AlonKellner-RedHat · 2026-06-24

@dreamer-89 awesome, go for it! but we need @sjmonson or @dbutenhof to assign it to you, I don't have the permissions 😅 

### sjmonson · 2026-06-24

@dreamer-89 Feel free to give it a shot, however the names `TTFT` and `TTLT` shouldn't be used as it conflicts with the definition of those metrics. Maybe `TTFT -> Time To First Round Trip` and `TTLT -> Time To Last Round Trip`.

### AlonKellner-RedHat · 2026-06-25

@sjmonson TTFT is actually the same value as Time To First Round Trip, both are `T_recv[0] - T_sent[0]`, right? Should they still be distinct?

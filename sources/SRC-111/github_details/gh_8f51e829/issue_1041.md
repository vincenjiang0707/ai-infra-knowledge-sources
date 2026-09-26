# [Issue #1041] [Bug]: Concurrency burst does not start all requests together

source: https://github.com/vllm-project/guidellm/issues/1041
state: closed | updated: 2026-08-27T19:53:17Z
labels: 

## 正文

### Bug Description

When `max_concurrency == max_requests` (a simultaneous burst), GuideLLM often does not start all requests together.

The pattern on 2 device servers: 
| Run | Config | Started immediately | Started later |
| --- | --- | --- | --- |
| throughput 50 / 50, 15 workers | M2 Max server | 43–46 | 4–7 |
| concurrent 17 / 17, 10–12 workers | M4 Mini server | 15–16 | 1–2 |

The late requests stay queued in guidellm. They are dequeued only when an earlier request on the same worker finishes. It is problematic because at each run, guidellm shows a different behaviour.

I traced the code, and I realized that guidellm splits `max_concurrency` across worker processes and gives each worker an `asyncio.Semaphore(async_limit)`. However, those workers do not grab request from shared `pending_queue`  only when they have a free slot. A busy worker can own more requests than its capacity. Those extra requests are gone from the shared queue, so idle workers cannot start them. They sit until that same worker finishes an in-flight request. I tracked each request's `scheduler_node_id` in 50 concurrent requests. 

```
worker: async_limit / dequeued_at_t0 / total_held
  0: 4 / 2 / 2   <- 2 idle slots
  3: 4 / 4 / 6   <- 2 more than slots
  4: 4 / 2 / 2   <- 2 idle slots
  6: 3 / 3 / 5   <- 2 more than slots
```

`GUIDELLM__MAX_WORKER_PROCESSES=1` hides the bug because one process cannot steal from another. 


### Expected Behavior

For this: 
```
guidellm run \
  --profile kind=throughput,max_concurrency=50 \
  --constraint kind=max_requests,count=50
```
I expected that all 50 requests would start together.

Each worker should hold at most its `async_limit` requests, so that no request has to wait when there exists free slots. 

### Steps to Reproduce

Any remote OpenAI-compatible server is enough. I started llama.cpp with GPT-OSS 20B.

1. Start a server: 
```
./build/bin/llama-server --host 0.0.0.0 --port 8080 --model gpt-oss-20b-MXFP4.gguf -c 20000 
```
2. Run a 50-request burst with several worker processes:
```
GUIDELLM__MAX_WORKER_PROCESSES=15 guidellm run \
  --backend kind=openai_http,target=http://<target_ip>:8080 \
  --profile kind=throughput,max_concurrency=50 \
  --constraint kind=max_requests,count=50 \
  --data kind=json_file,path=<some_json_data> \
  --output kind=json,path=burst.json
```
3. Compare each request's `info.timings.dequeued` to `scheduler_state.start_time` or `info.timings.targeted_start`.

### Operating System

Ubuntu 25.10

### Python Version

Python 3.12.13

### GuideLLM Version

guidellm version: 0.7.3

### Installation Method

pip install guidellm

### Installation Details

_No response_

### Error Messages or Stack Traces

No specific error message. Only incorrect starting time. 

### Additional Context

<img width="2384" height="2738" alt="Image" src="https://github.com/user-attachments/assets/71db7caf-50b1-45f9-89ed-bcbb15db45e1" />

## 评论 (1)

### himanshu1573 · 2026-08-23

Confirmed this reproduces, and I think it can be reproduced without a real model at all — guidellm's own `mock-server` is enough, which should make it CI-testable.

Setup (Apple Silicon M1, 10 worker processes, `async_limit=5` each):

```bash
guidellm mock-server --port 8010 --model mock-model \
    --request-latency 3.0 --ttft-ms 200 --itl-ms 20 --output-tokens 32

guidellm run \
  --backend "kind=openai_http,target=http://127.0.0.1:8010,model=mock-model" \
  --data "kind=synthetic_text,prompt_tokens=64,output_tokens=32" \
  --tokenizer "kind=hf_auto,model=gpt2" \
  --profile "kind=throughput,max_concurrency=50" \
  --constraint "kind=max_requests,count=50"
```

Results across three identical runs — non-deterministic, as you describe:

```text
run 1: 44/50 started immediately, 6 late
run 2: 46/50 started immediately, 4 late
run 3: 44/50 started immediately, 6 late
```

Peak actual concurrency was 44, not the requested 50.

Control, matching your finding: `GUIDELLM__MAX_WORKER_PROCESSES=1` gives 50/50 started immediately, no late requests.

On causation — every late request started within ~4ms of an earlier request finishing on the *same* worker, and each of those workers had exactly 5 earlier completions (its full `async_limit`):

```text
worker 2: late starts at 1.028s, 1.029s | same-worker finishes at 1.025-1.026s
worker 1: late starts at 1.025s, 1.029s | same-worker finishes at 1.024-1.025s
worker 3: late starts at 1.026s, 1.029s | same-worker finishes at 1.025-1.026s
```

So the late requests are waiting on a slot on the worker that owns them, while other workers are idle — requests received per worker ranged 4 to 7 when an even split would be 5. That matches your read: once a request lands in a worker's queue it can't be picked up by an idle worker.

One incidental thing I hit while measuring: `scheduler_node_id` is set as `self.messaging.worker_index or -1` (`worker.py:332, 348, 441`). Since `0` is falsy, worker 0 is always reported as `-1`. It doesn't cause this bug, but it does corrupt the per-worker telemetry you'd use to diagnose it — worker 0's requests show up under a phantom worker `-1`. Happy to send that as a separate PR.

I'd like to work on this — could I be assigned? Since the mock server reproduces it, I think a regression test can assert that a burst where `max_concurrency == max_requests` starts all requests without waiting on a same-worker completion.


# [Issue #1152] Ensure requests are forcefully killed a certain amount of time after benchmark completes.

source: https://github.com/vllm-project/guidellm/issues/1152
state: open | updated: 2026-09-25T15:47:38Z
labels: invalid, internal, needs followup

## 正文

### Bug Description

If a server acts improperly and does not close connections at the end of cancelled requests it can result in a stall at the end of each benchmark as GuideLLM waits for final status.

### Expected Behavior

GuideLLM should forcefully close request a certain amount of time after it cancels them.

### Steps to Reproduce

TODO

### Operating System

Any

### Python Version

Any

### GuideLLM Version

main

### Installation Method

Official Container Image (Docker)

### Installation Details

_No response_

### Error Messages or Stack Traces

```shell

```

### Additional Context

_No response_

## 评论 (2)

### tosokin · 2026-09-22

Adding more context to the issue:

## System Information

- **GuideLLM Version**: v0.7.3 and nightly build
- **Installation Method**: Official Container Image (Docker) - `ghcr.io/vllm-project/guidellm:v0.7.3`
- **Operating System**: OpenShift/Kubernetes environment
- **System Under Test**: llm-d router (standalone mode)
- **Backend**: [llm-d-inference-sim](https://github.com/llm-d/llm-d-inference-sim) (mock server)

## Bug Description

When benchmarking with GuideLLM using a constant profile and multiple rate values, the benchmark gets stuck between rate tests and never completes. The job continues to run with CPU usage around 2 cores, but no progress is made. This results in no summary report being generated.

### Detailed Symptoms

1. The benchmark successfully completes the first 2-3 rate tests (e.g., rates 5, 10, 20 from the list [5, 10, 20, 30, 40, 50, 60])
2. After completing a rate test GuideLLM stalls and becomes unresponsive
3. After approximately 20+ minutes, it may resume and complete one more rate test, then stall again
4. The job and pod continue running but make no further progress
5. CPU usage stays at ~2 cores but nothing is happening

## Steps to Reproduce

### Environment Setup

**Cluster**: Bare-metal OpenShift

**Hardware**: Dell R740XD-CL-G nodes

**Node Pinning** (anti-affinity to avoid resource contention):
- EPP + Envoy: dedicated node with label `role=epp`
- GuideLLM: dedicated node with label `role=loadgen`
- Inference Simulator (4 replicas): dedicated node with label `role=simulator`

### Prerequisites

Install the Gateway API Inference Extension CRD (required by EPP):
```bash
oc apply -f https://github.com/kubernetes-sigs/gateway-api-inference-extension/releases/latest/download/v1-manifests.yaml
```

### Component Deployment

#### 1. Deploy EPP + Envoy (Helm, standalone mode)

```bash
helm install optimized-baseline \
  oci://ghcr.io/llm-d/charts/llm-d-router-standalone \
  -f /llm-d/guides/recipes/router/base.values.yaml \
  -f /llm-d/guides/optimized-baseline/router/optimized-baseline.values.yaml \
  -n ${NAMESPACE} \
  --version v0 \
  --set router.nodeSelector.role=epp
```

**Resulting Configuration** (from chart defaults):
- EPP Image: `ghcr.io/llm-d/llm-d-router-endpoint-picker:main`
- Envoy Image: `envoyproxy/envoy:distroless-v1.33.2`
- EPP Resources: CPU request 4, no CPU limit, memory 8Gi/16Gi
- Envoy: concurrency=8, log level warn

#### 2. Deploy Inference Simulator

Deploy 4 replicas of [llm-d-inference-sim](https://github.com/llm-d/llm-d-inference-sim) with key arguments:

```yaml
image: ghcr.io/llm-d/llm-d-inference-sim:v0.11.2
args:
  - --model: Qwen/Qwen3-32B
  - --mode: random
  - --max-num-seqs: 2048
  - --max-model-len: 131072
  - --time-to-first-token: 1ms
  - --inter-token-latency: 10ms
  - --force-dummy-tokenizer
nodeSelector:
  role: simulator
```

#### 3. Run GuideLLM Benchmark

Deploy GuideLLM as a Kubernetes Job with key arguments:

```yaml
image: ghcr.io/vllm-project/guidellm:v0.7.3
args:
  - run
  - --disable-progress
  - --backend: kind=openai_http,target=http://optimized-baseline-epp:80,model=Qwen/Qwen3-32B,timeout=60
  - --tokenizer: kind=huggingface_auto,model=gpt2
  - --data: kind=synthetic_text,prompt_tokens=256,output_tokens=4096
  - --profile: '{"kind":"constant","rate":[5,10,20,30,40,50,60]}'
  - --constraint: kind=max_duration,seconds=120
  - --output: kind=json,path=/results/benchmarks.json
nodeSelector:
  role: loadgen
```

### Reproduce the Stall

1. Deploy all three components as described above
2. Monitor the GuideLLM job logs and EPP/Envoy CPU usage
3. Observe that:
   - First 2-3 rate tests complete (5, 10, 20 QPS)
   - After reaching max_duration (120s), the benchmark stalls
   - Job continues running with ~2 core CPU usage but no progress
   - After 20+ minutes, one more rate might complete, then stalls again
4. Check Envoy logs for "Too many open files" errors
5. The benchmark never completes all rates and never generates a summary report

## Expected Behavior

1. GuideLLM should complete all rate tests in the specified list
2. After `max_duration` (120 seconds) is reached for each rate, GuideLLM should:
   - Gracefully cancel any in-flight requests
   - Wait briefly for connections to close
   - Move to the next rate test regardless of connection state
3. The benchmark should complete and generate a summary report

## Actual Behavior

1. GuideLLM completes the first 2-3 rate tests successfully
2. After reaching `max_duration` for a rate test, GuideLLM stalls waiting for connections to close
3. The benchmark does not progress to the next rate or complete
4. No summary report is generated

### Observed Behavior Details

From the logs, we can see the benchmark stalling pattern:
```
26-09-16 14:55:11|INFO - Benchmark 3 (constant@20.00): active | elapsed=120.1s | successful=2217 errored=0 incomplete=0 | requests/s=19.14 output_tokens/s=78412.57
26-09-16 15:19:40|INFO - Benchmark 3 (constant@20.00): completed | elapsed=1589.4s | successful=2299 errored=0 incomplete=102 | requests/s=19.16 output_tokens/s=78472.53
26-09-16 15:19:40|INFO - Starting benchmark for strategy: constant@30.00
26-09-16 15:19:40|INFO - Benchmark 4 (constant@30.00): started | elapsed=0.0s | successful=0 errored=0 incomplete=0 | requests/s=0.00 output_tokens/s=0.00
[STALL - no further progress]
```

Notice that Benchmark 3 took **1589.4 seconds** (26+ minutes) instead of the expected 120 seconds, with 102 incomplete requests at the end.

## Attempted Workarounds

### 1. Adding Backend Timeout (Partially Effective)

Tried adding a timeout parameter to the backend configuration:
```bash
--backend <backend-url>,timeout=60
```

**Result**: Did not resolve the issue. The benchmark still stalled.

### 2. Using Nightly Build (No Change)

Tested with the latest nightly build.

**Result**: Same behavior - benchmark still stalls.

### 3. Killing the Backend Server (Confirmed Root Cause)

When manually stopping the backend server while GuideLLM was stalled:
- The stalled benchmark immediately completed
- The next benchmark in the sequence started
- The new benchmark immediately crashed (expected, as the server was gone)

**Conclusion**: This confirms that GuideLLM is waiting indefinitely for the backend to close connections.

## Root Cause Analysis

1. **GuideLLM waits indefinitely for connections to close** after cancelling requests at the end of a benchmark run
2. When the backend is saturated or slow to respond to cancellations, connections remain open
3. This causes GuideLLM to stall between benchmark rates
4. The open connections accumulate, eventually exhausting file descriptors on the proxy (Envoy)
5. The `max_duration` parameter only controls when GuideLLM stops sending new requests, not when it forcefully closes existing connections

## Additional Context

### Reproducibility
This issue is **consistently reproducible** - observed multiple times across different test runs with various rate configurations.

### Impact
- Cannot complete full benchmark runs with multiple rate tests
- Prevents proper performance evaluation of the system under load
- Workarounds (killing backend, raising FD limits) are not viable for production testing

### himanshu1573 · 2026-09-25

Hi, I tried to reproduce this on current main (`7f06bd31`) and would like to work on the fix.

**What I tested.** I used a small mock server that streams slowly, so every request was still running at the `max_duration` cutoff. I tried several bad server behaviors:

| Server behavior | Stalled? |
|---|---|
| normal slow stream | no |
| keeps its side of the socket open after guidellm disconnects | no |
| sends one token, then goes silent forever | no |
| accepts the request but never sends headers | no |
| 600 streams open at the cutoff | no, all sockets closed within 2 s |
| 3-rate constant sweep `[10,30,60]` | no, all rates finished |

So with a direct HTTP/1.1 connection, guidellm cancels and closes requests quickly. The difference in the report above is Envoy in the path, running out of file descriptors.

**Where it can hang.** After the cutoff, the worker waits for all in-flight requests with no time limit (`asyncio.gather(*pending_tasks)` in `_process_requests_loop`). If even one request does not finish after it is cancelled, that worker never reaches `_cancel_requests_loop`. Its queued requests then never get a final status, and the main process waits forever for `processed == created`. This could explain why the 102 incomplete requests only showed up at the very end.

**Proposed fix**, matching the issue: after cancelling, wait up to a grace period. Then mark the remaining requests as cancelled and move on. I would add a unit test with a backend that ignores cancellation, so the stall is proven without a real server.

@sjmonson two questions before I start:
1. Should the grace period be a setting (for example in `settings`), or a fixed value?
2. Is the worker the right place for it, or would you rather have it in `WorkerProcessGroup`?

@tosokin if you can hit the stall again, could you run `py-spy dump --pid <pid>` on the stuck guidellm processes (main and workers)? It shows the exact line each one is waiting on, so we can confirm the fix covers your case.


source: https://docs.nvidia.com/dynamo/zh-CN/dev/recipes/gemma-4-31b
lastmod: 2026-09-24T19:58:16.636Z

Gemma-4-31B


Gemma-4-31B

Serve Gemma-4-31B with Dynamo and TensorRT-LLM on B200, GB200, or H200 for long-context agentic workloads.

Each target below is a Dynamo + TensorRT-LLM deployment of Gemma-4-31B for multimodal, reasoning, and tool-calling workloads.

B200 and GB200 serve the NVFP4 checkpoint with FP8 KV cache and MTP speculative decoding, while H200 serves the BF16 checkpoint. All targets use KV-aware routing and CPU KV-cache offload.

Pick your GPU architecture; every command on this page updates to match.

Choose your deployment target

**Checkpoint**nvidia/Gemma-4-31B-IT-NVFP4 + google/gemma-4-31B-it-assistant

**Precision**NVFP4 weights + FP8 KV cache

**GPUs**8x B200: 8 TP1 workers

**Parallelism**TP1 per worker, 8 replicas

**Routing**KV-aware

**Checkpoint**nvidia/Gemma-4-31B-IT-NVFP4 + google/gemma-4-31B-it-assistant

**Precision**NVFP4 weights + FP8 KV cache

**GPUs**8x GB200: 8 TP1 workers

**Parallelism**TP1 per worker, 8 replicas

**Routing**KV-aware

**Checkpoint**google/gemma-4-31B-it

**Precision**BF16 weights + 16-bit KV cache

**GPUs**8x H200: 2 TP4 workers

**Parallelism**TP4 per worker, 2 replicas

**Routing**KV-aware

## Prerequisites

- An image-pull secret when required by the cluster. Replace
`your-image-pull-secret`

in the deployment manifest with the local secret name.

- A Kubernetes cluster with the Dynamo platform installed and 8x B200 GPUs available. See the
[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - A Hugging Face token with access to
`nvidia/Gemma-4-31B-IT-NVFP4`

and`google/gemma-4-31B-it-assistant`

for multi-token prediction (MTP).

- A Kubernetes cluster with the Dynamo platform installed and 8x GB200 GPUs available. See the
[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - A Hugging Face token with access to
`nvidia/Gemma-4-31B-IT-NVFP4`

and`google/gemma-4-31B-it-assistant`

for multi-token prediction (MTP).

- A Kubernetes cluster with the Dynamo platform installed and 8x H200 GPUs available. See the
[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - A Hugging Face token with access to
`google/gemma-4-31B-it`

.

## Deploy

### 1. Create namespace and secret

### 2. Create storage

Edit `recipes/gemma4-31b/model-cache/model-cache.yaml`

and set `storageClassName`

to a ReadWriteMany storage class available on the target cluster.

If the cluster already provides a shared ReadWriteMany model-cache persistent volume claim (PVC), skip creating `shared-model-cache`

and replace `claimName: shared-model-cache`

in the download, deploy, and performance manifests with the existing claim name.

### 3. Download the model

Edit `recipes/gemma4-31b/model-cache/model-download.yaml`

before creating the Job. The B200 and GB200 downloads are enabled by default. For H200, comment out those commands and uncomment `hf download google/gemma-4-31B-it`

. Download every checkpoint referenced by the selected deploy manifest.

### 4. Deploy the DGD

## Smoke Test

Send a test request to verify the deployment serves traffic. First forward the frontend port for your target:

Then send a chat completion using the model name for your target:

## Benchmark

A single AIPerf trace-replay Job, `perf/perf.yaml`

, covers all three DGDs. It replays a 3,541-request subset of a Mooncake-format agentic trace with a median 64K input sequence length (ISL), median 400-token output sequence length (OSL), and approximately 90% KV-cache reuse. This long-context workload exercises KV-aware routing and CPU KV-cache offload under repeated prefixes. The benchmark pod is co-located with a DGD frontend through `podAffinity`

.

Edit the `env`

block in `perf/perf.yaml`

to target your deployed DGD. Set `ENDPOINT`

, `TARGET_MODEL`

, and `CONCURRENCY`

from the table below, and set the `podAffinity`

value to the matching DGD name. The concurrency values reproduce the [Expected Performance](https://docs.nvidia.com/dynamo/dev/recipes/gemma-4-31b#expected-performance) numbers.

### Targeting a Variant

All targets use `/model-cache/traces/64k_400_90kv_agent_new_noschedule_short_15perc.jsonl`

as `TRACE_FILE`

.

### Dataset

The Job passes the trace to AIPerf with `--custom-dataset-type mooncake_trace`

. All targets use `/model-cache/traces/64k_400_90kv_agent_new_noschedule_short_15perc.jsonl`

; its SHA-256 is `f20d3f2bc83dd1306cda659fbe34e7c4d85ca5497626c98bc0b1c4d2211379d0`

.

### Stage the trace

Before creating the benchmark Job, materialize the trace and copy it to the `shared-model-cache`

PVC. The Job exits before AIPerf starts when `TRACE_FILE`

is absent. Keep `pvc-helper`

running to fetch the benchmark artifacts after the run.

### Run the benchmark

Then run the Job:

For concurrency sweeps and fetching artifacts, see the [benchmark README](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gemma4-31b/perf/README.md).

## Expected Performance

Measured on the 15% agentic trace subset. System throughput is per-GPU output tokens per second; user throughput is the P50 per-request output rate. The row for your selected GPU is highlighted:

## Compare All Targets

The B200 and GB200 targets serve the model on TensorRT-LLM with KV-aware routing and EAGLE-style MTP speculative decoding (draft length 3, acceptance length of 2.88). The column for your selected GPU is highlighted:

## Limitations

- MTP support has not been verified on H200 and is not enabled in the H200 deployment.
- Audio is not supported by the model.
- For streaming responses with multimodal inputs, the HTTP status code can be misreported. Newer Dynamo versions fix this by setting
`DYN_HTTP_PRE_COMMIT_ERROR_PEEK_MS`

, for example to`500`

. - Some video codecs, including AV1, are not included in the runtime image. Extend the image when those codecs are required.
`media_io_kwargs`

applies only when frontend decoding is enabled. When frontend decoding is disabled, the frameworks do not receive it correctly.- Multimodal items support public URLs only.
`reasoning_effort`

only enables or disables reasoning because the Gemma-4-31B chat template does not support finer levels.- On the MTP-enabled B200 and GB200 variants, one-model speculative decoding does not support
`min_p`

or`min_tokens`

; it rejects`frequency_penalty`

,`presence_penalty`

, and`repetition_penalty`

. Greedy decoding (`temperature=0`

) also rejects`n > 1`

and`best_of > 1`

. - This recipe supports only chat-type endpoints:
`/v1/chat/completions`

and`/v1/responses`

.

## Source

- Source READMEs:
[Gemma-4-31B recipe](https://github.com/ai-dynamo/dynamo/tree/main/recipes/gemma4-31b/)and[benchmark workflow](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gemma4-31b/perf/README.md) - Deploy manifests:
[B200](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gemma4-31b/trtllm/agg-b200-agentic/deploy.yaml),[GB200](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gemma4-31b/trtllm/agg-gb200-agentic/deploy.yaml), and[H200](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gemma4-31b/trtllm/agg-h200-agentic/deploy.yaml) - Benchmark manifest:
[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gemma4-31b/perf/perf.yaml) - Setup assets:
[model-cache.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gemma4-31b/model-cache/model-cache.yaml)and[model-download.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gemma4-31b/model-cache/model-download.yaml)
source: https://docs.nvidia.com/dynamo/zh-CN/dev/recipes/gpt-oss-120b
lastmod: 2026-09-24T19:58:16.636Z

GPT-OSS-120B


GPT-OSS-120B

Serve openai/gpt-oss-120b with Dynamo on vLLM (B200/H200) or TensorRT-LLM (GB200), aggregated or disaggregated.

Validated deployment targets for `openai/gpt-oss-120b`

(MXFP4 MoE, 128 experts, top-4) across two runtimes. The vLLM targets serve the Mooncake agentic trace (64K ISL / 400 OSL, 90% KV cache hit) on B200 or H200, aggregated or disaggregated, with KV-aware routing and EAGLE3 speculative decoding. The TensorRT-LLM targets cover short-prompt high-concurrency and long-context generation on GB200. The GPU choice selects the runtime — B200/H200 run vLLM, GB200 runs TensorRT-LLM — and the targets use different traffic shapes, so this page is not a backend benchmark. Pick your GPU and topology; every command on this page updates to match.

Choose your deployment target

**Checkpoint**openai/gpt-oss-120b

**Runtime**vLLM · MXFP4 + FP8 KV cache

**GPUs**8x B200, 8x TP1 replicas

**Techniques**KV-aware routing, EAGLE3-v3, flashinfer_trtllm MoE

**Workload**Agentic (64K ISL / 400 OSL, 90% KV hit)

**Checkpoint**openai/gpt-oss-120b

**Runtime**vLLM · MXFP4 + FP8 KV cache

**GPUs**8x B200, 2 prefill + 6 decode (in-pod)

**Techniques**KV-aware routing, EAGLE3-v3, flashinfer_trtllm MoE

**Workload**Agentic (64K ISL / 400 OSL, 90% KV hit)

**Checkpoint**openai/gpt-oss-120b

**Runtime**vLLM · MXFP4 + FP8 KV cache

**GPUs**8x H200, 8x TP1 replicas

**Techniques**KV-aware routing, EAGLE3-v3, SimpleCPUOffload, flashinfer_cutlass MoE

**Workload**Agentic (64K ISL / 400 OSL, 90% KV hit)

**Checkpoint**openai/gpt-oss-120b

**Runtime**vLLM · MXFP4 + FP8 KV cache

**GPUs**8x H200, 4 prefill + 4 decode (in-pod)

**Techniques**KV-aware routing, EAGLE3-v3, flashinfer_cutlass MoE

**Workload**Agentic (64K ISL / 400 OSL, 90% KV hit)

**Checkpoint**openai/gpt-oss-120b

**Runtime**TensorRT-LLM (tensorrtllm-runtime:1.2.1)

**GPUs**4x GB200 (ARM64), TP4, EP4 + attention-DP

**Workload**Short prompts, long outputs, high concurrency (128 ISL / 1000 OSL)

**Checkpoint**openai/gpt-oss-120b

**Runtime**TensorRT-LLM (tensorrtllm-runtime:1.2.1)

**GPUs**5x GB200/B200 (TP1 prefill + TP4 decode)

**Quantization**W4A8_MXFP4_MXFP8

**Workload**Long-context generation (8K ISL / 1K OSL)

## Prerequisites

- A Kubernetes cluster with the Dynamo platform installed and
**8x B200 on a single node**— the disaggregated target co-locates prefill and decode workers in one Pod. - A Hugging Face token with access to
`openai/gpt-oss-120b`

and`nvidia/gpt-oss-120b-Eagle3-v3`

(the EAGLE3 speculative-decoding head).

- A Kubernetes cluster with the Dynamo platform installed and
**8x H200 on a single node**— the disaggregated target co-locates prefill and decode workers in one Pod. - A Hugging Face token with access to
`openai/gpt-oss-120b`

and`nvidia/gpt-oss-120b-Eagle3-v3`

(the EAGLE3 speculative-decoding head).

- A Kubernetes cluster with the Dynamo platform installed and
**4x GB200 available on ARM64 nodes**— the aggregated target will not run on x86 Hopper/Ampere hardware. - A Hugging Face token with access to
`openai/gpt-oss-120b`

.

- A Kubernetes cluster with the Dynamo platform installed and
**5x GB200 or B200**available (1 prefill + 4 decode GPUs). - A Hugging Face token with access to
`openai/gpt-oss-120b`

.

Create the namespace and token secret:

Update `storageClassName`

in `model-cache/model-cache.yaml`

and the container image tag in `deploy.yaml`

to match your Dynamo release before deploying. Also edit namespace, node selectors, and cluster-specific placement.

## Deploy

Prepare the model cache (shared by all targets; the vLLM targets also pull the EAGLE3 head):

Then deploy:

Model loading takes roughly 15-30 minutes depending on storage speed:

## Smoke Test

Send a test request to verify the deployment serves traffic. First forward the frontend port for your target:

The disaggregated target is a single co-located Pod exposed as one Service (no separate frontend):

The disaggregated target is a single co-located Pod exposed as one Service (no separate frontend):

All targets serve `openai/gpt-oss-120b`

:

## Benchmark

A single AIPerf trace-replay Job — `perf/perf.yaml`

— covers every vLLM variant. It replays the Mooncake agentic trace (reused from the Kimi-K2.6 recipe; fetch it with `git lfs pull --include "recipes/kimi-k2.6/perf/traces/*"`

) at one concurrency value and writes artifacts to the shared `model-cache`

PVC. Edit the `env`

block to set `ENDPOINT`

, `TRACE_FILE`

, and `CONCURRENCY`

for your target:

To measure multiple concurrencies, clear server state between runs — otherwise residual KV/prefix-cache hits skew results. See the [benchmark README](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gpt-oss-120b/perf/README.md).

The TensorRT-LLM target ships a `perf.yaml`

Kubernetes Job that runs AIPerf at ISL 128 / OSL 1000 and 900 per GPU x 4 GPUs = 3,600 total concurrency (request count 10x concurrency). The Job wraps this AIPerf run:

The TensorRT-LLM target ships a `perf.yaml`

Kubernetes Job that runs AIPerf at ISL 8192 / OSL 1024 and 1,536 total concurrency (request count 10x concurrency). The Job wraps this AIPerf run:

## Expected Performance

Measured on the agentic 15% trace (8 GPUs) with the synthetic-acceptance EAGLE3 throughput proxy (AL=2.72; use for *relative* comparison — the generated text is intentionally garbage). Per-GPU throughput is system throughput / 8.

The TensorRT-LLM targets ship benchmark Jobs but no published numbers — reproduce them with the [Benchmark](https://docs.nvidia.com/dynamo/dev/recipes/gpt-oss-120b#benchmark) step above.

## Compare All Targets

vLLM targets (agentic Mooncake trace, 8 GPUs, MXFP4 + FP8 KV, EAGLE3-v3, KV-aware routing):

TensorRT-LLM targets (GB200, static synthetic traffic):

## Notes

- Reasoning and tool calling use the gpt-oss “harmony” format, wired with
`--dyn-reasoning-parser gpt_oss --dyn-tool-call-parser harmony`

;`tool_calls`

populates with`finish_reason: tool_calls`

. - The disaggregated targets run
**single-node in-pod**(prefill and decode co-located in one Pod). Multi-pod disaggregation is not supported. - Structured output (
`response_format: json_object`

/`json_schema`

) may return invalid JSON while speculative decoding is enabled — use tool calling or validate client-side. - The H200 aggregated target enables
`SimpleCPUOffload`

(about +9% throughput, quality-neutral); the B200 targets leave it off by default. - Speculative decoding uses the
`nvidia/gpt-oss-120b-Eagle3-v3`

head (EAGLE3-v3, draft length 3).

- The aggregated target requires ARM64 (GB200) nodes; the disaggregated target accepts GB200 or B200.
- Do not read the two TensorRT-LLM targets as an aggregated-vs-disaggregated benchmark; their traffic shapes differ by design.
- The disaggregated deployment uses 5 GPUs (1x TP1 prefill + 1x TP4 decode), while its
`perf.yaml`

computes total concurrency from a 6-GPU count (256 x 6 = 1,536); adjust`DEPLOYMENT_GPU_COUNT`

if you want strict per-GPU normalization. - The disaggregated target uses
`W4A8_MXFP4_MXFP8`

quantization via the`OVERRIDE_QUANT_ALGO`

environment variable, and UCX-based KV transfer (`max_tokens_in_buffer=9216`

).

## Source

- Source README:
[recipes/gpt-oss-120b/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gpt-oss-120b/README.md) - Benchmark README:
[recipes/gpt-oss-120b/perf/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gpt-oss-120b/perf/README.md) - vLLM aggregated:
[B200](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gpt-oss-120b/vllm/agg-b200-agentic/deploy.yaml)and[H200](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gpt-oss-120b/vllm/agg-h200-agentic/deploy.yaml)deploy.yaml - vLLM disaggregated:
[B200](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gpt-oss-120b/vllm/disagg-b200-agentic/deploy.yaml)and[H200](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gpt-oss-120b/vllm/disagg-h200-agentic/deploy.yaml)deploy.yaml - vLLM benchmark manifest:
[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gpt-oss-120b/perf/perf.yaml) - TRT-LLM aggregated:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gpt-oss-120b/trtllm/agg/deploy.yaml)and[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gpt-oss-120b/trtllm/agg/perf.yaml) - TRT-LLM disaggregated:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gpt-oss-120b/trtllm/disagg/deploy.yaml)and[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/gpt-oss-120b/trtllm/disagg/perf.yaml)
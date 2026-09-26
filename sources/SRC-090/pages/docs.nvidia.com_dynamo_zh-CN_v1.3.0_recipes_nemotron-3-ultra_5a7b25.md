source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/recipes/nemotron-3-ultra
lastmod: 2026-09-23T23:30:39.914Z

Nemotron-3-Ultra


Nemotron-3-Ultra

Serve nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4 with Dynamo and vLLM, tuned per GPU and workload.

Each target below is a validated aggregated vLLM deployment of Nemotron-3-Ultra — NVIDIA’s ~550B hybrid Mamba/Attention/MoE model (~55B active) — with MTP speculative decoding (1 token) and KV-aware routing; the B200 agentic target measured 310.8 system output tok/s per GPU on its trace. Pick your GPU and workload; every command on this page updates to match.

Choose your deployment target

**Checkpoint**nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4

**Precision**NVFP4 + FP8

**GPUs**4x B200 per worker, TP4 + EP

**Spec decode**MTP, 1 token

**Routing**KV-aware

**Workload**Chat 8K/1K Moontrace, 70% KV reuse

**Checkpoint**nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4

**Precision**NVFP4 + FP8

**GPUs**4x B200 per worker, TP4 + EP

**Spec decode**MTP, 1 token

**Routing**KV-aware

**Workload**Agentic 64K/400 Moontrace, 90% KV reuse

**Checkpoint**nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4

**Precision**NVFP4 + FP8

**GPUs**8x H200 per worker, TP8 + EP

**Spec decode**MTP, 1 token

**Routing**KV-aware

**Workload**Chat 8K/1K Moontrace, 70% KV reuse

**Checkpoint**nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4

**Precision**NVFP4 + FP8

**GPUs**8x H200 per worker, TP8 + EP

**Spec decode**MTP, 1 token

**Routing**KV-aware

**Workload**Agentic 64K/400 Moontrace, 90% KV reuse

## Prerequisites

- A Kubernetes cluster with the Dynamo Platform installed (DGD CRDs served) and
**4x B200 per aggregated worker**available (8x B200 for the disaggregated fallback). - An NGC image pull secret named
`nvcr-secret`

for`nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.3.0-nemotron-ultra-dev.1`

. - A Hugging Face token with access to
`nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4`

. - A
`shared-model-cache`

PVC containing the tokenizer-patched Ultra model view, or permission to create and populate it with the manifests in`model-cache/`

(~1200 Gi).

- A Kubernetes cluster with the Dynamo Platform installed (DGD CRDs served) and
**8x H200 per worker**available. - An NGC image pull secret named
`nvcr-secret`

for`nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.3.0-nemotron-ultra-dev.1`

. - A Hugging Face token with access to
`nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4`

. - A
`shared-model-cache`

PVC containing the tokenizer-patched Ultra model view, or permission to create and populate it with the manifests in`model-cache/`

(~1200 Gi).

Create the namespace and token secret:

Edit namespace, storage class, image tags, node selectors, and cluster-specific placement in the manifests before applying them.

## Deploy

Create and populate the model cache, then validate the patched model view before deploying any server:

Then deploy:

### Alternate topology: disaggregated fallback (1P1D, no MTP)

A disaggregated B200 agentic fallback splits prefill and decode into separate TP4 workers (8x B200 total: 4 prefill + 4 decode) with KV-aware routing plus P/D transfer, and runs without MTP. Its frontend service is `ultra-disagg-b200-1p1d-agentic-nomtp-frontend`

; benchmark it by retargeting the same perf Job at that endpoint with the agentic trace at concurrency 32:

Measured on the 15% agentic trace at concurrency 32: **61.6 user output tok/s** and **231.1 system output tok/s/GPU** (also listed in the performance table below).

## Smoke Test

Send a test request to verify the deployment serves traffic:

## Benchmark

A single AIPerf trace-replay Job ([ perf/perf.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/nemotron-3-ultra/perf/perf.yaml)) covers every target — only

`ENDPOINT`

, `TRACE_FILE`

, and `CONCURRENCY`

change in its env block. First stage the bundled Moontrace files from [onto the](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/recipes/nemotron-3-ultra/perf/traces)

`recipes/nemotron-3-ultra/perf/traces/`

`shared-model-cache`

PVC:Set `ENDPOINT`

to `ultra-agg-b200-chat-mtp-frontend:8000`

(the Job default) with the chat trace at concurrency 18, then apply. The Job wraps this AIPerf raw Moontrace replay:

Set `ENDPOINT`

to `ultra-agg-b200-agentic-mtp-frontend:8000`

with the agentic trace at concurrency 20, then apply. The Job wraps this AIPerf raw Moontrace replay:

For the disaggregated fallback, point `ENDPOINT`

at `ultra-disagg-b200-1p1d-agentic-nomtp-frontend:8000`

with the same agentic trace at concurrency 32.

Set `ENDPOINT`

to `ultra-agg-h200-chat-mtp-frontend:8000`

with the chat trace at concurrency 10, then apply. The Job wraps this AIPerf raw Moontrace replay:

Set `ENDPOINT`

to `ultra-agg-h200-agentic-mtp-frontend:8000`

with the agentic trace at concurrency 8, then apply. The Job wraps this AIPerf raw Moontrace replay:

Artifacts land on the PVC under `/opt/models/perf/<epoch>_ultra-bench/`

. 15% and 30% prefix-slice traces are provided for shorter runs. For concurrency sweeps, delete the worker pods between runs so residual KV/prefix-cache state does not skew results — see the [benchmark README](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/nemotron-3-ultra/perf/README.md) for the full workflow, artifact layout, and tunable environment variables.

## Expected Performance

Each target is tuned for its workload shape:

B200 rows use 15% raw Moontrace replay with `raw_direct_no_filter`

trace semantics; H200 rows use 300-sample replay evidence. `User output tok/s`

is Gen TPS/user p50 from AIPerf; `System output tok/s/GPU`

is TPS/GPU. Your selected target’s rows are highlighted:

Treat each row together with its matching recipe, image, trace, and server-shape artifacts.

## Compare All Targets

All targets serve `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4`

on the dedicated dev runtime image `vllm-runtime:1.3.0-nemotron-ultra-dev.1`

with KV-aware routing and a 262144 max model length:

## Notes

- This is a Day-0 recipe on a dedicated dev runtime image (
`vllm-runtime:1.3.0-nemotron-ultra-dev.1`

); it is functional and benchmarked but not yet promoted to a release runtime image. - The recipes pin
`VLLM_DISABLED_KERNELS=FlashInferFP8ScaledMMLinearKernel`

and pass`--no-enable-flashinfer-autotune`

on vLLM workers. Do not remove these unless rerunning the benchmark qualification — they select the non-FlashInfer FP8 linear kernel path and avoid a measured vLLM 0.22 FlashInfer FP8 regression. - No-MTP fallback manifests are included for every aggregated target at
`vllm/agg-<sku>-<usecase>-nomtp/deploy.yaml`

; their DGD names carry the`-nomtp`

suffix, and their measured rows appear in the performance table above. - Reasoning is controlled per request via
`chat_template_kwargs`

(`enable_thinking`

,`force_nonempty_content`

) and`nvext.max_thinking_tokens`

. Do not send`force_nonempty_content`

as a top-level request parameter. Top-level reasoning controls such as`include_reasoning`

and`reasoning_effort`

are part of shared Dynamo API compatibility work, not Ultra-specific failures. - Raw Moontrace replay may contain over-context or pathological long-generation rows. Preserve them as HTTP/error evidence rather than dropping them silently.
- Tool calling uses the
`qwen3_coder`

parser; reasoning parsing uses the model-local`ultra_v3_reasoning_parser.py`

(validated by the model-validate Job).

## Source

- Source README:
[recipes/nemotron-3-ultra/README.md](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/nemotron-3-ultra/README.md) - Benchmark workflow:
[recipes/nemotron-3-ultra/perf/README.md](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/nemotron-3-ultra/perf/README.md)and[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/nemotron-3-ultra/perf/perf.yaml) - B200 chat + MTP:
[vllm/agg-b200-chat-mtp/deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/nemotron-3-ultra/vllm/agg-b200-chat-mtp/deploy.yaml) - B200 agentic + MTP:
[vllm/agg-b200-agentic-mtp/deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/nemotron-3-ultra/vllm/agg-b200-agentic-mtp/deploy.yaml) - H200 chat + MTP:
[vllm/agg-h200-chat-mtp/deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/nemotron-3-ultra/vllm/agg-h200-chat-mtp/deploy.yaml) - H200 agentic + MTP:
[vllm/agg-h200-agentic-mtp/deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/nemotron-3-ultra/vllm/agg-h200-agentic-mtp/deploy.yaml) - B200 disaggregated agentic:
[vllm/disagg-b200-agentic/deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/nemotron-3-ultra/vllm/disagg-b200-agentic/deploy.yaml) - No-MTP fallbacks:
[vllm/](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/recipes/nemotron-3-ultra/vllm)(`agg-*-nomtp/deploy.yaml`

) - Model cache setup:
[model-cache/](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/recipes/nemotron-3-ultra/model-cache)(`model-cache.yaml`

,`model-download.yaml`

,`model-validate.yaml`

)
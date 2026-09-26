source: https://docs.nvidia.com/dynamo/zh-CN/dev/recipes/qwen3-6-35b-a3b
lastmod: 2026-09-24T19:58:16.636Z

Qwen3.6-35B-A3B


Qwen3.6-35B-A3B

Serve Qwen3.6-35B-A3B with Dynamo on B200, GB200, or H200.

These aggregated recipes serve the agentic workload with `nvidia/Qwen3.6-35B-A3B-NVFP4`

on B200 or GB200 and `Qwen/Qwen3.6-35B-A3B-FP8`

on H200.

Choose your deployment target

**Checkpoint**nvidia/Qwen3.6-35B-A3B-NVFP4

**Precision**NVFP4 weights + FP8 KV cache

**GPUs**1x B200

**Runtime**SGLang aggregate worker

**Spec decode**MTP, 3 tokens

**Checkpoint**Qwen/Qwen3.6-35B-A3B-FP8

**Precision**FP8 weights, BF16 KV

**GPUs**1x H200

**Runtime**SGLang aggregate worker

**Spec decode**MTP, 3 tokens

**Checkpoint**nvidia/Qwen3.6-35B-A3B-NVFP4

**Precision**NVFP4 weights + FP8 KV cache

**GPUs**1x GB200

**Runtime**SGLang aggregate worker

**Spec decode**MTP, 3 tokens

## Prerequisites

- A Kubernetes cluster with the Dynamo platform and DGD CRDs installed.
- A namespace with access to the selected GPU target.
- A ReadWriteMany
`model-cache`

PVC. Set`storageClassName`

in the model-cache manifest before deployment.

The checkpoint is downloaded from Hugging Face by the selected model-download Job. Add a Hugging Face token only if your environment requires authenticated access.

Edit namespace, storage class, image tags, node selectors, resource claims, and cluster-specific placement in the manifests before applying them.

## Deploy

Create the model cache and download the selected checkpoint:

Deploy the selected target:

## Smoke Test

Forward the frontend service and verify the model:

Send a chat request:

Forward the frontend service and verify the model:

Send a chat request:

Qwen3.6 also accepts image input. Send an `image_url`

content part:

## Benchmark

These results use [AIPerf](https://github.com/ai-dynamo/aiperf) 0.10.0 and the
[ 64k_400_90kv_agent_new_noschedule_short_15perc.jsonl](https://github.com/ai-dynamo/dynamo/blob/main/recipes/kimi-k2.6/perf/traces/64k_400_90kv_agent_new_noschedule_short_15perc.jsonl)
trace. The workload uses 64K input tokens, 400 output tokens, 90% KV reuse,
concurrency 32, and 3,541 trace requests. The trace contains 131 requests
expected to exceed the model context length and fail.
You can fetch the Git LFS-backed trace before running the benchmark:

All measurements use one GPU.

Run one separate 32-request pass using the same trace and options before the measured phase for warmup.

The MTP results use three speculative tokens with a synthetic acceptance length of 3.3153. This value was calculated for the coding workload in SpeedBench. The full trace produced 131 expected context-length errors.

When benchmarking with synthetic acceptance, uncomment the `SGLANG_SIMULATE_ACC_*`

variables in the manifest. `SGLANG_SIMULATE_ACC_TOKEN_MODE`

must be
`real-draft-token`

: with the default fixed fake token id SGLang emits id 100, which
is not a valid token in the Qwen tokenizer, so the frontend drops the response and
inter-token latency reports 0.

When benchmarking SGLang with synthetic acceptance, set
`SGLANG_SIMULATE_ACC_TOKEN_MODE=real-draft-token`

together with
`SGLANG_SIMULATE_ACC_LEN`

and `SGLANG_SIMULATE_ACC_METHOD`

. SGLang 0.5.16 uses
fixed token ID 100 when the token mode is omitted. That token decodes to the
Unicode replacement character for the Qwen tokenizer, so Dynamo buffers the
generated text until the response finishes and AIPerf cannot calculate
inter-token latency or output throughput per user.

## Expected Performance

Measured with 64K input tokens, 400 output tokens, and 90% KV reuse at concurrency 32
with 3,541 trace requests. MTP runs with simulated acceptance, `acc_len=3.3153`

from
SpeedBench coding, not acceptance measured on this agentic trace. The 32-request warmup
is a separate pass and is not included in these figures:

## Expected Accuracy

GPQA Diamond (`gpqa_diamond_aa_v3`

) via NVIDIA Eval Factory
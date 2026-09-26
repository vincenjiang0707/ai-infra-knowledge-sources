source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/recipes/llama-3-3-70b
lastmod: 2026-09-23T23:30:39.914Z

Llama-3.3-70B FP8


Llama-3.3-70B FP8

Serve Llama-3.3-70B FP8 with Dynamo and vLLM, sized from one node to two.

Three validated vLLM topologies for `RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic`

— aggregated TP4, single-node prefill/decode split, and two-node prefill/decode — all benchmarked with the same 8K ISL / 1K OSL traffic at 16 concurrency per GPU so you can compare normalized TPS/GPU across footprints. Pick your topology; every command on this page updates to match.

Choose your deployment target

**Checkpoint**RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic

**Precision**FP8 dynamic

**GPUs**4x H100/H200, one TP4 worker

**Techniques**Aggregated serving

**Workload**8K ISL / 1K OSL, 64 concurrency

**Checkpoint**RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic

**Precision**FP8 dynamic

**GPUs**8x H100/H200: 2x TP2 prefill + 1x TP4 decode

**Techniques**Disaggregated P/D over NIXL

**Workload**8K ISL / 1K OSL, 128 concurrency

**Checkpoint**RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic

**Precision**FP8 dynamic

**GPUs**16x H100/H200: 1x TP8 prefill + 1x TP8 decode

**Techniques**Disaggregated P/D over NIXL

**Workload**8K ISL / 1K OSL, 256 concurrency

## Prerequisites

- A Kubernetes cluster with the Dynamo platform installed and
**4x H100 or H200**available on one node.

- A Kubernetes cluster with the Dynamo platform installed and
**8x H100 or H200**available on one node.

- A Kubernetes cluster with the Dynamo platform installed and
**16x H100 or H200**available across two nodes.

- A Hugging Face token with access to
`RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic`

.

Create the namespace and token secret:

Update `storageClassName`

in `model-cache/model-cache.yaml`

to match your cluster, and edit namespace, image tags, node selectors, and Hugging Face secrets before applying these manifests. Model download takes approximately 15-30 minutes depending on network speed.

## Deploy

Prepare the model cache and download the checkpoint (shared by all three targets):

Then deploy:

## Smoke Test

Send a test request to verify the deployment serves traffic:

## Benchmark

Each target ships a `perf.yaml`

Kubernetes Job that waits for the model to come up, then runs AIPerf with the same traffic shape: ISL=8192, OSL=1024, 16 concurrency per GPU (so total concurrency scales with the target’s GPU count), and a request count of 10x total concurrency.

The Job wraps this AIPerf run (64 concurrency, 640 requests):

The Job wraps this AIPerf run (128 concurrency, 1,280 requests):

The Job wraps this AIPerf run (256 concurrency, 2,560 requests):

## Compare All Targets

All three targets serve `RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic`

on the vLLM runtime (`nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.2.1`

) and are benchmarked at 16 concurrency per GPU with 8K ISL / 1K OSL traffic:

## Related Feature Benchmarks

[Llama-3.3-70B topology benchmark](https://docs.nvidia.com/dynamo/v1.3.0/benchmarks/llama-3-70b-topology)— how the three topologies compare when normalized by GPU.

## Notes

- FP8 dynamic quantization is applied at runtime; the served model is
`RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic`

. - GPU counts differ by target (4 / 8 / 16), so compare total throughput and TPS/GPU — the topology comparison lives on the related Feature Benchmarks page.
- A GAIE (Gateway API Inference Extension) integration example is included: apply the manifests under
[vllm/agg/gaie/](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/recipes/llama-3-70b/vllm/agg/gaie)(or[vllm/disagg-single-node/gaie/](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/recipes/llama-3-70b/vllm/disagg-single-node/gaie)) to front the deployment with an inference gateway. These are integration artifacts, not separate recipe targets.

## Source

- Source README:
[recipes/llama-3-70b/README.md](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/llama-3-70b/README.md) - vLLM aggregated:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/llama-3-70b/vllm/agg/deploy.yaml)and[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/llama-3-70b/vllm/agg/perf.yaml) - vLLM disagg single-node:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/llama-3-70b/vllm/disagg-single-node/deploy.yaml)and[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/llama-3-70b/vllm/disagg-single-node/perf.yaml) - vLLM disagg multi-node:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/llama-3-70b/vllm/disagg-multi-node/deploy.yaml)and[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/llama-3-70b/vllm/disagg-multi-node/perf.yaml) - GAIE integration:
[vllm/agg/gaie/](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/recipes/llama-3-70b/vllm/agg/gaie) - Setup assets:
[recipes/llama-3-70b/model-cache/model-cache.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/llama-3-70b/model-cache/model-cache.yaml)and[recipes/llama-3-70b/model-cache/model-download.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/llama-3-70b/model-cache/model-download.yaml)
source: https://docs.nvidia.com/dynamo/recipes/nemotron-3-5-lightning
lastmod: 2026-09-24T19:58:16.636Z

# Nemotron 3.5 Lightning

Serve NVIDIA-Nemotron-3.5-Lightning-30B-A3B in NVFP4 or BF16 with Dynamo, vLLM, and experimental TensorRT-LLM targets.

This recipe deploys the NVFP4 or BF16 variant of `NVIDIA-Nemotron-3.5-Lightning-30B-A3B`

, a 30B hybrid Mamba/Attention/MoE model with about 3B active parameters per token. The vLLM targets cover H100, H200, B200, and GB200 with MTP, DFlash, or DSpark speculative decoding. The benchmark tables use a Mooncake-format agentic trace with 64K input tokens, 400 output tokens, and 90% KV reuse.

Choose your deployment target

**Checkpoint**nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16

**Precision**BF16

**GPUs**1x B200, or 4x B200 with KV routing

**Runtime**vLLM aggregate worker

**Spec decode**DSpark or MTP

**Checkpoint**nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4

**Precision**NVFP4 (W4A16)

**GPUs**1x H100, or 4x H100 with KV routing

**Runtime**vLLM aggregate worker

**Spec decode**DSpark, DFlash, or MTP

**Checkpoint**nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4

**Precision**NVFP4 (W4A16)

**GPUs**1x H200, or 4x H200 with KV routing

**Runtime**vLLM aggregate worker

**Spec decode**DSpark, DFlash, or MTP

**Checkpoint**nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16

**Precision**BF16

**GPUs**1x GB200

**Runtime**vLLM, aggregate worker

**Spec decode**DSpark or MTP

**Checkpoint**nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16

**Precision**BF16

**GPUs**2x B200

**Runtime**vLLM, 1 prefill + 1 decode

**Transport**IB/RDMA with UCX

**Spec decode**DSpark

**Checkpoint**nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4

**Precision**NVFP4 (W4A16)

**GPUs**2x H100

**Runtime**vLLM, 1 prefill + 1 decode

**Transport**AWS EFA/LIBFABRIC

**Spec decode**DFlash or DSpark

**Checkpoint**nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4

**Precision**NVFP4 (W4A16)

**GPUs**2x H200

**Runtime**vLLM, 1 prefill + 1 decode

**Transport**IB/RDMA with UCX

**Spec decode**DFlash or DSpark

**Checkpoint**nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16

**Precision**BF16

**GPUs**2x GB200

**Runtime**vLLM, 1 prefill + 1 decode

**Transport**UCX/NIXL with cluster-specific fabric resources

**Spec decode**DFlash or DSpark

**Checkpoint**nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16

**Precision**BF16

**GPUs**1x B200

**Runtime**TensorRT-LLM, aggregate worker

**Spec decode**MTP or no-spec fallback

**Status**Experimental

**Checkpoint**nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4

**Precision**NVFP4 (W4A16)

**GPUs**1x H100

**Runtime**TensorRT-LLM, aggregate worker

**Spec decode**MTP

**Status**Experimental

**Checkpoint**nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4

**Precision**NVFP4

**GPUs**1x H200

**Runtime**TensorRT-LLM, aggregate worker

**Spec decode**MTP

**Status**Experimental

**Checkpoint**nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16

**Precision**BF16

**GPUs**1x GB200

**Runtime**TensorRT-LLM, aggregate worker

**Spec decode**MTP or no-spec fallback

**Status**Experimental; review-stage

## Prerequisites

- A Kubernetes cluster with the Dynamo Platform installed and DGD CRDs served.
- A namespace with access to the selected GPU target.
- A Hugging Face token with access to the base model and draft models.
- An image pull secret if your cluster requires authenticated image pulls.

- AWS EFA/LIBFABRIC resources exposed as
`vpc.amazonaws.com/efa`

for the H100 disaggregated manifests. - AWS EFA userspace available in the runtime image or installed by your cluster bootstrap flow before pod startup. The manifests do not download or install EFA packages. Use the
[EFA check helper](https://github.com/ai-dynamo/dynamo/blob/main/recipes/nemotron-3.5-lightning/vllm/check-efa-userspace.sh)to validate a prepared image or running pod; its install mode requires a pinned`EFA_INSTALLER_VERSION`

and`EFA_INSTALLER_SHA256`

.

- IB/RDMA resources exposed as
`rdma/ib`

for the H200 and B200 disaggregated manifests.

- GB200 disaggregated manifests leave fabric resources cluster-specific. Add the UCX/NIXL resource claims or network resources required by your platform.

Create the namespace and Hugging Face token secret:

Edit storage class, image pull secret names, node selectors, fabric resources, and cluster-specific placement before applying these manifests.

## Deploy

Create the shared model cache, then download the checkpoints for the selected GPU family:

Then deploy the selected target.

DSpark is the promoted single-worker B200 aggregate path from the checked-in validation table. Use `agg-b200-mtp-bf16`

or `agg-b200-dspark-kv-router-bf16`

to compare the other aggregate options. For this validation trace, KV-aware routing did not materially change the result because KV-cache pressure was low; it can help workloads with enough reusable KV state to pressure a single worker.

DSpark is the highest-throughput H100 single-worker aggregate row in the checked-in validation table. Use `agg-h100-dflash`

, `agg-h100-mtp`

, or `agg-h100-dspark-kv-router`

to compare the other aggregate options. For this validation trace, KV-aware routing did not materially change the result because KV-cache pressure was low; it can help workloads with enough reusable KV state to pressure a single worker.

DSpark is the highest-throughput H200 single-worker aggregate row in the checked-in validation table. Use `agg-h200-dflash`

, `agg-h200-mtp`

, or `agg-h200-dspark-kv-router`

to compare the other aggregate options. For this validation trace, KV-aware routing did not materially change the result because KV-cache pressure was low; it can help workloads with enough reusable KV state to pressure a single worker.

DSpark is the highest-throughput GB200 aggregate row in the checked-in validation table. Use `agg-gb200-mtp-bf16`

for the other passing aggregate row.

Use this target for B200 disaggregated vLLM validation with DSpark speculative decoding.

DSpark is the highest-output-throughput H100 disaggregated row in the source inventory. Use `disagg-h100-dflash`

to compare the other speculative decoding mode.

DSpark is the highest-throughput H200 disaggregated row in the source inventory. Use `disagg-h200-dflash`

to compare the other speculative decoding mode.

The delivered GB200 disaggregated recipes are DSpark and DFlash. The command above deploys DSpark; use `disagg-gb200-dflash-bf16`

for the DFlash recipe.

Use `trtllm/agg-b200-bf16/deploy.yaml`

for the no-spec fallback.

The H100 TensorRT-LLM target uses the MTP manifest.

The H200 TensorRT-LLM target uses the MTP manifest.

Use `trtllm/agg-gb200-bf16/deploy.yaml`

for the no-spec fallback.

## Smoke Test

Port-forward the frontend service for the deployment you applied:

Then send a chat completion request:

## Benchmark

The checked-in recipe includes benchmark results in [ recipes/nemotron-3.5-lightning/perf/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/nemotron-3.5-lightning/perf/README.md). The pass criteria are

`tok/s/user >= 50`

and TTFT p50 under 5 seconds.To reproduce the shape, run AIPerf against the selected frontend with a Mooncake trace replay and the target concurrency from the table.

TensorRT-LLM rows are experimental smoke or inventory results in the source README. Use the same AIPerf shape after replacing the `--url`

and concurrency with the selected TensorRT-LLM row below.

## Expected Performance

## Compare All Targets

## Notes

- H100 disaggregated manifests request
`vpc.amazonaws.com/efa: 4`

; H200 and B200 disaggregated manifests request`rdma/ib: 1`

. Change those resources when your cluster exposes different RDMA devices.

- TensorRT-LLM manifests are experimental in this recipe.

## Source

- Source README:
[recipes/nemotron-3.5-lightning/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/nemotron-3.5-lightning/README.md) - vLLM README:
[recipes/nemotron-3.5-lightning/vllm/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/nemotron-3.5-lightning/vllm/README.md) - EFA check helper:
[recipes/nemotron-3.5-lightning/vllm/check-efa-userspace.sh](https://github.com/ai-dynamo/dynamo/blob/main/recipes/nemotron-3.5-lightning/vllm/check-efa-userspace.sh) - TensorRT-LLM README:
[recipes/nemotron-3.5-lightning/trtllm/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/nemotron-3.5-lightning/trtllm/README.md) - Performance notes:
[recipes/nemotron-3.5-lightning/perf/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/nemotron-3.5-lightning/perf/README.md) - Model cache manifests:
[model-cache](https://github.com/ai-dynamo/dynamo/tree/main/recipes/nemotron-3.5-lightning/model-cache) - BF16 model download:
[model-download-bf16.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/nemotron-3.5-lightning/model-cache/model-download-bf16.yaml)
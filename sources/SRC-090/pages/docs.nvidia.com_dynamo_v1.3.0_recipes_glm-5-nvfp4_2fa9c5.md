source: https://docs.nvidia.com/dynamo/v1.3.0/recipes/glm-5-nvfp4
lastmod: 2026-09-24T19:58:16.636Z

GLM-5 NVFP4


GLM-5 NVFP4

Serve GLM-5 NVFP4 with Dynamo and SGLang, disaggregated across five GB200 nodes.

This recipe serves `nvidia/GLM-5-NVFP4`

with disaggregated prefill/decode and EAGLE MTP speculative decoding across 5 nodes of 4x GB200 (TP4 prefill, TP16/DP16/EP16 decode), sustaining roughly 16.8K output tokens/sec on the standard UCX path (19K with the AWS EFA variant) at 512-way concurrency on a 1K ISL / 8K OSL long-output workload. Pick your KV-transfer path; every command on this page updates to match.

Choose your deployment target

**Checkpoint**nvidia/GLM-5-NVFP4

**Precision**NVFP4 + FP8 KV cache

**GPUs**20x GB200, 5 nodes of 4

**Parallelism**TP4 prefill, TP16/DP16/EP16 decode

**KV transfer**NIXL over UCX

**Workload**1K ISL / 8K OSL, 512 concurrency

**Checkpoint**nvidia/GLM-5-NVFP4

**Precision**NVFP4 + FP8 KV cache

**GPUs**20x GB200, 5x p6e-gb200.36xlarge

**Parallelism**TP4 prefill, TP16/DP16/EP16 decode

**KV transfer**NIXL LIBFABRIC over EFA RDMA

**Workload**1K ISL / 8K OSL, 512 concurrency

## Prerequisites

- A Kubernetes cluster with the Dynamo Operator plus DRA / ComputeDomain support for MNNVL placement.
- A shared RWX PVC for model weights and FlashInfer JIT artifacts.
- A Hugging Face token with access to
`nvidia/GLM-5-NVFP4`

.

**5x 4xGB200 nodes**in an NVL36 or NVL72 domain. The published runtime image (`nvcr.io/nvidia/ai-dynamo/sglang-runtime:1.1.1-cuda13`

) is used as-is.

**5x p6e-gb200.36xlarge**nodes (4x GB200 + 4x EFA NICs each) or equivalent GB200 in an MNNVL domain.- AWS EFA driver 3.0.0g or newer on the nodes (default on modern AWS EKS AMIs).
- A container registry you can push to — this variant requires building a custom image from
`Dockerfile.efa`

before deploying (there is no prebuilt EFA image).

Create the namespace and token secret:

The manifests use standard NVIDIA GPU Feature Discovery labels to select GB200 nodes and include common GPU/ARM tolerations. If your cluster uses different labels, taints, or storage classes, update `nodeSelector`

, `tolerations`

, and `storageClassName`

before deploying.

## Deploy

Create the model-cache PVC and download the weights (shared by both targets):

If your cluster already provides a shared RWX cache PVC, skip `model-cache.yaml`

and update `claimName: model-cache`

in the download, deploy, and perf manifests, keeping the mount path as `/model-store`

.

Edit `sglang/disagg/deploy.yaml`

and replace the `<your-namespace>`

placeholder, then:

First cold starts can take up to about an hour while the runtime loads weights and JIT-compiles FlashInfer/DeepGEMM kernels:

Build the custom container image first — it bakes a patched libfabric ([ofiwg/libfabric#12019](https://github.com/ofiwg/libfabric/pull/12019)) into the runtime so `fi_mr_reg`

on CUDA VRAM succeeds on GB200’s 64K-page arm64 kernel:

Then edit `sglang/disagg/efa/deploy.yaml`

to replace `<your-namespace>`

and the image placeholder, and:

After startup, verify the LIBFABRIC backend is actually carrying KV traffic (not silent TCP fallback) — the [EFA README](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/glm-5-nvfp4/sglang/disagg/efa/README.md) includes three checks (NIXL backend log line, executable `libplugin_LIBFABRIC.so`

mapping, and `nixl_num_failed_transfers_total`

staying at 0).

## Smoke Test

Send a test request to verify the deployment serves traffic:

## Benchmark

Both targets ship a `perf.yaml`

Kubernetes Job with the same workload shape: ISL=1000, OSL=8192, concurrency=512 (32 per decode GPU), 1,536 requests.

The Job wraps this AIPerf run:

Edit `sglang/disagg/perf.yaml`

to replace the namespace placeholder, then:

The Job wraps this AIPerf run:

Edit `sglang/disagg/efa/perf.yaml`

to replace the namespace placeholder, then:

## Expected Performance

Reference AIPerf run for the standard target (ISL=1k, OSL=8k, concurrency=512): 1,536 requests, 0 errors, 747.87s benchmark duration. This is a concurrency-burst benchmark, so TTFT includes queueing under 512 concurrent users.

Reference AIPerf run for the EFA variant at the same workload shape (ISL=1k, OSL=8k, concurrency=512; measured on 5x p6e-gb200.36xlarge, EFA driver 3.0.0g):

At long context (ISL=20k, OSL=2k, concurrency=64), the LIBFABRIC backend delivers 39% higher throughput and 56% lower TTFT p50 than the UCX default — full tables in the [EFA README](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/glm-5-nvfp4/sglang/disagg/efa/README.md).

## Compare All Targets

Both targets run the same disaggregated topology — 1 prefill node (TP4) plus 4 decode nodes (TP16/DP16/EP16) with EAGLE MTP speculative decoding and FP8 KV cache — and differ only in infrastructure and the KV-transfer backend:

## Notes

**EAGLE MTP speculative decoding**(~85-95% accept rate) is enabled by two env vars:`SGLANG_ENABLE_SPEC_V2=1`

(EAGLEWorkerV2 with overlap scheduler) and`SGLANG_NVFP4_CKPT_FP8_NEXTN_MOE=1`

(quantizes the BF16 MTP layer to FP8 at load time, matching the base model’s compute path).**FP8 KV cache**: uses`--kv-cache-dtype fp8_e4m3`

(the NSA backend auto-selects this on SM100/GB200), saving roughly 50% KV memory vs BF16.**FlashInfer JIT cache**: the runtime image has no prebuilt`flashinfer-jit-cache`

wheel, so the recipe sets`FLASHINFER_WORKSPACE_BASE=/model-store`

to persist first-run JIT artifacts on the shared PVC for later pod starts.- Worker containers run as root because FlashInfer’s bundled cubin package creates TRTLLM MoE symlinks inside its installed package directory during startup. The benchmark pod runs as a non-root user and pins Transformers v5 because
`nvidia/GLM-5-NVFP4`

declares`tokenizer_class=TokenizersBackend`

. - The standard target sets
`UCX_TLS=cuda_copy,cuda_ipc,tcp`

for NIXL/UCX KV transfer; the EFA variant instead sets`SGLANG_DISAGGREGATION_NIXL_BACKEND=LIBFABRIC`

and runs containers privileged so`fi_mr_reg`

can pin VRAM for RDMA. Without the env var, SGLang silently falls back to TCP on kernel 6.8+. **Recovery caveat**: the decode side is one TP16 rank group spread across four nodes. Treat single decode-pod replacement as disruptive and validate full-group recovery before relying on individual decode pod restarts; in validation, deleting one decode worker left the graph NotReady through repeated rank-group reinitialization attempts.

## Source

- Source README:
[recipes/glm-5-nvfp4/README.md](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/glm-5-nvfp4/README.md) - SGLang disaggregated prefill/decode:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/glm-5-nvfp4/sglang/disagg/deploy.yaml)and[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/glm-5-nvfp4/sglang/disagg/perf.yaml) - EFA variant:
[README.md](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/glm-5-nvfp4/sglang/disagg/efa/README.md),[Dockerfile.efa](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/glm-5-nvfp4/sglang/disagg/efa/Dockerfile.efa),[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/glm-5-nvfp4/sglang/disagg/efa/deploy.yaml), and[perf.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/glm-5-nvfp4/sglang/disagg/efa/perf.yaml) - Setup assets:
[recipes/glm-5-nvfp4/model-cache/model-cache.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/glm-5-nvfp4/model-cache/model-cache.yaml)and[recipes/glm-5-nvfp4/model-cache/model-download.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/glm-5-nvfp4/model-cache/model-download.yaml)
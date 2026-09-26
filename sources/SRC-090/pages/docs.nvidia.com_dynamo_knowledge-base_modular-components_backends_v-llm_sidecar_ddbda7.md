source: https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/sidecar
lastmod: 2026-09-24T19:58:16.636Z

# vLLM Sidecar

**Experimental.** The vLLM sidecar, launchers, packaging, and feature coverage
can change without notice.

`dynamo-vllm-sidecar`

is a CPU-only Dynamo worker that connects to vLLM’s native
gRPC service. It preserves the upstream engine process and argument surface
while using Dynamo for request handling and distributed serving. See the
[Sidecar Backends](https://docs.nvidia.com/dynamo/knowledge-base/concepts/system-architecture/sidecar-backends-experimental) page for the common
architecture.

## Readiness

This table covers launch topology only. The
[vLLM feature matrix](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/overview#feature-support-matrix) describes the in-process
backend; sidecar feature parity is still under evaluation. See the
[vLLM sidecar README](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/lib/sidecar/vllm/README.md)
for current protocol limitations.

## Launch Locally

From a Dynamo source checkout, build or install Dynamo so
`dynamo-vllm-sidecar`

is on `PATH`

. Install a vLLM build that provides
`vllm-rs`

and its native gRPC server.

Start Dynamo’s local discovery services, then run the aggregated launcher:

To run separate prefill and decode engines on two GPUs:

Each launcher starts the Dynamo frontend, the vLLM engine process or processes, and the matching sidecar workers. It binds the native gRPC endpoints to loopback.

Verify the frontend:

## Deploy on Kubernetes

No published vLLM sidecar image is available yet. Follow the
[Kubernetes quick start](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/lib/sidecar/vllm/README.md#deploy-on-kubernetes-quick-start)
to build the CPU-only sidecar image and pair it with a stock upstream vLLM
image. The source tree includes
[aggregated](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/lib/sidecar/vllm/deploy/agg.yaml)
and
[disaggregated](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/lib/sidecar/vllm/deploy/disagg.yaml)
manifests.
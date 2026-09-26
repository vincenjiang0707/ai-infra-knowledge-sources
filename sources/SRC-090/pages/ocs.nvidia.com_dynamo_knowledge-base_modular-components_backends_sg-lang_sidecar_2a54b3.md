source: https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/sg-lang/sidecar
lastmod: 2026-09-24T19:58:16.636Z

# SGLang Sidecar

**Experimental.** The SGLang sidecar, launchers, packaging, and feature
coverage can change without notice.

`dynamo-sglang-sidecar`

is a CPU-only Dynamo worker that connects to SGLang’s
native gRPC service. It preserves the upstream engine process and argument
surface while using Dynamo for request handling and distributed serving. See
the [Sidecar Backends](https://docs.nvidia.com/dynamo/knowledge-base/concepts/system-architecture/sidecar-backends-experimental) page for the common
architecture.

## Readiness

This table covers launch topology only. The
[SGLang feature matrix](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/sg-lang/overview#feature-support-matrix) describes the
in-process backend; sidecar feature parity is still under evaluation. See the
[SGLang sidecar README](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/lib/sidecar/sglang/README.md)
for current protocol details.

## Launch Locally

From a Dynamo source checkout, build or install Dynamo so
`dynamo-sglang-sidecar`

is on `PATH`

. Install SGLang v0.5.16 or later, which
provides the native `--grpc-port`

server option.

Start Dynamo’s local discovery services, then run the aggregated launcher:

To run separate prefill and decode engines on two GPUs:

Each launcher starts the Dynamo frontend, the SGLang engine process or processes, and the matching sidecar workers. It binds SGLang’s HTTP and native gRPC endpoints to loopback.

Verify the frontend:

## Deploy on Kubernetes

No published SGLang sidecar image is available yet. Follow the
[Kubernetes quick start](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/lib/sidecar/sglang/README.md#deploy-on-kubernetes-quick-start)
to build the CPU-only sidecar image and pair it with a stock upstream SGLang
image. The source tree includes
[aggregated](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/lib/sidecar/sglang/deploy/agg.yaml)
and
[disaggregated](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/lib/sidecar/sglang/deploy/disagg.yaml)
manifests.
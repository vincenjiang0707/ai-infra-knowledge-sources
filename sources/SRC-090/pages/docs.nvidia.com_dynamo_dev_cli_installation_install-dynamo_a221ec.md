source: https://docs.nvidia.com/dynamo/dev/cli/installation/install-dynamo
lastmod: 2026-09-24T19:58:16.636Z

# Local Installation

This guide walks through installing Dynamo on a local machine or VM with one or more GPUs.

For production multi-node clusters, see the [Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). To build from source for development, see [Building from Source](https://docs.nvidia.com/dynamo/dev/advanced-customizations/building-from-source).

## System Requirements

TensorRT-LLM does not support Python 3.11.

For the full compatibility matrix including backend framework versions, see the [Support Matrix](https://docs.nvidia.com/dynamo/reference/compatibility).

## Prerequisites

Before installing Dynamo, make sure the host has the following. The GPU driver is the only piece that must live on the host in every case — the prebuilt container bundles CUDA and all framework dependencies, so the CUDA toolkit is only needed for the Python virtual environment path.

Verify the driver is installed and the GPU is visible:

This covers single-machine setups only. Multi-node disaggregated serving additionally needs an RDMA-capable interconnect (NIXL/UCX) — out of scope for this guide. For clusters, the [Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart) covers the GPU Operator and, where applicable, the Network Operator instead of these host-level installs.

## Install Dynamo

### Clone the Dynamo repository

The repository provides the infrastructure Compose file, launch scripts, and engine configs referenced throughout this guide:

### Start infrastructure services (NATS + etcd)

Dynamo components discover each other through etcd and exchange events through NATS. Bring both up in the background with Docker Compose:

Leave these running for the rest of the guide.

NATS and etcd are **not strictly required** for a single-machine setup — you can pass `--discovery-backend file`

to the frontend and worker to skip them entirely (discovery falls back to the local filesystem and events to ZMQ). They are **recommended** because they match the multi-node, production, and Kubernetes deployment path. See [Discovery and events on a single machine](https://docs.nvidia.com/dynamo/dev/cli/installation/install-dynamo#discovery-and-events-on-a-single-machine) below for the trade-offs.

### Install for your backend

You can run Dynamo two ways. Choose one:

**Prebuilt container (recommended)**— all dependencies are pre-installed and the repository contents are bundled at`/workspace`

. Because the frontend and worker run*inside*this container, you’ll need to`docker exec`

into it to run subsequent commands.**Python virtual environment (PyPI)**— install the`ai-dynamo`

wheel for your backend directly on the host.

Pick a backend, release channel, backend version, and install form. The default selection starts the latest stable SGLang container.

### Choose your build

Unavailable combinations remain visible to show the current support boundary.

docker run --gpus all --network host --ipc host --rm -it nvcr.io/nvidia/ai-dynamo/sglang-runtime:1.5.0

The container command drops you into a shell with Dynamo and its backend dependencies installed. `--network host`

lets the container reach NATS and etcd on the host.

Before using a wheel command, create and activate a Python virtual environment:

Install the host packages required by your backend before running the selected wheel command:

###### SGLang

###### TensorRT-LLM

###### vLLM

For CUDA 13 (B300/GB300), the container is recommended. See the [SGLang install docs](https://docs.sglang.io/docs/get-started/install) for details.

See [Release Artifacts](https://docs.nvidia.com/dynamo/reference/release-artifacts) for the complete artifact inventory.

## Discovery and events on a single machine

Dynamo is a distributed runtime: the **frontend** (the OpenAI-compatible HTTP server) and the **worker** (the engine running your model) are separate processes that have to find each other. Two planes make that happen:

**Discovery plane**— how the frontend learns which workers exist. Workers register their endpoints on startup; the frontend watches for them and routes requests accordingly.**Event plane**— how components exchange KV-cache events and worker metrics, which power features like KV-aware routing and the planner.

On a single machine you can run either of two configurations:

The `file`

mode is the lightest way to get a model answering with no prerequisites — ideal for a quick local smoke test. This guide uses **etcd + NATS** instead because it is the same discovery path Dynamo uses for multi-node and Kubernetes deployments, so what you learn here carries forward to production.

To use the zero-dependency mode instead, skip the infrastructure step above and pass `--discovery-backend file`

to both the frontend and each worker.

This applies to **local, single-machine** setups. On Kubernetes, the Dynamo operator manages discovery natively (via custom resources and EndpointSlices) and sets `DYN_DISCOVERY_BACKEND=kubernetes`

automatically — neither `file`

mode nor a standalone etcd is used. See the [Discovery Plane](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/architecture#discovery-plane) design doc for the full picture.

## Troubleshooting

**CUDA/driver version mismatch**

Run `nvidia-smi`

to check your driver version. Dynamo requires driver 575.51.03+ for CUDA 12 or 580.00.03+ for CUDA 13. B300/GB300 GPUs require CUDA 13. See the [Support Matrix](https://docs.nvidia.com/dynamo/reference/compatibility) for full requirements.

**Python 3.11 with TensorRT-LLM**

TensorRT-LLM does not support Python 3.11. If you see installation failures with TensorRT-LLM, check your Python version with `python3 --version`

. Use Python 3.10 or 3.12 instead.

**Container runs but GPU not detected**

Ensure you passed `--gpus all`

to `docker run`

. Without this flag, the container won’t have access to GPUs:

## Next Steps

[Backend Guides](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/backends/sg-lang/overview)— Backend-specific configuration and features[Disaggregated Serving](https://docs.nvidia.com/dynamo/dev/kubernetes/disaggregated-serving/overview)— Scale prefill and decode independently[KV Cache Aware Routing](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-guide)— Smart request routing[Kubernetes Deployment](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart)— Production multi-node deployments
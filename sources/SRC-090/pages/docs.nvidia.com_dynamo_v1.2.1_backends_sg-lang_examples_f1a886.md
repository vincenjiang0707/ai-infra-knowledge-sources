source: https://docs.nvidia.com/dynamo/v1.2.1/backends/sg-lang/examples
lastmod: 2026-09-24T19:58:16.636Z

# Examples

For quick start instructions, see the [SGLang README](https://docs.nvidia.com/dynamo/v1.2.1/backends/sg-lang). This document provides all deployment patterns for running SGLang with Dynamo, including LLMs, multimodal, and diffusion models, and Kubernetes deployment.

## Infrastructure Setup

For local/bare-metal development, start etcd and optionally NATS using Docker Compose:

**etcd**is optional but is the default local discovery backend. You can also use`--discovery-backend file`

to use file system based discovery.**NATS**is only needed when using NATS-backed KV routing events (`--kv-events-config`

). Use ZMQ-backed events or`--no-router-kv-events`

for routing without NATS.**On Kubernetes**, neither is required when using the Dynamo operator (`DYN_DISCOVERY_BACKEND=kubernetes`

).

Each launch script runs the frontend and worker(s) in a single terminal. You can run each command separately in different terminals for testing. For AI agents working with Dynamo, you can run the launch script in the background and use the `curl`

commands to test the deployment.

## LLM Serving

### Aggregated Serving

The simplest deployment pattern: a single worker handles both prefill and decode.

### Aggregated Serving with KV Routing

Two workers behind a [KV-aware router](https://docs.nvidia.com/dynamo/v1.2.1/components/router) that maximizes cache reuse:

This launches the frontend with `--router-mode kv`

and two workers with ZMQ-based KV event publishing.

### Disaggregated Serving

Separates prefill and decode into independent workers connected via NIXL for KV cache transfer. Requires 2 GPUs.

For details on how SGLang disaggregation works with Dynamo, including the bootstrap mechanism and RDMA transfer flow, see [SGLang Disaggregation](https://docs.nvidia.com/dynamo/v1.2.1/backends/sg-lang/disaggregation).

### Disaggregated Serving with KV-Aware Prefill Routing

Scales to 2 prefill + 2 decode workers with KV-aware routing on both pools. Requires 4 GPUs.

The frontend uses `--router-mode kv`

and automatically detects prefill workers to activate an internal prefill router. Each worker publishes KV events over ZMQ on unique ports.

## Multimodal Serving

### Aggregated Multimodal

Serve multimodal models using SGLang’s built-in multimodal support:

###### Verify the deployment


### Multimodal with Disaggregated Components

For advanced multimodal deployments with separate encoder, prefill, and decode workers (E/PD and E/P/D patterns), see the dedicated [SGLang Multimodal](https://docs.nvidia.com/dynamo/v1.2.1/features/multimodal/multimodal-sglang.md) documentation.

## Diffusion Models

### Diffusion LM

Run diffusion language models like [LLaDA2.0](https://github.com/inclusionAI/LLaDA2.0):

### Image Diffusion

Generate images from text prompts using [FLUX](https://huggingface.co/black-forest-labs/FLUX.1-dev) or other diffusion models:

Options: `--model-path`

, `--fs-url`

(local or S3), `--http-url`

.

### Video Generation

Generate videos from text prompts using [Wan2.1](https://huggingface.co/Wan-AI) models:

Options: `--wan-size 1b|14b`

, `--num-frames`

, `--height`

, `--width`

, `--num-inference-steps`

.

For full details on all diffusion worker types (LLM, image, video), see [Diffusion](https://docs.nvidia.com/dynamo/v1.2.1/backends/sg-lang/diffusion).

### Kubernetes Deployment

For complete K8s deployment examples, see:

## Troubleshooting

### CuDNN Version Check Fails

Set `SGLANG_DISABLE_CUDNN_CHECK=1`

before launching. This is common when PyTorch ships a CuDNN version older than what SGLang’s Conv3d models require. Affects vision and diffusion models.

### Model Registration Fails with `config.json`

Error

This happens with diffusers models (FLUX.1-dev, Wan2.1, etc.) that use `model_index.json`

instead of `config.json`

. Ensure you are using the correct worker flag (`--image-diffusion-worker`

or `--video-generation-worker`

) rather than the standard LLM worker mode. These flags use a registration path that does not require `config.json`

.

### GPU OOM on Startup

If a previous run left orphaned GPU processes, the next launch may OOM. Check for zombie processes:

### Disaggregated Workers Cannot Connect

Ensure both prefill and decode workers can reach each other over TCP. The bootstrap mechanism uses `--disaggregation-bootstrap-port`

(default: 12345). For multi-node setups, ensure the port is reachable across hosts and set `--host 0.0.0.0`

.

## See Also

: Quick start and feature overview[SGLang README](https://docs.nvidia.com/dynamo/v1.2.1/backends/sg-lang): Architecture, configuration, and operational details[Reference Guide](https://docs.nvidia.com/dynamo/v1.2.1/backends/sg-lang/reference-guide): Vision model deployment patterns[SGLang Multimodal](https://docs.nvidia.com/dynamo/v1.2.1/features/multimodal/multimodal-sglang.md): Hierarchical cache integration[SGLang HiCache](https://docs.nvidia.com/dynamo/v1.2.1/integrations/kv-cache-integrations/hi-cache): Performance benchmarking tools[Benchmarking](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/benchmarking): P/D tuning guide[Tuning Disaggregated Performance](https://docs.nvidia.com/dynamo/v1.2.1/additional-resources/tuning-disaggregated-performance)
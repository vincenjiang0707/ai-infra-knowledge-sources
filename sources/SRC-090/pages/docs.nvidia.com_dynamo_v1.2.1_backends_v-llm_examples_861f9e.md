source: https://docs.nvidia.com/dynamo/v1.2.1/backends/v-llm/examples
lastmod: 2026-09-24T19:58:16.636Z

# Examples

For quick start instructions, see the [vLLM README](https://docs.nvidia.com/dynamo/v1.2.1/backends/v-llm). This document provides all deployment patterns for running vLLM with Dynamo, including aggregated, disaggregated, KV-routed, and expert-parallel configurations.

## Table of Contents

## Infrastructure Setup

For local/bare-metal development, start etcd and optionally NATS using Docker Compose:

**etcd**is optional but is the default local discovery backend. File-based discovery is also available (see`python -m dynamo.vllm --help`

for`--discovery-backend`

options).**NATS**is only needed when using NATS-backed KV routing events. ZMQ-backed events and prediction-based routing do not require NATS.**On Kubernetes**, neither is required when using the Dynamo operator.

Each launch script runs the frontend and worker(s) in a single terminal. You can run each command separately in different terminals for better log visibility. For AI agents working with Dynamo, you can run the launch script in the background and use the `curl`

commands to test the deployment.

## LLM Serving

### Aggregated Serving

The simplest deployment pattern: a single worker handles both prefill and decode. Requires 1 GPU.

Run on CUDA devices:

Run on XPUs:

### Aggregated Serving with KV Routing

Two workers behind a [KV-aware router](https://docs.nvidia.com/dynamo/v1.2.1/components/router) that maximizes cache reuse. Requires 2 GPUs.

Run on CUDA devices:

Run on XPUs:

This launches the frontend in KV routing mode with two workers publishing KV events over ZMQ.

### Disaggregated Serving

Separates prefill and decode into independent workers connected via NIXL for KV cache transfer. Requires 2 GPUs.

### Disaggregated Serving with KV Routing

Scales to 2 prefill + 2 decode workers with KV-aware routing on both pools. Requires 4 GPUs.

The frontend runs in KV routing mode and automatically detects prefill workers to activate an internal prefill router.

### Data Parallel / Expert Parallelism

Launches 4 data-parallel workers with expert parallelism behind a KV-aware router. Uses a Mixture-of-Experts model (`Qwen/Qwen3-30B-A3B`

). Requires 4 GPUs.

Run a disaggregated example and try adding another prefill worker once the setup is running! The system will automatically discover and utilize the new worker.

## Advanced Examples

### Speculative Decoding

Run **Meta-Llama-3.1-8B-Instruct** with **Eagle3** as a draft model for faster inference while maintaining accuracy.

**Guide:** [Speculative Decoding Quickstart](https://docs.nvidia.com/dynamo/v1.2.1/additional-resources/speculative-decoding/speculative-decoding-with-v-llm)


See also:[Speculative Decoding Feature Overview]for cross-backend documentation.

### Multimodal

Serve multimodal models using the vLLM-Omni integration.

**Guide:** [vLLM-Omni](https://docs.nvidia.com/dynamo/v1.2.1/backends/v-llm/v-llm-omni)

### Multi-Node

Deploy vLLM across multiple nodes using Dynamo’s distributed capabilities. Multi-node deployments require network connectivity between nodes and firewall rules allowing NATS/ETCD communication.

Start NATS/ETCD on the head node so all worker nodes can reach them:

For multi-node tensor/pipeline parallelism (when TP x PP exceeds GPUs on a single node), see [ launch/multi_node_tp.sh](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/examples/backends/vllm/launch/multi_node_tp.sh). For details on distributed execution, see the

[vLLM multiprocessing docs](https://docs.vllm.ai/en/stable/serving/parallelism_scaling/#running-vllm-with-multiprocessing).

### DeepSeek-R1

Dynamo supports DeepSeek R1 with data parallel attention and wide expert parallelism. Each DP attention rank is a separate Dynamo component emitting its own KV events and metrics.

Run on 2 nodes (16 GPUs, dp=16):

See [ launch/dsr1_dep.sh](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/examples/backends/vllm/launch/dsr1_dep.sh) for configurable options.

## Kubernetes Deployment

For complete Kubernetes deployment instructions, configurations, and troubleshooting, see the [vLLM Kubernetes Deployment Guide](https://github.com/ai-dynamo/dynamo/tree/v1.2.1/examples/backends/vllm/deploy/README.md).

See also the [Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/start-here/kubernetes-quickstart) for general Dynamo K8s documentation.

## Troubleshooting

### Workers Fail to Start with NIXL Errors

Ensure NIXL is installed and the side-channel ports are not in conflict. Each worker in a multi-worker setup needs a unique `VLLM_NIXL_SIDE_CHANNEL_PORT`

.

### KV Router Not Routing Correctly

Ensure `PYTHONHASHSEED=0`

is set for all vLLM processes when using KV-aware routing. See [Hashing Consistency](https://docs.nvidia.com/dynamo/v1.2.1/backends/v-llm/reference-guide#hashing-consistency-for-kv-events) for details.

### GPU OOM on Startup

If a previous run left orphaned GPU processes, the next launch may OOM. Check for zombie processes:

## See Also

: Quick start and feature overview[vLLM README](https://docs.nvidia.com/dynamo/v1.2.1/backends/v-llm): Configuration, arguments, and operational details[Reference Guide](https://docs.nvidia.com/dynamo/v1.2.1/backends/v-llm/reference-guide): Metrics and monitoring[Observability](https://docs.nvidia.com/dynamo/v1.2.1/backends/v-llm/observability): Performance benchmarking tools[Benchmarking](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/benchmarking): P/D tuning guide[Tuning Disaggregated Performance](https://docs.nvidia.com/dynamo/v1.2.1/additional-resources/tuning-disaggregated-performance)
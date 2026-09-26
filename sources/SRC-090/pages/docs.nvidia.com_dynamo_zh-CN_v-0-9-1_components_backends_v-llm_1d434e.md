source: https://docs.nvidia.com/dynamo/zh-CN/v-0-9-1/components/backends/v-llm
lastmod: 2026-09-23T23:30:39.914Z

# LLM Deployment using vLLM

This directory contains reference implementations for deploying Large Language Models (LLMs) in various configurations using vLLM. For Dynamo integration, we leverage vLLM’s native KV cache events, NIXL based transfer mechanisms, and metric reporting to enable KV-aware routing and P/D disaggregation.

## Use the Latest Release

We recommend using the latest stable release of Dynamo to avoid breaking changes:

You can find the latest release [here](https://github.com/ai-dynamo/dynamo/releases/latest) and check out the corresponding branch with:

## Table of Contents

[Feature Support Matrix](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/v-llm#feature-support-matrix)[Quick Start](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/v-llm#quick-start)[Single Node Examples](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/v-llm#run-single-node-examples)[Advanced Examples](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/v-llm#advanced-examples)[Deploy on Kubernetes](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/v-llm#kubernetes-deployment)[Configuration](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/v-llm#configuration)

## Feature Support Matrix

### Core Dynamo Features

### Large Scale P/D and WideEP Features

## vLLM Quick Start

Below we provide a guide that lets you run all of our the common deployment patterns on a single node.

### Start Infrastructure Services (Local Development Only)

For local/bare-metal development, start etcd and optionally NATS using [Docker Compose](https://github.com/ai-dynamo/dynamo/blob/v0.9.1/deploy/docker-compose.yml):

**etcd**is optional but is the default local discovery backend. You can also use`--kv_store file`

to use file system based discovery.**NATS**is optional - only needed if using KV routing with events (default). You can disable it with`--no-kv-events`

flag for prediction-based routing**On Kubernetes**, neither is required when using the Dynamo operator, which explicitly sets`DYN_DISCOVERY_BACKEND=kubernetes`

to enable native K8s service discovery (DynamoWorkerMetadata CRD)

### Pull or build container

We have public images available on [NGC Catalog](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/collections/ai-dynamo/artifacts). If you’d like to build your own container from source:

### Run container

This includes the specific commit [vllm-project/vllm#19790](https://github.com/vllm-project/vllm/pull/19790) which enables support for external control of the DP ranks.

## Run Single Node Examples

Below we provide simple shell scripts that run the components for each configuration. Each shell script runs `python3 -m dynamo.frontend`

to start the ingress and uses `python3 -m dynamo.vllm`

to start the vLLM workers. You can also run each command in separate terminals for better log visibility.

### Aggregated Serving

### Aggregated Serving with KV Routing

### Disaggregated Serving

### Disaggregated Serving with KV Routing

### Single Node Data Parallel Attention / Expert Parallelism

This example is not meant to be performant but showcases Dynamo routing to data parallel workers

Run a disaggregated example and try adding another prefill worker once the setup is running! The system will automatically discover and utilize the new worker.

## Advanced Examples

Below we provide a selected list of advanced deployments. Please open up an issue if you’d like to see a specific example!

### Speculative Decoding with Aggregated Serving (Meta-Llama-3.1-8B-Instruct + Eagle3)

Run **Meta-Llama-3.1-8B-Instruct** with **Eagle3** as a draft model using **aggregated speculative decoding** on a single node.
This setup demonstrates how to use Dynamo to create an instance using Eagle-based speculative decoding under the **VLLM aggregated serving framework** for faster inference while maintaining accuracy.

**Guide:** [Speculative Decoding Quickstart](https://docs.nvidia.com/dynamo/v-0-9-1/additional-resources/speculative-decoding/speculative-decoding-with-v-llm)


See also:[Speculative Decoding Feature Overview]for cross-backend documentation.

### Kubernetes Deployment

For complete Kubernetes deployment instructions, configurations, and troubleshooting, see [vLLM Kubernetes Deployment Guide](https://github.com/ai-dynamo/dynamo/tree/main/examples/backends/vllm/deploy/README.md)

## Configuration

vLLM workers are configured through command-line arguments. Key parameters include:

`--model`

: Model to serve (e.g.,`Qwen/Qwen3-0.6B`

)`--is-prefill-worker`

: Enable prefill-only mode for disaggregated serving`--metrics-endpoint-port`

: Port for publishing KV metrics to Dynamo`--connector`

: Specify which kv_transfer_config you want vllm to use`[nixl, lmcache, kvbm, none]`

. This is a helper flag which overwrites the engines KVTransferConfig.`--enable-prompt-embeds`

:**Enable prompt embeddings feature**(opt-in, default: disabled)**Required for:**Accepting pre-computed prompt embeddings via API**Default behavior:**Prompt embeddings DISABLED - requests with`prompt_embeds`

will fail**Error without flag:**`ValueError: You must set --enable-prompt-embeds to input prompt_embeds`



See `args.py`

for the full list of configuration options and their defaults.

The [documentation](https://docs.vllm.ai/en/v0.9.2/configuration/serve_args.html?h=serve+arg) for the vLLM CLI args points to running ‘vllm serve —help’ to see what CLI args can be added. We use the same argument parser as vLLM.

### Hashing Consistency for KV Events

When using KV-aware routing, ensure deterministic hashing across processes to avoid radix tree mismatches. Choose one of the following:

- Set
`PYTHONHASHSEED=0`

for all vLLM processes when relying on Python’s builtin hashing for prefix caching. - If your vLLM version supports it, configure a deterministic prefix caching algorithm, for example:

See the high-level notes in [Router Design](https://docs.nvidia.com/dynamo/v-0-9-1/design-docs/router-design#deterministic-event-ids) on deterministic event IDs.

## Request Migration

You can enable [request migration](https://docs.nvidia.com/dynamo/v-0-9-1/user-guides/fault-tolerance/request-migration) to handle worker failures gracefully. Use the `--migration-limit`

flag to specify how many times a request can be migrated to another worker:

This allows a request to be migrated up to 3 times before failing. See the [Request Migration Architecture](https://docs.nvidia.com/dynamo/v-0-9-1/user-guides/fault-tolerance/request-migration) documentation for details on how this works.

## Request Cancellation

When a user cancels a request (e.g., by disconnecting from the frontend), the request is automatically cancelled across all workers, freeing compute resources for other requests.

### Cancellation Support Matrix

For more details, see the [Request Cancellation Architecture](https://docs.nvidia.com/dynamo/v-0-9-1/user-guides/fault-tolerance/request-cancellation) documentation.
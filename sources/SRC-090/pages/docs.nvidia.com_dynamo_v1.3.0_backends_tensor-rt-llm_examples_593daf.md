source: https://docs.nvidia.com/dynamo/v1.3.0/backends/tensor-rt-llm/examples
lastmod: 2026-09-24T19:58:16.636Z

# Examples

Launch scripts cover aggregated, disaggregated, KV-routed, and multinode deployment patterns for the TensorRT-LLM backend.

For quick start instructions, see the [TensorRT-LLM README](https://docs.nvidia.com/dynamo/v1.3.0/backends/tensor-rt-llm). This document provides all deployment patterns for running TensorRT-LLM with Dynamo, including single-node, multi-node, and Kubernetes deployments.

## Table of Contents

## Infrastructure Setup

For local/bare-metal development, start etcd and optionally NATS using Docker Compose:

**etcd**is optional but is the default local discovery backend. You can also use`--discovery-backend file`

to use file system based discovery.**NATS**is optional - only needed if using NATS-backed KV routing events. Workers must be explicitly configured to publish events. Use ZMQ-backed events or`--no-router-kv-events`

on the frontend for routing without NATS.**On Kubernetes**, neither is required when using the Dynamo operator, which explicitly sets`DYN_DISCOVERY_BACKEND=kubernetes`

to enable native K8s service discovery (DynamoWorkerMetadata CRD).

Each launch script runs the frontend and worker(s) in a single terminal. You can run each command separately in different terminals for testing. Each shell script simply runs `python3 -m dynamo.frontend <args>`

to start up the ingress and `python3 -m dynamo.trtllm <args>`

to start up the workers.

For detailed information about KV-aware routing behavior, see [Routing Concepts](https://docs.nvidia.com/dynamo/v1.3.0/components/router/routing-concepts). For deployment modes, see the [Router Guide](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/kv-cache-aware-routing).

## Single Node Examples

### Aggregated

### Aggregated with KV Routing

### Disaggregated

### Disaggregated with KV Routing

In disaggregated workflow, requests are routed to the prefill worker to maximize KV cache reuse.

### Aggregated with Multi-Token Prediction (MTP) and DeepSeek R1

- There is a noticeable latency for the first two inference requests. Please send warm-up requests before starting the benchmark.
- MTP performance may vary depending on the acceptance rate of predicted tokens, which is dependent on the dataset or queries used while benchmarking. Additionally,
`ignore_eos`

should generally be omitted or set to`false`

when using MTP to avoid speculating garbage outputs and getting unrealistic acceptance rates.

## Advanced Examples

### Multinode Deployment

For comprehensive instructions on multinode serving, see the [Multinode Examples](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/tensor-rt-llm-details/multinode-examples) guide. It provides step-by-step deployment examples and configuration tips for running Dynamo with TensorRT-LLM across multiple nodes. While the walkthrough uses DeepSeek-R1 as the model, you can easily adapt the process for any supported model by updating the relevant configuration files. You can see the [Llama4 + Eagle](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/tensor-rt-llm-details/llama-4-eagle) guide to learn how to use these scripts when a single worker fits on a single node.

### Speculative Decoding

### Model-Specific Guides

[Gemma3 with Sliding Window Attention](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/tensor-rt-llm-details/gemma-3-sliding-window)— Reasoning model with tool calling support[GPT-OSS-120b](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/tensor-rt-llm-details/gpt-oss)

### Kubernetes Deployment

For complete Kubernetes deployment instructions, configurations, and troubleshooting, see the [TensorRT-LLM Kubernetes Deployment Guide](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/examples/backends/trtllm/deploy/README.md).

## Client

See the [client](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang#testing-the-deployment) section to learn how to send requests to the deployment.

To send a request to a multi-node deployment, target the node which is running `python3 -m dynamo.frontend <args>`

.
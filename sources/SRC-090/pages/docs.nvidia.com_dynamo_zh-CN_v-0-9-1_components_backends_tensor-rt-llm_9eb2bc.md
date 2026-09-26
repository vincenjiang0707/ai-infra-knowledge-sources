source: https://docs.nvidia.com/dynamo/zh-CN/v-0-9-1/components/backends/tensor-rt-llm
lastmod: 2026-09-23T23:30:39.914Z

LLM Deployment using TensorRT-LLM


LLM Deployment using TensorRT-LLM

This directory contains examples and reference implementations for deploying Large Language Models (LLMs) in various configurations using TensorRT-LLM.

## Use the Latest Release

We recommend using the latest stable release of dynamo to avoid breaking changes:

You can find the latest release [here](https://github.com/ai-dynamo/dynamo/releases/latest) and check out the corresponding branch with:

## Table of Contents

[Feature Support Matrix](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/tensor-rt-llm#feature-support-matrix)[Quick Start](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/tensor-rt-llm#quick-start)[Single Node Examples](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/tensor-rt-llm#single-node-examples)[Advanced Examples](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/tensor-rt-llm#advanced-examples)[KV Cache Transfer](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/tensor-rt-llm#kv-cache-transfer-in-disaggregated-serving)[Client](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/tensor-rt-llm#client)[Benchmarking](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/tensor-rt-llm#benchmarking)[Multimodal Support](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/tensor-rt-llm#multimodal-support)[Logits Processing](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/tensor-rt-llm#logits-processing)[Performance Sweep](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/tensor-rt-llm#performance-sweep)

## Feature Support Matrix

### Core Dynamo Features

### Large Scale P/D and WideEP Features

## TensorRT-LLM Quick Start

Below we provide a guide that lets you run all of our the common deployment patterns on a single node.

### Start Infrastructure Services (Local Development Only)

For local/bare-metal development, start etcd and optionally NATS using [Docker Compose](https://github.com/ai-dynamo/dynamo/blob/v0.9.1/deploy/docker-compose.yml):

**etcd**is optional but is the default local discovery backend. You can also use`--kv_store file`

to use file system based discovery.**NATS**is optional - only needed if using KV routing with events (default). You can disable it with`--no-kv-events`

flag for prediction-based routing**On Kubernetes**, neither is required when using the Dynamo operator, which explicitly sets`DYN_DISCOVERY_BACKEND=kubernetes`

to enable native K8s service discovery (DynamoWorkerMetadata CRD)

### Build container

### Run container

## Single Node Examples

Below we provide some simple shell scripts that run the components for each configuration. Each shell script is simply running the `python3 -m dynamo.frontend <args>`

to start up the ingress and using `python3 -m dynamo.trtllm <args>`

to start up the workers. You can easily take each command and run them in separate terminals.

For detailed information about the architecture and how KV-aware routing works, see the [Router Guide](https://docs.nvidia.com/dynamo/v-0-9-1/user-guides/kv-cache-aware-routing).

### Aggregated

### Aggregated with KV Routing

### Disaggregated

### Disaggregated with KV Routing

### Aggregated with Multi-Token Prediction (MTP) and DeepSeek R1

Notes:

- There is a noticeable latency for the first two inference requests. Please send warm-up requests before starting the benchmark.
- MTP performance may vary depending on the acceptance rate of predicted tokens, which is dependent on the dataset or queries used while benchmarking. Additionally,
`ignore_eos`

should generally be omitted or set to`false`

when using MTP to avoid speculating garbage outputs and getting unrealistic acceptance rates.

## Advanced Examples

Below we provide a selected list of advanced examples. Please open up an issue if you’d like to see a specific example!

### Multinode Deployment

For comprehensive instructions on multinode serving, see the [multinode-examples.md](https://docs.nvidia.com/dynamo/v-0-9-1/additional-resources/tensor-rt-llm-details/multinode-examples) guide. It provides step-by-step deployment examples and configuration tips for running Dynamo with TensorRT-LLM across multiple nodes. While the walkthrough uses DeepSeek-R1 as the model, you can easily adapt the process for any supported model by updating the relevant configuration files. You can see [Llama4+eagle](https://docs.nvidia.com/dynamo/v-0-9-1/additional-resources/tensor-rt-llm-details/llama-4-eagle) guide to learn how to use these scripts when a single worker fits on the single node.

### Speculative Decoding

### Kubernetes Deployment

For complete Kubernetes deployment instructions, configurations, and troubleshooting, see [TensorRT-LLM Kubernetes Deployment Guide](https://github.com/ai-dynamo/dynamo/tree/main/examples/backends/trtllm/deploy/README.md).

### Client

See [client](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/sg-lang#testing-the-deployment) section to learn how to send request to the deployment.

NOTE: To send a request to a multi-node deployment, target the node which is running `python3 -m dynamo.frontend <args>`

.

### Benchmarking

To benchmark your deployment with AIPerf, see this utility script, configuring the
`model`

name and `host`

based on your deployment: [perf.sh](https://github.com/ai-dynamo/dynamo/blob/v0.9.1/benchmarks/llm/perf.sh)

## KV Cache Transfer in Disaggregated Serving

Dynamo with TensorRT-LLM supports two methods for transferring KV cache in disaggregated serving: UCX (default) and NIXL (experimental). For detailed information and configuration instructions for each method, see the [KV cache transfer guide](https://docs.nvidia.com/dynamo/v-0-9-1/additional-resources/tensor-rt-llm-details/kv-cache-transfer).

## Request Migration

You can enable [request migration](https://docs.nvidia.com/dynamo/v-0-9-1/user-guides/fault-tolerance/request-migration) to handle worker failures gracefully. Use the `--migration-limit`

flag to specify how many times a request can be migrated to another worker:

**Prefill workers do not support request migration** and must use `--migration-limit=0`

(the default). Prefill workers only process prompts and return KV cache state - they don’t maintain long-running generation requests that would benefit from migration.

See the [Request Migration Architecture](https://docs.nvidia.com/dynamo/v-0-9-1/user-guides/fault-tolerance/request-migration) documentation for details on how this works.

## Request Cancellation

When a user cancels a request (e.g., by disconnecting from the frontend), the request is automatically cancelled across all workers, freeing compute resources for other requests.

### Cancellation Support Matrix

For more details, see the [Request Cancellation Architecture](https://docs.nvidia.com/dynamo/v-0-9-1/user-guides/fault-tolerance/request-cancellation) documentation.

## Client

See [client](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/sg-lang#testing-the-deployment) section to learn how to send request to the deployment.

NOTE: To send a request to a multi-node deployment, target the node which is running `python3 -m dynamo.frontend <args>`

.

## Benchmarking

To benchmark your deployment with AIPerf, see this utility script, configuring the
`model`

name and `host`

based on your deployment: [perf.sh](https://github.com/ai-dynamo/dynamo/blob/v0.9.1/benchmarks/llm/perf.sh)

## Multimodal support

Dynamo with the TensorRT-LLM backend supports multimodal models, enabling you to process both text and images (or pre-computed embeddings) in a single request. For detailed setup instructions, example requests, and best practices, see the [TensorRT-LLM Multimodal Guide](https://docs.nvidia.com/dynamo/v-0-9-1/user-guides/multimodality-support/tensor-rt-llm-multimodal).

## Logits Processing

Logits processors let you modify the next-token logits at every decoding step (e.g., to apply custom constraints or sampling transforms). Dynamo provides a backend-agnostic interface and an adapter for TensorRT-LLM so you can plug in custom processors.

### How it works

**Interface**: Implement`dynamo.logits_processing.BaseLogitsProcessor`

which defines`__call__(input_ids, logits)`

and modifies`logits`

in-place.**TRT-LLM adapter**: Use`dynamo.trtllm.logits_processing.adapter.create_trtllm_adapters(...)`

to convert Dynamo processors into TRT-LLM-compatible processors and assign them to`SamplingParams.logits_processor`

.**Examples**: See example processors in`lib/bindings/python/src/dynamo/logits_processing/examples/`

([temperature](https://github.com/ai-dynamo/dynamo/tree/main/lib/bindings/python/src/dynamo/logits_processing/examples/temperature.py),[hello_world](https://github.com/ai-dynamo/dynamo/tree/main/lib/bindings/python/src/dynamo/logits_processing/examples/hello_world.py)).

### Quick test: HelloWorld processor

You can enable a test-only processor that forces the model to respond with “Hello world!”. This is useful to verify the wiring without modifying your model or engine code.

Notes:

- When enabled, Dynamo initializes the tokenizer so the HelloWorld processor can map text to token IDs.
- Expected chat response contains “Hello world”.

### Bring your own processor

Implement a processor by conforming to `BaseLogitsProcessor`

and modify logits in-place. For example, temperature scaling:

Wire it into TRT-LLM by adapting and attaching to `SamplingParams`

:

### Current limitations

- Per-request processing only (batch size must be 1); beam width > 1 is not supported.
- Processors must modify logits in-place and not return a new tensor.
- If your processor needs tokenization, ensure the tokenizer is initialized (do not skip tokenizer init).

## Performance Sweep

For detailed instructions on running comprehensive performance sweeps across both aggregated and disaggregated serving configurations, see the [TensorRT-LLM Benchmark Scripts for DeepSeek R1 model](https://github.com/ai-dynamo/dynamo/blob/v0.9.1/examples/backends/trtllm/performance_sweeps/README.md). This guide covers recommended benchmarking setups, usage of provided scripts, and best practices for evaluating system performance.

## Dynamo KV Block Manager Integration

Dynamo with TensorRT-LLM currently supports integration with the Dynamo KV Block Manager. This integration can significantly reduce time-to-first-token (TTFT) latency, particularly in usage patterns such as multi-turn conversations and repeated long-context requests.

Here is the instruction: [Running KVBM in TensorRT-LLM](https://docs.nvidia.com/dynamo/v-0-9-1/user-guides/kv-cache-offloading#run-kvbm-in-dynamo-with-tensorrt-llm) .
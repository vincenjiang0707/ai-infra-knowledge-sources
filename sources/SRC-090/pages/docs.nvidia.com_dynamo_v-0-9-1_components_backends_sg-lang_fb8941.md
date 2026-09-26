source: https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/sg-lang
lastmod: 2026-09-24T19:58:16.636Z

# Running SGLang with Dynamo

## Use the Latest Release

We recommend using the latest stable release of dynamo to avoid breaking changes:

You can find the latest release [here](https://github.com/ai-dynamo/dynamo/releases/latest) and check out the corresponding branch with:

## Table of Contents

[Feature Support Matrix](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/sg-lang#feature-support-matrix)[Dynamo SGLang Integration](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/sg-lang#dynamo-sglang-integration)[Installation](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/sg-lang#installation)[Quick Start](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/sg-lang#quick-start)[Single Node Examples](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/sg-lang#run-single-node-examples)[Multi-Node and Advanced Examples](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/sg-lang#advanced-examples)[Deploy on SLURM or Kubernetes](https://docs.nvidia.com/dynamo/v-0-9-1/components/backends/sg-lang#deployment)

## Feature Support Matrix

### Core Dynamo Features

## Dynamo SGLang Integration

Dynamo SGLang integrates SGLang engines into Dynamo’s distributed runtime, enabling advanced features like disaggregated serving, KV-aware routing, and request migration while maintaining full compatibility with SGLang’s engine arguments.

### Argument Handling

Dynamo SGLang uses SGLang’s native argument parser, so **most SGLang engine arguments work identically**. You can pass any SGLang argument (like `--model-path`

, `--tp`

, `--trust-remote-code`

) directly to `dynamo.sglang`

.

#### Dynamo-Specific Arguments

#### Tokenizer Behavior

**Default (**: Dynamo handles tokenization/detokenization via our blazing fast frontend and passes`--use-sglang-tokenizer`

not set)`input_ids`

to SGLang**With**: SGLang handles tokenization/detokenization, Dynamo passes raw prompts`--use-sglang-tokenizer`


When using `--use-sglang-tokenizer`

, only `v1/chat/completions`

is available through Dynamo’s frontend.

### Request Cancellation

When a user cancels a request (e.g., by disconnecting from the frontend), the request is automatically cancelled across all workers, freeing compute resources for other requests.

#### Cancellation Support Matrix

⚠️ SGLang backend currently does not support cancellation during remote prefill phase in disaggregated mode.

For more details, see the [Request Cancellation Architecture](https://docs.nvidia.com/dynamo/v-0-9-1/user-guides/fault-tolerance/request-cancellation) documentation.

## Installation

### Install latest release

We suggest using uv to install the latest release of ai-dynamo[sglang]. You can install it with `curl -LsSf https://astral.sh/uv/install.sh | sh`


###### Expand for instructions


### Install editable version for development

###### Expand for instructions


This requires having rust installed. We also recommend having a proper installation of the cuda toolkit as sglang requires `nvcc`

to be available.

### Using docker containers

###### Expand for instructions


We are in the process of shipping pre-built docker containers that contain installations of DeepEP, DeepGEMM, and NVSHMEM in order to support WideEP and P/D. For now, you can quickly build the container from source with the following command.

And then run it using

## Quick Start

Below we provide a guide that lets you run all of our common deployment patterns on a single node.

### Start Infrastructure Services (Local Development Only)

For local/bare-metal development, start etcd and optionally NATS using [Docker Compose](https://github.com/ai-dynamo/dynamo/blob/v0.9.1/deploy/docker-compose.yml):

**etcd**is optional but is the default local discovery backend. You can also use`--kv_store file`

to use file system based discovery.**NATS**is optional - only needed if using KV routing with events (default). You can disable it with`--no-kv-events`

flag for prediction-based routing**On Kubernetes**, neither is required when using the Dynamo operator, which explicitly sets`DYN_DISCOVERY_BACKEND=kubernetes`

to enable native K8s service discovery (DynamoWorkerMetadata CRD)

Each example corresponds to a simple bash script that runs the OpenAI compatible server, processor, and optional router (written in Rust) and LLM engine (written in Python) in a single terminal. You can easily take each command and run them in separate terminals.

Additionally - because we use sglang’s argument parser, you can pass in any argument that sglang supports to the worker!

### Aggregated Serving

### Aggregated Serving with KV Routing

### Aggregated Serving for Embedding Models

Here’s an example that uses the [Qwen/Qwen3-Embedding-4B](https://huggingface.co/Qwen/Qwen3-Embedding-4B) model.

###### Send the following request to verify your deployment:


### Disaggregated serving

See [SGLang Disaggregation](https://docs.nvidia.com/dynamo/v-0-9-1/additional-resources/sg-lang-details/disaggregation) to learn more about how sglang and dynamo handle disaggregated serving.

### Disaggregated Serving with KV Aware Prefill Routing

### Disaggregated Serving with Mixture-of-Experts (MoE) models and DP attention

You can use this configuration to test out disaggregated serving with dp attention and expert parallelism on a single node before scaling to the full DeepSeek-R1 model across multiple nodes.

### Testing the Deployment

Send a test request to verify your deployment:

## Deployment

We currently provide deployment examples for Kubernetes and SLURM.
source: https://docs.nvidia.com/dynamo/v1.3.0/user-guides/lo-ra-adapters
lastmod: 2026-09-24T19:58:16.636Z

# LoRA Adapters

Serve fine-tuned LoRA adapters with dynamic loading and routing in Dynamo

LoRA (Low-Rank Adaptation) enables efficient fine-tuning and serving of specialized model variants without duplicating full model weights. Dynamo provides built-in support for dynamic LoRA adapter loading, caching, and inference routing.

## Backend Support

See the [Feature Matrix](https://docs.nvidia.com/dynamo/v1.3.0/resources/feature-matrix) for full compatibility details.

## Overview

Dynamo’s LoRA implementation provides:

**Dynamic loading**: Load and unload LoRA adapters at runtime without restarting workers**Multiple sources**: Load from local filesystem (`file://`

), S3-compatible storage (`s3://`

), or Hugging Face Hub (`hf://`

)**Automatic caching**: Downloaded adapters are cached locally to avoid repeated downloads**Discovery integration**: Loaded LoRAs are automatically registered and discoverable via`/v1/models`

**KV-aware routing**: Route requests to workers with the appropriate LoRA loaded**Kubernetes native**: Declarative LoRA management via the`DynamoModel`

CRD

### Architecture

The LoRA system consists of:

**Rust Core**(`lib/llm/src/lora/`

): High-performance downloading, caching, and validation**Python Manager**(`components/src/dynamo/common/lora/`

): Extensible wrapper with custom source support**Worker Handlers**(`components/src/dynamo/vllm/handlers.py`

): Load/unload API and inference integration

## Quick Start

### Prerequisites

- Dynamo installed with vLLM support
- For S3 sources: AWS credentials configured
- A LoRA adapter compatible with your base model

### Local Development

**1. Start Dynamo with LoRA support:**

**2. Load a LoRA adapter:**

**3. Run inference with the LoRA:**

### S3-Compatible Storage

For production deployments, store LoRA adapters in S3-compatible storage:

## Configuration

### Environment Variables

### vLLM Arguments

## Backend API Reference

### Load LoRA

Load a LoRA adapter from a source URI.

**Request:**

**Response:**

### List LoRAs

List all loaded LoRA adapters.

**Response:**

### Unload LoRA

Unload a LoRA adapter from the worker.

**Response:**

## Kubernetes Deployment

For Kubernetes deployments, use the `DynamoModel`

Custom Resource to declaratively manage LoRA adapters.

### DynamoModel CRD

### How It Works

When you create a `DynamoModel`

:

**Discovers endpoints**: Finds all pods running your`baseModelName`

**Creates service**: Automatically creates a Kubernetes Service**Loads LoRA**: Calls the LoRA load API on each endpoint**Updates status**: Reports which endpoints are ready

### Verify Deployment

For complete Kubernetes deployment details, see:

## Examples

## Troubleshooting

### LoRA Fails to Load

**Check S3 connectivity:**

**Check cache directory:**

**Check worker logs:**

### Model Not Found After Loading

- Verify the LoRA name matches exactly (case-sensitive)
- Check if the LoRA is listed:
`curl http://localhost:8081/v1/loras`

- Ensure discovery registration succeeded (check worker logs)

### Inference Returns Base Model Response

- Verify the
`model`

field in your request matches the`lora_name`

- Check that the LoRA is loaded on the worker handling your request
- For disaggregated serving, ensure both prefill and decode workers have the LoRA

## KV Cache-Aware LoRA Routing

When KV-aware routing is enabled, the router automatically accounts for LoRA adapter identity when computing block hashes. This means:

**Distinct hash spaces per adapter**: Blocks cached under adapter`A`

will never be confused with blocks cached under adapter`B`

or the base model, even if the token sequences are identical. The adapter name is mixed into the`LocalBlockHash`

computation.**Automatic prefix sharing within the same adapter**: Requests targeting the same LoRA adapter benefit from KV cache prefix matching just like base model requests do.**No configuration required**: The LoRA name is propagated automatically through KV events (`BlockStored`

) from the engine to the router. The router uses the`lora_name`

field on events to route LoRA requests to workers that have matching cached blocks.

This works end-to-end across the publisher pipeline, the KV consolidator (for deduplication), and the routing query path.

## See Also

[Feature Matrix](https://docs.nvidia.com/dynamo/v1.3.0/resources/feature-matrix)- Backend compatibility overview[vLLM Backend](https://docs.nvidia.com/dynamo/v1.3.0/backends/v-llm)- vLLM-specific configuration[Dynamo Operator](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/dynamo-operator)- Kubernetes operator overview[Routing Concepts](https://docs.nvidia.com/dynamo/v1.3.0/components/router/routing-concepts)- LoRA-aware request routing[KV Events for Custom Engines](https://docs.nvidia.com/dynamo/v1.3.0/integrations/kv-cache-integrations/kv-events-for-custom-engines)- Publishing LoRA-aware KV events
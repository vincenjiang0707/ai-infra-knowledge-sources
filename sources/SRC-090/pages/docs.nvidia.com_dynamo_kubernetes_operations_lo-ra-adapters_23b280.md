source: https://docs.nvidia.com/dynamo/kubernetes/operations/lo-ra-adapters
lastmod: 2026-09-25T12:26:00.485Z

# LoRA Adapters

Serve fine-tuned LoRA adapters with dynamic loading and routing in Dynamo

## What Are LoRA Adapters

LoRA (Low-Rank Adaptation) serves specialized model variants without duplicating full base weights. In Dynamo you can load adapters at runtime, route inference to workers that hold them, and manage them declaratively on Kubernetes. It provides:

**Dynamic loading**: Load and unload adapters without restarting workers**Multiple sources**:`file://`

,`s3://`

, or`hf://`

URIs**Automatic caching**: Downloaded adapters are cached under`DYN_LORA_PATH`

**Discovery**: Loaded adapters appear in`/v1/models`

**KV-aware routing**: Route requests to workers with the matching adapter and cached prefix blocks**Kubernetes native**: Declarative loading through the`DynamoModel`

CRD

###### Architecture


**Rust core**(`lib/llm/src/lora/`

): Downloading, caching, and validation**Python manager**(`components/src/dynamo/common/lora/`

): Custom source support**Worker handlers**(`components/src/dynamo/vllm/handlers.py`

): Load/unload API and inference integration

## Serve a LoRA Adapter

###### Kubernetes

###### Local

### Prerequisites

- A Kubernetes cluster with the Dynamo Platform installed and a vLLM runtime image
- A LoRA adapter compatible with your base model
- For
`s3://`

sources: AWS credentials in a Kubernetes Secret

Full manifests and MinIO setup: [Kubernetes LoRA deployment example](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/examples/backends/vllm/deploy/lora).

### Deploy a LoRA-enabled worker

Enable LoRA on the **worker**: set LoRA and system API environment variables, and pass vLLM LoRA flags in `args:`

. `DYN_SYSTEM_ENABLED`

and `DYN_SYSTEM_PORT`

expose load/unload on the worker system port.

Adapted from the [ agg_lora.yaml example](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/examples/backends/vllm/deploy/lora/agg_lora.yaml):

Apply and wait for readiness:

**Worker environment variables**

**vLLM worker arguments**

`--max-lora-rank`

to at least your adapter’s rank. A lower value causes load failures.###### S3 or MinIO credentials on the worker


Store secret keys in a Kubernetes Secret and set non-secret endpoint/region inline:

### Load an adapter

Use a `DynamoModel`

CRD for declarative, cluster-native loading. It discovers worker endpoints for `baseModelName`

, creates a Service, and calls the load API on each pod.

Verify readiness:

See [Managing Models with DynamoModel](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/managing-models-dynamo-model) for the full CRD workflow.

###### Load imperatively with the worker system API


Port-forward the worker system port and POST to `/v1/loras`

:

List loaded adapters with `GET /v1/loras`

. Unload with `DELETE /v1/loras/{lora_name}`

.

## KV Cache-Aware LoRA Routing

###### How LoRA-aware KV routing works


When KV-aware routing is enabled, the router accounts for LoRA adapter identity when computing block hashes:

**Distinct hash spaces per adapter**: Blocks cached under adapter`A`

are never confused with adapter`B`

or the base model, even when token sequences match. The adapter name is mixed into the`LocalBlockHash`

computation.**Prefix sharing within the same adapter**: Requests targeting the same LoRA adapter reuse KV prefix blocks like base-model requests.**No extra configuration**: The LoRA name propagates through KV events (`BlockStored`

) from the engine to the router. The router uses the`lora_name`

field to route requests to workers with matching cached blocks.

This works across the publisher pipeline, the KV consolidator, and the routing query path.

For a local two-worker demo with KV-aware routing, run [ agg_lora_router.sh](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/examples/backends/vllm/launch/lora/agg_lora_router.sh) and load the adapter on both worker system ports.

## Troubleshooting

###### LoRA fails to load


**Check S3 connectivity:**

**Check the cache directory:**

**Check worker logs:**

Confirm `--max-lora-rank`

is at least your adapter’s rank.

###### Model not found after loading


- Verify the LoRA name matches exactly (case-sensitive)
- List loaded adapters:
`curl http://localhost:9090/v1/loras`

(port-forward the worker’s`DYN_SYSTEM_PORT`

first on Kubernetes) - Check worker logs for discovery registration errors

###### Inference returns the base model response


- Confirm the request
`model`

field matches the loaded`lora_name`

- Verify the adapter is loaded on the worker handling the request
- For disaggregated serving, load the adapter on both prefill and decode workers

## Backend Support

See the [feature support matrix](https://docs.nvidia.com/dynamo/reference/general/compatibility.mdx#feature-support) for full compatibility details.
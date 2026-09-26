source: https://docs.nvidia.com/dynamo/zh-CN/dev/cli/operations/lo-ra-adapters
lastmod: 2026-09-23T23:30:39.914Z

# LoRA Adapters

Serve fine-tuned LoRA adapters with dynamic loading and routing in Dynamo

## What Are LoRA Adapters

Low-Rank Adaptation (LoRA) serves specialized model variants without duplicating full base weights. Dynamo supports dynamic LoRA lifecycle management with vLLM and SGLang, with different validation levels for each backend. It provides:

**Dynamic loading**: Load and unload adapters without restarting workers**Multiple sources**:`file://`

,`s3://`

, or`hf://`

URIs**Automatic caching**: Downloaded adapters are cached under`DYN_LORA_PATH`

**Discovery**: Loaded adapters appear in`/v1/models`

**KV-aware routing**: Route requests to workers with the matching adapter and cached prefix blocks; validated with vLLM**Kubernetes native**: Manage adapters declaratively through the`DynamoModel`

CRD; documented for vLLM

## Backend Support

See the [feature support matrix](https://docs.nvidia.com/dynamo/reference/compatibility#feature-support) for the backend and interaction matrices.

###### Architecture


**Rust core**(`lib/llm/src/lora/`

): Downloading, caching, and validation**Python manager**(`components/src/dynamo/common/lora/`

): Custom source support**Worker handlers**(`components/src/dynamo/vllm/handlers.py`

and`components/src/dynamo/sglang/request_handlers/handler_base.py`

): Backend load/unload and inference integration

## Serve a LoRA Adapter

The following Kubernetes and local workflows use vLLM. For the aggregated SGLang workflow, see [Serve a LoRA Adapter with SGLang](https://docs.nvidia.com/dynamo/dev/cli/operations/lo-ra-adapters#serve-a-lora-adapter-with-sglang).

Keep `DYN_SYSTEM_PORT`

on a trusted administrative network. The system API retrieves and loads model artifacts from configured URI sources; do not expose it to untrusted clients.

###### Kubernetes

###### Local

### Prerequisites

- A Kubernetes cluster with the Dynamo Platform installed and a vLLM runtime image
- A LoRA adapter compatible with your base model
- For
`s3://`

sources: AWS credentials in a Kubernetes Secret

Full manifests and MinIO setup: [Kubernetes LoRA deployment example](https://github.com/ai-dynamo/dynamo/tree/main/examples/backends/vllm/deploy/lora).

### Deploy a LoRA-enabled worker

Enable LoRA on the **worker**: set LoRA and system API environment variables, and pass vLLM LoRA flags in `args:`

. `DYN_SYSTEM_ENABLED`

and `DYN_SYSTEM_PORT`

expose load/unload on the worker system port.

Adapted from the [ agg_lora.yaml example](https://github.com/ai-dynamo/dynamo/blob/main/examples/backends/vllm/deploy/lora/agg_lora.yaml):

Apply and wait for readiness:

**Worker environment variables**

For `s3://`

sources, Dynamo uses the standard AWS credential provider chain, including environment variables, shared configuration and credentials files, web identity, container credentials, and Amazon EC2 instance metadata. Endpoint precedence is `AWS_ENDPOINT_URL_S3`

, the active profile’s S3 service endpoint, `AWS_ENDPOINT_URL`

, the active profile’s generic `endpoint_url`

, then the legacy `AWS_ENDPOINT`

fallback.

**vLLM worker arguments**

`--max-lora-rank`

to at least your adapter’s rank. A lower value causes load failures.###### S3 or MinIO credentials on the worker


Mount shared AWS files and set `AWS_PROFILE`

, or store environment credentials in a Kubernetes Secret. Set non-secret endpoint and region values inline:

### Load an adapter

Use a `DynamoModel`

CRD for declarative, cluster-native loading. It discovers worker endpoints for `baseModelName`

, creates a Service, and calls the load API on each pod.

Verify readiness:

See the [DynamoModel API reference](https://docs.nvidia.com/dynamo/dev/reference/api/kubernetes/full-api-reference#dynamomodel) for the CRD fields.

###### Load imperatively with the worker system API


Port-forward the worker system port and POST to `/v1/loras`

:

List loaded adapters with `GET /v1/loras`

. Unload with `DELETE /v1/loras/{lora_name}`

.

## Serve a LoRA Adapter with SGLang

**Experimental.** The repository validates dynamic loading, discovery, and inference for aggregated SGLang workers. Unloading is implemented but not exercised by an end-to-end test. Prefill and decode lifecycle registration has unit coverage, but disaggregated SGLang LoRA and feature pairings such as KV-aware routing are not end-to-end validated. The Kubernetes workflow above and the adapter-aware routing demo below are vLLM-specific.

### Prepare the adapter

Start MinIO and upload the example adapter:

See the [SGLang LoRA example](https://github.com/ai-dynamo/dynamo/tree/main/examples/backends/sglang/launch/lora) for the scripts and configurable environment variables.

## KV Cache-Aware LoRA Routing

This section describes the validated vLLM path. KV-aware routing with SGLang LoRA remains experimental because the combined path is not end-to-end validated.

With `DYN_LORA_ENABLED`

, only KV, random, and round-robin routing are LoRA-aware.
Direct, power-of-two, least-loaded, and device-aware-weighted modes fail startup.
Session affinity with LoRA is supported only in KV mode; random and round-robin
plus affinity are rejected.

###### How LoRA-aware KV routing works


When KV-aware routing is enabled, the router accounts for LoRA adapter identity when computing block hashes:

**Distinct hash spaces per adapter**: Blocks cached under adapter`A`

are never confused with adapter`B`

or the base model, even when token sequences match. The adapter name is mixed into the`LocalBlockHash`

computation.**Prefix sharing within the same adapter**: Requests targeting the same LoRA adapter reuse KV prefix blocks like base-model requests.**No extra configuration**: The LoRA name propagates through KV events (`BlockStored`

) from the engine to the router. The router uses the`lora_name`

field to route requests to workers with matching cached blocks.

This works across the publisher pipeline, the KV consolidator, and the routing query path.

For a local two-worker demo with KV-aware routing, run [ agg_lora_router.sh](https://github.com/ai-dynamo/dynamo/blob/main/examples/backends/vllm/launch/lora/agg_lora_router.sh) and load the adapter on both worker system ports.

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
- For vLLM disaggregated serving, load the adapter on both prefill and decode workers
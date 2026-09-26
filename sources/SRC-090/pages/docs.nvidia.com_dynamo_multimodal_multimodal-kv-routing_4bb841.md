source: https://docs.nvidia.com/dynamo/multimodal/multimodal-kv-routing
lastmod: 2026-09-24T19:58:16.636Z

# Multimodal KV Routing

Include multimodal identity in the router’s combined cache-and-load cost

## Overview

Multimodal KV routing extends Dynamo’s KV-aware router to account for image content when calculating cache overlap. The frontend assigns each image a stable hash and includes its identity in the routing view of the prompt.

When an image appears again, its identity contributes to each worker’s KV overlap. The router balances that cache credit against projected prefill and decode load, so the worker with the largest overlap does not necessarily win when it is busy. Cache-aware placement increases prefix reuse without abandoning load balancing.

The KV cache stores attention key/value state so a worker can skip repeated prefill work. The embedding cache stores vision encoder outputs so the encoder can skip repeated image processing. You can use both features together. See [Embedding Cache](https://docs.nvidia.com/dynamo/multimodal/embedding-cache).

## When to Use

Use multimodal KV routing when:

- Multiple backend workers serve multimodal requests.
- Images repeat across requests, such as product photos or shared reference images.
- You want to maximize KV cache reuse for multimodal content.

Single-worker deployments do not need routing, and workloads with entirely unique images receive little image-specific cache benefit.

## How It Works

The routing flow in general has three steps:

- The frontend computes a stable identity for each image.
- The frontend represents the image in a routing-only token view that matches the backend’s cache identity.
- The KV router includes that overlap in its combined cache-and-load score, selects the lowest-cost eligible worker, and forwards the same image identity.

By default, an HTTP image’s identity hashes the exact URL bytes, including its
query string. Reusing the identical URL produces the same identity, but two URLs
for the same image bytes do not. Enable `--frontend-decoding`

when you need
content-stable identity across URLs; the frontend then hashes decoded image
content. Data URLs follow the same rule: the default path hashes the full data
URI string, while frontend decoding hashes the decoded bytes.

###### vLLM

###### SGLang

###### TensorRT-LLM

vLLM provides two routing paths. Use the default Rust frontend for supported model families when you want minimal frontend processing. Use the Python chat processor when you need vLLM’s broader model support or want the frontend to preprocess images and transfer the processed inputs to workers.

**Default Rust frontend**

The frontend calculates only the image identity and routing token layout. The selected worker still runs the model’s multimodal processor. This path has lower frontend overhead, but multimodal routing depends on the model being registered with Dynamo’s Rust processor registry.

**Alternative: Python chat processor**

With `--dyn-chat-processor vllm`

, the frontend runs vLLM’s full multimodal processor. It supports models known to vLLM without requiring a Dynamo Rust processor specification and can transfer processed inputs through shared memory or NIXL. This shifts preprocessing and transfer work to the frontend.

## Launch

###### vLLM

###### SGLang

###### TensorRT-LLM

Use the Python chat processor when you need vLLM’s model-native multimodal processor or want to transfer processed multimodal inputs from the frontend. Otherwise, use the default Rust frontend.

**Default Rust frontend**

**Alternative: Python chat processor**

See [vLLM Multimodal](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/vllm-multimodal#multimodal-kv-routing) for model support, hashing behavior, transfer modes, and configuration.
source: https://docs.nvidia.com/dynamo/zh-CN/v1.1.1/integrations/flex-kv
lastmod: 2026-09-23T23:30:39.914Z

# FlexKV

## Introduction

[FlexKV](https://github.com/taco-project/FlexKV) is a scalable, distributed runtime for KV cache offloading developed by Tencent Cloud’s TACO team and NVIDIA in collaboration with the community. It acts as a unified KV caching layer for inference engines like SGLang, TensorRT-LLM, and vllm.

### Key Features

**Multi-level caching**: CPU memory, local SSD, and scalable storage (cloud storage) for KV cache offloading**Distributed KV cache reuse**: Share KV cache across multiple nodes using distributed RadixTree**High-performance I/O**: Supports io_uring and GPU Direct Storage (GDS) for accelerated data transfer**Asynchronous operations**: Get and put operations can overlap with computation through prefetching

## Prerequisites

**Dynamo installed**with vLLM support**Infrastructure services running**:**FlexKV installed**:**Optional: SSD offloading dependencies**(only required for CPU + SSD tiered offloading):

## Quick Start

### Enable FlexKV

Set the `DYNAMO_USE_FLEXKV`

environment variable and use the `--kv-transfer-config`

flag:

## Aggregated Serving

### Basic Setup

### With KV-Aware Routing

For multi-worker deployments with KV-aware routing to maximize cache reuse:

## Disaggregated Serving


Note:Disaggregated FlexKV serving is experimental. The prefill worker must use`PdConnector`

with two sub-connectors:`FlexKVConnectorV1`

(KV cache offloading) and`NixlConnector`

(P/D KV transfer). Using`FlexKVConnectorV1`

alone as the top-level connector in disaggregated mode isnot supportedand will result in a`TypeError`

.

FlexKV can be used with disaggregated prefill/decode serving. The prefill worker uses FlexKV for KV cache offloading, while NIXL handles KV transfer between prefill and decode workers. The `PdConnector`

wraps both connectors so they work together.

### Supported connector configuration

You can also use the provided launch script directly:

## Configuration

### Environment Variables

### CPU-Only Offloading

For simple CPU memory offloading:

### CPU + SSD Tiered Offloading

For multi-tier offloading with SSD storage, create a configuration file:

### Configuration Options


Note:For full configuration options, see the[FlexKV Configuration Reference].

## Distributed KV Cache Reuse

FlexKV supports distributed KV cache reuse to share cache across multiple nodes. This enables:

**Distributed RadixTree**: Each node maintains a local snapshot of the global index**Lease Mechanism**: Ensures data validity during cross-node transfers**RDMA-based Transfer**: Uses Mooncake Transfer Engine for high-performance KV cache transfer

For setup instructions, see the [FlexKV Distributed Reuse Guide](https://github.com/taco-project/FlexKV/blob/main/docs/dist_reuse/README_en.md).

## Architecture

FlexKV consists of three core modules:

### StorageEngine

Initializes the three-level cache (GPU → CPU → SSD/Cloud). It groups multiple tokens into blocks and stores KV cache at the block level, maintaining the same KV shape as in GPU memory.

### GlobalCacheEngine

The control plane that determines data transfer direction and identifies source/destination block IDs. Includes:

- RadixTree for prefix matching
- Memory pool to track space usage and trigger eviction

### TransferEngine

The data plane that executes data transfers:

- Multi-threading for parallel transfers
- High-performance I/O (io_uring, GDS)
- Asynchronous operations overlapping with computation
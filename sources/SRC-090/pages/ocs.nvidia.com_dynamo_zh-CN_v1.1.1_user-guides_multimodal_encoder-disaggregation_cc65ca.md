source: https://docs.nvidia.com/dynamo/zh-CN/v1.1.1/user-guides/multimodal/encoder-disaggregation
lastmod: 2026-09-23T23:30:39.914Z

# Encoder Disaggregation

## Overview

Encoder disaggregation separates the vision encoder from the prefill/decode pipeline into its own worker. Instead of running image encoding inline, a dedicated encode worker handles media processing and transfers the resulting embeddings to downstream workers via NIXL (RDMA).

This enables:

- Independent scaling of encode workers based on vision workload
- Reduced GPU memory pressure on prefill/decode workers
- Better GPU utilization by matching worker counts to actual bottlenecks

## When to Use

Use encoder disaggregation when:

- Vision encoding is a bottleneck and you need to scale encoders independently of LLM workers
- You want to run the vision encoder on different hardware (e.g., smaller GPUs for encoding, larger GPUs for LLM inference)
- Your deployment handles high volumes of multimodal requests and encoding throughput is limiting

For simple deployments or development/testing, the aggregated (EPD) pattern is easier to set up.

## Support Matrix

## Deployment Patterns

**E/PD** — Separate encoder, combined prefill+decode:

The encode worker runs the vision model and transfers embeddings via NIXL to a combined prefill+decode worker.

**E/P/D** — All stages separate:

Full disaggregation with separate workers for each stage. The encode worker transfers embeddings to the prefill worker, which then transfers KV cache to the decode worker.

## Launching

### vLLM

### TRT-LLM

### SGLang

See the backend-specific documentation ([vLLM](https://github.com/ai-dynamo/dynamo/blob/v1.1.1/docs/features/multimodal/multimodal-vllm.md), [TRT-LLM](https://github.com/ai-dynamo/dynamo/blob/v1.1.1/docs/features/multimodal/multimodal-trtllm.md), [SGLang](https://github.com/ai-dynamo/dynamo/blob/v1.1.1/docs/features/multimodal/multimodal-sglang.md)) for full configuration details and component flags.
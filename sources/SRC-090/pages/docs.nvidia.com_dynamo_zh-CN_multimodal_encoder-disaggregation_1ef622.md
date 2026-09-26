source: https://docs.nvidia.com/dynamo/zh-CN/multimodal/encoder-disaggregation
lastmod: 2026-09-24T19:58:16.636Z

# Encoder Disaggregation

Separate vision encoding into a dedicated worker for independent scaling

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

## Deployment Patterns

## Launching

###### vLLM

###### SGLang

###### TensorRT-LLM

See the backend-specific documentation ([vLLM](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/vllm-multimodal), [TRT-LLM](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/tensor-rt-llm/tensorrt-llm-multimodal), [SGLang](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/sg-lang/sglang-multimodal)) for full configuration details and component flags.
source: https://docs.vllm.ai/en/latest/models/extensions/instanttensor/
lastmod: 2026-09-23

# Loading Model Weights with InstantTensor[¶](https://docs.vllm.ai#loading-model-weights-with-instanttensor)

InstantTensor accelerates loading Safetensors weights on CUDA devices through distributed loading, pipelined prefetching, and direct I/O. InstantTensor also supports GDS (GPUDirect Storage) when available. For more details, see the [InstantTensor GitHub repository](https://github.com/scitix/InstantTensor).

## Installation[¶](https://docs.vllm.ai#installation)

## Use InstantTensor in vLLM[¶](https://docs.vllm.ai#use-instanttensor-in-vllm)

Add `--load-format instanttensor`

as a command-line argument.

For example:

## Benchmarks[¶](https://docs.vllm.ai#benchmarks)

| Model | GPU | Backend | Load Time (s) | Throughput (GB/s) | Speedup |
|---|---|---|---|---|---|
| Qwen3-30B-A3B | 1*H200 | Safetensors | 57.4 | 1.1 | 1x |
| Qwen3-30B-A3B | 1*H200 | InstantTensor | 1.77 | 35 | 32.4x |
| DeepSeek-R1 | 8*H200 | Safetensors | 160 | 4.3 | 1x |
| DeepSeek-R1 | 8*H200 | InstantTensor | 15.3 | 45 | 10.5x |

For the full benchmark results, see [https://github.com/scitix/InstantTensor/blob/main/docs/benchmark.md](https://github.com/scitix/InstantTensor/blob/main/docs/benchmark.md).
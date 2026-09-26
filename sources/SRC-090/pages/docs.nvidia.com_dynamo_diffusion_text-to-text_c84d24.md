source: https://docs.nvidia.com/dynamo/diffusion/text-to-text
lastmod: 2026-09-24T19:58:16.636Z

Text-to-Text (LLM Diffusion)


Text-to-Text (LLM Diffusion)

Generate text through iterative refinement with SGLang diffusion language models

Diffusion Language Models generate text through iterative refinement rather than autoregressive token-by-token generation. The model starts with masked tokens and progressively replaces them with predictions, refining low-confidence tokens each step. See the [Diffusion Overview](https://docs.nvidia.com/dynamo/diffusion/overview) for backend setup.

LLM diffusion is auto-detected: when `--dllm-algorithm`

is set, the worker automatically uses `DiffusionWorkerHandler`

without needing a separate flag. For more details on diffusion algorithms, see the [SGLang Diffusion Language Models documentation](https://docs.sglang.io/docs/supported-models/diffusion_language_models).

## Launch

See the [launch script](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/examples/backends/sglang/launch/diffusion_llada.sh) for configuration options.
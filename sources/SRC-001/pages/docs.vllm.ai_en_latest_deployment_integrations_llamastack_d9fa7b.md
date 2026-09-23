source: https://docs.vllm.ai/en/latest/deployment/integrations/llamastack/
lastmod: 2026-09-23

# Llama Stack[¶](https://docs.vllm.ai#llama-stack)

vLLM is also available via [Llama Stack](https://github.com/llamastack/llama-stack).

To install Llama Stack, run

## Inference using OpenAI-Compatible API[¶](https://docs.vllm.ai#inference-using-openai-compatible-api)

Then start the Llama Stack server and configure it to point to your vLLM server with the following settings:

Please refer to [this guide](https://llama-stack.readthedocs.io/en/latest/providers/inference/remote_vllm.html) for more details on this remote vLLM provider.

## Inference using Embedded vLLM[¶](https://docs.vllm.ai#inference-using-embedded-vllm)

An [inline provider](https://github.com/llamastack/llama-stack/tree/main/llama_stack/providers/inline/inference) is also available. This is a sample of configuration using that method:
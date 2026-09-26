source: https://docs.vllm.ai/en/latest/contributing/model/
lastmod: 2026-09-24

# Summary[¶](https://docs.vllm.ai#summary)

Important

Many decoder language models can now be automatically loaded using the [Transformers modeling backend](https://docs.vllm.ai/models/supported_models/#transformers) without having to implement them in vLLM. See if `vllm serve <model>`

works first!

vLLM models are specialized [PyTorch](https://pytorch.org/) models that take advantage of various [features](https://docs.vllm.ai/features/#compatibility-matrix) to optimize their performance.

The complexity of integrating a model into vLLM depends heavily on the model's architecture. The process is considerably straightforward if the model shares a similar architecture with an existing model in vLLM. However, this can be more complex for models that include new operators (e.g., a new attention mechanism).

Read through these pages for a step-by-step guide:

Tip

If you are encountering issues while integrating your model into vLLM, feel free to open a [GitHub issue](https://github.com/vllm-project/vllm/issues) or ask on our [developer slack](https://slack.vllm.ai). We will be happy to help you out!
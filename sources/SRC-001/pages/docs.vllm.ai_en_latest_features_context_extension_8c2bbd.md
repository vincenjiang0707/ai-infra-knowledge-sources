source: https://docs.vllm.ai/en/latest/features/context_extension/
lastmod: 2026-09-24

# Context Extension[¶](https://docs.vllm.ai#context-extension)

Note

The `--rope-scaling`

parameter used in older versions of vLLM is no longer supported. Please use the `--hf-overrides`

method with `rope_parameters`

instead.

This directory contains examples for extending the context length of models using vLLM.

## Offline Inference Example[¶](https://docs.vllm.ai#offline-inference-example)

The [ context_extension.py](https://github.com/vllm-project/vllm/blob/main/examples/features/context_extension/context_extension_offline.py) script demonstrates how to extend the context length of a Qwen model using the YARN method (rope_parameters) and run a simple chat example.

### Usage[¶](https://docs.vllm.ai#usage)

## OpenAI Online Method[¶](https://docs.vllm.ai#openai-online-method)

You can also use vLLM's OpenAI-compatible API to serve models with extended context length.

### Usage[¶](https://docs.vllm.ai#usage_1)

Run the vLLM server with the following command to extend the context length using YARN:

vllm serve Qwen/Qwen3-0.6B \
--hf-overrides '{"rope_parameters": {"factor": 4.0, "original_max_position_embeddings": 32768, "rope_theta": 1000000, "rope_type": "yarn"}}' \
--max-model-len 131072


### Client Example[¶](https://docs.vllm.ai#client-example)

After starting the server, you can use the OpenAI Python client to interact with it:

from openai import OpenAI
client = OpenAI(
base_url="http://localhost:8000/v1",
api_key="token-abc123" # Dummy API key, required by the client
)
response = client.chat.completions.create(
model="Qwen/Qwen3-0.6B",
messages=[
{"role": "system", "content": "You are a helpful assistant"},
{"role": "user", "content": "Hello"}
],
max_tokens=128,
temperature=0.8,
top_p=0.95
)
print(response.choices[0].message.content)


### Key Parameters[¶](https://docs.vllm.ai#key-parameters)

The available parameters depend on the `rope_type`

you choose. For detailed information about all supported RoPE types and their specific parameters, please refer to the [Hugging Face Transformers RoPE documentation](https://huggingface.co/docs/transformers/main/en/internal/rope_utils#transformers.RopeParameters).

Common parameters include:

`rope_type`

: The type of RoPE implementation (e.g., "yarn", "linear", "dynamic")`factor`

: The factor by which to extend the context length`original_max_position_embeddings`

: The original maximum position embeddings of the model

The following parameters are specific to vLLM:

`max_model_len`

: The new maximum sequence length after extension (original * factor). Used for KV cache pre‑allocation and request limit at serving time.
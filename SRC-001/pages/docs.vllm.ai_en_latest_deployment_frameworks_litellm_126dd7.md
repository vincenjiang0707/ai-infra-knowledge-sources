source: https://docs.vllm.ai/en/latest/deployment/frameworks/litellm/
lastmod: 2026-09-23

# LiteLLM[¶](https://docs.vllm.ai#litellm)

[LiteLLM](https://github.com/BerriAI/litellm) call all LLM APIs using the OpenAI format [Bedrock, Huggingface, VertexAI, TogetherAI, Azure, OpenAI, Groq etc.]

LiteLLM manages:

- Translate inputs to provider's
`completion`

,`embedding`

, and`image_generation`

endpoints [Consistent output](https://docs.litellm.ai/docs/completion/output), text responses will always be available at`['choices'][0]['message']['content']`

- Retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) -
[Router](https://docs.litellm.ai/docs/routing) - Set Budgets & Rate limits per project, api key, model
[LiteLLM Proxy Server (LLM Gateway)](https://docs.litellm.ai/docs/simple_proxy)

And LiteLLM supports all models on VLLM.

## Prerequisites[¶](https://docs.vllm.ai#prerequisites)

Set up the vLLM and litellm environment:

## Deploy[¶](https://docs.vllm.ai#deploy)

### Chat completion[¶](https://docs.vllm.ai#chat-completion)

-
Start the vLLM server with the supported chat completion model, e.g.

-
Call it with litellm:


## Code

import litellm
messages = [{"content": "Hello, how are you?", "role": "user"}]
# hosted_vllm is prefix key word and necessary
response = litellm.completion(
model="hosted_vllm/qwen/Qwen1.5-0.5B-Chat", # pass the vllm model name
messages=messages,
api_base="http://{your-vllm-server-host}:{your-vllm-server-port}/v1",
temperature=0.2,
max_tokens=80,
)
print(response)


### Embeddings[¶](https://docs.vllm.ai#embeddings)

-
Start the vLLM server with the supported embedding model, e.g.

-
Call it with litellm:


from litellm import embedding
import os
os.environ["HOSTED_VLLM_API_BASE"] = "http://{your-vllm-server-host}:{your-vllm-server-port}/v1"
# hosted_vllm is prefix key word and necessary
# pass the vllm model name
embedding = embedding(model="hosted_vllm/BAAI/bge-base-en-v1.5", input=["Hello world"])
print(embedding)


For details, see the tutorial [Using vLLM in LiteLLM](https://docs.litellm.ai/docs/providers/vllm).
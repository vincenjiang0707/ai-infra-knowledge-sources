source: https://docs.vllm.ai/en/latest/deployment/frameworks/crusoe/
lastmod: 2026-09-24

# Crusoe[¶](https://docs.vllm.ai#crusoe)

[Crusoe](https://crusoe.ai/) provides Managed Inference, an OpenAI-compatible API for open-weight models, powered by vLLM. Because the service speaks the OpenAI API, code written against a self-hosted vLLM server works against Crusoe endpoints without changes.

## Prerequisites[¶](https://docs.vllm.ai#prerequisites)

- A Crusoe account
- An Inference API key, created in the
[Crusoe Console](https://console.crusoe.ai/)under**Security > Inference API Key**

Set the key as an environment variable:

## Using the OpenAI SDK[¶](https://docs.vllm.ai#using-the-openai-sdk)

Point the OpenAI client at the Crusoe endpoint:

import os
from openai import OpenAI
client = OpenAI(
base_url="https://api.inference.crusoecloud.com/v1",
api_key=os.environ["CRUSOE_API_KEY"],
)
response = client.chat.completions.create(
model="zai/GLM-5.2",
messages=[{"role": "user", "content": "Hello, how are you?"}],
)
print(response.choices[0].message.content)


## Verifying with curl[¶](https://docs.vllm.ai#verifying-with-curl)

Command

## Available models[¶](https://docs.vllm.ai#available-models)

List the current model catalog:

For the full list of available models and API details, see the [Crusoe Managed Inference docs](https://docs.crusoecloud.com/managed-inference/overview).
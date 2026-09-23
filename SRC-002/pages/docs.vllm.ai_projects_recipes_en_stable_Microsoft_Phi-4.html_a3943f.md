source: https://docs.vllm.ai/projects/recipes/en/stable/Microsoft/Phi-4.html
lastmod: 2026-04-27

# Phi-4 Usage Guide[¶](https://docs.vllm.ai#phi-4-usage-guide)

This guide describes how to run **Microsoft Phi-4** models on GPU using vLLM.

The Phi-4 family includes several lightweight, open models from Microsoft. These models can process text and, in some variants, multimodal inputs like images, to generate text outputs. They come with a 128K token context length.

## GPU Deployment[¶](https://docs.vllm.ai#gpu-deployment)

### Installing vLLM[¶](https://docs.vllm.ai#installing-vllm)

### Running Phi-4-mini-instruct on a Single GPU[¶](https://docs.vllm.ai#running-phi-4-mini-instruct-on-a-single-gpu)

# Start server on a single GPU
vllm serve microsoft/Phi-4-mini-instruct \
--host 0.0.0.0 \
--max-model-len 4000


## Performance Metrics[¶](https://docs.vllm.ai#performance-metrics)

### Benchmarking[¶](https://docs.vllm.ai#benchmarking)

vllm bench serve \
--model microsoft/Phi-4-mini-instruct \
--dataset-name random \
--random-input-len 2000 \
--random-output-len 512 \
--num-prompts 100


## Querying with OpenAI API Client[¶](https://docs.vllm.ai#querying-with-openai-api-client)

from openai import OpenAI
client = OpenAI(
api_key="EMPTY",
base_url="http://localhost:8000/v1",
timeout=3600
)
messages = [
{
"role": "user",
"content": "write short story"
}
]
response = client.chat.completions.create(
model="microsoft/Phi-4-mini-instruct",
messages=messages,
temperature=0.0
)
print("Generated text:", response.choices[0].message.content)


### Multimodal Example (Image + Text)[¶](https://docs.vllm.ai#multimodal-example-image-text)

[!NOTE]

This model’s multimodality support is implemented via LoRA modules, and --trust-remote-code is required to enable the execution of those components.

To run this example, you must start the server with the`microsoft/Phi-4-multimodal-instruct`

model:

from openai import OpenAI
client = OpenAI(
api_key="EMPTY",
base_url="http://localhost:8000/v1",
timeout=3600
)
# Multimodal input: text + image
messages = [
{
"role": "user",
"content": [
{
"type": "text",
"text": "What is shown in this image? Describe it in detail."
},
{
"type": "image_url",
"image_url": {
"url": "https://example.com/image.jpg"
}
}
]
}
]
response = client.chat.completions.create(
model="microsoft/Phi-4-multimodal-instruct",
messages=messages,
temperature=0.0
)
print("Generated text:", response.choices[0].message.content)


## Available Phi-4 Variants[¶](https://docs.vllm.ai#available-phi-4-variants)

The Phi-4 series includes multiple model variants, all compatible with the same vLLM serving commands shown in this guide:

-
**microsoft/Phi-4-mini-instruct**

Instruction-tuned variant optimized for conversational tasks -
**microsoft/Phi-4-mini-reasoning**

Optimized for reasoning tasks -
**microsoft/Phi-4-reasoning**

Advanced reasoning capabilities -
**microsoft/Phi-4-multimodal-instruct**

Multimodal instruction-following model
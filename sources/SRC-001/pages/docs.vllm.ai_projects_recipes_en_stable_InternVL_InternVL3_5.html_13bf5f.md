source: https://docs.vllm.ai/projects/recipes/en/stable/InternVL/InternVL3_5.html
lastmod: 2026-04-27

# InternVL3.5 Usage Guide[¶](https://docs.vllm.ai#internvl35-usage-guide)

[InternVL3.5](https://github.com/OpenGVLab/InternVL) is a vision-language model developed by Shanghai AI Laboratory.
This guide describes how to deploy InternVL3.5 with vLLM and provide some simple examples of how to use the API.

## Installing vLLM[¶](https://docs.vllm.ai#installing-vllm)

## Installing vLLM (For AMD ROCm: MI300x/MI325x/MI355x)[¶](https://docs.vllm.ai#installing-vllm-for-amd-rocm-mi300xmi325xmi355x)

⚠️ The vLLM wheel for ROCm is compatible with Python 3.12, ROCm 7.0, and glibc >= 2.35. If your environment is incompatible, please use docker flow in [vLLM](https://vllm.ai/)

## Launching InternVL3.5 with vLLM[¶](https://docs.vllm.ai#launching-internvl35-with-vllm)

## Launching InternVL3.5 with vLLM on AMD GPUs[¶](https://docs.vllm.ai#launching-internvl35-with-vllm-on-amd-gpus)

* You can set `export VLLM_ROCM_USE_AITER=1`

for Better Performance on AMD GPUs. The default is `export VLLM_ROCM_USE_AITER=0`

## API Usage Examples[¶](https://docs.vllm.ai#api-usage-examples)

### Chat with Pure-Text[¶](https://docs.vllm.ai#chat-with-pure-text)

from openai import OpenAI
client = OpenAI(api_key='', base_url='http://0.0.0.0:8000/v1')
model_name = client.models.list().data[0].id
response = client.chat.completions.create(
model=model_name,
messages=[{
'role':
'user',
'content': [{
'type': 'text',
'text': '9.11 and 9.8, which is greater?',
}],
}],
temperature=0.6,
top_p=0.95,
)
print(response.choices[0].message.content)


### Chat with Image[¶](https://docs.vllm.ai#chat-with-image)

#### Single Image[¶](https://docs.vllm.ai#single-image)

from openai import OpenAI
client = OpenAI(api_key='', base_url='http://0.0.0.0:8000/v1')
model_name = client.models.list().data[0].id
response = client.chat.completions.create(
model=model_name,
messages=[{
'role':
'user',
'content': [{
'type': 'text',
'text': 'Describe the image.',
}, {
'type': 'image_url',
'image_url': {'url': 'https://raw.githubusercontent.com/open-mmlab/mmdeploy/main/tests/data/tiger.jpeg'},
}],
}],
temperature=0.0
)
print(response.choices[0].message.content)


#### Multiple Images[¶](https://docs.vllm.ai#multiple-images)

from openai import OpenAI
client = OpenAI(api_key='', base_url='http://0.0.0.0:8000/v1')
model_name = client.models.list().data[0].id
response = client.chat.completions.create(
model=model_name,
messages=[{
'role':
'user',
'content': [{
'type': 'text',
'text': 'Describe these two images.',
}, {
'type': 'image_url',
'image_url': {'url': 'https://raw.githubusercontent.com/open-mmlab/mmdeploy/main/demo/resources/human-pose.jpg'},
}, {
'type': 'image_url',
'image_url': {'url': 'https://raw.githubusercontent.com/open-mmlab/mmdeploy/main/demo/resources/det.jpg'},
}],
}],
temperature=0.0
)
print(response.choices[0].message.content)


### Thinking Mode[¶](https://docs.vllm.ai#thinking-mode)

To enable thinking mode, please set the system prompt to our **Thinking System Prompt**. When enabling thinking mode, we recommend setting `temperature=0.6`

to mitigate undesired repetition.

from openai import OpenAI
client = OpenAI(api_key='', base_url='http://0.0.0.0:8000/v1')
model_name = client.models.list().data[0].id
THINKING_SYSTEM_PROMPT = """
You are an AI assistant that rigorously follows this response protocol:
1. First, conduct a detailed analysis of the question. Consider different angles, potential solutions, and reason through the problem step-by-step. Enclose this entire thinking process within <think> and </think> tags.
2. After the thinking section, provide a clear, concise, and direct answer to the user's question. Separate the answer from the think section with a newline.
Ensure that the thinking process is thorough but remains focused on the query. The final answer should be standalone and not reference the thinking section.
""".strip()
response = client.chat.completions.create(
model=model_name,
messages=[{
'role': 'system',
'content': [{
'type': 'text',
'text': THINKING_SYSTEM_PROMPT,
}],
}, {
'role': 'user',
'content': [{
'type': 'text',
'text': '9.11 and 9.8, which is greater?',
}],
}],
temperature=0.6,
top_p=0.95,
)
print(response.choices[0].message.content)
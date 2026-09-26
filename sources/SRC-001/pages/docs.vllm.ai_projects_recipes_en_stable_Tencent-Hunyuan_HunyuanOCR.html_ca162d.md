source: https://docs.vllm.ai/projects/recipes/en/stable/Tencent-Hunyuan/HunyuanOCR.html
lastmod: 2026-04-27

# HunyuanOCR Usage Guide[¶](https://docs.vllm.ai#hunyuanocr-usage-guide)

## Introduction[¶](https://docs.vllm.ai#introduction)

[HunyuanOCR](https://huggingface.co/tencent/HunyuanOCR) stands as a leading end-to-end OCR expert VLM powered by Hunyuan's native multimodal architecture. In this guide, we demonstrate how to set up HunyuanOCR for online OCR serving with OpenAI compatible API server.

## Installing vLLM[¶](https://docs.vllm.ai#installing-vllm)

## Deploying HunyuanOCR[¶](https://docs.vllm.ai#deploying-hunyuanocr)

## Querying with OpenAI API Client[¶](https://docs.vllm.ai#querying-with-openai-api-client)

from openai import OpenAI
client = OpenAI(
api_key="EMPTY",
base_url="http://localhost:8000/v1",
timeout=3600
)
messages = [
{"role": "system", "content": ""},
{
"role": "user",
"content": [
{
"type": "image_url",
"image_url": {
"url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/chat-ui/tools-dark.png"
}
},
{
"type": "text",
"text": (
"Extract all information from the main body of the document image "
"and represent it in markdown format, ignoring headers and footers."
"Tables should be expressed in HTML format, formulas in the document "
"should be represented using LaTeX format, and the parsing should be "
"organized according to the reading order."
)
}
]
}
]
response = client.chat.completions.create(
model="tencent/HunyuanOCR",
messages=messages,
temperature=0.0,
extra_body={
"top_k": 1,
"repetition_penalty": 1.0
},
)
print(f"Generated text: {response.choices[0].message.content}")


## Configuration Tips[¶](https://docs.vllm.ai#configuration-tips)

- Use greedy sampling (i.e., temperature=0.0) or sampling with low temperature for the optimal OCR performance.
- Unlike multi-turn chat use cases, we do not expect OCR tasks to benefit significantly from prefix caching or image reuse, therefore it's recommended to turn off these features to avoid unnecessary hashing and caching.
- Depending on your hardware capability, adjust
`max_num_batched_tokens`

for better throughput performance. - Check out the official
[HunyuanOCR documentation](https://huggingface.co/tencent/HunyuanOCR#%F0%9F%92%AC-application-oriented-prompts)for more application-oriented prompts for various document parsing tasks.
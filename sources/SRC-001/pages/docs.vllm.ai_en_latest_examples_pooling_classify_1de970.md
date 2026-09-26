source: https://docs.vllm.ai/en/latest/examples/pooling/classify/
lastmod: 2026-09-24

# Classify[¶](https://docs.vllm.ai#classify)

Source [https://github.com/vllm-project/vllm/tree/main/examples/pooling/classify](https://github.com/vllm-project/vllm/tree/main/examples/pooling/classify).

## Classification Online[¶](https://docs.vllm.ai#classification-online)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""Example Python client for classification API using vLLM API server
NOTE:
start a supported classification model server with `vllm serve`, e.g.
vllm serve jason9693/Qwen2.5-1.5B-apeach
"""
import argparse
import pprint
import requests
headers = {"accept": "application/json", "Content-Type": "application/json"}
def parse_args():
parse = argparse.ArgumentParser()
parse.add_argument("--host", type=str, default="localhost")
parse.add_argument("--port", type=int, default=8000)
return parse.parse_args()
def main(args):
base_url = f"http://{args.host}:{args.port}"
models_url = base_url + "/v1/models"
classify_url = base_url + "/classify"
tokenize_url = base_url + "/tokenize"
response = requests.get(models_url, headers=headers)
model = response.json()["data"][0]["id"]
# /classify can accept str as input
prompts = [
"Hello, my name is",
"The president of the United States is",
"The capital of France is",
"The future of AI is",
]
payload = {
"model": model,
"input": prompts,
}
response = requests.post(classify_url, headers=headers, json=payload)
pprint.pprint(response.json())
# /classify can accept token ids as input
token_ids = []
for prompt in prompts:
response = requests.post(
tokenize_url,
json={"model": model, "prompt": prompt},
)
token_ids.append(response.json()["tokens"])
payload = {
"model": model,
"input": token_ids,
}
response = requests.post(classify_url, headers=headers, json=payload)
pprint.pprint(response.json())
if __name__ == "__main__":
args = parse_args()
main(args)


## Classification With LoRA Offline[¶](https://docs.vllm.ai#classification-with-lora-offline)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""Example of offline classification with a LoRA adapter."""
from vllm import LLM
from vllm.lora.request import LoRARequest
from vllm.transformers_utils.repo_utils import hf_api
def main():
lora_path = hf_api().snapshot_download(
repo_id="AmirMohseni/skywork-qwen3-0.6b-reward-lora"
)
llm = LLM(
model="Skywork/Skywork-Reward-V2-Qwen3-0.6B",
runner="pooling",
enable_lora=True,
max_lora_rank=8,
max_model_len=512,
)
prompt = "Which response is more helpful and correct?"
(output,) = llm.classify(
prompt,
lora_request=LoRARequest("reward-lora", 1, lora_path),
)
print(f"Prompt: {prompt!r}")
print(f"Class Probabilities: {output.outputs.probs}")
if __name__ == "__main__":
main()


## Vision Classification Online[¶](https://docs.vllm.ai#vision-classification-online)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# ruff: noqa: E501
"""Example Python client for multimodal classification API using vLLM API server
NOTE:
start a supported multimodal classification model server with `vllm serve`, e.g.
vllm serve muziyongshixin/Qwen2.5-VL-7B-for-VideoCls \
--runner pooling \
--max-model-len 5000 \
--limit-mm-per-prompt.video 1 \
--hf-overrides '{"architectures": ["Qwen2_5_VLForSequenceClassification"]}'
"""
import argparse
import pprint
import requests
from vllm.multimodal.utils import encode_image_url, fetch_image
input_text = "This product was excellent and exceeded my expectations"
image_url = "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/cat_snow.jpg"
image_base64 = {"url": encode_image_url(fetch_image(image_url))}
video_url = "https://www.bogotobogo.com/python/OpenCV_Python/images/mean_shift_tracking/slow_traffic_small.mp4"
def parse_args():
parse = argparse.ArgumentParser()
parse.add_argument("--host", type=str, default="localhost")
parse.add_argument("--port", type=int, default=8000)
return parse.parse_args()
def main(args):
base_url = f"http://{args.host}:{args.port}"
models_url = base_url + "/v1/models"
classify_url = base_url + "/classify"
response = requests.get(models_url)
model_name = response.json()["data"][0]["id"]
print("Text classification output:")
messages = [
{
"role": "assistant",
"content": "Please classify this text request.",
},
{
"role": "user",
"content": input_text,
},
]
response = requests.post(
classify_url,
json={"model": model_name, "messages": messages},
)
pprint.pprint(response.json())
print("Image url classification output:")
messages = [
{
"role": "user",
"content": [
{"type": "text", "text": "Please classify this image."},
{"type": "image_url", "image_url": {"url": image_url}},
],
}
]
response = requests.post(
classify_url,
json={"model": model_name, "messages": messages},
)
pprint.pprint(response.json())
print("Image base64 classification output:")
messages = [
{
"role": "user",
"content": [
{"type": "text", "text": "Please classify this image."},
{"type": "image_url", "image_url": image_base64},
],
}
]
response = requests.post(
classify_url,
json={"model": model_name, "messages": messages},
)
pprint.pprint(response.json())
print("Video url classification output:")
messages = [
{
"role": "user",
"content": [
{"type": "text", "text": "Please classify this video."},
{"type": "video_url", "video_url": {"url": video_url}},
],
}
]
response = requests.post(
classify_url,
json={"model": model_name, "messages": messages},
)
pprint.pprint(response.json())
if __name__ == "__main__":
args = parse_args()
main(args)
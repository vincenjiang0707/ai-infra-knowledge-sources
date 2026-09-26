source: https://docs.vllm.ai/en/latest/examples/basic/online_serving/
lastmod: 2026-09-24

# Online Serving[¶](https://docs.vllm.ai#online-serving)

Source [https://github.com/vllm-project/vllm/tree/main/examples/basic/online_serving](https://github.com/vllm-project/vllm/tree/main/examples/basic/online_serving).

## OpenAI Chat Completion Client[¶](https://docs.vllm.ai#openai-chat-completion-client)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""Example Python client for OpenAI Chat Completion using vLLM API server
NOTE: start a supported chat completion model server with `vllm serve`, e.g.
vllm serve meta-llama/Llama-2-7b-chat-hf
"""
import argparse
from openai import OpenAI
# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"
messages = [
{"role": "system", "content": "You are a helpful assistant."},
{"role": "user", "content": "Who won the world series in 2020?"},
{
"role": "assistant",
"content": "The Los Angeles Dodgers won the World Series in 2020.",
},
{"role": "user", "content": "Where was it played?"},
]
def parse_args():
parser = argparse.ArgumentParser(description="Client for vLLM API server")
parser.add_argument(
"--stream", action="store_true", help="Enable streaming response"
)
return parser.parse_args()
def main(args):
client = OpenAI(
# defaults to os.environ.get("OPENAI_API_KEY")
api_key=openai_api_key,
base_url=openai_api_base,
)
models = client.models.list()
model = models.data[0].id
# Chat Completion API
chat_completion = client.chat.completions.create(
messages=messages,
model=model,
stream=args.stream,
)
print("-" * 50)
print("Chat completion results:")
if args.stream:
for c in chat_completion:
print(c)
else:
print(chat_completion)
print("-" * 50)
if __name__ == "__main__":
args = parse_args()
main(args)


## OpenAI Completion Client[¶](https://docs.vllm.ai#openai-completion-client)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
import argparse
from openai import OpenAI
# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"
def parse_args():
parser = argparse.ArgumentParser(description="Client for vLLM API server")
parser.add_argument(
"--stream", action="store_true", help="Enable streaming response"
)
return parser.parse_args()
def main(args):
client = OpenAI(
# defaults to os.environ.get("OPENAI_API_KEY")
api_key=openai_api_key,
base_url=openai_api_base,
)
models = client.models.list()
model = models.data[0].id
# Completion API
completion = client.completions.create(
model=model,
prompt="A robot may not injure a human being",
echo=False,
n=2,
stream=args.stream,
logprobs=3,
)
print("-" * 50)
print("Completion results:")
if args.stream:
for c in completion:
print(c)
else:
print(completion)
print("-" * 50)
if __name__ == "__main__":
args = parse_args()
main(args)


## Watermark Detection Server[¶](https://docs.vllm.ai#watermark-detection-server)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""Minimal reference server for watermark detection."""
import argparse
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from vllm.tokenizers import TokenizerLike, cached_get_tokenizer
from vllm.v1.watermarking import GumbelWatermarkDetector
app = FastAPI()
tokenizer: TokenizerLike | None = None
detector: GumbelWatermarkDetector | None = None
class DetectionRequest(BaseModel):
text: str
class DetectionResponse(BaseModel):
score: float
p_value: float
num_scored_tokens: int
is_watermarked: bool
@app.post("/detect")
def detect(request: DetectionRequest) -> DetectionResponse:
assert tokenizer is not None
assert detector is not None
token_ids = tokenizer.encode(request.text, add_special_tokens=False)
result = detector.detect(token_ids)
return DetectionResponse(
score=result.score,
p_value=result.p_value,
num_scored_tokens=result.num_scored_tokens,
is_watermarked=result.is_watermarked,
)
def parse_args() -> argparse.Namespace:
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--tokenizer", required=True)
parser.add_argument("--key", required=True, type=int)
parser.add_argument("--prf", choices=("philox",), default="philox")
parser.add_argument("--context-width", type=int, default=4)
parser.add_argument("--p-value-threshold", type=float, default=0.01)
parser.add_argument("--host", default="127.0.0.1")
parser.add_argument("--port", type=int, default=8000)
return parser.parse_args()
def main(args: argparse.Namespace) -> None:
global tokenizer, detector
tokenizer = cached_get_tokenizer(args.tokenizer)
detector = GumbelWatermarkDetector(
key=args.key,
context_width=args.context_width,
p_value_threshold=args.p_value_threshold,
prf=args.prf,
)
uvicorn.run(app, host=args.host, port=args.port)
if __name__ == "__main__":
main(parse_args())
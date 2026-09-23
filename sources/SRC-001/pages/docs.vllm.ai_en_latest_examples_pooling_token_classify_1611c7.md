source: https://docs.vllm.ai/en/latest/examples/pooling/token_classify/
lastmod: 2026-09-23

# Token Classify[¶](https://docs.vllm.ai#token-classify)

Source [https://github.com/vllm-project/vllm/tree/main/examples/pooling/token_classify](https://github.com/vllm-project/vllm/tree/main/examples/pooling/token_classify).

## Forced Alignment Offline[¶](https://docs.vllm.ai#forced-alignment-offline)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# Adapted from Qwen3-ForcedAligner inference:
# https://github.com/QwenLM/Qwen3-ASR
"""Offline forced alignment example using Qwen3-ForcedAligner-0.6B.
Forced alignment takes audio and reference text as input and produces
word-level timestamps. The model predicts a time bin at each <timestamp>
token position; multiplying by ``timestamp_segment_time`` gives milliseconds.
Usage::
python forced_alignment_offline.py \
--model Qwen/Qwen3-ForcedAligner-0.6B
"""
from argparse import Namespace
import numpy as np
from vllm import LLM, EngineArgs
from vllm.utils.argparse_utils import FlexibleArgumentParser
def parse_args():
parser = FlexibleArgumentParser()
parser = EngineArgs.add_cli_args(parser)
parser.set_defaults(
model="Qwen/Qwen3-ForcedAligner-0.6B",
runner="pooling",
enforce_eager=True,
hf_overrides={"architectures": ["Qwen3ASRForcedAlignerForTokenClassification"]},
)
return parser.parse_args()
def build_prompt(words: list[str]) -> str:
"""Build the forced alignment prompt from a word list.
Format: <|audio_start|><|audio_pad|><|audio_end|>
word1<timestamp><timestamp>word2<timestamp><timestamp>...
"""
body = "<timestamp><timestamp>".join(words) + "<timestamp><timestamp>"
return f"<|audio_start|><|audio_pad|><|audio_end|>{body}"
def main(args: Namespace):
llm = LLM(**vars(args))
config = llm.llm_engine.vllm_config.model_config.hf_config
timestamp_token_id = config.timestamp_token_id
timestamp_segment_time = config.timestamp_segment_time
# Example: align these words against a 5-second audio clip
words = ["Hello", "world"]
prompt = build_prompt(words)
# Use a 5-second silent audio as placeholder (replace with real audio)
sample_rate = 16000
audio = np.zeros(sample_rate * 5, dtype=np.float32)
outputs = llm.encode(
[{"prompt": prompt, "multi_modal_data": {"audio": audio}}],
pooling_task="token_classify",
)
for output in outputs:
logits = output.outputs.data # [num_tokens, classify_num]
predictions = logits.argmax(dim=-1)
token_ids = output.prompt_token_ids
# Extract timestamps at <timestamp> positions
ts_predictions = [
pred.item() * timestamp_segment_time
for tid, pred in zip(token_ids, predictions)
if tid == timestamp_token_id
]
# Pair up start/end times per word
for i, word in enumerate(words):
start_ms = ts_predictions[i * 2]
end_ms = ts_predictions[i * 2 + 1]
print(f"{word:15s} {start_ms / 1000:.3f}s - {end_ms / 1000:.3f}s")
if __name__ == "__main__":
args = parse_args()
main(args)


## Forced Alignment Online[¶](https://docs.vllm.ai#forced-alignment-online)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# Adapted from Qwen3-ForcedAligner inference:
# https://github.com/QwenLM/Qwen3-ASR
"""Online forced alignment example using Qwen3-ForcedAligner-0.6B-hf.
Forced alignment takes audio and reference text as input and produces
word-level timestamps. The model predicts a time bin at each <timestamp>
token position; multiplying by ``timestamp_segment_time`` gives milliseconds.
This example uses STEP pooling to return logits only for <timestamp> tokens.
The ``step_tag_id`` value 151705 is this checkpoint's ``timestamp_token_id``
from its config.json.
Start the server with:
vllm serve Qwen/Qwen3-ForcedAligner-0.6B-hf \
--runner pooling \
--convert classify \
--pooler-config \
'{"tok_pooling_type":"STEP","step_tag_id":151705,"use_activation":false}' \
--enforce-eager \
--trust-request-chat-template
Then run:
python forced_alignment_online.py
"""
import argparse
import json
import mimetypes
import wave
from io import BytesIO
from pathlib import Path
from typing import Any
import numpy as np
import pybase64 as base64
import requests
import torch
from huggingface_hub import hf_hub_download
RAW_CONTENT_CHAT_TEMPLATE = "{{ messages[0]['content'] }}"
def build_prompt(words: list[str]) -> str:
"""Build the forced alignment prompt from a word list.
Format: <|audio_start|><|audio_pad|><|audio_end|>
word1<timestamp><timestamp>word2<timestamp><timestamp>...
"""
body = "<timestamp><timestamp>".join(words) + "<timestamp><timestamp>"
return f"<|audio_start|><|audio_pad|><|audio_end|>{body}"
def encode_audio_data_uri(audio_path: Path) -> str:
mime_type = mimetypes.guess_type(audio_path)[0] or "audio/wav"
audio_base64 = base64.b64encode(audio_path.read_bytes()).decode("utf-8")
return f"data:{mime_type};base64,{audio_base64}"
def encode_silent_wav_data_uri(sample_rate: int = 16000, duration_s: int = 5) -> str:
audio = np.zeros(sample_rate * duration_s, dtype=np.int16)
with BytesIO() as audio_buffer:
with wave.open(audio_buffer, "wb") as wav_file:
wav_file.setnchannels(1)
wav_file.setsampwidth(np.dtype(np.int16).itemsize)
wav_file.setframerate(sample_rate)
wav_file.writeframes(audio.tobytes())
audio_base64 = base64.b64encode(audio_buffer.getvalue()).decode("utf-8")
return f"data:audio/wav;base64,{audio_base64}"
def build_payload(model: str, prompt: str, audio_uri: str) -> dict[str, Any]:
return {
"model": model,
"messages": [
{
"role": "user",
"content": [
{"type": "text", "text": prompt},
{"type": "audio_url", "audio_url": {"url": audio_uri}},
],
}
],
"task": "token_classify",
"chat_template": RAW_CONTENT_CHAT_TEMPLATE,
}
def post_http_request(payload: dict[str, Any], api_url: str) -> requests.Response:
headers = {"User-Agent": "Test Client"}
return requests.post(api_url, headers=headers, json=payload)
def parse_response(response: requests.Response) -> dict[str, Any]:
try:
result = response.json()
except ValueError as exc:
raise RuntimeError(
f"Server returned non-JSON response: {response.text}"
) from exc
if response.status_code != 200 or "data" not in result:
raise RuntimeError(f"Server error ({response.status_code}): {result}")
return result
def load_timestamp_segment_time(model: str) -> float:
model_path = Path(model)
config_path = (
model_path / "config.json"
if model_path.exists()
else Path(hf_hub_download(repo_id=model, filename="config.json"))
)
with config_path.open() as f:
config = json.load(f)
return config["timestamp_segment_time"]
def parse_args():
parser = argparse.ArgumentParser()
parser.add_argument("--host", type=str, default="localhost")
parser.add_argument("--port", type=int, default=8000)
parser.add_argument(
"--model",
type=str,
default="Qwen/Qwen3-ForcedAligner-0.6B-hf",
)
parser.add_argument(
"--audio-path",
type=Path,
default=None,
help="Optional audio file. Defaults to a 5-second silent WAV.",
)
parser.add_argument(
"--words",
nargs="+",
default=["Hello", "world"],
help="Reference words to align against the audio.",
)
return parser.parse_args()
def main(args):
api_url = f"http://{args.host}:{args.port}/pooling"
prompt = build_prompt(args.words)
audio_uri = (
encode_audio_data_uri(args.audio_path)
if args.audio_path
else encode_silent_wav_data_uri()
)
payload = build_payload(args.model, prompt, audio_uri)
pooling_response = post_http_request(payload=payload, api_url=api_url)
result = parse_response(pooling_response)
timestamp_segment_time = load_timestamp_segment_time(args.model)
output = result["data"][0]
logits = torch.tensor(output["data"])
predictions = logits.argmax(dim=-1)
expected_timestamps = len(args.words) * 2
if len(predictions) != expected_timestamps:
raise RuntimeError(
f"Expected {expected_timestamps} timestamp predictions, "
f"but received {len(predictions)}. Check that the server was started "
"with STEP pooling."
)
ts_predictions = [
prediction.item() * timestamp_segment_time for prediction in predictions
]
for i, word in enumerate(args.words):
start_ms = ts_predictions[i * 2]
end_ms = ts_predictions[i * 2 + 1]
print(f"{word:15s} {start_ms / 1000:.3f}s - {end_ms / 1000:.3f}s")
if __name__ == "__main__":
args = parse_args()
main(args)


## NER Offline[¶](https://docs.vllm.ai#ner-offline)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# Adapted from https://huggingface.co/boltuix/NeuroBERT-NER
from argparse import Namespace
from vllm import LLM, EngineArgs
from vllm.utils.argparse_utils import FlexibleArgumentParser
def parse_args():
parser = FlexibleArgumentParser()
parser = EngineArgs.add_cli_args(parser)
# Set example specific arguments
parser.set_defaults(
model="boltuix/NeuroBERT-NER",
runner="pooling",
enforce_eager=True,
trust_remote_code=True,
)
return parser.parse_args()
def main(args: Namespace):
# Sample prompts.
prompts = [
"Barack Obama visited Microsoft headquarters in Seattle on January 2025."
]
# Create an LLM.
llm = LLM(**vars(args))
tokenizer = llm.get_tokenizer()
label_map = llm.llm_engine.vllm_config.model_config.hf_config.id2label
# Run inference
outputs = llm.encode(prompts, pooling_task="token_classify")
for prompt, output in zip(prompts, outputs):
logits = output.outputs.data
predictions = logits.argmax(dim=-1)
# Map predictions to labels
tokens = tokenizer.convert_ids_to_tokens(output.prompt_token_ids)
labels = [label_map[p.item()] for p in predictions]
# Print results
for token, label in zip(tokens, labels):
if token not in tokenizer.all_special_tokens:
print(f"{token:15} → {label}")
if __name__ == "__main__":
args = parse_args()
main(args)


## NER Online[¶](https://docs.vllm.ai#ner-online)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# Adapted from https://huggingface.co/boltuix/NeuroBERT-NER
"""Example online usage of Pooling API for Named Entity Recognition (NER).
Run `vllm serve <model> --runner pooling`
to start up the server in vLLM. e.g.
vllm serve boltuix/NeuroBERT-NER
"""
import argparse
import requests
import torch
def post_http_request(prompt: dict, api_url: str) -> requests.Response:
headers = {"User-Agent": "Test Client"}
response = requests.post(api_url, headers=headers, json=prompt)
return response
def parse_args():
parser = argparse.ArgumentParser()
parser.add_argument("--host", type=str, default="localhost")
parser.add_argument("--port", type=int, default=8000)
parser.add_argument("--model", type=str, default="boltuix/NeuroBERT-NER")
return parser.parse_args()
def main(args):
from transformers import AutoConfig, AutoTokenizer
api_url = f"http://{args.host}:{args.port}/pooling"
model_name = args.model
# Load tokenizer and config
tokenizer = AutoTokenizer.from_pretrained(model_name)
config = AutoConfig.from_pretrained(model_name)
label_map = config.id2label
# Input text
text = "Barack Obama visited Microsoft headquarters in Seattle on January 2025."
prompt = {"model": model_name, "input": text}
pooling_response = post_http_request(prompt=prompt, api_url=api_url)
# Run inference
output = pooling_response.json()["data"][0]
logits = torch.tensor(output["data"])
predictions = logits.argmax(dim=-1)
inputs = tokenizer(text, return_tensors="pt")
# Map predictions to labels
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
labels = [label_map[p.item()] for p in predictions]
assert len(tokens) == len(predictions)
# Print results
for token, label in zip(tokens, labels):
if token not in tokenizer.all_special_tokens:
print(f"{token:15} → {label}")
if __name__ == "__main__":
args = parse_args()
main(args)
source: https://docs.vllm.ai/projects/recipes/en/stable/GLM/GLM-ASR.html
lastmod: 2026-04-27

# GLM-ASR Usage Guide[¶](https://docs.vllm.ai#glm-asr-usage-guide)

This guide describes how to run GLM-ASR-Nano-2512 for automatic speech recognition.

## Model Introduction[¶](https://docs.vllm.ai#model-introduction)

GLM-ASR-Nano-2512 is a robust, open-source speech recognition model with 1.5B parameters (2B model size). Designed for real-world complexity, it outperforms OpenAI Whisper V3 on multiple benchmarks while maintaining a compact size.

### Key Capabilities[¶](https://docs.vllm.ai#key-capabilities)

**Exceptional Dialect Support**: Beyond standard Mandarin and English, the model is highly optimized for Cantonese (粤语) and other dialects, effectively bridging the gap in dialectal speech recognition.**Low-Volume Speech Robustness**: Specifically trained for "Whisper/Quiet Speech" scenarios. It captures and accurately transcribes extremely low-volume audio that traditional models often miss.**SOTA Performance**: Achieves the lowest average error rate (4.10) among comparable open-source models, showing significant advantages in Chinese benchmarks (Wenet Meeting, Aishell-1, etc.).

## Installing Dependencies[¶](https://docs.vllm.ai#installing-dependencies)

uv venv
source .venv/bin/activate
# Install transformers from source (required)
uv pip install git+https://github.com/huggingface/transformers.git
uv pip install -U "vllm[audio]" --torch-backend auto # vllm>=0.14.1 is required


## Running with vLLM[¶](https://docs.vllm.ai#running-with-vllm)

### Start Server[¶](https://docs.vllm.ai#start-server)

### Client Usage[¶](https://docs.vllm.ai#client-usage)

#### Using OpenAI SDK[¶](https://docs.vllm.ai#using-openai-sdk)

import base64
import httpx
from openai import OpenAI
# Initialize client
client = OpenAI(
base_url="http://localhost:8000/v1",
api_key="EMPTY"
)
# Load audio file and encode to base64
audio_url = "https://github.com/zai-org/GLM-ASR/raw/main/examples/example_en.wav"
audio_data = base64.b64encode(httpx.get(audio_url).content).decode("utf-8")
# Create transcription request
response = client.chat.completions.create(
model="zai-org/GLM-ASR-Nano-2512",
messages=[
{
"role": "user",
"content": [
{
"type": "input_audio",
"input_audio": {
"data": audio_data,
"format": "wav"
}
}
]
}
],
max_tokens=500
)
print(response.choices[0].message.content)


#### Using cURL[¶](https://docs.vllm.ai#using-curl)

# First encode audio to base64
AUDIO_BASE64=$(curl -sL "https://github.com/zai-org/GLM-ASR/raw/main/examples/example_en.wav" | base64)
curl http://localhost:8000/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
"model": "zai-org/GLM-ASR-Nano-2512",
"messages": [
{
"role": "user",
"content": [
{
"type": "input_audio",
"input_audio": {
"data": "'"${AUDIO_BASE64}"'",
"format": "wav"
}
}
]
}
],
"max_tokens": 500
}'


#### Using Local Audio File[¶](https://docs.vllm.ai#using-local-audio-file)

import base64
from openai import OpenAI
client = OpenAI(
base_url="http://localhost:8000/v1",
api_key="EMPTY"
)
# Load local audio file
with open("your_audio.mp3", "rb") as f:
audio_data = base64.b64encode(f.read()).decode("utf-8")
response = client.chat.completions.create(
model="zai-org/GLM-ASR-Nano-2512",
messages=[
{
"role": "user",
"content": [
{
"type": "input_audio",
"input_audio": {
"data": audio_data,
"format": "mp3" # or "wav", "flac", etc.
}
}
]
}
],
max_tokens=500
)
print(response.choices[0].message.content)


#### Using Transcribe Endpoint[¶](https://docs.vllm.ai#using-transcribe-endpoint)

import httpx
from openai import OpenAI
client = OpenAI(
base_url="http://localhost:8000/v1",
api_key="EMPTY"
)
# Transcribe audio from URL
audio_url = "https://github.com/zai-org/GLM-ASR/raw/main/examples/example_en.wav"
audio_file = httpx.get(audio_url).content
response = client.audio.transcriptions.create(
model="zai-org/GLM-ASR-Nano-2512",
file=("audio.wav", audio_file),
)
print(response.text)


#### Transcribe with cURL[¶](https://docs.vllm.ai#transcribe-with-curl)

curl http://localhost:8000/v1/audio/transcriptions \
-H "Authorization: Bearer EMPTY" \
-F "model=zai-org/GLM-ASR-Nano-2512" \
-F "file=@your_audio.wav"


## Notes[¶](https://docs.vllm.ai#notes)

**Transformers Version**: This model requires`transformers >= 5.0.0`

for optimal compatibility.
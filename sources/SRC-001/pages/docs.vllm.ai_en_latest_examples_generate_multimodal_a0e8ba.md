source: https://docs.vllm.ai/en/latest/examples/generate/multimodal/
lastmod: 2026-09-24

# Multimodal[¶](https://docs.vllm.ai#multimodal)

Source [https://github.com/vllm-project/vllm/tree/main/examples/generate/multimodal](https://github.com/vllm-project/vllm/tree/main/examples/generate/multimodal).

## Audio Language Offline[¶](https://docs.vllm.ai#audio-language-offline)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""This example shows how to use vLLM for running offline inference
with the correct prompt format on audio language models.
For most models, the prompt format should follow corresponding examples
on HuggingFace model repository.
"""
import os
from typing import Any, NamedTuple
from huggingface_hub import snapshot_download
from transformers import AutoTokenizer
from vllm import LLM, EngineArgs, SamplingParams
from vllm.assets.audio import AudioAsset
from vllm.lora.request import LoRARequest
from vllm.utils.argparse_utils import FlexibleArgumentParser
audio_assets = [AudioAsset("mary_had_lamb"), AudioAsset("winning_call")]
question_per_audio_count = {
0: "What is 1+1?",
1: "What is recited in the audio?",
2: "What sport and what nursery rhyme are referenced?",
}
class ModelRequestData(NamedTuple):
engine_args: EngineArgs
prompt: str | None = None
prompt_token_ids: dict[str, list[int]] | None = None
multi_modal_data: dict[str, Any] | None = None
stop_token_ids: list[int] | None = None
lora_requests: list[LoRARequest] | None = None
# NOTE: The default `max_num_seqs` and `max_model_len` may result in OOM on
# lower-end GPUs.
# Unless specified, these settings have been tested to work on a single L4.
# AudioFlamingo3
def run_audioflamingo3(question: str, audio_count: int) -> ModelRequestData:
model_name = "nvidia/audio-flamingo-3-hf"
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=2,
limit_mm_per_prompt={"audio": audio_count},
enforce_eager=True,
)
# AudioFlamingo3 uses <sound> token for audio
audio_placeholder = "<sound>" * audio_count
prompt = (
"<|im_start|>system\n"
"You are a helpful assistant.<|im_end|>\n"
"<|im_start|>user\n"
f"{audio_placeholder}{question}<|im_end|>\n"
"<|im_start|>assistant\n"
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
)
# CohereASR
def run_cohere_asr(question: str, audio_count: int) -> ModelRequestData:
assert audio_count == 1, "CohereASR only support single audio input per prompt"
model_name = "CohereLabs/cohere-transcribe-03-2026"
prompt = (
"<|startofcontext|><|startoftranscript|>"
"<|emo:undefined|><|en|><|en|><|pnc|><|noitn|>"
"<|notimestamp|><|nodiarize|>"
)
engine_args = EngineArgs(
model=model_name,
limit_mm_per_prompt={"audio": audio_count},
trust_remote_code=True,
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
)
# Gemma3N
def run_gemma3n(question: str, audio_count: int) -> ModelRequestData:
model_name = "google/gemma-3n-E2B-it"
engine_args = EngineArgs(
model=model_name,
max_model_len=2048,
max_num_batched_tokens=2048,
max_num_seqs=2,
limit_mm_per_prompt={"audio": audio_count},
enforce_eager=True,
)
prompt = f"<start_of_turn>user\n<audio_soft_token>{question}"
"<end_of_turn>\n<start_of_turn>model\n"
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
)
# GLM-ASR
def run_glmasr(question: str, audio_count: int) -> ModelRequestData:
model_name = "zai-org/GLM-ASR-Nano-2512"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
# GLM-ASR uses <|pad|> token for audio
audio_placeholder = "<|pad|>" * audio_count
messages = [{"role": "user", "content": f"{audio_placeholder}{question}"}]
prompt = tokenizer.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=4096,
max_num_seqs=2,
limit_mm_per_prompt={"audio": audio_count},
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
)
# FunAudioChat
def run_funaudiochat(question: str, audio_count: int) -> ModelRequestData:
# NOTE: FunAudioChat is not available on the HuggingFace Hub at the time of
# writing. Pass a local model path via `--model`.
model_name = "funaudiochat"
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=2,
limit_mm_per_prompt={"audio": audio_count},
enforce_eager=True,
)
audio_in_prompt = "".join(
["<|audio_bos|><|AUDIO|><|audio_eos|>\n" for _ in range(audio_count)]
)
prompt = f"{audio_in_prompt}{question}"
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
)
# Granite Speech
def run_granite_speech(question: str, audio_count: int) -> ModelRequestData:
# NOTE - the setting in this example are somewhat different from what is
# optimal for granite speech, and it is generally recommended to use beam
# search. Check the model README for suggested settings.
# https://huggingface.co/ibm-granite/granite-speech-3.3-8b
model_name = "ibm-granite/granite-speech-3.3-8b"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=2048,
max_num_seqs=2,
enable_lora=True,
max_lora_rank=64,
limit_mm_per_prompt={"audio": audio_count},
)
# The model has an audio-specific lora directly in its model dir;
# it should be enabled whenever you pass audio inputs to the model.
speech_lora_path = model_name
audio_placeholder = "<|audio|>" * audio_count
prompts = f"<|start_of_role|>system<|end_of_role|>Knowledge Cutoff Date: April 2024.\nToday's Date: December 19, 2024.\nYou are Granite, developed by IBM. You are a helpful AI assistant<|end_of_text|>\n<|start_of_role|>user<|end_of_role|>{audio_placeholder}{question}<|end_of_text|>\n<|start_of_role|>assistant<|end_of_role|>" # noqa: E501
return ModelRequestData(
engine_args=engine_args,
prompt=prompts,
lora_requests=[LoRARequest("speech", 1, speech_lora_path)],
)
# Kimi-Audio-7B-Instruct
def run_kimi_audio(question: str, audio_count: int) -> ModelRequestData:
"""Kimi-Audio-7B-Instruct for audio transcription and understanding."""
model_name = "moonshotai/Kimi-Audio-7B-Instruct"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=4096,
max_num_seqs=2,
limit_mm_per_prompt={"audio": audio_count},
)
# Kimi-Audio uses <|im_kimia_text_blank|> as placeholder for audio features
audio_placeholder = "<|im_kimia_text_blank|>" * audio_count
# Default prompt for transcription
if not question:
question = "Please transcribe the audio"
prompt = f"{audio_placeholder}{question}"
# Stop at EOS token (151644) to prevent repetition
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
stop_token_ids=[151644],
)
# MiDashengLM
def run_midashenglm(question: str, audio_count: int):
model_name = "mispeech/midashenglm-7b"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=4096,
max_num_seqs=5,
limit_mm_per_prompt={"audio": audio_count},
)
audio_in_prompt = "".join(
["<|audio_bos|><|AUDIO|><|audio_eos|>" for idx in range(audio_count)]
)
default_system = "You are a helpful language and speech assistant."
prompt = (
f"<|im_start|>system\n{default_system}<|im_end|>\n"
"<|im_start|>user\n"
f"{audio_in_prompt}{question}<|im_end|>\n"
"<|im_start|>assistant\n"
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
)
# MiniCPM-O
def run_minicpmo(question: str, audio_count: int) -> ModelRequestData:
model_name = "openbmb/MiniCPM-o-2_6"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=4096,
max_num_seqs=2,
limit_mm_per_prompt={"audio": audio_count},
)
stop_tokens = ["<|im_end|>", "<|endoftext|>"]
stop_token_ids = [tokenizer.convert_tokens_to_ids(i) for i in stop_tokens]
audio_placeholder = "(<audio>./</audio>)" * audio_count
audio_chat_template = "{% for message in messages %}{{'<|im_start|>' + message['role'] + '\n' + message['content'] + '<|im_end|>' + '\n'}}{% endfor %}{% if add_generation_prompt %}{{ '<|im_start|>assistant\n<|spk_bos|><|spk|><|spk_eos|><|tts_bos|>' }}{% endif %}" # noqa: E501
messages = [{"role": "user", "content": f"{audio_placeholder}\n{question}"}]
prompt = tokenizer.apply_chat_template(
messages,
tokenize=False,
add_generation_prompt=True,
chat_template=audio_chat_template,
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
stop_token_ids=stop_token_ids,
)
# Phi-4-multimodal-instruct
def run_phi4mm(question: str, audio_count: int) -> ModelRequestData:
"""Phi-4-multimodal-instruct supports both image and audio inputs. Here, we
show how to process audio inputs.
"""
model_path = snapshot_download("microsoft/Phi-4-multimodal-instruct")
# Since the vision-lora and speech-lora co-exist with the base model,
# we have to manually specify the path of the lora weights.
speech_lora_path = os.path.join(model_path, "speech-lora")
placeholders = "".join([f"<|audio_{i + 1}|>" for i in range(audio_count)])
prompts = f"<|user|>{placeholders}{question}<|end|><|assistant|>"
engine_args = EngineArgs(
model=model_path,
trust_remote_code=True,
max_model_len=12800,
max_num_seqs=2,
enable_lora=True,
max_lora_rank=320,
limit_mm_per_prompt={"audio": audio_count},
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompts,
lora_requests=[LoRARequest("speech", 1, speech_lora_path)],
)
# Qwen2-Audio
def run_qwen2_audio(question: str, audio_count: int) -> ModelRequestData:
model_name = "Qwen/Qwen2-Audio-7B-Instruct"
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=5,
limit_mm_per_prompt={"audio": audio_count},
)
audio_in_prompt = "".join(
[
f"Audio {idx + 1}: <|audio_bos|><|AUDIO|><|audio_eos|>\n"
for idx in range(audio_count)
]
)
prompt = (
"<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n"
"<|im_start|>user\n"
f"{audio_in_prompt}{question}<|im_end|>\n"
"<|im_start|>assistant\n"
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
)
# Qwen2.5-Omni
def run_qwen2_5_omni(question: str, audio_count: int):
model_name = "Qwen/Qwen2.5-Omni-7B"
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=5,
limit_mm_per_prompt={"audio": audio_count},
)
audio_in_prompt = "".join(
["<|audio_bos|><|AUDIO|><|audio_eos|>\n" for idx in range(audio_count)]
)
default_system = (
"You are Qwen, a virtual human developed by the Qwen Team, Alibaba "
"Group, capable of perceiving auditory and visual inputs, as well as "
"generating text and speech."
)
prompt = (
f"<|im_start|>system\n{default_system}<|im_end|>\n"
"<|im_start|>user\n"
f"{audio_in_prompt}{question}<|im_end|>\n"
"<|im_start|>assistant\n"
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
)
def run_qwen3_asr(question: str, audio_count: int) -> ModelRequestData:
model_name = "Qwen/Qwen3-Asr-1.7B"
audio_in_prompt = "<|audio_start|><|audio_pad|><|audio_end|>\n" * audio_count
prompt = f"<|im_start|>user\n{audio_in_prompt}<|im_end|>\n<|im_start|>assistant\n"
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=5,
limit_mm_per_prompt={"audio": audio_count},
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
)
# Ultravox 0.5-1B
def run_ultravox(question: str, audio_count: int) -> ModelRequestData:
model_name = "fixie-ai/ultravox-v0_5-llama-3_2-1b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
messages = [{"role": "user", "content": "<|audio|>\n" * audio_count + question}]
prompt = tokenizer.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=5,
trust_remote_code=True,
limit_mm_per_prompt={"audio": audio_count},
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
)
# Voxtral
# Make sure to install mistral-common[audio].
def run_voxtral(question: str, audio_count: int) -> ModelRequestData:
from mistral_common.protocol.instruct.chunk import (
AudioChunk,
TextChunk,
)
from mistral_common.protocol.instruct.messages import (
UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.tokens.tokenizers.audio import Audio
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
model_name = "mistralai/Voxtral-Mini-3B-2507"
tokenizer = MistralTokenizer.from_hf_hub(model_name)
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
max_num_seqs=2,
limit_mm_per_prompt={"audio": audio_count},
config_format="mistral",
load_format="mistral",
tokenizer_mode="mistral",
enforce_eager=True,
enable_chunked_prefill=False,
)
text_chunk = TextChunk(text=question)
audios = [
Audio.from_file(str(audio_assets[i].get_local_path()), strict=False)
for i in range(audio_count)
]
audio_chunks = [AudioChunk.from_audio(audio) for audio in audios]
messages = [UserMessage(content=[*audio_chunks, text_chunk])]
req = ChatCompletionRequest(messages=messages, model=model_name)
tokens = tokenizer.encode_chat_completion(req)
prompt_ids, audios = tokens.tokens, tokens.audios
audios_and_sr = [(au.audio_array, au.sampling_rate) for au in audios]
multi_modal_data = {"audio": audios_and_sr}
return ModelRequestData(
engine_args=engine_args,
prompt_token_ids=prompt_ids,
multi_modal_data=multi_modal_data,
)
# Whisper
def run_whisper(question: str, audio_count: int) -> ModelRequestData:
assert audio_count == 1, "Whisper only support single audio input per prompt"
model_name = "openai/whisper-large-v3-turbo"
prompt = "<|startoftranscript|>"
engine_args = EngineArgs(
model=model_name,
max_model_len=448,
max_num_seqs=5,
limit_mm_per_prompt={"audio": audio_count},
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
)
model_example_map = {
"audioflamingo3": run_audioflamingo3,
"cohere_asr": run_cohere_asr,
"funaudiochat": run_funaudiochat,
"gemma3n": run_gemma3n,
"glmasr": run_glmasr,
"granite_speech": run_granite_speech,
"kimi_audio": run_kimi_audio,
"midashenglm": run_midashenglm,
"minicpmo": run_minicpmo,
"phi4_mm": run_phi4mm,
"qwen2_audio": run_qwen2_audio,
"qwen2_5_omni": run_qwen2_5_omni,
"qwen3_asr": run_qwen3_asr,
"ultravox": run_ultravox,
"voxtral": run_voxtral,
"whisper": run_whisper,
}
def parse_args():
parser = FlexibleArgumentParser(
description="Demo on using vLLM for offline inference with "
"audio language models"
)
parser.add_argument(
"--model-type",
"-m",
type=str,
default="ultravox",
choices=model_example_map.keys(),
help='Huggingface "model_type".',
)
parser.add_argument(
"--model",
type=str,
default=None,
help="Model ID or local path override. Required for funaudiochat.",
)
parser.add_argument(
"--num-prompts", type=int, default=1, help="Number of prompts to run."
)
parser.add_argument(
"--num-audios",
type=int,
default=1,
choices=[0, 1, 2],
help="Number of audio items per prompt.",
)
parser.add_argument(
"--seed",
type=int,
default=0,
help="Set the seed when initializing `vllm.LLM`.",
)
parser.add_argument(
"--tensor-parallel-size",
"-tp",
type=int,
default=None,
help="Tensor parallel size to override the model's default setting. ",
)
return parser.parse_args()
def main(args):
model = args.model_type
if model not in model_example_map:
raise ValueError(f"Model type {model} is not supported.")
if model == "funaudiochat" and not args.model:
raise ValueError("--model is required when --model-type=funaudiochat")
if args.tensor_parallel_size is not None and args.tensor_parallel_size < 1:
raise ValueError(
f"tensor_parallel_size must be a positive integer, "
f"got {args.tensor_parallel_size}"
)
audio_count = args.num_audios
req_data = model_example_map[model](
question_per_audio_count[audio_count], audio_count
)
if model == "funaudiochat":
req_data.engine_args.model = args.model
# Disable other modalities to save memory
default_limits = {"image": 0, "video": 0, "audio": 0}
req_data.engine_args.limit_mm_per_prompt = default_limits | dict(
req_data.engine_args.limit_mm_per_prompt or {}
)
engine_args = vars(req_data.engine_args) | {"seed": args.seed}
if args.tensor_parallel_size is not None:
engine_args["tensor_parallel_size"] = args.tensor_parallel_size
llm = LLM(**engine_args)
# We set temperature to 0.2 so that outputs can be different
# even when all prompts are identical when running batch inference.
sampling_params = SamplingParams(
temperature=0.2, max_tokens=64, stop_token_ids=req_data.stop_token_ids
)
def get_input(start, end):
mm_data = req_data.multi_modal_data
if not mm_data:
mm_data = {}
if end - start > 0:
mm_data = {
"audio": [
asset.audio_and_sample_rate for asset in audio_assets[start:end]
]
}
inputs = {"multi_modal_data": mm_data}
if req_data.prompt:
inputs["prompt"] = req_data.prompt
else:
inputs["prompt_token_ids"] = req_data.prompt_token_ids
return inputs
# Batch inference
assert args.num_prompts > 0
if audio_count != 1:
inputs = get_input(0, audio_count)
inputs = [inputs] * args.num_prompts
else:
# For single audio input, we need to vary the audio input
# to avoid deduplication in vLLM engine.
inputs = []
for i in range(args.num_prompts):
start = i % len(audio_assets)
inp = get_input(start, start + 1)
inputs.append(inp)
# Add LoRA request if applicable
lora_request = (
req_data.lora_requests * args.num_prompts if req_data.lora_requests else None
)
outputs = llm.generate(
inputs,
sampling_params=sampling_params,
lora_request=lora_request,
)
for o in outputs:
generated_text = o.outputs[0].text
print(generated_text)
if __name__ == "__main__":
args = parse_args()
main(args)


## Encoder Decoder Multimodal Offline[¶](https://docs.vllm.ai#encoder-decoder-multimodal-offline)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""This example shows how to use vLLM for running offline inference with
the explicit/implicit prompt format on enc-dec LMMs for text generation.
"""
import os
import time
from collections.abc import Sequence
from typing import NamedTuple
from vllm import LLM, EngineArgs, PromptType, SamplingParams
from vllm.assets.audio import AudioAsset
from vllm.utils.argparse_utils import FlexibleArgumentParser
class ModelRequestData(NamedTuple):
engine_args: EngineArgs
prompts: Sequence[PromptType]
def run_whisper():
os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"
engine_args = EngineArgs(
model="openai/whisper-large-v3-turbo",
max_model_len=448,
max_num_seqs=16,
limit_mm_per_prompt={"audio": 1},
dtype="half",
)
prompts = [
{ # Test implicit prompt
"prompt": "<|startoftranscript|>",
"multi_modal_data": {
"audio": AudioAsset("mary_had_lamb").audio_and_sample_rate,
},
},
{ # Test explicit encoder/decoder prompt
"encoder_prompt": {
"prompt": "",
"multi_modal_data": {
"audio": AudioAsset("winning_call").audio_and_sample_rate,
},
},
"decoder_prompt": "<|startoftranscript|>",
},
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
def run_fireredasr2():
"""FireRedASR2 – Automatic Speech Recognition model.
This model uses a Conformer encoder + Qwen2 LLM decoder architecture
for speech-to-text transcription. Audio is passed via the implicit
prompt format with the ``<|AUDIO|>`` placeholder token.
"""
engine_args = EngineArgs(
model="allendou/FireRedASR2-LLM-vllm",
max_model_len=448,
max_num_seqs=16,
limit_mm_per_prompt={"audio": 1},
)
prompt_str = (
"<|im_start|>user\n<|AUDIO|>请转写音频为文字<|im_end|>\n<|im_start|>assistant\n"
)
prompts = [
{ # Implicit prompt with audio
"prompt": prompt_str,
"multi_modal_data": {
"audio": AudioAsset("mary_had_lamb").audio_and_sample_rate,
},
},
{ # Another audio sample
"prompt": prompt_str,
"multi_modal_data": {
"audio": AudioAsset("winning_call").audio_and_sample_rate,
},
},
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
model_example_map = {
"fireredasr2": run_fireredasr2,
"whisper": run_whisper,
}
def parse_args():
parser = FlexibleArgumentParser(
description="Demo on using vLLM for offline inference with "
"vision language models for text generation"
)
parser.add_argument(
"--model-type",
"-m",
type=str,
default="whisper",
choices=model_example_map.keys(),
help='Huggingface "model_type".',
)
parser.add_argument(
"--seed",
type=int,
default=0,
help="Set the seed when initializing `vllm.LLM`.",
)
return parser.parse_args()
def main(args):
model = args.model_type
if model not in model_example_map:
raise ValueError(f"Model type {model} is not supported.")
req_data = model_example_map[model]()
# Disable other modalities to save memory
engine_args = req_data.engine_args
default_limits = {"image": 0, "video": 0, "audio": 0}
limit_mm_per_prompt = default_limits | (engine_args.limit_mm_per_prompt or {})
engine_args.limit_mm_per_prompt = limit_mm_per_prompt
engine_args.seed = args.seed
llm = LLM.from_engine_args(engine_args)
prompts = req_data.prompts
# Create a sampling params object.
sampling_params = SamplingParams(
temperature=0,
top_p=1.0,
max_tokens=64,
skip_special_tokens=False,
)
start = time.time()
# Generate output tokens from the prompts. The output is a list of
# RequestOutput objects that contain the prompt, generated
# text, and other information.
outputs = llm.generate(prompts, sampling_params)
# Print the outputs.
for output in outputs:
prompt = output.prompt
generated_text = output.outputs[0].text
print(f"Decoder prompt: {prompt!r}, Generated text: {generated_text!r}")
duration = time.time() - start
print("Duration:", duration)
print("RPS:", len(prompts) / duration)
if __name__ == "__main__":
args = parse_args()
main(args)


## Mistral-Small Offline[¶](https://docs.vllm.ai#mistral-small-offline)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# ruff: noqa
import argparse
from vllm import LLM
from vllm.sampling_params import SamplingParams
from vllm.assets.image import ImageAsset
from vllm.multimodal.utils import encode_image_url
# This script is an offline demo for running Mistral-Small-3.1
#
# If you want to run a server/client setup, please follow this code:
#
# - Server:
#
# ```bash
# # Mistral format
# vllm serve mistralai/Mistral-Small-3.1-24B-Instruct-2503 \
# --tokenizer-mode mistral --config-format mistral --load-format mistral \
# --limit-mm-per-prompt.image 4 --max-model-len 16384
#
# # HF format
# vllm serve mistralai/Mistral-Small-3.1-24B-Instruct-2503 \
# --limit-mm-per-prompt.image 4 --max-model-len 16384
# ```
#
# - Client:
#
# ```bash
# curl --location 'http://<your-node-url>:8000/v1/chat/completions' \
# --header 'Content-Type: application/json' \
# --header 'Authorization: Bearer token' \
# --data '{
# "model": "mistralai/Mistral-Small-3.1-24B-Instruct-2503",
# "messages": [
# {
# "role": "user",
# "content": [
# {"type" : "text", "text": "Describe this image in detail please."},
# {"type": "image_url", "image_url": {"url": "https://s3.amazonaws.com/cms.ipressroom.com/338/files/201808/5b894ee1a138352221103195_A680%7Ejogging-edit/A680%7Ejogging-edit_hero.jpg"}},
# {"type" : "text", "text": "and this one as well. Answer in French."},
# {"type": "image_url", "image_url": {"url": "https://www.wolframcloud.com/obj/resourcesystem/images/a0e/a0ee3983-46c6-4c92-b85d-059044639928/6af8cfb971db031b.png"}}
# ]
# }
# ]
# }'
# ```
#
# Usage:
# python demo.py simple
# python demo.py advanced
# Lower max_model_len and/or max_num_seqs on low-VRAM GPUs.
# These scripts have been tested on 2x L40 GPUs
def run_simple_demo(args: argparse.Namespace):
model_name = "mistralai/Mistral-Small-3.1-24B-Instruct-2503"
sampling_params = SamplingParams(max_tokens=8192)
llm = LLM(
model=model_name,
tokenizer_mode="mistral" if args.format == "mistral" else "hf",
config_format="mistral" if args.format == "mistral" else "hf",
load_format="mistral" if args.format == "mistral" else "hf",
limit_mm_per_prompt={"image": 1},
max_model_len=4096,
max_num_seqs=2,
tensor_parallel_size=2,
mm_processor_cache_gb=0 if args.disable_mm_processor_cache else 4,
)
prompt = "Describe this image in one sentence."
messages = [
{
"role": "user",
"content": [
{"type": "text", "text": prompt},
{
"type": "image_url",
"image_url": {
"url": encode_image_url(ImageAsset("cherry_blossom").pil_image)
},
},
],
},
]
outputs = llm.chat(messages, sampling_params=sampling_params)
print("-" * 50)
print(outputs[0].outputs[0].text)
print("-" * 50)
def run_advanced_demo(args: argparse.Namespace):
model_name = "mistralai/Mistral-Small-3.1-24B-Instruct-2503"
max_img_per_msg = 3
max_tokens_per_img = 4096
sampling_params = SamplingParams(max_tokens=8192, temperature=0.7)
llm = LLM(
model=model_name,
tokenizer_mode="mistral" if args.format == "mistral" else "hf",
config_format="mistral" if args.format == "mistral" else "hf",
load_format="mistral" if args.format == "mistral" else "hf",
limit_mm_per_prompt={"image": max_img_per_msg},
max_model_len=max_img_per_msg * max_tokens_per_img,
tensor_parallel_size=2,
mm_processor_cache_gb=0 if args.disable_mm_processor_cache else 4,
)
prompt = "Describe the following image."
url_1 = "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png"
url_2 = "https://picsum.photos/seed/picsum/200/300"
url_3 = "https://picsum.photos/id/32/512/512"
messages = [
{
"role": "user",
"content": [
{"type": "text", "text": prompt},
{"type": "image_url", "image_url": {"url": url_1}},
{"type": "image_url", "image_url": {"url": url_2}},
],
},
{
"role": "assistant",
"content": "The images show nature.",
},
{
"role": "user",
"content": "More details please and answer only in French!.",
},
{
"role": "user",
"content": [
{"type": "image_url", "image_url": {"url": url_3}},
],
},
]
outputs = llm.chat(messages=messages, sampling_params=sampling_params)
print("-" * 50)
print(outputs[0].outputs[0].text)
print("-" * 50)
def parse_args():
parser = argparse.ArgumentParser(
description="Run a demo in simple or advanced mode."
)
parser.add_argument(
"mode",
choices=["simple", "advanced"],
help="Specify the demo mode: 'simple' or 'advanced'",
)
parser.add_argument(
"--format",
choices=["mistral", "hf"],
default="mistral",
help="Specify the format of the model to load.",
)
parser.add_argument(
"--disable-mm-processor-cache",
action="store_true",
help="If True, disables caching of multi-modal processor.",
)
return parser.parse_args()
def main():
args = parse_args()
if args.mode == "simple":
print("Running simple demo...")
run_simple_demo(args)
elif args.mode == "advanced":
print("Running advanced demo...")
run_advanced_demo(args)
if __name__ == "__main__":
main()


## OpenAI Chat Completion Client For Multimodal[¶](https://docs.vllm.ai#openai-chat-completion-client-for-multimodal)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""An example showing how to use vLLM to serve multimodal models
and run online serving with OpenAI client.
Launch the vLLM server with the following command:
(single image inference with Llava)
vllm serve llava-hf/llava-1.5-7b-hf
(multi-image inference with Phi-3.5-vision-instruct)
vllm serve microsoft/Phi-3.5-vision-instruct --runner generate \
--trust-remote-code --max-model-len 4096 --limit-mm-per-prompt.image 2
(audio inference with Ultravox)
vllm serve fixie-ai/ultravox-v0_5-llama-3_2-1b \
--max-model-len 4096 --trust-remote-code
run the script with
python openai_chat_completion_client_for_multimodal.py --chat-type audio
"""
import os
import pybase64 as base64
import requests
from openai import OpenAI
from vllm.utils.argparse_utils import FlexibleArgumentParser
# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"
client = OpenAI(
# defaults to os.environ.get("OPENAI_API_KEY")
api_key=openai_api_key,
base_url=openai_api_base,
)
headers = {"User-Agent": "vLLM Example Client"}
def encode_base64_content_from_url(content_url: str) -> str:
"""Encode a content retrieved from a remote url to base64 format."""
with requests.get(content_url, headers=headers) as response:
response.raise_for_status()
result = base64.b64encode(response.content).decode("utf-8")
return result
def encode_base64_content_from_file(file_path: str) -> str:
"""Encode a local file content to base64 format."""
with open(file_path, "rb") as file:
file_content = file.read()
result = base64.b64encode(file_content).decode("utf-8")
return result
# Text-only inference
def run_text_only(model: str, max_completion_tokens: int) -> None:
chat_completion = client.chat.completions.create(
messages=[{"role": "user", "content": "What's the capital of France?"}],
model=model,
max_completion_tokens=max_completion_tokens,
)
result = chat_completion.choices[0].message.content
print("Chat completion output:\n", result)
# Single-image input inference
def run_single_image(model: str, max_completion_tokens: int) -> None:
## Use image url in the payload
image_url = "https://vllm-public-assets.s3.us-west-2.amazonaws.com/vision_model_images/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
image_file = "/path/to/image.jpg" # local file
chat_completion_from_url = client.chat.completions.create(
messages=[
{
"role": "user",
"content": [
{"type": "text", "text": "What's in this image?"},
{
"type": "image_url",
"image_url": {"url": image_url},
},
],
}
],
model=model,
max_completion_tokens=max_completion_tokens,
)
result = chat_completion_from_url.choices[0].message.content
print("Chat completion output from image url:\n", result)
## Use local image url in the payload
# Launch the API server/engine with the --allowed-local-media-path argument.
if os.path.exists(image_file):
chat_completion_from_local_image_url = client.chat.completions.create(
messages=[
{
"role": "user",
"content": [
{"type": "text", "text": "What's in this image?"},
{
"type": "image_url",
"image_url": {"url": f"file://{image_file}"},
},
],
}
],
model=model,
max_completion_tokens=max_completion_tokens,
)
result = chat_completion_from_local_image_url.choices[0].message.content
print("Chat completion output from local image file:\n", result)
else:
print(f"Local image file not found at {image_file}, skipping local file test.")
## Use base64 encoded image in the payload
image_base64 = encode_base64_content_from_url(image_url)
chat_completion_from_base64 = client.chat.completions.create(
messages=[
{
"role": "user",
"content": [
{"type": "text", "text": "What's in this image?"},
{
"type": "image_url",
"image_url": {"url": f"data:image/jpeg;base64,{image_base64}"},
},
],
}
],
model=model,
max_completion_tokens=max_completion_tokens,
)
result = chat_completion_from_base64.choices[0].message.content
print("Chat completion output from base64 encoded image:", result)
## Use base64 encoded local image in the payload
if os.path.exists(image_file):
local_image_base64 = encode_base64_content_from_file(image_file)
chat_completion_from_local_image_base64 = client.chat.completions.create(
messages=[
{
"role": "user",
"content": [
{"type": "text", "text": "What's in this image?"},
{
"type": "image_url",
"image_url": {
"url": f"data:image/jpeg;base64,{local_image_base64}"
},
},
],
}
],
model=model,
max_completion_tokens=max_completion_tokens,
)
result = chat_completion_from_local_image_base64.choices[0].message.content
print("Chat completion output from base64 encoded local image:", result)
else:
print(f"Local image file not found at {image_file}, skipping local file test.")
# Multi-image input inference
def run_multi_image(model: str, max_completion_tokens: int) -> None:
image_url_duck = "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/duck.jpg"
image_url_lion = "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/lion.jpg"
chat_completion_from_url = client.chat.completions.create(
messages=[
{
"role": "user",
"content": [
{"type": "text", "text": "What are the animals in these images?"},
{
"type": "image_url",
"image_url": {"url": image_url_duck},
},
{
"type": "image_url",
"image_url": {"url": image_url_lion},
},
],
}
],
model=model,
max_completion_tokens=max_completion_tokens,
)
result = chat_completion_from_url.choices[0].message.content
print("Chat completion output:\n", result)
# Video input inference
def run_video(model: str, max_completion_tokens: int) -> None:
video_url = "https://huggingface.co/datasets/raushan-testing-hf/videos-test/resolve/main/sample_demo_1.mp4"
video_base64 = encode_base64_content_from_url(video_url)
## Use video url in the payload
chat_completion_from_url = client.chat.completions.create(
messages=[
{
"role": "user",
"content": [
{"type": "text", "text": "What's in this video?"},
{
"type": "video_url",
"video_url": {"url": video_url},
},
],
}
],
model=model,
max_completion_tokens=max_completion_tokens,
)
result = chat_completion_from_url.choices[0].message.content
print("Chat completion output from video url:\n", result)
## Use base64 encoded video in the payload
chat_completion_from_base64 = client.chat.completions.create(
messages=[
{
"role": "user",
"content": [
{"type": "text", "text": "What's in this video?"},
{
"type": "video_url",
"video_url": {"url": f"data:video/mp4;base64,{video_base64}"},
},
],
}
],
model=model,
max_completion_tokens=max_completion_tokens,
)
result = chat_completion_from_base64.choices[0].message.content
print("Chat completion output from base64 encoded video:\n", result)
# Audio input inference
def run_audio(model: str, max_completion_tokens: int) -> None:
from vllm.assets.audio import AudioAsset
audio_url = AudioAsset("winning_call").url
audio_base64 = encode_base64_content_from_url(audio_url)
# OpenAI-compatible schema (`input_audio`)
chat_completion_from_base64 = client.chat.completions.create(
messages=[
{
"role": "user",
"content": [
{"type": "text", "text": "What's in this audio?"},
{
"type": "input_audio",
"input_audio": {
# Any format supported by soundfile/PyAV is supported
"data": audio_base64,
"format": "wav",
},
},
],
}
],
model=model,
max_completion_tokens=max_completion_tokens,
)
result = chat_completion_from_base64.choices[0].message.content
print("Chat completion output from input audio:\n", result)
# HTTP URL
chat_completion_from_url = client.chat.completions.create(
messages=[
{
"role": "user",
"content": [
{"type": "text", "text": "What's in this audio?"},
{
"type": "audio_url",
"audio_url": {
# Any format supported by soundfile/PyAV is supported
"url": audio_url
},
},
],
}
],
model=model,
max_completion_tokens=max_completion_tokens,
)
result = chat_completion_from_url.choices[0].message.content
print("Chat completion output from audio url:\n", result)
# base64 URL
chat_completion_from_base64 = client.chat.completions.create(
messages=[
{
"role": "user",
"content": [
{"type": "text", "text": "What's in this audio?"},
{
"type": "audio_url",
"audio_url": {
# Any format supported by soundfile/PyAV is supported
"url": f"data:audio/ogg;base64,{audio_base64}"
},
},
],
}
],
model=model,
max_completion_tokens=max_completion_tokens,
)
result = chat_completion_from_base64.choices[0].message.content
print("Chat completion output from base64 encoded audio:\n", result)
def run_multi_audio(model: str, max_completion_tokens: int) -> None:
from vllm.assets.audio import AudioAsset
# Two different audios to showcase batched inference.
audio_url = AudioAsset("winning_call").url
audio_base64 = encode_base64_content_from_url(audio_url)
audio_url2 = AudioAsset("azacinto_foscolo").url
audio_base64_2 = encode_base64_content_from_url(audio_url2)
# OpenAI-compatible schema (`input_audio`)
chat_completion_from_base64 = client.chat.completions.create(
messages=[
{
"role": "user",
"content": [
{"type": "text", "text": "Are these two audios the same?"},
{
"type": "input_audio",
"input_audio": {
"data": audio_base64,
"format": "wav",
},
},
{
"type": "input_audio",
"input_audio": {
"data": audio_base64_2,
"format": "wav",
},
},
],
}
],
model=model,
max_completion_tokens=max_completion_tokens,
)
result = chat_completion_from_base64.choices[0].message.content
print("Chat completion output from input audio:\n", result)
example_function_map = {
"text-only": run_text_only,
"single-image": run_single_image,
"multi-image": run_multi_image,
"multi-audio": run_multi_audio,
"video": run_video,
"audio": run_audio,
}
def parse_args():
parser = FlexibleArgumentParser(
description="Demo on using OpenAI client for online serving with "
"multimodal language models served with vLLM."
)
parser.add_argument(
"--chat-type",
"-c",
type=str,
default="single-image",
choices=list(example_function_map.keys()),
help="Conversation type with multimodal data.",
)
parser.add_argument(
"--max-completion-tokens",
"-n",
type=int,
default=128,
help="Maximum number of tokens to generate for each completion.",
)
return parser.parse_args()
def main(args) -> None:
chat_type = args.chat_type
model = client.models.list().data[0].id
example_function_map[chat_type](model, args.max_completion_tokens)
if __name__ == "__main__":
args = parse_args()
main(args)


## Qwen2 5 Omni - Readme[¶](https://docs.vllm.ai#qwen2-5-omni-readme)

# Qwen2.5-Omni Offline Inference Examples
This folder provides several example scripts on how to inference Qwen2.5-Omni offline.
## Thinker Only
```bash
# Audio + image + video
python examples/generate/multimodal/qwen2_5_omni/only_thinker.py \
-q mixed_modalities
# Read vision and audio inputs from a single video file
python examples/generate/multimodal/qwen2_5_omni/only_thinker.py \
-q use_audio_in_video
# Multiple audios
python examples/generate/multimodal/qwen2_5_omni/only_thinker.py \
-q multi_audios
```
This script will run the thinker part of Qwen2.5-Omni, and generate text response.
You can also test Qwen2.5-Omni on a single modality:
```bash
# Process audio inputs
python examples/generate/multimodal/audio_language_offline.py \
--model-type qwen2_5_omni
# Process image inputs
python examples/generate/multimodal/vision_language_offline.py \
--modality image \
--model-type qwen2_5_omni
# Process video inputs
python examples/generate/multimodal/vision_language_offline.py \
--modality video \
--model-type qwen2_5_omni
```


## Qwen2 5 Omni - Only Thinker[¶](https://docs.vllm.ai#qwen2-5-omni-only-thinker)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""This example shows how to use vLLM for running offline inference
with the correct prompt format on Qwen2.5-Omni (thinker only).
"""
from typing import NamedTuple
from vllm import LLM, SamplingParams
from vllm.assets.audio import AudioAsset
from vllm.assets.image import ImageAsset
from vllm.assets.video import VideoAsset
from vllm.multimodal.image import convert_image_mode
from vllm.utils.argparse_utils import FlexibleArgumentParser
class QueryResult(NamedTuple):
inputs: dict
limit_mm_per_prompt: dict[str, int]
# NOTE: The default `max_num_seqs` and `max_model_len` may result in OOM on
# lower-end GPUs.
# Unless specified, these settings have been tested to work on a single L4.
default_system = (
"You are Qwen, a virtual human developed by the Qwen Team, Alibaba "
"Group, capable of perceiving auditory and visual inputs, as well as "
"generating text and speech."
)
def get_mixed_modalities_query() -> QueryResult:
question = (
"What is recited in the audio? "
"What is the content of this image? Why is this video funny?"
)
prompt = (
f"<|im_start|>system\n{default_system}<|im_end|>\n"
"<|im_start|>user\n<|audio_bos|><|AUDIO|><|audio_eos|>"
"<|vision_bos|><|IMAGE|><|vision_eos|>"
"<|vision_bos|><|VIDEO|><|vision_eos|>"
f"{question}<|im_end|>\n"
f"<|im_start|>assistant\n"
)
return QueryResult(
inputs={
"prompt": prompt,
"multi_modal_data": {
"audio": AudioAsset("mary_had_lamb").audio_and_sample_rate,
"image": convert_image_mode(
ImageAsset("cherry_blossom").pil_image, "RGB"
),
"video": VideoAsset(name="baby_reading", num_frames=16).np_ndarrays,
},
},
limit_mm_per_prompt={"audio": 1, "image": 1, "video": 1},
)
def get_use_audio_in_video_query() -> QueryResult:
question = (
"Describe the content of the video, then convert what the baby say into text."
)
prompt = (
f"<|im_start|>system\n{default_system}<|im_end|>\n"
"<|im_start|>user\n<|vision_bos|><|VIDEO|><|vision_eos|>"
f"{question}<|im_end|>\n"
f"<|im_start|>assistant\n"
)
asset = VideoAsset(name="baby_reading", num_frames=16)
audio = asset.get_audio(sampling_rate=16000)
return QueryResult(
inputs={
"prompt": prompt,
"multi_modal_data": {
"video": asset.np_ndarrays,
"audio": audio,
},
"mm_processor_kwargs": {
"use_audio_in_video": True,
},
},
limit_mm_per_prompt={"audio": 1, "video": 1},
)
def get_multi_audios_query() -> QueryResult:
question = "Are these two audio clips the same?"
prompt = (
f"<|im_start|>system\n{default_system}<|im_end|>\n"
"<|im_start|>user\n<|audio_bos|><|AUDIO|><|audio_eos|>"
"<|audio_bos|><|AUDIO|><|audio_eos|>"
f"{question}<|im_end|>\n"
f"<|im_start|>assistant\n"
)
return QueryResult(
inputs={
"prompt": prompt,
"multi_modal_data": {
"audio": [
AudioAsset("winning_call").audio_and_sample_rate,
AudioAsset("mary_had_lamb").audio_and_sample_rate,
],
},
},
limit_mm_per_prompt={
"audio": 2,
},
)
def get_multi_images_query() -> QueryResult:
question = "What are the differences between these two images?"
prompt = (
f"<|im_start|>system\n{default_system}<|im_end|>\n"
"<|im_start|>user\n<|vision_bos|><|IMAGE|><|vision_eos|>"
"<|vision_bos|><|IMAGE|><|vision_eos|>"
f"{question}<|im_end|>\n"
f"<|im_start|>assistant\n"
)
return QueryResult(
inputs={
"prompt": prompt,
"multi_modal_data": {
"image": [
convert_image_mode(ImageAsset("cherry_blossom").pil_image, "RGB"),
convert_image_mode(ImageAsset("stop_sign").pil_image, "RGB"),
],
},
},
limit_mm_per_prompt={
"image": 2,
},
)
query_map = {
"mixed_modalities": get_mixed_modalities_query,
"use_audio_in_video": get_use_audio_in_video_query,
"multi_audios": get_multi_audios_query,
"multi_images": get_multi_images_query,
}
def main(args):
model_name = "Qwen/Qwen2.5-Omni-7B"
query_result = query_map[args.query_type]()
llm = LLM(
model=model_name,
max_model_len=5632,
max_num_seqs=5,
limit_mm_per_prompt=query_result.limit_mm_per_prompt,
seed=args.seed,
)
# We set temperature to 0.2 so that outputs can be different
# even when all prompts are identical when running batch inference.
sampling_params = SamplingParams(temperature=0.2, max_tokens=64)
outputs = llm.generate(query_result.inputs, sampling_params=sampling_params)
for o in outputs:
generated_text = o.outputs[0].text
print(generated_text)
def parse_args():
parser = FlexibleArgumentParser(
description="Demo on using vLLM for offline inference with "
"audio language models"
)
parser.add_argument(
"--query-type",
"-q",
type=str,
default="mixed_modalities",
choices=query_map.keys(),
help="Query type.",
)
parser.add_argument(
"--seed",
type=int,
default=0,
help="Set the seed when initializing `vllm.LLM`.",
)
return parser.parse_args()
if __name__ == "__main__":
args = parse_args()
main(args)


## Qwen3 Omni - Only Thinker[¶](https://docs.vllm.ai#qwen3-omni-only-thinker)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""This example shows how to use vLLM for running offline inference
with the correct prompt format on Qwen3-Omni (thinker only).
"""
from typing import NamedTuple
from vllm import LLM, SamplingParams
from vllm.assets.audio import AudioAsset
from vllm.assets.image import ImageAsset
from vllm.assets.video import VideoAsset
from vllm.multimodal.image import convert_image_mode
from vllm.utils.argparse_utils import FlexibleArgumentParser
class QueryResult(NamedTuple):
inputs: dict
limit_mm_per_prompt: dict[str, int]
# NOTE: The default `max_num_seqs` and `max_model_len` may result in OOM on
# lower-end GPUs.
# Unless specified, these settings have been tested to work on a single L4.
default_system = (
"You are Qwen, a virtual human developed by the Qwen Team, Alibaba "
"Group, capable of perceiving auditory and visual inputs, as well as "
"generating text and speech."
)
def get_mixed_modalities_query() -> QueryResult:
question = (
"What is recited in the audio? "
"What is the content of this image? Why is this video funny?"
)
prompt = (
f"<|im_start|>system\n{default_system}<|im_end|>\n"
"<|im_start|>user\n<|audio_start|><|audio_pad|><|audio_end|>"
"<|vision_start|><|image_pad|><|vision_end|>"
"<|vision_start|><|video_pad|><|vision_end|>"
f"{question}<|im_end|>\n"
f"<|im_start|>assistant\n"
)
return QueryResult(
inputs={
"prompt": prompt,
"multi_modal_data": {
"audio": AudioAsset("mary_had_lamb").audio_and_sample_rate,
"image": convert_image_mode(
ImageAsset("cherry_blossom").pil_image, "RGB"
),
"video": VideoAsset(name="baby_reading", num_frames=16).np_ndarrays,
},
},
limit_mm_per_prompt={"audio": 1, "image": 1, "video": 1},
)
def get_use_audio_in_video_query() -> QueryResult:
question = (
"Describe the content of the video in details, then convert what the "
"baby say into text."
)
prompt = (
f"<|im_start|>system\n{default_system}<|im_end|>\n"
"<|im_start|>user\n<|vision_start|><|video_pad|><|vision_end|>"
f"{question}<|im_end|>\n"
f"<|im_start|>assistant\n"
)
asset = VideoAsset(name="baby_reading", num_frames=16)
audio = asset.get_audio(sampling_rate=16000)
return QueryResult(
inputs={
"prompt": prompt,
"multi_modal_data": {
"video": asset.np_ndarrays,
"audio": audio,
},
"mm_processor_kwargs": {
"use_audio_in_video": True,
},
},
limit_mm_per_prompt={"audio": 1, "video": 1},
)
def get_multi_audios_query() -> QueryResult:
question = "Are these two audio clips the same?"
prompt = (
f"<|im_start|>system\n{default_system}<|im_end|>\n"
"<|im_start|>user\n<|audio_start|><|audio_pad|><|audio_end|>"
"<|audio_start|><|audio_pad|><|audio_end|>"
f"{question}<|im_end|>\n"
f"<|im_start|>assistant\n"
)
return QueryResult(
inputs={
"prompt": prompt,
"multi_modal_data": {
"audio": [
AudioAsset("winning_call").audio_and_sample_rate,
AudioAsset("mary_had_lamb").audio_and_sample_rate,
],
},
},
limit_mm_per_prompt={
"audio": 2,
},
)
def get_multi_images_query() -> QueryResult:
question = "What are the differences between these two images?"
prompt = (
f"<|im_start|>system\n{default_system}<|im_end|>\n"
"<|im_start|>user\n<|vision_start|><|image_pad|><|vision_end|>"
"<|vision_start|><|image_pad|><|vision_end|>"
f"{question}<|im_end|>\n"
f"<|im_start|>assistant\n"
)
return QueryResult(
inputs={
"prompt": prompt,
"multi_modal_data": {
"image": [
convert_image_mode(ImageAsset("cherry_blossom").pil_image, "RGB"),
convert_image_mode(ImageAsset("stop_sign").pil_image, "RGB"),
],
},
},
limit_mm_per_prompt={
"image": 2,
},
)
query_map = {
"mixed_modalities": get_mixed_modalities_query,
"use_audio_in_video": get_use_audio_in_video_query,
"multi_audios": get_multi_audios_query,
"multi_images": get_multi_images_query,
}
def main(args):
model_name = args.model
query_result = query_map[args.query_type]()
llm = LLM(
model=model_name,
max_model_len=args.max_model_len,
max_num_seqs=5,
limit_mm_per_prompt=query_result.limit_mm_per_prompt,
seed=args.seed,
tensor_parallel_size=args.tensor_parallel_size,
gpu_memory_utilization=args.gpu_memory_utilization,
)
# We set temperature to 0.2 so that outputs can be different
# even when all prompts are identical when running batch inference.
sampling_params = SamplingParams(temperature=0.2, max_tokens=256)
outputs = llm.generate(query_result.inputs, sampling_params=sampling_params)
for o in outputs:
generated_text = o.outputs[0].text
print(generated_text)
def parse_args():
parser = FlexibleArgumentParser(
description="Demo on using vLLM for offline inference with "
"audio language models"
)
parser.add_argument(
"--query-type",
"-q",
type=str,
default="mixed_modalities",
choices=query_map.keys(),
help="Query type.",
)
parser.add_argument(
"--seed",
type=int,
default=0,
help="Set the seed when initializing `vllm.LLM`.",
)
parser.add_argument(
"--model",
type=str,
default="Qwen/Qwen3-Omni-30B-A3B-Instruct",
help="Model name or path.",
)
parser.add_argument(
"--tensor-parallel-size",
"-tp",
type=int,
default=1,
help="Tensor parallel size for distributed inference.",
)
parser.add_argument(
"--gpu-memory-utilization",
type=float,
default=0.9,
help="GPU memory utilization (0.0 to 1.0).",
)
parser.add_argument(
"--max-model-len",
type=int,
default=12800,
help="Maximum model context length.",
)
return parser.parse_args()
if __name__ == "__main__":
args = parse_args()
main(args)


## Vision Language Multi Image Offline[¶](https://docs.vllm.ai#vision-language-multi-image-offline)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""This example shows how to use vLLM for running offline inference with
multi-image input on vision language models for text generation,
using the chat template defined by the model.
"""
import os
from argparse import Namespace
from typing import NamedTuple
from huggingface_hub import snapshot_download
from PIL.Image import Image
from transformers import AutoProcessor, AutoTokenizer
from vllm import LLM, EngineArgs, SamplingParams
from vllm.lora.request import LoRARequest
from vllm.multimodal.utils import fetch_image
from vllm.platforms import current_platform
from vllm.utils.argparse_utils import FlexibleArgumentParser
QUESTION = "What is the content of each image?"
IMAGE_URLS = [
"https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/duck.jpg",
"https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/lion.jpg",
"https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/flycatcher.jpeg",
"https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/somefish.jpg",
"https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/starfish.jpg",
"https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/snail.jpg",
"https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/thistle.jpg",
"https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/husky.jpg",
"https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/orangetabbycat.jpg",
"https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/guineapig.jpg",
"https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/rabbit.jpg",
"https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/horsepony.jpg",
]
class ModelRequestData(NamedTuple):
engine_args: EngineArgs
prompt: str
image_data: list[Image]
stop_token_ids: list[int] | None = None
chat_template: str | None = None
lora_requests: list[LoRARequest] | None = None
sampling_params: SamplingParams | None = None
# NOTE: The default `max_num_seqs` and `max_model_len` may result in OOM on
# lower-end GPUs.
# Unless specified, these settings have been tested to work on a single L4.
def load_aria(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "rhymes-ai/Aria"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
dtype="bfloat16",
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = "<fim_prefix><|img|><fim_suffix>\n" * len(image_urls)
prompt = (
f"<|im_start|>user\n{placeholders}{question}<|im_end|>\n<|im_start|>assistant\n"
)
stop_token_ids = [93532, 93653, 944, 93421, 1019, 93653, 93519]
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
stop_token_ids=stop_token_ids,
image_data=[fetch_image(url) for url in image_urls],
)
def load_bee(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "Open-Bee/Bee-8B-RL"
engine_args = EngineArgs(
model=model_name,
max_model_len=16384,
max_num_seqs=16,
limit_mm_per_prompt={"image": len(image_urls)},
trust_remote_code=True,
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
}
]
processor = AutoProcessor.from_pretrained(model_name, trust_remote_code=True)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_command_a_vision(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "CohereLabs/command-a-vision-07-2025"
# NOTE: This model is 122B parameters and requires tensor parallelism
# Recommended to use tp=4 on H100 GPUs
engine_args = EngineArgs(
model=model_name,
max_model_len=32768,
tensor_parallel_size=4,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
}
]
processor = AutoProcessor.from_pretrained(model_name)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_deepseek_vl2(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "deepseek-ai/deepseek-vl2-tiny"
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=2,
hf_overrides={"architectures": ["DeepseekVLV2ForCausalLM"]},
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholder = "".join(
f"image_{i}:<image>\n" for i, _ in enumerate(image_urls, start=1)
)
prompt = f"<|User|>: {placeholder}{question}\n\n<|Assistant|>:"
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_deepseek_ocr(question: str, image_urls: list[str]) -> ModelRequestData:
from vllm.model_executor.models.deepseek_ocr import NGramPerReqLogitsProcessor
model_name = "deepseek-ai/DeepSeek-OCR"
engine_args = EngineArgs(
model=model_name,
max_num_seqs=2,
limit_mm_per_prompt={"image": len(image_urls)},
logits_processors=[NGramPerReqLogitsProcessor],
)
placeholder = "<image>\n" * len(image_urls)
prompt = placeholder + question
# The following sampling params config is taken from
# the official Deepseek-OCR inference example.
# (IMPORTANT) Use the custom logits processor and avoid skipping
# special tokens for this model for the optimal OCR performance.
sampling_params = SamplingParams(
temperature=0.0,
max_tokens=8192,
# ngram logit processor args
extra_args=dict(
ngram_size=30,
window_size=90,
# whitelist: <td>, </td>
whitelist_token_ids={128821, 128822},
),
skip_special_tokens=False,
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
sampling_params=sampling_params,
)
# exaone4_5
def load_exaone4_5(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "LGAI-EXAONE/EXAONE-4.5-33B"
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
max_num_seqs=2,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
}
]
processor = AutoProcessor.from_pretrained(model_name)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_gemma3(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "google/gemma-3-4b-it"
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
max_num_seqs=2,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
}
]
processor = AutoProcessor.from_pretrained(model_name)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_granite4_vision(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "ibm-granite/granite-vision-4.1-4b"
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=16,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
}
]
processor = AutoProcessor.from_pretrained(model_name)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_h2ovl(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "h2oai/h2ovl-mississippi-800m"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=8192,
limit_mm_per_prompt={"image": len(image_urls)},
mm_processor_kwargs={"max_dynamic_patch": 4},
)
placeholders = "\n".join(
f"Image-{i}: <image>\n" for i, _ in enumerate(image_urls, start=1)
)
messages = [{"role": "user", "content": f"{placeholders}\n{question}"}]
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
prompt = tokenizer.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
# Stop tokens for H2OVL-Mississippi
# https://huggingface.co/h2oai/h2ovl-mississippi-800m
stop_token_ids = [tokenizer.eos_token_id]
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
stop_token_ids=stop_token_ids,
image_data=[fetch_image(url) for url in image_urls],
)
# HunyuanOCR
def load_hunyuan_vl(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "tencent/HunyuanOCR"
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholder = (
"<｜hy_place▁holder▁no▁100｜><｜hy_place▁holder▁no▁102｜><｜hy_place▁holder▁no▁101｜>" # noqa: E501
) * len(image_urls)
prompt = f"<｜hy_begin▁of▁sentence｜>{placeholder}{question}<｜hy_User｜>"
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_idefics3(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "HuggingFaceM4/Idefics3-8B-Llama3"
# The configuration below has been confirmed to launch on a single L40 GPU.
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
max_num_seqs=16,
enforce_eager=True,
limit_mm_per_prompt={"image": len(image_urls)},
# if you are running out of memory, you can reduce the "longest_edge".
# see: https://huggingface.co/HuggingFaceM4/Idefics3-8B-Llama3#model-optimizations
mm_processor_kwargs={
"size": {"longest_edge": 2 * 364},
},
)
placeholders = "\n".join(
f"Image-{i}: <image>\n" for i, _ in enumerate(image_urls, start=1)
)
prompt = f"<|begin_of_text|>User:{placeholders}\n{question}<end_of_utterance>\nAssistant:" # noqa: E501
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_interns1(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "internlm/Intern-S1-mini"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=4096,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = "\n".join(
f"Image-{i}: <IMG_CONTEXT>\n" for i, _ in enumerate(image_urls, start=1)
)
messages = [{"role": "user", "content": f"{placeholders}\n{question}"}]
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
prompt = tokenizer.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_internvl(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "OpenGVLab/InternVL2-2B"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=4096,
limit_mm_per_prompt={"image": len(image_urls)},
mm_processor_kwargs={"max_dynamic_patch": 4},
)
placeholders = "\n".join(
f"Image-{i}: <image>\n" for i, _ in enumerate(image_urls, start=1)
)
messages = [{"role": "user", "content": f"{placeholders}\n{question}"}]
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
prompt = tokenizer.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
# Stop tokens for InternVL
# models variants may have different stop tokens
# please refer to the model card for the correct "stop words":
# https://huggingface.co/OpenGVLab/InternVL2-2B/blob/main/conversation.py
stop_tokens = ["<|endoftext|>", "<|im_start|>", "<|im_end|>", "<|end|>"]
stop_token_ids = [tokenizer.convert_tokens_to_ids(i) for i in stop_tokens]
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
stop_token_ids=stop_token_ids,
image_data=[fetch_image(url) for url in image_urls],
)
def load_keye_vl(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "Kwai-Keye/Keye-VL-8B-Preview"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=8192,
max_num_seqs=5,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
},
]
processor = AutoProcessor.from_pretrained(model_name, trust_remote_code=True)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
image_data = [fetch_image(url) for url in image_urls]
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=image_data,
)
def load_keye_vl1_5(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "Kwai-Keye/Keye-VL-1_5-8B"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=32768,
max_num_seqs=5,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
},
]
processor = AutoProcessor.from_pretrained(model_name, trust_remote_code=True)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
image_data = [fetch_image(url) for url in image_urls]
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=image_data,
)
def load_kimi_vl(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "moonshotai/Kimi-VL-A3B-Instruct"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=4096,
max_num_seqs=4,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
}
]
processor = AutoProcessor.from_pretrained(model_name, trust_remote_code=True)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_llama4(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "meta-llama/Llama-4-Scout-17B-16E-Instruct"
engine_args = EngineArgs(
model=model_name,
max_model_len=131072,
tensor_parallel_size=8,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
}
]
processor = AutoProcessor.from_pretrained(model_name)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_llava(question: str, image_urls: list[str]) -> ModelRequestData:
# NOTE: CAUTION! Original Llava models wasn't really trained on multi-image inputs,
# it will generate poor response for multi-image inputs!
model_name = "llava-hf/llava-1.5-7b-hf"
engine_args = EngineArgs(
model=model_name,
max_num_seqs=16,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
}
]
processor = AutoProcessor.from_pretrained(model_name)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_llava_next(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "llava-hf/llava-v1.6-mistral-7b-hf"
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
max_num_seqs=16,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
}
]
processor = AutoProcessor.from_pretrained(model_name)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_llava_onevision(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "llava-hf/llava-onevision-qwen2-7b-ov-hf"
engine_args = EngineArgs(
model=model_name,
max_model_len=16384,
max_num_seqs=16,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
}
]
processor = AutoProcessor.from_pretrained(model_name)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_mistral3(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "mistralai/Mistral-Small-3.1-24B-Instruct-2503"
# Adjust this as necessary to fit in GPU
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
max_num_seqs=2,
tensor_parallel_size=2,
limit_mm_per_prompt={"image": len(image_urls)},
ignore_patterns=["consolidated.safetensors"],
)
placeholders = "[IMG]" * len(image_urls)
prompt = f"<s>[INST]{question}\n{placeholders}[/INST]"
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_nvlm_d(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "nvidia/NVLM-D-72B"
# Adjust this as necessary to fit in GPU
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=8192,
tensor_parallel_size=4,
limit_mm_per_prompt={"image": len(image_urls)},
mm_processor_kwargs={"max_dynamic_patch": 4},
)
placeholders = "\n".join(
f"Image-{i}: <image>\n" for i, _ in enumerate(image_urls, start=1)
)
messages = [{"role": "user", "content": f"{placeholders}\n{question}"}]
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
prompt = tokenizer.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
# OpenPangu
def load_openpangu_vl(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "FreedomIntelligence/openPangu-VL-7B"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=8192,
max_num_seqs=2,
enforce_eager=True,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = "[unused18][unused19][unused20]" * len(image_urls)
prompt = (
f"<s>[unused9]系统：[unused10][unused9]用户：{question}{placeholders}"
"[unused10][unused9]助手："
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
# Ovis
def load_ovis(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "AIDC-AI/Ovis2-1B"
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
max_num_seqs=2,
trust_remote_code=True,
dtype="half",
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = "\n".join(
f"Image-{i}: <image>\n" for i, _ in enumerate(image_urls, start=1)
)
messages = [{"role": "user", "content": f"{placeholders}\n{question}"}]
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
prompt = tokenizer.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
# ovis2_5
def load_ovis2_5(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "AIDC-AI/Ovis2.5-2B"
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
max_num_seqs=2,
trust_remote_code=True,
dtype="half",
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = "\n".join(
f"Image-{i}: <image>\n" for i, _ in enumerate(image_urls, start=1)
)
prompt = (
f"<|im_start|>user\n\n{placeholders}\n{question}<|im_end|>\n"
"<|im_start|>assistant\n"
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_paddleocr_vl(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "PaddlePaddle/PaddleOCR-VL"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=8192,
max_num_seqs=2,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = "<|IMAGE_START|><|IMAGE_PLACEHOLDER|><|IMAGE_END|>" * len(image_urls)
prompt = f"<|begin_of_sentence|>User: {question}{placeholders}\nAssistant: "
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_pixtral_hf(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "mistral-community/pixtral-12b"
# Adjust this as necessary to fit in GPU
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
max_num_seqs=2,
tensor_parallel_size=2,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = "[IMG]" * len(image_urls)
prompt = f"<s>[INST]{question}\n{placeholders}[/INST]"
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_phi3v(question: str, image_urls: list[str]) -> ModelRequestData:
# num_crops is an override kwarg to the multimodal image processor;
# For some models, e.g., Phi-3.5-vision-instruct, it is recommended
# to use 16 for single frame scenarios, and 4 for multi-frame.
#
# Generally speaking, a larger value for num_crops results in more
# tokens per image instance, because it may scale the image more in
# the image preprocessing. Some references in the model docs and the
# formula for image tokens after the preprocessing
# transform can be found below.
#
# https://huggingface.co/microsoft/Phi-3.5-vision-instruct#loading-the-model-locally
# https://huggingface.co/microsoft/Phi-3.5-vision-instruct/blob/main/processing_phi3_v.py#L194
engine_args = EngineArgs(
model="microsoft/Phi-3.5-vision-instruct",
trust_remote_code=True,
max_model_len=4096,
max_num_seqs=2,
limit_mm_per_prompt={"image": len(image_urls)},
mm_processor_kwargs={"num_crops": 4},
)
placeholders = "\n".join(
f"<|image_{i}|>" for i, _ in enumerate(image_urls, start=1)
)
prompt = f"<|user|>\n{placeholders}\n{question}<|end|>\n<|assistant|>\n"
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_phi4mm(question: str, image_urls: list[str]) -> ModelRequestData:
"""Phi-4-multimodal-instruct supports both image and audio inputs. Here, we
show how to process multi images inputs.
"""
model_path = snapshot_download("microsoft/Phi-4-multimodal-instruct")
# Since the vision-lora and speech-lora co-exist with the base model,
# we have to manually specify the path of the lora weights.
vision_lora_path = os.path.join(model_path, "vision-lora")
engine_args = EngineArgs(
model=model_path,
trust_remote_code=True,
max_model_len=4096,
max_num_seqs=2,
limit_mm_per_prompt={"image": len(image_urls)},
enable_lora=True,
max_lora_rank=320,
# Note - mm_processor_kwargs can also be passed to generate/chat calls
mm_processor_kwargs={"dynamic_hd": 4},
)
placeholders = "".join(f"<|image_{i}|>" for i, _ in enumerate(image_urls, start=1))
prompt = f"<|user|>{placeholders}{question}<|end|><|assistant|>"
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
lora_requests=[LoRARequest("vision", 1, vision_lora_path)],
)
def load_phi4siglip(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "microsoft/Phi-4-reasoning-vision-15B"
placeholders = "\n".join("<image>" for _ in image_urls)
prompt = f"<|user|>\n{placeholders}\n{question}<|end|>\n<|assistant|>\n"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=8192,
max_num_seqs=2,
limit_mm_per_prompt={"image": len(image_urls)},
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_qwen2_vl(question: str, image_urls: list[str]) -> ModelRequestData:
try:
from qwen_vl_utils import smart_resize
except ModuleNotFoundError:
print(
"WARNING: `qwen-vl-utils` not installed, input images will not "
"be automatically resized. You can enable this functionality by "
"`pip install qwen-vl-utils`."
)
smart_resize = None
model_name = "Qwen/Qwen2-VL-7B-Instruct"
# Tested on L40
engine_args = EngineArgs(
model=model_name,
max_model_len=32768 if smart_resize is None else 4096,
max_num_seqs=5,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{"role": "system", "content": "You are a helpful assistant."},
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
},
]
processor = AutoProcessor.from_pretrained(model_name)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
if smart_resize is None:
image_data = [fetch_image(url) for url in image_urls]
else:
def post_process_image(image: Image) -> Image:
width, height = image.size
resized_height, resized_width = smart_resize(
height, width, max_pixels=1024 * 28 * 28
)
return image.resize((resized_width, resized_height))
image_data = [post_process_image(fetch_image(url)) for url in image_urls]
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=image_data,
)
def load_qwen2_5_vl(question: str, image_urls: list[str]) -> ModelRequestData:
try:
from qwen_vl_utils import smart_resize
except ModuleNotFoundError:
print(
"WARNING: `qwen-vl-utils` not installed, input images will not "
"be automatically resized. You can enable this functionality by "
"`pip install qwen-vl-utils`."
)
smart_resize = None
model_name = "Qwen/Qwen2.5-VL-3B-Instruct"
engine_args = EngineArgs(
model=model_name,
max_model_len=32768 if smart_resize is None else 4096,
max_num_seqs=5,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{"role": "system", "content": "You are a helpful assistant."},
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
},
]
processor = AutoProcessor.from_pretrained(model_name)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
if smart_resize is None:
image_data = [fetch_image(url) for url in image_urls]
else:
def post_process_image(image: Image) -> Image:
width, height = image.size
resized_height, resized_width = smart_resize(
height, width, max_pixels=1024 * 28 * 28
)
return image.resize((resized_width, resized_height))
image_data = [post_process_image(fetch_image(url)) for url in image_urls]
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=image_data,
)
def load_r_vl(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "YannQi/R-4B"
engine_args = EngineArgs(
model=model_name,
max_model_len=16384,
max_num_seqs=16,
trust_remote_code=True,
limit_mm_per_prompt={"image": len(image_urls)},
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
}
]
processor = AutoProcessor.from_pretrained(model_name, trust_remote_code=True)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_smolvlm(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "HuggingFaceTB/SmolVLM2-2.2B-Instruct"
# The configuration below has been confirmed to launch on a single L40 GPU.
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
max_num_seqs=16,
enforce_eager=True,
limit_mm_per_prompt={"image": len(image_urls)},
mm_processor_kwargs={
"max_image_size": {"longest_edge": 384},
},
)
placeholders = "\n".join(
f"Image-{i}: <image>\n" for i, _ in enumerate(image_urls, start=1)
)
prompt = (
f"<|im_start|>User:{placeholders}\n{question}<end_of_utterance>\nAssistant:" # noqa: E501
)
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=[fetch_image(url) for url in image_urls],
)
def load_step3(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "stepfun-ai/step3-fp8"
# NOTE: Below are verified configurations for step3-fp8
# on 8xH100 GPUs.
engine_args = EngineArgs(
model=model_name,
max_num_batched_tokens=4096,
gpu_memory_utilization=0.85,
tensor_parallel_size=8,
limit_mm_per_prompt={"image": len(image_urls)},
reasoning_parser="step3",
)
prompt = (
"<｜begin▁of▁sentence｜> You are a helpful assistant. <|BOT|>user\n "
f"{'<im_patch>' * len(image_urls)}{question} <|EOT|><|BOT|"
">assistant\n<think>\n"
)
image_data = [fetch_image(url) for url in image_urls]
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=image_data,
)
def load_step_vl(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "stepfun-ai/Step3-VL-10B"
engine_args = EngineArgs(
model=model_name,
max_num_batched_tokens=4096,
limit_mm_per_prompt={"image": len(image_urls)},
hf_overrides={"vision_config": {"enable_patch": False}},
trust_remote_code=True,
reasoning_parser="deepseek_r1",
)
prompt = (
"<｜begin▁of▁sentence｜> You are a helpful assistant.<|BOT|>user\n "
f"{'<im_patch>' * len(image_urls)}{question}<|EOT|><|BOT|>"
"assistant\n<think>\n"
)
image_data = [fetch_image(url) for url in image_urls]
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=image_data,
)
# GLM-4.1V
def load_glm4_1v(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "zai-org/GLM-4.1V-9B-Thinking"
engine_args = EngineArgs(
model=model_name,
max_model_len=45082,
max_num_seqs=2,
limit_mm_per_prompt={"image": len(image_urls)},
enforce_eager=True,
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
}
]
processor = AutoProcessor.from_pretrained(model_name)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
image_data = [fetch_image(url) for url in image_urls]
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=image_data,
)
# GLM-4.5V
def load_glm4_5v(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "zai-org/GLM-4.5V"
engine_args = EngineArgs(
model=model_name,
max_model_len=32768,
max_num_seqs=2,
limit_mm_per_prompt={"image": len(image_urls)},
enforce_eager=True,
tensor_parallel_size=4,
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
}
]
processor = AutoProcessor.from_pretrained(model_name)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
image_data = [fetch_image(url) for url in image_urls]
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=image_data,
)
# GLM-4.5V-FP8
def load_glm4_5v_fp8(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "zai-org/GLM-4.5V-FP8"
engine_args = EngineArgs(
model=model_name,
max_model_len=32768,
max_num_seqs=2,
limit_mm_per_prompt={"image": len(image_urls)},
enforce_eager=True,
tensor_parallel_size=4,
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
}
]
processor = AutoProcessor.from_pretrained(model_name)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
image_data = [fetch_image(url) for url in image_urls]
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=image_data,
)
def load_molmo2(question: str, image_urls: list[str]) -> ModelRequestData:
model_name = "allenai/Molmo2-8B"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
dtype="bfloat16",
limit_mm_per_prompt={"image": len(image_urls)},
max_num_batched_tokens=36864,
)
placeholders = [{"type": "image", "image": url} for url in image_urls]
messages = [
{
"role": "user",
"content": [
*placeholders,
{"type": "text", "text": question},
],
},
]
processor = AutoProcessor.from_pretrained(model_name)
prompt = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
image_data = [fetch_image(url) for url in image_urls]
return ModelRequestData(
engine_args=engine_args,
prompt=prompt,
image_data=image_data,
)
model_example_map = {
"aria": load_aria,
"bee": load_bee,
"command_a_vision": load_command_a_vision,
"deepseek_vl_v2": load_deepseek_vl2,
"deepseek_ocr": load_deepseek_ocr,
"exaone4_5": load_exaone4_5,
"gemma3": load_gemma3,
"granite4_vision": load_granite4_vision,
"h2ovl_chat": load_h2ovl,
"hunyuan_vl": load_hunyuan_vl,
"idefics3": load_idefics3,
"interns1": load_interns1,
"internvl_chat": load_internvl,
"keye_vl": load_keye_vl,
"keye_vl1_5": load_keye_vl1_5,
"kimi_vl": load_kimi_vl,
"llama4": load_llama4,
"llava": load_llava,
"llava-next": load_llava_next,
"llava-onevision": load_llava_onevision,
"mistral3": load_mistral3,
"molmo2": load_molmo2,
"NVLM_D": load_nvlm_d,
"openpangu_vl": load_openpangu_vl,
"ovis": load_ovis,
"ovis2_5": load_ovis2_5,
"paddleocr_vl": load_paddleocr_vl,
"phi3_v": load_phi3v,
"phi4_mm": load_phi4mm,
"phi4_siglip": load_phi4siglip,
"pixtral_hf": load_pixtral_hf,
"qwen2_vl": load_qwen2_vl,
"qwen2_5_vl": load_qwen2_5_vl,
"rvl": load_r_vl,
"smolvlm": load_smolvlm,
"step3": load_step3,
"stepvl": load_step_vl,
"glm4_1v": load_glm4_1v,
"glm4_5v": load_glm4_5v,
"glm4_5v_fp8": load_glm4_5v_fp8,
}
def run_generate(
model,
question: str,
image_urls: list[str],
seed: int,
tensor_parallel_size: int | None,
):
req_data = model_example_map[model](question, image_urls)
engine_args = req_data.engine_args
engine_args.seed = seed
if tensor_parallel_size is not None:
engine_args.tensor_parallel_size = tensor_parallel_size
if current_platform.is_rocm():
os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"
llm = LLM.from_engine_args(engine_args)
sampling_params = SamplingParams(
temperature=0.0, max_tokens=256, stop_token_ids=req_data.stop_token_ids
)
outputs = llm.generate(
{
"prompt": req_data.prompt,
"multi_modal_data": {"image": req_data.image_data},
},
sampling_params=sampling_params,
lora_request=req_data.lora_requests,
)
print("-" * 50)
for o in outputs:
generated_text = o.outputs[0].text
print(generated_text)
print("-" * 50)
def run_chat(
model: str,
question: str,
image_urls: list[str],
seed: int,
tensor_parallel_size: int | None,
):
req_data = model_example_map[model](question, image_urls)
# Disable other modalities to save memory
default_limits = {"image": 0, "video": 0, "audio": 0}
req_data.engine_args.limit_mm_per_prompt = default_limits | dict(
req_data.engine_args.limit_mm_per_prompt or {}
)
engine_args = req_data.engine_args
engine_args.seed = seed
if tensor_parallel_size is not None:
engine_args.tensor_parallel_size = tensor_parallel_size
if current_platform.is_rocm():
os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"
llm = LLM.from_engine_args(engine_args)
sampling_params = (
SamplingParams(
temperature=0.0, max_tokens=256, stop_token_ids=req_data.stop_token_ids
)
if req_data.sampling_params is None
else req_data.sampling_params
)
outputs = llm.chat(
[
{
"role": "user",
"content": [
{
"type": "text",
"text": question,
},
*(
{
"type": "image_url",
"image_url": {"url": image_url},
}
for image_url in image_urls
),
],
}
],
sampling_params=sampling_params,
chat_template=req_data.chat_template,
lora_request=req_data.lora_requests,
)
print("-" * 50)
for o in outputs:
generated_text = o.outputs[0].text
print(generated_text)
print("-" * 50)
def parse_args():
parser = FlexibleArgumentParser(
description="Demo on using vLLM for offline inference with "
"vision language models that support multi-image input for text "
"generation"
)
parser.add_argument(
"--model-type",
"-m",
type=str,
default="phi3_v",
choices=model_example_map.keys(),
help='Huggingface "model_type".',
)
parser.add_argument(
"--method",
type=str,
default="generate",
choices=["generate", "chat"],
help="The method to run in `vllm.LLM`.",
)
parser.add_argument(
"--seed",
type=int,
default=0,
help="Set the seed when initializing `vllm.LLM`.",
)
parser.add_argument(
"--num-images",
"-n",
type=int,
choices=list(range(1, len(IMAGE_URLS) + 1)), # the max number of images
default=2,
help="Number of images to use for the demo.",
)
parser.add_argument(
"--tensor-parallel-size",
"-tp",
type=int,
default=None,
help="Tensor parallel size to override the model's default setting. ",
)
return parser.parse_args()
def main(args: Namespace):
model = args.model_type
method = args.method
seed = args.seed
tensor_parallel_size = args.tensor_parallel_size
if tensor_parallel_size is not None and tensor_parallel_size < 1:
raise ValueError(
f"tensor_parallel_size must be a positive integer, "
f"got {tensor_parallel_size}"
)
image_urls = IMAGE_URLS[: args.num_images]
if method == "generate":
run_generate(model, QUESTION, image_urls, seed, tensor_parallel_size)
elif method == "chat":
run_chat(model, QUESTION, image_urls, seed, tensor_parallel_size)
else:
raise ValueError(f"Invalid method: {method}")
if __name__ == "__main__":
args = parse_args()
main(args)


## Vision Language Offline[¶](https://docs.vllm.ai#vision-language-offline)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""This example shows how to use vLLM for running offline inference with
the correct prompt format on vision language models for text generation.
For most models, the prompt format should follow corresponding examples
on HuggingFace model repository.
"""
import os
import random
from contextlib import contextmanager
from typing import NamedTuple
from huggingface_hub import snapshot_download
from transformers import AutoProcessor, AutoTokenizer
from vllm import LLM, EngineArgs, SamplingParams
from vllm.assets.image import ImageAsset
from vllm.assets.video import VideoAsset
from vllm.lora.request import LoRARequest
from vllm.multimodal.image import convert_image_mode
from vllm.platforms import current_platform
from vllm.utils.argparse_utils import FlexibleArgumentParser
class ModelRequestData(NamedTuple):
engine_args: EngineArgs
prompts: list[str]
stop_token_ids: list[int] | None = None
lora_requests: list[LoRARequest] | None = None
sampling_params: list[SamplingParams] | None = None
# NOTE: The default `max_num_seqs` and `max_model_len` may result in OOM on
# lower-end GPUs.
# Unless specified, these settings have been tested to work on a single L4.
# Aria
def run_aria(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "rhymes-ai/Aria"
# NOTE: Need L40 (or equivalent) to avoid OOM
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=2,
dtype="bfloat16",
limit_mm_per_prompt={modality: 1},
)
prompts = [
(
f"<|im_start|>user\n<fim_prefix><|img|><fim_suffix>{question}"
"<|im_end|>\n<|im_start|>assistant\n"
)
for question in questions
]
stop_token_ids = [93532, 93653, 944, 93421, 1019, 93653, 93519]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
stop_token_ids=stop_token_ids,
)
# Bee-8B
def run_bee(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "Open-Bee/Bee-8B-RL"
prompts = [
(
f"<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n"
f"<|im_start|>user\n<image>\n{question}<|im_end|>"
f"<|im_start|>assistant\n<think>\n"
)
for question in questions
]
engine_args = EngineArgs(
model=model_name,
max_model_len=16384,
limit_mm_per_prompt={modality: 1},
trust_remote_code=True,
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
def run_bagel(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "ByteDance-Seed/BAGEL-7B-MoT"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=8192,
max_num_seqs=2,
limit_mm_per_prompt={modality: 1},
)
prompts = [
(
f"<|im_start|>user\n<|image_pad|>\n{question}<|im_end|>\n"
f"<|im_start|>assistant\n"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# BLIP-2
def run_blip2(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
# BLIP-2 prompt format is inaccurate on HuggingFace model repository.
# See https://huggingface.co/Salesforce/blip2-opt-2.7b/discussions/15#64ff02f3f8cf9e4f5b038262 #noqa
prompts = [f"Question: {question} Answer:" for question in questions]
engine_args = EngineArgs(
model="Salesforce/blip2-opt-2.7b",
limit_mm_per_prompt={modality: 1},
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
def run_command_a_vision(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "CohereLabs/command-a-vision-07-2025"
engine_args = EngineArgs(
model=model_name,
max_model_len=32768,
tensor_parallel_size=4,
limit_mm_per_prompt={modality: 1},
)
prompts = [
f"<|START_OF_TURN_TOKEN|><|USER_TOKEN|><|IMG_PATCH|>{question}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>"
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Deepseek-VL2
def run_deepseek_vl2(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "deepseek-ai/deepseek-vl2-tiny"
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=2,
hf_overrides={"architectures": ["DeepseekVLV2ForCausalLM"]},
limit_mm_per_prompt={modality: 1},
)
prompts = [
f"<|User|>: <image>\n{question}\n\n<|Assistant|>:" for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
def run_deepseek_ocr(questions: list[str], modality: str) -> ModelRequestData:
from vllm.model_executor.models.deepseek_ocr import NGramPerReqLogitsProcessor
assert modality == "image"
model_name = "deepseek-ai/DeepSeek-OCR"
engine_args = EngineArgs(
model=model_name,
limit_mm_per_prompt={modality: 1},
logits_processors=[NGramPerReqLogitsProcessor],
)
# deepseek-ocr use plain prompt template
prompts = [f"<image>\n{question}" for question in questions]
# The following sampling params config is taken from
# the official Deepseek-OCR inference example.
# (IMPORTANT) Use the custom logits processor and avoid skipping
# special tokens for this model for the optimal OCR performance.
sampling_params = [
SamplingParams(
temperature=0.0,
max_tokens=8192,
# ngram logit processor args
extra_args=dict(
ngram_size=30,
window_size=90,
# whitelist: <td>, </td>
whitelist_token_ids={128821, 128822},
),
skip_special_tokens=False,
)
for _ in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
sampling_params=sampling_params,
)
def run_deepseek_ocr2(questions: list[str], modality: str) -> ModelRequestData:
from vllm.model_executor.models.deepseek_ocr import NGramPerReqLogitsProcessor
assert modality == "image"
model_name = "deepseek-ai/DeepSeek-OCR-2"
engine_args = EngineArgs(
model=model_name,
limit_mm_per_prompt={modality: 1},
logits_processors=[NGramPerReqLogitsProcessor],
)
# deepseek-ocr use plain prompt template
prompts = [f"<image>\n{question}" for question in questions]
# The following sampling params config is taken from
# the official Deepseek-OCR inference example.
# (IMPORTANT) Use the custom logits processor and avoid skipping
# special tokens for this model for the optimal OCR performance.
sampling_params = [
SamplingParams(
temperature=0.0,
max_tokens=8192,
# ngram logit processor args
extra_args=dict(
ngram_size=30,
window_size=90,
# whitelist: <td>, </td>
whitelist_token_ids={128821, 128822},
),
skip_special_tokens=False,
)
for _ in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
sampling_params=sampling_params,
)
# Dots-OCR
def run_dots_ocr(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
prompts = [f"<|img|><|imgpad|><|endofimg|>{question}" for question in questions]
engine_args = EngineArgs(
model="rednote-hilab/dots.ocr",
limit_mm_per_prompt={modality: 1},
trust_remote_code=True,
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Eagle2.5-VL
def run_eagle2_5(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "nvidia/Eagle2.5-8B"
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=2,
trust_remote_code=True,
limit_mm_per_prompt={modality: 1},
)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
messages = [
[{"role": "user", "content": f"<image>\n{question}"}] for question in questions
]
prompts = tokenizer.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
# Stop tokens for Eagle2.5 (Qwen2 based)
stop_tokens = ["<|endoftext|>", "<|im_start|>", "<|im_end|>"]
stop_token_ids = [tokenizer.convert_tokens_to_ids(i) for i in stop_tokens]
stop_token_ids = [token_id for token_id in stop_token_ids if token_id is not None]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
stop_token_ids=stop_token_ids,
)
# Ernie4.5-VL
def run_ernie45_vl(questions: list[str], modality: str) -> ModelRequestData:
model_name = "baidu/ERNIE-4.5-VL-28B-A3B-PT"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=5,
limit_mm_per_prompt=mm_limit,
trust_remote_code=True,
)
image_placeholder = "Picture 1:<|IMAGE_START|><|image@placeholder|><|IMAGE_END|>"
video_placeholder = "Video 1:<|VIDEO_START|><|video@placeholder|><|VIDEO_END|>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + video_placeholder
prompts = [
(
f"<|begin_of_sentence|>User: {question}{placeholder}\n"
"Assistant: <think></think>"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# EXAONE-4.5
def run_exaone4_5(questions: list[str], modality: str) -> ModelRequestData:
model_name = "LGAI-EXAONE/EXAONE-4.5-33B"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=5,
mm_processor_kwargs={
"min_pixels": 28 * 28,
"max_pixels": 1280 * 28 * 28,
"fps": 1,
},
limit_mm_per_prompt=mm_limit,
)
image_placeholder = "<vision><|image_pad|></vision>"
video_placeholder = "<vision><|video_pad|></vision>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + video_placeholder
prompts = [
(
"<|system|>\nYou are a helpful assistant.<|endofturn|>\n"
f"<|user|>\n{placeholder}"
f"{question}<|endofturn|>\n"
"<|assistant|>\n"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Gemma 3
def run_gemma3(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "google/gemma-3-4b-it"
engine_args = EngineArgs(
model=model_name,
max_model_len=2048,
max_num_seqs=2,
mm_processor_kwargs={"do_pan_and_scan": True},
limit_mm_per_prompt={modality: 1},
)
prompts = [
(
"<bos><start_of_turn>user\n"
f"<start_of_image>{question}<end_of_turn>\n"
"<start_of_turn>model\n"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Gemma3N
def run_gemma3n(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "google/gemma-3n-E2B-it"
engine_args = EngineArgs(
model=model_name,
max_model_len=2048,
max_num_seqs=2,
limit_mm_per_prompt={modality: 1},
enforce_eager=True,
)
prompts = [
(
"<start_of_turn>user\n"
f"<image_soft_token>{question}<end_of_turn>\n"
"<start_of_turn>model\n"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Gemma 4
def run_gemma4(questions: list[str], modality: str) -> ModelRequestData:
assert modality in ("image", "video")
model_name = "google/gemma-4-31B-it"
# NOTE: Gemma-4-31B is a large model. Users running into Out-Of-Memory (OOM)
# errors might need to set `tensor_parallel_size` to > 1.
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=2,
limit_mm_per_prompt={modality: 1},
)
if modality == "image":
prompts = [
(
"<bos><start_of_turn>user\n"
f"<|image|>\n{question}<end_of_turn>\n"
"<start_of_turn>model\n"
)
for question in questions
]
else: # video
prompts = [
(
"<bos><start_of_turn>user\n"
f"<|video|>\n{question}<end_of_turn>\n"
"<start_of_turn>model\n"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# GLM-4v
def run_glm4v(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "zai-org/glm-4v-9b"
engine_args = EngineArgs(
model=model_name,
max_model_len=2048,
max_num_seqs=2,
trust_remote_code=True,
enforce_eager=True,
hf_overrides={"architectures": ["GLM4VForCausalLM"]},
limit_mm_per_prompt={modality: 1},
)
prompts = [
(
"<|user|>\n<|begin_of_image|><|endoftext|><|end_of_image|>"
f"{question}<|assistant|>"
)
for question in questions
]
stop_token_ids = [151329, 151336, 151338]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
stop_token_ids=stop_token_ids,
)
# GLM-4.1V
def run_glm4_1v(questions: list[str], modality: str) -> ModelRequestData:
model_name = "zai-org/GLM-4.1V-9B-Thinking"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=2,
mm_processor_kwargs={
"size": {"shortest_edge": 12544, "longest_edge": 47040000},
"fps": 1,
},
limit_mm_per_prompt=mm_limit,
enforce_eager=True,
)
image_placeholder = "<|begin_of_image|><|image|><|end_of_image|>"
video_placeholder = "<|begin_of_video|><|video|><|end_of_video|>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + video_placeholder
prompts = [
(
"[gMASK]<sop><|system|>\nYou are a helpful assistant.<|user|>\n"
f"{placeholder}"
f"{question}<|assistant|>assistant\n"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# GLM-4.5V
def run_glm4_5v(questions: list[str], modality: str) -> ModelRequestData:
model_name = "zai-org/GLM-4.5V"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=2,
mm_processor_kwargs={
"size": {"shortest_edge": 12544, "longest_edge": 47040000},
"fps": 1,
},
limit_mm_per_prompt=mm_limit,
enforce_eager=True,
tensor_parallel_size=4,
)
image_placeholder = "<|begin_of_image|><|image|><|end_of_image|>"
video_placeholder = "<|begin_of_video|><|video|><|end_of_video|>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + video_placeholder
prompts = [
(
"[gMASK]<sop><|system|>\nYou are a helpful assistant.<|user|>\n"
f"{placeholder}"
f"{question}<|assistant|>assistant\n"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# GLM-4.5V-FP8
def run_glm4_5v_fp8(questions: list[str], modality: str) -> ModelRequestData:
model_name = "zai-org/GLM-4.5V-FP8"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=2,
mm_processor_kwargs={
"size": {"shortest_edge": 12544, "longest_edge": 47040000},
"fps": 1,
},
limit_mm_per_prompt=mm_limit,
enforce_eager=True,
tensor_parallel_size=4,
)
image_placeholder = "<|begin_of_image|><|image|><|end_of_image|>"
video_placeholder = "<|begin_of_video|><|video|><|end_of_video|>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + video_placeholder
prompts = [
(
"[gMASK]<sop><|system|>\nYou are a helpful assistant.<|user|>\n"
f"{placeholder}"
f"{question}<|assistant|>assistant\n"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# GLM-OCR
def run_glm_ocr(questions: list[str], modality: str) -> ModelRequestData:
model_name = "zai-org/GLM-OCR"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=2,
mm_processor_kwargs={
"size": {"shortest_edge": 12544, "longest_edge": 47040000},
"fps": 1,
},
limit_mm_per_prompt=mm_limit,
enforce_eager=True,
)
image_placeholder = "<|begin_of_image|><|image|><|end_of_image|>"
video_placeholder = "<|begin_of_video|><|video|><|end_of_video|>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + video_placeholder
prompts = [
(
"[gMASK]<sop><|system|>\nYou are a helpful assistant.<|user|>\n"
f"{placeholder}"
f"{question}<|assistant|>assistant\n"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# H2OVL-Mississippi
def run_h2ovl(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "h2oai/h2ovl-mississippi-800m"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=8192,
limit_mm_per_prompt={modality: 1},
)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
messages = [
[{"role": "user", "content": f"<image>\n{question}"}] for question in questions
]
prompts = tokenizer.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
# Stop tokens for H2OVL-Mississippi
# https://huggingface.co/h2oai/h2ovl-mississippi-800m
stop_token_ids = [tokenizer.eos_token_id]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
stop_token_ids=stop_token_ids,
)
# HunyuanOCR
def run_hunyuan_vl(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "tencent/HunyuanOCR"
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
limit_mm_per_prompt={modality: 1},
)
placeholder = "<｜hy_place▁holder▁no▁100｜><｜hy_place▁holder▁no▁102｜><｜hy_place▁holder▁no▁101｜>" # noqa: E501
prompts = [
f"<｜hy_begin▁of▁sentence｜>{placeholder}{question}<｜hy_User｜>"
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
stop_token_ids=None,
)
# Idefics3-8B-Llama3
def run_idefics3(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "HuggingFaceM4/Idefics3-8B-Llama3"
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
max_num_seqs=2,
enforce_eager=True,
# if you are running out of memory, you can reduce the "longest_edge".
# see: https://huggingface.co/HuggingFaceM4/Idefics3-8B-Llama3#model-optimizations
mm_processor_kwargs={
"size": {"longest_edge": 3 * 364},
},
limit_mm_per_prompt={modality: 1},
)
prompts = [
(f"<|begin_of_text|>User:<image>{question}<end_of_utterance>\nAssistant:")
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Intern-S1
def run_interns1(questions: list[str], modality: str) -> ModelRequestData:
model_name = "internlm/Intern-S1-mini"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=8192,
max_num_seqs=2,
limit_mm_per_prompt=mm_limit,
enforce_eager=True,
)
image_placeholder = "<IMG_CONTEXT>"
video_placeholder = "<video>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + "\n" + video_placeholder
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
messages = [
[{"role": "user", "content": f"{placeholder}\n{question}"}]
for question in questions
]
prompts = tokenizer.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Intern-S1-Pro
def run_interns1_pro(questions: list[str], modality: str) -> ModelRequestData:
model_name = "internlm/Intern-S1-Pro"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=8192,
max_num_seqs=2,
limit_mm_per_prompt=mm_limit,
enforce_eager=True,
tensor_parallel_size=4,
)
image_placeholder = "<|vision_start|><|image_pad|><|vision_end|>"
video_placeholder = "<|vision_start|><|video_pad|><|vision_end|>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + video_placeholder
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
messages = [
[{"role": "user", "content": f"{placeholder}\n{question}"}]
for question in questions
]
prompts = tokenizer.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# InternVL
def run_internvl(questions: list[str], modality: str) -> ModelRequestData:
model_name = "OpenGVLab/InternVL3-2B"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=8192,
limit_mm_per_prompt=mm_limit,
)
image_placeholder = "<image>"
video_placeholder = "<video>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + "\n" + video_placeholder
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
messages = [
[{"role": "user", "content": f"{placeholder}\n{question}"}]
for question in questions
]
prompts = tokenizer.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
# Stop tokens for InternVL
# models variants may have different stop tokens
# please refer to the model card for the correct "stop words":
# https://huggingface.co/OpenGVLab/InternVL2-2B/blob/main/conversation.py
stop_tokens = ["<|endoftext|>", "<|im_start|>", "<|im_end|>", "<|end|>"]
stop_token_ids = [tokenizer.convert_tokens_to_ids(i) for i in stop_tokens]
stop_token_ids = [token_id for token_id in stop_token_ids if token_id is not None]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
stop_token_ids=stop_token_ids,
)
# Kanana-V
def run_kanana_v(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "kakaocorp/kanana-1.5-v-3b-instruct"
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
trust_remote_code=True,
limit_mm_per_prompt={modality: 1},
)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
messages = [
[{"role": "user", "content": f"<image>\n{question}"}] for question in questions
]
prompts = tokenizer.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Keye-VL
def run_keye_vl(questions: list[str], modality: str) -> ModelRequestData:
model_name = "Kwai-Keye/Keye-VL-8B-Preview"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
trust_remote_code=True,
limit_mm_per_prompt=mm_limit,
)
image_placeholder = "<|vision_start|><|image_pad|><|vision_end|>"
video_placeholder = "<|vision_start|><|video_pad|><|vision_end|>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + video_placeholder
prompts = [
(
f"<|im_start|>user\n{placeholder}"
f"{question}<|im_end|>\n"
"<|im_start|>assistant\n"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Keye-VL-1.5
def run_keye_vl1_5(questions: list[str], modality: str) -> ModelRequestData:
model_name = "Kwai-Keye/Keye-VL-1.5-8B"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
trust_remote_code=True,
limit_mm_per_prompt=mm_limit,
)
image_placeholder = "<|vision_start|><|image_pad|><|vision_end|>"
video_placeholder = "<|vision_start|><|video_pad|><|vision_end|>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + video_placeholder
prompts = [
(
f"<|im_start|>user\n{placeholder}"
f"{question}<|im_end|>\n"
"<|im_start|>assistant\n"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Kimi-VL
def run_kimi_vl(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
prompts = [
"<|im_user|>user<|im_middle|><|media_start|>image<|media_content|>"
f"<|media_pad|><|media_end|>{question}<|im_end|>"
"<|im_assistant|>assistant<|im_middle|>"
for question in questions
]
engine_args = EngineArgs(
model="moonshotai/Kimi-VL-A3B-Instruct",
trust_remote_code=True,
max_model_len=4096,
limit_mm_per_prompt={modality: 1},
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Kimi-VL
def run_kimi_k25(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "vision_chunk"
prompts = [
"<|im_user|>user<|media_begin|>image<|media_content|>"
f"<|media_pad|><|media_end|>{question}<|im_end|>"
"<|im_assistant|>assistant<|im_middle|>"
for question in questions
]
engine_args = EngineArgs(
model="moonshotai/Kimi-K2.5",
trust_remote_code=True,
max_model_len=4096,
limit_mm_per_prompt={modality: 1},
tensor_parallel_size=4,
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# LightOnOCR
def run_lightonocr(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
prompts = [
"<|im_start|>system<|im_end|>\n<|im_start|>user\n<|image_pad|><|im_end|>\n<|im_start|>assistant\n"
for _ in questions
]
engine_args = EngineArgs(
model="lightonai/LightOnOCR-1B",
limit_mm_per_prompt={modality: 1},
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
def run_lfm2_vl(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "LiquidAI/LFM2-VL-450M"
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
limit_mm_per_prompt={modality: 1},
)
processor = AutoProcessor.from_pretrained(model_name)
messages = [
[
{
"role": "user",
"content": [{"type": "image"}, {"type": "text", "text": question}],
}
]
for question in questions
]
prompts = processor.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
def run_llama4(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "meta-llama/Llama-4-Scout-17B-16E-Instruct"
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
max_num_seqs=4,
tensor_parallel_size=8,
gpu_memory_utilization=0.4,
limit_mm_per_prompt={modality: 1},
)
tokenizer = AutoTokenizer.from_pretrained(model_name)
messages = [
[
{
"role": "user",
"content": [{"type": "image"}, {"type": "text", "text": f"{question}"}],
}
]
for question in questions
]
prompts = tokenizer.apply_chat_template(
messages, add_generation_prompt=True, tokenize=False
)
stop_token_ids = None
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
stop_token_ids=stop_token_ids,
)
# LLaVA-1.5
def run_llava(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
prompts = [f"USER: <image>\n{question}\nASSISTANT:" for question in questions]
engine_args = EngineArgs(
model="llava-hf/llava-1.5-7b-hf",
max_model_len=4096,
limit_mm_per_prompt={modality: 1},
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# LLaVA-1.6/LLaVA-NeXT
def run_llava_next(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
prompts = [f"[INST] <image>\n{question} [/INST]" for question in questions]
engine_args = EngineArgs(
model="llava-hf/llava-v1.6-mistral-7b-hf",
max_model_len=8192,
limit_mm_per_prompt={modality: 1},
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# LlaVA-NeXT-Video
# Currently only support for video input
def run_llava_next_video(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "video"
prompts = [f"USER: <video>\n{question} ASSISTANT:" for question in questions]
engine_args = EngineArgs(
model="llava-hf/LLaVA-NeXT-Video-7B-hf",
max_model_len=8192,
max_num_seqs=2,
limit_mm_per_prompt={modality: 1},
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# LLaVA-OneVision
def run_llava_onevision(questions: list[str], modality: str) -> ModelRequestData:
image_placeholder = "<image>"
video_placeholder = "<video>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + "\n" + video_placeholder
prompts = [
(f"<|im_start|>user {placeholder}\n{question}<|im_end|><|im_start|>assistant\n")
for question in questions
]
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model="llava-hf/llava-onevision-qwen2-7b-ov-hf",
max_model_len=16384,
limit_mm_per_prompt=mm_limit,
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# MiniCPM-V
def run_minicpmv_base(questions: list[str], modality: str, model_name):
assert modality in ["image", "video", "image+video"]
# If you want to use `MiniCPM-o-2_6` with audio inputs, check `audio_language_offline.py` # noqa
# 2.0
# The official repo doesn't work yet, so we need to use a fork for now
# For more details, please see: See: https://github.com/vllm-project/vllm/pull/4087#issuecomment-2250397630 # noqa
# model_name = "HwwwH/MiniCPM-V-2"
# 2.5
# model_name = "openbmb/MiniCPM-Llama3-V-2_5"
# 2.6
# model_name = "openbmb/MiniCPM-V-2_6"
# o2.6
# modality supports
# 2.0: image
# 2.5: image
# 2.6: image, video
# o2.6: image, video, audio
# model_name = "openbmb/MiniCPM-o-2_6"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=2,
trust_remote_code=True,
limit_mm_per_prompt=mm_limit,
)
# NOTE The stop_token_ids are different for various versions of MiniCPM-V
# 2.0
# stop_token_ids = [tokenizer.eos_id]
# 2.5
# stop_token_ids = [tokenizer.eos_id, tokenizer.eot_id]
# 2.6 / o2.6
stop_tokens = ["<|im_end|>", "<|endoftext|>"]
stop_token_ids = [tokenizer.convert_tokens_to_ids(i) for i in stop_tokens]
image_placeholder = "(<image>./</image>)"
video_placeholder = "(<video>./</video>)"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + "\n" + video_placeholder
prompts = [
tokenizer.apply_chat_template(
[
{
"role": "user",
"content": f"{placeholder}\n{question}",
}
],
tokenize=False,
add_generation_prompt=True,
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
stop_token_ids=stop_token_ids,
)
def run_minicpmo(questions: list[str], modality: str) -> ModelRequestData:
return run_minicpmv_base(questions, modality, "openbmb/MiniCPM-o-2_6")
def run_minicpmv(questions: list[str], modality: str) -> ModelRequestData:
return run_minicpmv_base(questions, modality, "openbmb/MiniCPM-V-2_6")
# Mistral-3 HF-format
def run_mistral3(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "mistralai/Mistral-Small-3.1-24B-Instruct-2503"
# NOTE: Need L40 (or equivalent) to avoid OOM
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
max_num_seqs=2,
tensor_parallel_size=2,
limit_mm_per_prompt={modality: 1},
ignore_patterns=["consolidated.safetensors"],
)
prompts = [f"<s>[INST]{question}\n[IMG][/INST]" for question in questions]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Molmo
def run_molmo(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "allenai/Molmo-7B-D-0924"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
dtype="bfloat16",
limit_mm_per_prompt={modality: 1},
)
prompts = [
f"<|im_start|>user <image>\n{question}<|im_end|><|im_start|>assistant\n"
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Molmo2
def run_molmo2(questions: list[str], modality: str) -> ModelRequestData:
model_name = "allenai/Molmo2-8B"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
dtype="bfloat16",
limit_mm_per_prompt=mm_limit,
max_num_batched_tokens=36864,
)
image_placeholder = "<|image|>"
video_placeholder = "<|video|>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + video_placeholder
prompts = [
f"{placeholder}<|im_start|>user\n{question}<|im_end|>\n<|im_start|>assistant\n"
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Nemontron_VL
def run_nemotron_vl(questions: list[str], modality: str) -> ModelRequestData:
model_name = "nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=8192,
limit_mm_per_prompt={modality: 1},
)
assert modality == "image"
placeholder = "<image>"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
messages = [
[{"role": "user", "content": f"{placeholder}\n{question}"}]
for question in questions
]
prompts = tokenizer.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
# Stop tokens for InternVL
# models variants may have different stop tokens
# please refer to the model card for the correct "stop words":
# https://huggingface.co/OpenGVLab/InternVL2-2B/blob/main/conversation.py
stop_tokens = ["<|endoftext|>", "<|im_start|>", "<|im_end|>", "<|end|>"]
stop_token_ids = [tokenizer.convert_tokens_to_ids(i) for i in stop_tokens]
stop_token_ids = [token_id for token_id in stop_token_ids if token_id is not None]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
stop_token_ids=stop_token_ids,
)
# NVLM-D
def run_nvlm_d(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "nvidia/NVLM-D-72B"
# Adjust this as necessary to fit in GPU
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=4096,
tensor_parallel_size=4,
limit_mm_per_prompt={modality: 1},
)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
messages = [
[{"role": "user", "content": f"<image>\n{question}"}] for question in questions
]
prompts = tokenizer.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# OpenPangu
def run_openpangu_vl(questions: list[str], modality: str) -> ModelRequestData:
model_name = "FreedomIntelligence/openPangu-VL-7B"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=4,
trust_remote_code=True,
enforce_eager=True,
limit_mm_per_prompt=mm_limit,
)
image_placeholder = "[unused19]"
video_placeholder = "[unused32]"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + video_placeholder
prompts = [
(
f"<s>[unused9]系统：[unused10][unused9]用户：[unused18]{placeholder}[unused20]{question}[unused10][unused9]助手："
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Ovis
def run_ovis(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "AIDC-AI/Ovis2-1B"
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=2,
trust_remote_code=True,
dtype="half",
limit_mm_per_prompt={modality: 1},
)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
messages = [
[{"role": "user", "content": f"<image>\n{question}"}] for question in questions
]
prompts = tokenizer.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Ovis2_5
def run_ovis2_5(questions: list[str], modality: str) -> ModelRequestData:
model_name = "AIDC-AI/Ovis2.5-2B"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=2,
trust_remote_code=True,
dtype="half",
limit_mm_per_prompt=mm_limit,
)
image_placeholder = "<image>"
video_placeholder = "<video>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + "\n" + video_placeholder
prompts = [
f"<|im_start|>user\n\n{placeholder}\n{question}<|im_end|>\n<|im_start|>assistant\n"
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# PaddleOCR-VL
def run_paddleocr_vl(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "PaddlePaddle/PaddleOCR-VL"
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=2,
limit_mm_per_prompt={modality: 1},
trust_remote_code=True,
)
placeholder = "<|IMAGE_START|><|IMAGE_PLACEHOLDER|><|IMAGE_END|>"
prompts = [
(f"<|begin_of_sentence|>User: {question}{placeholder}\nAssistant: ")
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# PaliGemma
def run_paligemma(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
# PaliGemma has special prompt format for VQA
prompts = ["caption en" for _ in questions]
engine_args = EngineArgs(
model="google/paligemma-3b-mix-224",
limit_mm_per_prompt={modality: 1},
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# PaliGemma 2
def run_paligemma2(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
# PaliGemma 2 has special prompt format for VQA
prompts = ["caption en" for _ in questions]
engine_args = EngineArgs(
model="google/paligemma2-3b-ft-docci-448",
limit_mm_per_prompt={modality: 1},
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Phi-3-Vision
def run_phi3v(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
prompts = [
f"<|user|>\n<|image_1|>\n{question}<|end|>\n<|assistant|>\n"
for question in questions
]
# num_crops is an override kwarg to the multimodal image processor;
# For some models, e.g., Phi-3.5-vision-instruct, it is recommended
# to use 16 for single frame scenarios, and 4 for multi-frame.
#
# Generally speaking, a larger value for num_crops results in more
# tokens per image instance, because it may scale the image more in
# the image preprocessing. Some references in the model docs and the
# formula for image tokens after the preprocessing
# transform can be found below.
#
# https://huggingface.co/microsoft/Phi-3.5-vision-instruct#loading-the-model-locally
# https://huggingface.co/microsoft/Phi-3.5-vision-instruct/blob/main/processing_phi3_v.py#L194
engine_args = EngineArgs(
model="microsoft/Phi-3.5-vision-instruct",
trust_remote_code=True,
max_model_len=4096,
max_num_seqs=2,
# Note - mm_processor_kwargs can also be passed to generate/chat calls
mm_processor_kwargs={"num_crops": 16},
limit_mm_per_prompt={modality: 1},
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Phi-4-multimodal-instruct
def run_phi4mm(questions: list[str], modality: str) -> ModelRequestData:
"""Phi-4-multimodal-instruct supports both image and audio inputs. Here, we
show how to process image inputs.
"""
assert modality == "image"
model_path = snapshot_download("microsoft/Phi-4-multimodal-instruct")
# Since the vision-lora and speech-lora co-exist with the base model,
# we have to manually specify the path of the lora weights.
vision_lora_path = os.path.join(model_path, "vision-lora")
prompts = [
f"<|user|><|image_1|>{question}<|end|><|assistant|>" for question in questions
]
engine_args = EngineArgs(
model=model_path,
trust_remote_code=True,
max_model_len=5120,
max_num_seqs=2,
max_num_batched_tokens=12800,
enable_lora=True,
max_lora_rank=320,
# Note - mm_processor_kwargs can also be passed to generate/chat calls
mm_processor_kwargs={"dynamic_hd": 16},
limit_mm_per_prompt={modality: 1},
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
lora_requests=[LoRARequest("vision", 1, vision_lora_path)],
)
# Phi-4-reasoning-vision
def run_phi4siglip(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "microsoft/Phi-4-reasoning-vision-15B"
prompts = [
f"<|user|>\n<image>\n{question}<|end|>\n<|assistant|>\n"
for question in questions
]
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=8192,
max_num_seqs=2,
limit_mm_per_prompt={modality: 1},
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Pixtral HF-format
def run_pixtral_hf(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "mistral-community/pixtral-12b"
# NOTE: Need L40 (or equivalent) to avoid OOM
engine_args = EngineArgs(
model=model_name,
max_model_len=6144,
max_num_seqs=2,
limit_mm_per_prompt={modality: 1},
)
prompts = [f"<s>[INST]{question}\n[IMG][/INST]" for question in questions]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Qwen2-VL
def run_qwen2_vl(questions: list[str], modality: str) -> ModelRequestData:
model_name = "Qwen/Qwen2-VL-7B-Instruct"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=5,
# Note - mm_processor_kwargs can also be passed to generate/chat calls
mm_processor_kwargs={
"min_pixels": 28 * 28,
"max_pixels": 1280 * 28 * 28,
},
limit_mm_per_prompt=mm_limit,
)
image_placeholder = "<|vision_start|><|image_pad|><|vision_end|>"
video_placeholder = "<|vision_start|><|video_pad|><|vision_end|>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + video_placeholder
prompts = [
(
"<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n"
f"<|im_start|>user\n{placeholder}"
f"{question}<|im_end|>\n"
"<|im_start|>assistant\n"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Qwen2.5-VL
def run_qwen2_5_vl(questions: list[str], modality: str) -> ModelRequestData:
model_name = "Qwen/Qwen2.5-VL-3B-Instruct"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=5,
mm_processor_kwargs={
"min_pixels": 28 * 28,
"max_pixels": 1280 * 28 * 28,
"fps": 1,
},
limit_mm_per_prompt=mm_limit,
)
image_placeholder = "<|vision_start|><|image_pad|><|vision_end|>"
video_placeholder = "<|vision_start|><|video_pad|><|vision_end|>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + video_placeholder
prompts = [
(
"<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n"
f"<|im_start|>user\n{placeholder}"
f"{question}<|im_end|>\n"
"<|im_start|>assistant\n"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Qwen2.5-Omni
def run_qwen2_5_omni(questions: list[str], modality: str):
model_name = "Qwen/Qwen2.5-Omni-7B"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=5,
mm_processor_kwargs={
"min_pixels": 28 * 28,
"max_pixels": 1280 * 28 * 28,
"fps": 1,
},
limit_mm_per_prompt=mm_limit,
)
image_placeholder = "<|vision_bos|><|IMAGE|><|vision_eos|>"
video_placeholder = "<|vision_bos|><|VIDEO|><|vision_eos|>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + video_placeholder
default_system = (
"You are Qwen, a virtual human developed by the Qwen Team, Alibaba "
"Group, capable of perceiving auditory and visual inputs, as well as "
"generating text and speech."
)
prompts = [
(
f"<|im_start|>system\n{default_system}<|im_end|>\n"
f"<|im_start|>user\n{placeholder}"
f"{question}<|im_end|>\n"
"<|im_start|>assistant\n"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Qwen3-VL-Dense
def run_qwen3_vl(questions: list[str], modality: str) -> ModelRequestData:
model_name = "Qwen/Qwen3-VL-4B-Instruct"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=5,
mm_processor_kwargs={
"min_pixels": 28 * 28,
"max_pixels": 1280 * 28 * 28,
"fps": 1,
},
limit_mm_per_prompt=mm_limit,
)
image_placeholder = "<|vision_start|><|image_pad|><|vision_end|>"
video_placeholder = "<|vision_start|><|video_pad|><|vision_end|>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + video_placeholder
prompts = [
(
"<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n"
f"<|im_start|>user\n{placeholder}"
f"{question}<|im_end|>\n"
"<|im_start|>assistant\n"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Qwen3-VL-MOE
def run_qwen3_vl_moe(questions: list[str], modality: str) -> ModelRequestData:
model_name = "Qwen/Qwen3-VL-30B-A3B-Instruct"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=5,
mm_processor_kwargs={
"min_pixels": 28 * 28,
"max_pixels": 1280 * 28 * 28,
"fps": 1,
},
limit_mm_per_prompt=mm_limit,
)
image_placeholder = "<|vision_start|><|image_pad|><|vision_end|>"
video_placeholder = "<|vision_start|><|video_pad|><|vision_end|>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + video_placeholder
prompts = [
(
"<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n"
f"<|im_start|>user\n{placeholder}"
f"{question}<|im_end|>\n"
"<|im_start|>assistant\n"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Qwen3.5-Dense
def run_qwen3_5(questions: list[str], modality: str) -> ModelRequestData:
model_name = "Qwen/Qwen3.5-4B"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=5,
mm_processor_kwargs={
"min_pixels": 28 * 28,
"max_pixels": 1280 * 28 * 28,
"fps": 1,
},
limit_mm_per_prompt=mm_limit,
)
image_placeholder = "<|vision_start|><|image_pad|><|vision_end|>"
video_placeholder = "<|vision_start|><|video_pad|><|vision_end|>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + video_placeholder
prompts = [
(
"<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n"
f"<|im_start|>user\n{placeholder}"
f"{question}<|im_end|>\n"
"<|im_start|>assistant\n"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Qwen3.5-MoE
def run_qwen3_5_moe(questions: list[str], modality: str) -> ModelRequestData:
model_name = "Qwen/Qwen3.5-35B-A3B"
mm_limit = {"image": 1, "video": 1} if modality == "image+video" else {modality: 1}
engine_args = EngineArgs(
model=model_name,
max_model_len=4096,
max_num_seqs=5,
mm_processor_kwargs={
"min_pixels": 28 * 28,
"max_pixels": 1280 * 28 * 28,
"fps": 1,
},
limit_mm_per_prompt=mm_limit,
)
image_placeholder = "<|vision_start|><|image_pad|><|vision_end|>"
video_placeholder = "<|vision_start|><|video_pad|><|vision_end|>"
if modality == "image":
placeholder = image_placeholder
elif modality == "video":
placeholder = video_placeholder
elif modality == "image+video":
placeholder = image_placeholder + video_placeholder
prompts = [
(
"<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n"
f"<|im_start|>user\n{placeholder}"
f"{question}<|im_end|>\n"
"<|im_start|>assistant\n"
)
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# R-4B
def run_r_vl(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "YannQi/R-4B"
prompts = [
f"<|im_start|>user <image>\n{question}<|im_end|><|im_start|>assistant\n"
for question in questions
]
engine_args = EngineArgs(
model=model_name,
max_model_len=16384,
limit_mm_per_prompt={modality: 1},
)
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# SkyworkR1V
def run_skyworkr1v(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "Skywork/Skywork-R1V-38B"
engine_args = EngineArgs(
model=model_name,
trust_remote_code=True,
max_model_len=4096,
limit_mm_per_prompt={modality: 1},
)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
messages = [
[{"role": "user", "content": f"<image>\n{question}"}] for question in questions
]
prompts = tokenizer.apply_chat_template(
messages, tokenize=False, add_generation_prompt=True
)
# Stop tokens for SkyworkR1V
# https://huggingface.co/Skywork/Skywork-R1V-38B/blob/main/conversation.py
stop_tokens = ["<｜end▁of▁sentence｜>", "<|endoftext|>"]
stop_token_ids = [tokenizer.convert_tokens_to_ids(i) for i in stop_tokens]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
stop_token_ids=stop_token_ids,
)
# SmolVLM2-2.2B-Instruct
def run_smolvlm(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "HuggingFaceTB/SmolVLM2-2.2B-Instruct"
engine_args = EngineArgs(
model=model_name,
max_model_len=8192,
max_num_seqs=2,
enforce_eager=True,
mm_processor_kwargs={
"max_image_size": {"longest_edge": 384},
},
limit_mm_per_prompt={modality: 1},
)
prompts = [
(f"<|im_start|>User:<image>{question}<end_of_utterance>\nAssistant:")
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# Step3
def run_step3(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "stepfun-ai/step3-fp8"
# NOTE: Below are verified configurations for step3-fp8
# on 8xH100 GPUs.
engine_args = EngineArgs(
model=model_name,
max_num_batched_tokens=4096,
gpu_memory_utilization=0.85,
tensor_parallel_size=8,
limit_mm_per_prompt={modality: 1},
reasoning_parser="step3",
)
prompts = [
"<｜begin▁of▁sentence｜> You are a helpful assistant. <|BOT|>user\n "
f"<im_patch>{question} <|EOT|><|BOT|>assistant\n<think>\n"
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
# StepVL10B
def run_step_vl(questions: list[str], modality: str) -> ModelRequestData:
assert modality == "image"
model_name = "stepfun-ai/Step3-VL-10B"
engine_args = EngineArgs(
model=model_name,
max_num_batched_tokens=4096,
tensor_parallel_size=1,
trust_remote_code=True,
limit_mm_per_prompt={modality: 1},
reasoning_parser="deepseek_r1",
)
prompts = [
"<｜begin▁of▁sentence｜> You are a helpful assistant.<|BOT|>user\n "
f"<im_patch>{question} <|EOT|><|BOT|>assistant\n<think>\n"
for question in questions
]
return ModelRequestData(
engine_args=engine_args,
prompts=prompts,
)
model_example_map = {
"aria": run_aria,
"bagel": run_bagel,
"bee": run_bee,
"blip-2": run_blip2,
"command_a_vision": run_command_a_vision,
"deepseek_vl_v2": run_deepseek_vl2,
"deepseek_ocr": run_deepseek_ocr,
"deepseek_ocr2": run_deepseek_ocr2,
"dots_ocr": run_dots_ocr,
"eagle2_5": run_eagle2_5,
"ernie45_vl": run_ernie45_vl,
"exaone4_5": run_exaone4_5,
"gemma3": run_gemma3,
"gemma3n": run_gemma3n,
"gemma4": run_gemma4,
"glm4v": run_glm4v,
"glm4_1v": run_glm4_1v,
"glm4_5v": run_glm4_5v,
"glm4_5v_fp8": run_glm4_5v_fp8,
"glm_ocr": run_glm_ocr,
"h2ovl_chat": run_h2ovl,
"hunyuan_vl": run_hunyuan_vl,
"idefics3": run_idefics3,
"interns1": run_interns1,
"interns1_pro": run_interns1_pro,
"internvl_chat": run_internvl,
"kanana_v": run_kanana_v,
"keye_vl": run_keye_vl,
"keye_vl1_5": run_keye_vl1_5,
"kimi_vl": run_kimi_vl,
"kimi_k25": run_kimi_k25,
"lightonocr": run_lightonocr,
"lfm2_vl": run_lfm2_vl,
"llama4": run_llama4,
"llava": run_llava,
"llava-next": run_llava_next,
"llava-next-video": run_llava_next_video,
"llava-onevision": run_llava_onevision,
"minicpmo": run_minicpmo,
"minicpmv": run_minicpmv,
"mistral3": run_mistral3,
"molmo": run_molmo,
"molmo2": run_molmo2,
"nemotron_vl": run_nemotron_vl,
"NVLM_D": run_nvlm_d,
"openpangu_vl": run_openpangu_vl,
"ovis": run_ovis,
"ovis2_5": run_ovis2_5,
"paddleocr_vl": run_paddleocr_vl,
"paligemma": run_paligemma,
"paligemma2": run_paligemma2,
"phi3_v": run_phi3v,
"phi4_mm": run_phi4mm,
"phi4_siglip": run_phi4siglip,
"pixtral_hf": run_pixtral_hf,
"qwen2_vl": run_qwen2_vl,
"qwen2_5_vl": run_qwen2_5_vl,
"qwen2_5_omni": run_qwen2_5_omni,
"qwen3_vl": run_qwen3_vl,
"qwen3_vl_moe": run_qwen3_vl_moe,
"qwen3_5": run_qwen3_5,
"qwen3_5_moe": run_qwen3_5_moe,
"rvl": run_r_vl,
"skywork_chat": run_skyworkr1v,
"smolvlm": run_smolvlm,
"step3": run_step3,
"stepvl": run_step_vl,
}
MODELS_NEED_VIDEO_METADATA = [
"glm4_1v",
"glm_ocr",
"glm4_5v",
"glm4_5v_fp8",
"molmo2",
"qwen2_5_vl",
"qwen3_vl",
"qwen3_vl_moe",
"qwen3_5",
"qwen3_5_moe",
]
MODELS_SUPPORT_VIT_CUDA_GRAPH = [
"llama4",
"gemma4",
"qwen2_vl",
"qwen2_5_vl",
"qwen3_vl",
"qwen3_vl_moe",
"kimi_vl",
"qwen3_5",
"qwen3_5_moe",
"internvl_chat",
"stepvl",
"glm4_1v",
"deepseek_ocr",
"ernie45_vl",
"minicpmv2_5_vl",
"minicpmv2_6_vl",
"minicpmv4_vl",
]
def get_multi_modal_input(args):
"""Return {
"data": image or video,
"question": question,
}
"""
if args.modality == "image":
# Input image and question
image = convert_image_mode(ImageAsset("cherry_blossom").pil_image, "RGB")
img_questions = [
"What is the content of this image?",
"Describe the content of this image in detail.",
"What's in the image?",
"Where is this image taken?",
]
return {
"data": image,
"questions": img_questions,
}
if args.modality == "video":
# Input video and question
needs_metadata = args.model_type in MODELS_NEED_VIDEO_METADATA
video = VideoAsset(name="baby_reading", num_frames=args.num_frames).np_ndarrays
metadata = VideoAsset(name="baby_reading", num_frames=args.num_frames).metadata
vid_questions = ["Why is this video funny?"]
return {
"data": ([(video, metadata)] if needs_metadata else video),
"questions": vid_questions,
}
if args.modality == "vision_chunk":
# Input vision chunks and question
image = convert_image_mode(ImageAsset("cherry_blossom").pil_image, "RGB")
vision_chunk_questions = [
"What is the content of this image chunk?",
"Describe the content of this image chunk in detail.",
]
return {
"data": {"type": "image", "image": image},
"questions": vision_chunk_questions,
}
if args.modality == "image+video":
image = convert_image_mode(ImageAsset("cherry_blossom").pil_image, "RGB")
needs_metadata = args.model_type in MODELS_NEED_VIDEO_METADATA
video = VideoAsset(name="baby_reading", num_frames=args.num_frames).np_ndarrays
metadata = VideoAsset(name="baby_reading", num_frames=args.num_frames).metadata
img_video_questions = [
"What is shown in the image? What happens in the video?",
"Describe both the image and the video content.",
]
return {
"data": {
"image": image,
"video": ([(video, metadata)] if needs_metadata else video),
},
"questions": img_video_questions,
}
msg = f"Modality {args.modality} is not supported."
raise ValueError(msg)
def apply_image_repeat(
image_repeat_prob, num_prompts, data, prompts: list[str], modality
):
"""Repeats images with provided probability of "image_repeat_prob".
Used to simulate hit/miss for the MM preprocessor cache.
"""
assert image_repeat_prob <= 1.0 and image_repeat_prob >= 0
no_yes = [0, 1]
probs = [1.0 - image_repeat_prob, image_repeat_prob]
inputs = []
inputs_with_empty_media = []
cur_image = data
for i in range(num_prompts):
if image_repeat_prob is not None:
res = random.choices(no_yes, probs)[0]
if res == 0:
# No repeat => Modify one pixel
cur_image = cur_image.copy()
new_val = (i // 256 // 256, i // 256, i % 256)
cur_image.putpixel((0, 0), new_val)
uuid = "uuid_{}".format(i)
inputs.append(
{
"prompt": prompts[i % len(prompts)],
"multi_modal_data": {modality: cur_image},
"multi_modal_uuids": {modality: uuid},
}
)
inputs_with_empty_media.append(
{
"prompt": prompts[i % len(prompts)],
"multi_modal_data": {modality: None},
"multi_modal_uuids": {modality: uuid},
}
)
return inputs, inputs_with_empty_media
def maybe_add_vit_cuda_graph_compilation_config(args, engine_args):
model = args.model_type
modality = args.modality
enable_vit_cuda_graph = args.enable_vit_cuda_graph
if enable_vit_cuda_graph and model in MODELS_SUPPORT_VIT_CUDA_GRAPH:
if modality == "image" or modality == "video":
vision_items_per_batch = 1
elif modality == "image+video":
vision_items_per_batch = 2
else:
raise ValueError(
f"modality={modality} is not supported for vit cuda graph."
)
engine_args.compilation_config = {
"cudagraph_mm_encoder": True,
"encoder_cudagraph_max_vision_items_per_batch": vision_items_per_batch,
}
return engine_args
@contextmanager
def time_counter(enable: bool):
if enable:
import time
start_time = time.time()
yield
elapsed_time = time.time() - start_time
print("-" * 50)
print("-- generate time = {}".format(elapsed_time))
print("-" * 50)
else:
yield
def parse_args():
parser = FlexibleArgumentParser(
description="Demo on using vLLM for offline inference with "
"vision language models for text generation"
)
parser.add_argument(
"--model-type",
"-m",
type=str,
default="llava",
choices=model_example_map.keys(),
help='Huggingface "model_type".',
)
parser.add_argument(
"--num-prompts", type=int, default=4, help="Number of prompts to run."
)
parser.add_argument(
"--modality",
type=str,
default="image",
choices=["image", "video", "image+video", "vision_chunk"],
help="Modality of the input.",
)
parser.add_argument(
"--num-frames",
type=int,
default=16,
help="Number of frames to extract from the video.",
)
parser.add_argument(
"--seed",
type=int,
default=0,
help="Set the seed when initializing `vllm.LLM`.",
)
parser.add_argument(
"--image-repeat-prob",
type=float,
default=None,
help="Simulates the hit-ratio for multi-modal preprocessor cache (if enabled)",
)
parser.add_argument(
"--disable-mm-processor-cache",
action="store_true",
help="If True, disables caching of multi-modal processor.",
)
parser.add_argument(
"--time-generate",
action="store_true",
help="If True, then print the total generate() call time",
)
parser.add_argument(
"--use-different-prompt-per-request",
action="store_true",
help="If True, then use different prompt (with the same multi-modal "
"data) for each request.",
)
parser.add_argument(
"--verify-mm-cache-hit-with-uuids",
action="store_true",
help="If True, will send all requests in a second batch with empty mm "
"data to verify cache hits with UUIDs.",
)
parser.add_argument(
"--tensor-parallel-size",
"-tp",
type=int,
default=None,
help="Tensor parallel size to override the model's default setting. ",
)
parser.add_argument(
"--enable-vit-cuda-graph",
action="store_true",
help="If True, will enable vit cuda graph capture and replay for the model.",
)
return parser.parse_args()
def main(args):
model = args.model_type
if model not in model_example_map:
raise ValueError(f"Model type {model} is not supported.")
if args.tensor_parallel_size is not None and args.tensor_parallel_size < 1:
raise ValueError(
f"tensor_parallel_size must be a positive integer, "
f"got {args.tensor_parallel_size}"
)
modality = args.modality
mm_input = get_multi_modal_input(args)
data = mm_input["data"]
questions = mm_input["questions"]
req_data = model_example_map[model](questions, modality)
# Disable other modalities to save memory
default_limits = {"image": 0, "video": 0, "audio": 0, "vision_chunk": 0}
req_data.engine_args.limit_mm_per_prompt = default_limits | dict(
req_data.engine_args.limit_mm_per_prompt or {}
)
engine_args = req_data.engine_args
engine_args.seed = args.seed
mm_processor_cache_gb = 0 if args.disable_mm_processor_cache else 4
engine_args.mm_processor_cache_gb = mm_processor_cache_gb
if args.tensor_parallel_size is not None:
engine_args.tensor_parallel_size = args.tensor_parallel_size
engine_args = maybe_add_vit_cuda_graph_compilation_config(args, engine_args)
if current_platform.is_rocm():
os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"
llm = LLM.from_engine_args(engine_args)
# Don't want to check the flag multiple times, so just hijack `prompts`.
prompts = (
req_data.prompts
if args.use_different_prompt_per_request
else [req_data.prompts[0]]
)
# We set temperature to 0.2 so that outputs can be different
# even when all prompts are identical when running batch inference.
sampling_params = (
SamplingParams(
temperature=0.2, max_tokens=64, stop_token_ids=req_data.stop_token_ids
)
if req_data.sampling_params is None
else req_data.sampling_params
)
def _mm_data(data, modality):
if modality == "image+video":
return {"image": data["image"], "video": data["video"]}
return {modality: data}
def _mm_uuid(uuid, modality):
if modality == "image+video":
return {"image": uuid, "video": uuid + "v"}
return {modality: uuid}
def _mm_empty(modality):
if modality == "image+video":
return {"image": None, "video": None}
return {modality: None}
assert args.num_prompts > 0
if args.num_prompts == 1:
# Single inference
uuid = "uuid_0"
inputs = {
"prompt": prompts[0],
"multi_modal_data": _mm_data(data, modality),
"multi_modal_uuids": _mm_uuid(uuid, modality),
}
inputs_with_empty_media = {
"prompt": prompts[0],
"multi_modal_data": _mm_empty(modality),
"multi_modal_uuids": _mm_uuid(uuid, modality),
}
else:
# Batch inference
if args.image_repeat_prob is not None:
if modality == "image+video":
raise ValueError(
"--image-repeat-prob is not supported for 'image+video' modality"
)
# Repeat images with specified probability of "image_repeat_prob"
inputs, inputs_with_empty_media = apply_image_repeat(
args.image_repeat_prob,
args.num_prompts,
data,
prompts,
modality,
)
else:
# Use the same image/video for all prompts
inputs = []
inputs_with_empty_media = []
for i in range(args.num_prompts):
uuid = "uuid_{}".format(i)
inputs.append(
{
"prompt": prompts[i % len(prompts)],
"multi_modal_data": _mm_data(data, modality),
"multi_modal_uuids": _mm_uuid(uuid, modality),
}
)
inputs_with_empty_media.append(
{
"prompt": prompts[i % len(prompts)],
"multi_modal_data": _mm_empty(modality),
"multi_modal_uuids": _mm_uuid(uuid, modality),
}
)
# Add LoRA request if applicable
lora_request = (
req_data.lora_requests * args.num_prompts if req_data.lora_requests else None
)
with time_counter(args.time_generate):
outputs = llm.generate(
inputs,
sampling_params=sampling_params,
lora_request=lora_request,
)
print("-" * 50)
for o in outputs:
generated_text = o.outputs[0].text
print(generated_text)
print("-" * 50)
if args.verify_mm_cache_hit_with_uuids:
try:
# Verify cache hits with UUIDs
print(
"Sending a second batch of requests with empty media"
" and matching UUIDs."
)
outputs = llm.generate(
inputs_with_empty_media,
sampling_params=sampling_params,
lora_request=lora_request,
)
print("-" * 50)
for o in outputs:
generated_text = o.outputs[0].text
print(generated_text)
print("-" * 50)
except Exception as e:
print(f"Failed to verify cache hits with UUIDs. Error: {e}")
if __name__ == "__main__":
args = parse_args()
main(args)
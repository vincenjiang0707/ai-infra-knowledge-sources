source: https://docs.nvidia.com/dynamo/zh-CN/diffusion/text-to-audio
lastmod: 2026-09-24T19:58:16.636Z

Text-to-Audio


Text-to-Audio

Synthesize speech with vLLM-Omni through the /v1/audio/speech endpoint

Text-to-audio (TTS) generation runs a vLLM-Omni worker with `--output-modalities audio`

. See the [Diffusion Overview](https://docs.nvidia.com/dynamo/diffusion/overview) for installation and shared configuration.

## Tested Models

## Launch

Launch using the provided script with `Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice`

:

## Generate Speech

###### CustomVoice (predefined speaker)

###### CustomVoice + style

###### VoiceDesign (describe a voice)

## Parameters

The `/v1/audio/speech`

endpoint follows the [vLLM-Omni](https://docs.vllm.ai/projects/vllm-omni/en/latest/) API format. All TTS-specific parameters are top-level fields:

Text to synthesize.

TTS model name.

Speaker name (e.g., vivian, ryan). Validated against model config.

Audio output format.

Speed factor (0.25–4.0).

Synthesis task type (Qwen3-TTS).

Language code. Validated against model config.

Voice style/emotion description. Required for VoiceDesign.

Reference audio URL or base64 data URI. Required for Base.

Transcript of reference audio (Base task).

Maximum tokens to generate (1–4096).

Available voices and languages are loaded dynamically from the model’s `config.json`

at startup. Non-Qwen3-TTS audio models (e.g., MiMo-Audio) use a generic text prompt and ignore TTS-specific parameters.

`stream: true`

) and the Base task (voice cloning) are not yet supported.
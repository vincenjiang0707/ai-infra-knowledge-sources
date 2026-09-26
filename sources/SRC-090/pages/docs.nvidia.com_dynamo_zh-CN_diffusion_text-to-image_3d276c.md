source: https://docs.nvidia.com/dynamo/zh-CN/diffusion/text-to-image
lastmod: 2026-09-24T19:58:16.636Z

Text-to-Image


Text-to-Image

Generate images from text prompts with vLLM-Omni, SGLang, or TensorRT-LLM

Choose a backend for text-to-image generation. See the [Diffusion Overview](https://docs.nvidia.com/dynamo/diffusion/overview) for installation and shared configuration.

###### vLLM-Omni

###### SGLang

###### TensorRT-LLM

Text-to-image generation runs a vLLM-Omni worker with `--output-modalities image`

.

## Tested Models

To run a non-default model, pass `--model`

to the launch script:

## Launch

Launch using the provided script with `Qwen/Qwen-Image`

:

## Generate an Image

Image generation is available on two endpoints: `/v1/chat/completions`

returns base64-encoded images inline in `choices[].delta.content[].image_url`

, while `/v1/images/generations`

returns a URL or base64 depending on `response_format`

.

###### /v1/images/generations

###### /v1/chat/completions

## See Also

[Text-to-Image with SGLang](https://docs.nvidia.com/dynamo/diffusion/text-to-image#sglang)[Text-to-Image with TensorRT-LLM](https://docs.nvidia.com/dynamo/diffusion/text-to-image#tensorrt-llm)[Disaggregated Serving](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/v-llm-omni-disaggregated-serving)— GLM-Image (2-stage text-to-image)[vLLM-Omni Configuration reference](https://docs.nvidia.com/dynamo/reference/backends/v-llm-omni-configuration)
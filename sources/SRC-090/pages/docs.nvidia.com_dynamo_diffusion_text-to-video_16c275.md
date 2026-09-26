source: https://docs.nvidia.com/dynamo/diffusion/text-to-video
lastmod: 2026-09-24T19:58:16.636Z

Text-to-Video


Text-to-Video

Generate videos from text prompts with vLLM-Omni, SGLang, TensorRT-LLM, or FastVideo

Choose a backend for text-to-video generation. See the [Diffusion Overview](https://docs.nvidia.com/dynamo/diffusion/overview) for installation and shared configuration.

###### vLLM-Omni

###### SGLang

###### TensorRT-LLM

###### FastVideo

Text-to-video generation runs a vLLM-Omni worker with `--output-modalities video`

.

## Tested Models

To run a non-default model, pass `--model`

to the launch script:

## Launch

Launch using the provided script with `Wan-AI/Wan2.1-T2V-1.3B-Diffusers`

:

## Generate a Video

Generate a video via `/v1/videos`

:

The response returns a video URL or base64 data depending on `response_format`

(e.g. `{"object": "video", "status": "completed", "data": [{"url": "file:///tmp/dynamo_media/videos/req-abc123.mp4"}]}`

).

## Request Parameters (`nvext`

)

The `/v1/videos`

endpoint also accepts NVIDIA extensions via the `nvext`

field for fine-grained control:

Frames per second.

Number of frames (overrides `fps * seconds`

).

Negative prompt for guidance.

Number of denoising steps.

CFG guidance scale.

Random seed for reproducibility.

The `nvext.boundary_ratio`

and `nvext.guidance_scale_2`

fields apply to the dual-expert MoE schedule used in image-to-video. See [Image-to-Video with vLLM-Omni](https://docs.nvidia.com/dynamo/diffusion/image-to-video#vllm-omni).

## See Also

[Image-to-Video with vLLM-Omni](https://docs.nvidia.com/dynamo/diffusion/image-to-video#vllm-omni)— animate a source image with the same`/v1/videos`

endpoint[Text-to-Video with SGLang](https://docs.nvidia.com/dynamo/diffusion/text-to-video#sglang)[Text-to-Video with TensorRT-LLM](https://docs.nvidia.com/dynamo/diffusion/text-to-video#tensorrt-llm)[Text-to-Video with FastVideo](https://docs.nvidia.com/dynamo/diffusion/text-to-video#fastvideo)[vLLM-Omni Configuration reference](https://docs.nvidia.com/dynamo/reference/backends/v-llm-omni-configuration)
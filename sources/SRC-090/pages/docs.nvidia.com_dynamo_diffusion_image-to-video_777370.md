source: https://docs.nvidia.com/dynamo/diffusion/image-to-video
lastmod: 2026-09-24T19:58:16.636Z

Image-to-Video


Image-to-Video

Animate source images with vLLM-Omni or SGLang

Choose a backend for image-to-video generation. See the [Diffusion Overview](https://docs.nvidia.com/dynamo/diffusion/overview) for installation and shared configuration.

###### vLLM-Omni

###### SGLang

Image-to-video (I2V) uses the same `/v1/videos`

endpoint as [text-to-video](https://docs.nvidia.com/dynamo/diffusion/text-to-video#vllm-omni), with an additional `input_reference`

field that provides the source image. Run a vLLM-Omni worker with `--output-modalities video`

.

## Tested Models

To run a non-default model, pass `--model`

to the launch script:

## Launch

Launch with the provided script using `Wan-AI/Wan2.2-TI2V-5B-Diffusers`

:

## Generate a Video from an Image

The `input_reference`

field accepts:

**HTTP/HTTPS URL**:`"https://example.com/image.png"`

**Base64 data URI**:`"data:image/png;base64,iVBORw0KGgo..."`

**Local file path**:`"/path/to/image.png"`

or`"file:///path/to/image.png"`


## Request Parameters (`nvext`

)

I2V accepts all [text-to-video nvext fields](https://docs.nvidia.com/dynamo/diffusion/text-to-video#request-parameters-nvext), plus two fields that control the dual-expert MoE denoising schedule in Wan2.x models:

nvext.boundary_ratio

MoE expert switching boundary (I2V).

nvext.guidance_scale_2

CFG scale for the low-noise expert (I2V).
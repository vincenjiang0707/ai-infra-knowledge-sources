source: https://docs.nvidia.com/dynamo/diffusion/overview
lastmod: 2026-09-24T19:58:16.636Z

# Diffusion

## Overview

Dynamo serves diffusion models for text-to-image, text-to-video, image-to-video, text-to-audio, and text-to-text generation. These workloads use the same frontend, routing, scaling, and observability infrastructure as LLM inference.

The built-in backends expose OpenAI-compatible endpoints for images (`/v1/images/generations`

), videos (`/v1/videos`

), audio (`/v1/audio/speech`

), and text generation.

Built-in diffusion backends currently use Dynamo CLI launch scripts and `python -m dynamo.*`

entrypoints. Dynamo does not yet ship prebuilt Kubernetes recipes for these backends. FastVideo is the exception and includes a Kubernetes deployment path.

### Install the Backend

Choose the tab for the backend you plan to use.

###### vLLM-Omni

###### SGLang

###### TensorRT-LLM

###### FastVideo

[vLLM-Omni](https://github.com/vllm-project/vllm-omni) provides image, video, and audio generation through `python -m dynamo.vllm.omni`

.

**Prerequisites**

- A working
[vLLM backend setup](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/overview). - An
`amd64`

host. Dynamo container builds do not install vLLM-Omni on`arm64`

.

Dynamo container images include vLLM-Omni. A PyPI installation of `ai-dynamo[vllm]`

does not include it automatically. For a source installation, pin the vLLM-Omni release that matches your vLLM version:

###### Local launchers, media storage, and stage configuration


The `agg_omni_*.sh`

and `disagg_omni_glm_image.sh`

scripts launch the frontend and workers directly on one host. They are intended for local development and testing and do not create a `DynamoGraphDeployment`

.

Generated media uses [fsspec](https://filesystem-spec.readthedocs.io/) storage. The default is `file:///tmp/dynamo_media`

. Set `--media-output-fs-url`

for S3, GCS, or Azure Blob storage, and optionally set `--media-output-http-url`

to rewrite response URLs.

vLLM-Omni includes built-in YAML stage configurations for supported models. Set `--stage-configs-path`

only to override them.

See the [vLLM-Omni Configuration reference](https://docs.nvidia.com/dynamo/reference/backends/v-llm-omni-configuration) for the complete flag surface.
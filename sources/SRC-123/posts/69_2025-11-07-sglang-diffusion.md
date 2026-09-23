# 2025-11-07-sglang-diffusion

source: https://lmsys.org/blog/2025-11-07-sglang-diffusion

# SGLang Diffusion: Accelerating Video and Image Generation

We are excited to introduce SGLang Diffusion, which brings SGLang's state-of-the-art performance to accelerate image and video generation for diffusion models.
SGLang Diffusion supports major open-source video and image generation models (Wan, Hunyuan, Qwen-Image, Qwen-Image-Edit, Flux) while providing fast inference speeds and ease of use via multiple API entry points (OpenAI-compatible API, CLI, Python interface). SGLang Diffusion delivers 1.2x - 5.9x speedup across diverse workloads.
In collaboration with the FastVideo team, we provide a complete ecosystem for diffusion models, from post-training to production serving. The code is available [here](https://github.com/sgl-project/sglang/tree/main/python/sglang/multimodal_gen). Documentation is available [here](https://docs.sglang.io/diffusion/index.html).

SGL Diffusion Performance Benchmark on an H100 GPU

SGLang Diffusion Performance Benchmark on an H200 GPU

## Why Diffusion in SGLang?

With diffusion models becoming the backbone for state-of-the-art image and video generation, we have heard strong community demand for bringing SGLang's signature performance and seamless user experience to these new modalities. We built SGLang Diffusion to answer this call, providing a unified, high-performance engine for both language and diffusion tasks.

This unified approach is crucial, as the future of generation lies in combining architectures.
Pioneering models are already fusing the strengths of autoregressive (AR) and diffusion-based approaches—from models like ByteDance's [Bagel](https://github.com/ByteDance-Seed/Bagel) and Meta's [Transfusion](https://arxiv.org/abs/2408.11039) that use a single transformer for both tasks, to NVIDIA's [Fast-dLLM v2](https://nvlabs.github.io/Fast-dLLM/v2/) which adapts AR models for parallel generation.

SGLang Diffusion is designed to be a future-proof, high-performance solution ready to power these innovative systems.

## Architecture

SGLang Diffusion is engineered for both performance and flexibility, built upon SGLang's battle-tested serving architecture. It inherits the powerful SGLang scheduler and reuses highly-optimized sgl-kernel for maximum efficiency.

At its core, our architecture is designed to accommodate the diverse structures of modern diffusion models. We introduce `ComposedPipelineBase`

, a flexible abstraction that orchestrates a series of modular `PipelineStage`

s. Each stage encapsulates a common diffusion function—such as the denoising loop in `DenoisingStage`

or VAE decoding in `DecodingStage`

—allowing developers to easily combine and reuse these components to construct complex, customized pipelines.

To achieve state-of-the-art speed, we integrate advanced parallelism techniques. It supports Unified Sequence Parallelism (USP)—a combination of Ulysses-SP and Ring-Attention—for the core transformer blocks, alongside CFG-parallelism and tensor parallelism (TP) for other model components.

To accelerate development and foster a powerful ecosystem, our system is built on an enhanced fork of **FastVideo**, and we are collaborating closely with their team. This partnership allows SGLang Diffusion to focus on delivering cutting-edge inference speed, while **FastVideo** provides comprehensive support for training-related tasks like model distillation.

## Model Support

We support various popular open-source video & image generation models, including:

- Video models: Wan-series, FastWan, Hunyuan
- Image models: Qwen-Image, Qwen-Image-Edit, Flux

For full list of supported models, reference [here](https://docs.sglang.io/diffusion/compatibility_matrix.html).

## Usage

For a seamless user experience, we provide a suite of familiar interfaces, including a CLI, a Python engine API, and an OpenAI-compatible API, allowing users to integrate diffusion generation into their workflows with minimal effort.

### Install

SGLang Diffusion can be installed via multiple ways:

```
# with pip or uv
uv pip install 'sglang[diffusion]' --prerelease=allow
# from source
git clone https://github.com/sgl-project/sglang.git
cd sglang
uv pip install -e "python[diffusion]" --prerelease=allow
```


### CLI

Launch a server and then send requests:

```
sglang serve --model-path black-forest-labs/FLUX.1-dev --port 3000
curl http://127.0.0.1:3000/v1/images/generations \
-o >(jq -r '.data[0].b64_json' | base64 --decode > example.png) \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
"model": "black-forest-labs/FLUX.1-dev",
"prompt": "A cute baby sea otter",
"n": 1,
"size": "1024x1024",
"response_format": "b64_json"
}'
```


Or, generate an image without launching a server:

```
sglang generate --model-path black-forest-labs/FLUX.1-dev \
--prompt "A Logo With Bold Large Text: SGL Diffusion" \
--save-output
```


Reference [install guide](https://docs.sglang.io/diffusion/installation.html) and [cli guide](https://docs.sglang.io/diffusion/api/cli.html) for more installation methods.

### Demo

#### Text to Video: Wan-AI/Wan2.1

```
sglang generate --model-path Wan-AI/Wan2.1-T2V-1.3B-Diffusers \
--prompt "A curious raccoon" \
--save-output
```


Fallback link: [Download the video](https://github.com/lm-sys/lm-sys.github.io/releases/download/test/T2V.mp4)

#### Image to Video: Wan-AI/Wan2.1-I2V

```
sglang generate --model-path=Wan-AI/Wan2.1-I2V-14B-480P-Diffusers \
--prompt="Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard. The fluffy-furred feline gazes directly at the camera with a relaxed expression. Blurred beach scenery forms the background featuring crystal-clear waters, distant green hills, and a blue sky dotted with white clouds. The cat assumes a naturally relaxed posture, as if savoring the sea breeze and warm sunlight. A close-up shot highlights the feline's intricate details and the refreshing atmosphere of the seaside." \
--image-path="https://github.com/Wan-Video/Wan2.2/blob/990af50de458c19590c245151197326e208d7191/examples/i2v_input.JPG?raw=true" \
--num-gpus 2 --enable-cfg-parallel --save-output
```


Fallback link: [Download the video](https://github.com/lm-sys/lm-sys.github.io/releases/download/test/TI2V.mp4)

#### Text to Image: FLUX

```
sglang generate --model-path black-forest-labs/FLUX.1-dev \
--prompt "A Logo With Bold Large Text: SGL Diffusion" \
--save-output
```


#### Text to Image: Qwen-Image

```
sglang generate --model-path=Qwen/Qwen-Image \
--prompt='A curious raccoon' \
--width=720 --height=720 --save-output
```


#### Image to Image: Qwen-Image-Edit

```
sglang generate --model-path=Qwen/Qwen-Image-Edit \
--prompt="Convert 2D style to 3D style" --image-path="https://github.com/lm-sys/lm-sys.github.io/releases/download/test/TI2I_Qwen_Image_Edit_Input.jpg" \
--width=1536 --height=1024 --save-output
```


## Performance Benchmark

As shown in the chart at the top of this post, we compared the performance of SGLang Diffusion:

- Against a popular open-source baseline, Hugging Face Diffusers. SGLang Diffusion delivers state-of-the-art performance, significantly accelerating both image and video generation.
- Under different parallelism setups. Both CFG-Parallel and USP deliver significant speedups compared to the single-GPU setup.

## Roadmap and Diffusion Ecosystem

Our vision is to build a comprehensive diffusion ecosystem in collaboration with the **FastVideo** team, providing an end-to-end solution from model training to high-performance inference.

The SGLang Diffusion team is centered on continuous innovation in performance and model support:

- Model support and optimizations
- Optimize Wan, FastWan, Hunyuan, Qwen-Image series, FLUX
- Support LongCat-Video

- Kernel support and fusions
- Quantization kernels
- Rotary embedding kernels
- Flash Attention 4 integration in sgl-kernel for blackwell

- More server features
- Configurable cloud storage upload of generated files
- Batching support
- More parallelism methods
- Quantization

- General architecture:
- Simplify the effort of supporting new models
- Enhance cache and attention backend supports


Building this ecosystem is a community effort, and we welcome and encourage all forms of contribution. Join us in shaping the future of open-source diffusion generation.

## Acknowledgment

SGLang Diffusion Team: [Yuhao Yang](https://github.com/yhyang201), [Xinyuan Tong](https://github.com/JustinTong0323), [Yi Zhang](https://github.com/yizhang2077), [Ke Bao](https://github.com/ispobock), [Ji Li](https://github.com/GeLee-Q/GeLee-Q), [Xi Chen](https://github.com/RubiaCx), [Laixin Xie](https://github.com/laixinn), [Yikai Zhu](https://github.com/zyksir), [Mick](https://mickqian.github.io)

FastVideo Team: [Peiyuan Zhang](https://github.com/jzhang38), [William Lin](https://github.com/SolitaryThinker), [Yongqi Chen](https://github.com/BrianChen1129), [Kevin Lin](https://github.com/kevin314), [Wenxuan Tan](https://github.com/Edenzzzz), [Wei Zhou](https://github.com/JerryZhou54), [Runlong Su](https://github.com/rlsu9), [Jinzhe Pan](https://github.com/Eigensystem), [Hangliang Ding](https://github.com/foreverpiano), [Matthew Noto](https://github.com/RandNMR73), [You Zhou](https://github.com/PorridgeSwim), [Jiali Chen](https://github.com/Gary-ChenJL), [Hao Zhang](https://haozhang.ai/)

Special thanks to NVIDIA and Voltage Park for their compute support.

## Learn more

- Roadmap:
[Diffusion (2025 Q4)](https://github.com/sgl-project/sglang/issues/12799) - Slack channel:
[#diffusion](https://sgl-fru7574.slack.com/archives/C09P0HTKE6A)(join via slack.sglang.io)

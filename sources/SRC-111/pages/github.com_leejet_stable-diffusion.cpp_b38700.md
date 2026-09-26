source: https://github.com/leejet/stable-diffusion.cpp

Diffusion model(SD,Flux,Wan,...) inference in pure C/C++

**Note that this project is under active development.
API and command-line option may change frequently.**

**2026/09/20**🚀 stable-diffusion.cpp adds**Day-0 support for Qwen-Image-2.1****2026/08/20**🚀 stable-diffusion.cpp now supports**LTX-2.5****2026/08/04**🚀 stable-diffusion.cpp adds**Day-1 support for MiniMax-H3****2026/06/25**🚀 stable-diffusion.cpp now supports**Krea2****2026/06/04**🚀 stable-diffusion.cpp now supports**Ideogram4****2026/05/31**🚀 stable-diffusion.cpp now supports**PiD****2026/05/27**🚀 stable-diffusion.cpp now supports**Lens****2026/05/17**🚀 stable-diffusion.cpp now supports**LTX-2.3****2026/04/11**🚀 stable-diffusion.cpp now uses a brand-new embedded web UI.**2026/01/18**🚀 stable-diffusion.cpp now supports**FLUX.2-klein****2025/12/01**🚀 stable-diffusion.cpp now supports**Z-Image****2025/11/30**🚀 stable-diffusion.cpp now supports**FLUX.2-dev****2025/10/13**🚀 stable-diffusion.cpp now supports**Qwen-Image-Edit / Qwen-Image-Edit 2509****2025/10/12**🚀 stable-diffusion.cpp now supports**Qwen-Image****2025/09/14**🚀 stable-diffusion.cpp now supports**Wan2.1 Vace****2025/09/06**🚀 stable-diffusion.cpp now supports**Wan2.1 / Wan2.2**

- Plain C/C++ implementation based on
[ggml](https://github.com/ggml-org/ggml), working in the same way as[llama.cpp](https://github.com/ggml-org/llama.cpp) - Super lightweight and without external dependencies
- Supported models
- Image Models
[SD1.x, SD2.x, SD-Turbo](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/sd.md)[SDXL, SDXL-Turbo](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/sd.md)[Some SD1.x and SDXL distilled models](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/distilled_sd.md)[SD3/SD3.5](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/sd3.md)[FLUX.1-dev/FLUX.1-schnell](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/flux.md)[FLUX.2-dev/FLUX.2-klein](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/flux2.md)[Lens](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/lens.md)[Chroma](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/chroma.md)[Chroma1-Radiance](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/chroma_radiance.md)[Qwen Image](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/qwen_image.md)[Qwen Image 2.1](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/qwen_image_2.1.md)[PiD](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/pid.md)[LongCat Image](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/longcat_image.md)[Z-Image](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/z_image.md)[MiniT2I](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/minit2i.md)[SenseNova U1.5](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/sensenova_u1.md)[Ovis-Image](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/ovis_image.md)[Anima](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/anima.md)[ERNIE-Image](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/ernie_image.md)[Boogu Image](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/boogu_image.md)[Krea2](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/krea2.md)[Mage-Flow](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/mage_flow.md)[SeFi-Image](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/sefi_image.md)[HiDream-O1-Image](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/hidream_o1_image.md)[Ideogram4](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/ideogram4.md)[LLaDA-Image](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/llada_image.md)

[Image Edit Models](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/edit.md)- Video Models
[PhotoMaker](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/photo_maker.md)support.[IP-Adapter](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/ip_adapter.md)support (SD 1.5 and SDXL, including Plus)- Control Net support with SD 1.5
[ADetailer](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/adetailer.md)- LoRA support, same as
[stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features#lora) - Latent Consistency Models support (LCM/LCM-LoRA)
- Faster and memory efficient latent decoding with
[TAESD](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/taesd.md) - Upscale images generated with
[ESRGAN](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/esrgan.md)

- Image Models
- Supported backends
- CPU (AVX, AVX2 and AVX512 support for x86 architectures)
- CUDA
- Vulkan
- Metal
- OpenCL
- SYCL

- Supported weight formats
- Pytorch checkpoint (
`.ckpt`

or`.pth`

or`.pt`

) - Safetensors (
`.safetensors`

) - GGUF (
`.gguf`

)

- Pytorch checkpoint (
- Convert mode supports converting model weights to
`.gguf`

or`.safetensors`

- Supported platforms
- Linux
- Mac OS
- Windows
- Android (via Termux,
[Local Diffusion](https://github.com/rmatif/Local-Diffusion))

- Flash Attention for memory usage optimization
- Negative prompt
[stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)style tokenizer (not all the features, only token weighting for now)- VAE tiling processing for reduce memory usage
- Sampling method
`Euler A`

`Euler`

`Heun`

`DPM2`

`DPM++ 2M`

`DPM++ 2M v2`

`DPM++ 2S a`

`ER-SDE`

`LCM`


- Cross-platform reproducibility
`--rng cuda`

, default, consistent with the`stable-diffusion-webui GPU RNG`

`--rng cpu`

, consistent with the`comfyui RNG`


- Embedds generation parameters into png output as webui-compatible text string

- Download pre-built binaries from the
[releases page](https://github.com/leejet/stable-diffusion.cpp/releases) - Or build from source by following the
[build guide](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/build.md)

-
download weights(.ckpt or .safetensors or .gguf). For example

- Stable Diffusion v1.5 from
[https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5](https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5)

curl -L -O https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors

- Stable Diffusion v1.5 from

`./bin/sd-cli -m ../models/v1-5-pruned-emaonly.safetensors -p "a lovely cat"`

**For detailed command-line arguments, check out cli doc.**

If you want to improve performance or reduce VRAM/RAM usage, please refer to [performance guide](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/performance.md).
For runtime and parameter backend placement, see the [backend selection guide](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/backend.md).

[Troubleshooting](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/troubleshooting.md)[Backend selection](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/backend.md)[RPC](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/rpc.md)[LoRA](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/lora.md)[LCM/LCM-LoRA](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/lcm.md)[Docker](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/docker.md)[Quantization and GGUF](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/quantization_and_gguf.md)[INT8 convrot safetensors](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/int8_convrot.md)[Inference acceleration via caching](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/caching.md)

These projects wrap `stable-diffusion.cpp`

for easier use in other languages/frameworks.

- Golang (non-cgo):
[seasonjs/stable-diffusion](https://github.com/seasonjs/stable-diffusion) - Golang (cgo):
[Binozo/GoStableDiffusion](https://github.com/Binozo/GoStableDiffusion) - Golang (non-cgo):
[l8bloom/gosd](https://github.com/l8bloom/gosd) - C#:
[DarthAffe/StableDiffusion.NET](https://github.com/DarthAffe/StableDiffusion.NET) - Python:
[william-murray1204/stable-diffusion-cpp-python](https://github.com/william-murray1204/stable-diffusion-cpp-python) - Rust:
[newfla/diffusion-rs](https://github.com/newfla/diffusion-rs) - Flutter/Dart:
[rmatif/Local-Diffusion](https://github.com/rmatif/Local-Diffusion)

These projects use `stable-diffusion.cpp`

as a backend for their image generation.

[GIMP Plugins](https://github.com/themanyone/gimp-plugins)[Jellybox](https://jellybox.com)[Stable Diffusion GUI](https://github.com/fszontagh/sd.cpp.gui.wx)[Stable Diffusion CLI-GUI](https://github.com/piallai/stable-diffusion.cpp)[Local Diffusion](https://github.com/rmatif/Local-Diffusion)[sd.cpp-webui](https://github.com/daniandtheweb/sd.cpp-webui)[LocalAI](https://github.com/mudler/LocalAI)[Neural-Pixel](https://github.com/Luiz-Alcantara/Neural-Pixel)[KoboldCpp](https://github.com/LostRuins/koboldcpp)

Thank you to all the people who have already contributed to stable-diffusion.cpp!
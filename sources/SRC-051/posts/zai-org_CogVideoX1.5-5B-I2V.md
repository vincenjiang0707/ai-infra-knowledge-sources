# zai-org/CogVideoX1.5-5B-I2V

source: https://huggingface.co/zai-org/CogVideoX1.5-5B-I2V

---
license: other
license_link: https://huggingface.co/THUDM/CogVideoX-5b-I2V/blob/main/LICENSE
language:
  - en
tags:
  - video-generation
  - thudm
  - image-to-video
inference: false
---

# CogVideoX1.5-5B-I2V

<p style="text-align: center;">
  <div align="center">
  <img src=https://github.com/THUDM/CogVideo/raw/main/resources/logo.svg width="50%"/>
  </div>
  <p align="center">
  <a href="https://huggingface.co/THUDM/CogVideoX1.5-5B-I2V/blob/main/README_zh.md">📄 中文阅读</a> | 
  <a href="https://huggingface.co/spaces/THUDM/CogVideoX-5B-Space">🤗 Huggingface Space</a> |
  <a href="https://github.com/THUDM/CogVideo">🌐 Github </a> | 
  <a href="https://arxiv.org/pdf/2408.06072">📜 arxiv </a>
</p>
<p align="center">
📍 Visit <a href="https://chatglm.cn/video?fr=osm_cogvideox"> Qingying </a> and the <a href="https://open.bigmodel.cn/?utm_campaign=open&_channel_track_key=OWTVNma9"> API Platform </a> to experience the commercial video generation model
</p>

## Model Introduction

CogVideoX is an open-source video generation model similar to [QingYing](https://chatglm.cn/video?fr=osm_cogvideo).
Below is a table listing information on the video generation models available in this generation:


<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Model Name</th>
    <th style="text-align: center;">CogVideoX1.5-5B</th>
    <th style="text-align: center;">CogVideoX1.5-5B-I2V (Current Repository)</th>
  </tr>
  <tr>
    <td style="text-align: center;">Video Resolution</td>
    <td colspan="1" style="text-align: center;">1360 * 768</td>
    <td colspan="1" style="text-align: center;"> Min(W, H) = 768 <br> 768 ≤ Max(W, H) ≤ 1360 <br> Max(W, H) % 16 = 0 </td>
  </tr>
  <tr>
    <td style="text-align: center;">Inference Precision</td>
    <td colspan="2" style="text-align: center;"><b>BF16 (recommended)</b>, FP16, FP32, FP8*, INT8, not supported INT4</td>
  </tr>
  <tr>
    <td style="text-align: center;">Single GPU Inference Memory Consumption</td>
    <td colspan="2"  style="text-align: center;"><b>BF16: 9GB minimum*</b></td>
  </tr>
  <tr>
    <td style="text-align: center;">Multi-GPU Inference Memory Consumption</td>
    <td colspan="2" style="text-align: center;"><b>BF16: 24GB* using diffusers</b><br></td>

  </tr>
  <tr>
    <td style="text-align: center;">Inference Speed<br>(Step = 50, FP/BF16)</td>
    <td colspan="2" style="text-align: center;">Single A100: ~1000 seconds (5-second video)<br>Single H100: ~550 seconds (5-second video)</td>
  </tr>
  <tr>
    <td style="text-align: center;">Prompt Language</td>
    <td colspan="5" style="text-align: center;">English*</td>
  </tr>
  <tr>
    <td style="text-align: center;">Max Prompt Length</td>
    <td colspan="2" style="text-align: center;">224 Tokens</td>
  </tr>
  <tr>
    <td style="text-align: center;">Video Length</td>
    <td colspan="2" style="text-align: center;">5 or 10 seconds</td>
  </tr>
  <tr>
  <td style="text-align: center;">Frame Rate</td>
  <td colspan="2" style="text-align: center;">16 frames/second</td>
  </tr>
</table>

**Data Explanation**

+ Testing with the `diffusers` library enabled all optimizations included in the library. This scheme has not been
  tested on non-NVIDIA A100/H100 devices. It should generally work with all NVIDIA Ampere architecture or higher
  devices. Disabling optimizations can triple VRAM usage but increase speed by 3-4 times. You can selectively disable
  certain optimizations, including:

```
pipe.enable_sequential_cpu_offload()
pipe.vae.enable_slicing()
pipe.vae.enable_tiling()
```

+ In multi-GPU inference, `enable_sequential_cpu_offload()` optimization needs to be disabled.
+ Using an INT8 model reduces inference speed, meeting the requirements of lower VRAM GPUs while retaining minimal video
  quality degradation, at the cost of significant speed reduction.
+ [PytorchAO](https://github.com/pytorch/ao) and [Optimum-quanto](https://github.com/huggingface/optimum-quanto/) can be
  used to quantize the text encoder, Transformer, and VAE modules, reducing CogVideoX’s memory requirements, making it
  feasible to run the model on smaller VRAM GPUs. TorchAO quantization is fully compatible with `torch.compile`,
  significantly improving inference speed. `FP8` precision is required for NVIDIA H100 and above, which requires source
  installation of `torch`, `torchao`, `diffusers`, and `accelerate`. Using `CUDA 12.4` is recommended.
+ Inference speed testing also used the above VRAM optimizations, and without optimizations, speed increases by about
  10%. Only `diffusers` versions of models support quantization.
+ Models support English input only; other languages should be translated into English during prompt crafting with a
  larger model.

**Note**

+ Use [SAT](https://github.com/THUDM/SwissArmyTransformer) for inference and fine-tuning SAT version models. Check our
  GitHub for more details.

## Getting Started Quickly 🤗

This model supports deployment using the Hugging Face diffusers library. You can follow the steps below to get started.

**We recommend that you visit our [GitHub](https://github.com/THUDM/CogVideo) to check out prompt optimization and
conversion to get a better experience.**

1. Install the required dependencies



```shell
# diffusers (from source)
# transformers>=4.46.2
# accelerate>=1.1.1
# imageio-ffmpeg>=0.5.1
pip install git+https://github.com/huggingface/diffusers
pip install --upgrade transformers accelerate diffusers imageio-ffmpeg
```

2. Run the code

```python
import torch
from diffusers import CogVideoXImageToVideoPipeline
from diffusers.utils import export_to_video, load_image

prompt = "A little girl is riding a bicycle at high speed. Focused, detailed, realistic."
image = load_image(image="input.jpg")
pipe = CogVideoXImageToVideoPipeline.from_pretrained(
    "THUDM/CogVideoX1.5-5B-I2V",
    torch_dtype=torch.bfloat16
)

pipe.enable_sequential_cpu_offload()
pipe.vae.enable_tiling()
pipe.vae.enable_slicing()

video = pipe(
    prompt=prompt,
    image=image,
    num_videos_per_prompt=1,
    num_inference_steps=50,
    num_frames=81,
    guidance_scale=6,
    generator=torch.Generator(device="cuda").manual_seed(42),
).frames[0]

export_to_video(video, "output.mp4", fps=8)
```

## Quantized Inference

[PytorchAO](https://github.com/pytorch/ao) and [Optimum-quanto](https://github.com/huggingface/optimum-quanto/) can be
used to quantize the text encoder, transformer, and VAE modules to reduce CogVideoX's memory requirements. This allows
the model to run on free T4 Colab or GPUs with lower VRAM! Also, note that TorchAO quantization is fully compatible
with `torch.compile`, which can significantly accelerate inference.

```python
# To get started, PytorchAO needs to be installed from the GitHub source and PyTorch Nightly.
# Source and nightly installation is only required until the next release.

import torch
from diffusers import AutoencoderKLCogVideoX, CogVideoXTransformer3DModel, CogVideoXImageToVideoPipeline
from diffusers.utils import export_to_video, load_image
from transformers import T5EncoderModel
from torchao.quantization import quantize_, int8_weight_only

quantization = int8_weight_only

text_encoder = T5EncoderModel.from_pretrained("THUDM/CogVideoX1.5-5B-I2V", subfolder="text_encoder",
                                              torch_dtype=torch.bfloat16)
quantize_(text_encoder, quantization())

transformer = CogVideoXTransformer3DModel.from_pretrained("THUDM/CogVideoX1.5-5B-I2V", subfolder="transformer",
                                                          torch_dtype=torch.bfloat16)
quantize_(transformer, quantization())

vae = AutoencoderKLCogVideoX.from_pretrained("THUDM/CogVideoX1.5-5B-I2V", subfolder="vae", torch_dtype=torch.bfloat16)
quantize_(vae, quantization())

# Create pipeline and run inference
pipe = CogVideoXImageToVideoPipeline.from_pretrained(
    "THUDM/CogVideoX1.5-5B-I2V",
    text_encoder=text_encoder,
    transformer=transformer,
    vae=vae,
    torch_dtype=torch.bfloat16,
)

pipe.enable_model_cpu_offload()
pipe.vae.enable_tiling()
pipe.vae.enable_slicing()

prompt = "A little girl is riding a bicycle at high speed. Focused, detailed, realistic."
image = load_image(image="input.jpg")
video = pipe(
    prompt=prompt,
    image=image,
    num_videos_per_prompt=1,
    num_inference_steps=50,
    num_frames=81,
    guidance_scale=6,
    generator=torch.Generator(device="cuda").manual_seed(42),
).frames[0]

export_to_video(video, "output.mp4", fps=8)
```

Additionally, these models can be serialized and stored using PytorchAO in quantized data types to save disk space. You
can find examples and benchmarks at the following links:

- [torchao](https://gist.github.com/a-r-r-o-w/4d9732d17412888c885480c6521a9897)
- [quanto](https://gist.github.com/a-r-r-o-w/31be62828b00a9292821b85c1017effa)

## Further Exploration

Feel free to enter our [GitHub](https://github.com/THUDM/CogVideo), where you'll find:

1. More detailed technical explanations and code.
2. Optimized prompt examples and conversions.
3. Detailed code for model inference and fine-tuning.
4. Project update logs and more interactive opportunities.
5. CogVideoX toolchain to help you better use the model.
6. INT8 model inference code.

## Model License

This model is released under the [CogVideoX LICENSE](LICENSE).

## Citation

```
@article{yang2024cogvideox,
  title={CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer},
  author={Yang, Zhuoyi and Teng, Jiayan and Zheng, Wendi and Ding, Ming and Huang, Shiyu and Xu, Jiazheng and Yang, Yuanming and Hong, Wenyi and Zhang, Xiaohan and Feng, Guanyu and others},
  journal={arXiv preprint arXiv:2408.06072},
  year={2024}
}
```



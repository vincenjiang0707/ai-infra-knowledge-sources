source: https://docs.vllm.ai/projects/recipes/en/stable/Qwen/Qwen-Image.html
lastmod: 2026-04-27

# Qwen-Image Usage Guide[¶](https://docs.vllm.ai#qwen-image-usage-guide)

Qwen-Image models include the following models:

| Model | HuggingFace | Description |
|---|---|---|
Qwen-Image |
|

**Qwen-Image-2512**[🤗 Qwen/Qwen-Image-2512](https://huggingface.co/Qwen/Qwen-Image-2512)**Qwen-Image-Edit**[🤗 Qwen/Qwen-Image-Edit](https://huggingface.co/Qwen/Qwen-Image-Edit)**Qwen-Image-Edit-2509**[🤗 Qwen/Qwen-Image-Edit-2509](https://huggingface.co/Qwen/Qwen-Image-Edit-2509)**Qwen-Image-Edit-2511**[🤗 Qwen/Qwen-Image-Edit-2511](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)**Qwen-Image-Layered**[🤗 Qwen/Qwen-Image-Layered](https://huggingface.co/Qwen/Qwen-Image-Layered)All models share the same DiT transformer core; hence, the acceleration methods (e.g., cache methods, parallelism methods) are applicable across the entire series.

## Installation[¶](https://docs.vllm.ai#installation)

# Clone and install vllm-omni
git clone https://github.com/vllm-project/vllm-omni.git
cd vllm-omni
uv venv
source .venv/bin/activate
uv pip install -e . vllm==0.18.0


## Usage[¶](https://docs.vllm.ai#usage)

### Text-to-Image (Qwen-Image, Qwen-Image-2512)[¶](https://docs.vllm.ai#text-to-image-qwen-image-qwen-image-2512)

Qwen-Image and Qwen-Image-2512 are text-to-image models. Use the `text_to_image.py`

script:

# Qwen-Image (default)
python3 ./examples/offline_inference/text_to_image/text_to_image.py \
--model Qwen/Qwen-Image \
--prompt "a cup of coffee on the table" \
--output output_qwen_image.png \
--num-inference-steps 50 \
--cfg-scale 4.0
# Qwen-Image-2512
python3 ./examples/offline_inference/text_to_image/text_to_image.py \
--model Qwen/Qwen-Image-2512 \
--prompt "a cup of coffee on the table" \
--output output_qwen_image_2512.png \
--num-inference-steps 50 \
--cfg-scale 4.0


Notes: 1. vLLM-Omni enables torch.compile by default. Try

`--enforce-eager`

if you want to disable it. 2. vLLM-Omni does not enable CPU offload automatically. If you encounter OOM, please`--enable-cpu-offload`

or`--enable-layerwise-offload`

.

### Image Editing (Qwen-Image-Edit)[¶](https://docs.vllm.ai#image-editing-qwen-image-edit)

Qwen-Image-Edit is the image editing version of Qwen-Image. It simultaneously feeds the input image into Qwen2.5-VL (for visual semantic control) and the VAE Encoder (for visual appearance control), achieving capabilities in both semantic and appearance editing.

# Single image input (Qwen-Image-Edit)
python3 ./examples/offline_inference/image_to_image/image_edit.py \
--model Qwen/Qwen-Image-Edit \
--image qwen_bear.png \
--prompt "Let this mascot dance under the moon, surrounded by floating stars and poetic bubbles such as 'Be Kind'" \
--output output_image_edit.png \
--num-inference-steps 50 \
--cfg-scale 4.0


For multiple image inputs, use `Qwen/Qwen-Image-Edit-2509`

or `Qwen/Qwen-Image-Edit-2511`

:

# Qwen-Image-Edit-2511 example (multiple images)
python3 ./examples/offline_inference/image_to_image/image_edit.py \
--model Qwen/Qwen-Image-Edit-2511 \
--image image1.png image2.png \
--prompt "Add a white art board written with colorful text 'vLLM-Omni' on grassland. Add a paintbrush in the bear's hands. position the bear standing in front of the art board as if painting" \
--output output_image_edit.png \
--num-inference-steps 50 \
--cfg-scale 4.0


### Image Layering (Qwen-Image-Layered)[¶](https://docs.vllm.ai#image-layering-qwen-image-layered)

Qwen-Image-Layered decomposes an input image into multiple RGBA layers:

python3 ./examples/offline_inference/image_to_image/image_edit.py \
--model Qwen/Qwen-Image-Layered \
--image input.png \
--prompt "" \
--output layered \
--num-inference-steps 50 \
--cfg-scale 4.0 \
--layers 4 \
--color-format "RGBA"


### Key Arguments[¶](https://docs.vllm.ai#key-arguments)

| Argument | Description |
|---|---|
`--model` |
Model name or local path. Use `Qwen/Qwen-Image-Edit-2509` or later for multiple image support. |
`--image` |
Path(s) to the source image(s) (PNG/JPG, converted to RGB). Can specify multiple images. |
`--prompt` / `--negative-prompt` |
Text description (string). |
`--cfg-scale` |
True classifier-free guidance scale (default: 4.0). Classifier-free guidance is enabled by setting `cfg_scale > 1` and providing a `negative_prompt` . Higher guidance scale encourages images closely linked to the text prompt, usually at the expense of lower image quality. |
`--guidance-scale` |
Guidance scale for guidance-distilled models (default: 1.0, disabled). Unlike classifier-free guidance (`--cfg-scale` ), guidance-distilled models take the guidance scale directly as an input parameter. Enabled when `guidance_scale > 1` . Ignored when not using guidance-distilled models. |
`--num-inference-steps` |
Diffusion sampling steps (more steps = higher quality, slower). |
`--output` |
Path to save the generated PNG. For Qwen-Image-Layered, this is used as the filename prefix. |
`--vae-use-slicing` |
Enable VAE slicing for memory optimization. |
`--vae-use-tiling` |
Enable VAE tiling for memory optimization. |
`--cfg-parallel-size` |
Set to `2` to enable CFG Parallel. |
`--enable-cpu-offload` |
Enable CPU offloading for diffusion models. |
`--layers` |
Number of layers to decompose the input image into (Qwen-Image-Layered only). |
`--color-format` |
Output color channel format (`RGB` or `RGBA` ). Qwen-Image-Layered uses `RGBA` . |

## Acceleration Methods[¶](https://docs.vllm.ai#acceleration-methods)

### Cache Acceleration[¶](https://docs.vllm.ai#cache-acceleration)

vLLM-Omni supports **cache-dit** and **tea-cache** for Qwen-Image models.

#### Cache-DiT[¶](https://docs.vllm.ai#cache-dit)

# Text-to-Image with Cache-DiT
python3 ./examples/offline_inference/text_to_image/text_to_image.py \
--model Qwen/Qwen-Image \
--prompt "a cup of coffee on the table" \
--cache-backend cache_dit


Advanced Cache-DiT options:

python3 ./examples/offline_inference/image_to_image/image_edit.py \
--model Qwen/Qwen-Image-Edit \
--image qwen_bear.png \
--prompt "Edit description" \
--cache-backend cache_dit \
--cache-dit-max-continuous-cached-steps 3 \
--cache-dit-residual-diff-threshold 0.24 \
--cache-dit-enable-taylorseer


#### TeaCache[¶](https://docs.vllm.ai#teacache)

# Text-to-Image with TeaCache
python3 ./examples/offline_inference/text_to_image/text_to_image.py \
--model Qwen/Qwen-Image \
--prompt "a cup of coffee on the table" \
--cache-backend tea_cache


### Ulysses Sequence Parallelism[¶](https://docs.vllm.ai#ulysses-sequence-parallelism)

Distributes computation across GPUs without quality loss. Recommended for high-resolution images (>1536px) with 2–8 GPUs.

# Text-to-Image with Ulysses SP
python3 ./examples/offline_inference/text_to_image/text_to_image.py \
--model Qwen/Qwen-Image \
--prompt "a cup of coffee on the table" \
--ulysses-degree 4
# Image Editing with Ulysses SP
python3 ./examples/offline_inference/image_to_image/image_edit.py \
--model Qwen/Qwen-Image-Edit \
--image qwen_bear.png \
--prompt "Add a white art board written with colorful text 'vLLM-Omni' on grassland." \
--output output_image_edit.png \
--num-inference-steps 50 \
--cfg-scale 4.0 \
--ulysses-degree 4


### Ring-Attention Sequence Parallelism[¶](https://docs.vllm.ai#ring-attention-sequence-parallelism)

Ring-based sequence parallelism, suitable for memory-constrained environments with very long sequences.

# Text-to-Image with Ring-Attention
python3 ./examples/offline_inference/text_to_image/text_to_image.py \
--model Qwen/Qwen-Image \
--prompt "a cup of coffee on the table" \
--ring-degree 4
# Image Editing with Ring-Attention
python3 ./examples/offline_inference/image_to_image/image_edit.py \
--model Qwen/Qwen-Image-Edit \
--image qwen_bear.png \
--prompt "Edit description" \
--ring-degree 4


### CFG Parallelism[¶](https://docs.vllm.ai#cfg-parallelism)

Splits classifier-free guidance positive/negative branches across 2 GPUs. Particularly effective for image editing with `cfg-scale > 1`

.

# Image Editing with CFG Parallel (2 GPUs)
python3 ./examples/offline_inference/image_to_image/image_edit.py \
--model Qwen/Qwen-Image-Edit \
--image qwen_bear.png \
--prompt "Edit description" \
--cfg-parallel-size 2 \
--num-inference-steps 50 \
--cfg-scale 4.0


### Tensor Parallelism[¶](https://docs.vllm.ai#tensor-parallelism)

Shards model weights across multiple GPUs. Useful for running the 20B model across 2+ GPUs.

# Text-to-Image with Tensor Parallelism (2 GPUs)
python3 ./examples/offline_inference/text_to_image/text_to_image.py \
--model Qwen/Qwen-Image \
--prompt "a cup of coffee on the table" \
--tensor-parallel-size 2
# Image Editing with Tensor Parallelism
python3 ./examples/offline_inference/image_to_image/image_edit.py \
--model Qwen/Qwen-Image-Edit \
--image qwen_bear.png \
--prompt "Edit description" \
--tensor-parallel-size 2


### CPU Offload[¶](https://docs.vllm.ai#cpu-offload)

Offloads DiT layers to CPU memory between forward passes. Enables inference on limited VRAM.

# Text-to-Image with CPU offload (module-wise)
python3 ./examples/offline_inference/text_to_image/text_to_image.py \
--model Qwen/Qwen-Image \
--prompt "a cup of coffee on the table" \
--enable-cpu-offload
# Image Editing with CPU offload (layerwise, saves more VRAM, but slower)
python3 ./examples/offline_inference/image_to_image/image_edit.py \
--model Qwen/Qwen-Image-Edit \
--image qwen_bear.png \
--prompt "Edit description" \
--enable-layerwise-offload


### VAE Patch Parallelism[¶](https://docs.vllm.ai#vae-patch-parallelism)

Distributes VAE decode tiling across GPUs, reducing peak VAE memory usage at high resolutions.

# Text-to-Image with VAE Patch Parallelism
python3 ./examples/offline_inference/text_to_image/text_to_image.py \
--model Qwen/Qwen-Image \
--prompt "a cup of coffee on the table" \
--height 1536 --width 1536 \
--ulysses-degree 2 \
--vae-patch-parallel-size 2


VAE patch parallelism cannot be used alone. It must be used together with other parallelism methods.


### Quantization[¶](https://docs.vllm.ai#quantization)

Qwen-Image and Qwen-Image-2512 support FP8 and INT8 quantization. Qwen-Image-Edit variants do **not** support quantization.

#### FP8[¶](https://docs.vllm.ai#fp8)

# Text-to-Image with FP8 quantization
python3 ./examples/offline_inference/text_to_image/text_to_image.py \
--model Qwen/Qwen-Image \
--prompt "a cup of coffee on the table" \
--quantization fp8
# Skip sensitive layers (recommended for better quality)
python3 ./examples/offline_inference/text_to_image/text_to_image.py \
--model Qwen/Qwen-Image \
--prompt "a cup of coffee on the table" \
--quantization fp8 \
--ignored-layers "img_mlp"


#### INT8[¶](https://docs.vllm.ai#int8)

python3 ./examples/offline_inference/text_to_image/text_to_image.py \
--model Qwen/Qwen-Image \
--prompt "a cup of coffee on the table" \
--quantization int8


## Feature Support Summary[¶](https://docs.vllm.ai#feature-support-summary)

For detailed features support for Qwen-Image series models in vLLM-Omni, see the

[Feature Support Table]For detailed compatibility between features (e.g., combining Cache + SP + CFG-Parallel), see the[Feature Compatibility Guide].

## Combining Acceleration Methods[¶](https://docs.vllm.ai#combining-acceleration-methods)

A few guidelines help pick the right combination:

**Cache**(TeaCache or Cache-DiT) reduces redundant DiT computation per inference.**Parallelism**(SP, TP, CFG-parallel, VAE patch) splits work across GPUs. Use one cache backend together with any supported parallel strategy. See the[Feature Compatibility Guide](https://github.com/vllm-project/vllm-omni/blob/main/docs/user_guide/feature_compatibility.md)for supported combinations.**TeaCache and Cache-DiT cannot be used together.****Sequence parallelism (Ulysses / Ring)**is the best parallelism choice for high-resolution or long-sequence workloads. It generally outperforms tensor parallelism (TP) in these settings by distributing token-dimension computation across GPUs.**Tensor parallelism**is most useful when model weights alone do not fit on a single GPU.**CFG parallelism**targets non-distilled diffusion with full classifier-free guidance (`--cfg-scale > 1`

). It assigns the positive and negative CFG branches to separate GPUs, achieving up to ~1.5× speedup when guidance is the dominant cost. It is not well-suited for guidance-distilled models (CFG is not applied).**To reduce peak VRAM**, use`--enable-cpu-offload`

,`--enable-layerwise-offload`

or pair`--vae-patch-parallel-size`

with another parallel method to lower VAE decode memory at high resolutions.**To trade quality for speed**, FP8 / INT8 quantization is available for Qwen-Image and Qwen-Image-2512.

### Examples[¶](https://docs.vllm.ai#examples)

**1) Sequence parallelism only:**

python3 ./examples/offline_inference/text_to_image/text_to_image.py \
--model Qwen/Qwen-Image \
--prompt "a cup of coffee on the table" \
--ulysses-degree 4


**2) Cache only (single GPU):**

python3 ./examples/offline_inference/text_to_image/text_to_image.py \
--model Qwen/Qwen-Image \
--prompt "a cup of coffee on the table" \
--cache-backend cache_dit


**3) Cache + SP (recommended for long sequence generation):**

python3 ./examples/offline_inference/text_to_image/text_to_image.py \
--model Qwen/Qwen-Image \
--prompt "a cup of coffee on the table" \
--cache-backend cache_dit \
--ulysses-degree 4


**4) SP + VAE patch parallel (high-resolution, VRAM-constrained):**

python3 ./examples/offline_inference/text_to_image/text_to_image.py \
--model Qwen/Qwen-Image \
--prompt "a cup of coffee on the table" \
--height 1536 --width 1536 \
--ulysses-degree 2 \
--vae-patch-parallel-size 2


**5) Image editing: cache + CFG parallel:**

python3 ./examples/offline_inference/image_to_image/image_edit.py \
--model Qwen/Qwen-Image-Edit \
--image qwen_bear.png \
--prompt "Edit description" \
--cache-backend cache_dit \
--cfg-parallel-size 2 \
--num-inference-steps 50 \
--cfg-scale 4.0


**6) CPU offload (add when OOM):**

python3 ./examples/offline_inference/text_to_image/text_to_image.py \
--model Qwen/Qwen-Image \
--prompt "a cup of coffee on the table" \
--enable-cpu-offload


**7) Quantization + SP:**
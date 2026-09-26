source: https://docs.vllm.ai/projects/recipes/en/stable/Wan-AI/Wan2.2.html
lastmod: 2026-04-27

# Wan2.2 Usage Guide[¶](https://docs.vllm.ai#wan22-usage-guide)

This guide provides instructions for running Wan2.2 video generation models using vLLM-Omni with Cache-DiT acceleration.

## Supported Models[¶](https://docs.vllm.ai#supported-models)

**Wan-AI/Wan2.2-T2V-A14B-Diffusers**: Text-to-Video (MoE architecture, 14B active parameters)**Wan-AI/Wan2.2-I2V-A14B-Diffusers**: Image-to-Video (MoE architecture, 14B active parameters)**Wan-AI/Wan2.2-TI2V-5B-Diffusers**: Unified Text-to-Video + Image-to-Video (dense 5B)

## Installing vLLM-Omni[¶](https://docs.vllm.ai#installing-vllm-omni)

uv venv
source .venv/bin/activate
uv pip install vllm==0.12.0
uv pip install git+https://github.com/vllm-project/vllm-omni.git@ef01223c42be10ee260b9f6e5ec31894cd09d86e


The CLI examples below are from the vLLM-Omni repo. If you want to run them directly, clone that repo and run the scripts from its `examples/offline_inference`

directory.

## Text-to-Video Generation[¶](https://docs.vllm.ai#text-to-video-generation)

### Basic Usage[¶](https://docs.vllm.ai#basic-usage)

from vllm_omni.entrypoints.omni import Omni
omni = Omni(model="Wan-AI/Wan2.2-T2V-A14B-Diffusers")
frames = omni.generate(
"Two anthropomorphic cats in comfy boxing gear fight on a spotlighted stage.",
height=720,
width=1280,
num_frames=81,
num_inference_steps=40,
guidance_scale=4.0,
)


### CLI Usage[¶](https://docs.vllm.ai#cli-usage)

```bash
python examples/offline_inference/text_to_video/text_to_video.py \
--model Wan-AI/Wan2.2-T2V-A14B-Diffusers \
--prompt "A serene lakeside sunrise with mist over the water." \
--height 720 \
--width 1280 \
--num_frames 81 \
--num_inference_steps 40 \
--guidance_scale 4.0 \
--fps 24 \
--output t2v_output.mp4
```


## Image-to-Video Generation[¶](https://docs.vllm.ai#image-to-video-generation)

### Basic Usage[¶](https://docs.vllm.ai#basic-usage_1)

import PIL.Image
from vllm_omni.entrypoints.omni import Omni
omni = Omni(model="Wan-AI/Wan2.2-I2V-A14B-Diffusers")
image = PIL.Image.open("input.jpg").convert("RGB")
frames = omni.generate(
"A cat playing with yarn",
pil_image=image,
height=480,
width=832,
num_frames=81,
num_inference_steps=50,
guidance_scale=5.0,
)


### CLI Usage[¶](https://docs.vllm.ai#cli-usage_1)

```bash
python examples/offline_inference/image_to_video/image_to_video.py \
--model Wan-AI/Wan2.2-I2V-A14B-Diffusers \
--image input.jpg \
--prompt "A cat playing with yarn" \
--num_frames 81 \
--num_inference_steps 50 \
--guidance_scale 5.0 \
--fps 16 \
--output i2v_output.mp4
```


### TI2V CLI Usage[¶](https://docs.vllm.ai#ti2v-cli-usage)

```bash
python examples/offline_inference/image_to_video/image_to_video.py \
--model Wan-AI/Wan2.2-TI2V-5B-Diffusers \
--image input.jpg \
--prompt "A cat playing with yarn" \
--num_frames 81 \
--num_inference_steps 50 \
--guidance_scale 5.0 \
--fps 16 \
--output ti2v_output.mp4
```


## Cache-DiT Acceleration[¶](https://docs.vllm.ai#cache-dit-acceleration)

vLLM-Omni supports Cache-DiT acceleration for Wan2.2 models, which can significantly speed up video generation through caching mechanisms.

### Enabling Cache-DiT[¶](https://docs.vllm.ai#enabling-cache-dit)

from vllm_omni.entrypoints.omni import Omni
omni = Omni(
model="Wan-AI/Wan2.2-T2V-A14B-Diffusers",
cache_backend="cache_dit",
)
frames = omni.generate(
"A beautiful sunset over the ocean",
height=720,
width=1280,
num_frames=81,
num_inference_steps=40,
)


### Custom Cache-DiT Configuration[¶](https://docs.vllm.ai#custom-cache-dit-configuration)

For fine-tuned control over the acceleration:

omni = Omni(
model="Wan-AI/Wan2.2-T2V-A14B-Diffusers",
cache_backend="cache_dit",
cache_config={
"Fn_compute_blocks": 8,
"Bn_compute_blocks": 0,
"max_warmup_steps": 4,
"residual_diff_threshold": 0.12,
},
)


## Key Parameters[¶](https://docs.vllm.ai#key-parameters)

| Parameter | Default | Description |
|---|---|---|
`height` |
720 (T2V) / auto (I2V) | Video height (multiples of 16) |
`width` |
1280 (T2V) / auto (I2V) | Video width (multiples of 16) |
`num_frames` |
81 | Number of frames to generate |
`num_inference_steps` |
40-50 | Denoising steps |
`guidance_scale` |
4.0-5.0 | Classifier-free guidance scale |
`boundary_ratio` |
0.875 | Boundary split ratio for MoE models |
`flow_shift` |
5.0 (720p) / 12.0 (480p) | Scheduler flow shift |

## Notes[¶](https://docs.vllm.ai#notes)

- The CLI scripts use
`diffusers.utils.export_to_video`

, so`diffusers`

must be installed in the environment where you run them.
# whats-new-for-game-developers-dlss-5-with-3d-guided-neural-rendering-nvidia-ace-updates-and-new-rtx-kit-capabilities

source: https://developer.nvidia.com/blog/whats-new-for-game-developers-dlss-5-with-3d-guided-neural-rendering-nvidia-ace-updates-and-new-rtx-kit-capabilities/

[NVIDIA DLSS 5](https://www.nvidia.com/en-us/geforce/news/dlss-5-3d-guided-neural-rendering/) introduces DLSS 3D-Guided Neural Rendering and granular controls that help game developers add lifelike lighting and material detail while preserving their artistic intent. We also look at updates to [NVIDIA ACE](https://developer.nvidia.com/ace-for-games), RTX Mega Geometry 2.0, and RTX Kit across character AI, high-density geometry, and rendering workflows.

This post covers:

- How DLSS 5 uses the game engine’s rendered frame as the foundation for 3D-Guided Neural Rendering and how NBA 2K27’s developer, Visual Concepts, uses DLSS 5 to enhance materials and lighting while preserving scanned facial geometry
- New NVIDIA ACE speech and inferencing capabilities
- RTX Kit SDK updates including RTX Mega Geometry 2.0 support for streaming continuous level-of-detail clusters

## DLSS 5 introduces 3D-guided neural rendering with developer controls

DLSS 5 with 3D-guided neural rendering extends the graphics pipeline as a final neural-rendering stage. It uses the game engine’s rendered frame, including its artist-authored geometry, textures, and lighting buffers as an unyielding foundation.

The engine frame defines what must remain, while developers direct what may change. Using frame color and motion vectors, the model is designed to add lifelike lighting and material detail while preserving scene structure, character identity, and artistic intent.

Built specifically for real-time 3D rendering, DLSS 5 delivers deterministic, temporally stable output. Operating on a strict one-frame-in, one-frame-out model with game-engine motion vectors keeps results consistent as players move. The compact, specialized model runs locally on a single GeForce RTX 50 Series GPU at up to 4K.

**Controls and integration for developers**

**Art direction:**Developers can choose from among several models, mix them across scenes, gameplay, or cutscenes, and adjust Structure Intensity and Tone Intensity to tune high-frequency detail and broader lighting and color response.**Targeted application:**Developers can use semantic AI masking to apply or hold back the effect across recognized scene elements, then use engine-level masks to isolate props or asset groups such as glassware, water droplets, and foliage.**Input quality:**DLSS 5 noticeably elevates traditional rasterized graphics, but giving the model richer source data, like ray-traced or path-traced lighting, yields dramatically more-accurate results.

DLSS 5 is available now in NBA 2K27, developed by Visual Concepts and published by 2K, for all GeForce RTX 50 Series desktop and laptop GPUs. GeForce NOW Ultimate members can also experience it when streaming from NVIDIA-operated GeForce RTX 5080-powered gaming rigs in the cloud. Visual Concepts uses overall tone and style controls plus a per-pixel uplift control mask to fine-tune character detail while respecting player likenesses.

In *NBA 2K27*, DLSS 5 preserves scanned facial geometry while enhancing skin subsurface scattering, light transmission through hair and ears, and contact shadows.

For more details about DLSS 5, check out our [DLSS 5 article](https://www.nvidia.com/en-us/geforce/news/dlss-5-3d-guided-neural-rendering/). Sign up to be notified for DLSS updates for developers [here](https://developer.nvidia.com/rtx/dlss/notify-me).

## NVIDIA ACE expands model and platform support

NVIDIA ACE offers ready-to-integrate AI models and tools for building knowledgeable, interactive, and conversational in-game characters. The latest updates expand the speech pipeline and inference framework, making it easier for developers to run AI in their games.

To run these models locally alongside game graphics, the NVIDIA In-Game Inferencing (NVIGI) SDK delivers a high-performance, streamlined path for deploying local AI models through in-process C++ execution.

**Key Release Highlights**

: A 600M-parameter Automatic Speech Recognition (ASR) model that transcribes player speech using a streaming architecture designed to minimize latency while maintaining accuracy.**NVIDIA Nemotron Speech 3.5 Streaming**: A 600M-parameter Text-to-Speech model that generates high-quality audio and supports custom fine-tuning.**Qwen3 TTS**

**NVIDIA In-Game Inference SDK Updates**

**RTX Spark Support (Developer Preview)**: Adds early support for RTX Spark, NVIDIA’s new AI and graphics platform for slim laptops and ultra-efficient desktops.**Expanded Model Support**: Integrates Gemma4 into the GPT plugin.**New Plugins & Samples**: Adds a Stable Diffusion plugin along with sample code.**Performance Enhancements**: Incorporates the latest`llama.cpp`

updates to maximize inference performance.

Access NVIDIA In-Game Inference SDK [here](https://developer.nvidia.com/rtx/in-game-inferencing).

## Updates across NVIDIA RTX Kit advance neural rendering and path tracing

NVIDIA RTX Kit is a suite of rendering technologies for training and deploying AI in shaders, path tracing detailed scenes at game-ready performance, and rendering lifelike digital characters. The latest SDK updates expand support for high-density geometry, neural texture workflows, lighting, and texture filtering.

RTX Kit 2026.3 updates include:

- RTX Character Rendering 1.4 improves far-field hair BCSDF sampling and energy conservation
- RTX Dynamic Illumination 3.1 adds DLSS Ray Reconstruction integration and some improvements to ReSTIR PT
- RTX Neural Texture Compression 0.10 beta adds support for the Microsoft DirectX 12 Agility SDK preview with Linear Algebra, enabling RTX Tensor Core acceleration for neural texture decompression in DirectX shaders. It also adds Windows ARM64 support.
- RTX Neural Shading 1.4 adds support for the latest DirectX Linear Algebra preview toolchain and updates its shader and sample dependencies.
- RTX Texture Filtering 1.3 introduces Collaborative Texture Filtering, a technique designed to improve magnification quality for stochastic texture filtering. It also adds Windows ARM64 support.

### RTX Mega Geometry 2.0 is now available

In addition to the RTX Kit updates, [RTX Mega Geometry SDK](https://github.com/NVIDIA-RTX/RTXMG) has been updated to 2.0 which adds support for streaming of continuous level-of-detail clusters for high-density meshes. The scale of detail is demonstrated in a newly released textured glTF version of Zorah.

RTX Mega Geometry is coming soon to Gears of War: E-Day, offering GeForce games higher frame rates, higher levels of image quality, and with even more responsive controls. We sat down with the Coalition’s Studio Technical Director, Kate Rayner, and Rendering Lead, Mike Perzel to learn more about Gears of War: E-Day’s integrations of RTX Mega Geometry and DLSS.

*Video 3. RTX: Inside the Game | Gears of War: E-Day with DLSS 4.5 and RTX Mega Geometry *

## Resources for game developers

Check out the full list of [game developer resources](https://developer.nvidia.com/game-development) and stay up to date with the latest NVIDIA game development news:

- Subscribe to our
[newsletter](https://developer.nvidia.com/email-signup)(select gaming as your industry) - Follow us on social:
[X](https://x.com/NVIDIAGameDev),[LinkedIn](https://www.linkedin.com/showcase/79124990/),[Facebook](https://www.facebook.com/NVIDIAGameDev/), and[YouTube](https://www.youtube.com/@NVIDIAGameDeveloper/featured) - Join our
[Discord community](https://discord.com/invite/C8FKNVMnhq)

## Start the discussion at forums.developer.nvidia.com

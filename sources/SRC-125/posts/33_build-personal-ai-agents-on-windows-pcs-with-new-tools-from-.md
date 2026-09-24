# build-personal-ai-agents-on-windows-pcs-with-new-tools-from-microsoft-and-nvidia

source: https://developer.nvidia.com/blog/build-personal-ai-agents-on-windows-pcs-with-new-tools-from-microsoft-and-nvidia/

[AI agents](https://www.nvidia.com/en-us/ai/) are changing how you interact with your PC. Creators, developers, and AI enthusiasts are already using these agents extensively to assist with day-to-day tasks such as coding, video editing, and content management.

NVIDIA and Microsoft are teaming up to enable the next generation of developers to build on-device agents on the Windows platform, with easier setup, native security, and integration with the apps and tools developers already use.

This post details new tools NVIDIA and Microsoft unveiled at [NVIDIA GTC Taipei at COMPUTEX 2026](https://www.nvidia.com/en-tw/gtc/taipei/computex/) and [Microsoft Build 2026](https://www.nvidia.com/en-us/events/microsoft-build/) to meet the exploding demand for agents. These tools include turnkey agent sandboxing on native Windows, 2x faster agentic inference, new agent apps and tools from Nous Research and H Company, and enhanced multi-GPU support across llama.cpp and [ComfyUI](https://comfy.org/download). The local AI development stack is now ready to run complex agentic AI workflows alongside users.

## How to secure local agents with Microsoft eXecution Containers and NVIDIA OpenShell

At Microsoft Build, Microsoft announced a set of security primitives to allow agents to execute code, operate on files, and orchestrate tasks across systems with built-in identity and policy execution. The Microsoft eXecution Containers (MXC) form the policy layer, defining and instrumenting isolation and containment while relying on native Windows operating system constructs to apply these policies.

For developers, this lowers a critical barrier: agents interacting with personal files and apps pose real prompt injection risks, and MXC ensures they can’t access the full system.

NVIDIA is also collaborating with Microsoft to bring NVIDIA [OpenShell](https://github.com/NVIDIA/OpenShell) runtime to Windows, built on MXC. Integrating MXC through OpenShell provides an easy-to-integrate package for developers to deploy autonomous, always-on agents safely, while providing additional capabilities such as policy creation and management, inference routing, and personally identifiable information (PII) obfuscation.

Top agentic apps are looking to leverage MXC and OpenShell to strengthen their security in Windows, including the popular open source agents [OpenClaw](https://github.com/openclaw/openclaw) and [Hermes Agent](https://github.com/nousresearch/hermes-agent).

**How does NVIDIA RTX Spark power personal AI agents?**

Earlier this week at GTC Taipei, NVIDIA unveiled the [NVIDIA RTX Spark](https://www.nvidia.com/en-us/products/rtx-spark/) product family, including small form factor desktops and laptops built for the age of personal assistants. These desktops and laptops deliver 1 petaflop of AI power, up to 128 GB of memory, and CUDA-accelerated AI frameworks for running large models alongside everyday work.

Microsoft is creating an RTX Spark special developer edition—the Surface RTX Spark Dev Box—preloaded with a modified Windows configured for developers and the top developer tools you need to get started. To learn more, see [Building the next generation of devices for developers: Surface RTX Spark Dev Box](https://blogs.windows.com/devices/2026/06/02/building-the-next-generation-of-devices-for-developers-surface-rtx-spark-dev-box/).

**How are NVIDIA NemoClaw, Hermes Agent, and H Company expanding agent capabilities?**

[NVIDIA NemoClaw](https://www.nvidia.com/en-us/ai/nemoclaw/) for building [autonomous AI agents](https://www.nvidia.com/en-us/glossary/ai-agents/) now supports all NVIDIA client systems—[GeForce RTX](https://www.nvidia.com/en-us/geforce/rtx/), [NVIDIA RTX PRO](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/), [NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/), and [NVIDIA DGX Station for Windows](https://www.nvidia.com/en-us/products/workstations/dgx-station-for-windows/)—through Linux and Windows Subsystem for Linux (WSL). This enables you to easily set up and sandbox an agent, with optimized local models handpicked for your hardware. The update also includes enhancements to the installer to make it easier and more seamless. NemoClaw also now supports running Hermes Agent as an option.

This week, Hermes Agent also released native Windows support, including both a command-line interface, alongside a sleek, new desktop application. This streamlines the user experience, while making it easier for the agent to interact with and use native Windows apps, APIs, and files.

In addition, AI research and product firm H Company released their new Holo 3.1 range of models. These models are tuned for Computer Use, a mode that enables agents to take actions by seeing the screen and clicking, extending agentic capabilities across a broader range of apps. They include quantized checkpoints for 35% lower memory compared to FP8. The company also announced a new Computer Use harness with support for local models, coming soon. NVIDIA has helped H Company optimize their new models and harness to deliver over 2x performance on NVIDIA GPUs.

**How are NVIDIA and the OSS community accelerating inference for local agentic AI?**

With agents running 24 hours a day, seven days a week on increasingly complex tasks, efficient local compute matters even more. NVIDIA has collaborated with the open source community to enhance the top inference backends for agents, llama.cpp and vLLM.

llama.cpp now delivers 2x performance on Qwen 3.5 and 3.6 27B dense models, and 1.6x performance on Qwen 3.5 and 3.6 35B mixture-of-expert (MoE) models. The following two techniques make this possible:

**Multi-Token Prediction (MTP)**: An advanced speculative decoding technique, where a smaller draft model proposes several tokens ahead that the target model verifies in a single forward pass, delivering faster throughput at identical output quality. MTP is the most practical for developers because it requires no additional training for models that already support it.**Programmatic Dependent Launch****(PDL)**: This update provides faster decode performance. Dependent kernels can be concurrently executed on the same CUDA stream. Prior to this, dependent kernels in a single CUDA stream had to be sequential.

vLLM has already adopted MTP, but is receiving additional optimizations that improve inference performance by 2.6x. These include better BF16 kernel selection for MoE models and reduced runtime overhead through improvements to CUDA Graphs.

You can start exploring these updates now through LM Studio, llama.cpp, and vLLM.

## How does multi-GPU support scale AI performance for RTX PCs?

One popular way to run AI locally has been to use multiple GPUs to access more memory and compute. While cloud frameworks like vLLM are well optimized for multiple GPUs thanks to their use in data centers, PC frameworks like llama.cpp and the ComfyUI implementation in PyTorch are not optimized for it.

To solve this challenge, NVIDIA has collaborated with both llama.cpp and ComfyUI to enhance performance for RTX PCs with two equivalent GPUs. This enables you to run larger models and use the compute of both GPUs for better performance.

llama.cpp now supports tensor parallelism (TP), fully utilizing both GPUs for up to ~2x memory capacity and up to ~1.8x compute performance. LM Studio has made these changes available for wider use through their application. To get started with LM Studio, Open the LM Studio app, select Settings, then select Runtime to enable TP.

ComfyUI integrates the Classifier-Free Guidance (CFG) method for up to 2x compute across two GPUs. Users can also split model chains across GPUs to fully load them in memory, enabling them to run the high VRAM mode. This eliminates the memory swapping overhead of low VRAM mode for an additional performance gain.

To get started with multi-GPU inference, check out the [llama.cpp](https://github.com/ggml-org/llama.cpp/blob/master/docs/multi-gpu.md) GitHub repo and [How to Build a Multi-GPU AI PC](https://build.nvidia.com/rtx/multi-gpu).

## What’s new for media and video developers?

The [NVIDIA AI for Media SDK (AI4M)](https://developer.nvidia.com/topics/ai/generative-ai/ai-for-media) is now available under private access for developers building AI-powered video and broadcast pipelines. It includes the following features:

**LipSync reaches GA:**With language-optimized models now supporting French, German, and Spanish, LipSync enables higher-quality dubbing and content localization with improved articulation over the base model.**Active Speaker Detection (ASD) GA:**Enhanced multicamera and multimic support plus cross-video speaker ID correlation unlock automated workflows—lip-sync dubbing, video editing, and advanced logging—that previously required manual effort.

## More tools for GPU-accelerated AI development and deployment on Windows

The broader Windows AI platform with Windows ML continues to mature, powered by NVIDIA [TensorRT for RTX](https://github.com/NVIDIA/TensorRT-RTX/tree/main) on NVIDIA GPUs. Developers now have multiple paths to ship GPU-accelerated AI in Windows applications.

Windows AI Foundry and Windows AI APIs are now GPU accelerated. When you call a supported API on RTX hardware, workloads are routed for higher-performance local inference on NVIDIA GPUs. The first supported model is Phi-Silica, a 3.3B small language model (SLM) for summarization, rewriting, code generation, and other on-device AI tasks.

Windows ML and TensorRT for RTX adoption continue to gain momentum. Four partners have recently upgraded from DirectML:

- Voicemod achieves 42% faster real-time AI voice conversion
- Topaz delivers 20% faster 1080p-to-4K upscaling while reducing engine storage by 3-4x
- DxO PhotoLab 9.7 ships faster AI photo processing
- Camo Streamlight AI autotune feature intelligently adjust light levels in real time

For those interested in running Linux applications in Windows, the new Windows Subsystem for Linux Containers (WSL-C) is a built-in way to create, run, and interact with Linux AI containers from native Windows applications. Application users do not need to install and manage WSL system resources themselves, and developers can build this functionality into their apps using a C/C++ library. WSL-C unlocks complex, professional-grade development environments directly on Windows PCs, enabling you to work faster, iterate locally, and maintain parity with production workflows.

## Get started building personal AI agents on Windows PCs

AI agents are reshaping how software is built, used, and deployed—and the local AI stack on NVIDIA RTX is ready. With secure agent sandboxing, faster inference, multi-GPU scaling, and a maturing Windows AI platform, developers building on the over 100 million NVIDIA RTX PCs worldwide have the infrastructure to ship the next generation of AI applications.

Learn more and [start developing for NVIDIA RTX AI PCs](https://developer.nvidia.com/ai-apps-for-rtx-pcs).

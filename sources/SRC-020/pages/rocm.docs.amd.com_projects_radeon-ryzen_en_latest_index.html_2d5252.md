source: https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/index.html

# Use ROCm on Radeon and Ryzen[#](https://rocm.docs.amd.com#use-rocm-on-radeon-and-ryzen)

**Unlock Local AI Development on Your AMD Hardware**

Transform your AMD-powered system into a powerful and private machine learning workstation. With the latest ROCm™ software stack, you can now harness the full potential of high-end AMD Radeon™ GPUs and Ryzen™ APUs for your AI workflows on both Linux® and Windows®.

ROCm™ 7.2.1 supports the latest Radeon™ 9000 Series (RDNA™ 4) and select 7000 Series (RDNA™ 3) GPUs, and introduces support for Ryzen™ APUs, enabling cost-effective, local development and inference for researchers and engineers using Pytorch.

## Expanded Platform Support[#](https://rocm.docs.amd.com#expanded-platform-support)

Quickly see what’s supported on your system. ROCm™ 7.2.1 focuses on bringing PyTorch support to new platforms while maintaining robust support on our established Linux platform for Radeon GPUs.

Hardware |
Operating System |
Supported Frameworks |
|---|---|---|
Radeon™ GPUs (9000 & select 7000 Series) |
Linux® |
PyTorch, TensorFlow, JAX, ONNX |
Radeon™ GPUs (9000 & select 7000 Series) |
Windows® |
PyTorch |
Ryzen™ APUs (AI Max 300 Series, select AI 400 Series & select AI 300 Series) |
Linux®, Windows® |
PyTorch |

## Your Local, Private AI Powerhouse[#](https://rocm.docs.amd.com#your-local-private-ai-powerhouse)

Modern AI models demand significant computational power and memory. A local workstation equipped with a Radeon™ GPU, featuring up to 48GB of VRAM, offers a secure and economical alternative to relying solely on cloud-based solutions. Furthermore, expanded support to Ryzen™ APUs, with up to 128GB of shared memory, allow even laptop users to develop ML workflows securely and efficiently.

## Leadership in Open-Source GPU Programming[#](https://rocm.docs.amd.com#leadership-in-open-source-gpu-programming)

**ROCm is the leading open-source software foundation for GPU programming**. The same ROCm™ stack that powers your desktop development on RDNA™ architecture GPUs also supports AMD Instinct™ accelerators on CDNA™ architecture in the datacenter. This unified platform creates a seamless migration path, allowing you to develop applications locally and deploy them at scale with confidence. This maximizes GPU hardware investments, facilitating the development, testing, and deployment of AI workloads, GPU-accelerated HPC, scientific computing, CAD, and other applications.

As a primarily open-source ecosystem, ROCm™ gives you the freedom to inspect, customize, and tailor the software stack to your specific needs, backed by a collaborative community of developers.

## ROCm™ Key Capabilities[#](https://rocm.docs.amd.com#rocm-key-capabilities)

Frequent ROCm™ releases introduce major platform expansions and key software improvements.

**New Platform Updates**:

**Windows**: PyTorch on Windows updated with ROCm 7.2.1 on AMD Radeon graphics products and AMD Ryzen AI processors.**WSL ROCDXG**: This release marks the first time AMD is supporting Ryzen Strix and Strix Halo SKUs versus the legacy WSL solution. AMD is introducing production support for the open-source ROCDXG (librocdxg) WSL solution with Adrenalin 26.2.2 + ROCm 7.2.1.

**Established Features & Framework Support (Radeon on Linux)**:

**Pytorch and Tensorflow**: Full and established support for both training and inference.**vLLM**: Full support.**JAX**: Support for JAX (inference only).**Llama.cpp**: Supported for efficient inference.**FlashAttention-2**: Backward pass enabled for more efficient training.**ONNX Runtime**: Expanded support for INT8 and INT4 inference with MIGraphX.**Operating Systems**: Support for Red Hat Enterprise Linux (RHEL) 10.1 (AMD Radeon graphics products only) as well as Ubuntu.See the full support matrices

[here](https://rocm.docs.amd.com/docs/compatibility/compatibility.html)

## Get Started[#](https://rocm.docs.amd.com#get-started)

Ready to build? Find all the resources you need at the links below.

**AMD Playbooks**:[Visit the Developer AMD AI Playbooks](https://developer.amd.com/playbooks/)**ROCm Documentation for Instinct™**:[Visit the Official ROCm for Instinct Documentation Hub](https://rocmdocs.amd.com/)**Compatibility Matrices**:[Check Full Hardware/Software Compatibility](https://rocm.docs.amd.com/docs/compatibility/compatibility.html)**Linux Drivers**:[Download the Latest Radeon™ Software for Linux](https://www.amd.com/en/support/download/linux-drivers.html)**Experiment with TheRock**:[Try the ROCm 7.13.0 Technology Preview Release](https://rocm.docs.amd.com/en/7.13.0-preview/index.html)**Join the Developer Discord**:[Join the AMD Developer Discord](https://discord.com/invite/amd-dev)**ROCm Documentation: AMD Strix Halo system optimization**:[AMD Strix Halo system optimization — ROCm Documentation](https://rocm.docs.amd.com/en/latest/how-to/system-optimization/strixhalo.html)
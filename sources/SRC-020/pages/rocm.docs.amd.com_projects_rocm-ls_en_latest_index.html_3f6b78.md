source: https://rocm.docs.amd.com/projects/rocm-ls/en/latest/index.html

# ROCm Life Science documentation[#](https://rocm.docs.amd.com#rocm-life-science-documentation)

2026-09-22

2 min read time

The AMD ROCm™ Life Science (ROCm-LS) toolkit is a GPU-accelerated library suite developed for life science and healthcare applications, offering a robust set of tools optimized for AMD hardware. It is an open-source software collection for high-performance life science applications built on the core ROCm platform, which helps you to accelerate life science processing and analyze workloads on AMD accelerators and GPUs.

You can leverage ROCm-LS to accelerate both new and existing life science workloads, utilizing the speed of AMD devices to execute intensive applications with larger datasets. ROCm-LS creates scalable solutions to address the needs of today’s data-driven landscape. With ROCm-LS, you can build pre- and post-processing applications for your AI models and accelerate your existing life science pipelines with minimal effort.

The ROCm-LS libraries provide tools to build a complete workflow for life science acceleration on AMD GPUs:

**hipCIM:**A high-performance GPU imaging library that accelerates and scales image processing workflows on AMD Instinct™ GPUs.**MONAI on ROCm:**An open-source framework that brings advanced deep learning capabilities for medical imaging to AMD GPU platforms.

MONAI on ROCm provides out-of-the-box integration with hipCIM, enabling accelerated image I/O and transformation operations for supported whole-slide images (WSI). Together, hipCIM and MONAI on ROCm enable researchers and healthcare professionals to streamline scientific imaging pipelines, enhance computational performance, and accelerate innovation across a wide range of life science use cases.

The documentation is structured as follows:

For ready-to-run code samples that demonstrate the ROCm-LS capabilities on the AMD ROCm platform, see the [ROCm-LS examples](https://github.com/ROCm-LS/examples).
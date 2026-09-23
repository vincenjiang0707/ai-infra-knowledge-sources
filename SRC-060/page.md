# 腾讯 Hunyuan

source: https://github.com/PaddlePaddle/ERNIE/releases

# Releases: PaddlePaddle/ERNIE

## Release list

## ERNIE 4.5 Open-source

# ERNIE 4.5

We introduce ERNIE 4.5, a new family of large-scale multimodal models comprising 10 distinct variants. The model family consist of Mixture-of-Experts (MoE) models with 47B and 3B active parameters, with the largest model having 424B total parameters, as well as a 0.3B dense model. For the MoE architecture, we propose a novel heterogeneous modality structure, which supports parameter sharing across modalities while also allowing dedicated parameters for each individual modality. This MoE architecture has the advantage to enhance multimodal understanding without compromising, and even improving, performance on text-related tasks. All of our models are trained with optimal efficiency using the [PaddlePaddle](https://github.com/PaddlePaddle/Paddle) deep learning framework, which also enables high-performance inference and streamlined deployment for them. We achieve 47% Model FLOPs Utilization (MFU) in our largest ERNIE 4.5 language model pre-training. Experimental results show that our models achieve state-of-the-art performance across multiple text and multimodal benchmarks, especially in instruction following, world knowledge memorization, visual understanding and multimodal reasoning. All models are publicly accessible under Apache 2.0 to support future research and development in the field. Additionally, we open source the development toolkits for ERNIE 4.5, featuring industrial-grade capabilities, resource-efficient training and inference workflows, and multi-hardware compatibility.

# ERNIEKit: ERNIE Development Toolkit Based on PaddlePaddle

**ERNIEKit** is an industrial-grade development toolkit for ERNIE 4.5. It provides training and compression capabilities, including Pre-Training, Supervised Fine-Tuning (SFT), Low-Rank Adaptation (LoRA), Direct Preference Optimization (DPO), and Quantization-Aware Training (QAT) and Post-Training Quantization (PTQ) techniques. It includes practical applications and tutorials for leveraging ERNIE models.

## Feature

-
🚀

**Industrial-grade High-Performance Pre-Training**

Optimized ERNIE 4.5 pre-training implementation featuring 3D hybrid parallelism and FP8 mixed precision acceleration. -
🪙

**Low-bit Quantization-aware Fine-tuning**

To significantly lower the barriers and costs of fine-tuning and deploying the ERNIE 4.5 model, we introduce a novel FP8 Quantization-Aware Training (QAT) methodology. This solution synergistically integrates low-precision training with optimizer offloading. Consequently, the minimum resources for fine-tuning ERNIE 4.5-300B-A47B has been substantially reduced from 96 GPUs to only 16 GPUs, while maintaining the model's original performance. Crucially, unlike prevalent FP8 mixed-precision schemes that rely on online block-wise and tile-wise quantization, the models produced by ERNIEKit's QAT solution achieve a significant advantage: they support highly efficient offline tensor-wise FP8 quantization for inference. This eliminates the computational overhead associated with dynamic quantization at inference time. -
👁️

**Visual Training & Debugging Interface**

Gradio-based WebUI for zero-code fine-tuning, alignment, and inference. -
**🔌 Multiple Hardware Support**

Support NVDIA GPU, Kunlunxin XPU and Ascend NPU Training.
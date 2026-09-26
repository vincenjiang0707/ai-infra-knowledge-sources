# [Issue #146] [Outdated][RFC] Model Optimizer - Product Roadmap

source: https://github.com/NVIDIA/Model-Optimizer/issues/146
state: closed | updated: 2026-06-23T16:00:58Z
labels: roadmap

## 正文

# Model Optimizer - Product Roadmap
[Model Optimizer's](https://github.com/NVIDIA/Model-Optimizer) goal is to provide a unified library that enables our developers to easily achieve state of the art model optimizations resulting in the best inference speed-ups. Model Optimizer will continuously enhance its existing features leveraging advanced capabilities to introduce new cutting-edge techniques and stay at the forefront of AI model optimization.

In striving for this, our roadmap and development follow these product strategies:

1. Provide a one-stop-shop for SOTA optimization methods (quantization, distillation, sparsity, pruning, speculation, etc) with easy-to-use APIs for developers to chain different methods with reproducibility.
2. Provide transparency and extensibility, making it easy for developers and researchers to innovate and contribute.
3. Provide the best easy-to-use recipes in the ecosystem through software-hardware co-design on NVIDIA platforms. Since Model-Optimizer's launch, we’ve been delivering 50% to ~5x speedup on top of existing runtime and compiler optimizations on NVIDIA GPUs with minimal impact on model accuracy ([Latest News](https://github.com/NVIDIA/Model-Optimizer?tab=readme-ov-file#latest-news)).
4. Tightly integrate into the Deep Learning inference and training ecosystem, beyond NVIDIA’s in-house stacks. Offer many-to-many optimizations by supporting popular frameworks like [vLLM](https://github.com/vllm-project/vllm), [SGLang](https://github.com/sgl-project/sglang), [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM), [TensorRT](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html#overview), [NeMo](https://github.com/NVIDIA/NeMo), and [Hugging Face](https://huggingface.co/).

In the following sections, we outline our key investment areas and upcoming features. All are subject to change and we’ll update this doc regularly. Our goal of sharing roadmaps is to increase visibility of Model-Optimizer's directions and upcoming features. 

Community contributions are highly encouraged. If you're interested in contributing to specific features, we welcome any questions and feedback in this thread and feature requests in github Issues 😊.

## Roadmap:


We'll do our best to provide visibility into our upcoming releases. Details are subject to change and this table is not comprehensive.

<img width="901" height="478" alt="Image" src="https://github.com/user-attachments/assets/d06a4bb2-7b4f-490e-82aa-0af41ecdd4fb" />


## High level goals:
### Quantization
- Optimized FP4 [Post Training Quantization (PTQ)](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/llm_ptq#post-training-quantization-ptq).
- Expand data-type availability.
- Expand advanced quantization techniques.
- Expand hosted pre-optimized checkpoints on HuggingFace.

### Training for Inference
- Optimized FP4 [Quantization Aware Training (QAT)](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/llm_qat#quantization-aware-training-qat).
- Improved Token-efficient pruning/distillation techniques.
- Improved Speculative decoding module training techniques.
- Simplified flows for Speculative Decoding Module Training/Distillation/QAT.

### ONNX/TRT
- Expanding Auto and Windows support.
- Optimized FP4 [Post Training Quantization (PTQ)](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/onnx_ptq).
- Expand advanced quantization techniques.
- Improve caching techniques.

### Platform Support & Ecosystem
- Open sourced for all developers with improved extensibility, transparency, debuggability and accessibility.
- Ready-to-deploy optimized checkpoints for both ease of use and resource limited developers.
- Expanded support for TRT-LLM, vLLM and SGLang.
- In-framework deployment for quick prototyping.
- Continuous support for new and upcoming models.

## Expanded Details:
### 1. FP4 inference on NVIDIA Blackwell
[NVIDIA Blackwell platform](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/) powers a new era of computing with FP4 AI inference capabilities. Model-Optimizer has provided initial FP4 recipes and quantization techniques and will continue to improve FP4 with advanced techniques:
1. For the majority of developers, Model-Optimizer offers **[Post Training Quantization (PTQ)](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/llm_ptq#post-training-quantization-ptq)** (weight and activation, weight-only) and our proprietary AutoQuantize for FP4 inference. [AutoQuantize](https://nvidia.github.io/Model-Optimizer/guides/_pytorch_quantization.html#optimal-partial-quantization-using-autoquantize-auto-quantize) automates per-layer quantization formats to achieve minimal model accuracy loss.
2. For developers who require lossless FP4 quantization, Model-Optimizer offers **[Quantization Aware Training (QAT)](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/llm_qat#quantization-aware-training-qat)**, which makes the neural network more resilient to quantization. Model-Optimizer QAT already works with [NVIDIA Megatron](https://github.com/NVIDIA/Megatron-LM), [NVIDIA NeMo](https://www.nvidia.com/en-us/ai-data-science/products/nemo/), native PyTorch training, and [Hugging Face Trainer](https://huggingface.co/docs/transformers/en/main_classes/trainer).

### 2. Model optimization techniques
#### 2.1 Model compression algorithms
Model-Optimizer collaborates with Nvidia and external research labs to continuously develop and integrate state-of-the-art techniques into our library for faster inference. Our recent focus areas include:
- Advanced PTQ methods (e.g., [SVDQuant](https://svdquant.mit.edu/), [QuaRot](https://arxiv.org/abs/2404.00456), [SpinQuant](https://arxiv.org/abs/2405.16406))
- QAT with distillation, a proven path for FP4 inference
- Attention sparsity (e.g., [SnapKV](https://arxiv.org/abs/2404.14469), [DuoAttention](https://arxiv.org/abs/2410.10819))
- [AutoQuantize](https://nvidia.github.io/Model-Optimizer/guides/_pytorch_quantization.html#optimal-partial-quantization-using-autoquantize-auto-quantize) improvements (e.g., support more fine-trained format selection and various weight and activation combination)
- New token-efficient pruning and distillation methods
- Infrastructure to support general rotation and smoothing

#### 2.2 Optimized techniques for LLM and VLM
Model-Optimizer works with [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM), [vLLM](https://github.com/vllm-project/vllm) and [SGLang](https://github.com/sgl-project/sglang) to streamline optimized model deployment. This includes expanding focus on model optimizations that require finetuning. To allow streamlined experience, Model-optimizer is working with (Hugging Face/ NVIDIA [NeMo](https://www.nvidia.com/en-us/ai-data-science/products/nemo/) and [Megatron-LM](https://github.com/NVIDIA/Megatron-LM)) to deliver exceptional E2E solution for these optimizations. Our focus areas include:
- (Speculation) Integrated draft model: Medusa, Redrafter, MTP and [EAGLE](https://arxiv.org/abs/2401.15077).
- (Speculation/Distillation) Standalone draft model training through pruning and knowledge distillation. 
- (Distillation) Standalone model shrinking/compressing through pruning and knowledge distillation (e.g. Llama-3.2 1/3B).
- (Quantization) Quantization aware training with support of FP8 and FP4.
- Out-of-the-box deployment with trtllm-serve, [NVIDIA NIM](https://www.nvidia.com/en-us/ai/), and vLLM serve.
- Hosting pre-optimized checkpoints for popular models such as DeepSeek-R1, Llama-3.1, Llama-3.3 and Nemotron family on [Hugging Face Model-Optimizer collection](https://huggingface.co/collections/nvidia/model-optimizer-66aa84f7966b3150262481a4).

#### 2.3 Optimized techniques for diffusers
Model-Optimizer will continue to accelerate image generation inference by investing in these areas:
- Quantization: Expand model support for INT8/FP8/FP4 PTQ and QAT. e.g., [FLUX](https://github.com/black-forest-labs/flux) model series.
- Caching: Adding more training-free and lightweight finetuning-based caching techniques with user-friendly APIs. (Previous work: [Cache Diffusion](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/diffusers/cache_diffusion)).
- Improve easy of use of the deployment pipelines, including adding multi-GPU support.

### 3. Developer Productivity
#### 3.1 Open-sourcing
To provide extensibility and transparency for everyone, Model-Optimizer is now Open Source! Paired with continued documentation/code additions to improve extensibility/usability, Model-Optimizer will continue to have a large focus on enabling our community to expand and contribute for their own use-cases. This will enable developers, for example, to experiment with custom calibration algorithms or contribute to the latest techniques. Users can also self-service to add model support or non-standard data-types, and benefit from improved debuggability and accessibility. 

#### 3.2 Ready-to-deploy optimized checkpoints
For developers who have limited GPU resources to optimize large models or prefer to skip the optimization steps, we currently offer quantized checkpoints of popular models in the [Hugging Face Model Optimizer collection](https://huggingface.co/collections/nvidia/model-optimizer-66aa84f7966b3150262481a4). Developers can deploy these optimized checkpoints directly on TensorRT-LLM, vLLM and SGLang (Depending on the checkpoint). We currently have published FP8/FP4/Medusa Llama family model checkpoints and FP4 checkpoint for DeepSeek-R1. In the near future we are working to expand to optimized FLUX, diffusion, Medusa-trained checkpoints, Eagle-trained checkpoints and more.

### 4. Choice of Deployment
#### 4.1 Popular Community Frameworks
To offer greater flexibility, we’ve been investing in supporting popular inference and serving frameworks like [vLLM](https://github.com/vllm-project/vllm) and [SGLang](https://github.com/sgl-project/sglang), in addition to having seamless integration with the NVIDIA AI software ecosystem. We currently provide an [initial workflow for vLLM deployment](https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/llm_ptq/README.md#deploy-fp8-quantized-model-using-vllm) and an example for deploying [Unified HuggingFace Checkpoint](https://nvidia.github.io/Model-Optimizer/deployment/3_unified_hf.html), with more model support planned.

#### 4.2 In-Framework Deployment
We have enabled and released a path for deployment within native PyTorch. This decouples model build/compile from runtime and offers several benefits:
1. When optimizing inference performance or exploring new model compression techniques, Model-Optimizer users can quickly prototype in the PyTorch runtime and native PyTorch APIs to evaluate performance gains. Once satisfied, they can transition to the TensorRT-LLM runtime as the final step to maximize performance.
2. For models not yet supported by TensorRT-LLM or applications that do not need ultra-fast inference speeds, users can get out-of-the-box performance improvements within native PyTorch.

Developers can utilize [AutoDeploy](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/llm_autodeploy#deploy-autoquant-models-with-autodeploy) or [Real Quantization](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/llm_qat#end-to-end-qlora-with-real-quantization) for these in-framework deployments.

### 5. Expand Support Matrix
#### 5.1 Data types
Alongside our existing [supported dtypes](https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/llm_ptq/README.md#model-support-list), we’ve recently added [MXFP4](https://arxiv.org/pdf/2310.10537) support and will soon expand to emerging popular dtypes like [FP6](https://github.com/microsoft/DeepSpeed/tree/master/blogs/deepspeed-fp6/03-05-2024) and sub-4-bit. Our focus is to further speed up GenAI inference with the least possible impact on model fidelity.

#### 5.2 Model Support
We strive to streamline our techniques to provide the shortest time from new model/feature to optimized model. This provides our community with the shortest time to deploy. We’ll continue to expand LLM/Diffusion model support, invest more in LLM with multi-modality (vision, video, audio, image generation, and action), and continuously expand our model support based on community interests.

#### 5.3 Platform & Other Support
Model-Optimizer's explicit quantization will be part of the upcoming [NVIDIA DriveOS](https://developer.nvidia.com/drive/os) releases. We recently added an e2e [BEVFormer INT8 example](https://github.com/NVIDIA/DL4AGX/tree/master/AV-Solutions) in NVIDIA DL4AGX, with more model support coming soon for Automotive customers. Model-Optimizer also has planned support for ONNX FP4 for [DRIVE Thor](https://nvidianews.nvidia.com/news/nvidia-unveils-drive-thor-centralized-car-computer-unifying-cluster-infotainment-automated-driving-and-parking-in-a-single-cost-saving-system).

In Q4 2024, Model-Optimizer added formal support for Windows (see [Model-Optimizer-Windows](https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/windows/README.md)), targeting Windows RTX PC systems with tight integration with Windows ecosystem such as [torch.onnx.export](https://pytorch.org/docs/stable/onnx.html), [HuggingFace-Optimum](https://huggingface.co/docs/optimum/en/exporters/onnx/usage_guides/export_a_model/), [GenAI](https://github.com/microsoft/onnxruntime-genai/), and [Olive](https://github.com/microsoft/Olive/). It currently supports quantization such as INT4 AWQ, INT8, FP8 and we’ll expand to more techniques suitable for Windows.


## 评论 (8)

### namgyu-youn · 2025-06-23

@omrialmog @kevalmorabia97 ; Hi, I have some questions about token-efficient pruning.

As you know, TensorRT-Model-Optimizers currently supports fusion (with NAS) pruning. And it could be categorized like the following:
- Pruning Criteria: Lp-norm (by `_estimate_importance`)
- Structured pruning after training

When we focus on pruning criteria, **sensitivity or saliency** could be options for improvement.

But because the main object is token-efficient pruning, the objective might be related to dynamic token pruning or layer-wise KV cache pruning. Could you suggest some references about this? I hope the ticket is not closed yet.

### therealnaveenkamal · 2025-09-24

Hi @kevalmorabia97 - I would like to contribute to this repo (ModelOpt sounds very interesting to me). Do you have any features or issues that I can work on?

### kevalmorabia97 · 2025-10-07

Hi @namgyu-youn can you open a separate github issue regarding your nas/pruning questions so we can discuss there in detail?

### omrialmog · 2025-10-09

Hi @therealnaveenkamal, thats awesome youre interested in contributing! 

I would suggest starting by reading our [contributing guidelines](https://github.com/NVIDIA/TensorRT-Model-Optimizer/blob/main/CONTRIBUTING.md)

One thing that could be a good start is adding support for modelopt diffusers for a popular video model quantization like https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B-Diffusers.

Its suggested you can follow https://github.com/NVIDIA/TensorRT-Model-Optimizer/tree/main/examples/diffusers and see how other models are implemented there.

If you have other areas of interest we would be happy to help best we can on your interests!

### GHGmc2 · 2025-10-21

Thanks for the great work!

May I know will pruning with NAS part (paper: [Puzzle: Distillation-Based NAS for Inference-Optimized LLMs](https://arxiv.org/abs/2411.19146)) be open sourced in the future?

### namgyu-youn · 2025-10-21

> Hi [@namgyu-youn](https://github.com/namgyu-youn) can you open a separate github issue regarding your nas/pruning questions so we can discuss there in detail?

Unfortunately not; there was no reply for 4 months, even though this issue is on the roadmap.

### Palmik · 2025-11-21

> Expand hosted pre-optimized checkpoints on HuggingFace.

Would love to see pre-optimized DeepSeek 3.2 (in nvfp4) if it's still on the roadmap.

### Trenton-Starkey · 2026-06-23

For the latest roadmap please see -  https://github.com/NVIDIA/Model-Optimizer/issues/1699 

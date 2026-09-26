# [Issue #1699] [RFC] NVIDIA Model Optimizer — Product Roadmap

source: https://github.com/NVIDIA/Model-Optimizer/issues/1699
state: open | updated: 2026-09-09T07:50:28Z
labels: roadmap

## 正文

# **[RFC] NVIDIA Model Optimizer — Product Roadmap**

[NVIDIA Model Optimizer](https://github.com/NVIDIA/Model-Optimizer) provides a unified library of SOTA model optimization techniques — quantization, sparsity, pruning, distillation, NAS, and speculative decoding — that compress deep learning models for downstream deployment frameworks.

This document outlines our investment areas and upcoming work. Details are subject to change and we'll update this roadmap regularly. We welcome questions and feedback in this thread and feature requests in GitHub Issues.

We organize upcoming work into three horizons: **Now (Q2 – Q3 2026)**, and early plans for **Next (Q4 2026)**. Specific items may shift between horizons as work progresses. 

---

## **1. Model optimization techniques**

Model Optimizer collaborates with internal teams and external research labs to continuously develop and integrate state-of-the-art techniques into the library. Active areas include advanced PTQ, QAT with distillation, attention sparsity, token-efficient pruning, NAS, and distillation, mixed-precision quantization, and emerging speculative-decoding techniques.

### **Now (Q2 – Q3 2026)**

- [ ] **PTQ Recipe Framework** — modular pipeline for post-training quantization across LLM, VLM, and diffusion/video models. YAML recipe interface with mixed-precision support; pluggable calibration; unified Hugging Face export.

  - [ ] **NVFP4 GPTQ** — production-grade GPTQ algorithm tuned for NVFP4 deployment.  
  - [ ] **NVFP4 Autoquant** — production-grade and robust autoquant recipe tuned for NVFP4 deployment  
  - [ ] **NVFP4 PTQ Recipe Book** — partner-facing guidance on recipe selection (which technique for which model class).  
  - [ ] **NVFP4 Scale for Accuracy Recovery -** umbrella of production-grade weight-scale-setting methods (Per-block MSE, 4/6, Per-Block Output Error). Closes the accuracy gap that NVFP4 PTQ alone can't recover, without requiring a training pass.  
  - [ ] **TensorRT compatibility** — ModelOpt quantization with the latest TensorRT for edge, automotive, and embedded targets. NVFP4 recipes for sub-130B and sub-10B model classes.

- [ ] **PTQ Developer Experience**

  - [ ] **Single-GPU PTQ for large MoE -** quantize trillion-scale MoE models on a single H200 or B200 via sequential per-layer calibration with offloading..  
  - [ ] **Faster, Multi-node PTQ**  — Distributed model and data parallelism leveraging FSDP2. Distributed model loading and exporting leveraging layer-wise pattern. Targets speedup over single-GPU layer-wise path.

- [ ] **QAT/QAD** and **Training-based PTQ methods** — framework, algorithms, and efficiency infrastructure for optimization techniques that use a training pass.

  - [ ] *New training-based algorithms*  
    - [ ] **Weight Scale Learning** — quantization scales become learnable parameters optimized during a light training pass, instead of being set analytically from calibration statistics. New default for QAD; recovers more accuracy than classical scale-setting on the same training budget.  
    - [ ] **(Experimental) AdaRound, DiscQuant, FlatQuant** — additional training-based PTQ algorithms.  
  - [ ] *Efficiency*  
    - [ ] **Memory-efficient QAD via offline knowledge distillation** — pre-compute teacher outputs once, then run student-only QAD; eliminates the dual-model memory cost that today blocks QAD on large models.  
    - [ ] **Hugging Face QAT/QAD efficiency** — Ulysses sequence parallelism for long-context calibration; Liger fused kernels for training throughput.  
    - [ ] **(Experimental) Per-layer training infrastructure** — sequential per-layer training without full-GPU-memory budget.  
  - [ ] *Coverage*  
    - [ ] **QAD in Megatron-Bridge** — broader model coverage for QAD recipes. Nemotron, Qwen3.6 and GPT-OSS families.

- [ ] **Speculative decoding** — recipes and examples in examples/speculative_decoding/. Coverage list maintained alongside the NVFP4 tracker.

  - [ ] **EAGLE3 & DFlash Productization** — end-to-end Synthesis → Train → Eval → Hugging Face publication workflow with reproducible recipes, so partners can train and publish their own draft models for any target LLM. 

- [ ] **dLLM (diffusion LLM) support** — NVFP4 PTQ recipes for diffusion-based language models, including hybrid precision schemes.

- [ ] **NAS and Pruning** — two complementary frameworks for compressing models via structural pruning and distillation.

  - [ ] **Puzzletron** — heterogeneous pruning across any model architecture, with M-Bridge distillation:  
    - [x] **AnyModel pruning** — Heterogeneous architecture support, M-Bridge distillation, LM-Eval integration. - Enables production grade E2E for heterogeneous model compression.   
    - [x] **Reproducible recipes** — Qwen 3.5 / 3.6 family and Nemotron-3-Nano-30B-A3B-Base-BF16.  
    - [ ] **vLLM deployment** — heterogeneous pruned models served natively.  
    - [ ] **Memory- (supported)  and throughput-constrained NAS** — budget-driven pruning; specify memory or throughput target (not just parameter count).  
    - [ ] **Simpler usage** — minimizes friction for partner adoption by introducing intelligent configuration generation, automated cost/time estimation, and multi-node compression support.   

  - [x] **Minitron** — LLM-focused parameter NAS with short distillation:  
    - [x] **M-Bridge framework** — automatic parameter-and memory based NAS for pruned candidate selection; short knowledge distillation. Supports Dense, MoE, Mamba, and Hybrid LLMs.  
    - [ ] **Reproducible recipe** — Qwen 3.5 / 3.6 family and Nemotron-3-Nano-30B-A3B-Base-BF16.  
    - [x] **VLM pruning and distillation** — extend M-Bridge to prune the language backbone of VLM architectures with image-text calibration data.

### **Next (Q4 2026)**

- [ ] **Algorithm stacking** — compose AWQ + Weight Scale Learning + GPTQ from a single YAML recipe via the PTQ Recipe Framework.  
- [ ] **Auto-quant / auto-prune pipelines** — the framework selects technique combinations automatically.  
- [ ] More TBD 

---

## **2. Framework architecture**

Model Optimizer's architecture organizes around five components, each on its own publishing track. The goal is a layered framework where contributors can add a model or technique by working in a single component, without reading the rest of the codebase.

**Optimization Lib** — model-agnostic algorithms (PTQ, QAT, QAD, pruning, distillation, AWQ, numerics).  
**Modeling Lib** — per-model modules organized like Hugging Face Transformers (models/\<model\>/\<opt_method\>.py).  
**Recipes Lib** — first-class YAML/JSON recipes per (model × technique), shipped alongside the optimized checkpoint, with a trust_remote_code-style escape hatch for customization.  
**Export Lib** — formally defined HF export format covering quantization, sparsity, and mixed precision, aligned with compressed-tensors.  
**Unified entrypoint (nv-modelopt)** — single CLI replacing example scripts. nv-modelopt --model X --recipe Y --output Z. Distributed execution via torchrun or sbatch.

### **Now (Q2 – Q3 2026)**

- [ ] **Recipes Library** — YAML recipe configs as first-class artifacts, with composable layers for algorithm, calibration dataset, numerics, and customizations.

  - [ ] LLM PTQ and SpecDec recipes covered today; existing LLM PTQ recipes converted to model-agnostic defaults.  
  - [ ] Per-(model × technique) recipes ship alongside the optimized checkpoint so partners can reproduce.  
  - [ ] Code escape hatch — trust_remote_code-style mechanism for cases YAML can't express.

- [ ] **Modeling Library** — per-model modules organized like Hugging Face Transformers; LLM dynamic modeling code reorganized into per-model folders.

  - [ ] Folder layout — modelopt/torch/models/\<model\>/\<opt_method\>.py.  
  - [ ] Unified model-loading API — single API for Hugging Face, Megatron, and independent-repo paths.  
  - [ ] Per-model contribution — model owners can add or fix their own model by working in a single folder.

- [ ] **nv-modelopt unified entrypoint** — single CLI for ModelOpt workflows, replacing the scattered example scripts.

  - [ ] Command shape — nv-modelopt --model X --recipe Y --output Z --logs path.  
  - [ ] Distributed execution — torchrun and sbatch / srun (Slurm) supported.  
  - [ ] Initial coverage — llm_ptq workflow; additional workflows land progressively (see Next).

### **Next (Q4 2026)**

- [ ] **Recipes Library — expanded technique coverage**  
  - [ ] Diffusion PTQ recipes joining the library.  
  - [ ] Sparsity, distillation, Megatron recipes joining alongside PTQ.  
  - [ ] Training-based recipes — QAT, distillation, and SpecDec recipe pipelines integrated.  
- [ ] **Modeling Library — expanded coverage**  
  - [ ] Diffusers modeling moved into the per-model layout.  
  - [ ] Independent-repo loading — models hosted outside the main repo loadable through the unified API.  
  - [ ] Non-standard models brought into the layout (custom architectures).  
- [ ] **Export Library bootstrapped**  
  - [ ] Quantization export converted to ModelOpt's dynamic-module infrastructure.  
  - [ ] LLM PTQ Export generalized as model-agnostic; model-dependent export logic relocates to the Modeling Library.  
  - [ ] Pre-quantize fusion infrastructure (model-agnostic core + per-model conversion).  
- [ ] **nv-modelopt — expanded workflow coverage**  
  - [ ] Diffusion PTQ integrated.  
  - [ ] ONNX PTQ integrated.  
  - [ ] Sparsity workflows integrated.  
  - [ ] Training-based workflows — QAT, distillation, and SpecDec integrated.  
  - [ ] Example scripts deprecate — nv-modelopt becomes the recommended path.

---

## **3. Serving and runtime integration**

Model Optimizer integrates with the major inference and training stacks so that ModelOpt-optimized checkpoints deploy without glue code.

### **Now (Q2 – Q3 2026)**

- [ ] **vLLM and SGLang upstream** — ModelOpt established as a first-class quantization backend in vLLM and SGLang, with canonical schemes aligned with compressed-tensors.

  - [ ] **Schemes supported** — NVFP4, FP8 (per-tensor, per-channel-per-token, block), INT4 AWQ, W4A8 AWQ.  
  - [ ] **Automatic scheme detection** — partners load ModelOpt-quantized checkpoints without configuring the loader.

- [ ] **KV cache quantization** — recipe definitions and PyTorch accuracy validation for KV cache quantization schemes. Runtime deployment (memory layout, kernels) lives in vLLM, SGLang, and TRT-LLM.

  - [ ] **Skip-Last-N** — preserve the last N tokens unquantized to maintain recency precision; recipe schema + accuracy validation.  
  - [ ] **Mixed-precision (FP8 K + NVFP4 V)** — different formats for K and V; recipe schema + calibration for static FP8 K scales.  
  - [ ] **Pure NVFP4 KV** — accuracy validation reference; runtime owns dynamic per-block scale computation.

### **Next (Q4 2026)**

- [ ] **Hugging Face Transformers v5.0 (universal serving path)** — modelopt → export → Transformers v5.0 serving, opening a third deployment path alongside vLLM and SGLang.

  - [ ] **Server features** — paged attention, in-flight batching, MoE fusion.  
  - [ ] **Broad model coverage** — supports the full Transformers model surface, including architectures not yet in vLLM / SGLang / TRT-LLM.  
  - [ ] **Evaluation + further training** — viable for evaluation and additional QAT/QAD on published FP4 checkpoints.

- [ ] **vLLM / SGLang sparsity and SpecDec loading** — 2:4 weight sparsity, sparse attention, and SpecDec checkpoints load natively with full recipe metadata; no partner glue code required.

- [ ] **NVIDIA-NeMo/Megatron-Bridge** — ModelOpt embedded in NeMo training and release pipelines.

- [ ] **NeMo-RL integration** — quantization-aware distillation (QAD) integrated into the NeMo-RL post-training loop, so RL-trained models retain accuracy when quantized to NVFP4. Removes the post-hoc PTQ accuracy gap that today's RL-fine-tuned models incur on deployment.



---

## **4. Beyond LLM — diffusion, AR+diffusion, video, image, world model, multimodal, Auto-VLA**

### **Now (Q2 – Q3 2026)**

- [ ] **Video/Image/World Model optimization** — quantization, sparsity, and distillation recipes in ModelOpt for video diffusion models.

  - [ ] **NVFP4 and FP8 quantization** — recipes for video diffusion models.  
  - [ ] **2:4 weight and activation sparsity** — for Wan2.2 and LTX2 reference architectures.  
  - [ ] **VSA + sparse kernels** — Video Sparse Attention and sparse kernel APIs integrated in ModelOpt; end-to-end sparse inference demonstrated on LTX2.  
  - [ ] **FastGen × ModelOpt** ([NVlabs/FastGen](https://github.com/NVlabs/FastGen)) — step-distillation algorithms integrated.

- [ ] **VLM PTQ** — recipes and workflow supported for VLM families; pluggable image-text calibration.

- [ ] **VLA PTQ** - recipes and workflow to quantize Auto models ([Alpamayo](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/alpamayo))

### **Next (Q4 2026)**

- [ ] **Video/Image/World Model — expanded recipes** 

  - [ ] **Unified distillation trainer** — shared training infrastructure with NeMo AutoModel.  
  - [ ] **SageAttention** quantized attention (QK + PV to FP8/FP4).  
  - [ ] **NVFP4 3D-CNN for VAE** —  quantize the temporal-spatial 3D convolutions in the video diffusion VAE to NVFP4 (Wan2.2 and LTX2)  
  - [ ] **Sparse-attention recipes** — calibration-driven for video diffusion deployment.".

- [ ] **VLM — expanded recipes**

  - [ ] **VLM QAT/QAD** — recipes for production VLM family deployment.  
  - [ ] **VLM Puzzletron pruning** — extends M-Bridge pruning to vision-language architectures.  
  - [ ] **Multimodal routing** — embedding cache + multimodal routing benchmarks; approximate routing for cache-warm workers.

- [ ] **VLA** - expanded recipes

  - [ ] **VLA QAT/QAD** — recipes for production VLM family deployment.

  - [ ] [Experimental] VLA pruning / distillation

---

## **5. Agentic optimization workflows**

Reusable agent skills that triage pipeline failures, onboard new models, and run PTQ → deployment → evaluation autonomously.

### **Now (Q2 – Q3 2026)**

- [ ] **Agent PTQ skill** — decision-tree routing, remote execution, Slurm / Docker support, unlisted-model handling.

- [ ] **Agent Eval skill** — auto-detection of quantization + benchmark recommendations.

- [ ] **Agent Deployment skill** — vLLM / SGLang / TRT-LLM OpenAI-compatible endpoint generation.

### **Next (Q4 2026)**

- [ ] **Deployment debug loop** — automated triage based on observed failures.

- [ ] **End-to-end agentic workflow documentation** with CI guide and cross-skill references.

- [ ] **ModelOpt launcher** — standalone CLI for multi-step optimization pipelines, decoupled from the full NeMo stack.

  - [ ] **Standalone installation** — no NeMo dependency required.  
  - [ ] **nemo-run backed** — uses NeMo Run as the execution engine.  
  - [ ] **Execution modes** — local Docker for single-machine, Slurm for multi-machine multi-step pipelines.

---

*Questions, comments, and feature requests welcome in this thread. Specific items are tracked as separate GitHub issues with the roadmap label.*  


## 评论 (4)

### Sai-Murali-Marisetty · 2026-06-16

The VLA PTQ gap in Section 4 is something I'd like to take on.

Background: I led BEVFormer inference optimization at Qualcomm — reduced latency from 450ms → 48ms via custom CUDA kernels, operator fusion, and INT8 PTQ on Snapdragon 8 Gen 2/3 edge SoCs. I also contributed quantization techniques to AIMET and shipped flagship models to Qualcomm AI Hub, so I'm familiar with the per-channel calibration and bias correction challenges that tend to break accuracy in vision transformer backbones.

My plan for the Alpamayo PTQ recipe:
- Calibration using the PhysicalAI-AV dataset (driving scenes, multi-sensor)
- NVFP4 + INT8 PTQ following the Recipes Library YAML format from Section 2
- Accuracy benchmarks (mAP delta) + latency on a single GPU, with a notebook showing the end-to-end flow
- Validate in AlpaSim closed-loop to confirm no behavioral regression post-quantization

Before I open a draft PR, a couple of alignment questions:
1. Is there a preferred calibration sequence length / number of scenes for VLA models, or should I follow the LLM PTQ defaults?
2. Any constraints on the YAML recipe schema I should match — specifically for models with interleaved vision and action heads?

Happy to start with a draft PR this week if this direction looks right to the team.

### rohansjoshi · 2026-06-23

> The VLA PTQ gap in Section 4 is something I'd like to take on.
> 
> Background: I led BEVFormer inference optimization at Qualcomm — reduced latency from 450ms → 48ms via custom CUDA kernels, operator fusion, and INT8 PTQ on Snapdragon 8 Gen 2/3 edge SoCs. I also contributed quantization techniques to AIMET and shipped flagship models to Qualcomm AI Hub, so I'm familiar with the per-channel calibration and bias correction challenges that tend to break accuracy in vision transformer backbones.
> 
> My plan for the Alpamayo PTQ recipe:
> 
> * Calibration using the PhysicalAI-AV dataset (driving scenes, multi-sensor)
> * NVFP4 + INT8 PTQ following the Recipes Library YAML format from Section 2
> * Accuracy benchmarks (mAP delta) + latency on a single GPU, with a notebook showing the end-to-end flow
> * Validate in AlpaSim closed-loop to confirm no behavioral regression post-quantization
> 
> Before I open a draft PR, a couple of alignment questions:
> 
> 1. Is there a preferred calibration sequence length / number of scenes for VLA models, or should I follow the LLM PTQ defaults?
> 2. Any constraints on the YAML recipe schema I should match — specifically for models with interleaved vision and action heads?
> 
> Happy to start with a draft PR this week if this direction looks right to the team.

I've added an example with Alpamayo quantization already [here](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/alpamayo) with NVFP4, FP8, and mixed precision recipes, which have been validated with minADE open-loop evaluation. Could you say why you're targeting NVFP4 + INT8 instead of FP8? Also, can you explain what mAP delta is?

### baonudesifeizhai · 2026-06-29

NVFP4 Autoquant — production-grade and robust autoquant recipe tuned for NVFP4 deployment  we currently try to use that in vllm-omni side autoquanting cosmos3 nano    see (https://huggingface.co/feizhai123/Cosmos3-Nano-ModelOpt-AutoQuant-E5.0-P32-S12-Fixed)  
emm really improved  accuracy and video  quailty compare to standard nvfp4   
see here https://github.com/vllm-project/vllm/pull/45735  currently for nvfp4 have latency problem and also mixed have graph break...
so could you move forward that autoquants and nvfp4 quantization method in vllm?  really appreciate   

### Edwardf0t1 · 2026-07-01

@kevalmorabia97 @Trenton-Starkey Could we pin this RFC issue to the top in our Issues?

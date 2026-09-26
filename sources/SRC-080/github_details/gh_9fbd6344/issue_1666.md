# [Issue #1666] Does Model Optimizer support QAT for GLM-5 with FP8, INT4, and NVFP4 quantization?

source: https://github.com/NVIDIA/Model-Optimizer/issues/1666
state: open | updated: 2026-08-02T22:08:40Z
labels: question

## 正文

## How would you like to use ModelOpt

<!-- Description of what you would like to do with ModelOpt. -->
I would like to perform **Quantization-Aware Training (QAT)** on the GLM-5 model (744B parameters, MoE architecture) using Model-Optimizer, targeting the following low‑precision formats:
- FP8
- INT4 (full QAT, both weights and activations)
- NVFP4

Specifically, I want to verify official support and obtain any available examples or configuration templates for GLM-5 QAT with these precisions.




## System information
CUDA version: 13
GPU: Blackwell



## 评论 (6)

### LinearPro · 2026-07-13

I also want to know!

### ChenhanYu · 2026-07-14

QAT/D support for none-Nemotron models will be coming to Megatron-Bridge (with ModelOpt fakequant and logits distillation). The first support targets NVFP4 (where FP8 should also work) on Qwen3.6 and GPT-OSS. Details can be found in https://github.com/NVIDIA-NeMo/Megatron-Bridge/issues/4512

Megatron-Bridge has GLM-5 support. It maybe our next recipe support target if there is no OSS contribution by then. 

### kevalmorabia97 · 2026-07-14

In terms of software support, PTQ and QAD for LLMs in Megatron-Bridge framework is already supported but we have not published any reproducible recipes yet. You can refer to the documentation here if you want to give it a try: https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/megatron_bridge/

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: ceba67181cbb936614eea71339e5023eebce2fdba21b4ade4798130b84a69269

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 28d6e689583c60532582793a81393d68be3c0d4845202200ebbca8cd5f0574d2

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 88250778b65e6c92675145ef9196dabacc469af0fc4eed923013e63e0ecbb3d1

Release follow-up: this open ModelOpt issue needs release relevance confirmed. Link its planned fix/validation, or confirm it is not a v0.46.0 blocker.

# [Issue #2624] Q2 2026 Roadmap 

source: https://github.com/vllm-project/llm-compressor/issues/2624
state: closed | updated: 2026-07-13T18:39:43Z
labels: enhancement, RFC, keep-open, ROADMAP

## 正文

# Q2 Roadmap

## Lifecycle Refactoring + SmoothQuant, AWQ, and RTN Distributed Support
Finishing off this round of performance updates (initially supported through LLM Compressor v0.10) by adding DDP support to the QuantizationModifier / RTN, SmoothQuant and AWQ. Part of this includes refactoring the quantization lifecycle, including how / when observers are called. 


### Status: Completed
- [x] https://github.com/vllm-project/llm-compressor/pull/2585
- [x] https://github.com/vllm-project/llm-compressor/pull/2671
- [x] https://github.com/vllm-project/llm-compressor/pull/2457
- [x] https://github.com/vllm-project/llm-compressor/pull/2557
- [x] https://github.com/vllm-project/llm-compressor/pull/2785

## Transformers v5 Support  
Although LLM Compressor has started to added support for some features in transformers v5, this has been on a model specific basis (i.e to support Qwen3.5, Gemma 4). Widespread updates are still required to fully support transformers >=v5

### Status: Completed
- [x] Support for updated MoE Calibration: https://github.com/vllm-project/llm-compressor/issues/2036

Related PRs:
1. https://github.com/vllm-project/llm-compressor/pull/2647

## FP4 + Rotations vLLM Support and Validation (QutLass)
### Status: In progress
- [ ] vLLM Support for NVFP4 + micro-rotations: https://github.com/vllm-project/llm-compressor/issues/2006. Support for this already exists in vLLM but needs to be connected to the compressed-tensors integration

## Benchmarking NVFP4 across modifiers
### Status: In Progress
With all the support landed to support NVFP4 generally across LLM Compressor as well as support for FP4 with rotations in vLLM, benchmarking is required to establish the preferred pathway for model quantization. This includes benchmarking MoE and non-MoE models across the following cases:
- [ ] RTN with and without rotations
- [ ] GPTQ with and without rotations
- [ ] AWQ (with rotations as well?)
- [ ] AutoRound 

Related PRs: 
- [x] https://github.com/vllm-project/llm-compressor/pull/2526

## Custom definition support for oneshot

Currently, if a model does not have a definition in transformers, the only algorithms that are supported in LLM Compressor for this type of model are data-free pathways using the `model_free_ptq`.  Algorithms requiring data through oneshot are not supported (such as GPTQ or any activation-quantization scheme requiring calibration data). 

A PoC was established for this through [DeepSeek v3.2 where a custom definition](https://github.com/vllm-project/llm-compressor/tree/main/src/llmcompressor/modeling/deepseekv32) was added in order to support [NVFP4](https://github.com/vllm-project/llm-compressor/blob/main/examples/disk_offloading/deepseek_v32_example.py)
quantized variants of this model. We want to continue hardening this pathway, to ensure all models can be supported through LLM Compressor.

- [ ] Pytorch custom definition handling
- [ ] Observer support in vLLM?

## MXFP4 vLLM Integration / Validation
### Status: Completed
- [x] MXFP4 Support - Activation Quantization Validation for Non MoE models (move examples out of the experimental folder)
PR: https://github.com/vllm-project/vllm/pull/41664

## Humming Kernels
### Status: In Progress 
- [x] Packing support for non-4bit/8bit support in compressed-tensors 
   - https://github.com/vllm-project/compressed-tensors/pull/732
- [ ] vLLM Integration 
   - https://github.com/vllm-project/vllm/pull/46389
   - https://github.com/vllm-project/vllm/pull/46390

## REAP Support
### Status: Completed
- [x] https://github.com/vllm-project/llm-compressor/pull/2864

##  Potential Research Initiatives:

Potenital research areas to be explored as part of Q2.

- [ ] HIGGS: https://github.com/vllm-project/llm-compressor/issues/2690
- [ ] R3 rotations in vLLM
- [ ] WUSH Transforms
- [ ] iMatrix Ablations
- [ ] KVZap: https://arxiv.org/abs/2601.07891

## CI/CD Buildkite Migration
### Status: Completed
- [x] Migrate Compressed-Tensors CI/CD to Buildkite 
- [x] Migrate LLM Compressor CI/CD to Buildkite 

## Model Support
- [x] Kimi-K2.6
    - https://huggingface.co/RedHatAI/Kimi-K2.6-FP8-BLOCK
    - https://huggingface.co/RedHatAI/Kimi-K2.6-NVFP4
- [x] Qwen 3.6
   - [RedHatAI/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/RedHatAI/Qwen3.6-35B-A3B-NVFP4)
   - [RedHatAI/Qwen3.6-35B-A3B-FP8-dynamic](https://huggingface.co/RedHatAI/Qwen3.6-35B-A3B-FP8-dynamic)
- [x]  Gemma 4
   - [RedHatAI/gemma-4-31B-it-NVFP4](https://huggingface.co/RedHatAI/gemma-4-31B-it-NVFP4)
   - [RedHatAI/gemma-4-31B-it-FP8-block](https://huggingface.co/RedHatAI/gemma-4-31B-it-FP8-block)
   - [RedHatAI/gemma-4-31B-it-FP8-Dynamic](https://huggingface.co/RedHatAI/gemma-4-31B-it-FP8-Dynamic)
   - [RedHatAI/gemma-4-26B-A4B-it-NVFP4](https://huggingface.co/RedHatAI/gemma-4-26B-A4B-it-NVFP4)
[RedHatAI/gemma-4-26B-A4B-it-FP8-Dynamic](https://huggingface.co/RedHatAI/gemma-4-26B-A4B-it-FP8-Dynamic)
- [x] DeepSeek V4
   -  https://huggingface.co/RedHatAI/DeepSeek-V4-Flash-NVFP4-FP8
- [x] DiffusionGemma
    - [diffusiongemma-26B-A4B-it-NVFP4](https://huggingface.co/RedHatAI/diffusiongemma-26B-A4B-it-NVFP4)
    - [diffusiongemma-26B-A4B-it-FP8-dynamic](https://huggingface.co/RedHatAI/diffusiongemma-26B-A4B-it-FP8-dynamic)
-  [x] Nemotron 3 Ultra Quantized Checkpoints
    - [Nemotron-3-Ultra-550B-A55B-FP8-Dynamic](https://huggingface.co/RedHatAI/NVIDIA-Nemotron-3-Ultra-550B-A55B-FP8-Dynamic)
    - [Nemotron-3-Ultra-550B-A55B-BF16-FP8-BLOCK](https://huggingface.co/RedHatAI/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16-FP8-BLOCK)
    - [Nemotron-3-Ultra-550B-A55B-BF16-W4A16-G128](https://huggingface.co/RedHatAI/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16-W4A16-G128)

## 评论 (0)

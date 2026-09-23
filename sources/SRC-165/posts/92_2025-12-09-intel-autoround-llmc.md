# 2025-12-09-intel-autoround-llmc

source: https://vllm.ai/blog/2025-12-09-intel-autoround-llmc

# Advancing Low‑Bit Quantization for LLMs: AutoRound x LLM Compressor

**Achieve faster, more efficient LLM serving without sacrificing accuracy!**

## TL;DR

We’re excited to announce that ** AutoRound**—Intel’s state‑of‑the‑art tuning‑based post‑training quantization (PTQ) algorithm—is now integrated into

**. This collaboration delivers:**

[LLM Compressor](https://github.com/vllm-project/llm-compressor)- Higher accuracy for low bit-width quantization
- Lightweight tuning (hundreds of steps, not thousands)
- Zero additional inference overhead
- Seamless compatibility with
`compressed-tensors`

and direct serving in[vLLM](https://github.com/vllm-project/vllm) - Streamlined workflow: quantize and serve models with just a few lines of code

Broader quantization schemes and model coverage are coming next—try it now and help shape what we build.

## What Is AutoRound?

**AutoRound** is an advanced post-training quantization (PTQ) algorithm designed for Large Language Models (LLMs) and Vision-Language Models (VLMs). It introduces three trainable parameters per quantized tensor: `V`

(rounding offset/adjustment), `α`

and `β`

(learned clipping range controls). By processing decoder layers sequentially and applying signed gradient descent, AutoRound jointly optimizes rounding and clipping to minimize block‑wise output reconstruction error.

Core strengths:

**Superior accuracy**, especially at very low bit‑widths**Support multiple data types:**W4A16, MXFP8, MXFP4, FP8, NVFP4, with more on the way**Mixed‑bit**, layer‑wise precision search for flexible accuracy–efficiency trade‑offs- Applicability across both
**LLMs**and**VLMs**

AutoRound enables quantized models in a range of low‑bit formats that are designed to accelerate inference on **Intel® Xeon® processors**, **Intel® Gaudi® AI accelerators**, **Intel® Data Center GPUs**, **Intel® Arc™ B‑Series Graphics**, as well as other GPUs (e.g., CUDA‑based devices).

Looking forward, Intel is adding native support for FP8, MXFP8, and MXFP4 formats to its next-generation **Data Center GPUs, codenamed Crescent Island**. Models quantized with AutoRound will naturally scale to take advantage of these data types across the Intel AI hardware portfolio. This creates a consistent path from algorithmic innovation to real‑world deployment.

For more details, please refer to the paper [AutoRound (EMNLP 2024)](https://aclanthology.org/2024.findings-emnlp.662.pdf) and the GitHub repository [intel/auto-round](https://github.com/intel/auto-round).

## Why Integrate Into LLM Compressor?

**LLM** **Compressor** already provides a unified, modular system for compression primitives such as quantization and pruning. Integrating AutoRound into this ecosystem:

- Aligns with the existing modifier architecture (e.g.,
`GPTQModifier`

) - Reuses the sequential calibration and layer‑onloading infrastructure
- Enables future interoperability with richer multi‑modifier recipes
- Produces quantized models that are ready for vLLM serving, enabling a clean workflow from compression to deployment

## Integration Overview

We completed the first stage of integration by introducing the new `AutoRoundModifier`

into LLM Compressor, enabling production of `W{n}A16`

(e.g., W4A16) compressed models that seamlessly load in vLLM, as implemented in [PR #1994](https://github.com/vllm-project/llm-compressor/pull/1994). With a straightforward configuration—just specify your model and calibration data—you can quickly generate high‑quality low‑bit checkpoints. This initial stage supports quantizing a range of dense LLMs, including the **Llama** and **Qwen** model families, and demonstrates robust compatibility for practical deployment.

## Try It Now (Quickstart)

### 1. Install

### 2. Load Model & Tokenizer

### 3. Prepare Calibration Data

### 4. Run Quantization using AutoRound

The AutoRound quantization can run on a variety of devices, including CPUs and GPUs. Quantization and serving may not happen on the same device. For example, you can quantize on a workstation with GPU and later deploy on AIPC.

In practice, **128 calibration samples + ~200 iterations** often reach stable convergence. Increase the number of samples or iterations if you are targeting extremely low bits or tighter accuracy targets.

### 5. Serve in vLLM

Once quantization is complete, the same compressed model can be served on different hardware, independent of the device used for tuning. For example, you can serve the quantized Qwen3‑8B‑W4A16‑G128‑AutoRound model on a single **Intel® Arc™ Pro B60 GPU**:

Note: Please install vLLM from PR [#29484](https://github.com/vllm-project/vllm/pull/29484/). When serving on XPU, you must run vLLM with the `--enforce-eager`

flag.

### 6. Evaluate (Example: GSM8K with `lm_eval`

)

Note: The results may fluctuate due to non-determinism.

## Conclusion & Future Plans

With this first integration, AutoRound and LLM Compressor already provide a practical, production‑oriented path to low‑bit LLMs: W4A16 quantization is supported end‑to‑end, the workflow is simple to configure, and dense models such as Llama and Qwen are supported. The setup is robust, streamlined, and ready for practical deployment.

Looking ahead, we plan to extend support to additional schemes such as FP8, MXFP4, MXFP8, and NVFP4, add automatic mixed‑bit search for fine‑grained per‑layer optimization, and cover more model families, including Mixture‑of‑Experts (MoE) models. We also aim to deepen interoperability with other algorithms in LLM Compressor, which will allow AutoRound to combined into richer multi‑modifier recipes that serve both community use cases and Intel production workloads.

If you’d like to influence which formats, models, and workflows we prioritize next, please join the discussion in [RFC #1968](https://github.com/vllm-project/llm-compressor/issues/1968) and share your benchmarks or deployment requirements, or bring your feedback to the Intel Community so we can align the roadmap with real‑world needs.

### Acknowledgements

We wish to acknowledge the LLM Compressor and vLLM community. Specifically, we thank Kyle Sayers, Dipika Sikka, Brian Dellabetta, Charles Hernandez, Robert Shaw and Kunshang Ji for their invaluable feedback on the early proposal and their diligent review of the pull requests.

#### Related RFCs and PRs

[llm-compressor#1968](https://github.com/vllm-project/llm-compressor/issues/1968), [llm-compressor#1994](https://github.com/vllm-project/llm-compressor/pull/1994), [llm-compressor#2055](https://github.com/vllm-project/llm-compressor/pull/2055), [llm-compressor#2062](https://github.com/vllm-project/llm-compressor/pull/2062), [auto-round#993](https://github.com/intel/auto-round/pull/993), [auto-round#1053](https://github.com/intel/auto-round/pull/1053), [auto-round#1055](https://github.com/intel/auto-round/pull/1055), [auto-round#1072](https://github.com/intel/auto-round/pull/1072),
[vllm#29484](https://github.com/vllm-project/vllm/pull/29484).

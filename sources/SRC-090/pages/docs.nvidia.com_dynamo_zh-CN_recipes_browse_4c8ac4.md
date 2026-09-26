source: https://docs.nvidia.com/dynamo/zh-CN/recipes/browse
lastmod: 2026-09-24T19:58:16.636Z

SGLang recipes for agentic traffic on B200, GB200, or H200, with FP8 KV caching, prefix caching, and speculative decoding.

SGLang 1x H200 · 1x B200 · 1x GB200 Agentic · MTP

Open recipe K-EXAONE 2.0 LG AI Research

750B-A37B MoE in NVFP4 on B200, aggregated or disaggregated 1P1D, with MTP speculative decoding and KV-aware routing on an 8K/1K chat trace.

vLLM 4x/8x B200 Chat trace replay

Open recipe Gemma-4-31B Google / NVIDIA

Aggregated TensorRT-LLM recipes for long-context agentic traffic on B200, GB200, or H200, with KV-aware routing and CPU KV-cache offload.

TensorRT-LLM 8x B200/GB200/H200 Agentic + multimodal

Open recipe DeepSeek-V4.1-Flash DeepSeek

SGLang recipes on GB200, aggregated with KV-aware routing and DSpark speculation, or 1P1D disaggregated with Mooncake KV transfer over the NVLink fabric.

SGLang 8x GB200 Day-0 · up to 1M context

Open recipe vLLM recipes for agentic traffic on GB200 or H200, aggregated or 1P1D disaggregated with KV-aware routing, NIXL KV transfer, and H200 MTP7.

vLLM 8x/16x H200 · 4x/8x GB200 Agentic · up to 1M context

Open recipe B200 chat profiles with NVFP4 weights, FP8 KV cache, EAGLE3, and KV-aware routing. Choose two aggregate workers or two prefill workers and one decode worker.

vLLM 8x / 12x B200 Chat

Open recipe Kimi-K3 recipes for vLLM on H200, GB200, and GB300, plus SGLang on GB200 and GB300.

SGLang · vLLM H200 · GB200 · GB300 Day-0

Open recipe vLLM and SGLang recipes for chat and agentic traffic on GB300 or GB200, aggregated or disaggregated, with KV-aware routing, MTP speculation, and FP8 weights/KV over MNNVL.

vLLM + SGLang 16x GB200 · 16x GB300 Chat + agentic · 262K context

Open recipe SGLang recipes for long-context agentic traffic on B200 (NVFP4) or H200 (FP8), aggregated or disaggregated, with KV-aware routing, EAGLE MTP speculation, and HiCache CPU offload.

SGLang 8x/16x H200 · 4x/12x B200 Agentic · up to 500K context

Open recipe Inkling NVFP4 Thinking Machines

Thinking Machines’ first open-weights model — a multimodal MoE with controllable reasoning effort. vLLM GB300 targets serve agentic traffic at 1M context with MTP speculation and KV-aware routing, aggregated or disaggregated; the Day-0 SGLang B200 target adds image and audio input.

SGLang · vLLM 8x GB300 / 8x B200 Agentic · 1M context Text + image + audio

Open recipe Kimi-K2.6 Moonshot / NVIDIA

Multi-target vLLM matrix covering B200 and H200 for chat and agentic traffic, with Eagle3 MLA speculation and KV-aware routing.

vLLM 4x B200 / 8x H200 Chat + agentic

Open recipe Nemotron 3.5 Lightning NVIDIA

30B hybrid Mamba/Attention/MoE recipe matrix for H100, H200, B200, and GB200, with NVFP4 and BF16 variants, vLLM MTP/DFlash/DSpark targets, DSpark with KV-routing, and experimental TensorRT-LLM MTP/no-spec.

vLLM + TRT-LLM 1-4x GPU Agentic · 1M context

Open recipe Aggregated vLLM targets for B200 and H200 chat and agentic traffic with MTP speculative decoding and trace-backed benchmarks.

vLLM 4x B200 / 8x H200 Chat + agentic

Open recipe NVFP4 and FP8 vLLM targets for B200 and H200 chat and agentic traffic with MTP speculative decoding and KV-aware routing.

vLLM 4x B200 / 4x H200 Chat + agentic

Open recipe 20x GB200 SGLang P/D recipe for 1K input / 8K output traffic with EAGLE speculative decoding, plus an AWS EFA variant.

SGLang 20x GB200 Long output / static ISL-OSL

Open recipe DeepSeek-V4-Pro NVIDIA checkpoint / DeepSeek

vLLM agentic recipe — MoE 1.6T / 49B active, B200 (NVFP4, 1M ctx) and H200 (FP8), aggregated or disaggregated with MTP-2 and KV-aware routing.

vLLM 8–32x B200/H200 Agentic

Open recipe DeepSeek-V4-Pro-0813 DeepSeek

vLLM agentic recipe — MoE 1.6T, MXFP4 experts + FP8 KV, GB200 and H200, aggregated or disaggregated with KV-aware routing. Full 1M context with no CPU KV offload.

vLLM 8–16x GB200/H200 Agentic 1M ctx

Open recipe DeepSeek-V4-Flash NVIDIA checkpoint / DeepSeek

vLLM agentic recipe — MoE 284B / 13B active, B200 (NVFP4) and H200 (FP8), aggregated or disaggregated (2P1D / 4P3D) with KV-aware routing.

vLLM 4–28x B200/H200 Agentic

Open recipe TensorRT-LLM GB200 targets for static traffic plus vLLM B200/H200 agentic targets (agg + disagg) with KV-aware routing and EAGLE3 speculative decoding.

TRT-LLM + vLLM H200 · B200 · GB200 Static + agentic

Open recipe Disaggregated vLLM serving with KV-aware routing on 16x H200, for multi-turn conversational traffic with prefix reuse.

vLLM 16x H200 Multi-turn conversation Related benchmark

Open recipe vLLM recipes for long-context agentic traffic on B200 NVFP4 and H200 FP8, aggregated or disaggregated 1P2D, with KV-aware routing and MTP speculation on H200 aggregated.

vLLM 2-4x B200/H200 Agentic trace replay

Open recipe 16-GPU TensorRT-LLM recipe matrix for Hopper/Blackwell and aggregate/P-D serving.

TRT-LLM 16x H100/H200 Static ISL-OSL

Open recipe FP8 recipe set spanning TensorRT-LLM aggregate, TensorRT-LLM P/D, and vLLM P/D targets.

TRT-LLM 2-8x GPU Static ISL-OSL

Open recipe No recipes match the selected filters.
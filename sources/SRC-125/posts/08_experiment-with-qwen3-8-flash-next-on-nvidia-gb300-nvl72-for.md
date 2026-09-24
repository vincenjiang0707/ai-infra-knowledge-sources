# experiment-with-qwen3-8-flash-next-on-nvidia-gb300-nvl72-for-agentic-coding

source: https://developer.nvidia.com/blog/experiment-with-qwen3-8-flash-next-on-nvidia-gb300-nvl72-for-agentic-coding/

Alibaba released the model weights for Qwen3.8-Flash-Next as a preview of the upcoming Qwen4 architecture for developers to experiment with and evaluate. It’s a multimodal mixture-of-experts (MoE) model with a 125B-parameter main model supplemented by an additional 51B N-gram embeddings, with 6B parameters activated per token. It has a native 262,144-token context window, extensible to 1M tokens with YaRN.

NVIDIA provides best-effort Day 0 functional support through SGLang, vLLM, and NVIDIA TensorRT LLM, validation across NVIDIA GB300 NVL72 for inference, and post-training recipes from NVIDIA NeMo AutoModel and NVIDIA NeMo RL.

## Architectural innovations for long-context inference

Qwen3.8-Flash-Next is designed for high-volume, context-intensive applications such as agentic coding, document processing, and tool-driven workflows. As context grows, attention compute and KV cache memory become bottlenecks. The model addresses both with a hybrid architecture combining Gated DeltaNet (GDN) and Qwen Sparse Attention (QSA). Three out of every four layers use GDN to continuously compress historical context into a fixed-size recurrent state, eliminating KV cache growth as sequences lengthen. The remaining layer uses QSA for precise retrieval across the full context.

Previous sparse-attention approaches rely on token-level indexers that become increasingly computationally expensive as context length grows. QSA aggregates the sequence into micro-blocks, estimates their importance at the block level, and selects only the most relevant regions. This cuts attention, compute, and indexing overhead within each layer, making the design well-suited to architectures alternating between GDN and QSA layers.

Alibaba’s [published benchmarks](https://qwen.ai/blog?id=qwen3.8-flash-next) suggest that QSA can improve the efficiency of 1M-token workloads. Compared with full attention, its attention kernel delivered speedups of up to 7.6x during prefill and 4.9x during decoding. In a cache-heavy online serving test at a 1M-token context length and with a 90% prefix-cache hit rate, Qwen3.8-Flash-Next achieved 8.6x the prefill throughput of Qwen3.7-Plus.

## Running Qwen3.8-Flash-Next on NVIDIA GB300 NVL72

The GB300 NVL72 features a rack-scale architecture that integrates 72 NVIDIA Blackwell Ultra GPUs into a single platform. Its large, 72-GPU NVIDIA NVLink domain enables efficient all-to-all communication at 130 TB/s, eliminating bottlenecks that appear when expert traffic must cross traditional off-the-shelf networks. Running on NVIDIA GB300 NVL72 delivers over** **16K tokens per second per GPU** and over 200 tokens per second per user, **enabling developers to experiment with agentic coding applications at high throughput and low latency.

Beyond rack-scale deployment, Qwen3.8-Flash-Next also runs on local NVIDIA hardware, including NVIDIA DGX Station, NVIDIA DGX Spark clusters, and workstations with four NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition GPUs. Developers can prototype and evaluate agentic coding workflows on local hardware and scale the same model to GB300 NVL72 for production serving.

## Post-train Qwen3.8-Flash-Next and serve it with your preferred inference engine

Developers can fine-tune the model for domain-specific use cases using [NVIDIA NeMo AutoModel](https://github.com/NVIDIA-NeMo/Automodel/tree/main/docs/model-coverage/llm/qwen/qwen3-8-flash-next.mdx), a PyTorch-native fine-tuning library with Day-0 Hugging Face checkpoint support. Train directly on existing checkpoints without model conversion, with support for full SFT or memory-efficient LoRA fine-tuning. Users can go a step to perform reinforcement learning using NVIDIA [NeMo RL recipes](https://github.com/NVIDIA-NeMo/RL/blob/qwen3-8-flash-next-support/docs/guides/models/qwen/qwen3-8-flash-next.md).

NVIDIA supports multiple inference stacks to meet a variety of developer needs. [SGLang](https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next), [vLLM](https://recipes.vllm.ai/Qwen/Qwen3.8-Flash-Next), and [TokenSpeed](https://lightseek.org/tokenspeed/recipes/models#qwen3-8-flash-next) provide open-source inference recipes for developers requiring greater control over performance on the NVIDIA-accelerated platform.

## Get started with Qwen3.8-Flash-Next

Try the model directly from [QwenCloud.](https://www.qwencloud.com/models/qwen3.8-flash?spm=a2ty_o06.30285417.0.0.1d73c921wJU38r&file=qwen3.8-flash)

Download the model weights from [Hugging Face](https://huggingface.co/nvidia/Qwen3.8-Flash-Next-NVFP4) or [ModelScope](https://modelscope.cn/models/Qwen/Qwen3.8-Flash-Next) and [deploy](https://docs.nvidia.com/nim/vision-language-models/2.1.1/get-started/advanced/get-started-qwen3.8-flash-next.html) with a [model-free NVIDIA NIM](https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/vllm-model-free-nim/-) from NVIDIA NGC.

## Start the discussion at forums.developer.nvidia.com

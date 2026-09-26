# [Issue #2125] Removal of "1 The ATOM engine is promising, however it has yet to serve production tokens. It is still in its infant stage."

source: https://github.com/SemiAnalysisAI/InferenceX/issues/2125
state: open | updated: 2026-07-09T09:09:45Z
labels: 

## 正文

Hi, SA team!

ATOM framework has been successfully deployed on commercial service. And can you plz remove this in the 
https://inferencex.semianalysis.com/inference

<img width="1036" height="269" alt="Image" src="https://github.com/user-attachments/assets/384bf7ee-1c20-4ab2-86ab-a449ffbc7f33" />

=

https://4d1c06dd.isolation.zscaler.com/profile/da20bab3-7555-450b-99cd-53b17d97b595/zia-session/?controls_id=f3135616-bddc-4ff9-aade-39e700e5bf52&region=cle&tenant=fe557fcecd6e&user=16ecc6bc0797c33dc85ff02c86c1553c87cd85b514a37125be12db087215a315&original_url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FxwpTZCQcDfgIEDnGWHxkVQ&key=sh-1&hmac=a2a0f9fb29ed52ebf1a5cec1d7a4b3f2ec8800ef5ac308e85577e5e7dd71f184

= traslation

Alibaba Mama × AMD: Practical Qwen Model Inference Optimization Based on SGLang-ATOM

To address the complex and diverse LLM application scenarios in Alibaba Mama’s advertising business, the Alibaba Mama AI Infra inference team collaborated with AMD to deploy Qwen3.5/3.6 series models on AMD Instinct GPUs using the SGLang-ATOM Plugin Mode solution. Through clear division of responsibilities, both teams advanced performance and engineering efficiency in parallel. Test results show that the inference performance of Qwen3.5 series models on MI308X is better than or on par with comparable competing products, effectively meeting the advertising business’s core requirements for low latency and high throughput.

Background

Alibaba Mama’s advertising-related businesses cover a wide range of LLM scenarios, including agents, image-text review, and offline data generation. These workloads extensively use Qwen3.5/Qwen3.6 models of different sizes, especially Qwen3.6-35B-A3B and Qwen3.5-397B-A17B.

For service objectives, online and nearline businesses must maximize throughput while satisfying strict latency constraints, while offline businesses prioritize maximum throughput.

Input and output sizes vary significantly across scenarios. Input lengths range from hundreds of tokens to hundreds of thousands of tokens, while output lengths range from dozens to thousands of tokens. Some scenarios also include multimodal inputs such as images.

These business characteristics require the inference system to address three types of challenges simultaneously: multi-model and multi-business requests, performance, and engineering delivery efficiency.

On the model side, Qwen3.5 covers Dense, MoE, multimodal, and other architectures. Some models reach hundreds of billions of parameters, placing high demands on weight loading, quantization, attention, MoE, and memory management. On the request side, agents, multi-turn conversations, and long context significantly increase prefill overhead. KV cache hit rate, request allocation, and mixed long/short request scheduling directly affect end-to-end latency. On the engineering side, advertising workloads iterate quickly, and online/nearline systems require high stability. Therefore, we wanted to reuse the existing SGLang serving system as much as possible, rather than rewriting the entire business framework for a specific hardware platform.

Therefore, the solution we needed was neither a single-point kernel optimization nor a complete replacement of the existing serving stack, but a combination of two types of capabilities:

Alibaba continues to build and optimize business-required capabilities around the SGLang framework, including request scheduling, batching, prefix/KV cache, long context, multimodal encoding/decoding, online/offline mixed deployment, observability, and stability. In addition, Alibaba Mama’s open-source inference performance simulator InferSim is used to analyze theoretical performance across different business scenarios, identify performance bottlenecks, and define performance targets.

AMD focuses on ATOM modeling inference implementation, providing a ROCm-native optimized, lightweight framework capability that is responsible only for the model execution path. This includes Qwen model architecture adaptation, weight loading, FP8/PTPC quantization, attention, MoE, kernel fusion, and ROCm backend optimization.

The two sides are connected through SGLang plugin mode, allowing the business side to retain the SGLang user experience while enabling the model side to use an execution path better aligned with AMD Instinct GPUs.

Solution: SGLang-ATOM Plugin Mode

ATOM is a lightweight ROCm-native inference execution engine introduced by AMD for AMD Instinct GPUs. Its goal is to provide a direct path to peak performance for modern LLM inference workloads. It focuses on the model execution layer rather than rebuilding a full serving framework. Through optimizations such as AITER-native kernels, MoE dispatch, MLA attention, and kernel fusion, it can rapidly support new model architectures and feed these optimizations back into open-source ecosystems such as vLLM and SGLang through plugins. This helps AMD GPUs achieve higher performance and faster deployment in complex reasoning, RAG, multi-step agentic, and MoE-heavy workloads.

Figure 1. AMD ATOM architecture

In our practice, the positioning of SGLang-ATOM is very clear: SGLang is the business-side serving framework, while ATOM is a ROCm-native optimized, lightweight framework responsible only for modeling inference implementation. With this design, the business system still uses SGLang’s startup method, OpenAI-compatible API, scheduling, and request-processing logic.

Within SGLang, we continue to build framework-side capabilities required by advertising workloads, such as request admission, batch construction, cache reuse, long-context request management, multimodal input processing, online/offline task isolation, worker allocation, and observability metrics. Underlying model construction, weight loading, attention, MoE, quantization, and kernel dispatch are taken over by ATOM and further mapped to ROCm components such as AITER, MORI, and RCCL.

For engineering integration, the solution uses SGLang’s out-of-tree external model package mechanism:

export SGLANG_EXTERNAL_MODEL_PACKAGE=atom.plugin.sglang.models
python3 -m sglang.launch_server --model-path <model_path> ...

The advantage of this approach is that we can continue evolving based on upstream SGLang without maintaining a long-term fork, and without requiring the advertising business to adapt to a new serving API. SGLang’s model registration process loads atom.plugin.sglang.models. When a request hits a model architecture supported by ATOM, SGLang selects the wrapper provided by ATOM. The wrapper then builds the ATOM model stack through prepare_model(..., engine="sglang") and uses load_model_in_plugin_mode to handle weight loading, parallel sharding, quantized weight mapping, and fused checkpoint layout.

This plugin path already covers models such as Qwen3.5 and Qwen3-Next. For our advertising business, the most important point is that Qwen3.5 Dense/MoE variants can run as first-class external models inside upstream SGLang, while the language tower is built and executed by ATOM. Qwen3.5-397B-A17B, Qwen3.5-35B-A3B, Qwen3.5-27B, and their corresponding FP8 versions can all use this mode. For Qwen3-Next, ATOM also encapsulates GDN/linear-attention-related paths, allowing these models to run in the SGLang forward batch context.

From a system boundary perspective, the division of responsibilities is clear:

Alibaba is responsible for various functional and performance optimizations of the SGLang framework itself, including service entry, request lifecycle, batching, prefix/KV cache, multimodal request processing, long-context strategies, online/offline mixed workload governance, and business observability. In addition, Alibaba Mama’s open-source inference performance simulator InferSim is used to analyze theoretical performance under different business scenarios, locate performance issues, and establish performance targets.

AMD is responsible for the ATOM modeling side, including Qwen model architecture adaptation, weight loading, FP8/PTPC quantization mapping, attention backend, MoE computation, kernel fusion, and ROCm kernel selection.

This division allows “business framework optimization” and “model execution optimization” to proceed in parallel. Alibaba can continue optimizing request allocation, cache hit rate, online/offline mixed deployment, and capacity strategy around advertising scenarios. AMD/ATOM can continue evolving model-specific modeling, kernels, quantization, and communication paths. Only by combining the two can the best performance be achieved in real production scenarios.

Qwen3.5-35B-A3B-FP8 TP1 and Qwen3.5-397B-A17B-FP8 TP4 on MI308X show better or comparable performance under different context lengths compared with competing GPUs of the same class.

Figure 2. Alibaba Mama internal performance test data: performance of Qwen3.5-35B-A3B-FP8 TP1 and Qwen3.5-397B-A17B-FP8 TP4 on MI308X

Technical Optimization Details
1. Multimodal Performance Optimization for Qwen3.5 Models

In advertising review, content understanding, and multimodal agent scenarios, Qwen3.5 series models natively support multimodal capabilities. They can process text, images, and other inputs in a unified request and perform cross-modal understanding and generation.

Compared with pure-text models, Qwen3.5’s multimodal path adds multiple stages to the inference pipeline, including multimodal data format adaptation, preprocessing, cross-modal alignment, ViT encoder execution, visual patch embedding, and cross-modal feature fusion. These stages lengthen the single-request pipeline and make multimodal data coordination and feature adaptation important components of end-to-end latency.

Figure 3. Qwen3.5 multimodal request processing, ViT encoding, and LLM backbone execution flow in SGLang

From actual performance bottlenecks, the additional overhead of Qwen3.5 multimodal inference mainly comes from three paths: host-side multimodal preprocessing, multimodal data transfer, and GPU-side ViT encoder computation.

Traditional host-side JPEG decoding and tensor conversion are expensive. Decoding a single 720p image takes about 27 ms, and latency increases rapidly in multi-image or video-frame scenarios. To address this bottleneck, we integrated rocJPEG into the SGLang Tokenizer image decoder path, offloading JPEG decoding to the GPU through the torchvision backend. Decoding a single 720p image can be reduced to about 4 ms, achieving roughly 7× acceleration and reducing multimodal request preprocessing latency at the source.

Figure 4. rocJPEG offloads JPEG decoding to the GPU, reducing host-side image decoding and tensor conversion overhead

The second bottleneck is multimodal data transfer between the Tokenizer and Scheduler. In SGLang, the Tokenizer and Scheduler usually run in different processes, so preprocessed multimodal data must be passed to the Scheduler through IPC. Traditional CPU-based gloo:broadcast is inefficient for large multimodal data blocks and can introduce additional host overhead.

The ROCm backend supports CUDA IPC, allowing data to be transferred directly through GPU-to-GPU communication, avoiding CPU staging and repeated CPU/GPU copies. At the same time, steps such as image hashing are offloaded to the GPU, further reducing host-side burden.

Figure 5. Profile timeline of broadcast, image data hashing, ViT, LLM prefill, and decode stages in multimodal requests

Figure 6. Tokenizer and Scheduler share multimodal data in HBM through CUDA IPC, reducing CPU transfer overhead

The third bottleneck is the ViT encoder. After high-resolution images are processed through patch-based tokenization, the number of visual tokens increases rapidly with resolution, and full self-attention has O(N²) complexity. For example, a 960×1280 image generates about 4,800 visual tokens, corresponding to more than 23 million attention interactions. In multi-image, high-resolution, or long-video scenarios, the number of visual tokens can grow further, causing memory pressure, high latency, and low GPU utilization.

To mitigate this issue, data parallelism can be applied to the ViT module, splitting multi-image inputs across multiple GPUs for parallel processing and reducing per-GPU computation pressure. In tests with five 960×1280 images per request, ViT DP improved performance by about 3%–4%, and the benefit increases as the number of images and video frames grows.

After combining these optimizations, the multimodal pipeline no longer depends only on the decode performance of the language model itself. Instead, latency is reduced across the full path, from image decoding and inter-process transfer to visual encoding and service-side scheduling. By combining framework-side serving capabilities with the ROCm-native execution path on the modeling side, image-text review, content quality evaluation, and multimodal agents can move from “deployable” to “able to meet production latency and cost requirements.”

2. GDN Optimization

Figure 7. Overall structure and block design of Gated DeltaNet

The Qwen3.5 series introduces GDN, or Gated Delta Networks, which creates new adaptation requirements for the inference framework’s prefill and decode paths. The prefill stage needs to handle chunk attention over long sequences, while the decode stage needs to frequently update recurrent state.

For online and nearline advertising scenarios, the fixed overhead of each decode step accumulates continuously, directly affecting TPOT and end-to-end latency. For long-context or batched requests, the prefill path affects overall throughput before the first token.

In the prefill stage, ATOM adds a fused chunk fast path for GDN chunk attention. This path targets long-sequence prefill scenarios on AMD GPUs. By fusing some originally separate computation steps, it reduces kernel launches and intermediate tensor reads/writes. If shape or hardware conditions are not met, the original general implementation remains available as a fallback to ensure functional coverage and stability.

In the decode stage, ATOM adds a dedicated fast path for GDN recurrent attention. This path targets common non-speculative decode requests. It merges previously separate gating computation and recurrent state update into a single execution path, reducing intermediate result writeback and extra kernel scheduling overhead. For complex layouts, prefill, speculative decode, and other scenarios, the system automatically falls back to the original general implementation.

Considering online service stability, the decode fast path is enabled through an environment-variable switch and retains a complete fallback path. Idle or padding slots are explicitly handled to prevent invalid positions from affecting subsequent computation.

Because this path is a lossy fast kernel, it may theoretically introduce bf16-level numerical differences in recurrent state. Therefore, it was not treated as a lossless optimization directly, but validated through end-to-end tasks. In actual GSM8K testing, accuracy was basically on par with the original implementation, with no stable accuracy degradation observed. Normal variation appeared across different runs, and some results were even slightly higher than the original version.

In addition to GDN recurrent update, the Qwen3.5 decode hot path also includes MRoPE Q/K processing overhead. ATOM further adds a fused MRoPE Q/K Triton path. When model shape and runtime conditions are satisfied, the fused implementation is enabled; otherwise, it automatically falls back to the general rotary embedding path. The implementation also considers dynamic-shape scenarios, reducing repeated compilation overhead under different decode batch sizes.

After combining these optimizations, in Qwen3.5-35B-A3B-FP8 on MI308X under a long-output decode stress test, GDN decode fast path and fused MRoPE Q/K increased total token throughput from about 7,467 tok/s to about 8,004 tok/s, an improvement of about 7.2%. Mean end-to-end latency decreased by about 6.5%. Mean TPOT decreased from about 77.4 ms to about 71.9 ms, a reduction of about 7.2%.

For the GDN prefill fused chunk path, Qwen3.5-35B-A3B-FP8 input token throughput improved by about 3.4%. For MoE models such as Qwen3.5-397B-A17B-FP8, prefill-related optimizations brought about a 4.2% throughput improvement. All these optimizations retain fallback paths, making it easier to gradually enable them across different model forms, hardware conditions, and request patterns.

3. Optimized KV Cache Layout and Integration of High-Performance AITER Operators

In the Attention module, ATOM integrates high-performance MHA and PagedAttention operators provided by the AMD AITER Library, and customizes a specialized KV Cache layout for the AMD CDNA architecture.

Compared with the standard KV Cache layout:

[num_blocks, num_kv_heads, head_dim, block_size]

the optimized layout better matches the memory access pattern of PagedAttention on AMD GPUs:

k_cache: [num_blocks, num_kv_heads, head_dim // x, block_size, x]
v_cache: [num_blocks, num_kv_heads, block_size // X, head_dim, X]

This layout better aligns KV cache memory access with the AMD CDNA architecture, significantly improving PagedAttention memory access efficiency. During the decode stage, the system no longer needs additional device-to-device layout conversion, eliminating redundant D2D copy and related scheduling overhead.

Figure 8. KV Cache layout distribution

For business scenarios such as Qwen3.5 with long context and high-concurrency requests, KV cache memory access efficiency during decode directly affects TPOT and tail latency. With the specialized KV Cache layout, decode throughput can improve by about 15%–20%, while overall inference latency is reduced.

4. Using Different Parallelization Strategies for Different Business Scenarios

For parallelization strategy, different business scenarios use different deployment methods.

For online and nearline services, TTFT and tail latency are the primary constraints. Therefore, a large TP configuration within a single machine is more suitable. It shards a single model instance across more GPUs, reducing model-side latency for single-request prefill and decode.

For throughput-first scenarios such as offline data generation, a multi-DP and smaller-TP configuration within a single machine is more suitable. This runs more parallel replicas on the same node and improves overall token throughput and resource utilization through higher batch size and concurrency.

Summary

From the perspective of Alibaba Mama’s advertising business, the core value of SGLang-ATOM is not simply replacing one LLM inference engine with another. Instead, it combines two categories of capabilities.

The first category is Alibaba’s experience in scheduling, allocation, cache, batching, multimodal processing, long context, and serving within the SGLang framework, as well as performance analysis using Alibaba Mama’s open-source inference performance simulator InferSim.

The second category is AMD’s optimization capability in Qwen model modeling, FP8/PTPC quantization, attention, MoE, kernel fusion, multimodal data paths, and ROCm communication.

Only by combining these two can complex production workloads achieve latency, throughput, stability, and delivery speed at the same time.

The advantages of SGLang-ATOM plugin mode are also reflected in engineering deployment. It preserves the usage pattern of upstream SGLang and integrates ATOM through SGLANG_EXTERNAL_MODEL_PACKAGE. It does not require maintaining a long-term fork, nor does it require business teams to learn a new serving stack.

For teams already using SGLang, this means lower migration cost and nearly zero learning cost. For teams that need to quickly validate AMD Instinct GPUs, it means shorter time-to-market.

More importantly, this path is ROCm-native. ATOM, AITER, MORI, RCCL, and AMD Instinct GPUs form a complete optimization loop. This supports current major models such as Qwen3.5/Qwen3.6 and can continue evolving with Qwen-Next, multimodal models, and longer-context models.

For advertising workloads with high concurrency, multiple scenarios, and strict SLAs, SGLang-ATOM provides a practical path: Alibaba continues to optimize SGLang framework capabilities, AMD continues to optimize ATOM modeling implementation, the business framework avoids major changes, model optimization continues to deepen, and hardware capability is released quickly.

About Us

The Alibaba Mama Engineering Platform AI Infra team is committed to building a production-grade AI Infra platform for search and advertising scenarios, as well as GenAI / AI Agent applications based on LLMs and AIGC.

The team serves the core businesses of Taotian e-commerce and is responsible for building and optimizing training and inference platforms for ultra-large-scale embedding representation learning, Sparse-Dense models, and dense large models.

In areas such as high-performance online serving and training platforms, distributed systems, heterogeneous computing, and AI compiler optimization, the team has solid engineering practice and advanced technical expertise, and continues to explore industry-leading technical solutions and deployment capabilities.

The team has openings for campus recruitment and internships. You are welcome to join.

Contact email: [ys472446@taobao.com](mailto:ys472446@taobao.com); [yunlong.xyl@taobao.com](mailto:yunlong.xyl@taobao.com)

The AMD AI Framework FDE team provides a practical model continuous-optimization path based on the SGLang-ATOM Plugin technical solution. The team is committed to helping customers bring products to market quickly with low migration cost and zero learning barrier, while continuously supporting future model evolution and performance improvement.

You can obtain a full introduction to this technical system and discuss in-depth technical requirements through ATOM.

END

You May Also Like

KDD’26 | From Scaling to Structured Representation: Reconstruction and Validation of Transformer Architectures in CTR Models

ECCV 2026 | Seven Selected Papers from Taotian Group: From Generative Models to 4D Space Construction, Exploring New Frontiers in Visual Generation

Alibaba Mama & Tsinghua Propose a New Generative Bidding Algorithm, AIGB-Pearl | ICLR 2026 Oral

ICML’26 | Taotian Group Open-Sources the First E-Commerce Short Video Understanding Benchmark E-VAds and RL-Enhanced Reasoning Model

ICML’26 | HiDe: Rethinking the High-Resolution Zoom-in Mechanism of Multimodal Large Models

Follow “Alibaba Mama Technology” to learn more.

## 评论 (0)

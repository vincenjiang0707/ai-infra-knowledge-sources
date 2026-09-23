source: https://docs.ray.io/en/latest/serve/llm/user-guides/index.html
lastmod: 

# User guides[#](https://docs.ray.io#user-guides)

How-to guides for deploying, scaling, and operating Ray Serve LLM. If you are new, start with the [Quickstart](https://docs.ray.io/quick-start.html), then come back here to go deeper.

## Configure and deploy[#](https://docs.ray.io#configure-and-deploy)

[Configuration reference](https://docs.ray.io/configuration.html): every`LLMConfig`

field, from model loading and engine kwargs to accelerators, placement, and deployment options.[Deployment initialization](https://docs.ray.io/deployment-initialization.html): speed up model loading and replica startup with caching, streaming load formats, and initialization callbacks.[Multi-LoRA deployment](https://docs.ray.io/multi-lora.html): serve many LoRA adapters on a shared base model with runtime switching and an LRU cache.

## Scale across GPUs and nodes[#](https://docs.ray.io#scale-across-gpus-and-nodes)

[Cross-node parallelism](https://docs.ray.io/cross-node-parallelism.html): distribute a model across GPUs and nodes with tensor and pipeline parallelism and placement groups.[Data parallel attention](https://docs.ray.io/data-parallel-attention.html): replicate the model into coordinated data-parallel groups to raise throughput, especially for MoE models.[Fractional GPU serving](https://docs.ray.io/fractional-gpu.html): pack multiple small-model replicas onto a single GPU.

## Optimize latency and throughput[#](https://docs.ray.io#optimize-latency-and-throughput)

[Prefill/decode disaggregation](https://docs.ray.io/prefill-decode.html): split prompt processing and token generation onto separate replicas to tune each independently.[KV cache offloading](https://docs.ray.io/kv-cache-offloading.html): extend KV cache capacity with LMCache and tiered storage backends.[Prefix-aware routing](https://docs.ray.io/prefix-aware-routing.html): route requests to replicas that already hold a matching prefix to maximize cache hits.[Direct streaming](https://docs.ray.io/direct-streaming.html): bypass the ingress when streaming tokens to cut per-token latency.

## Choose an engine[#](https://docs.ray.io#choose-an-engine)

[vLLM compatibility](https://docs.ray.io/vllm-compatibility.html): use vLLM features such as embeddings, structured outputs, vision, and reasoning through Ray Serve LLM.[Custom vLLM models](https://docs.ray.io/custom-vllm.html): serve an out-of-tree architecture with a vLLM plugin, using a Qwen3 reward model as the example.[SGLang integration](https://docs.ray.io/sglang.html): run SGLang as the inference engine instead of vLLM.

## Operate in production[#](https://docs.ray.io#operate-in-production)

[Observability and monitoring](https://docs.ray.io/observability.html): engine and request metrics, Grafana dashboards, and Prometheus integration.
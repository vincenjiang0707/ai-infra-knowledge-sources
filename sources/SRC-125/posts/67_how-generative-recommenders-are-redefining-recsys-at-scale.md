# how-generative-recommenders-are-redefining-recsys-at-scale

source: https://developer.nvidia.com/blog/how-generative-recommenders-are-redefining-recsys-at-scale/

Recommender systems (RecSys) are one of the most ubiquitous machine learning problems in the consumer internet industry yet notoriously difficult to train and serve at scale. The advent of LLMs has inspired a shift from the traditional embedding-similarity-based objective to a generative one, where the goal is to predict the next action or item in a large catalog given a sequence of user histories.

This post covers the architectural shift toward generative recommenders (GRs), the production challenges it introduces, and how the NVIDIA `recsys-examples`

and `nv-embedding-cache`

address them.

## Why traditional RecSys breaks at scale

### Data type and volume

User histories, the primary RecSys data type, represent a record of how users interact with items in a catalog. Unlike modalities such as text or images, user histories involve a mix of categorical and continuous features that change frequently over time. At industry scale, this data can get to the order of terabytes or petabytes every day. Even on the most high-end hardware accelerators, data of this size will be unable to fit GPU high-bandwidth memory (HBM), introducing many bottlenecks during training and inference.

### Sparsity and the long-tail problem

The long-tail problem in recommender systems describes the phenomenon where a small number of popular items in a catalog get the majority of the interaction. This issue arises because the catalog of items can far exceed the number of users, leading to very sparse user-item interaction data. Because the probability distribution of interacting with an item is heavily skewed towards how popular that item is, training data provides little signal to a vast majority of niche items that represent ground truth for user preferences.

### Cold start problem

As new users or items join a RecSys platform, there is no interaction history to immediately produce a quality embedding. Rather, it has to be deduced from a smaller set of features, which can negatively impact the trajectory of recommendations. This can be partially resolved by correlating with similar items and semantic descriptions, but there is a risk that initial recommendations are poor and degrade user experience.

### Strict latency requirements

In production, RecSys models are often served online to millions of users under strict service-level agreements (SLAs), where small increases in latency can impact user experience. Unlike LLM workloads that may tolerate autoregressive decoding latency, RecSys models must frequently retrieve and rank thousands of candidate items in a few milliseconds.

## Generative recommenders

Unlike traditional embedding-based recommenders that model user-item preference with geometric similarity, GRs reframe recommendation as a sequence modelling problem similar to LLMs.

The objective is to model the probability distribution of next action or item conditioned on a sequence of user history:

The shift toward more homogeneous, transformer-like architectures can better leverage scaling laws, potentially unify retrieval and ranking within a single model, and more naturally integrate with the rapidly evolving LLM ecosystem.

The two prevalent approaches that implement this objective in recommenders are Hierarchical Sequential Transduction Units (HSTU) and Semantic IDs:

### HSTU

HSTU, introduced by Meta in 2024, is a foundational GR model architecture that reframes RecSys under the generative objective and introduces key innovations to enable efficient training and serving at production scale.

HSTU represents input data as a per-user sequence of interleaved items and actions (like, click, etc.) ordered by timestamp. It also removes the dependence on explicit feature engineering, a common practice in traditional RecSys models, in favor of learned sequential representations from attention over user-item interactions. This formulation makes user histories analogous to next token prediction in LLMs, where in training you can get a meaningful learning signal both within a sequence and across batches.

Unlike standard Transformer attention, HSTU modifies the attention aggregation mechanism by replacing softmax normalization with SiLU-based weighting, incorporating relative attention bias, and applying elementwise gating before output projection. These modifications preserve stronger magnitude information across long sequences while enabling more efficient kernel fusion and lower-latency inference.

### Semantic IDs

Modeling next item prediction over a large corpus of items with a sparse set of user-item interactions can introduce many challenges: bottlenecks from full softmax calculation, weak training signal from long tail items, and poor generalization to semantically similar items.

Semantic IDs (SIDs), introduced by Google, alleviate these issues by producing a smaller set of new vocabulary tokens based on hierarchical clustering of item embeddings. Architectures such as TIGER, PLUM, OneRec v1/v2, and many modern GR architectures use Semantic IDs as the foundation for scalable autoregressive recommendation.

Unlike traditional RecSys, autoregressive decoding of Semantic IDs directly generates recommendations instead of searching within an embedding space, and naturally provides a ranking via output logits. This allows search methodologies like beam search to produce multiple Semantic IDs in a single forward pass, improving throughput and allowing niche items in a cluster to be chosen.

`recsys-examples`

repository

The [recsys-examples](https://github.com/NVIDIA/recsys-examples/tree/main) repository is a collection of examples to demonstrate the best practice for training and deploying generative recommenders on NVIDIA GPUs using PyTorch. It includes optimized implementations of HSTU and semantic ID models, covering both training and inference workflows. The repository also consolidates three modular components: DynamicEmb for embedding layers, a KV cache and storage manager tailored for recommender systems, and efficient CUDA ops for HSTU and semantic ID beam search decoding.

### Dynamic embedding

Traditional embedding tables in RecSys assume a fixed, static vocabulary. However, in production, new users and items appear continuously, and the long-tail of the item catalog grows much faster than any single GPU’s HBM can keep up with. Over-provisioning a static table wastes memory on rows that will never be touched, while under-provisioning causes expensive copies that can degrade model performance and quality.

DynamicEmb replaces static tables with a GPU-optimized scored hash table that maps arbitrary feature IDs to embedding rows on demand. Rows are allocated only for IDs the model actually sees, and the table lives across HBM and pinned host memory so it can grow well beyond a single GPU’s capacity. The implementation builds on the algorithms from the [HierarchicalKV](https://arxiv.org/pdf/2603.17168) hash-table design. The combination of admission control and score-based eviction allows capacity to be spent on IDs that matter to model training, and makes the long-tail problem tractable at scale.

It is provided as a TorchRec backend, with tables sharded row-wise across ranks using the `EmbeddingBagCollection`

and `EmbeddingCollection`

APIs. Fused CUDA kernels handle lookup and gradient reduction for `SUM`

, `MEAN`

, and sequence pooling modes. Prefetching techniques keep frequently accessed embeddings resident in HBM for efficient access.

### HSTU support

Recsys-examples provides a production-style training and inference stack for HSTU. Item, user, action, and contextual embedding tables are managed through TorchRec, with DynamicEmb providing dynamic capacity and caching for the high-cardinality tables. For dense layers, the HSTU backbone uses Megatron-Core so a single training run can leverage data, tensor, sequence, and pipeline parallelism. The library is designed to be modular across the entire stack so that components can be plug and play with custom architectures.

During training, `TorchRec/DynamicEmb`

and `Megatron-Core`

are seamlessly integrated to coordinate sharding and parallelism across both embedding and dense modules. The training pipeline incorporates dynamic shuffling to balance workloads across ranks, overlaps embedding communication and prefetching with dense computation, and includes a HSTU layer with fused ops and FBGEMM attention kernels optimized for NVIDIA Ampere, Hopper, and Blackwell GPUs. Together, these optimizations improve end-to-end Model FLOP Utilization (MFU) to 31.40% from 7.65% on two DGX H100 nodes, demonstrating substantial [gains in training](https://github.com/NVIDIA/recsys-examples/blob/main/examples/hstu/training/benchmark/E2E_BENCHMARK.md) efficiency.

For inference, `recsys-examples`

is designed to meet strict low-latency requirements by supporting PyTorch AOTInductor to execute the model in the Torch C++ runtime while remaining compatible with NVIDIA Triton Inference Server.

Frequently accessed embeddings are kept close to the GPU using `nv-embedding-cache`

, and computation is further reduced through a customized `FlexKV`

-enabled KV cache that distributes cache entries across multiple memory tiers.

When deployed with Triton Inference Server, inference with the Pytorch AOTI backend & no KV cache delivers a 1.14x ~ 1.28x speedup over the Python backend, and inference with the Pytorch AOTI backend with KV cache delivers a 2.20x ~ 2.38x speedup in an ideal all GPU cache-hit scenario.

### Semantic ID-GR

Semantic ID-based GR introduces a serving pattern that is very different from chat-based LLM inference: long user context, short autoregressive decoding, and large beam widths over constrained item-token spaces. In practical Semantic ID workloads, a request may contain thousands of historical tokens, decode only 2–3 Semantic ID tokens, and use beam widths such as 128 or 256 to improve recommendation diversity.

Existing LLM serving systems such as vLLM, SGLang, and TensorRT LLM are primarily optimized for multi-user chat-style serving with paged KV cache, dynamic batching, and long decoding. They are powerful general frameworks, but do not naturally expose the core abstractions needed by Semantic ID-GR: shared request-level context KV, short per-beam decode KV, beam-path tracking, dynamic beam width, and item-constrained generation.

To address this, `recsys-examples`

provides a GR-specialized inference framework [example](https://github.com/NVIDIA/recsys-examples/tree/main/examples/sid-gr-inference) for Qwen based Semantic ID models. The framework separates KV cache to isolate beam dependent and independent components: long shared context into `ContextKV`

, short decode history into `BeamKV`

, and logical beam ancestry into `BeamPath`

. This avoids treating every beam as a separate long sequence. The runtime also includes GR-native continuous batching, direct pool-view CUDA graph replay, item-constrained `topK`

, and a dedicated `gr-decode_atten`

backend that operates directly on the GR KV layout.

On a single NVIDIA H100 80GB GPU with Qwen3-1.7B, context lengths of 1,000 and 5,000 tokens, beam width of 256, and 3 output tokens, the GR-specialized path consistently outperforms the SGLang beam-search in the measured offline and online benchmarks.

| Metric | Workload | GR Result | Baseline | Improvement |
|---|---|---|---|---|
| Offline latency | ctx=1000, batch=4, beam=256, output=3 | 47.736 ms | 102.318 ms | 2.14x faster |
| Offline latency | ctx=5000, batch=4, beam=256, output=3 | 154.224 ms | 349.857 ms | 2.27x faster |
| Offline latency | ctx=5000, batch=8, beam=256, output=3 | 307.917 ms | 685.354 ms | 2.23x faster |
| Online serving throughput | ctx=5000, concurrency=4, beam=256, output=3 | ~19.7 req/s | ~10.7 req/s | ~1.85x higher |
| Online median latency | ctx=5000, concurrency=4, beam=256, output=3 | ~198 ms | ~370 ms | ~46% lower |
| Offline correctness | ctx=1000/5000, batch=1/2/4/8, beam=256 | Top1 exact 1.000 | SGLang comparison | TopK overlap mean 0.960 |

*Table 2. Serving results for recsys-examples Semantic ID-GR inference framework*

This makes Semantic ID-GR serving a natural complement to the HSTU and embedding components in recsys-examples: HSTU and `DynamicEmb`

address production-scale training and embedding-heavy inference, while the Semantic ID-GR inference path targets autoregressive Semantic ID generation with long context, large beam search, and strict recommender-system latency requirements.

`nv-embedding-cache`



(NVE) is an SDK for accelerating large-scale embedding table lookups and operations in recommender inference. It provides modular components including optimized kernels, software cache primitives, and PyTorch-compatible bindings, enabling low-latency access to embedding tables that exceed the capacity of a single GPU’s HBM.[nv-embedding-cache](https://github.com/NVIDIA/nv-embedding-cache)

Production recommender embedding tables routinely exceed the capacity of a single GPU’s HBM, forcing inference systems to stage embeddings across multiple memory tiers. Furthermore, recommenders often exhibit access patterns that are very favorable to caching.

NVE manages this through a hierarchical lookup flow, composed of GPU cache in HBM as the hot tier, CPU cache in DRAM as the warm tier, and a remote parameter store (typically Redis or RocksDB-backed). Hot keys promotion into the GPU cache is customizable, and a lockless invalidate-and-commit protocol lets lookups and cache modifications run concurrently on the GPU without stalling the lookup stream. Sharding across devices is handled via CUDA virtual memory, so a single logical table can span multiple GPUs or nodes.

NVE provides `NVEmbedding`

and `NVEmbeddingBag`

as drop-in replacements for `torch.nn.Embedding`

and `torch.nn.EmbeddingBag`

for easy integration with the PyTorch ecosystem. The modules expose familiar arguments while adding cache specific configuration flags. Because the layers behave like standard `nn.Module`

components, they can be integrated into existing recommender models with minimal graph changes. For deployment, NVE registers its lookup operators against the LibTorch Stable ABI, providing `AOTInductor`

support in the C++ runtime.

Recsys-examples DynamicEmb tables are supported in NVE, allowing an easy transition between training and inference. On DLRM v3, the MLPerf generative recommender benchmark based on HSTU, recsys-examples and NVE were able to achieve [99,997 queries/sec](https://developer.nvidia.com/blog/nvidia-platform-delivers-lowest-token-cost-enabled-by-extreme-co-design/) inference throughput in an online server scenario. An example of how to perform inference with these two libraries can be found [here](https://github.com/NVIDIA/recsys-examples/tree/main/examples/hstu/inference).

## Get started

Check out the following repositories for quick-start guides and more details:

## Start the discussion at forums.developer.nvidia.com

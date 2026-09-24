# co-designing-ai-model-attention-for-fast-interactive-long-context-inference

source: https://developer.nvidia.com/blog/co-designing-ai-model-attention-for-fast-interactive-long-context-inference/

As agentic and long-context workloads become common, the context lengths increase and attention consumes a larger share of inference time (Figure 1). Because attention now dominates that cost, how it is designed—not just how it is implemented—increasingly determines a model’s inference performance. Shaping model architecture around how GPUs execute it is the premise of AI model co-design. For a discussion of how model design choices impact both throughput and interactivity without sacrificing accuracy, see the previous post, [AI Model Co-Design: Hardware-Friendly LLM Design](https://developer.nvidia.com/blog/ai-model-co-design-hardware-friendly-llm-design/).

This post examines how group size (query heads per KV head), head dimension, and sequence length shape the performance of dense attention, where every query attends to all keys and values along the sequence length. We distill that analysis, together with how attention is parallelized across GPUs, into four practical guidelines: a co-design checklist that helps model developers raise inference throughput and interactivity on NVIDIA GPUs. Stay tuned for a post covering sparse attention.

Every analysis is grounded in two sources: analytical formulas from GEMM-shape arithmetic, and measured data from prefill and decode kernels with FP8 for both attention compute and the KV cache.

Abbreviation | Definition |
| PB | Prefill batch size |
| DB | Decode batch size |
| QH | Number of query heads |
| KH | Number of KV heads (KH = QH for MHA, KH = QH/G for GQA, KH = 1 for MQA) |
| Group size = QH/KH (query heads sharing one KV head) | |
| Hsz | Head dimension (typically 64, 128, or 256) |
| ISL | Input sequence length (query tokens in prefill) |
| KVSL | Average KV cache sequence length in a decode iteration |

*Table 1. Notations used in the equations featured in this post*

## How are prefill and decode two different problems?

Prefill processes the full prompt in parallel, producing large GEMM-M (= ISL × [speculative decoding](https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/), decode generates one token at a time, producing small GEMM-M (=

Speculative decoding increases GEMM-M and can shift decode toward compute-bound. Because the query lengths, KV access, and bottleneck differ for prefill and decode (Table 2), each parameter is analyzed separately for each phase.

Prefill | Decode | |
| Query length | Full input (ISL tokens) | 1 token |
| KV context | Prompt (ISL tokens) | Full KV cache (KVSL tokens) |
| Attention GEMM-M | ISL × | |
| Primary bottleneck | Compute (matmul + softmax) | HBM bandwidth (memory) |

*Table 2. Prefill and decode differ in query length, KV context, attention GEMM-M, and primary bottleneck*

Note: With prefix caching, common in agentic and multiturn apps, a new turn may have a short ISL while attending to a large prefix cache. With a short ISL but long prefix cache, prefill behaves like decode.

## How arithmetic intensity governs compute- versus memory-bound behavior

The roofline bounds GPU performance by compute and bandwidth ceilings, as [previously explained](https://developer.nvidia.com/blog/ai-model-co-design-hardware-friendly-llm-design/). Arithmetic intensity determines which binds (Equation 1):

Arithmetic Intensity = Total FLOPs / Total bytes accessed

The *ridge point* marks the transition from memory-bound to compute-bound. Prefill lies well above it and is compute-bound, while decode lies below it and is memory-bound (Figure 2). Speculative decoding raises decode arithmetic intensity and can move it toward the ridge.

## How does the FlashAttention kernel compute attention on GPU?

FlashAttention computes attention without materializing the full attention matrix. It streams tiles of

- First, batched matmul (BMM1) scores queries against keys
- Second, online softmax normalizes the scores using a running max and sum
- Third, second batched matmul (BMM2) weights the values

The BMMs run on Tensor Cores while the softmax exponentials run on special-function units. The BMM shapes drive the arithmetic intensity analysis that follows.

## GEMM shapes

Attention performance follows from the shapes of its two matmuls. Table 3 lists the per-phase (Batch, M, N, K) dimensions of BMM1 and BMM2.

BMM | Phase | Batch | M | N | K | Meaning |
| BMM1 | Prefill | PB × KH | ISL × | ISL | Hsz | Q · Kᵀ: score queries against keys |
| Decode | DB × KH | 1 × | KVSL | Hsz | ||
| BMM2 | Prefill | PB × KH | ISL × | Hsz | ISL | Weights · V: aggregate values |
| Decode | DB × KH | 1 × | Hsz | KVSL |


*Table 3. GEMM (Batch, M, N, K) shapes for BMM1 and BMM2*For decode, GEMM-M =

## Group size

Group size (

Arithmetic intensity as a function of ** **In the following formulas, “Bytes” refers to HBM bytes moved. For simplicity, assume 1 byte per element (that is, FP8 KV cache).

### Prefill

As


FLOPs = 4 × PB × QH × ISL² × Hsz (constant in

Bytes = 2 × PB × KH × Hsz × ISL × (

Arithmetic Intensity = 2 ×

### Decode (GEMM-M = )

Doubling [NVIDIA Nemotron 3](https://developer.nvidia.com/topics/ai/nemotron) adopted GQA with two KV heads, which makes decode more efficient. Equations 5, 6, and 7:

FLOPs = 4 × DB × QH × KVSL × Hsz (constant in

Bytes = 2 × DB × KH × Hsz × (

Arithmetic Intensity = 2 ×

Figure 4 shows decode runtime falls about 2x per doubling of

Note: Speculative decoding raises effective GEMM-M to (1+

**Guideline 1: **Choose

## Head dimension

Unlike group size, head dimension (Hsz) does not affect arithmetic intensity. Doubling Hsz doubles both FLOPs (Equations 2 and 5) and bytes (Equations 3 and 6), leaving their ratio unchanged. Yet Figure 5 shows runtime increasing with Hsz because attention kernels perform three types of work that scale differently with Hsz.

**Matmul:**Grows with Hsz, but in aligned steps. The[previous post](https://developer.nvidia.com/blog/ai-model-co-design-hardware-friendly-llm-design/)recommends model dimensions that are multiples of 128 to align with GPU tile sizes and cache-line widths. A partially filled tile costs as much as a full tile, so Hsz = 64 pays for 128. Hsz ≥ 512 pushes close to the tensor memory (TMEM) capacity limit. That makes 128 and 256 the efficient choices.**Memory**(the KV state): Also grows with Hsz. Since the GPU moves data in 128-byte units, memory access, like matmul, is most efficient when Hsz is multiple of 128.**Softmax**is different: Its cost is independent of Hsz because it operates on attention-score matrix (query tokens × keys), which has no head dimension. Equations 8 and 9:

Softmax ops (prefill) ≈ PB × QH × ISL²

Softmax ops (decode) ≈ DB × QH × KVSL

The balance between these determines Hsz cost in each phase (Figure 5).

Prefill is compute-bound** **(matmul plus softmax). As Hsz grows, matmul FLOPs grow while softmax stays fixed. If prefill were pure matmul, doubling Hsz would double runtime; but the fixed softmax does not scale, so runtime rises less than Hsz does. Figure 5 confirms this: prefill climbs with Hsz but slower than Hsz grows. A wider Hsz amortizes softmax, shifting more kernel time to matmul and making prefill less softmax-bound.

Decode is memory-bound (streaming the KV cache). Larger Hsz increases KV bytes per token (Equation 6), so runtime should scale with Hsz. Figure 5 confirms this, though slightly sublinearly because setup, post-processing, and flash-decoding reduction overheads don’t scale with Hsz and weigh more on the shorter KVSL = 32K kernel.

**Guideline 2**: Use Hsz of 128 or 256.** **Hsz doesn’t change arithmetic intensity but [must align with the hardware](https://developer.nvidia.com/blog/ai-model-co-design-hardware-friendly-llm-design/). Typically, Hsz = 64 still pays for a 128-wide tile, while Hsz ≥ 512 pushes close to the TMEM capacity limit. That makes 128 and 256 the sweet spot.

## Sequence length

Sequence length (ISL / KVSL) affects prefill and decode differently, because it enters each phase through a different variable: prefill processes all ISL input tokens together, while each decode step reads a KV cache of length KVSL. The two therefore scale at different rates (Figure 6).

### Prefill scales quadratically

Prefill performs ISL² work (every token attends to every token), while KV traffic grows only proportional to ISL (Eq. 2, 3). Arithmetic intensity therefore rises linearly with ISL, keeping prefill well above the ridge point and compute-bound. Doubling ISL should roughly quadruple runtime (Figure 6). At short ISL, scaling is below 4x because fixed setup and post-processing overheads dominate; quadratic scaling appears once ISL is large enough to amortize them.

### Decode scales linearly

Each step reads the full KV cache to generate one token, so bytes grow with KVSL while per-step work remains small (Equations 5 and 6). Arithmetic intensity stays near 2 ×

**Guideline 3**: Reduce effective KV state where possible. The use case sets sequence length, but the cost is asymmetric: prefill grows as ISL², while decode grows linearly with KVSL. Reduce effective KV state through KV-cache compression, sparse or sliding-window attention, or hybrid model architectures (like Nemotron 3) where only some layers carry the growing global KV state.

## Tensor parallelism splits attention heads across GPUs

Tensor parallelism (TP) splits the attention heads across GPUs, giving each GPU QH/TP query heads and KH/TP KV heads. It shards heads, not tokens. In Table 3, only the batch dimension, containing KH/TP, shrinks; the per-GPU GEMM shape and arithmetic intensity remain unchanged.

TP has a practical limit: KV heads must divide evenly across GPUs. Once TP > KH, a group’s query heads span multiple ranks, each requiring a copy of the shared KV head. This duplicates KV state, adding memory and bandwidth overhead without benefit (Figure 7). Thus, keep TP ≤ KH so each GPU owns at least one complete group: one KV head and its

Models with few KV heads (Nemotron 3 with two, for example), quickly exhaust TP because the cache cannot be sharded below one KV head per GPU without duplication. Attention must then scale differently: Attention Data Parallelism (ADP) shards requests, while KV Parallelism (KVP) shards long-sequence KV caches across GPUs. The FFN scales separately with Expert Parallelism (EP).

[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) combines these as [Wide EP](https://developer.nvidia.com/blog/scaling-large-moe-models-with-wide-expert-parallelism-on-nvl72-rack-scale-systems/) (ADP for attention plus EP for the FFN), and [Helix Parallelism](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/blogs/tech_blog/blog22_Helix_Parallelism_Scaling_Multi_Million_Token_Decoding_with_KV_Cache_Sharding.md) (KVP for attention plus EP for the FFN). In both cases, KH determines efficient scaling.

**Guideline 4**: Let KH determine the parallelism strategy. Keep TP ≤ KH so each GPU has a full KV head. Models with few KV heads (MQA with 1, or GQA with 2) exhaust TP quickly and are better served by ADP or KVP for attention plus EP for the MoE FFN (implemented as [Wide EP](https://developer.nvidia.com/blog/scaling-large-moe-models-with-wide-expert-parallelism-on-nvl72-rack-scale-systems/) and [Helix Parallelism](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/blogs/tech_blog/blog22_Helix_Parallelism_Scaling_Multi_Million_Token_Decoding_with_KV_Cache_Sharding.md) in TensorRT-LLM).

## Get started co-designing AI model attention

Use the four guidelines summarized below as a model design checklist to get started co-designing AI model attention. These choices can improve GPU utilization, inference speed, throughput, and interactivity on the same hardware.

**Guideline 1**: Choose the group size ( ) for decode and push it high. Prefill is not sensitive to group size.**Guideline 2**: Use a head dimension (Hsz) = 128 or 256 to align with the GPU tiles and 128-byte transfers while staying within TMEM budget. A larger head also hides softmax in prefill.**Guideline 3**: Reduce effective KV state through KV-cache compression, sparse or sliding-window attention, or hybrid models.**Guideline 4**: Match parallelism to KV head count (KH). Keep TP ≤ KH and scale a few KH models with[Wide EP](https://developer.nvidia.com/blog/scaling-large-moe-models-with-wide-expert-parallelism-on-nvl72-rack-scale-systems/)and[Helix Parallelism](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/blogs/tech_blog/blog22_Helix_Parallelism_Scaling_Multi_Million_Token_Decoding_with_KV_Cache_Sharding.md).

### Acknowledgments

*This post is an NVIDIA cross-team effort. We are grateful to Timmy Liu, Jatin Mitra, Tiyasa Mitra, Bhargava Gopireddy, Brian Pharris, Julien Demouth, and Eduardo Alvarez for their help.*

## Start the discussion at forums.developer.nvidia.com

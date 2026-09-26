# [Issue #57] Clarify KernelBench’s Benchmarking Scope: Inline CUDA Kernels vs. Forward Kernels Using PyTorch

source: https://github.com/ScalingIntelligence/KernelBench/issues/57
state: closed | updated: 2026-01-19T12:33:41Z
labels: 

## 正文

I’m trying to understand the intended purpose of KernelBench and find some ambiguity in the paper:

- **Inline CUDA kernels**: Designed to evaluate LLM-generated, from‑scratch CUDA kernels that **do not reuse** PyTorch primitives (e.g., as in [AI CUDA Engineer](https://pub.sakana.ai/ai-cuda-engineer/leaderboard) workflow).

- **Forward kernels**: Designed to evaluate LLM-generated wrappers or glue code that **do call** into existing PyTorch implementations (e.g., as in [CUDA-L1](https://deep-reinforce.com/cuda_l1) workflow).

The paper does not clearly state which of these two scenarios KernelBench is meant to measure. As a result, it’s unclear whether submissions are expected to:

1. Write fully self‑contained CUDA kernels with no PyTorch calls, or
2. Write high‑level `forward()` functions that simply delegate to PyTorch’s optimized backend.

# Questions

1. What exactly does KernelBench measure?
    - Inline/custom CUDA kernels only?
    - Forward wrappers calling PyTorch?
    - Both, with separate tracks?

2. What are the benchmarking requirements?
    - Are PyTorch calls disallowed in the “inline CUDA” track?
    - If PyTorch calls are allowed, what level of originality is expected?

Please update the README and/or paper to explicitly define the two benchmarking modes (if both are intended), including:
- Allowed APIs and library calls for each track.
- Example submissions for each mode.

**If only one mode is intended, please clarify in both the paper and the repository documentation.**

## 评论 (2)

### simonguozirui · 2026-01-18

Hi @yuxuan-z19, for the original KernelBench release and [paper](https://arxiv.org/abs/2502.10517), we clearly define the format to be PyTorch `Model` --> PyTorch `ModelNew` with **inline** cuda kernels, in Section 3.1. 
See the examples in `prompts` of pairs of (`Model`, `ModelNew`) for concrete fomrat specification that we provide model during evaluation. That is different from both the AI CUDA engineer and the CUDA-L1 format you linked here, where they write the forward function in torch or CUDA. Although the community is free to use the KernelBench tasks for their own evaluation format and settings, as long as they state it clearly. 

We explicitly ensure that outputed program must contain custom cuda (or other DSL) kernels. In the original paper, we let the model decide which PyTorch ops to replace with custom kernels as it sees fit. In some settings, it might be better to strictly enforce all computation ops must be written in the target kernel language (no torch computatioal allowed), especially for settings like RL (like in [Kevin](https://arxiv.org/abs/2507.11948)). We recently released a tool #110 that you can use to check programs do contain kernel code and flag reward hacking behavior.

We will make that clear in the WIP benchmarking guide on the repo. 

### yuxuan-z19 · 2026-01-19

###  Point 1: Definition of “CUDA kernel”

> “we clearly define the format to be PyTorch Model --> PyTorch ModelNew with inline cuda kernels, in Section 3.1.”

The way you define “CUDA kernel” in the paper is extremely vague. To us PERF folks, a CUDA kernel means either **pure handwritten CUDA C++ without any 3rd-party libraries** or a **DSL-based implementation** (e.g., CuGraph-optimized PyTorch operators). Your ICML paper does not clarify whether the benchmark tests LLMs on generating **a single operator**, or more generally, **a piece of CUDA code**. Without this, it’s impossible to interpret the results: are we measuring true CUDA code generation capability, or just PyTorch operator optimization?

### Point 2: Benchmark rules and levels

> “Although the community is free to use the KernelBench tasks for their own evaluation format and settings, as long as they state it clearly.”

If that’s the case, **_why did KernelBench simultaneously fail in past ICLR 2026 reviews_**?

- [KernelBench is not a reliable benchmark. Many of its shapes are too small, and the choice of pytorch eager as a baseline means you're mostly profiling against overhead.](https://openreview.net/forum?id=c339hUw3cy&noteId=vLDg4fdqS2)
- [KernelBench, as a benchmark, is quite flawed, because many of its tasks use shapes that are too small, exacerbating the overheads induced by not using torch.compile as the baseline.](https://openreview.net/forum?id=f4GtuI2blh&noteId=OwqbUWVENl)
- etc.

The rules are ambiguous, and your “levels” are inconsistent. For example:
- Level1 97: [FlashAttention BF16](https://github.com/ScalingIntelligence/KernelBench/blob/main/KernelBench/level1/97_ScaledDotProductAttention.py)
- Level3 50: [ReLU+Self-Attention](https://github.com/ScalingIntelligence/KernelBench/blob/main/KernelBench/level3/50_ReLUSelfAttention.py)

A FlashAttention kernel is orders of magnitude more complex than ReLU + Self-Attention, yet the level assignment contradicts the stated goal of measuring LLM’s kernel-writing ability. This shows the benchmark **doesn’t actually test operator-level correctness**, nor does it consider input shapes, tensor initialization, or runtime coverage, as a [real compiler benchmark](https://github.com/meta-pytorch/tritonbench) does.

### Point 3: Kernel checker

> We explicitly ensure that outputed program must contain custom cuda (or other DSL) kernels ... tool https://github.com/ScalingIntelligence/KernelBench/pull/110 ... check programs do contain kernel code and flag reward hacking behavior.

A regex-based checker is laughably insufficient. One can trivially write a Torch C++ “handwritten” kernel that passes your regex while **never generating actual low-level CUDA code**. You do not forbid ATen or other high-level libraries, so the tool does **not enforce kernel-level correctness at all.** A proper professional check would involve `torch.profiler` or similar tooling to extract compiled CUDA kernels and cross-verify them against a whitelist, only that would give meaningful guarantees.

### Bottom line

KernelBench’s design shows fundamental misunderstanding of both CUDA kernels and LLM benchmark methodology. As it stands, it measures neither LLM kernel-writing capability nor end-to-end CUDA performance in a meaningful way. The current version cannot claim to be a rigorous benchmark.

**If ICLR couldn’t endorse it as a valid agent benchmark, why should ICML, ACL, or NeurIPS? Accepted or not, KernelBench is an unreliable foundation for any follow-up work.**


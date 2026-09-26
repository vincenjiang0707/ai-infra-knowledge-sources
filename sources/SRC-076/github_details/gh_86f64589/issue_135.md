# [Issue #135] What is the difference between KernelAgent and NVIDIA's AVO (Agentic Variation Operators)?

source: https://github.com/meta-pytorch/KernelAgent/issues/135
state: closed | updated: 2026-06-01T18:03:51Z
labels: 

## 正文

Hi developers,

Thank you for open-sourcing such a great kernel agent! I am very interested in triton kernel auto-generation and a newbie to this project.

Could you please help me distinguish the differences meta's KernelAgent and [NVIDIA's AVO](https://arxiv.org/html/2603.24517v1)?

## 评论 (2)

### Laurawly · 2026-05-14

> Hi developers,
> 
> Thank you for open-sourcing such a great kernel agent! I am very interested in triton kernel auto-generation and a newbie to this project.
> 
> Could you please help me distinguish the differences meta's KernelAgent and [NVIDIA's AVO](https://arxiv.org/html/2603.24517v1)?

Thanks for the question! My understanding is that KernelAgent and AVO are related in spirit but not the same abstraction.

KernelAgent is designed as a general open-source pipeline for PyTorch/Triton kernel synthesis and optimization: it can decompose workloads, generate verified Triton kernels, compose them back into an end-to-end forward pass, and optionally run a hardware-guided optimization loop with profiling, bottleneck diagnosis, parallel exploration, correctness checks, and benchmarking.

AVO, based on the paper, frames the problem as autonomous evolutionary search: agentic variation operators replace fixed mutation/crossover rules and use lineage, domain knowledge, and execution feedback to evolve candidates. The reported evaluation is focused on attention kernels on Blackwell GPUs.

In short: KernelAgent is a broader framework for verified Triton kernel generation and optimization across KernelBench/PyTorch-style workloads; AVO is a specialized agentic evolutionary search method shown on attention-kernel optimization. The two approaches are complementary and share the use of agents + feedback, but differ in scope and search formulation.

### zigzagcai · 2026-05-15

Thank you @Laurawly for such detailed explanation.

I think your KernelAgent framework is excellent, which models the computation graph using AST and then lets the subagent optimize the small kernels.

I plan to try your AST decomposition method, combined with agentic variation, to figure out whether it possible to automatically optimize the inference pass of model.

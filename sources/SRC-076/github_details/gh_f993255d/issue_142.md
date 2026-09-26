# [Issue #142] Question: How to validate the backward pass of KernelBench ops?

source: https://github.com/ScalingIntelligence/KernelBench/issues/142
state: closed | updated: 2026-03-05T07:58:29Z
labels: 

## 正文

(empty)

## 评论 (1)

### simonguozirui · 2026-03-05

Hi @zigzagcai, KernelBench is currently forward pass only, and many frameworks that followed focus on that as well: [PyTorch BackendBench](https://github.com/meta-pytorch/BackendBench), [FlashInfer-Bench](https://flashinfer.ai/2025/10/21/flashinfer-bench.html), and [NVIDIA compute-eval](https://github.com/NVIDIA/compute-eval).

Backward pass is certainly important, but requires much more careful consideration. A few things that come to mind immediately (definitely not exhaustive): the right numerical check and tolerance against a PyTorch autograd reference (note [torch.autograd.gradcheck](https://docs.pytorch.org/docs/stable/generated/torch.autograd.gradcheck.gradcheck.html) with float64, non-determinism from atomic ops during backward passes  [see more](https://pytorch.org/docs/stable/notes/randomness.html), hard to find clean decomposed reference to check the gradient against for fused ops. 

Worth pointing out that @RobertTLange and Sakana's [robust-kbench](https://github.com/SakanaAI/robust-kbench) has support for backward pass evaluation; they validate the custom backward kernel against PyTorch's autograd reference with explicit tolerances (atol=1e-5, rtol=1e-5) (see this function [here](https://github.com/SakanaAI/robust-kbench/blob/078f5bab29934a822268d59a4e707d449abf9b4e/robust_kbench/sandbox/correct_backward_fn.py#L36C1-L37C1)). I think that is a great starting point.  

Happy to discuss further, I don't have a complete picture yet of the right approach for KernelBench torch ops yet. I can put that on the roadmap.

# [Issue #68] Why Torch.compile is usually slower than eager mode?

source: https://github.com/ScalingIntelligence/KernelBench/issues/68
state: closed | updated: 2025-10-23T20:46:20Z
labels: 

## 正文

Hi, thank you for releasing the dataset for your inspiring work.

I've noticed that in table 1 in your [paper](https://arxiv.org/pdf/2502.10517), the speedup over torch.compile is usually higher than over torch eager mode, which means torch.compile is usually slower than eager mode. 

One example I've looked into myself is the `cross_entropy forward` task. I've tried different modes of torch.compile, and also given it more warmup iterations. However, seems like in all cases torch.compile is slower than eager. I'm wondering if this phenomenon is expected, especially for task as simple as `cross_entropy forward`? Or I could be missing something for torch.compile, and could you kindly provide some guidance on the best practice?

Attached is the speedup of my kernel over torch eager and torch.compile, where the speedup over torch eager is lower (which means eager is faster) than torch.compile.

Thank you very much for your time and help! @simonguozirui 

<img width="1289" height="41" alt="Image" src="https://github.com/user-attachments/assets/028b4bca-a01e-43a0-858e-957c936648c5" />


## 评论 (4)

### PaliC · 2025-10-23

tl;dr: This is expected and I would use eager as the reference for level 1.

This is a good question. torch.compile does have a small (roughly constant) amount of overhead associated with it (e.g., guard checking, cache lookups, etc.). For singular ops (as in KernelBench level 1), this overhead can sometimes dominate the actual operation, which is expected since individual ops are already highly optimized CUDA implementations.

The main performance gains from torch.compile come from vertical fusions, which should be more apparent in the higher levels of KernelBench. For level 1, I’d focus primarily on beating the eager benchmark.

Note: This behavior may change for PyTorch versions >2.5, as the compiler evolves frequently. It’s worth retesting with newer releases.

### simonguozirui · 2025-10-23

This was an issue that confused me for a long time as well when I was first working on the paper, and drove me crazy for a bit. Thank you to @PaliC and others from the PyTorch team for helping me understand why that might be the case. 

Thank you @LeoXinhaoLee for raising this (I put a note in the paper, actually in a footnote under section 4.1, and in detail in Appendix B). For our Fall 25 roadmap #74, we plan to upgrade our Torch version as @PaliC suggests and provide a comprehensive guide on how to profile and advice on what baseline to run against for each of the 3 levels.

### LeoXinhaoLee · 2025-10-23

Thank you guys very much for your help and suggestions! Looking forward to seeing the updated KernelBench benchmark guidelines!

### simonguozirui · 2025-10-23

@Marsella8 @PaliC @pythonomar22 @AffectionateCurry @nathanjpaek   let's take note on this when making the new benchmarking guide!

# [Issue #43] [Feature] Add benchmark for AMD accelerators

source: https://github.com/ScalingIntelligence/KernelBench/issues/43
state: closed | updated: 2025-10-05T06:07:41Z
labels: 

## 正文

AMD accelerators do not have competitive training and inference performance with NVIDIA accelerators. This lack of performance, in part, could be significantly improved with kernel level optimizations for `pytorch`.

This benchmark could serve as a community driven development accelerator to bridge this performance gap.

## 评论 (3)

### simonguozirui · 2025-06-01

Hi Nelly, thanks for taking an interest in the KernelBench project and the suggestion.

We recently spoke with the AMD team. A good first goal is to add HiP (AMD equivalent of CUDA) support as a KernelBench backend.

See efforts such as #37 to integrate AMD accelerators as a backend for KernelBench. We welcome contributors from AMD and beyond (from the community). 


### ai-nikolai · 2025-08-19

@simonguozirui - great initiative, is there any news on progress with the PR?

Also, would it be worth considering external file compilation (i.e. not in-line)? I would be open to contribute to a next generation of the paper, if you guys are interested. Thanks.

### simonguozirui · 2025-10-05

Hi @ai-nikolai, yes @willhu-jpg and I discussed with the AMD team recently and was trying to see if they can provide guidance on how to best integerate inline or other kernel compilation pipeline with AMD.

I agree with you we might have to think about integerating with other frameworks that not necessariliy support inline. Although a lot of frameworks could be used with jit compilation or inline code, some of the more performant frameworks require compilation, linking, or namespace management. ThunderKitten integration I worked on with @simran-arora was one example of that and it wasn't too clean. 

This fall, team @pythonomar22  @nathanjpaek @AffectionateCurry and I will think about best ways to do this. But if you (or anyone) have interesting design ideas re that, we would love to hear.

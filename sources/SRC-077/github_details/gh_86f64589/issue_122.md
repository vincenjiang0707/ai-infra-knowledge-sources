# [Issue #122] Regarding the choice of large language models?

source: https://github.com/meta-pytorch/KernelAgent/issues/122
state: open | updated: 2026-03-19T02:49:34Z
labels: 

## 正文

I am curious whether switching to another LLM—such as DeepSeek-v3.2 or Qwen3—would yield similar results. Additionally, I wonder whether the reported 100% accuracy reflects the outcome of a single execution or the result averaged over multiple experimental runs.

## 评论 (3)

### Jack-Khuu · 2026-03-18

The choice of LLM definitely has an effect on the quality of the generation (imagine doing this with a 3B model), and I expect as foundational models get stronger some of the harness will be overkill.

> 100% accuracy reflects the outcome of a single execution or the result averaged over multiple experimental runs

Mind elaborating which 100% you're referring to? 
If this is in reference to kernel synthesis/optimization, it's possible for a single sweep across all problems (e.g. KernelBench) to have some that fails to optimize/generate due to general model non-determinism (in which case retry typically make it go through)

### Arthur-Ling · 2026-03-19

From the blog https://pytorch.org/blog/kernelfalcon-autonomous-gpu-kernel-generation-via-deep-agents/, we can see that "coverage of L1/2/3 is all 100%". I find this extremely interesting and am curious about how you managed to achieve 100% coverage for L1, L2, and L3.  And have you recorded the success rate of kernel synthesis for KernelBench Level 1 using GPT‑5 or o4‑mini when running it just once?

### Jack-Khuu · 2026-03-19

cc: @Laurawly who wrote the original blog

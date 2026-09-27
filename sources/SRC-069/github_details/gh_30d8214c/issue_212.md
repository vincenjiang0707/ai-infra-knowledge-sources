# [Issue #212] [Question] Supported CUDA/Torch/Python combinations

source: https://github.com/deepseek-ai/DeepGEMM/issues/212
state: open | updated: 2025-10-15T10:32:03Z
labels: 

## 正文

Hey @LyricZhao,

in my fork I tried to dry-run the publish workflow and found that some wheels cannot be build. Could you have a brief look and check if we need to exclude i.e. old cuda or old python versions?

I'll submit a new PR soon to finalize the wheel build

Run: https://github.com/ko3n1g/DeepGEMM/actions/runs/18435420460

Thx!

## 评论 (21)

### LyricZhao · 2025-10-13

Thanks for the fixes, CUDA {12, 13} x Python {3.8, 3.9, 3.10, 3.11, 3.12, 3.13} are enough.

### LyricZhao · 2025-10-13

In https://github.com/deepseek-ai/DeepGEMM/pull/214/files, I saw you remove the Python 3.8 support? Our cluster has some Python 3.8 environment, which means we still need it.

### LyricZhao · 2025-10-13

Another way to solve the Python issue, is to use a Python ABI framework that supports any Python :)

### ko3n1g · 2025-10-14

@LyricZhao could you create and push a new tag to main?:) 

No release, just the tag 

### LyricZhao · 2025-10-14

Pushed, thx again! https://github.com/deepseek-ai/DeepGEMM/releases/tag/v2.1.1

### ko3n1g · 2025-10-14

Are you the owner of https://pypi.org/project/deep-gemm/? If so, can you add `ko3n1g` as maintainer to it?

---

Edit: In case you are not the owner, we can choose the project name `deepgemm` instead of `deep_gemm`. Note that the package name will be untouched (it will still be: `deep_gemm`). 
In short: Project-name and Package-name are often the same, but pip doesn't enforce it (take `PIL` and `pillow` as an example).
 

### ko3n1g · 2025-10-15

In case this notification got lost in transit, @LyricZhao :)

### LyricZhao · 2025-10-15

Oh, sorry. Creating now (I am not the owner)

### LyricZhao · 2025-10-15

Sorry, can you create the project for me? We have lots of internal stuffs going, I am not familar with PyPi packing and distribution, and my time is limited.

### LyricZhao · 2025-10-15

I've created the account, but seems more procedures to distribute.

### ko3n1g · 2025-10-15

No worries happy to help. But are you fine we're diverging from the name `deep-gemm` as this is already taken by someone else? We would choose `deepgemm` instead.

### LyricZhao · 2025-10-15

I think `deep_gemm` is better? As our training/inference framework is using `import deep_gemm`. Changing into `deepgemm` will introduce so many compatibility issues.

### LyricZhao · 2025-10-15

Does pypi support `_` instead of `-`?

### ko3n1g · 2025-10-15

this is not about the import-name but about the pip-install command.

It will always stay `import deep_gemm`

but we have to go with `pip install deepgemm` instead of `pip install deep-gemm` (since the latter is already taken)

### LyricZhao · 2025-10-15

How about `pip install deep_gemm`? Consistent with importing names.

### ko3n1g · 2025-10-15

Also taken, PyPI auto-translates `_` to `-`. 

### LyricZhao · 2025-10-15

Ok, then `deepgemm` is fine for me :)

### ko3n1g · 2025-10-15

Here's the required PR: https://github.com/deepseek-ai/DeepGEMM/pull/217

### ko3n1g · 2025-10-15

Thanks a lot for taking your time to discuss this with me! We're almost done:)

### LyricZhao · 2025-10-15

Thanks! Already merged.

### ko3n1g · 2025-10-15

I'll create a new tag now (hope its fine)

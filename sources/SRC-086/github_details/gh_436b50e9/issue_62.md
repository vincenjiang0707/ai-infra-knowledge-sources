# [Issue #62] Results for different configs

source: https://github.com/FasterDecoding/Medusa/issues/62
state: closed | updated: 2023-11-17T07:34:55Z
labels: 

## 正文

Awesome project! I was wondering if you would be able to share the mt-bench results for the different Medusa configs. Specifically from this ablation:
![image](https://github.com/FasterDecoding/Medusa/assets/39166683/99bd7684-10c2-4c84-adef-00dea9439a37)


## 评论 (8)

### leeyeehoo · 2023-11-16

We are working on V1.0. So at that time, you will expect us to show more detailed information on how the ablation works (and maybe an Arxiv report).

### zankner · 2023-11-16

Understood. If I am benchmarking for a paper should I assume that the settings reported in the repository, ie (mc_sim_7b_63), are the current optimal inference settings?

### leeyeehoo · 2023-11-17

If you have your own model, and you want to generate a sparse tree, please refer to [the preview version](https://github.com/FasterDecoding/Medusa/tree/v1.0-prerelease/medusa/eval). The folder contains a readme that will guide you customize your tree settings step by step.

### zankner · 2023-11-17

Understood thanks! Is there a timeline for v1 will be fully released?

### leeyeehoo · 2023-11-17

It will be very soon... We still have some minor issues to try to fix :)  pls stay tuned!

### zankner · 2023-11-17

Are there any breaking changes? Ie if I have been basing my code off the main branch are there any bugs or issues with that branch? Sorry for all the questions

### leeyeehoo · 2023-11-17

The eval folder is self-contained and should be compatible with the original one. We are trying to implement other recent models w full-finetuning and the branch is not tested yet...

### zankner · 2023-11-17

Ah ok thank you very much! Great work btw!

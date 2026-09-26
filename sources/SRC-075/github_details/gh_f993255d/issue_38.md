# [Issue #38] Revamped Eval Function

source: https://github.com/ScalingIntelligence/KernelBench/issues/38
state: open | updated: 2025-11-22T22:45:08Z
labels: 

## 正文

During investigation with Sakana's Kernel in #25, we created a stronger eval function to avoid that kind of exploits that some observed.
I didn't merge it in (sit on a branch) because we want to make sure our paper result didn't change from such an update (for ICML rebuttal).

During ICML rebuttal, I have also checked if any of our existing kernels have similar kind of exploits. Luckily, none of our kernels are smart enough to do that yet.

Now that ICML is over, I plan to merge the more robust eval function in.  

In particular, the simple fix is 
```
compute reference, Model
clear cache
compute reference, ModelNew
check if they are equivalent

AND

compute reference, ModelNew
clear cache
compute reference, Model
check if they are equivalent
```
Check both directions to be extra sure!

## 评论 (2)

### simonguozirui · 2025-05-07

Actually shout out to the @CognitionAI-AI folks for spotting that again in their [Kevin](https://cognition.ai/blog/kevin-32b) blog post. They resort to `by first running the tested kernel and then the reference implementation, thus avoiding this hack.` So this proposed eval update will address that as well.

We should keep the infra updated and robust so more people can build on this!

### simonguozirui · 2025-11-22

We have been systematically revamping eval function the last few weeks, with team (@Marsella8 @PaliC @bkal01  @alexzhang13). We have been writing a benchmarking guide, adding additional adversarial unit tests, and a blog post uncovering the common issues. Checkout active PRs #89  and #82.

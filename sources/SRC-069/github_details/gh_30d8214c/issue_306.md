# [Issue #306] About the version of DeepEP for mega_moe_kernel

source: https://github.com/deepseek-ai/DeepGEMM/issues/306
state: closed | updated: 2026-04-30T08:03:31Z
labels: 

## 正文

Thank you for your marvelous work! i've been trying to test the mega_moe kernel , and encountered an error about deepep:
```
ep_buffer = deep_ep.ElasticBuffer(
                ^^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'deep_ep' has no attribute 'ElasticBuffer'
```
And I found that there's no ElasticBuffer in the latest DeepEP... Could you please give the version of DeepEP for the kernel? Many many thanks!

## 评论 (3)

### engineer1109 · 2026-04-17

+1 

### thisjiang · 2026-04-24

+1

### zheanxu · 2026-04-30

Thank you for your kind words and for testing the mega_moe kernel!

The `ElasticBuffer` class is indeed a new feature introduced in **DeepEP v2**. The latest DeepEP release (v2) includes this API, but the older version does not. Please make sure you install the correct version — you can find it at the link you mentioned: [DeepEP v2](https://github.com/deepseek-ai/DeepEP/pull/605). After updating, the error should be resolved.

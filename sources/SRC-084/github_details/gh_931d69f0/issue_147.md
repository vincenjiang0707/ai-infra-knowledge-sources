# [Issue #147] Groupsize constraint for marlin

source: https://github.com/dropbox/hqq/issues/147
state: closed | updated: 2025-02-05T14:46:07Z
labels: 

## 正文

 I notice that for marlin, it says it ONLY WORKS WITH AXIS=1, group_size= - 1. I wonder the reason, especially the groupsize constraint.

## 评论 (2)

### mobicham · 2025-02-05

Because the CUDA kernel only supports those settings. 
Marlin HQQ in VLLM only supports `axis=1` and `group_size=64` by the way, so if you're interested in VLLM runtime make sure to use those settings.

### ZeleiShao · 2025-02-05

Thank you really really much!!!

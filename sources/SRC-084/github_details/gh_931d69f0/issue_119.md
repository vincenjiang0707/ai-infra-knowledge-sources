# [Issue #119] integrated into gpt-fast

source: https://github.com/dropbox/hqq/issues/119
state: closed | updated: 2024-11-01T18:44:53Z
labels: 

## 正文

Is it possible to easily integrate hqq's quantization and forward into gpt-fast repo? In gpt-fast, there is int8, int4 quantization, i want to replace them with hqq and using hqq for low-bit inference while keep other structures unchanged. What is the easiest way to do this with least code change? Thanks for any valuable advice!

## 评论 (1)

### mobicham · 2024-09-14

It's already integrated in torchao: https://github.com/pytorch/ao/releases/tag/v0.5.0 
So you just use `quantize_(model, int4_weight_only(group_size, use_hqq=True)` for example

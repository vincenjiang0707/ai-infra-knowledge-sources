# [Issue #2356] [BUG] AWQ `sym=True` regression

source: https://github.com/ModelCloud/GPTQModel/issues/2356
state: closed | updated: 2026-01-13T07:57:51Z
labels: bug

## 正文

We are fixing an `sym=True` aka (`zero_point=False`)  on `main`. 

Should be fixed once https://github.com/ModelCloud/GPTQModel/pull/2355 is completed.

## 评论 (2)

### Qubitium · 2026-01-13

PR #2355 does not fix this bug but actually exposed it. Fix will come from another PR. 

In the mean time, please use `sym=False` for `awq` quantization until we push/merge the fix to `main`. 

To clear any confusion for those coming from `autoawq`. `main` dev branch has merged `zero_point` property (normalized it) with gpt-qmodel `sym` so one `symmetric` property is used/shared for both gptq/awq. Save format retains `zero_point` qcfg in json for compatbility with vllm/sglang loading.  

### Qubitium · 2026-01-13

Fixed with https://github.com/ModelCloud/GPTQModel/pull/2357. 

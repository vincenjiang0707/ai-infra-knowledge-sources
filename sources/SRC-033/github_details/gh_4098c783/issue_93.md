# [Issue #93] Support out_dtype in torch.bmm

source: https://github.com/Ascend/pytorch/issues/93
state: open | updated: 2026-03-27T06:24:50Z
labels: 

## 正文

Since torch 2.8, `torch.bmm` supports an `out_dtype` parameter. From the [docs](https://docs.pytorch.org/docs/2.8/generated/torch.bmm.html) "the dtype of the output tensor, Supported only on CUDA and for torch.float32 given torch.float16/torch.bfloat16 input dtypes"

Could this be added?


## 评论 (2)

### yunyiyun · 2026-01-09

感谢您的反馈，后续会跟进支持

### zhuhaozhecool · 2026-03-24

Hi @fiskrt  May I know why you need this feature to get higher accuracy?

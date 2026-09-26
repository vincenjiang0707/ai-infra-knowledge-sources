# [Issue #86] npu如何设置随机种子

source: https://github.com/Ascend/pytorch/issues/86
state: open | updated: 2025-10-14T06:22:48Z
labels: 

## 正文

请问一下，在npu上如何设置随机种子呢，我试了一下用torch::manual_seed(seed)只在cpu上起作用，npu并没有起作用

## 评论 (1)

### yunyiyun · 2025-10-14

torch_npu.npu.manual_seed

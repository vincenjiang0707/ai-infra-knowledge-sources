# [Issue #47] 2.1.0版本build报错

source: https://github.com/Ascend/pytorch/issues/47
state: open | updated: 2024-08-13T03:43:25Z
labels: 

## 正文

pytorch/third_party/op-plugin/op_plugin/ops/base_ops/opapi/SwiGluKernelNpuOpApi.cpp:30:12: error: could not convert ‘output_sizes’ from ‘SmallVector<[...],8>’ to ‘SmallVector<[...],32>’

v2.1.0-6.0.rc1版本build报错

## 评论 (1)

### yunyiyun · 2024-08-13

使用推荐的docker环境构建

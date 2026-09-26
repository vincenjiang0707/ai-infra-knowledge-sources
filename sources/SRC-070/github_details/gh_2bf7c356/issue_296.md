# [Issue #296] If I modify config.cuh and internode.cu, can DeepEP support a setup with two nodes, each having one GPU?

source: https://github.com/deepseek-ai/DeepEP/issues/296
state: closed | updated: 2026-09-20T03:17:41Z
labels: 

## 正文

Hi DeepEP Group,

Our test platform has 2 nodes with 1 GH200 each. We want to run DeepEP's internode test, but there's a config NUM_MAX_NVL_PEERS == 8. Can we modify this config and other assertions to support our 2-node platform?

## 评论 (1)

### sphish · 2025-07-15

You can refer to https://github.com/deepseek-ai/DeepEP/issues/104

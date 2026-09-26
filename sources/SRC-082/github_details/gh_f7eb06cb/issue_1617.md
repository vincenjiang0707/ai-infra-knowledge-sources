# [Issue #1617] Torch Linear instead of Triton Linear

source: https://github.com/ModelCloud/GPTQModel/issues/1617
state: closed | updated: 2025-12-23T09:47:35Z
labels: 

## 正文

Hey Team, 

In our tests in transformers we were expecting the layer type to be `tritonv2` for T4 gpus, but after the latest release it's `torch`. Any ideas why ? Thanks a lot !

## 评论 (1)

### Qubitium · 2025-12-23

Ooops. This got lost somewhere. Since gptqmodel does auto kernel selection, ci tests should not test for kernel type when in auto mode but switch to manual selection in ci tests, if single kernel detection is desired

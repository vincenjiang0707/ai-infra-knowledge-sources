# [Issue #4415] [Bug]在使用最新的latest-cu128的docker 镜像的时候出现 illegal memory access

source: https://github.com/InternLM/lmdeploy/issues/4415
state: closed | updated: 2026-04-10T02:20:33Z
labels: awaiting response, Stale

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug
在使用openmmlab/lmdeploy:latest-cu12.8和openmmlab/lmdeploy:latest-cu12的时候，输入任何内容都会触发下面的错误。使用的环境是V100 32GB * 8.

[TM][ERROR] CUDA runtime error: an illegal memory access was encountered /opt/lmdeploy/src/turbomind/core/stream.h:27


### Reproduction

下载最新版的docker pull openmmlab/lmdeploy:latest-cu12.8
加载glm-4.7-flash-awq模型
执行推理任务的时候出现错误，会导致框架重新启动

### Environment

```Shell
lmdeploy:latest-cu12.8
ubuntu 2204
```

### Error traceback

```Shell
[TM][ERROR] CUDA runtime error: an illegal memory access was encountered /opt/lmdeploy/src/turbomind/core/stream.h:27
[TM][ERROR] CUDA runtime error: an illegal memory access was encountered /opt/lmdeploy/src/turbomind/core/allocator.cc:49
[TM][ERROR] CUDA runtime error: an illegal memory access was encountered /opt/lmdeploy/src/turbomind/core/allocator.cc:49
[TM][ERROR] void turbomind::LlamaLinear::Impl::Forward(turbomind::core::Tensor&, const turbomind::core::Tensor&, const turbomind::LlamaDenseWeight&, const turbomind::core::Buffer_<int>&, const turbomind::core::Buffer_<int>&): 1
[TM][ERROR] CUDA runtime error: an illegal memory access was encountered /opt/lmdeploy/src/turbomind/core/allocator.cc:55
```

## 评论 (0)

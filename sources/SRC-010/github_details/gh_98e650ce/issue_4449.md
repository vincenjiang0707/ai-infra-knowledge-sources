# [Issue #4449] [Feature] Qwen3.5 VLM能不能新打一个镜像？

source: https://github.com/InternLM/lmdeploy/issues/4449
state: closed | updated: 2026-03-27T17:32:57Z
labels: awaiting response

## 正文

### Motivation

现在的镜像是0.12.2版本，新修复的Qwen3.5不能支持图片的问题 在这个版本里没有，能不能新建一个新的镜像，把新修复的功能带上呢？感谢～我自己打镜像总是跑不通。

### Related resources

_No response_

### Additional context

_No response_

## 评论 (2)

### lvhan028 · 2026-03-24

因为 lmdeploy pypi 空间满了，正式版本发布流程走不了。
刚刚发起了 latest docker image 构建和发布的 workflow，晚些时间可以尝试下 openmmlab/lmdeploy:latest-cu12.8 


### zhangyexun · 2026-03-24

> 因为 lmdeploy pypi 空间满了，正式版本发布流程走不了。 刚刚发起了 latest docker image 构建和发布的 workflow，晚些时间可以尝试下 openmmlab/lmdeploy:latest-cu12.8

好的，太感谢了！！


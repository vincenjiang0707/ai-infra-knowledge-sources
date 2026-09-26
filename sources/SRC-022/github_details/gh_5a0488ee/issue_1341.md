# [Issue #1341] [Feature]: cbuild: support running without sudo

source: https://github.com/ROCm/rccl/issues/1341
state: closed | updated: 2025-01-06T15:31:16Z
labels: Under Investigation

## 正文

### Suggestion Description

sudo is actually not needed in docker if you setup docker as rootless service (good for security) and sudo is not available on all the systems. Please remove sudo from the cbuild script

### Operating System

linux

### GPU

any

### ROCm Component

rccl, rocm

## 评论 (4)

### sohaibnd · 2024-12-30

Hi @nicolalunghi-xlnx, sorry for the late response. Which "cbuild" script are you referring to?

### nicolalunghi-xlnx · 2025-01-06

Hi sorry you can close this as I picked the wrong repo.


### nicolalunghi-xlnx · 2025-01-06

Hi actually this was related to the rdma-core project

https://github.com/linux-rdma/rdma-core/blob/master/buildlib/cbuild

I don't know how to open an issue there

### sohaibnd · 2025-01-06

> I don't know how to open an issue there

See https://github.com/linux-rdma/rdma-core?tab=readme-ov-file#reporting-bugs

Please don't open issues unrelated to ROCm under its repos. I'm closing this issue.



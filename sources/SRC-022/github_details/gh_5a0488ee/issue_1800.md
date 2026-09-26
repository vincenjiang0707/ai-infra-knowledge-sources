# [Issue #1800] [Issue]: RCCL DMABUF breaks when /boot isn't readable

source: https://github.com/ROCm/rccl/issues/1800
state: closed | updated: 2025-10-21T17:41:11Z
labels: Under Investigation

## 正文

### Problem Description

/boot might not be readable (e.g. on Azure Linux 3), hence [this](https://github.com/ROCm/rccl/blob/6b4ad0fd74e3b24afea3ea025501b0fb2b0431d4/src/misc/rocmwrap.cc#L134) can break
A [more robust approach of reading kconfig](https://github.com/kubernetes/system-validators/blob/e6e77857caf8e6f5ef43fb61d59d034f5f4c0f94/validators/kernel_validator.go#L177) should be used

### Operating System

Azure Linux 3

### CPU

N/A

### GPU

MI300X

### ROCm Version

6.2

### ROCm Component

rccl

### Steps to Reproduce

run rccl-tests with NCCL_DMABUF_ENABLE=1

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (4)

### ppanchad-amd · 2025-07-11

Hi @arsdragonfly. Internal ticket has been created to investigate this issue. Thanks!

### lucbruni-amd · 2025-07-21

Hi @arsdragonfly, just wanted to let you know I was able to consistently reproduce your issue and I'm working with the team to get a fix in. Thanks for your patience.

### mberenjk · 2025-07-25

Hi @arsdragonfly 
Could you please test with this PR and see if the issue is resolved?
https://github.com/ROCm/rccl/pull/1825

### lucbruni-amd · 2025-10-21

#1825 has been merged to the `develop` branch addressing this issue, which has fallen inactive. Closing this issue as resolved.

Please feel free to reopen this issue if it persists with the latest changes, or open a new one if you have other inquiries. Thanks!

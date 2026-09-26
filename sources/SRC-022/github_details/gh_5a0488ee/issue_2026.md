# [Issue #2026] [Feature]: Any plan to support strix halo gfx1151?

source: https://github.com/ROCm/rccl/issues/2026
state: closed | updated: 2026-01-22T18:08:11Z
labels: Feature Request, status: triage

## 正文

### Suggestion Description

I just tried out the RCCL tests on two Strix Halo devices over Thunderbolt. It seems like currently it does not support RCCL, or RCCL is not enabled. I tried to manually build RCCL with gfx1151 support but got stuck with the final linking step.
I wonder if there will be support for Strix Halo devices for RCCL in the future? Any information would be appreciated.

### Operating System

Ubuntu 25.04

### GPU

Ryzen™ Al Max+ 395

### ROCm Component

_No response_

## 评论 (2)

### huanrwan-amd · 2025-11-17

@ChihayaK Thanks for posting. At the moment, we do not have plans to support Strix Halo for RCCL. Please stay tuned for future updates.

### huanrwan-amd · 2026-01-22

@ChihayaK we will track this support through https://github.com/ROCm/rocm-systems/issues/2788

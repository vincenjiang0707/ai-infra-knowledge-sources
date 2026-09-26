# [Issue #80] [Feature]: Add Extra Memcpy Types to Event Information

source: https://github.com/ROCm/rocprofiler-sdk/issues/80
state: closed | updated: 2025-08-07T18:29:57Z
labels: Under Investigation, Feature Request

## 正文

### Suggestion Description

In CUPTI, there are several memory event types that give us insight on the whether the source is pinned, pageable etc. which is very useful when analyzing traces: https://github.com/pytorch/kineto/blob/16e2a56ba1b65412ea774d183b577d3fc2734501/libkineto/src/cupti_strings.cpp#L41

In Roctracer/rocprofiler we have much less support within Kineto: https://github.com/pytorch/kineto/blob/16e2a56ba1b65412ea774d183b577d3fc2734501/libkineto/src/RoctracerLogger.h#L30

It is not clear if the support in Kineto is simply out of date or if ROCm profiling doesn't have these event types all together. Thank you!

### Operating System

_No response_

### GPU

_No response_

### ROCm Component

_No response_

## 评论 (2)

### ppanchad-amd · 2025-07-11

Hi @sraikund16. Internal ticket has been created to assist with your issue. Thanks!

### systems-assistant[bot] · 2025-08-07

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/140

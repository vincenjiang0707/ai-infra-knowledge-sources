# [Issue #1254] [Issue]: Unexpected fallthrough?

source: https://github.com/ROCm/rccl/issues/1254
state: closed | updated: 2024-10-29T21:49:27Z
labels: 

## 正文

### Problem Description

There is an undocumented fallthrough [here](https://github.com/ROCm/rccl/blob/9cbb3da224de813bf1f2356b4431f7b375ee6d35/src/misc/msccl/msccl_lifecycle.cc#L520):
```
      threadLocalStatus.groupStatus = mscclGroupUnsupportedOp;
      NCCLCHECK(mscclFallBackSavedParams());
    case mscclGroupUnsupportedOp:
      NCCLCHECK(mscclFallBackSavedParams());
      break;
```
This looks like a bug. Is the fallthrough intentional (mark with `[[fallthrough]]`) or should it be a `break`?

### Operating System

N/A

### CPU

N/A

### GPU

AMD Instinct MI300X

### ROCm Version

ROCm 6.1.0, ROCm 6.0.0, ROCm 5.7.1, ROCm 5.7.0, ROCm 5.6.0, ROCm 5.5.1, ROCm 5.5.0

### ROCm Component

_No response_

### Steps to Reproduce

Code issue

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

N/A

### Additional Information

_No response_

## 评论 (1)

### corey-derochie-amd · 2024-10-29

This fix will be present in ROCm 6.4.

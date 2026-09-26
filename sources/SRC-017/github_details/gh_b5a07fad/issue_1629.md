# [Issue #1629] NCCL RAS Structured Output

source: https://github.com/NVIDIA/nccl/issues/1629
state: closed | updated: 2026-08-18T14:33:27Z
labels: question, implemented

## 正文

NCCL RAS == great feature thank you!
https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting/ras.html

I was wondering if there are any plans to provide structured output (easily programatically parsed) eg: json, csv or similar which would be useful for monitoring purposes.


## 评论 (2)

### kiskra-nvidia · 2025-03-03

We're glad to hear you like it!

Yes, we are planning to provide optional structured output (most likely JSON) but we have no ETA for when it might be available.

### kiskra-nvidia · 2026-04-15

JSON output was added in 2.28.7; closing.

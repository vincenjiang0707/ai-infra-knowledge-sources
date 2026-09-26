# [Issue #166] UCX Version Checking

source: https://github.com/ai-dynamo/nixl/issues/166
state: closed | updated: 2026-04-17T17:16:55Z
labels: enhancement

## 正文

Add checks when creating UCX backend to ensure the library is compatible with NIXL. Multiple installs, or version limitations should be explicitly communicated to use. Examples:

- Until UCX is decoupled from our wheel, linked version of UCX should always be known and compared against 

- UCX <=1.18, gdr_copy bug, no multi-GPU support, no EFA support
- UCX <=1.17, cuda_ipc not supported, no NVLink
- UCX <=1.13, unsupported entirely



## 评论 (1)

### aknvda · 2026-04-17

@brminich said this issue is not needed and should be closed. Closing this issue with reference to https://github.com/ai-dynamo/nixl/pull/1529#issuecomment-4269746830

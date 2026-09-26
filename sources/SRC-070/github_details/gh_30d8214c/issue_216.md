# [Issue #216] Question: planned support for Geforce GPUs (at least Blackwell sm_12x)..

source: https://github.com/deepseek-ai/DeepGEMM/issues/216
state: open | updated: 2025-12-05T09:12:38Z
labels: 

## 正文

Hi,
altough Geforce Ada (sm_89) also has fp8 tensor core support and fp8 it's supported on cutlass since very recently tough (4.0 or 4.1 I think)..
thanks..

## 评论 (1)

### LyricZhao · 2025-12-05

Sorry, as we don't have SM89/120 devices, we don't have plans or people to support this. From my perspective, adding a new architecture support is hard for us to maintain, e.g. the GEMM heuristics are hard to cover all archs. So we encourage the OSS community makes a fork and supports it. The main repo is always using the computation center GPUs.

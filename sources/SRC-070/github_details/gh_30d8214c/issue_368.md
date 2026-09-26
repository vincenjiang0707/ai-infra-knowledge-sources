# [Issue #368] question about tmem barrier

source: https://github.com/deepseek-ai/DeepGEMM/issues/368
state: open | updated: 2026-06-29T16:00:25Z
labels: 

## 正文

I have a question about the comment here:

https://github.com/deepseek-ai/DeepGEMM/blob/54e22612409371d6364144b69086735beb54e98b/deep_gemm/include/deep_gemm/impls/sm100_fp8_fp4_mega_moe.cuh#L269

Since TMEM is consumed by both CTAs, the next line uses 2 * kNumEpilogueThreads. Shouldn't this barrier therefore use arrive at all CTAs instead?

Conversely, for tmem_full_barrier above, it seems that only the leader CTA calls arrive. Is my understanding correct?

## 评论 (1)

### Rachmanino · 2026-06-29

When both CTA complete tcgen05_ld from TMEM, they arrive on leader CTA's tmem_empty_barrier to signal that their TMEM are both free, and is ready for next tcgen05mma.
When leader CTA's mma warp issues tcgen05mma, it issues tcgen05 commit on both CTA's tmem_empty_barrier, so that they can wait on their own mbarrier for tcgen05mma completion.

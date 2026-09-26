# [Issue #2288] [Question]: Should the automatic Blackwell AllGather CE path reject sysmem-backed symmetric windows?

source: https://github.com/NVIDIA/nccl/issues/2288
state: closed | updated: 2026-08-07T01:31:52Z
labels: question

## 正文

### Question

Hi NCCL team,
While reviewing the CE collective selection logic in taskAppend() on the current master branch, I noticed that the two CE selection paths use different eligibility conditions.
The main CE path rejects symmetric windows containing host-backed cuMem segments. However, the automatic CE optimization for large Blackwell AllGather operations does not appear to perform the same check.
As a result, when the send or receive window contains a sysmem-backed segment, the main CE path falls back, but the automatic Blackwell AllGather path may still select CE. This automatic path also does not require NCCL_CTA_POLICY_ZERO.
Relevant source:
https://github.com/NVIDIA/nccl/blob/master/src/enqueue.cc#L3043-L3115
Commit 7416f22 was introduced to disallow elastic buffers in regular collective and RMA paths. It added sysmem-segment checks to the main CE path and the symmetric scheduler, but the automatic Blackwell AllGather CE path was not updated:
https://github.com/NVIDIA/nccl/commit/7416f22cb7b5c70ea841015885249ae332afc031
Could you please clarify:
Is the automatic Blackwell AllGather CE path intended to support symmetric windows containing host-backed cuMem segments?
If not, should this path also reject windows containing sysmem segments?
Is bypassing NCCL_CTA_POLICY_ZERO intentional for this automatic Blackwell optimization?
My expectation is that CE eligibility should be consistent between the two paths, and collectives using sysmem-backed symmetric windows should fall back unless that memory type is explicitly supported by the CE implementation.

## 评论 (4)

### xiaofanl-nvidia · 2026-07-19

+ @bhramesh-nvidia to review and discuss with the team. 

+CC @kgioioso , @zhenhaohe 

### bhramesh-nvidia · 2026-07-21

@lukeshi-code Thanks for reporting this! Answering your questions below.

1. Both CE selection paths should reject operations when either symmetric window contains a host-backed cuMem segment. The automatic Blackwell AllGather path currently lacks this eligibility check, so that is something we will fix.

2. NCCL_CTA_POLICY_ZERO is an opt-in policy requesting CE whenever CE is supported, primarily to minimize SM consumption (even when that may not be the most performant). The automatic Blackwell AllGather route is a separate performance optimization: under its assumptions, CE is expected to outperform the kernel implementation. Therefore, it intentionally does not require NCCL_CTA_POLICY_ZERO.

Please let me know if you have any more questions.

### lukeshi-code · 2026-07-22

Thanks for the clarification. Just to confirm my understanding:  
NCCL_CTA_POLICY_ZERO is an opt-in policy that prefers CE whenever the operation is eligible, even if CE may not provide the best performance.  
The automatic Blackwell AllGather path selects CE without requiring NCCL_CTA_POLICY_ZERO, but only when its specific conditions are satisfied.  
Both paths eventually use the same CE implementation, and NCCL_CTA_POLICY_ZERO only affects path selection; it does not change how the CE collective is executed or whether it uses SM CTAs.
Is this interpretation correct?

### bhramesh-nvidia · 2026-08-06

Yes, the blackwell allgather path uses the same underlying CE implementation. We've also pushed a fix for the missing sysmem checks [(commit)](https://github.com/NVIDIA/nccl/commit/8e110544489b1be0c9ca569485c61ad3a8045504) that will go into the upcoming v2.31 release. Thanks for reporting the bug!

# [Issue #691] [Proposal] Adding HybridEP compatibility with newer NVSHMEM versions

source: https://github.com/deepseek-ai/DeepEP/issues/691
state: open | updated: 2026-09-19T09:27:07Z
labels: 

## 正文

On the main branch v1.x, there was runtime timeout when NVSHMEM modified the way default qpairs were stored by introducing a QP-specific APIs (starting ~3.5.19). It was discussed in issue #553 , and subsequently PR #564 was merged to allow DeepEP to work with the newer NVSHMEM versions. Can those patches (since moved to legacy in the main branch) also be applied to `hybrid-ep`? I have a case to use hybrid ep with a newer NVSHMEM version.

## 评论 (1)

### 0z5a · 2026-09-19

I’d be happy to take this.
@youngjeong46 

I think the safest scope is to port the compatibility approach from #564 into hybrid-ep, rather than changing the HybridEP communication design.

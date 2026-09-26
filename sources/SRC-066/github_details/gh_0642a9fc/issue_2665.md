# [Issue #2665] [QST]Question about tma load for weights in example92: Is swizzling required?

source: https://github.com/NVIDIA/cutlass/issues/2665
state: closed | updated: 2026-09-17T17:00:06Z
labels: question, ? - Needs Triage, inactive-30d, inactive-90d

## 正文

Hi,
I have a question regarding the use of tma load for weights in example92, which focuses on MoE kernels for the Blackwell SM100 architecture.
I've noticed that the example utilizes tma load to fetch the weights. However, I couldn't find an explicit swizzling mechanism being applied to the weights in the code.
My question is:
Is it necessary to apply swizzling to the weights when using tma load in this particular context (example92)? I understand that swizzling is often employed to avoid shared memory bank conflicts, but I'm unsure if it's implicitly handled or intentionally omitted in this case.
If swizzling is indeed recommended, could you please provide some guidance or point me to the relevant part of the code where this should be implemented?
Thank you for your time and clarification.


## 评论 (4)

### github-actions[bot] · 2025-10-23

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### CalebDu · 2025-11-14

Hello @zhenxl, swizzling mode(such as Swizzle64B, Swizzle128B, etc) for SMEM is chosen in `CollectiveBuilder` by given tile size and data type.
https://github.com/NVIDIA/cutlass/blob/bd96096d58e4886e204cd1d71a385ca73e7719b8/include/cutlass/gemm/collective/builders/sm100_common.inl#L79-L82
After  swizzling mode for SMEM  selected, `make_tma_copy_atom` will create` TMA descriptor` by swizzling mode, data type and tile size.,etc.
https://github.com/NVIDIA/cutlass/blob/bd96096d58e4886e204cd1d71a385ca73e7719b8/include/cute/atom/copy_traits_sm90_tma.hpp#L1115-L1144
You can compile debug  build and trace how tma descriptor is created by breakpoint.

### github-actions[bot] · 2025-12-17

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-03-17

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

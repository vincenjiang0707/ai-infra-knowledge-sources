# [Issue #2805] [QST] Details of Auto Schedule Execution Strategy on Blackwell

source: https://github.com/NVIDIA/cutlass/issues/2805
state: closed | updated: 2026-09-24T16:54:31Z
labels: question, ? - Needs Triage, inactive-30d, inactive-90d

## 正文

On the Blackwell architecture, which is preferred to use Auto Schedule. When running GEMM with Auto Schedule, how many SMs does the scheduler actually assign to the kernel? Does Auto Schedule internally make use of Distributed Shared Memory (DSMEM), and is there a way to inspect this?

Background:
I am currently running into an issue on Blackwell where I explicitly set cluster<_1, _1, _1>, so the kernel should be using only a single CTA cluster. However, when debugging and printing out the shared memory addresses, it appears as if two clusters are involved.

This makes me wonder:

1. Does Auto Schedule internally change the number of SMs assigned to the kernel?

2. Can Auto Schedule implicitly increase the number of clusters, even when the user specifies cluster<1,1,1>?

3. If DSMEM is being used implicitly, how can we confirm or inspect this behavior?

Any clarification on how Auto Schedule interacts with SM assignment and cluster configuration on Blackwell would be greatly appreciated.

## 评论 (2)

### github-actions[bot] · 2025-12-24

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-03-24

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

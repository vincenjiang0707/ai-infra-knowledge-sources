# [Issue #2775] [QST] Why No Threadfence in semaphore.release for Serial Splitk GEMM

source: https://github.com/NVIDIA/cutlass/issues/2775
state: closed | updated: 2026-09-14T16:47:53Z
labels: question, ? - Needs Triage, inactive-30d, inactive-90d

## 正文

When implementing General Matrix Multiplication (GEMM) with a serial Splitk architecture, we have observed that the semaphore.release function in the current code does not invoke a threadfence. However, we are concerned about whether data inconsistency issues may arise in a multi-threaded environment. Is this design reasonable? Could it lead to data visibility anomalies? If not, what is the synchronization guarantee logic it relies on?

## 评论 (2)

### github-actions[bot] · 2025-12-14

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-03-14

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

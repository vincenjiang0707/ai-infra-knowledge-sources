# [Issue #2700] [QST]How to choose CopyAtom about SM100_TMEM

source: https://github.com/NVIDIA/cutlass/issues/2700
state: closed | updated: 2026-09-14T16:47:52Z
labels: question, ? - Needs Triage, inactive-30d, inactive-90d

## 正文

**What is your question?**
hello，I am using SM100a TMEM to complete my gemm, but i do not konw how to choose a appropriate CopyAtom. For example, i do not know the difference of SM100_TMEM_LOAD_16dp128b2x and SM100_TMEM_LOAD_32dp128b2x，there is any plan to write something aoubt this in document? Thank you!

## 评论 (3)

### CalebDu · 2025-11-14

You can refer [PTX doc](https://docs.nvidia.com/cuda/parallel-thread-execution/#tcgen05-memory-layout). There are figures to demonstrate `tcgen05.ld/st` instruction.
You also can refer how Cutlass choose tmem load atom.
https://github.com/NVIDIA/cutlass/blob/bd96096d58e4886e204cd1d71a385ca73e7719b8/include/cutlass/epilogue/collective/builders/sm100_builder.inl#L593-L712

### github-actions[bot] · 2025-12-14

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-03-14

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

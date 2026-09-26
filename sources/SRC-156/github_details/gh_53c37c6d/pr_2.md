# [PR #2] fix tcgen05.cp wiki

source: https://github.com/mit-han-lab/KernelWiki/pull/2
state: closed | updated: 2026-05-31T14:40:10Z
labels: 

## 正文

cc @DongyunZou  @Lyken17
fixes https://github.com/mit-han-lab/KernelWiki/issues/1

## 评论 (1)

### DongyunZou · 2026-05-31

Thanks for catching this, and sorry for the incorrect statement in the wiki. You’re right that `tcgen05.cp` copies from SMEM to TMEM rather than between TMEM regions.
I’ll merge this PR first and follow up with a small cleanup if needed to align the example/comment with the PTX syntax. Thanks again for the fix.

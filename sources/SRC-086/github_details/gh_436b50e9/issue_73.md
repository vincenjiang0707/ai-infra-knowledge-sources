# [Issue #73] Medusa 1 and 2 speed up

source: https://github.com/FasterDecoding/Medusa/issues/73
state: closed | updated: 2024-01-25T03:01:00Z
labels: 

## 正文

The difference between Medusa-1 and Medusa-2 is just training strategy. Why the two methods can lead to different speed up?

## 评论 (2)

### ctlllll · 2024-01-24

Thanks for your interest! Yes, they are just different training strategies, but they lead to different prediction abilities of Medusa heads, i.e., in Medusa-2, the backbone model is trained together with Medusa heads, therefore improving Medusa heads' prediction, which can translate to better speedup.

### LotuSrc · 2024-01-25

Thanks for your reply.

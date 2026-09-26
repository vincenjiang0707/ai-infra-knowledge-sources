# [Issue #2239] [Question]: ProxyOp and ProxyStep in NCCL Inspector

source: https://github.com/NVIDIA/nccl/issues/2239
state: open | updated: 2026-08-14T18:16:08Z
labels: question

## 正文

### Question

Are there any plans to add NCCL Inspector tracking for these events?

## 评论 (5)

### xiaofanl-nvidia · 2026-06-23

++ @rishdas @armratner 

### ahmd-k · 2026-06-30

Any updates?

### rishdas · 2026-08-10

Apologies for late reply yes will most likely try to do it 2.33/2.34 release time frame as an option.
We are also open to accepting pull request e.g. https://github.com/NVIDIA/nccl/pull/2304.
Thank you

### LYAccc · 2026-08-14

 Hi @rishdas @ahmd-k , I’d like to take this on if no one is already working on it.
 
   I’m thinking of starting with opt-in ProxyOp/ProxyStep support in the Inspector’s verbose JSON output. Would that be a reasonable first scope?

Thanks!

### rishdas · 2026-08-14

yes that would and I will be happy to to review.
@xiaofanl-nvidia , @gcongiu, @shamisp

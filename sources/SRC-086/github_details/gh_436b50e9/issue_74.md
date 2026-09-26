# [Issue #74] Question about Heads warmup

source: https://github.com/FasterDecoding/Medusa/issues/74
state: open | updated: 2024-01-24T13:49:06Z
labels: 

## 正文

Hi, I'm not an expert, so this might be a stupid question, but I have a question about the Heads warmup part of the Medusa paper. In that part it is mentioned to train the backbone first with medusa-1 loss in the first stage. When I read the paper referenced in that part(https://arxiv.org/abs/2202.10054), my guess is that it would be better to train the medusa head first. My questions are as follows 
1. why fine-tune the backbone first? 
2. does it really work to train backbone with medusa-1 loss while medusa head is initialized to 0 and frozen, since the output of medusa head would be 0 anyway? why?



## 评论 (1)

### ctlllll · 2024-01-24

Sorry, it's a typo. It should be only training the heads first and then together. We'll fix it in the next version, and thanks so much for pointing it out!

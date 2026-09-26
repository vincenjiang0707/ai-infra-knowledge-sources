# [Issue #1231] CoQA's implementation only predicts the last answer of each text

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/1231
state: open | updated: 2026-09-05T14:56:03Z
labels: bug, good first issue

## 正文

For CoQA, in coqa/utils.py, only the last answer of each text (i.e. the answer for the last turn_id, with all the previous questions and answers in the context window) is predicted. On the website of the authors of CoQA, they seem to consider all turn_id (see their [sample prediction file](https://nlp.stanford.edu/data/coqa/drqa-pgnet-coqa-dev-hist1.txt.json) where they have answers for every turn_id, and the official [evaluation script](https://nlp.stanford.edu/data/coqa/evaluate-v1.0.py) where they do an average of the result for every turn_id).

Here is an excerpt from the paper (https://arxiv.org/pdf/1808.07042.pdf) : 

![image](https://github.com/EleutherAI/lm-evaluation-harness/assets/47578089/5eb6f6ea-17bd-4ce3-8e6c-15a98d86ca2d)

I haven't found how it's implemented with other popular LLM evaluation frameworks, but I'm pretty sure that predicting only the answer to the last question is not what is intended by the authors of CoQA.

## 评论 (2)

### StellaAthena · 2024-01-01

I think it probably makes sense to support both versions of this task, but we should make it clear that the one described in the OP is the official one.

### Arin016 · 2026-09-05

Opened #4104 implementing this, following @StellaAthena's direction: default `coqa` now evaluates every turn (v4.0) with a `coqa_last_turn` legacy variant kept. Verified expansion/targets/no-leak on the real split. Happy to adjust based on review.

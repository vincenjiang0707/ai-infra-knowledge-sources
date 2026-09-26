# [Issue #679] [RFC]:

source: https://github.com/vllm-project/speculators/issues/679
state: closed | updated: 2026-06-29T13:54:32Z
labels: RFC

## 正文

### Motivation.

I would like to propose adding dspark support to vllm-project/speculators.

dspark has already been integrated in DeepSpec, and the implementation can be used as a reference:
https://github.com/deepseek-ai/DeepSpec

### Proposed Change.

DSpark is a draft model for speculative decoding that predicts blocks of tokens
from randomly sampled anchor positions, using cross-attention over target model
hidden states. It generalizes EAGLE-style feature-level prediction from
sequential (one position ahead) to parallel (full blocks from any position).

### Any Other Things.

# References
DSpark paper: https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf
DSpark code: https://github.com/deepseek-ai/DeepSpec

## 评论 (1)

### dsikka · 2026-06-29

See: https://github.com/vllm-project/speculators/pull/678

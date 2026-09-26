# [Issue #39] [New feature] More sampling schemes

source: https://github.com/FasterDecoding/Medusa/issues/39
state: closed | updated: 2024-01-24T14:00:19Z
labels: enhancement

## 正文

I am concerning that top-k greedy decoding may sacrify writing creativity. Is there any experiment analyzing if random sampling k tokens with necleus sampling works?

## 评论 (2)

### ctlllll · 2023-09-19

Thanks for your interest! In principle, this along with other sampling schemes should work (we can simply follow the importance sampling scheme in the speculative decoding paper), but we didn't implement it. I'll add this to our roadmap. If you are interested in implementing this, this will mainly involve `evaluate_posterior` function in `Medusa/medusa/model/utils.py` and `medusa_generate` function in `Medusa/medusa/model/medusa_model.py` :)

### ctlllll · 2024-01-24

Added in v1.0 (e.g., https://github.com/FasterDecoding/Medusa/blob/93bee11f14e3a5403a46aa9dce36102d3ec8d0b9/medusa/model/utils.py#L196)

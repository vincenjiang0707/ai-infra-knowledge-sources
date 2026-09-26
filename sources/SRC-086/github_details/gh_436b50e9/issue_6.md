# [Issue #6] Quesitons about the Performance

source: https://github.com/FasterDecoding/Medusa/issues/6
state: closed | updated: 2023-09-13T23:46:43Z
labels: 

## 正文

1) Is the baseline in your graph using greedy decoding or beam search?
2) What is the performance of your decoding method in the evaluation dataset? How large is the performance regression?

## 评论 (1)

### ctlllll · 2023-09-13

Hey Adam,

1. The baseline is greedy decoding/sampling decoding, depending on the temperature configuration from the original [MT bench](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge). But you can think of it as greedy decoding, as the speeds are the same.
2. We have a [figure](https://sites.google.com/view/medusa-llm#h.ybsda3p1jr2)(Choice of threshold in typical acceptance) in the ablation study part of the blog. Please check it out :)

I'll close this issue, feel free to reopen it if you have further questions :)


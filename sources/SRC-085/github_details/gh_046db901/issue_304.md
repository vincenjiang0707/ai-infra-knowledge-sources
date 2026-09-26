# [Issue #304] How can I test benchmark(ex. mmlu) for checking accuracy of eagle 3 ?

source: https://github.com/SafeAILab/EAGLE/issues/304
state: closed | updated: 2025-10-20T07:56:40Z
labels: 

## 正文

Since evaluation code files in EAGLE github only calculate speed up, I want to compare accuracy of benchmark  between original model and eagle-attached model. Is there evaluation code that I didn't find ? Or should I make new evaluation code for calculating accuracy of eagle3?

## 评论 (1)

### hongyanz · 2025-10-20

The EAGLE series are mathematically guaranteed to maintain the output distribution of the target model (module deterministic inference, see https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/). You can also make your own code to test the accuracy.

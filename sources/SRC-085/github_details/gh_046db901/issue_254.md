# [Issue #254] Question about EAGLE-3 paper

source: https://github.com/SafeAILab/EAGLE/issues/254
state: closed | updated: 2025-07-12T19:00:29Z
labels: 

## 正文

In the EAGLE-3 paper, it says "In Step 1, with the prefix “How can”, we reuse ghow and gcan from the target model. In Step 2, the prefix becomes “How can I”. Ideally, we would reuse ghow, gcan, and gI from the target model. However, this is not possible because the token “I” has not yet been checked by the target model, and we cannot obtain gI." 

Is the paper saying the only reason gI was not used is because token "I" has not been checked, and that is why gI cannot be obtained, or is there an additional reason why gI cannot be obtained?

## 评论 (1)

### hongyanz · 2025-07-09

You can only get "a_l" rather than "g_l" if the drafted token "l" has not been checked yet.

# [Issue #83] Question about quantization.

source: https://github.com/dropbox/hqq/issues/83
state: closed | updated: 2024-06-13T09:26:23Z
labels: 

## 正文

Is there randomness in the quantization process? As I get different eval results when I run the same model multiple times.

## 评论 (2)

### mobicham · 2024-06-12

No, it's deterministic. What eval are you running ?

### mxjmtxrm · 2024-06-13

The randomness is from evaluation. Thank you.

# [Issue #289] Questions about Lossy Decoding with EAGLE-3

source: https://github.com/SafeAILab/EAGLE/issues/289
state: closed | updated: 2025-09-03T15:16:36Z
labels: 

## 正文

In the code, there are signs that lossy decoding was previously supported, with a threshold parameter in the Model class, and description of a posterior_threshold parameter in evaluate_posterior() in utils.py

Is there any remaining support for lossy decoding in EAGLE-3, if not, is it possible to integrate it manually? Also, is there any way of testing out an EAGLE drafter by itself, without verification from the target model?

## 评论 (1)

### hongyanz · 2025-09-03

In the EAGLE-1 to EAGLE-3, we never support lossy decoding. We are interested in lossless decoding.

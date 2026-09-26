# [Issue #809] [FEATURE] add support for speculative speculative decoding

source: https://github.com/vllm-project/speculators/issues/809
state: open | updated: 2026-07-20T07:47:22Z
labels: 

## 正文

source - https://github.com/tanishqkumar/ssd

quoting from repo

```
SSD is a new type of speculative decoding (SD). In normal SD, a small and fast model guesses the next few tokens that a larger slower model may generate, and the large model then verifies them in one forward pass: drafting and verification happen one after the other on the same hardware.

In SSD, they happen in parallel, on distinct hardware. The small model anticipates likely verification outcomes in advance, and speculates for all of them at once. If it guessed correctly, the speculation can be returned immediately so drafting overhead is eliminated entirely.
```

would you be interested in supporting this? if yes, id like to help raise a PR after we discuss some architecture implementations.

## 评论 (1)

### JINO-ROHIT · 2026-07-20

cc: @orestis-z @shanjiaz 

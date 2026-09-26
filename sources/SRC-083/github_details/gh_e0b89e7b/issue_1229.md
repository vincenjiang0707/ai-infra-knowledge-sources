# [Issue #1229] 8bit CAME optimizer

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1229
state: open | updated: 2026-06-29T17:34:15Z
labels: Optimizers

## 正文

### Feature request

I would really love a 8bit version of CAME optimizer being supported.

### Motivation

If the implementation is possible.

### Your contribution

Pixart Sigma model was trained with CAME instead of Adam, so its a really good optim

## 评论 (3)

### turbo-boo · 2025-03-23

yeah, I agree

### rpathade · 2026-05-13

I’d be interested in taking a first pass at this and checking how CAME’s factored row/column and residual states can fit into the existing bitsandbytes 8-bit optimizer abstractions.

### yanfeiwong · 2026-06-29

I've actually implemented one here: https://github.com/yanfeiwong/adafactor-8bit#-came-confidence-guided-updates

It's built on top of Adafactor rather than being a standalone CAME optimizer, but with a bit of configuration you can make it behave like an 8-bit CAME (more accurately, 4-bit β1 + 8-bit β2 + 8-bit β3).

It's still pretty new and needs more testing, but feel free to check it out!

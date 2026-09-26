# [Issue #752] How to implement 1F1B pipeline parallelism in Jax?

source: https://github.com/AI-Hypercomputer/maxtext/issues/752
state: closed | updated: 2026-04-28T18:20:14Z
labels: feature request

## 正文

Not GPipe. Run pipeline forward meanwhile backward.

## 评论 (4)

### gobbleturk · 2024-08-28

We are still looking into this in the open source side! Likely at least 6 months away

### sbhavani · 2024-12-09

Is this still in progress for maxtext?

### gobbleturk · 2024-12-09

Yes this is still something we are considering, likely requires a paradigm shift (multiple programs multiple data) to support

### gobbleturk · 2026-04-28

One way to implement this in jax is using mpmd partir/shardy - see https://github.com/openxla/shardy

We will work on integrating this into maxtext but you can use this as a reference

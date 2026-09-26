# [Issue #518] Add TheoremQA

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/518
state: open | updated: 2026-09-09T00:47:22Z
labels: help wanted, feature request, good first issue

## 正文

This is awesome work and we should include it. It may be a bit tricky as it involves external calls to the WolframAlpha API for answer evaluation though.

https://github.com/wenhuchen/TheoremQA

## 评论 (5)

### rishabbala · 2023-08-14

Hey @StellaAthena wondering if this issue is still open/required. If so I can take it on. Could you give me a brief overview of what has to be done

### ShayekhBinIslam · 2024-04-01

@lintangsutawika I am interested in contributing here.

### lintangsutawika · 2024-04-01

That's awesome! Feel free to start a PR anytime. 

### KahnSvaer · 2025-01-15

If this is still open can I start work on this @baberabb 

### bongho · 2026-09-09

@baberabb mind if I pick this up? The assignment to @ShayekhBinIslam is from 2024-04 with no PR since. `TIGER-Lab/TheoremQA` is parquet-native (800 test rows), so it loads on `datasets` 5.x without a script. Two things I'd rather settle first: 53 of the 800 rows carry a `Picture` column a text-only task can't answer, and touching that column raises `ImportError` without Pillow, so I'd drop it and keep the 747 text-only rows; answers are typed (`float`, `integer`, `bool`, `list of integer`, `option`, `list of float`), so I'd grade per `Answer_type` with a relative tolerance on floats. Shout if you'd rather it went another way.


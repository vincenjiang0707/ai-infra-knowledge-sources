# [Issue #3666] Add SimpleQA (OpenAI factuality benchmark)

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3666
state: open | updated: 2026-09-09T00:47:21Z
labels: 

## 正文

## Gap

[SimpleQA](https://openai.com/index/introducing-simpleqa/) — OpenAI's short-form factuality benchmark released in October 2024 — has no official task in lm-evaluation-harness. It is now widely cited as the standard for measuring parametric factual accuracy in LLMs and is used by labs across the industry, yet there is no way to evaluate against it using this harness.

## What SimpleQA is

- **4,326 fact-seeking questions**, each with exactly one unambiguous, verifiable short answer
- Designed to measure **factual recall** independently from reasoning ability
- Tracks three states: *correct*, *incorrect*, and *not attempted* — which gives a richer picture of reliability than accuracy alone
- Dataset is publicly available at `basicv8vc/SimpleQA` on HuggingFace

## Proposed fix

Add `lm_eval/tasks/simpleqa/` with:
- `simpleqa.yaml` — task config (`generate_until`, zero-shot by default, matching the paper's setup)
- `utils.py` — deterministic string normalization + scoring (exact match, token F1, not_attempted)
- `README.md` — description, metrics, citation, usage

This is addressed in the accompanying PR.

## 评论 (4)

### bongho · 2026-06-03

Hi, I'm interested in picking up SimpleQA for the harness — I'd like to use it for some factuality evaluation work and think it would be a valuable addition.

@sarthakkgupta opened PR #3667 addressing this back in March, but it's been inactive since 2026-03-31 (~2 months with no further commits or comments).

@sarthakkgupta — are you planning to continue? Happy to help with review or rebases if so. If you'd prefer to hand it off, I'd be glad to carry the work forward with you credited as Co-authored-by on the eventual merge.

If there's no response in ~10 days, I'll check in with the maintainers (@baberabb) on whether to proceed with a fresh implementation building on the original work.

Thanks!


### sarthakkgupta · 2026-06-04

@bongho, I will be glad to collaborate on this. You can proceed with rebase.

Thanks.

### bongho · 2026-06-11

@sarthakkgupta thanks for the go-ahead! Opened #3832 carrying your implementation forward, rebased onto `main` with your authorship preserved.

One fix along the way: the config had `test_split: train`, but `basicv8vc/SimpleQA` only ships a `test` split, so the task hit `KeyError: 'train'` on load — corrected to `test`. Tests pass. Happy to credit you however you prefer. Thanks again!


### bongho · 2026-09-09

Three open PRs on this now: #3667 (@sarthakkgupta's original), #3832 (my rebase of it, CI green), and #3888. All three approximate the paper's GPT-4o judge with string matching, which is probably the actual open question here rather than the code. @baberabb do you want a string-match contract in-tree now, or hold for an LLM-judge path? Happy to close #3832 in favour of whichever you prefer — three open PRs on one task isn't helping anyone.


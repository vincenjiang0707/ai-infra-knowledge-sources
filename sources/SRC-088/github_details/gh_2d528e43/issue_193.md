# [Issue #193] Implement TyDiQA

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/193
state: closed | updated: 2026-08-27T13:02:37Z
labels: help wanted, feature request, good first issue

## 正文

https://github.com/google-research-datasets/tydiqa

## 评论 (4)

### LakshyaChaudhry · 2026-02-11

Hi, I'd like to work on this. I'll implement TyDiQA as a YAML-based task covering all 11 languages using the existing HuggingFace dataset. Will open a PR soon.

### devesssi · 2026-03-14

@LakshyaChaudhry is this done? 

### bongho · 2026-04-16

Hi @devesssi and @LakshyaChaudhry — PR #3677 implements TyDiQA Gold Passage for all 11 typologically diverse languages. It follows current project conventions (YAML-based task config, HuggingFace dataset, no external dependencies). All checklist items complete. Would love any feedback from maintainers!

### bongho · 2026-08-25

@LakshyaChaudhry are you still on this? If not I'll pick it back up — I had #3677 open for it and closed it unreviewed.

One correction to my own comment above: the Gold Passage task covers **9** languages, not 11. `secondary_task` has no Japanese or Thai rows in either split:

```python
>>> ds = load_dataset("google-research-datasets/tydiqa", "secondary_task", split="validation")
>>> Counter(r.split("-")[0] for r in ds["id"])
{'arabic': 921, 'russian': 812, 'finnish': 782, 'telugu': 669, 'indonesian': 565,
 'swahili': 499, 'english': 440, 'korean': 276, 'bengali': 113}   # 5077 total
```

So `tydiqa_goldp_ja` / `_th` would register tasks that always evaluate zero documents. Opening a PR shortly with the 9 that exist.


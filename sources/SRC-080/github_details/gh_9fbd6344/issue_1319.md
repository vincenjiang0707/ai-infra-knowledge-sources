# [Issue #1319] Logical conflict between data loading and collation.

source: https://github.com/NVIDIA/Model-Optimizer/issues/1319
state: closed | updated: 2026-06-19T04:37:58Z
labels: question, stale, waiting for feedback

## 正文

In _load_ultrachat_conversations, the messages are constructed using only the user role:
msgs = [{"role": "user", "content": prompt}]

However, LanguageDataCollator.__call__ implements a mandatory check that skips any sample missing an assistant turn:
```python
if not any(m.get("role") == "assistant" for m in messages):
    continue
```

So, this causes all samples to be skipped during training because no assistant responses exist in the pre-processed data. Is that right?

## 评论 (4)

### juhi10071998 · 2026-04-22

Hi @wenqibiao, thanks for bringing this up. Could you point to the file location where this is happening?

### wenqibiao · 2026-04-23

> Hi [@wenqibiao](https://github.com/wenqibiao), thanks for bringing this up. Could you point to the file location where this is happening?

ok. File location: 
```text
git branch: main
git commit: 010b220dc09890bf7646f8fad5b69fd0bc41ac5b
1) file A (_load_ultrachat_conversations): examples/dataset/make_dataset.py, line 282.
2) file B (LanguageDataCollator.__call__): modelopt/torch/utils/plugins/transformers_dataset.py, line 288.
```



### github-actions[bot] · 2026-06-05

Issue has not received an update in over 14 days. Adding stale label.

### github-actions[bot] · 2026-06-19

This issue was closed because it has been 14 days without activity since it has been marked as stale.

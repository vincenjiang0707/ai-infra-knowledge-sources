# [Issue #1850] [Help Wanted] Update `oneshot` args to match `*Arguments` config classes

source: https://github.com/vllm-project/llm-compressor/issues/1850
state: closed | updated: 2026-08-11T18:02:11Z
labels: good first issue, stale

## 正文

`src/llmcompressor/entrypoints/oneshot.py:oneshot` relists all the arguments from the `DatasetArguments, ModelArguments, RecipeArguments, TrainingArguments` class in `src/llmcompressor/args`.

However, it seem like a few arguments are missing or have different type hints or defaults. These should be updated to match. Missing arguments include `preprocessing_func, data_collator, raw_kwargs, max_train_samples, pipeline, tracing_ignore, sequential_targets` from the `DatasetArguments` class.

## 评论 (7)

### ArkaSanka · 2025-10-02

Please assign this to me, I am interested in looking into this.

### dsikka · 2025-10-02

Thank you!

### Etelis · 2025-10-21

If @ArkaSanka is not working on this, could you assign me? @dsikka 


### ArkaSanka · 2025-10-21

Hi @Etelis, I'm working on it, submitting the PR soon

### dsikka · 2026-02-13

Hi @ArkaSanka are you interested in working on this?

### ArkaSanka · 2026-02-13

Yes @dsikka, if you could getting the PR #1957, I can rebase it  

### github-actions[bot] · 2026-08-11

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!

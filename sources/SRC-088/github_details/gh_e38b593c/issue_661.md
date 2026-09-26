# [Issue #661] [RFC]: Flexible data source discovery

source: https://github.com/vllm-project/speculators/issues/661
state: closed | updated: 2026-07-02T18:34:39Z
labels: RFC

## 正文

### Motivation.

Training a speculator on local data currently requires either passing individual `.json`/`.jsonl` files or using a named preset from `DATASET_CONFIGS`.  Separately, Magpie and Nemotron are popular open instruction-tuning datasets that would be useful presets in `DATASET_CONFIGS`. Magpie is already referenced in our scripts under a local config dict, so promoting it to the shared registry unifies the two code paths.

### Proposed Change.

Extend `load_raw_dataset()` in `src/speculators/data_generation/preprocessing.py` to support a resolution chain. Today the function handles two cases (local `.json`/`.jsonl` file, or named preset). We should extend to:
1. **Local file** (existing) — match paths ending in `.json`/`.jsonl`.
2. **Local directory** (new) — recursively glob `*.json`/`*.jsonl` from the directory and load as one dataset.
3. **Named preset** (existing) — look up `DATASET_CONFIGS`.
4. **Arbitrary HuggingFace dataset** (new) — a `hf:` prefix loads any HF dataset ID directly, with optional `:<subset>:<split>` suffix.


### Any Other Things.

- All source types compose with mixed `--data` usage: `--data sharegpt --data /my/shards/ --data hf:nvidia/HelpSteer2 --data extra.jsonl`.
- For the `hf:` path, datasets not in conversations format will fail at the preprocessing stage with an actionable error with no silent data corruption.
- A future follow-up could add auto-detection of common HF schemas (instruction/response, prompt/completion, messages) and normalize them automatically, reducing the need for per-dataset `normalize_fn` boilerplate.
- Test coverage: integration tests with a temp directory of JSONL shards and a small public HF dataset would validate both new paths.

## 评论 (4)

### KKothuri · 2026-06-25

Looking into this. Will make the required changes and test

### KKothuri · 2026-06-26

I see that there is significant overlap with Issue #583 and PR #637. Will keep it discovery-only and separate from #637's normalization per your #583 scoping

### shanjiaz · 2026-06-26

> @KKothuri Assigned the issue to you. Feel free use #637 as a reference if you'd like but please only focuse on changes requested in this RFC. RFC #583 contains lots of good points. We're trying to separating it into smaller separate pieces. Feel free to reach out if you have any questions! 

### KKothuri · 2026-06-29

Hi @shanjiaz, raised a PR https://github.com/vllm-project/speculators/pull/675. Added a case for hf datasets with only split mentioned without subset. Let me know if I should change anything there. PTAL. Thank you.

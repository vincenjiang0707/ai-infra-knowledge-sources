# [Issue #583] [RFC]: Prepare-data ingestion & normalization

source: https://github.com/vllm-project/speculators/issues/583
state: open | updated: 2026-07-05T16:10:18Z
labels: RFC

## 正文

### Motivation.

`scripts/prepare_data.py` and the data_generation loaders accept a handful of hard-coded dataset presets plus a single local `.json/.jsonl` path, with bespoke per-dataset normalizers and ad-hoc role mapping. 
That makes it hard to: train on a local *bundle* (a directory of split/parquet files), combine several sources, point at an arbitrary HF dataset/split, or rerun safely (the old `--overwrite` left stale files and
could silently produce an empty dataset). Conversation schemas (`messages` vs
`conversations`, ShareGPT `from/value` vs OpenAI `role/content`) are also normalized inconsistently.


### Proposed Change.


Generalize ingestion so local bundles, configured presets, and mixed prompt/message
schemas all reduce to one normalized conversation format before preprocessing.
- **Ingestion order** in `load_raw_dataset`: local file → local directory bundle → named
  preset (`DATASET_CONFIGS`) → HF hub path with optional `":split"` or `":[split_1|...|split_n]"` suffix. Directories are discovered recursively, grouped by `(format, source)` to preserve each split/file's
  provenance, and concatenated on their common columns (non-shared columns dropped with a
  per-column warning; mixed parquet schemas grouped and reconciled). An internal
  `__speculators_source` column tracks provenance and is dropped before save.
- **Registry**: add `nemotron` (+ per-split variants), `codealpaca`, `magpie`; extend
  `DatasetConfig` with split tuples, `prompt`/`messages` field hints, and a
  `preprocessing_supported` guard for response-only presets. Generalize the per-dataset
  normalizers into small factories.
- **Normalization**: factor `_normalize_turn` out behind a `ROLE_ALIASES` table and rename
  a `messages` column to `conversations` when none exists.
- **Proportional sampling**: under `--max-samples`, select a subset proportionally by
  source so a bundle/multi-source mix is preserved rather than truncated. Sampling is
  global across sources (documented, with a hook for alternative policies).
- **Safety/correctness**: `--data` takes multiple space-separated sources; `--output`
  defaults to `./output`; `--overwrite` refuses to delete a directory containing
  non-artifact files, then does a clean rebuild; truncate `input_ids`/`loss_mask` to
  `max_length`; raise on an all-empty result unless `--allow-empty-output`.

### Any Other Things.

These are separable and can be split into smaller PRs if preferred (ingestion/bundles,
schema normalization, proportional sampling, rerun-safety). The sampling policy is global
across sources by design — can switch to per-input-equal/proportional.

## 评论 (3)

### shanjiaz · 2026-06-23

@imargulis Thanks for putting this together! For now we'd like to focus on three pieces, ideally as separate PRs:

  1. Schema normalization

The ROLE_ALIASES table approach makes sense, a declarative lookup is cleaner and easier to extend. We'd also want the column rename (messages → conversations) to happen automatically during ingestion rather than requiring per-dataset normalizer functions like `_normalize_ultrachat`. Extending DatasetConfig with field hints (conversations_column, prompt_column/answer_column) so normalizers can be generated from config instead of hand-written fits here too. Most of the hand-written normalizer functions in DATASET_CONFIGS would be replaced by config fields on DatasetConfig itself. I’d be careful with the multi-modal preprocessing tho, and prefer we handle that in a different PR

  2. Safety/correctness

The --overwrite hardening makes sense, input_ids/loss_mask truncation to max_length, and we should be raising on an all-empty result.

  3. Directory bundle discovery

Supporting --data /path/to/directory/ with recursive file discovery would be useful, we already accept multiple --data flags, so this is a natural extension for local data bundles.Adding nemotron and magpie to DATASET_CONFIGS would also be nice to have here.


### WindChimeRan · 2026-07-04

The normalization work is heading toward more generality than we need, which makes it fragile. I'd keep the shared pipeline minimal.

The useful split: role names ("human"→"user") are uniform across datasets — one shared table, centralize hard. 

Column layout (messages vs conversations, which field holds the turns) is per-dataset — don't build config hints for datasets we don't have yet. conversations_column has no user and already sprouted bugs. When we need to blend or reshape sources, a one-off script beats generalizing the shared pipeline.

Question:For future datasets, do they mostly just need a column pointed at the right name? If a lot are coming and they're that simple, the hint is worth building now. If they're occasional and each one's different, I'd hold off.

@imargulis @shanjiaz 

### imargulis · 2026-07-05

@WindChimeRan @shanjiaz 

Agreed — generalize later. Role names are uniform across datasets, so I'm keeping the
`ROLE_ALIASES` table + `_normalize_turn` and a single `messages→conversations` rename.
But column layout is per-dataset, so I've dropped the config-driven machinery
(`conversations_column`, `prompt_column`/`answer_column`, the normalizer factories); each
non-conversations schema stays a bespoke `normalize_fn` escape hatch (gsm8k, nemotron,
sharegpt4v). I'd rather add a factory when a real second prompt/answer-style case shows up
than carry speculative machinery now. #688 is trimmed to reflect this.

# [Issue #1055] [Feature request] Auto-generate a model card (`README.md`) for saved speculator checkpoints

source: https://github.com/vllm-project/speculators/issues/1055
state: open | updated: 2026-09-08T06:14:42Z
labels: 

## 正文

# [Feature request] Auto-generate a model card (`README.md`) for saved speculator checkpoints

## Motivation.

I trained DSpark draft models with Speculators and pushed the best checkpoint to the Hugging Face Hub. The upload works, but the repo has no `README.md`, so the model page is blank: no frontmatter, no link to the verifier, no usage snippet.

Checkpoints currently contain `config.json`, `model.safetensors`, `optimizer_state_dict.pt`, `train_command.txt` and `val_metrics.json`, plus `run.yaml` at the run root — but no `README.md`, and no model-card or hub-upload code exists in `src/` or `scripts/`.

Why it matters:

- **A speculator is useless without its verifier.** That link lives only in `speculator_config` inside `config.json`. Putting it in `base_model:` frontmatter makes the Hub render the relationship.
- **Discoverability.** Without `library_name`/`tags`, community speculators don't surface in Hub search or filtering.
- **The published RedHatAI cards set an expectation the library doesn't help users meet.** Hand-writing a card is exactly the step people skip.
- **Everything needed is already on disk:** architecture from `config.json`, training config from `run.yaml`, command/git SHA/package versions from `train_command.txt`, validation loss from `val_metrics.json`. This is templating over existing artifacts.

I couldn't find an existing issue for this — happy to close as a duplicate if I missed one.

## Proposed Change.

1. **Card generator** (`src/speculators/model_card.py`) that renders `README.md` from a checkpoint directory. `huggingface-hub` is already a base dependency, so `ModelCard`/`ModelCardData` covers this with no new deps.
2. **Emit during checkpointing** in `BaseCheckpointer.save_checkpoint`, so `checkpoint_best` is directly uploadable. Gated by `--model-card / --no-model-card`; never overwrite an existing `README.md` without an explicit flag.
3. **CLI entry point** `speculators model-card <checkpoint_dir>` for already-trained checkpoints, reused at the end of `speculators convert`.

Card contents:

- **Frontmatter:** `library_name: speculators`, `base_model:` (verifier from `config.json`), `tags:` (`speculative-decoding`, `vllm`, algorithm), `pipeline_tag: text-generation`.
- **Body:** vLLM usage snippet; architecture from `config.json` (including algorithm-specific fields like DSpark's `markov_rank`); training summary from `run.yaml`; reproduction command and environment from `train_command.txt`; validation metrics table (below); `acceptance.csv`/`perf_results.csv` when present.

**Validation metrics table.** `compute_metrics` already produces exactly the numbers a reader wants, and `val_metrics.json` persists them — they just never reach the card. Render them as markdown:

- A summary row: `accept_len_epoch` (expected accepted draft length), `accept_rate_epoch`, `full_acc_epoch`, `loss_epoch`.
- A per-position table from the `position_{i}_acc_epoch` keys, one row per draft slot, so readers can see acceptance decay across the block — the single most useful signal for choosing `num_speculative_tokens` at serve time.
- For DSpark, the confidence-head calibration metrics (`confidence_abs_error_epoch`, `confidence_cumprod_bias_epoch`).

## 评论 (1)

### LOGO127 · 2026-09-08

I'd be interested in working on this, subject to maintainer scope approval and whether anyone is already implementing it. I checked main at `3419401a380db305ed6493ba4680ad8a3c3e0e45` and found two integration details worth settling before coding:

- In `Trainer.maybe_update_best`, `save_checkpoint` runs before `save_val_metrics`; the regular checkpoint path also precedes validation. Generating a card only inside `save_checkpoint` could omit the current validation results. The generated card needs a post-metrics refresh path, while preserving user-authored README files.
- Following #1032, DSpark's `accept_len` and `eal` both include the verifier's bonus token but represent analytical rejection-sampling acceptance and greedy acceptance respectively. The card should label these separately and not present training validation metrics as measured serving acceptance or throughput.

The intended end state would cover the requested standalone generator/CLI, conversion reuse, and optional checkpoint integration, with tests for absent artifacts, existing README preservation, post-validation refresh and metric labels. A local-only generator would not upload anything; I'd also propose making raw command/environment inclusion explicit opt-in, since provenance may contain private paths or credentials. Missing metrics would remain missing, not become fabricated zeros.

Would you be open to this scope, and do you have a preferred policy for refreshing automatically generated cards after validation? I can keep rendering and training-lifecycle integration in separately reviewable commits while retaining the complete feature scope. No implementation or assignment is claimed yet. This source audit and proposal were prepared with AI assistance.


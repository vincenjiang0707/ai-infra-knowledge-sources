# [Issue #978] [RFC]: Surface the effective Muon LR when --muon-lr is left unset

source: https://github.com/vllm-project/speculators/issues/978
state: closed | updated: 2026-08-11T14:41:00Z
labels: RFC

## 正文

## Motivation

`train.py` silently derives `muon_lr = 10 * args.lr` when `--muon-lr` is not passed explicitly (`scripts/train.py:1308-1309`). This is documented in `--help` (`"Defaults to 10*lr"`, line 1286), but the *effective* value is never surfaced anywhere at runtime — not in the training logs, and not in `train_command.txt` (which records `sys.argv`, so an implicit default never appears there at all).

This caused real ambiguity across two independent training efforts on this codebase: when comparing a run that used `--muon-lr` explicitly against one that only passed `--lr` (relying on the 10x default), it was impossible to tell from the saved command alone whether the Muon LR had been independently tuned or was just riding the default multiplier. Resolving this required going back to the original ablation logs on a separate system to confirm intent. Since `--muon-lr` and `--lr` are otherwise-independent knobs feeding two separate optimizer instances (`torch.optim.Muon` and `torch.optim.AdamW`, see `src/speculators/train/optimizers.py:86-105`), this coupling is easy to miss, especially when only `--lr` is being swept in an ablation.

## Proposed Change

1. In `build_optimizers()` (`src/speculators/train/optimizers.py`), extend the existing `logger.info` call at line 80 (or add an adjacent one) to always log the resolved `muon_lr` and `lr` values being used, regardless of whether `--muon-lr` was passed explicitly or derived from the default.
2. Persist the *resolved* argument values (post-default-resolution), not just raw `sys.argv`, into `train_command.txt` (or a sibling file) so a checkpoint's provenance always shows the actual Muon LR used, even when it came from the implicit default.
3. Optional, smaller addition: emit a one-time warning at startup when `--optimizer muon` is used without an explicit `--muon-lr`, so it's visible in the training log stream itself, not just in a saved file someone has to go looking for.

## Any Other Things

While investigating this, we also noticed `_resolve_scheduler_steps` (`src/speculators/train/trainer.py:128-138`) already auto-derives `scheduler_total_steps` from `num_epochs * len(train_loader)` — using the real packed-batch count via `MultipackDistributedBatchSamplerV2.__len__`, not an estimate. We were not aware this existed and manually estimated/recalibrated `--scheduler-total-steps` from measured token counts on every run instead (including on resumed/extended runs, where getting this wrong previously caused a full-epoch LR warm-restart regression for us). If this default is reliable for online training with resumed checkpoints, it may be worth calling out more prominently in the docs/tutorials, since at least two independent training efforts on this codebase were unaware of it and did the calibration by hand.

## 评论 (1)

### shubhra · 2026-08-11

Closing — this was posted in error / superseded by a follow-up RFC that better reflects the intended scope.

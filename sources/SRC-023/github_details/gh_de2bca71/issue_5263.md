# [Issue #5263] GEMM tuners: an interrupted run loses everything (results are only written at the end)

source: https://github.com/ROCm/aiter/issues/5263
state: open | updated: 2026-09-04T00:04:51Z
labels: 

## 正文

Tuners write `-o` / `-o2` only after every shape completes. A long run that is interrupted — machine reclaimed, container stopped, OOM, timeout — loses **all** results, including the shapes that had already finished.

On a shared machine this is the dominant cost of tuning: we lost multi-hour `--libtype all` runs repeatedly and ended up wrapping the tuner in an external chunking driver (6 shapes per invocation) purely to bound the loss.

**Proposal**: append each shape's winner (and its `-o2` candidates) as it completes and flush; on startup, skip shape keys already present in the output file. That is consistent with how `--compare/--update_improved` already reads the tuned file, gives `--resume` for free, and makes CI's `op_tune.sh` restartable.

Found while tuning GLM-5.2 on gfx950 (see #5262 for a related scalability fix from the same campaign).

## 评论 (1)

### ThomasNing · 2026-09-04

**Correction to this issue — my original claim was wrong.**

Results are *not* only written at the end: `run()` calls `result_to_csv(...)` after **every batch**, and `pre_process()` already builds a skip mask against the tuned file, so a rerun resumes where the last one stopped. I should have read the loop before filing.

The real defect is narrower: `--batch` defaults to **100**, which is larger than most tuning runs (ours were 42, 6 and 5 shapes), so a typical run collapses into a single batch and the checkpoint never fires before the end. The feature exists and works — the default hides it.

Fix proposed in #5270: when the user has not chosen a batch size, aim for ~8 checkpoints. It can only make batches smaller, never larger; an explicit `--batch` is unchanged; runs of ≥800 shapes are unaffected.

Apologies for the noise in the original report.

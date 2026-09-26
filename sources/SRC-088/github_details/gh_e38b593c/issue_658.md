# [Issue #658] Save the training launch command to the checkpoint dir

source: https://github.com/vllm-project/speculators/issues/658
state: closed | updated: 2026-06-29T11:44:45Z
labels: enhancement, good first issue

## 正文

## Summary

`scripts/train.py` has ~70 CLI flags, but a finished checkpoint records nothing about how it was produced. Once the shell scrollback is gone, the run is effectively unreproducible — there's no reliable way to know which verifier, loss, learning rate, seed, etc. produced a checkpoint sitting in `--save-path`. This is especially painful when running and comparing many experiments.

We should write the exact launch command into `--save-path` so any checkpoint can be reproduced by copy-paste.

## Proposed change

In `main()` (rank 0 only), write `sys.argv` (the `torchrun ... scripts/train.py ...` / `python scripts/train.py ...` invocation) to a file in `--save-path`, e.g. `train_command.txt`:

- reconstruct the command from `sys.argv`;
- write it atomically, rank-0 only, alongside the checkpoints;
- optionally prepend a short provenance header (timestamp, git commit SHA, `world_size`) as comments so a stale checkpoint can be traced back.

That's the whole feature: no schema, no namespace serialization, no new dependencies.

## Notes

- A few args are resolved/mutated at runtime (`mask_token_id`, `draft_vocab_size`, `num_speculative_steps`, default `target_layer_ids`). The saved command still reproduces them on re-run, so it is sufficient for reproducibility — it just isn't a snapshot of the *effective* resolved values.
- Good first issue. It touches the CLI, so per `CONTRIBUTING.md` it warrants maintainer sign-off before implementation.

## 评论 (2)

### orestis-z · 2026-06-25

@rahul-tuli would like to take this, is that okay? I can feel the pain the issue is solving 

### rahul-tuli · 2026-06-26

Go for it @orestis-z 

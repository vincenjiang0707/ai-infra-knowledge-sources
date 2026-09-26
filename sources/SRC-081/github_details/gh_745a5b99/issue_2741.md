# [Issue #2741] [Feature] Native intra-calibration resume in `SequentialPipeline`

source: https://github.com/vllm-project/llm-compressor/issues/2741
state: closed | updated: 2026-09-11T16:50:51Z
labels: stale

## 正文

## Motivation

Large MoE calibrations are long-running (DeepSeek-V3/V4-class models: ~10-12h on 8 H200/B300 ranks for 768 ultrachat samples × seq_len 512). The `SequentialPipeline` currently has **no resume mechanism**: a process crash, OOM, network disconnect, or operator interrupt at hour 8 of 10 means restarting calibration from subgraph 0.

This is the dominant tail-risk for large-model `oneshot()` runs. Even modest reliability — "if I crash at hour 8, I can resume from hour 7" — would change the operational economics of calibrating models that don't fit on a single rank.

## Why not just checkpoint the model state at save time?

- During calibration, weights stay BF16. Observer state accumulates on each `Linear` module, but `ModelCompressor.compress_model(model)` (which materializes packed FP4/FP8 weights) runs once at save time, *after* `oneshot()` returns.
- Snapshotting `model.state_dict()` mid-calibration just gives you the BF16 source weights you already have. The recoverable state is the **per-`Linear` observer accumulator** — `past_min_vals`, `past_max_vals`, `past_global_min_vals`, `past_global_max_vals` on each matched `Observer`.

## Proposed minimum API surface

`SequentialPipeline.__call__` currently iterates `subgraphs` and calls `LifecycleCallbacks.sequential_epoch_end(subgraph)` after each one (`llmcompressor/pipelines/sequential/pipeline.py:163`). Two additions cover resume:

1. **Per-subgraph observer-state snapshot** (after each `SEQUENTIAL_EPOCH_END`):
   - Serialize observer accumulators for the just-completed subgraph's matched modules.
   - Atomic write to a checkpoint dir (e.g. `<output_dir>/_checkpoints/subgraph_N.pt`).
   - Size: observer state per `Linear` is small (4 tensors of shape matching the channel/group axis, fp32). For a 671B-MoE layer, single-subgraph observer state is on the order of tens of MB.

2. **Resume parameter on `SequentialPipeline.__call__`**:
   - `resume_from: int | None` — if set, skip forward passes for subgraphs `< resume_from`.
   - On entry, scan `<output_dir>/_checkpoints/` for the highest completed subgraph, load its observer state into the matched modules, then fast-forward the dataloader to the appropriate batch position before resuming sequential iteration.

Atomic writes via `.tmp + os.replace` and a small `_progress.json` marker would let an operator inspect a killed run and know exactly which subgraph completed.

## Design questions for maintainers

- **Granularity:** per-subgraph (this proposal) vs per-layer (coarser, fewer checkpoints) vs per-batch (finer, larger checkpoint surface)? Per-subgraph aligns with the existing `SEQUENTIAL_EPOCH_END` event, which is why I propose it.
- **Calibration-data hash:** if the user resumes with a different `--samples`/`--max-seq-len`/`seed`, do we error or silently use the new data on remaining subgraphs? Erroring is safer; silent continuation is operationally convenient.
- **Compatibility with non-`SequentialPipeline` pipelines:** Independent / single-shot pipelines don't have subgraph iteration, so they don't get resume. Document this as a `SequentialPipeline`-only feature.
- **Interaction with #1809 (parallel calibration):** if subgraphs eventually run in parallel, the per-subgraph snapshot key needs to disambiguate which subgraph completed. The proposal's `_checkpoints/subgraph_N.pt` naming already supports this; the resume scan should accept arbitrary completed-subgraph IDs, not require contiguous prefixes.

## Reproducer / motivating use case

671B-parameter DeepSeek-V4-Flash MoE, 256 routed experts sharded 8-way (32 experts per rank), 568 GB BF16 source. Production recipe: NVFP4 routed experts + FP8_BLOCK attention + MTP layer. Calibration walltime extrapolated from our 4-rank dryrun: ~2.7-3h on 8 ranks (faster than our original 10-12h estimate, but still long enough that resume matters).

Related: #1809 (parallel calibration, broader pipeline restructuring); #2734 (multi-rank disjoint-module collective desync, observer-level workaround documented there).

Happy to draft a PR for the per-subgraph snapshot + `resume_from` parameter if the design is roughly right.

## 评论 (2)

### github-actions[bot] · 2026-08-19

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!

### kylesayrs · 2026-09-11

This is quite a complex feature to manage, especially with the offloading system. For that reason, this feature cannot be reasonably maintained as of today. Efforts are underway to make LLM Compressor as reliable and performant as possible.

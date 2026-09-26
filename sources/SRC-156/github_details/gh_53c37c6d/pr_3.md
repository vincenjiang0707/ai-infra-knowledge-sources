# [PR #3] Expand KernelWiki with KernelPilot evidence

source: https://github.com/mit-han-lab/KernelWiki/pull/3
state: closed | updated: 2026-06-09T11:00:39Z
labels: 

## 正文

## Summary

This PR expands KernelWiki with a KernelPilot-driven evidence refresh for Blackwell/Hopper kernel optimization work.

- Adds new PR/source pages and candidate-ledger entries across TensorRT-LLM, SGLang, vLLM, FlashInfer, FlashAttention, CCCL/CUB, TileLang, Triton, QuACK, and related kernel projects.
- Adds pinned artifact bundles with provenance for selected upstream PRs, including diffs and key implementation files.
- Adds synthesized wiki coverage for new kernel/technique areas such as TensorRT-LLM Blackwell indexer kernels, FlashAttention SM100 MLA/top-k work, CCCL memory primitives, and external source-map research.
- Regenerates the cross-reference query indices so the new material is discoverable by technique, kernel type, repository, language, problem, and hardware feature.

## Effectiveness evidence

The downstream KernelPilot audit below shows that this expanded KernelWiki content was useful across seven kernel tasks. The table maps each KernelPilot task to the KernelWiki/PR references it used and the concrete optimization techniques validated in the task.

<img width="1200" alt="KernelPilot effectiveness evidence for KernelWiki references" src="https://raw.githubusercontent.com/BBuf/KernelWiki/kernelwiki-pr-assets-20260608/pr-assets/kernelpilot-effectiveness.png" />

## Validation

- `python3 scripts/validate.py`
  - Validated 2787 files.
  - Collected 2735 source IDs.
  - Validated 94 asset bundles: 69 verbatim, 13 extracted, 12 derived.
  - Validated 14 candidate ledgers.
  - Result: all files valid.
- `python3 scripts/generate-indices.py`
  - Regenerated all `queries/*.md` indices.
  - Result: clean working tree after regeneration.


## 评论 (1)

### DongyunZou · 2026-06-09

Thanks for the contribution! I only adjusted the metadata presentation before merging: removed stale hard-coded counts/cutoff wording, kept one repository update date in README, and added a script for dynamic corpus counts. Validation passes, so I’ll merge this now.

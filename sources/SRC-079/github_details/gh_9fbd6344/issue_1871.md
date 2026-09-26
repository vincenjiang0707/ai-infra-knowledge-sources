# [Issue #1871] Clarify canonical documentation between guides and example READMEs (pruning)

source: https://github.com/NVIDIA/Model-Optimizer/issues/1871
state: closed | updated: 2026-09-18T19:32:08Z
labels: bug, documentation, feature request, investigating

## 正文

 ModelOpt documentation is split between docs/source/guides/ and examples/, often with overlapping content. For example, pruning is documented in both.

examples/pruning/ and docs/source/guides/3_pruning.rst. 

As a reader, I am confused which one to read and use. They both overlap and do not seem to be in sync.

## 评论 (7)

### hiSandog · 2026-07-03

The pruning docs need a single canonical path, otherwise example READMEs and guides will keep diverging. A small index table could map each pruning workflow to the maintained guide, the example README, and the supported release/version. It would also be worth adding a docs check that flags example links pointing at superseded guide locations.


### h-guo18 · 2026-07-05

cc @shengliangxu I think this is a valid suggestions that might be worth considering during the re-architecture

### github-actions[bot] · 2026-07-20

Issue has not received an update in over 14 days. Adding stale label.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 587f9a0ee7e5902fb85bd251fac4005adf7a1a7b55da46240034acd5fbfd0edb

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: f0212ff41f892a4c0eeac353e36e91c0536c5e5c12bf12f93f97a2941222e204

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 9d043836b79bb16714e80e23ec49d23977c00963208e401c77360217e73b7dfb

Release follow-up: this open ModelOpt issue needs release relevance confirmed. Link its planned fix/validation, or confirm it is not a v0.46.0 blocker.

### DIYA73 · 2026-09-18

Opened PR #2469 to address this. Added a note to the RST guide clarifying that examples/pruning/README.md is the canonical reference for Minitron and Puzzletron, while the guide covers FastNAS for Computer Vision models.

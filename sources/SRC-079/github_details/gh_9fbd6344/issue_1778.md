# [Issue #1778] Transformers 4.57 does not support Qwen 3.5 - upgrade transformers to 5.x

source: https://github.com/NVIDIA/Model-Optimizer/issues/1778
state: closed | updated: 2026-07-22T04:09:36Z
labels: stale, waiting for feedback, installation

## 正文

Modelopt: main (6/21/2026)

Transformers 4.57 in ModelOpt does not support Qwen 3.5 (compressing the model with puzzletron) - upgrade transformers to 5.x.

## 评论 (3)

### kevalmorabia97 · 2026-06-22

If a specific feature / model isnt supported by an older transformers vesrion, you can add an assertion / warning in that specific example to use newer transformers. Or set `transformers>=5.0` in `examples/puzzletron/requirements.txt`.  In general, we will not enforce transformers 5.x in modelopt for atleast few releases since most modelopt features still work with transformers 4.57 (and also 5.x) and not all external users may have upgraded to transformers 5.x yet.

### github-actions[bot] · 2026-07-07

Issue has not received an update in over 14 days. Adding stale label.

### github-actions[bot] · 2026-07-22

This issue was closed because it has been 14 days without activity since it has been marked as stale.

# [Issue #4084] Two cache/sample logging integrity issues: request-cache keys omit the task config (stale prompts reported as the new config); --samples logs wrong doc ids for unsorted lists

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/4084
state: open | updated: 2026-09-04T07:24:40Z
labels: 

## 正文

## Summary

Two integrity issues in the harness's caching and sample logging, following up on #4062 and #4063 (thank you for the 0.4.13 reporting fix; the scoring-contract half of #4062 remains open as filed).

### 1. Request cache keys omit the task config, so edited tasks silently reuse stale prompts

`Task.build_all_requests` (lm_eval/api/task.py) builds the `--cache_requests` key from the task name, shot count, rank/world size, chat-template and few-shot flags, system prompt hash, and tokenizer name. The key contains no digest of the task configuration itself: no `doc_to_text`, `doc_to_choice`, `description`, `dataset_path`/`dataset_name`/`dataset_kwargs`, dataset revision, `process_docs`, `generation_kwargs`, filter pipeline, harness version, or few-shot seed. The default cache directory lives inside the package and survives harness upgrades.

Consequence: edit a task YAML (or override a stock task by name, or the upstream dataset changes), rerun with request caching on, and the harness reloads the previously built prompts while reporting the new config in `results["configs"]`. Scores are computed over prompts that no longer match the task definition, invisibly.

Reproduction (local JSON datasets, no network, no inference): two tasks share a name; the first caches its prompt; the second, with a different `doc_to_text` and dataset, reruns and logs `built prompt` equal to the FIRST task's prompt while reporting its own new config. Verified twice with byte-identical output.

Suggested fix: include a digest of the task config (and harness version, and few-shot seed) in the cache key; a regression test that edits a config and asserts the cache misses.

### 2. With `--samples`, logged doc ids are wrong whenever the list is not ascending

In `evaluate()` (lm_eval/evaluator.py), `doc_iterator(samples=...)` iterates the selected documents in dataset order, so `doc_id` is the position within the ordered subset, but `doc_id_true = indices[doc_id]` indexes the caller's list by that position. For a non-ascending list, positions and list slots no longer correspond and every logged sample pairs one document's id with another document's content. Example: `--samples task=5,2,9` evaluates docs 2, 5, 9 (positions 0, 1, 2) and logs ids 5, 2, 9 against that order, so the sample holding doc 2 is logged as doc 5 and vice versa.

Reproduction (end-to-end through `lm_eval.evaluator.evaluate`, dummy LM): a 10-doc task evaluated with samples `[5, 2, 9]` logs 2 of 3 samples with mismatched ids. Verified twice, byte-identical.

Suggested fix: build the ordered selected-id list (`sorted(samples)`) once and map positions through it, or have `doc_iterator` yield the original dataset index; a regression test with a non-ascending list pins it. Since `log_samples` output feeds per-sample analysis and leaderboard inspection, the mislabel is silent data corruption for any affected run.

Both reproductions are small and deterministic; happy to share them as PRs with tests.


## 评论 (3)

### YusefSyed · 2026-09-02

I’d like to take the second issue only: incorrect logged document IDs for non-ascending `--samples` selections. I’ll leave the request-cache-key concern untouched, add a provider-free evaluator regression that ties each logged ID to its document marker, and keep the fix limited to the selected-ID mapping (including distributed iterator semantics).


### AUTHENSOR · 2026-09-02

PR #4089 carries the fix for the doc-id limb (one-line mapping change plus three regression tests, branch on the AUTHENSOR fork) since it looked small enough to just send. If you would rather carry it yourself, the branch is yours to pull from. The request-cache-key limb is untouched there if you want the remaining half.

### YusefSyed · 2026-09-04

Thanks for the offer. I will continue carrying #4085 since it was already open and covers the effective iterator mapping end to end, including duplicate selections, empty input, distributed ranks, and positive out-of-range handling. I compared the two approaches: `doc_iterator()` evaluates each selected document once, so retaining duplicates through `sorted(indices)` can still misalign the logged IDs; #4085 derives the same deduplicated, in-range dataset-order IDs the iterator actually visits. I will keep the request-cache-key limb out of scope. The remaining #4085 gate is a stale CLA status even though CLA Assistant records the agreement; an admin resync request is posted on the PR. Happy to adjust if maintainers choose a different contract.

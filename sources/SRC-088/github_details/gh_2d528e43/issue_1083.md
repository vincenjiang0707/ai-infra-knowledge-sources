# [Issue #1083] Add ZeroScrolls Benchmark

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/1083
state: open | updated: 2026-09-01T06:37:01Z
labels: help wanted, feature request, good first issue

## 正文

https://arxiv.org/abs/2305.14196


## 评论 (3)

### bongho · 2026-06-16

Picking this up if no one's working on it. ZeroScrolls is the zero-shot variant of SCROLLS, which is already implemented under `lm_eval/tasks/scrolls/`, so I plan to reuse that task structure (per-subset metrics, doc handling) and adapt it for the `tau/zero_scrolls` validation splits (the official test set is leaderboard-only). I'll start with the subsets shared with SCROLLS and add the ZeroScrolls-specific ones (e.g. `space_digest`, `book_sum_sort`, `musique`, `squality`).

One note: `tau/zero_scrolls` loads via a dataset script, so it'll need `trust_remote_code`. Let me know if you'd prefer a different data path.


### bongho · 2026-06-16

Update — flagging a blocker honestly before anyone spends time here.

`tau/zero_scrolls` is a script-based dataset, and recent `datasets` (5.x) has dropped dataset-script support entirely (`trust_remote_code` is gone), so it no longer loads — this corrects my earlier note. The only public parquet mirror I could find (`simonjegou/zero_scrolls`) ships just the `test` split, which has no gold labels (the official test set is leaderboard-only), so it can't be scored offline.

So the real prerequisite is a parquet conversion of the gold-bearing **validation** splits (per subset). Once that exists on the Hub, the task is straightforward to build on the existing `lm_eval/tasks/scrolls/` structure. Flagging in case a maintainer would prefer to host that conversion, or knows of an existing labeled mirror.

(The same root cause likely affects the existing `scrolls` tasks under recent `datasets` — happy to open a separate issue if that's useful.)

Pausing here rather than leaving a half-working PR.


### LangxiaoXie · 2026-09-01

@bongho — thanks for flagging the blocker rather than leaving a half-working PR; that saved me a detour. I think there's a way around it that doesn't need a parquet conversion.

The dataset repo publishes a static per-subset `.zip` (JSONL inside) alongside the loading script, and those aren't routed through the script, so `datasets` 5.x can read them directly over fsspec:

```python
url = "https://huggingface.co/datasets/tau/zero_scrolls/resolve/main/{name}.zip"
load_dataset("json", data_files={
    split: f"zip://{name}/{split}.jsonl::{url}" for split in ("validation", "test")
})
```

This is the same trick `lm_eval/tasks/scrolls/task.py` already uses — which also answers your last parenthetical: the existing `scrolls` tasks were migrated to this zip path already, so they aren't broken under recent `datasets`, and no separate issue is needed.

Two corrections to the "test has no gold labels" assumption, from inspecting the archives:

- `gov_report` and `qasper` **do** carry a populated `output` on `test` in the zips. The nulling you saw appears to come from the loading-script wrapper / the parquet mirror, not the underlying files.
- `quality` is the real exception — `output` is null on all 500 test rows, genuinely withheld. So validation (21 labeled rows) is the right eval split for that one specifically, not for the benchmark as a whole.

One upstream data bug worth knowing before anyone builds on this: **`qasper.zip` has no distinct test split.** Its `test.jsonl` and `validation.jsonl` are byte-identical (same MD5, 28 rows each), while `gov_report` and `quality` ship 500 test rows each. Verified by loading straight from the Hub, so it isn't a corrupted download. Evaluating qasper on `test` currently scores validation data.

Also worth noting for whoever implements this: the `input` field already contains the complete official zero-shot prompt (instruction + document + trailing cue), so `doc_to_text` is just `doc["input"]` — no hand-written templates, which keeps it faithful to the paper.

You claimed this first, so it's yours if you want it. I have the three subsets above working locally, built on `ConfigurableTask` like `scrolls`. Happy to hand it over or open a PR — whichever's easier for you.


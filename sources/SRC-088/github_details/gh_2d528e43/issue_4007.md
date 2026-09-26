# [Issue #4007] Generative-task scorers cannot distinguish an unparseable response from a wrong answer (census: 2,936/4,524 tasks affected)

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/4007
state: open | updated: 2026-08-17T09:19:26Z
labels: 

## 正文

A resolved-config census of this repo (all 13,668 task YAML → 12,839 tasks, 0 unreadable) finds that **2,936 of 4,524 generative tasks (64.9%)** score an unparseable model response identically to a wrong answer, with no signal that distinguishes the two cases in the reported metric.

Two mechanisms account for it:
- **Regex extraction with a sentinel fallback (2,119 tasks).** `RegexFilter` (`filters/extraction.py:28`) and `MultiChoiceRegexFilter` (`:134`) substitute `"[invalid]"` when the pattern doesn't match. No sentinel equals a gold answer, so the failure is scored 0 — indistinguishable from a genuinely wrong answer.
- **String equality with no extraction (817 tasks).** When a task declares no `filter_list`, `take_first` (`api/task.py:757-776`) is installed alone and `exact_match` reduces to `predictions == references` (`api/metrics.py:239`) — the entire response must equal the gold string verbatim.

**The information to fix this already exists and is already computed** — it's discarded rather than absent. `"[invalid]"` (and its equivalents: `["invalid"]` in `POSFilter`, an empty span in `SPANFilter`) is produced at 9 call sites across 6 modules. Of the 2,936 affected tasks, only 4 in the entire framework (0.09%) surface any "did this parse" signal downstream (`eq_bench`'s `percent_parseable`, `simple_cooccurrence_bias_gen`'s explicit sentinel check) — and none of those 4 are in the affected set.

This also isn't visible to most users after the fact: 2,378 of the 2,936 affected tasks (81%) declare only one scoring pipeline, so there's no second number to notice a discrepancy against.

**Proposed fix, scoped to be purely additive (no change to existing scores or behavior):** emit a companion count/rate alongside the existing metric whenever a fallback sentinel fires — e.g. `exact_match: 0.65, unparsed_rate: 0.12` — using the sentinel value these filters already produce. Happy to open a PR implementing this if the direction is welcome.

Methodology and full breakdown (by task family, by fewshot/no-fewshot split, sample-verified 40/40 against framework source): https://anonymous.4open.science/r/knowledgeshift-E772/, `scripts/13` + `scripts/14`. Reproducible against any harness commit.

## 评论 (2)

### arrdel · 2026-08-17

The pattern is the shape a group of us have been converging on this week, one repo over. In `inspect_evals` the same class of bug lands in three PRs opened this weekend: [#2173](https://github.com/UKGovernmentBEIS/inspect_evals/pull/2173) (documents the convention: `nan` at metric level, plus a coverage metric, plus an unscorable rate), [#2174](https://github.com/UKGovernmentBEIS/inspect_evals/pull/2174) (implements it for AgentHarm), and [#2165](https://github.com/UKGovernmentBEIS/inspect_evals/pull/2165) (implements it for `strong_reject` via `Score.unscored()`). Same underlying observation: a wrong answer and a response the metric could not read are two different states, and the reported number should not conflate them.

One observation on the proposal shape.

**Two states or three.** `unparsed_rate` alongside `exact_match` names the sentinel-fallback state. It does not name the "response was parseable but did not equal the gold string" state, which on the 817 no-filter tasks is where `predictions == references` treats "plausible answer, different formatting" identically to "refused to answer". Whether that gap matters depends on whether we read `exact_match` as an oracle over gold formatting or over correctness; on generative tasks with free-form output, most of the confusion lives in that tail. A minimally-invasive extension: also report `matched_rate` (predictions with non-sentinel content, whether or not they matched). Both are cheap, both are additive, and together they name the three states rather than two, without changing any existing headline number.

The `scripts/13 + scripts/14` census methodology (13,668 configs resolved, 40 samples reproduced against framework source, 4 tasks in the entire tree surfacing any parse signal) is worth having in the PR body when you open it. It makes the scope claim auditable rather than illustrative.


### FazeelUsmani · 2026-08-17

Did this in inspect_evals last week (UKGovernmentBEIS/inspect_evals#2165), for one data point: additive works, existing scores don't move.

Watch the sentinel though. strong_reject was returning an empty dict for unparseable judge output. Metrics skipped it fine, but it didn't count towards unscored_samples and the epoch reducer rejected it outright, so any run with epochs > 1 died on the first one. Had to switch to the nan value the aggregation layer already recognises.

Same question here really, what does unparsed_rate do under repeats and at group aggregation?

Not trying to take this off you. Happy to help if useful.


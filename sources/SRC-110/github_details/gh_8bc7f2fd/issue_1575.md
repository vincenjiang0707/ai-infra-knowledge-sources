# [Issue #1575] [Bug] LLM-judge failures are invisible in reports, and the generic score extractor can silently inflate scores (violating the documented fail-close contract)

source: https://github.com/modelscope/evalscope/issues/1575
state: closed | updated: 2026-08-15T04:23:15Z
labels: 

## 正文

## Summary

The repo already documents a **fail-close** contract for LLM-judge failures: `hipho/utils.py:140-142` — *"A failed judge request must score 0, never full credit: `LLMJudge.judge` reports failures as an `[ERROR] ...` string."* Fail-close to 0.0 is therefore **intended behavior**, not the bug.

The actual gaps are fourfold, and they sit in the **shared** extraction path (`ScoreExtractor` → `LLMJudge.get_score`), which all judge-based benchmarks that don't override `llm_match_score` go through:

1. **The generic path can silently give *full credit* or *garbage credit* — the exact thing the fail-close contract forbids.**
   - `NumericScoreExtractor` clamps out-of-range values to `[0,1]` with **no warning** (`score_extractors.py:61`). A user running a 0–100-scale judge (custom `prompt_template`/`score_pattern`) gets `[[90]]` → **1.0**, i.e. the failed/extreme case is awarded *perfect* credit — the opposite direction of the documented "never full credit" intent.
   - Unlike `hipho/utils.py:144` (which checks the `[ERROR]` prefix **before** running any regex), `LLMJudge.get_score` (`llm_judge.py:178-190`) passes the raw response straight to the extractor. With a loose custom numeric pattern, digits embedded in the `[ERROR]` string (model_id `Qwen3-235B`, api_url `.../v1/`, etc.) can be parsed as a **garbage nonzero score**.
2. **A matched-but-unmapped category silently returns 0.0 with no warning** (`score_extractors.py:31`) — inconsistent with the no-match branch one line below (`:33`) which *does* `logger.warning`. Same file, same failure class, different observability.
3. **Judge failures are invisible in the aggregate report.** `score.explanation` preserves the raw `[ERROR]` text (`llm_judge_mixin.py:156`), but nothing downstream reads it — the default `Mean` aggregator folds every per-sample `{'acc': float}` into the headline number with no filtering, no failure counter, no report banner (`aggregators.py:34-52`). A judge outage silently drags the reported accuracy down.
4. **Zero test coverage.** The 73-line extractor module has no direct or indirect tests (grep of `tests/` for `ScoreExtractor`/`NumericScoreExtractor`/`PatternScoreExtractor` is empty). The only judge-related test asserts strategy selection (`tests/api/test_default_data_adapter.py:85-98`).

## Code path (verified)

```
LLMJudgeMixin.llm_match_score                        # api/mixin/llm_judge_mixin.py:125-163
  judge_response = self.llm_judge.judge(prompt)      # llm_judge.py:159-162  -> '[ERROR] ...' on API error
  judge_score = self.llm_judge.get_score(judge_response)  # llm_judge.py:178-190 -> extractor
  score.value = {'acc': judge_score}                 # llm_judge_mixin.py:155
  score.explanation = f'LLM judge: {judge_response}' # llm_judge_mixin.py:156  (write-only)
    -> default_data_adapter.py:716-723 (JudgeStrategy.LLM) / 698-714 (LLM_RECALL via _merge_scores :165-181)
    -> Mean aggregator, unfiltered (metrics/aggregators/aggregators.py:34-52)
```

`LLMJudgeMixin` is inherited by every `DataAdapter` (`api/benchmark/benchmark.py:25`). Grep-verified: **35 benchmarks** set `llm_judge_default = True`; **30 override** `llm_match_score` with their own parsing (and are unaffected by this bug); the remaining **6 fall through to this shared path** — `baby_vision`, `zerobench`, `world_vqa`, `math_verse` (via `VisionLanguageAdapter`), `minerva_math`, `imo_answerbench` (via `DefaultDataAdapter`) — plus any custom-dataset run with `judge_strategy='llm'/'llm_recall'`.

## Repro evidence (standalone, exact extractor logic)

| case | input | score | note |
|---|---|---|---|
| judge API error | `[ERROR] Error ... HTTP 500` | 0.0 | documented fail-close, *does* warn (`:33`) |
| unmapped grade | `'D'` w/ custom pattern `[ABCD]` map `{A:1,B:.5,C:0}` | **0.0, no warning** | silent edge `:31` |
| pure word | `'excellent'` (PATTERN) | 0.0 | warns |
| out-of-range | `[[90]]` numeric (0–100 judge) | **1.0, no warning** | silent clamp `:61` — *full credit* |
| numeric API error | `[ERROR] ...` | 0.0 | warns |
| loose pattern + error | `[ERROR] Qwen3-235B@.../v1/...` parsed with a loose `\d+` pattern | **garbage nonzero** | generic path lacks hipho's `:144` prefix guard |
| baselines | `'A'` → 1.0, `[[0.5]]` → 0.5 | correct | |

## Suggested direction (smallest-diff, no contract break)

1. `score_extractors.py:31` — `logger.warning(...)` when the matched answer is not in `score_mapping` (mirrors `:33`).
2. `score_extractors.py:61` — warn when a value is clamped (`val != clamped`); keep the clamp itself (removing it breaks the documented numeric contract and lets out-of-range floats leak into aggregators).
3. `LLMJudge.get_score` (`llm_judge.py:178`) — if `response.startswith('[ERROR]')`, log explicitly **before** extraction — the same guard `hipho/utils.py:144` already ships. This closes the garbage-nonzero hole for loose patterns.
4. Add unit tests for both extractors (empty, no-match, unmapped, clamp, `[ERROR]` prefix).

Whether a failed-judge sample should additionally be *excluded with a visible count* (rather than scored 0) is a semantics decision I'd like the maintainers to rule on before a fix lands.

## Affected / not affected

- **Affected:** judge-based runs on the shared `LLJMJudgeMixin` path (the 6 benchmarks above), and custom-dataset runs with `judge_strategy='llm'` / `'llm_recall'`. Under `LLM_RECALL`, `_merge_scores` (`:177`) *replaces* the rule-based score with the judge score — a judge failure can actively *worsen* a partial rule score (e.g. 0.5 → 0.0).
- **Not affected:** rule-based (`JudgeStrategy.RULE`) runs; benchmarks that override `llm_match_score` with their own parsing (`charxiv`, `cl_bench`, `aime`, `alpaca_eval`, etc. — note `cl_bench_adapter.py:163-173` already labels "LLM judge parsing failed" in `explanation`/`metadata`, the pattern the generic path should follow).


## 评论 (1)

### Yunnglin · 2026-08-14

Thanks for this — the four-way breakdown and especially the reachability
table made it easy to verify. Confirmed all four gaps on `main`.

We're currently designing a broader refactor of the LLM-judge layer, and
the semantics question you flagged belongs in it rather than in a patch.
Planned scope:

- position swapping, to mitigate position bias in pairwise judging
- repeated scoring / multi-sample judgments
- multi-judge aggregation
- disagreement statistics across judges
- offline re-scoring, i.e. re-judging from cached predictions without
  re-running inference
- failure degradation — your point 3: a judge failure should be visible
  and handled explicitly, not silently folded into the headline number

So we'd rather not settle "score 0 vs. exclude with a visible count"
inside #1576. It is a contract-level decision we want to make once,
together with the failure-degradation design above.

#1576 as scoped (points 1, 2 and 4) is good and can land on its own. I
pushed one commit to your branch: `_clamped` let NaN through, because
every comparison against the bounds is false for NaN. On `main` a NaN
token silently became 1.0; after your refactor it became `nan`, which
would poison the whole aggregate since nothing in the metric path filters
NaN. It now fails closed to `clamp_min`. That commit also adds the blank
lines yapf wanted, which was the failing pre-commit hook.

Will follow up here once the refactor design is written up.


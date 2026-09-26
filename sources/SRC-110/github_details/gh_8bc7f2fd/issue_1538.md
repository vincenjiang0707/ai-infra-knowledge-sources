# [Issue #1538] [Bug]: score_milestones returns 1.0 when milestones exist but fail to parse — unscorable is indistinguishable from perfect

source: https://github.com/modelscope/evalscope/issues/1538
state: closed | updated: 2026-08-06T00:29:38Z
labels: 

## 正文

### Bug Description

`score_milestones()` returns **1.0** — a perfect score — when the milestones exist and simply fail to parse. A sample that could not be scored is indistinguishable, at every point downstream, from a sample that scored perfectly.

`evalscope/benchmarks/acebench/utils.py:266`

```python
def score_milestones(predicted_calls, milestones) -> float:
    if not milestones:
        return 1.0                      # (A)

    candidates = milestones if _is_milestone_candidates(milestones) else [milestones]
    best = 0.0
    for candidate in candidates:
        expected_calls = _parse_milestone_strings(candidate)
        if not expected_calls:
            best = max(best, 1.0)       # (B)  <- line 276
            continue
        matched = _count_subsequence_matches(predicted_calls, expected_calls)
        best = max(best, round(matched / len(expected_calls), 3))
    return best
```

**(A) is arguable.** No milestones at all — vacuously satisfied. Reasonable people differ and I am not proposing you change it.

**(B) is the one.** Here the milestones *exist*. They just did not survive parsing, and the empty list is read as "nothing required, therefore everything satisfied."

### Why the parse can come back empty without anything raising

`_parse_milestone_strings` at `:551` drops silently:

```python
for milestone in milestones:
    if isinstance(milestone, str):
        calls.extend(parse_call_list(milestone))
    else:
        item_calls = _calls_from_json_like(milestone)
        if item_calls is not None:
            calls.extend(item_calls)
return calls
```

`_calls_from_json_like` (`:354`) returns `None` on anything it cannot interpret, and the `is not None` guard then discards it without appending, without warning, and without raising. A malformed milestone, an unexpected nesting depth, a schema change upstream — all of them produce `[]`, and `[]` at line 275 becomes `1.0`.

### Steps to Reproduce

```python
from evalscope.benchmarks.acebench.utils import score_milestones

# milestones are PRESENT and non-empty, but unparseable
print(score_milestones([], milestones=[{"unexpected_schema": "value"}]))
# -> 1.0
```

The model produced no calls at all and scores perfectly.

### Expected Behavior

The two cases need to be separable. Any of these would do it, and which one is yours to pick:

- Return `None`/`nan` for the unparseable case and exclude it from the aggregate, rather than scoring it.
- Raise, so a malformed benchmark file fails loudly at load rather than silently inflating a run.
- Keep returning a number but count it separately, so a report can say *scored 940, unscorable 60* instead of *940*.

The third is the one I would want as a consumer of the numbers, because it survives aggregation. A rate whose denominator quietly includes samples that were never measured is the failure that does not announce itself.

### Honest scope

I have **not** observed this firing on a real ACEBench run — I do not have the dataset in front of me, and it is entirely possible every milestone in it parses cleanly today and this is latent. So: a latent defect in a scoring primitive, not a claim that your published numbers are wrong.

What makes it worth filing anyway is the direction. **It can only ever fail upward.** A parse failure inflates the score and never deflates it, so nothing downstream is motivated to catch it — there is no angry user reporting that their model scored too well. That asymmetry is why this class survives in codebases for years.

Happy to open a PR for whichever of the three shapes you prefer.

---

Context on why I was in here: this failure class is what I work on — writes and measurements that return cleanly while the thing they claim never happened. Same shape as `0` meaning both *no hallucination detected* and *nothing was evaluated*. If it is ever useful to have someone go through a codebase looking for the rest of them, that is at unreached.dev. The issue stands on its own regardless and needs nothing from me.


## 评论 (3)

### ebarkhordar · 2026-08-04

The dataset is public, so I went after the open question in your "Honest scope" section. Everything below is on HEAD `fa4da9b774c408cd1a9cfb92095f4fafae86dd2d`, Python 3.11, clean container, against the `evalscope/acebench` `en/agent` split that `acebench_adapter.py:73` reads `mile_stone` out of.

**Your minimal case reproduces, and (B) is latent on the shipped data.**

```
score_milestones([], [{'unexpected_schema': 'value'}]) -> 1.0
```

All 50 rows of `en/agent-00000-of-00001.parquet` carry a non-empty `mile_stone`, and:

```
candidates with at least one parsing to []    : 0
samples where EVERY candidate parses to []    : 0
samples where score_milestones([], ms) == 1.0 : 0
```

Line 276 does not fire on this data. Your caution was right.

**The asymmetry is live anyway, on a line your report does not name.**

Every milestone item in that subset is a `str` (270 of them), so none reach `_calls_from_json_like` at `:354`. They go through `parse_call_list` at `:557`, and 14 of the 270 come back `[]`:

```
"[add_food_delivery_order(username='Grace', merchant_name='Domino's', items=[...])]"
"[add_reminder(title='Today's spending', description='Today's spending 88.0 yuan', ...)]"
"[send_message(sender_name='Eve', receiver_name='Frank', message='Don't forget tomorrow afternoon's meeting')]"
```

Unescaped apostrophes inside single-quoted literals. `_calls_from_python_expr` (`:393`) hits them and swallows the error:

```
ast.parse("[f(merchant_name='Domino's')]", mode='eval')
  -> SyntaxError: unterminated string literal (detected at line 1)
_calls_from_python_expr(...) -> []          # :396 except Exception: return []
```

This is also why (B) stays latent. `_parse_milestone_strings` uses `calls.extend(...)`, so a failing item contributes nothing while its siblings carry the candidate, and `expected_calls` is never empty. The loss lands at `:279` instead, where the score is `matched / len(expected_calls)`: the dropped milestone leaves the denominator, so it stops being required at all.

12 of the 50 agent samples lose at least one milestone this way. Scoring a prediction that satisfies exactly the milestones the parser recovered:

```
id                    milestone strings -> expected_calls    score    honest score
agent_multi_step_0     3 -> 1                                 1.0      0.333
agent_multi_step_1     4 -> 2                                 1.0      0.5
agent_multi_step_4     4 -> 3                                 1.0      0.75
agent_multi_step_5     3 -> 2                                 1.0      0.667
agent_multi_turn_8     4 -> 3                                 1.0      0.75
agent_multi_turn_9     3 -> 2                                 1.0      0.667
agent_multi_turn_10    5 -> 4                                 1.0      0.8
agent_multi_turn_11    5 -> 4                                 1.0      0.8
agent_multi_turn_12    8 -> 7                                 1.0      0.875
agent_multi_turn_13    7 -> 6                                 1.0      0.857
agent_multi_turn_14    7 -> 6                                 1.0      0.857
agent_multi_turn_15    6 -> 5                                 1.0      0.833
```

Same direction you identified: it only ever fails upward.

The reason this is worth separating from (B): a guard at line 276 catches none of the 12, because `expected_calls` is non-empty in every one of them. The signal that tells "nothing was required" apart from "we could not read what was required" is a count, not an emptiness check. `_parse_milestone_strings` knows how many items it was handed and how many it recovered, and it discards that difference at `:557`.

Whether the 14 strings are a data bug or a parser gap is your call, and the two fixes are different: escaping them in the dataset fixes these 14, while making the recovery count visible catches the next batch too.

What I did not check: I have not run a model eval end to end, so I cannot say what a published ACEBench agent number would move by. This is the scoring primitive against the shipped data. The dataset repo has only `en`, so the 14 are all I can speak to.

One note on history, in case it changes how you read this. `evalscope/benchmarks/acebench/utils.py` has exactly one commit, `75e2d312` (#1386). Both `best = max(best, 1.0)` and the `except Exception: return []` arrived with the file and carry no rationale comment, so nothing in the history suggests either was a decision someone weighed and settled.

### Yunnglin · 2026-08-05

Fixed on `main` in #1544. Thanks for the careful report — and for pointing at the asymmetry rather than just the line, that framing is what made the real extent of it obvious.

**What changed**

Rather than pick one of your three shapes, the parsing layer itself turned out to be the defect. Upstream never parses milestones: `agent_eval_process` compares them as raw strings against the recorded call trace and always divides by the declared milestone count. So `score_milestones` now does the same, and the whole `_parse_milestone_strings` / `_calls_from_json_like` path is gone. Your repro returns `0.0` now:

```python
>>> from evalscope.benchmarks.acebench.checker import milestone_accuracy
>>> milestone_accuracy([], [{'unexpected_schema': 'value'}])
0.0
>>> milestone_accuracy([], ['not a call'])
0.0
>>> milestone_accuracy([], [])          # genuinely empty, vacuously satisfied
1.0
```

Case (A) is kept at `1.0` because upstream does the same (`if milestone_len == 0: accuracy = 1.00`), so leaving it alone keeps our numbers comparable with the published ones.

**On "latent"**

It was worse than latent, just not in the shape you predicted. The `[]` → `1.0` branch is not reached on the current data, but the same root cause fires through a narrower door: the ground truth contains milestones that are not valid Python, because apostrophes inside string values are unescaped:

```
[add_food_delivery_order(username='Eve', merchant_name='Domino's', items=[...])]
[add_reminder(title='Today's spending', ...)]
```

Those were dropped silently, which shrank the *denominator* instead of emptying it. On the English `agent` split that is **12 of 50 samples**. Concretely, `agent_multi_step_0` declares 3 milestones and only 1 survived parsing, so a model hitting that single one scored `1.0` where upstream caps it at `0.333`. Same failure direction you described — it could only ever inflate.

There is a regression test for each branch of this, including the real `agent_multi_step_0` milestones, in `tests/benchmark/test_acebench.py`.

**Wider scope**

Auditing this turned up more divergence from the official protocol than the milestone scorer, so #1544 also aligns the rest of it. The parts worth knowing about if you use these numbers:

- Official prompts are used verbatim, and an answer that is not a decodable `[ApiName(...)]` list now scores zero instead of being rescued by lenient parsing.
- `model_eval/checker.py` semantics are ported, most consequentially that a parameter the schema does not mark `required` may be omitted. Our previous exact-key-set rule disagreed with upstream on **314 of 326** applicable samples, all in the deflating direction.
- `agent` categories now run a real rollout against ACEBench's simulated APIs and are graded on the resulting environment state. Previously the adapter asked the model to *report* its own final state, and fell back to using milestone progress as the accuracy — which is what made the bug you found reachable as an accuracy, not just a secondary metric.
- The 17 fine-grained categories are reported with the official grouping and weighting (`normal` 0.578 / `special` 0.2676 / `agent` 0.1545), and both languages are selectable via `extra_params.language`.

The checker port and the vendored simulated APIs are verified differentially against a local ACEBench checkout: set `ACEBENCH_REPO=/path/to/ACEBench` and the test suite additionally compares every verdict over both languages, plus the environment state the vendored APIs reach against upstream's executor.

**Separately, the dataset was stale**

`evalscope/acebench` on ModelScope had been imported from a third-party mirror. The whole `zh` configuration was missing, and 11 English records had drifted, including the three answers upstream corrected on 2025-10-29 (`normal_atom_enum_9`, `normal_atom_number_17`, `normal_atom_list_34`) and `special_incomplete_0`, whose parameter names carried stray spaces that broke the substring check the `special` categories are graded with. It is now rebuilt from the official repository and every field of all 2040 records verified against it.

**Using it**

This lands after `v1.10.0`, so it is on `main` only for now:

```bash
pip install git+https://github.com/modelscope/evalscope.git@main
```

If you have a local ACEBench clone and want to re-check any of the above yourself, the differential tests are the fastest way in. And ACEBench numbers produced before this change are not comparable with numbers after it — decoding is stricter, the optional-parameter rule changed, and `end_state_acc` is gone from the metric list.


### siliroid · 2026-08-06

Thanks for the quick turnaround on #1544 — and for the note about the asymmetry.

That line stuck with me more than the fix did. Pointing at *"detection exists, the return value doesn't carry it"* rather than at the line number is exactly the framing I use to find these, and it's rare that a maintainer names it back. It's genuinely useful to know it read that way from your side.

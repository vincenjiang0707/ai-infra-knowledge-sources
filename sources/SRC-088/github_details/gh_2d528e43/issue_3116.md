# [Issue #3116] hendrycks MATH remove_boxed() does not handle \fbox{} despite fallback logic in last_boxed_only_string()

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3116
state: open | updated: 2026-08-31T13:21:58Z
labels: 

## 正文

In the hendrycks_math/utils.py, the function last_boxed_only_string() correctly falls back to \fbox{...} if \boxed{...} is not present. However, remove_boxed() only handles \boxed{} but not \fbox{} . Is this intentional?   

## 评论 (1)

### nata2627 · 2026-08-31

The asymmetry is real: with no `\boxed` anywhere in the string, `last_boxed_only_string` falls back and returns an `\fbox{...}` span, and `remove_boxed` asserts on `\boxed{`, so the pair raises a bare `AssertionError` on the extractor's own fallback.

It does not look reachable on `main` (`6bfdbcbd`), which is probably why it has never been reported as a failure. I scanned every solution in the datasets the three unguarded call sites read — `EleutherAI/hendrycks_math` (12500 solutions, all seven configs, train and test), `HuggingFaceH4/MATH-500` (500) and `Putnam-AXIOM/putnam-axiom-dataset-ICML-2025-522` (1122 across its three splits). `last_boxed_only_string` returns an `\fbox` span for **0** of those 14122, and returns `None` for none of them either, so `hendrycks_math`, `minerva_math` and `putnam_axiom` never hand `remove_boxed` anything but a `\boxed` span.

The other direction — a model response carrying `\fbox` and no `\boxed` — is already covered everywhere it can occur: `aime` catches `(AssertionError, IndexError)` around the pair, `putnam_axiom.process_results` catches `Exception`, `leaderboard/math.remove_boxed` returns `INVALID_ANSWER` instead of raising, and `agieval` and `hrm8k` reach the pair only under `if "\boxed" in raw_string`.

Not checked: tasks outside this repository that import these helpers. I am not working on this.


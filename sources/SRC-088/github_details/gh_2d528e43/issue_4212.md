# [Issue #4212] `mbpp_plus_instruct` grades against the assertion printed in its own prompt, and never uses the MBPP+ test suite

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/4212
state: open | updated: 2026-09-25T01:16:53Z
labels: 

## 正文

`lm_eval/tasks/mbpp/mbpp_plus_instruct.yaml:5-6`:

```yaml
doc_to_text: "{{prompt if prompt is defined else text}} Your code should satisfy the following assertion:\n{{test_list[0]}}"
doc_to_target: "{{test_list[0]}}"
```

`doc_to_target` is the reference handed to `pass_at_1` (`lm_eval/tasks/mbpp/utils.py:18-29`;
`lm_eval/api/task.py:1633` passes `references=[gold]`). It is byte-identical to a span of the prompt.

The `evalplus/mbppplus` dataset carries a `test` field holding the expanded EvalPlus suite. No mbpp
YAML references it.

## Measured

Run through the harness's own task object against the live dataset, using the real `code_eval`
metric with its genuine `unsafe_execute`, `reliability_guard` and timeout:

```
57 mbpp_plus_instruct docs
  constant-returning cheat  -> pass@1 = 1.000
  correct implementation    -> pass@1 = 0.000
```

Controls in both directions confirmed the metric itself is sound
(`correct-impl -> {'pass@1': 1.0}`, `wrong-impl -> {'pass@1': 0.0}`).

One caveat, stated plainly: `code_eval`'s `multiprocessing.Manager()` fails in the sandbox used,
so the IPC was swapped `Manager` → `Pipe`. Nothing else in the metric was modified. If that
substitution invalidates the result in your view, please say so and I will redo it differently.

## Consequence

A model that emits a function body satisfying only the single printed assertion scores as if it had
passed MBPP+. The task measures prompt-copying, and the EvalPlus tests it advertises never execute.

## Suggested fix

Point `doc_to_target` at the dataset's `test` field and drop the assertion from `doc_to_text`, or
rename the task so it does not claim MBPP+ coverage.

## 评论 (4)

### anika-bansal · 2026-09-23

Hi, I'd like to claim this. Are you planning to submit the fix yourself, or is this open for someone else to pick up?

### anika-bansal · 2026-09-23

Since I'm on a tight timeline, I'm going to start working on this now — happy to coordinate or step back if you're already on it.

### shaurya416 · 2026-09-23

Not planning to submit it myself — it's yours, and no need to step back.

Two things that may save you time. The fix itself is small: point `doc_to_target` at the dataset's `test` field (the expanded EvalPlus suite, which nothing currently references) and drop `{{test_list[0]}}` from `doc_to_text`. The part that bit me was testing it: `code_eval`'s `multiprocessing.Manager()` dies with `EOFError` in some sandboxes, which is why my repro swapped `Manager` → `Pipe` for the IPC only. If your CI has the same problem, that swap is the workaround; the `unsafe_execute` / `reliability_guard` / timeout path is untouched by it.

Happy to review when it's up.

### shaurya416 · 2026-09-25

Correction to the suggested fix in the issue body and to my comment of 2026-09-23: dropping `{{test_list[0]}}` from `doc_to_text` is wrong, because that assertion is the only place the prompt names the function that the `test` text calls. The intended change is `doc_to_target: "{{test}}"` only, with the prompt kept as it was, which is also how EvalPlus builds its MBPP+ prompts (task text plus `test_list[0]`). The measurements are in https://github.com/EleutherAI/lm-evaluation-harness/pull/4228#issuecomment-5825039860.


# [Issue #1883] Add Regression Testing

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/1883
state: open | updated: 2026-09-07T18:27:44Z
labels: help wanted, feature request, good first issue

## 正文

As per the issue title. 

It would be great to have regression tests for some core tasks set up, checking that 1. some key tasks' scores don't regress or change and 2. that the printouts for results stay the same (results tables).


ideally, we'd have:
- on-CPU tests (with `limit=10`) that can always run
- full on-GPU tests that can be run when desired for larger changes.

If any contributors are interested in taking this on, it'd be a huge help! Otherwise, I hope to get to this.

## 评论 (10)

### zafstojano · 2024-05-27

@haileyschoelkopf 
1. Which tasks would you consider as core?
2. Which models do you believe are most effective/efficient for doing this?

### giorgossideris · 2024-05-27

Hello @haileyschoelkopf, I would be interested in helping with this.

### haileyschoelkopf · 2024-05-27

Thanks all for the interest! 

@clefourrier @KonradSzafer are tackling some regression testing now actually--if anything can be passed off maybe they can share. 

models that would be useful to test would be
- gpt2
- a small model which uses a Llama tokenizer / sentencepiece

and core tasks would be
- `mmlu`
- `arc_easy`, `arc_challenge`
- `lambada_openai`
- `wikitext` 
- other Open LLM Leaderboard tasks
- more could be added based on computational cost of running these tests.


Something that would be helpful which isn't currently being done is checking equivalence of the printed results tables, to ensure that the formatting there or printing of task groupings does not get modified by a new PR. This could be done by extending the current `tests/test_evaluator.py` tests. 

Something which could be taken on and is not yet being worked on would be to implement a greater number of tests for the `evaluate()` and `simple_evaluate()` functions, or to mock the CLI and test `cli_evaluate()` with various options to ensure that these components are functioning as intended. I could describe a number of tests that would be useful if this is of interest! the CLI testing would be a big one.

### giorgossideris · 2024-05-31

@haileyschoelkopf could you expand on the new tests that you consider as useful?

### harshil-1402 · 2026-06-15

can you assign this issue to me so that i can contribute on this 

### haeliotang · 2026-06-16

Hi @haileyschoelkopf — you noted the CLI testing (`cli_evaluate()` / more tests for `evaluate()`/`simple_evaluate()`) wasn't yet being worked on, so I took a look and prototyped it.

Parser-level parsing and config precedence are already well covered in `test_cli_subcommands.py`. The gap I found: no test asserts the parsed `run` flags actually reach `simple_evaluate(...)` — `test_run_command_execute_basic` mocks `simple_evaluate` and only checks it's called, not the kwargs. So a refactor could silently drop or mis-map a flag and every test would still pass.

I wrote a small mock-based test class that parses real `run` argv, runs the real `EvaluatorConfig.from_cli` mapping, and asserts the kwargs reaching `simple_evaluate` (`--model`, `--limit`, `--num_fewshot`, `--predict_only`, `--gen_kwargs`, and the `--seed`→python/numpy/torch/fewshot ordering). 6 tests, CPU-only, ~0.05s. I verified it catches silent regressions — it fails if e.g. the `--limit` wiring is dropped. One nuance surfaced: `--predict_only` requires `--output_path` via config validation.

Happy to open a PR — would you prefer it folded into `test_cli_subcommands.py` or a new `tests/test_cli_run_wiring.py`?

### aarushi211 · 2026-09-03

Hi! I’d like to contribute to this.

I looked through the current `tests/test_evaluator.py` coverage and noticed that some validation behavior in `simple_evaluate()` / `evaluate()` does not appear to have direct regression tests, for example, rejecting `limit` and `samples` when both are provided, and rejecting an empty task list in `simple_evaluate()`.

I also saw the ongoing work in #3858 and #4027, so I’d like to keep this scoped to evaluator-level validation and avoid overlapping with the CLI wiring or CPU snapshot work.

Would tests covering these validation paths be useful as a small contribution under this issue?


### sinanezhadian · 2026-09-05

On what the numerical half of this should actually assert, since the comparison rule is most of the design and both obvious choices fail.

**Exact equality flakes.** Re-running the same task on the same weights at a different batch size, or under different concurrent load, changes logprobs on any GPU backend — kernel reduction order depends on the batch a request lands in, and floating-point addition is not associative. Borderline items flip and the test goes red on a PR that changed nothing relevant. This is much rarer on CPU at `limit=10`, which is why the two tiers @haileyschoelkopf describes need different rules rather than the same rule at different scale.

**A hand-picked epsilon fails the other way.** Too tight and it flakes anyway; too loose and it silently permits exactly the regressions the test exists to catch, with no principled way to tell which one you have.

**The way out is to measure the threshold instead of choosing it.** Pin one reference config, run the chosen core task N times changing nothing at all, and record the spread of the headline metric. That standard deviation is the harness's own noise on that task, and roughly 2.8x it (the ISO 5725 repeatability limit) is the smallest change the test can distinguish from that noise. Assert against that, store it beside the reference scores, and re-measure when the reference config changes.

That also gives a real answer to @giorgossideris's question about which tests are worth having: a task whose noise floor is wider than the regressions you care about cannot be regression-tested at that N, and is better spent as a results-table-shape test. It turns "which tasks" from a taste question into a measurement.

Two practical notes:

- Store the config the reference numbers were produced under, not just the numbers — engine and version, batch size, dtype, and the concurrency during the run. Most of the variance lives in defaults nobody set explicitly, and defaults move between releases, so a reference score without its config expires silently and nobody finds out until the test starts failing for unrelated reasons.
- All of the above is about the GPU tier. For the `limit=10` CPU tests, exact match on results-table shape is the right assertion and needs none of this.

@aarushi211's scope — evaluator-level validation, rejecting `limit` and `samples` together, rejecting an empty task list — is orthogonal to all of it and worth doing on its own. Those paths are deterministic, so they belong in the exact-match CPU tier where a strict assertion is safe.

### aarushi211 · 2026-09-05

Thanks, this helps clarify the distinction @sinanezhadian . I'll keep my scope focused on the deterministic evaluator validation paths (limit + samples, and empty tasks) and open a small PR for those tests separately from the numerical regression work.

### sinanezhadian · 2026-09-07

Correction to my own comment above, before it gets built into a test.

I said "roughly 2.8x it". The sqrt(2) inside that constant is right: you are comparing a new run against a stored reference, so the difference carries both uncertainties. The 1.96 is not, because it assumes sigma is *known* - and here you have just estimated it from N runs, with N-1 degrees of freedom. The factor is t(0.975, N-1) * sqrt(2):

| N | factor |
|---|---|
| 3 | 6.08 |
| 5 | 3.92 |
| 10 | 3.20 |
| 20 | 2.96 |
| 30 | 2.89 |

2.77 is only the large-sample limit. For a regression gate the consequence is concrete: a threshold set 29% too narrow at N=5 fires on ordinary run-to-run variation, and a CI check that cries wolf gets muted - which is worse than not having one.

So store N beside the reference sigma, use the t factor for that N, and re-derive it when the reference config changes. And if the resulting band is wider than the regressions you actually care about, that is the useful answer: the task cannot be regression-tested at that N, so either raise N or accept the coarser resolution deliberately. Assumes roughly normal, independent runs.

(Same constant, same mistake, in two other threads this week. Correcting it wherever I put it.)

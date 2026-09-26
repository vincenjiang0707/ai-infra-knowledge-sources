# [Issue #3924] [Proposal] behavioral_drift: output integrity metric for detecting silent model collapse

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3924
state: open | updated: 2026-08-01T06:09:43Z
labels: 

## 正文

## Problem
Standard benchmarks measure task performance. But a model can score well on MMLU while output quality silently collapses — loss improves but outputs degenerate into repeating patterns. Perplexity misses this completely.

## Evidence
6-round Qwen2.5-1.5B fine-tuning: loss improved 9.13→8.78 but outputs collapsed to digit sequences. behavioral_drift scored 0.0 (correct). Perplexity missed entirely.

## Proposed Metric
Three deterministic signals, multiplicative drift_score (0-1):
1. self-BLEU — intra-output similarity (mode collapse detection)
2. digit_density_delta — numeric output spike vs baseline
3. repetition_ratio — unique/total token ratio (degeneracy detection)

One signal fails → total score 0. Additive gives misleading 0.67.

## Implementation
147 lines of Python, zero dependencies. Already submitted to huggingface/evaluate (PR #778). Can adapt to lm-eval-harness format — custom metric in lm_eval/api/metrics.py, or standalone contrib utility. Happy to implement whichever format maintainers prefer.

## 评论 (5)

### YuhaoLin2005 · 2026-07-10

## Update (July 11): additional evidence and context

Since the original proposal, the behavioral_drift metric now has:

1. **Causal experiment evidence**: n=30 between-subjects experiment (DeepSeek V4 Pro). Config rules causally shape agent output: WITH rule 73% vs WITHOUT 20%, odds ratio 11.0, Fisher exact p=0.0092. This directly supports the claim that output integrity metrics matter — when behavioral constraints fail silently, output quality degrades measurably.

2. **ECC merge**: The delivery-gate (quality verification) and growth-log (learning capture) components have been independently merged in ECC (226K stars, #2377/#2378) after full maintainer review.

3. **Prose Barrier framework**: We've formalized the structural constraint that makes behavioral_drift necessary — NL-based agents cannot independently verify their own output because verification and generation share the same channel. Filesystem-level checks (like drift_score) bypass this barrier.

4. **anthropics/skills pipeline**: The full quality pipeline (4 independent modules: pre-task calibration, persona-review, delivery-verification, neural-gate) is now submitted to the official Anthropic skills repository.

Happy to adapt the 147-line implementation to lm-eval-harness format whenever maintainers are ready.

### Kelvinz-89757 · 2026-07-28

Working on this — porting the `behavioral_drift` metric (self-BLEU × digit_density_delta × repetition_ratio, multiplicative composition) from huggingface/evaluate PR #778 into `lm_eval/api/metrics.py` as a `register_metric`/`register_aggregation` pair usable by any `generate_until` task via `metric_list`. Will open a PR shortly.

### YuhaoLin2005 · 2026-07-28

Really appreciate you taking this on. I read through your comment and the PR implementation carefully — here's the one thing I think will need design thought before the PR lands.

**The baseline reference problem.** The PR's API is `compute(predictions=ft_outputs, references=base_outputs)` — it needs base model outputs on the same prompts to compute digit_density_delta and repetition_ratio_baseline. The metric subtracts baseline digit density from FT digit density, so you can't skip this. But `generate_until` evaluates one model at a time — there's no second set of outputs available.

A few ways this could work in lm-eval-harness:

1. **Pre-computed reference file.** Store base model outputs as a dataset alongside the eval config. The metric loads references from disk instead of getting them from the eval loop. Cleanest separation, but adds a data dependency.

2. **Two-pass evaluation.** Run `generate_until` on the base model first, save outputs, then run on the FT model with those outputs as references. Works with existing infrastructure but doubles runtime.

3. **Degraded mode without baseline.** Let the metric run with references omitted, output only self-BLEU and repetition_ratio. digit_density_delta would be unavailable. Loses the strongest signal (digit degradation is how the Qwen2.5 collapse was caught) but lowers the barrier to entry.

The concatenated-reference self-BLEU should port cleanly — it only needs predictions, no references. Just needs to collect all outputs before computing (PR does a join-all-except-current approach, not per-example).

Happy to think through whichever path you prefer or review a draft PR. The 136-line reference implementation is at huggingface/evaluate#778 if you haven't looked at it yet.

### Kelvinz-89757 · 2026-07-30

PR is up: #3968

Quick summary of what's implemented, and where I landed on the baseline question:

- Ported the three signals and the multiplicative composition as-is (thresholds included) — no changes there.
- Kept self-BLEU as the dependency-free unigram-precision BLEU from the original PR rather than switching to `sacrebleu` (already a core dep here). Tried the swap first — `sacrebleu`'s brevity penalty actually inverts the mode-collapse signal under the concatenated-reference construction (identical/collapsed outputs score self-BLEU ≈ 0 instead of ≈ 1, since the artificially-lengthened reference tanks the BP). Wanted to flag that in case it's useful if anyone else tries the same swap elsewhere.
- For the baseline problem you raised: default behavior now uses the doc's own gold answer (`doc_to_target`) as the digit_density_delta baseline, since `generate_until` only has one model's outputs to work with per run. Added an optional `baseline_path` (set via `metric_list`) that takes a JSON list or newline-delimited file of real base-model outputs and uses those positionally instead — so if you run the base checkpoint first and save its outputs, you get the exact original semantics.

What I deliberately didn't build: automatic two-pass evaluation (running the base model as part of the same invocation). That's your option 2, and it'd need the evaluator to orchestrate two separate model runs in one command — a bigger change to the harness than this PR's scope, and probably worth its own design discussion rather than bundling into a metric PR.

Wanted to check with you before spending more time on it: is the manual pre-step (run base model once, save outputs, pass the file via `baseline_path`) an acceptable workflow for your use case, or is automatic two-pass evaluation something you'd actually want built out? Happy to open a separate issue for that if there's interest, but didn't want to assume.


### YuhaoLin2005 · 2026-08-01

Thanks for the port — nice work. The sacrebleu BP detail is a good catch; that's the kind of subtlety that silently changes a metric's meaning.

On your question: yes, `baseline_path` works for me as the v1 design. I run the base checkpoint first anyway, so the manual pre-step matches how I'd actually use it. And the `doc_to_target` default is fine as a fallback — you already flagged the gsm8k dilution yourself, so anyone on numeric tasks knows to bring their own baseline.

On two-pass: for my own use case, the manual pre-step is enough. I don't think it's worth opening an issue or building it preemptively; the proxy baseline only becomes a real problem once the metric gets actual adoption. If that demand shows up, I'd be glad to work on it with you.

One last thing: the CLA check on the PR is still showing `not_signed`. Could you sign it via the CLAassistant link when you get a chance? It's the only thing between the PR and a review.


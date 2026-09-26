# [Issue #4022] Feature request: EvalPort import/export for per-document samples and results

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/4022
state: open | updated: 2026-09-12T04:52:45Z
labels: 

## 正文

## Motivation

I maintain [EvalPort](https://github.com/adhabnr-ux/evalport), an open, schema-validated JSON interchange format for portable LLM evaluation test cases, graders, suites, and results — the idea being that eval datasets and results don't have to be locked to one framework's proprietary shape. It already has 24 tested adapter packages for other eval frameworks (Ragas, MLflow, LangSmith, TruLens, Hugging Face `evaluate`, and others).

`lm-evaluation-harness` is the harness most of the field already measures against — the numbers behind most open model cards and leaderboards come from it — so being able to move `simple_evaluate()` output in and out of a portable format seemed worth building for real rather than just proposing in the abstract. I already built and tested a standalone package that does this: [`lm-eval-harness-openeval-adapter`](https://github.com/adhabnr-ux/evalport/tree/main/adapters/lm-eval-harness-openeval-adapter), with 21 tests running real `simple_evaluate(model="dummy", ..., log_samples=True)` calls against real tasks (`copa`, `boolq`, `gsm8k`) and validated against EvalPort's real schema validators. It currently lives outside this repo entirely, and works fine that way — I'm not assuming this belongs upstream, just flagging that it exists and offering it in case there's interest, rather than only describing the idea.

Two concrete things worth mentioning about how it was built, since they might be relevant if this ever becomes a PR: I read `lm_eval/result_schema.py`'s `SampleResult` TypedDict as the reference shape, then verified against the actually-installed 0.4.12 package rather than trusting the docstring alone — and found two real discrepancies. `arguments`'s docstring describes a dict (`{"gen_args_N": {...}}`); the real returned value is a list of lists instead. And per-sample metric scores (`sample["exact_match"]`, `sample["acc"]`) come back as `numpy.float64`, not JSON-serializable `float`. Both are handled in the adapter, documented in its README, and I'd guess worth a look regardless of whether this feature request goes anywhere, since they're a real gap between the typed docstring and current behavior.

## Feature description

Optional `to_openeval()` / `from_openeval()` helpers (e.g. `lm_eval.evalport`) that take a `samples[task_name]` list — the per-document output of `simple_evaluate(..., log_samples=True)` — and produce/consume an EvalPort `Suite`/`ResultSet`. No changes to core evaluation logic; a pure data-shape converter sitting alongside the existing output writers.

```python
from lm_eval import simple_evaluate
from lm_eval.evalport import to_openeval, result_to_openeval  # proposed

results = simple_evaluate(
    model="hf", model_args="pretrained=your-model",
    tasks=["gsm8k"], log_samples=True,
)
samples = results["samples"]["gsm8k"]

# Portable suite -- test cases, real prompts, real targets, real gradable metrics.
suite = to_openeval("gsm8k", samples)
# Portable results -- one real per-document score per (metric, filter) pair,
# not an average or a fabricated per-example value.
result_set = result_to_openeval("gsm8k", samples, aggregate=results["results"]["gsm8k"])
```

`exact_match` (as used by `gsm8k` and others) maps directly onto EvalPort's own `exact_match` grader type; every other metric (`acc`, `acc_norm`, `f1`, task-specific metrics) maps to EvalPort's `custom` grader type with the real metric name and filter preserved, since fabricating required params for a grader type this module can't actually verify (e.g. a `semantic_similarity` threshold) isn't something I'm willing to do.

## Additional context

Full working reference: [adapters/lm-eval-harness-openeval-adapter](https://github.com/adhabnr-ux/evalport/tree/main/adapters/lm-eval-harness-openeval-adapter) (README has the full design writeup, including what round-trips losslessly and what doesn't — results only round-trip back to the original documents, not to a live `Task` object, since that needs a full YAML config and registered filters that aren't portable data). Spec: https://github.com/adhabnr-ux/evalport/blob/main/spec/SPEC.md. Happy to answer questions or scope this down if there's interest — and equally fine if this isn't a direction you want to take the harness in; the adapter works standalone either way.

## 评论 (2)

### omid511 · 2026-09-11

Spun the two docstring gaps you flagged into a small docs-only PR: #4137 (arguments shape + score types in SampleResult). No behavior change; the EvalPort feature direction itself is untouched and still yours to drive.

### adhabnr-ux · 2026-09-12

Thanks for spinning #4137 out of this — good catch pinning down the `arguments` shape and the numpy score-type gap in the actual docstrings rather than leaving it just in my adapter's README. Appreciate you keeping this issue itself untouched rather than closing it out from under the feature direction.

No urgency on a decision here — the adapter works fine standalone either way, so this stays open only as long as it's useful for the team to have around, not because anything's blocked on it. Happy to update it if `SampleResult`'s real shape changes again, or to help scope a smaller version of the proposal if the full `to_openeval()`/`from_openeval()` surface is more than you'd want to take on upstream.

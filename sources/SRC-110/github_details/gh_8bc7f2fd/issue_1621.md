# [Issue #1621] Proposal: EvalPort adapter for portable benchmark datasets (Sample / BenchmarkMeta)

source: https://github.com/modelscope/evalscope/issues/1621
state: closed | updated: 2026-08-26T02:20:19Z
labels: 

## 正文

Hi maintainers — I'm Sahi, maintainer of [EvalPort](https://github.com/adhabnr-ux/evalport), an open spec (JSON Schemas + Python/TS SDKs) for portable LLM eval test suites, test cases, and result sets. Read through `CONTRIBUTING.md`'s "Adding a New Benchmark" section and `evalscope/api/dataset`/`evalscope/api/benchmark` before writing this, so this is grounded in the actual adapter pattern rather than a generic pitch.

EvalScope's benchmark contract is genuinely clean: a `BenchmarkMeta(name=..., dataset_id=..., subset_list=..., metric_list=..., eval_split=...)` registered via `@register_benchmark`, paired with a `DataAdapter.record_to_sample()` that maps a raw dataset row to a `Sample`. That `record_to_sample -> Sample` boundary is basically the exact seam an EvalPort adapter needs.

Concretely, I think this could be a `evalscope/benchmarks/evalport/evalport_adapter.py` following your own documented pattern:

```python
from evalscope.api.benchmark import BenchmarkMeta, DefaultDataAdapter
from evalscope.api.dataset import Sample
from evalscope.api.registry import register_benchmark
from evalport_sdk import TestSuite

@register_benchmark(
    BenchmarkMeta(
        name='evalport',
        pretty_name='EvalPort Suite',
        dataset_id='local://path/to/suite.evalport.json',  # or a suite URL
        metric_list=['acc'],
        eval_split='test',
    )
)
class EvalPortAdapter(DefaultDataAdapter):
    def record_to_sample(self, record):
        # record is already an EvalPort TestCase dict — input/target map directly
        return Sample(input=record['input'], target=record['expected'])
```

...plus the inverse direction: exporting an EvalScope `Score`/`AggScore` run as an EvalPort ResultSet, so results are comparable across tools that also speak EvalPort (a few CLI harnesses have adopted it already).

Given EvalScope already evaluates LLM, VLM, and AIGC benchmarks with a registry that's designed for exactly this kind of pluggable adapter, this felt like a natural fit rather than a stretch. Spec: https://github.com/adhabnr-ux/evalport/blob/main/SPEC.md

No pressure — if this isn't a priority I understand, EvalScope has plenty going on. If it's interesting, I'm happy to send a PR that follows your Step 1-4 contribution flow (adapter dir, requirements.txt, docs) rather than just leaving this as talk. Thanks for the well-documented adapter pattern, it made this easy to scope.

## 评论 (4)

### Yunnglin · 2026-08-24

Hi Sahi — thanks for reading the adapter contract first; `record_to_sample()` → `Sample` is indeed the right seam. We're going to pass on a native adapter for now:

- **No code needed for import.** An EvalPort suite converts to JSONL and runs today via our existing `general_qa` / `general_mcq` / `general_vqa` adapters with `dataset_args`' `local_path` — no new registry entry required.
- **The spec can't express our core cases yet.** `TestCase.input` is `string | string[]`, so VLM / T2I / audio benchmarks have nowhere to go; there's also no counterpart for `Sample.choices`, `subset_key`, or `sandbox` / `files` (agentic tasks). On the result side our `AggScore` carries a structured `MetricIdentity` (aggregation + dimensions), pass@k over repeats, and a `num` that drops judge failures fail-closed rather than scoring them 0 — repeat/attempt representation is still open on your side (Discussion #22), so an export today would be lossy.
- **The benchmark hub overlaps.** 12 of the 14 suites already ship here with official prompts and scoring.

Suggestion: an `evalscope-openeval-adapter` in your own `adapters/`, same shape as the OpenCompass one. Our report JSON is a stable Pydantic schema (`Report`, `schema_version: 2`, under `outputs/<timestamp>/reports/`) — read it externally, nothing needed from us. Open an issue if anything there is ambiguous.

Worth revisiting once the spec covers multimodal inputs and repeat semantics, and a second framework reads/writes it natively.

(Two notes on the snippet: EvalScope has no `local://` scheme, and the field is `expected_output`.)


### adhabnr-ux · 2026-08-24

Thanks for the detailed breakdown, Yunlin — this is more useful than a "sure, let's add it" would have been.

We'll go with the JSONL + `general_qa`/`general_mcq`/`general_vqa` + `dataset_args.local_path` path as the documented interop story for now rather than pushing for a native adapter. I went through `docs/en/advanced_guides/custom_dataset/llm.md` and `evalscope/report/report.py` to make sure I understood the shape correctly before replying:

- `local_path` is a plain filesystem path passed through `dataset_args`, not a URI scheme — confirmed, no `local://`. My snippet was wrong to imply one; correcting that in EvalPort's own docs.
- On the field name: `Report` is exactly what you described — a Pydantic model with `schema_version: int = 2`, `extra='forbid'`, and a `model_validator` that hard-rejects anything that isn't `schema_version == 2`. That's a genuinely stable contract to read externally. My snippet used the wrong field name for EvalPort's own `TestCase` — it's `expected_output`, not what I had. Fixing that too.

On the spec gaps — these are real and on us, not framework-adapter gaps you're declining to paper over:
- `TestCase.input` being `string | string[]` genuinely has no home for VLM/T2I/audio inputs, or for `Sample.choices`/`subset_key`/sandbox-and-files. That's a spec limitation, not a missing adapter.
- Repeat/attempt representation: I opened Discussion #22 on this (attempt + isolation fields on Result, joined by `(test_case_id, run_id, attempt)`) after AgentVerity raised the same gap from a different angle in issue #20. It's mid comment-period right now, converging toward an additive `attempt`/`isolation` field pair rather than a `ResultSet` restructure — so "still open" is accurate, not "resolved, just not shipped." I'm not going to claim it covers your `AggScore`/`MetricIdentity`/pass@k/fail-closed-judge-num semantics yet; that's a separate, harder question about how much of your result-side structure the spec should even try to represent.

On the suggestion: an `evalscope-openeval-adapter` living in EvalPort's own `adapters/`, reading your `Report` JSON externally rather than needing anything from your side, is exactly the right shape given the schema is already stable and public — same pattern as the OpenCompass one. To be clear, that's not built yet; I'm noting it as the concrete next step once the input/repeat gaps above are closer to landing, not claiming existing work.

Appreciate you writing this up carefully instead of a one-line "not now." Will follow up here (or open a fresh issue) if anything in the `Report` schema turns out ambiguous once we actually get to building against it.

### Yunnglin · 2026-08-24

Closing since we've landed on the external-adapter path — the JSONL + `general_qa`/`general_mcq`/`general_vqa` route works today, and an `evalscope-openeval-adapter` reading our `Report` JSON needs nothing from this repo. Happy to reopen if the `Report` schema turns out ambiguous, or once the spec's multimodal/repeat gaps land and a native integration becomes worth revisiting. Thanks for the thoughtful proposal.

### adhabnr-ux · 2026-08-26

Thanks, Yunlin — appreciate the thoroughness throughout this thread. Will follow up if the `Report` schema turns out ambiguous once there's actually an `evalscope-openeval-adapter` being built against it.

— Sahi

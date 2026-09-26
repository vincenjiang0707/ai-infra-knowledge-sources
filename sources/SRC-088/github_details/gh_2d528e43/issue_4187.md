# [Issue #4187] `mmlu_*_generative` `get_response` compares the whole first line to the gold letter — models that prefix or explain their answer score exactly 0.000

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/4187
state: open | updated: 2026-09-19T02:33:34Z
labels: 

## 正文

**Minimal reproduction** (pure filter + metric, no API calls):

```python
from lm_eval.api.metrics import exact_match_hf_evaluate
from lm_eval.filters.extraction import RegexFilter, WhitespaceFilter
from lm_eval.filters.selection import TakeFirstFilter

chain = [RegexFilter(r"^(.*?)(?=\n|$)"), WhitespaceFilter(), RegexFilter(r"^(.*?)\s*$"), TakeFirstFilter()]
# filter a raw response through `chain`, then:
exact_match_hf_evaluate(predictions=[pred], references=["B"], ignore_case=True, ignore_punctuation=True)
```

(this mirrors `lm_eval/tasks/mmlu/generative/_default_template_yaml` → `filter_list: get_response`)

measured:

| raw response | filtered `pred` | `exact_match` vs `"B"` |
|---|---|---|
| `B` | `B` | **1.0** |
| `B.` | `B.` | **1.0** |
| `B. 4` | `B. 4` | **0.0** |
| `B. \(6x^2 + 4x + 6\)` | same | **0.0** |
| `ANSWER: B` | `ANSWER: B` | **0.0** |

**Observed at scale**: `mmlu_*_generative`, 10 subjects × 30 items, `--apply_chat_template`, two models
(`deepseek-flash`, `deepseek-v4-pro`), `num_fewshot 0`:

- reported **exact_match = 0.000 (0/298) for both models**;
- **0% of the 298 responses are empty** — the models answered, e.g. `B. 4` (letter plus option text) or `ANSWER: B`;
- judging the **same** raw responses with a letter-extraction scorer yields ≈0.73 for that run.

**Impact**: the task silently reports "the model cannot do MMLU" for any model that does not reply with a
bare letter, and the run gives no hint that the predictions were unparseable. Related: this is also why
models that enter a reasoning preamble before answering score 0 here.

**Suggested direction**: give the generative MMLU task the letter-extraction fallback used elsewhere in the
harness (or have `get_response` capture a leading `^[A-D]\b` group), and/or warn when a large fraction of
filtered predictions are not valid choices.

## 评论 (2)

### laa1991 · 2026-09-18

Follow-up: the reproducible material behind this report is now public — **https://github.com/laa1991/silent-zero**

- the one-command reproduction (same task, same prompt, same 16-token budget, only the endpoint changes: **0.0000 ↔ 0.9333**) is in the README;
- raw readings (wire-tapped request fields, `usage` counters, the firing census **with negative controls**) are under `evidence/`;
- `repro/check_silent_zero.py` applies the failure definition (success **and** collapsed **and** nothing said so) to any results file, and `repro/check_harness_specifics.py` reproduces the harness-specific parts **without any API calls**.

Happy to run anything on my side, or to open a PR if you want the fix landed.

### lindicaphxag-tech · 2026-09-19

PR #4188 implements the narrow fix discussed here: route generative MMLU answers through the existing multi-choice filter so prefixes such as `Answer: B` and `B. 4` resolve to the answer letter, with regression coverage against the real task configuration. The focused tests pass and the CLA check is green. Could a maintainer assign/review it?

# [Issue #3957] gsm8k: mutation study finds gaps in task-specific scoring tests

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3957
state: open | updated: 2026-08-06T20:59:03Z
labels: 

## 正文

### What this is, and what it is not

**This is not a bug report. The harness code is correct as written.** Every change described below is
a mutation *we* introduced deliberately, as part of a mutation-adequacy study of the test suite.
Nothing here says lm-evaluation-harness computes anything wrong today, and we are not claiming any
published number is wrong.

What it reports is a **test sensitivity gap**: a class of change that alters reported gsm8k numbers
and that the existing suite does not detect. If such a change arrived by accident — an innocuous
config edit, a refactor, a dependency bump changing a default — CI would stay green and the resulting
scores would be wrong with no signal.

We are offering tests, not a fix, because there is nothing to fix.

All harness code and suite claims below are pinned to
`f4d4b3de3ee6741a7151a9fe74945ee515262f4c`.

### The short version

We broke the gsm8k pipeline 26 different ways and ran the disclosed pytest invocation against each.
The pattern in this corpus was not the one we expected, and we think it is worth testing
prospectively:

> **The caught mutations cluster on shared primitives and prompt assembly; effect magnitude does not
> separate caught from missed mutations.**

Break `lm_eval/api/metrics.py::mean` — a shared registered aggregation — and 8–11 tests fail,
depending on the mutation. Break gsm8k's declared extraction, normalization, or task-specific metric
settings, and none of those mutations is caught, however large the effect on the score. In this
corpus, the suite protects shared primitives well and the task-specific scoring surface not at all.

The sharpest illustration: **a mutation that drives reported gsm8k accuracy to exactly zero leaves
the disclosed suite invocation green.**

### The zero-accuracy demonstration

We changed `doc_to_target` so the answer after the final marker passes through Jinja's integer
coercion and then has one added. The operator's intended shape is “gold plus one,” but external audit
caught a real qualification: Jinja does not parse comma-formatted numbers. In the frozen sample,
**document 146** has the target `2,125`; under this mutation **`2,125` becomes `1`** rather than
receiving the intended increment. The accurate description is therefore that the mutation rewrites
every measured gold, usually by adding one.

**The item-level part.** On both measured models, no answer that was correct before the rewrite
remains correct afterwards. This is an executed per-document result, not a universal impossibility
claim. Some predictions do match newly rewritten targets.

**The stub-specific part.** These figures come from a *deterministic stub model* over a frozen
200-document sample, not from a model run. Read them as "the pipeline's scoring collapsed", not as an
accuracy measurement of any real system:

```
exact_match,flexible-extract     0.6900  ->  0.0000     (stub model, 200 documents)
exact_match,strict-match         0.4250  ->  0.0000     (stub model, 200 documents)
```

**And what real models do.** We reran the same 200 documents on CPU with two models your own tests
use — `pythia-70m`, which is what `Test_HFLM` builds and therefore what `test_generate_until` asserts
on, and `pythia-14m-deduped`, used by `tests/test_evaluator.py`:

```
                                 unmutated      under the mutation
pythia-70m       strict-match     0.0000    ->   0.0000
                 flexible-extract 0.0200    ->   0.0000
pythia-14m-ded.  strict-match     0.0000    ->   0.0000
                 flexible-extract 0.0150    ->   0.0100
```

On `pythia-70m` the flexible score does go to exactly zero, so the collapse is not an artifact of our
stub. On the 14M model it lands at 0.0100 instead, and the reason is worth seeing:

```
pythia-70m       correct unmutated [4, 52, 53, 96]    under D1 []
pythia-14m-ded.  correct unmutated [92, 144, 186]     under D1 [146, 152]
```

**In both cases the intersection is empty.** Not one previously-correct answer survived. The 14M
model's residual 0.0100 is not partial preservation: it is two *different* documents matching the
rewritten targets. One is document 146's malformed target `1`; the aggregate cannot distinguish that
from an intended arithmetic rewrite.

So the item-level result holds on both measured models, and the aggregate is the part that varies:
on one model the rewrite shows as `0.0200 → 0.0000`, on the other as
`0.0150 → 0.0100`, which looks like rounding noise. Either way the disclosed suite invocation stays
green.

The suite command disclosed below reports `607 passed, 14 skipped, 0 failed` afterwards, identical
to baseline. That result involves no deterministic stub; it is pytest against a mutated harness,
including the model-backed test discussed below.

**To be clear about what we are and are not asking.** We are *not* asking you to validate dataset
contents or to defend gold answers you do not own — the gsm8k answers come from upstream and that is
reasonably not your responsibility. We use this mutation only as a probe: it deliberately changes
every gold answer in the measured sample, and what it demonstrates is a property of the test rather
than of the data:

`tests/models/test_huggingface.py::Test_HFLM::test_generate_until` is the only test that exercises
real gsm8k task output in a standard environment. (`test_vllm.py` calls `importorskip("vllm")`,
`test_sglang.py` is `skipif(not torch.cuda.is_available())`, and `test_hf_steered.py` is
unconditionally skipped for a documented CI dependency conflict, so three of the four modules that
build gsm8k requests skip.)

That test **does** see this change. All ten of the prompts it builds differ under the mutation: the
few-shot exemplar answers move from `#### 12` to `#### 13`. It passes anyway, because it does not
assert on prompts. It caps each generation at ten tokens and asserts ten generated strings from
`pythia-70m`; none of those asserted outputs moves.

So the coverage that test provides for the request path looks **incidental rather than structural**.
It fires when a prompt perturbation happens to shift one of ten asserted outputs from a small model —
dropping a whole few-shot exemplar does — and not otherwise.

**How much evidence is behind that, stated plainly.** Of every mutation where we measured whether
the asserted outputs moved, **all three that left them unchanged survived, and both that moved them
were caught.** The three survivors are D1 and two follow-up templates intended to subtract one from
or multiply numeric golds by ten. The arithmetic labels are not global guarantees: their Jinja
integer coercion also mishandles comma-formatted values. On the ten requests actually measured, all
three mutations change every prompt and none changes any generated string asserted by the test.

Taken together, D1 and the three arithmetic follow-up mutants are four variants of one mutation
shape — rewriting `doc_to_target` through Jinja integer coercion — not independent observations:
three left the asserted outputs unchanged and survived, while the fourth moved one asserted output
and was caught, so the interesting result is the unpredictable detection boundary within a single
shape.

One prediction failed and is worth reporting: the template intended to add *one thousand* to numeric
golds **did** move one asserted output, and was caught. So `× 10` preserves every asserted output and
`+ 1000` does not on the ten requests measured, for reasons we cannot currently predict — which is
the content of calling this coverage *incidental* rather than structural. Two mutations of the same
shape land on opposite sides of the detection boundary.

This designed same-shape set is not a rate, and we are not offering it as one.

It is still the part we would most like a maintainer's opinion on, and where we would most welcome
being told we have over-read it.

### What we measured

Each mutation was separately confirmed to change real pipeline output before its suite result was
interpreted, so none of them is a no-op:

The corpus-level accuracy effects compared in this section come from a deterministic stub model over
a frozen 200-document sample. The "caught / not caught" column is the disclosed pytest invocation
against a mutated harness and involves no stub.

| Mutation | Touches | Suite |
| --- | --- | --- |
| weighted or truncated `mean` (4 variants) | shared aggregation | **caught**, 8–11 tests each |
| `num_fewshot` 5 → 4, → 3, → 1 | prompt assembly | caught |
| whitespace on `doc_to_target` (2 variants) | prompt assembly | caught |
| few-shot delimiter (2 variants) | prompt assembly | caught |
| rewrite final gold through integer coercion, then add one | prompt assembly + scoring | **not caught** |
| drop the `#### ` anchor from strict-match | gsm8k config | **not caught** |
| drop only the *space* from that anchor | gsm8k config | **not caught** |
| `flexible-extract` `group_select` −1 → 0 | gsm8k config | **not caught** |
| `ignore_punctuation` false → true | gsm8k config | **not caught** |
| drop `,`, `\$`, or `\.$` from `regexes_to_ignore` | gsm8k config | **not caught** |
| equality → containment in `exact_match_hf_evaluate` (3 variants) | metric | **not caught** |
| equality → numeric tolerance in `exact_match_hf_evaluate` (2 variants) | metric | **not caught** |
| drop the Bessel correction in `sample_stddev` | metric | **not caught** |
| `sample_stddev` divides by `n + 1` | metric | **not caught** |

Every "not caught" row ran:

```bash
python -m pytest -n=auto \
  --ignore=tests/models/test_openvino.py \
  --ignore=tests/models/test_hf_steered.py \
  --ignore=tests/scripts/test_zeno_visualize.py
```

and produced `607 passed, 14 skipped`. That is your documented command plus two further explicit
ignores: `test_hf_steered.py` is already unconditionally module-skipped, and the zeno script's
dependencies were unavailable. We state the command so the count is reproducible rather than
approximate.

The `mean` row is the one that shows the pattern. It is the only score-path family that gets caught,
because `test_aggregation_pipeline.py`, `test_evaluator_utils.py`, `test_utils.py`, `test_metrics.py`
and `test_misc.py` all reach it — and the two smallest reported-accuracy changes among mutants whose
accuracy moved are `mean` mutants that get caught, at 0.0021 and 0.0033.

The size of the effect carries no information about whether it is caught. Measured over the mutants
where a reported accuracy moved — **all magnitudes below are from the deterministic stub over the
frozen 200 documents, not from a model run**, so treat them as relative sizes within one controlled
setting rather than as accuracies:

```
smallest caught  0.002136      smallest missed  0.005000
largest  caught  0.690000      largest  missed  0.690000
```

The ranges overlap completely, so no threshold on effect size separates caught from missed. The
cleanest case is an exact tie: adding whitespace to `doc_to_target` and D1's integer-coercion rewrite
both move a reported accuracy by exactly `0.690000`. The first is caught and the second is not. Same
magnitude, same part of the pipeline, opposite outcomes — the difference is only whether the prompt
change happens to shift one of the ten generated strings `test_generate_until` asserts on.

### The uncovered surface, concretely

**1. No native assertion pins gsm8k's declared scoring rules.**

```bash
grep -rn --include='*.py' regexes_to_ignore tests/ | wc -l   # 0
grep -rn --include='*.py' group_select tests/ | wc -l        # 0
```

The four `regexes_to_ignore` rules each reconcile a real formatting difference between what models
emit and how golds are written. Removing the `,` rule alone turns a correct answer into a wrong one:

```bash
python - <<'PY'
from lm_eval.api.metrics import exact_match_hf_evaluate as em
rules = [",", r"\$", "(?s).*#### ", r"\.$"]
kw = dict(ignore_case=True, ignore_punctuation=False)
for label, rs in (("all four rules", rules), ("without the comma rule", rules[1:])):
    got = em(predictions=["1234"], references=["#### 1,234"], regexes_to_ignore=rs, **kw)
    print(f"{label:24s} {float(got['exact_match'])}")
PY
```

```
all four rules           1.0
without the comma rule   0.0
```

The suite does load `gsm8k.yaml` when its model tests build requests, but those tests do not assert on
these scoring settings. `tests/test_filters.py` does not cover the extraction side either: it exercises
`MultiChoiceRegexFilter`, which subclasses `RegexFilter` but overrides `apply`, using patterns it
defines itself. So neither `RegexFilter.apply` nor gsm8k's declared patterns are reached by it.

**2. No native test names `exact_match_hf_evaluate`.** Replacing its equality test with containment,
or with a numeric tolerance, changes scores in the frozen record and passes.

**3. `sample_stddev` is covered, but by a test that cannot see the change.** This is the most
interesting of the three, because it is an insensitive test rather than a missing one.

Dropping the Bessel correction makes every reported stderr too small by a factor depending only on
sample size, not on the data, since the sum of squared deviations cancels:

```
relative error = 1 - sqrt((n-1)/n)
at n = 200     = 0.250313%
```

`tests/test_misc.py::test_bootstrapping` compares `mean_stderr` against a bootstrap estimate with
`abs=1e-4` on 1000 uniform samples. Under the mutation, at its own setup:

```bash
python - <<'PY'
import math, random
random.seed(42)
arr = [random.random() for _ in range(1000)]
mu = sum(arr)/len(arr); sq = sum((x-mu)**2 for x in arr)
pinned = math.sqrt(sq/999)/math.sqrt(1000)
for name, d in (("drop the correction (n)", 1000), ("divide by n+1", 1001)):
    moved = abs(pinned - math.sqrt(sq/d)/math.sqrt(1000))
    print(f"{name:26s} moves {moved:.3e}  = {100*moved/1e-4:.2f}% of the 1e-4 tolerance")
PY
```

```
drop the correction (n)    moves 4.552e-06  = 4.55% of the 1e-4 tolerance
divide by n+1              moves 9.097e-06  = 9.10% of the 1e-4 tolerance
```

The tolerance is about 22 times the first effect and 11 times the second, so doubling the error does
not help. The correction scales stderr by `sqrt(n/(n-1))`, `1.00050038` at `n = 1000`, and that shift
*shrinks as n grows*, only exceeding `1e-4` on uniform data below about **n = 127**:

```bash
python -c "
import math
print(max(n for n in range(2,100000) if (0.2887/math.sqrt(n))*(1-math.sqrt((n-1)/n)) >= 1e-4))"
# 127
```

The tolerance is not loose by oversight: a test written against a bootstrap estimate cannot be
tighter than bootstrap noise. Catching this needs an exact assertion, not a tightened tolerance.

### What we are proposing

A PR adding score-path tests that read gsm8k's declared config rather than restating it, so a change
to `gsm8k.yaml` reaches the assertion, plus one exact `sample_stddev` test next to
`test_bootstrapping`. No dataset, no model, no network. Details in the PR.

Those tests address items 1 to 3 above. They deliberately do **not** try to address the
`test_generate_until` insensitivity, because we do not think an outside contributor should pick that
design. The options range from asserting on the assembled prompts rather than only on generated text,
to raising `max_gen_toks`, to leaving it as a smoke test and accepting that request-path coverage is
incidental. That is a maintainer's call and we would rather ask than guess.

### Scope and honesty notes

- One task family, gsm8k, at pinned commit
  `f4d4b3de3ee6741a7151a9fe74945ee515262f4c`. We have not checked whether other tasks share this
  shape, though the structure of the suite suggests they might.
- We chose the mutations. 26 is a small sample and a different set might behave differently.
- The "sharedness rather than magnitude" reading is **exploratory**: we formed it after seeing these
  results, not before, so it is a hypothesis worth testing prospectively rather than a finding we can
  claim. What is solid is the table.
- We introduced every mutation described. None was found in the wild.
- We are outside contributors doing a study, not reporting a production incident.

## 评论 (2)

### Arnav66692 · 2026-07-29

A sharper statement of the core result, which the original framing understated.

Of twelve mutations to gsm8k's configured extraction and scoring semantics, the suite caught zero. None of the eleven mutations it did catch came from a test asserting those semantics: seven were generated-output snapshot comparisons and four were collateral assertions on a shared aggregation primitive.

The gap is not confined to task configuration. Seven of the surviving mutations edit shared code in `lm_eval/api/metrics.py` rather than `gsm8k.yaml`. Those are the equality comparison and the standard-error computation that gsm8k's scoring routes through, and neither is gsm8k-specific.

The clearest single case is a matched pair on line 11 of `gsm8k.yaml`. Two edits to the same declaration produce an identical measured accuracy delta of 0.690000 under a controlled workload, and receive opposite outcomes. The difference is whether the change happens to shift the tokens a generated-output snapshot compares.


### Arnav66692 · 2026-08-06

Opened #3983 carrying the first batch of regression tests from this study: the gsm8k
extraction and scoring semantics described above, as one new file `tests/test_gsm8k_scoring.py`.
Tests only, no behavior change. Each test was re-verified this week on a fresh clone of current
main, failing against the mutation it pins and passing unmutated, with the full suite green before
and after.

A second, smaller PR will follow for the stderr finite-sample correction, which also relates to
#3966.


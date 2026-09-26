# [Issue #3930] [Bug] afrixnli prompt_1: doc_to_text uses .format() braces, so premise and hypothesis are never substituted (35 tasks)

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3930
state: closed | updated: 2026-08-10T11:31:32Z
labels: 

## 正文

## Summary

The `afrixnli_*_prompt_1` tasks (both `direct/` and `translate/`) declare an inline `doc_to_text` that uses Python `.format()` placeholder syntax (`{premise}`, `{hypothesis}`). `doc_to_text` is rendered through Jinja2, where single braces are literal text and double braces are required for substitution.

The prompt sent to the model therefore contains the literal strings `{premise}` and `{hypothesis}` rather than the document content. The model is asked to perform natural language inference on an empty stem.

The task raises no error and produces a plausible-looking number, which is likely why this has gone unnoticed.

**Version:** lm_eval 0.4.13.dev0, editable install from main at commit `97a5e2c7`
**Environment:** Python 3.12, CPU-only torch, Linux

## Reproduction

```bash
lm_eval --model hf \
  --model_args pretrained=EleutherAI/pythia-160m \
  --tasks afrixnli_swa_prompt_1 \
  --limit 1 --device cpu \
  --log_samples --output_path ./audit/
```

The rendered `arg_0` from the samples file:

```
Please identify whether the premise entails or contradicts the hypothesis in the following premise
and hypothesis. The answer should be exact entailment, contradiction, or neutral.

Premise: {premise}
Hypothesis: {hypothesis}

Is it entailment, contradiction, or neutral?
```

The `doc` in the same record, showing the content that should have been substituted:

```json
{
  "premise": "Naam, sikukuwa nafikiri juu ya hilo, lakini nilichanganyikiwa sana, na, hatimaye nikaendelea kuzungumza naye tena.",
  "hypothesis": "Sijaongea na yeye tena.",
  "label": 2
}
```

For contrast, `afrixnli_swa_prompt_3` renders correctly and does include the Swahili premise and hypothesis.

## Impact

The task is `output_type: multiple_choice` with three continuations. Since the prompt is identical for every document, the score collapses to the model's prior over the label words.

Measured on `afrixnli_eng_prompt_1` with `Qwen/Qwen2.5-0.5B`, `--limit 200`, CPU:

| metric | value |
|---|---|
| acc | 0.3300 (± 0.0333) |
| f1 | 0.1638 |

Accuracy is at chance for a balanced three-class task. The weighted F1 of 0.1638 is the arithmetic signature of a single degenerate prediction across all examples: always predicting one class on a balanced three-class set yields weighted F1 of 1/6, or 0.1667.

English is used here as a control, since it rules out "the model does not know the language" as an explanation.

## Root cause

In `lm_eval/tasks/afrixnli/gen_utils.py`, the `prompt_map` writes the placeholders differently for `prompt_1` than for the others:

```python
"prompt_1": "... The answer should be exact entailment, contradiction, or neutral.\n\n"
            "Premise: {premise}\nHypothesis: {hypothesis}\n\n"     # single braces
            "Is it entailment, contradiction, or neutral?",

"prompt_3": f"Given the following premise and hypothesis in {lang}, ..."
            "Premise: {{premise}} \nHypothesis: {{hypothesis}}",     # double braces, correct
```

Prompts 3, 4 and 5 place the placeholders in a plain (non f-string) fragment using double braces, so they survive into the generated YAML. Prompt 1 uses single braces in the same position. Prompt 2 receives no inline `doc_to_text` and falls through to the template.

Two things compound this:

1. The `afrixnli_yaml` template contains no `doc_to_text` key, so the broken inline string is the only one in the resolution chain. There is nothing to fall back to.
2. `lm_eval/tasks/afrixnli/direct/prompt_1/utils.py` defines a correct `doc_to_text` function using `.format()`, but nothing references it. It is dead code.

## Scope

- `lm_eval/tasks/afrixnli/direct/prompt_1/afrixnli_*.yaml` (18 languages)
- `lm_eval/tasks/afrixnli/translate/prompt_1/afrixnli_translate_*.yaml` (17 languages)

Total 35 tasks. Not affected: prompt_2 through prompt_5 in either mode, and the `anli prompt/` and `lai prompt/` task families.

Introduced in #2825.

I have not verified whether any published results were produced through this code path, and I make no claim about them. This report is limited to what the harness renders today.

## Proposed fix

Change the `prompt_1` entry in `gen_utils.py` to Jinja braces, matching prompts 3 through 5, then regenerate the affected YAMLs with the existing generator rather than hand-editing:

```bash
python gen_utils.py --output-dir ./direct    --mode prompt_1 --overwrite
python gen_utils.py --output-dir ./translate --mode prompt_1 --overwrite
```

An alternative is to add `doc_to_text: !function utils.doc_to_text` to the templates and drop the inline strings, which would also revive the currently dead `utils.doc_to_text`. That is a larger change and would need the same treatment for the other prompts.

Happy to open a PR. Which approach would you prefer?


## 评论 (2)

### chuenchen309 · 2026-07-16

Confirmed independently — and the root cause is a single line in the generator, not the 35 YAMLs themselves.

`lm_eval/tasks/afrixnli/gen_utils.py` → `prompt_func()` builds `doc_to_text` for every language, and `prompt_1` is the only entry in `prompt_map` still using single-brace `.format()` placeholders:

```python
"prompt_1": "...Premise: {premise}\nHypothesis: {hypothesis}\n\n...",  # single braces → literal under Jinja2
"prompt_3": "...Premise: {{premise}} \nHypothesis: {{hypothesis}}",     # double braces → substituted
"prompt_4": "...{{premise}} ... {{hypothesis}}",
"prompt_5": "...{{premise}} ... {{hypothesis}}",
```

`gen_lang_yamls()` writes that string verbatim into `doc_to_text:` of each generated file (the `prompt_func(mode, ...)` call), which is exactly why every committed `*_prompt_1` YAML (both `direct/` and `translate/`) carries the un-substituted `{premise}`/`{hypothesis}` while prompt_3/4/5 render fine.

So the fix is `{premise}`→`{{premise}}` and `{hypothesis}`→`{{hypothesis}}` in the `prompt_1` template, **then regenerate** — patching only the 35 YAMLs would be silently undone the next time `gen_utils.py` runs. Happy to open a PR for this if nobody is already on it.

### chuenchen309 · 2026-07-16

Update: #3932 already implements exactly this — it flips all 35 `prompt_1` YAMLs (direct + translate) to `{{premise}}`/`{{hypothesis}}` **and** updates `gen_utils.py`, so the generator-regression concern is covered too. No separate PR needed from me; that one looks complete.

# [Issue #3493] Standardizing Task Formats

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3493
state: open | updated: 2026-08-15T16:54:28Z
labels: 

## 正文

Task configuration in lm-eval can sometimes feel more complex than it needs to be. Tasks implementing the same pattern across and within formats (multiple choice, generation, chain-of-thought) end up with minor variations, but you still need completely separate configs for each. We're proposing a "presets" system to standardize common patterns and want community input on the design.

Switching, say, from log-likelihood scoring to generation requires rewriting most of your task config. For example, here's what it takes to convert MMLU from labeled MCQ format to cloze format:

```yaml
# MCQ format - labeled choices A, B, C, D
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nA. {{choices[0]}}\nB. {{choices[1]}}\nC. {{choices[2]}}\nD. {{choices[3]}}\nAnswer:"
doc_to_choice: ["A", "B", "C", "D"]
doc_to_target: answer
```

```yaml
# Cloze format - full text choices, no labels
output_type: multiple_choice
doc_to_text: "{{question.strip()}}\nAnswer:"
doc_to_choice: "{{choices}}"
doc_to_target: "{{choices[answer]}}"
```

Three jinja fields change (and additionally setting the metrics) for what's conceptually a one-line decision: "use cloze format instead of MCQ." In practice, this means maintaining separate task files for each, and the inevitable duplication and drift.

MMLU alone has multiple variants that differ mainly in prompting style, and the names don't make clear which is which. This makes it hard to choose the right one, compare results across papers, or apply consistent prompting for chat and reasoning models.

## Presets

With presets, your task config only specifies the data mapping:

```yaml
# Your task specifies the data mapping once
doc_to_text: question
doc_to_choice: choices
doc_to_target: answer

# Set the default preset
presets: mcq
```
And the preset handles all the format-specific details: prompt structure, target formatting, answer extraction, and metrics.

### Runtime Selection

Tasks will support multiple presets, selected at runtime:

```bash
lm_eval --tasks mmlu --preset mcq       # log-likelihood scoring
lm_eval --tasks mmlu --preset generate  # generation-based
lm_eval --tasks mmlu --preset cot       # chain-of-thought
```
All variants live in one place, so you're not hunting through separate files to find the right one. This also makes it easy to switch between log-likelihood and generation, which has been a common pain point when running MCQ tasks against API models. 

### Available Presets

We're starting with four common formats:

| Preset | Output Type | Description |
|--------|-------------|-------------|
| `mcq` | `multiple_choice` | Standard A/B/C/D format with log-likelihood scoring. |
| `cloze` | `multiple_choice` | Full text choices without labels. |
| `generate` | `generate_until` | Model generates an answer, which is extracted and matched. |
| `cot` | `generate_until` | Chain-of-thought reasoning before answering. |

## Open Questions

Presets cover common patterns and are not meant to handle every case. For tasks that need custom prompt structures or answer extraction, full task configs remain available.

One open question is the right balance for user customization? We could allow overriding a range of fields, such as instructions or choice labels:

```yaml
presets:
  type: mcq
  instruction: "Answer the following question."
  choice_labels: ["1", "2", "3", "4"]
```

But more complexity starts to defeat the purpose of standardization. The last thing we want is yet another language syntax layer to  for users to learn.

Few-shot examples are another consideration. If your examples look like:

```
Q: What is the capital of France?
A: B
```

...and you switch to `cot`, the model sees direct answers but gets prompted to "think step by step", a mismatch thats not really appropriate. 

Some implementation details we'd especially like feedback on:

1. Chat and reasoning models: What prompting patterns have worked well for you? Are there conventions we should adopt as defaults?

2. Customization depth: What's the right balance between flexibility and simplicity?

3. Task inheritance: How should presets interact with task groups and inheritance? Should child tasks be able to override a parent's preset?

4. Missing formats: Are there evaluation patterns beyond mcq, cloze, generate, and cot that would benefit from preset support?

## 评论 (1)

### seva9523 · 2026-08-15

Hi — the presets proposal looks like a strong candidate for a semantic compatibility check.

I maintain [[EvalRepro](https://github.com/seva9523/EvalRepro)](https://github.com/seva9523/EvalRepro), an Apache-2.0 tool and GitHub Action for comparing materialized AI-evaluation inputs and task contracts. Rather than asking the project to adopt anything, I’d like to volunteer a bounded, fork-side pilot on one MMLU variant: compare the existing explicit configuration with its preset-generated equivalent and produce hash-only manifests for sample membership and order, rendered prompt/query, choices, target, and task metadata.

The aim would be to give this design discussion reviewable evidence about what remains identical and what changes intentionally. I recently used the same method to compare 22,773 records across seven evaluation surfaces; the methodology and limitations are public in [[this case study](https://github.com/seva9523/EvalRepro/discussions/27)](https://github.com/seva9523/EvalRepro/discussions/27).

If that would be useful, which MMLU format pair and contract fields would you consider the best first pilot? I can keep the work self-contained in a draft PR and label the result `fork-validated` unless and until maintainers review it.

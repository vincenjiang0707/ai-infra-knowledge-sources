# [Issue #4230] MultiChoiceRegexFilter fallback matches "Note: All" as answer A (no word boundary), overriding the real answer in flexible-extract

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/4230
state: open | updated: 2026-09-25T07:07:14Z
labels: 

## 正文

### Summary

In `MultiChoiceRegexFilter`, the last-resort fallback pattern `:[\s]*(A|B|C|D)` has no word boundary after the letter. Any `"<Label>: <Word starting with A-D>"` line counts as an answer. Tasks whose `flexible-extract` uses `group_select: -1` keep the *last* match, so a trailing "Note: ..." or "Explanation: ..." line overrides the model's actual answer.

### Reproduction

Tested on main @ d6de8164. The filter settings are the ones gpqa's `flexible-extract` uses.

```python
from lm_eval.filters.extraction import MultiChoiceRegexFilter

f = MultiChoiceRegexFilter(regex_pattern=r"(\([A-Z]\))", group_select=-1,
                           ignore_case=True, ignore_punctuation=True)
doc = {"choices": ["2.4 eV", "3.1 eV", "0.8 eV", "5.6 eV"]}
for resp in [
    "Let's compute the band gap step by step.\nAnswer: B\nNote: All energies are rounded.",
    "Final answer: C\nExplanation: Because the photon energy exceeds the gap.",
    "Answer: D",
]:
    print(repr(resp), "->", f.apply([[resp]], [doc])[0][0])
```

Output:

```
'...Answer: B\nNote: All energies are rounded.' -> (A)    # expected (B)
'Final answer: C\nExplanation: Because the photon...' -> (B)  # expected (C)
'Answer: D' -> (D)
```

### Where

- `lm_eval/filters/extraction.py:227-229`: `rf":[\s]*({without_paren_fallback_regex})"`
- The same code is copied in:
  - `lm_eval/tasks/bbh/zeroshot/utils.py:212`
  - `lm_eval/tasks/bbh/cot_zeroshot/utils.py:212`
  - `lm_eval/tasks/mmlu/flan_cot_zeroshot/utils.py:93`
  - `lm_eval/tasks/mmlu/flan_n_shot/generative/utils.py:93`

Affected scores: the `flexible-extract` filter of gpqa (cot_zeroshot / cot_n_shot / generative), mmlu flan_cot_zeroshot and flan_n_shot generative, and bbh zeroshot / cot_zeroshot.

### Proposed fix

Add `\b` after the letter group, i.e. `rf":[\s]*({without_paren_fallback_regex})\b"`, in all 5 places. I compared extractions before and after the change on 34 realistic outputs across the 5 copies:

- Unchanged: "Answer: B", "Answer:B)", "Answer: B.", "Answer: D. Because ...", "Final Answer: C", "ANSWER: A" and the answers matched by the `(X)` / choice-text patterns.
- Fixed: the "Note: ...", "Explanation: ..." and "Caveat: ..." trailing-line cases now give the correct letter.
- Behavior change to review: "Answer: AB" and "Answer: B2" now give `[invalid]` instead of the first letter. I think that is the safer behaviour, but happy to adjust.

I have a patch with regression tests in `tests/test_filters.py` (for the core filter and both bbh copies) and would be glad to open a PR if this approach looks right.

*Disclosure: this report was prepared with an AI assistant (Claude), which ran the reproduction and drafted the text; posted by me.*

## 评论 (3)

### tk1475 · 2026-09-25

@lucaluo925, since you mentioned you have a patch: note that the same fallback regex `:[\s]*(A|B|C|D)` is copied into four task utils besides `lm_eval/filters/extraction.py`: `lm_eval/tasks/bbh/zeroshot/utils.py`, `lm_eval/tasks/bbh/cot_zeroshot/utils.py`, `lm_eval/tasks/mmlu/flan_cot_zeroshot/utils.py` and `lm_eval/tasks/mmlu/flan_n_shot/generative/utils.py`. Adding `\b` after the letter group fixes all of them. I checked that against your repro plus a couple of controls ("Answer: B" still matches, "Explanation: A..." no longer does). I'm happy to share the parametrized test if it helps your PR.


### lucaluo925 · 2026-09-25

Thanks @tk1475, this is a helpful catch. I’ve checked and confirmed the same fallback regex exists in these four additional utils files on the main branch. I will fix all five occurrences together in the PR by adding `\b` after the letter group to align the behavior. Your parameterized test is welcome; feel free to paste it here or share a gist. I will include it in the PR and credit you in the PR description. I will wait for maintainer sign-off on the fix direction before opening the PR.

### tk1475 · 2026-09-25

Here it is. It goes at the end of `tests/test_filters.py` and needs `import importlib.util` and `from pathlib import Path` at the top, if they aren't there already. On `main`, the "Note:" and "Explanation:" cases fail for the core filter and all four task copies. The "Answer: D" and "Answer: B." cases are controls that pass either way.

```python
# The bare-letter fallback `:\s*(A|B|...)` had no word boundary, so any trailing
# "Label: Word" line whose word starts with a choice letter ("Note: All",
# "Explanation: Because") was read as an answer and, with group_select=-1,
# overrode the real one.
BARE_LETTER_CASES = [
    ("Let's compute.\nAnswer: B\nNote: All energies are rounded.", "(B)"),
    ("Final answer: C\nExplanation: Because the photon energy exceeds it.", "(C)"),
    ("Answer: D", "(D)"),
    ("Answer: B.", "(B)"),
]


@pytest.mark.parametrize(("resp", "expected"), BARE_LETTER_CASES)
def test_multi_choice_regex_bare_letter_fallback_needs_word_boundary(resp, expected):
    filt = MultiChoiceRegexFilter(
        regex_pattern=r"(\([A-Z]\))",
        group_select=-1,
        ignore_case=True,
        ignore_punctuation=True,
    )
    docs = [{"choices": ["2.4 eV", "3.1 eV", "0.8 eV", "5.6 eV"]}]

    assert filt.apply([[resp]], docs) == [[expected]]


@pytest.mark.parametrize(
    "task_utils",
    [
        "bbh/zeroshot",
        "bbh/cot_zeroshot",
        "mmlu/flan_cot_zeroshot",
        "mmlu/flan_n_shot/generative",
    ],
)
@pytest.mark.parametrize(("resp", "expected"), BARE_LETTER_CASES)
def test_task_multi_choice_regex_bare_letter_fallback_needs_word_boundary(
    task_utils, resp, expected
):
    # bbh and mmlu keep their own copies of MultiChoiceRegexFilter. bbh reads the
    # choices from doc["input"], mmlu from doc["choices"].
    path = Path(__file__).parent.parent / f"lm_eval/tasks/{task_utils}/utils.py"
    spec = importlib.util.spec_from_file_location(
        task_utils.replace("/", "_") + "_utils", path
    )
    utils = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(utils)

    filt = utils.MultiChoiceRegexFilter(
        regex_pattern=r"(\([A-Z]\))",
        group_select=-1,
        ignore_case=True,
        ignore_punctuation=True,
    )
    docs = [
        {
            "input": "Options:\n(A) 2.4 eV\n(B) 3.1 eV\n(C) 0.8 eV\n(D) 5.6 eV",
            "choices": ["2.4 eV", "3.1 eV", "0.8 eV", "5.6 eV"],
        }
    ]

    assert filt.apply([[resp]], docs) == [[expected]]
```

No credit needed. Thanks for fixing it!


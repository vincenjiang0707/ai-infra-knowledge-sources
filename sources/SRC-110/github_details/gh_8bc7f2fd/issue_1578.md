# [Issue #1578] AIME judge verdict set by the word "Yes" anywhere in judge text; AIR-Bench scores taken from the last two bare numbers

source: https://github.com/modelscope/evalscope/issues/1578
state: closed | updated: 2026-08-17T10:54:52Z
labels: 

## 正文

## Summary

Two benchmark adapters parse LLM judge output with positional or substring
heuristics that are not bound to the judge's actual decision. In the AIME
adapters, the correctness verdict is True whenever the word "Yes" appears
anywhere in the judge's free-text response, so a wrong answer is scored correct
when the judge says "Yes" while explaining why the answer is wrong. In the
AIR-Bench Chat adapter, the two scores are taken from the last two bare numbers
in the judge output, so a candidate can choose its own scores by ending its
answer with score-shaped numbers that the judge then quotes or echoes. Both
results feed the benchmarks' reported metrics (`acc` for AIME, `judge_score`
and `win_rate` for AIR-Bench Chat).

## Affected code

Commit: 31ccc8c02671832df1f0a4aba64689c850898c95

1. `evalscope/benchmarks/aime/aime_adapter.py:183`

   ```python
   is_correct = bool(re.search(r'\bYes\b', judge_response, re.IGNORECASE))
   ```

   This line sits in `llm_match_score` (lines 171-194). The boolean sets
   `score.value['acc']`, the reported accuracy metric. `AIME25Adapter`
   (line 241) and `AIME26Adapter` (line 289) subclass `AIME24Adapter` without
   overriding the method, so aime24, aime25, and aime26 are all affected. The
   judge prompt (lines 18-77) asks for a bare "Yes" or "No" with no rationale,
   but the parser does not enforce that contract; it searches the entire
   response.

2. `evalscope/benchmarks/air_bench/air_bench_chat_adapter.py:384-402`
   (`_extract_judge_scores`)

   The parser returns the first line containing exactly two bare numbers in
   the 0-10 range, and otherwise falls back to `slash_nums[-2:]` or
   `nums[-2:]` over the whole judge output. `_judge_pair` (lines 356-382)
   consumes `nums[0]` and `nums[1]` as the two assistants' scores with only a
   1..10 range check. `llm_match_score` (lines 284-354) averages these into
   `judge_score`, the benchmark's primary metric, and `win_rate`. The judge
   prompt template (lines 42-54) embeds the candidate's answer verbatim, which
   gives the candidate a channel into the parsed text.

## PoC

Two standalone scripts (stdlib only, exit 0) download the genuine adapter
files from this repository at the pinned commit, verify their sha256 hashes
(refusing to run on mismatch), extract the real methods by line range, assert
the sink lines are present verbatim in the fetched source, and drive them with
a stubbed judge:

- `poc_public_a_aime.py`: feeds `llm_match_score` a battery of judge responses and
  compares the parsed verdict with a human reading.
- `poc_public_b_airbench.py`: feeds `_extract_judge_scores` and `_judge_pair` judge
  outputs with candidate-planted trailing numbers and compares the extracted
  scores with the scores the judge actually assigned.

Key output from `poc_a_aime.py`:

```
3  True    False  FLIP!  'Yes, the answer is incorrect.'
4  False   True   FLIP!  'No. The answer is correct.'
5  True    False  FLIP!  'The student concluded "Yes, 42". The reference is 137, so...'
3/7 judge responses produce a verdict opposite to what a human reader concludes.
```

Key output from `poc_b_airbench.py`:

```
[3] ATTACK: judge quotes candidate-planted trailing numbers
    extracted      : assistant1=9.0, assistant2=1.0
    intended       : assistant1=3.0, assistant2=8.0
    result         : HIJACKED
[4] ATTACK: planted numbers win the last-two fallback slice
    extracted      : assistant1=10.0, assistant2=2.0
    intended       : assistant1=4.0, assistant2=6.0
    result         : HIJACKED
```


<details>
<summary>Full standalone PoC scripts</summary>

`poc_public_a_aime.py`:

```python
#!/usr/bin/env python3
"""PoC A, ETB-01: evalscope AIME judge verdict is set by the word "Yes" ANYWHERE
in the judge's free text.

Upstream code under test (genuine file downloaded from raw.githubusercontent.com
at the pinned commit, sha256-verified at runtime; refuses to run on mismatch):
    evalscope/benchmarks/aime/aime_adapter.py
    - JUDGE_PROMPT          lines 18-77   (context only, shows the judge contract)
    - llm_match_score       lines 171-194 (the real scoring method)
    - line 183: is_correct = bool(re.search(r'\bYes\b', judge_response, re.IGNORECASE))

Consumption (upstream, same file): score.value['acc'] = 1.0 if is_correct else 0.0;
score.main_score_name = 'acc'. 'acc' is the AIME24/AIME25 reported accuracy metric.
So any word-boundary "yes" (any case) anywhere in the judge response scores the
candidate answer as correct.

The judge prompt says "Respond with only Yes or No ... Do not include a rationale."
Nothing enforces that. A verbose judge, a judge affirming a negatively phrased
question, or a judge quoting the candidate's own "Yes" all flip the verdict.
"""
import hashlib
import re
import sys
import urllib.request
from pathlib import Path  # noqa: F401 (kept for parity)

COMMIT = '31ccc8c02671832df1f0a4aba64689c850898c95'
RAW = 'https://raw.githubusercontent.com/modelscope/evalscope/' + COMMIT + '/evalscope/benchmarks/aime/aime_adapter.py'
EXPECTED_SHA256 = '00c36f3d07a82f8814469a5fd92ec4cbf051dac4814bdd76d6070449f309fa31'


def fetch_verified() -> str:
    data = urllib.request.urlopen(RAW, timeout=30).read()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print('REFUSING TO RUN: sha256 mismatch on evalscope/benchmarks/aime/aime_adapter.py.')
        print(f'  expected {EXPECTED_SHA256}')
        print(f'  got      {digest}')
        print('Upstream changed; re-pin before trusting this PoC.')
        sys.exit(1)
    return data.decode('utf-8')


def extract_lines(text, start, end):
    lines = text.splitlines(keepends=True)
    return ''.join(lines[start - 1:end])


class StubScore:
    """Minimal stand-in for evalscope.api.metric.Score (same attribute surface
    the upstream method touches)."""

    def __init__(self, extracted_prediction=None, prediction=None):
        self.extracted_prediction = extracted_prediction
        self.prediction = prediction
        self.value = {}
        self.explanation = ''
        self.metadata = {}
        self.main_score_name = None


class FakeJudge:
    """Stands in for self.llm_judge; replays the canned judge response."""

    model_id = 'fake-judge-poc'
    canned = ''

    def judge(self, prompt=None):
        return self.canned


PROMPT_LINES = (18, 77)     # JUDGE_PROMPT
METHOD_LINES = (171, 194)   # llm_match_score

UPSTREAM_TEXT = None


def build_adapter_under_test():
    """Exec the byte-identical upstream method into a synthetic class."""
    global UPSTREAM_TEXT
    if UPSTREAM_TEXT is None:
        UPSTREAM_TEXT = fetch_verified()
    src_prompt = extract_lines(UPSTREAM_TEXT, *PROMPT_LINES)
    src_method = extract_lines(UPSTREAM_TEXT, *METHOD_LINES)

    ns = {'re': re, 'Score': StubScore, 'TaskState': object}
    exec(src_prompt, ns)  # defines JUDGE_PROMPT exactly as upstream

    class_src = 'class _AdapterUnderTest:\n    judge_strategy = "llm"\n' + src_method
    exec(class_src, ns)
    adapter = ns['_AdapterUnderTest']()
    adapter.llm_judge = FakeJudge()
    return adapter, src_method


# (judge_response, human_verdict, note)
BATTERY = [
    ('Yes', True, 'clean control: correct'),
    ('No', False, 'clean control: incorrect'),
    ('Yes, the answer is incorrect.', False,
     'judge affirms then negates; wrong answer scored correct'),
    ('No. The answer is correct.', True,
     'judge negates then affirms; correct answer scored incorrect'),
    ('The student concluded "Yes, 42". The reference is 137, so the answers are '
     'not equivalent. No.', False,
     'candidate-seeded token: judge quotes the candidate saying Yes'),
    ('yes', True, 'lowercase control: re.IGNORECASE makes case irrelevant'),
    ('yesterday the grader confirmed they do not match. No.', False,
     'word-boundary control: "yesterday" must NOT match \\bYes\\b'),
]


def main():
    sha = EXPECTED_SHA256
    print('PoC A / ETB-01: AIME anywhere-match verdict parse')
    print(f'upstream : {RAW}')
    print(f'commit   : {COMMIT}')
    print(f'sha256   : {sha}')
    print(f'sink     : aime_adapter.py:183  is_correct = bool(re.search('
          f"r'\\bYes\\b', judge_response, re.IGNORECASE))")
    print()

    adapter, src_method = build_adapter_under_test()
    assert "re.search(r'\\bYes\\b', judge_response, re.IGNORECASE)" in src_method, \
        'upstream extraction drifted; aborting'

    flips = 0
    hdr = f'{"#":<3}{"parsed":<8}{"human":<7}{"verdict":<6} judge response'
    print(hdr)
    print('-' * 100)
    for i, (resp, human, note) in enumerate(BATTERY, 1):
        FakeJudge.canned = resp
        score = adapter.llm_match_score('candidate answer', 'candidate answer',
                                        'reference answer', task_state=None)
        parsed = score.value['acc'] == 1.0
        flip = parsed != human
        flips += flip
        shown = resp if len(resp) <= 60 else resp[:57] + '...'
        print(f'{i:<3}{str(parsed):<8}{str(human):<7}'
              f'{"FLIP!" if flip else "ok":<6} {shown!r}')
        print(f'{"":<24}note: {note}')
    print('-' * 100)
    print(f'{flips}/{len(BATTERY)} judge responses produce a verdict opposite to '
          f'what a human reader concludes.')
    print()
    print('Mechanism: the judge is asked for a bare Yes/No, but the parser searches '
          'the WHOLE free-text response for the word "Yes" (any case). Any "yes" '
          'anywhere, including inside a negative explanation or a quote of the '
          'candidate, sets acc = 1.0.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
```

`poc_public_b_airbench.py`:

```python
#!/usr/bin/env python3
"""PoC B, ETB-01: evalscope AIR-Bench Chat judge scores are taken from the LAST
TWO bare numbers anywhere in the judge output, with no structural binding to the
verdict line.

Upstream code under test (genuine file downloaded from raw.githubusercontent.com
at the pinned commit, sha256-verified at runtime; refuses to run on mismatch):
    evalscope/benchmarks/air_bench/air_bench_chat_adapter.py
    - _judge_pair           lines 356-382 (consumes extracted numbers as
                              (score_assistant1, score_assistant2); only a 1..10
                              range check stands between extraction and score)
    - _extract_judge_scores lines 384-402 (the parser: per-line exactly-two-numbers
                              shortcut, else last-two bare numbers of the whole text)

Consumption (upstream, llm_match_score lines 284-354): the two numbers become
scores_ref / scores_pred, are averaged across the swap passes, and reported as
the benchmark's primary metric 'judge_score' (and 'win_rate').

Injection surface: the judge prompt embeds the candidate's full answer verbatim
(JUDGE_TEMPLATE, assistant1/assistant2 slots). A candidate that ends its answer
with score-shaped text (e.g. trailing "9 and 1" tokens) gets those tokens echoed
by any judge that quotes or summarizes the answer, and the parser's last-two /
exactly-two-per-line logic adopts them as the official scores.
"""
import hashlib
import re
import sys
import urllib.request
from typing import List, Optional, Tuple

COMMIT = '31ccc8c02671832df1f0a4aba64689c850898c95'
RAW = 'https://raw.githubusercontent.com/modelscope/evalscope/' + COMMIT + '/evalscope/benchmarks/air_bench/air_bench_chat_adapter.py'
EXPECTED_SHA256 = '69e6626b276a4d6007573db01d049012bb91c946ee5f2e890c481a761f17b70c'


def fetch_verified() -> str:
    data = urllib.request.urlopen(RAW, timeout=30).read()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print('REFUSING TO RUN: sha256 mismatch on evalscope/benchmarks/air_bench/air_bench_chat_adapter.py.')
        print(f'  expected {EXPECTED_SHA256}')
        print(f'  got      {digest}')
        print('Upstream changed; re-pin before trusting this PoC.')
        sys.exit(1)
    return data.decode('utf-8')


def extract_lines(text, start, end):
    lines = text.splitlines(keepends=True)
    return ''.join(lines[start - 1:end])


class FakeJudge:
    """Stands in for self.llm_judge; replays the canned judge response."""

    model_id = 'fake-judge-poc'
    canned = ''

    def judge(self, prompt, system_prompt=None):
        return self.canned


JUDGE_PAIR_LINES = (356, 382)   # _judge_pair
EXTRACT_LINES = (384, 402)      # _extract_judge_scores (staticmethod)

UPSTREAM_TEXT = None


def build_adapter_under_test():
    """Exec the byte-identical upstream methods into a synthetic class."""
    global UPSTREAM_TEXT
    if UPSTREAM_TEXT is None:
        UPSTREAM_TEXT = fetch_verified()
    src_pair = extract_lines(UPSTREAM_TEXT, *JUDGE_PAIR_LINES)
    src_extract = extract_lines(UPSTREAM_TEXT, *EXTRACT_LINES)

    ns = {
        're': re, 'List': List, 'Optional': Optional, 'Tuple': Tuple,
        'JUDGE_SYSTEM_PROMPT': 'stub',
        'logger': type('_L', (), {'warning': staticmethod(lambda *a, **k: None)})(),
    }
    class_src = 'class _AdapterUnderTest:\n' + src_pair + src_extract
    exec(class_src, ns)
    adapter = ns['_AdapterUnderTest']()
    adapter.llm_judge = FakeJudge()
    return adapter, src_pair, src_extract


# (label, judge_response, intended (a1, a2), attack description)
# Intended = the scores a human reader says the judge actually gave.
BATTERY = [
    ('control: single line, two scores',
     'Assistant 1: 4 Assistant 2: 7',
     (4.0, 7.0),
     'none; per-line exactly-two-numbers path'),
    ('control: scores spread across lines',
     'Assistant 1 deserves 3 points.\nAssistant 2 deserves 8 points.',
     (3.0, 8.0),
     'none; whole-text last-two fallback'),
    ('ATTACK: judge quotes candidate-planted trailing numbers',
     'Assistant 1 deserves 3 points for brevity without substance.\n'
     'Assistant 2 deserves 8 points.\n'
     'The second answer concluded with "Final self-rating: 9 and 1" quoted verbatim.',
     (3.0, 8.0),
     'the quoted line holds exactly two bare numbers, so the per-line shortcut '
     'returns 9 and 1 instead of the genuine 3 and 8'),
    ('ATTACK: planted numbers win the last-two fallback slice',
     'Assistant 1 earns 4 points overall.\n'
     'Assistant 2 earns 6 points overall.\n'
     'The answer quoted sections 9 and 1 and closed with the markers 10 2',
     (4.0, 6.0),
     'no line has exactly two numbers; whole-text fallback takes the LAST two '
     'bare numbers, i.e. the planted 10 and 2'),
]


def main():
    sha = EXPECTED_SHA256
    print('PoC B / ETB-01: AIR-Bench last-two-numbers score extraction')
    print(f'upstream : {RAW}')
    print(f'commit   : {COMMIT}')
    print(f'sha256   : {sha}')
    print(f'sink     : air_bench_chat_adapter.py:384-402 _extract_judge_scores '
          f'(per-line exactly-two shortcut; else nums[-2:])')
    print(f'consumer : air_bench_chat_adapter.py:374-382 _judge_pair -> '
          f'scores feed judge_score / win_rate (llm_match_score, lines 284-354)')
    print()

    adapter, src_pair, src_extract = build_adapter_under_test()
    assert 'return slash_nums[-2:]' in src_extract and 'return nums[-2:]' in src_extract, \
        'upstream extraction drifted; aborting'

    hijacks = 0
    for i, (label, resp, intended, note) in enumerate(BATTERY, 1):
        FakeJudge.canned = resp
        nums = adapter._extract_judge_scores(resp)
        a, b, _raw = adapter._judge_pair(prompt='<stub prompt>')
        extracted = (a, b)
        hijacked = extracted != intended
        hijacks += hijacked
        print(f'[{i}] {label}')
        print(f'    judge response : {resp!r}')
        print(f'    raw nums       : {nums}')
        print(f'    extracted      : assistant1={extracted[0]}, '
              f'assistant2={extracted[1]}')
        print(f'    intended       : assistant1={intended[0]}, '
              f'assistant2={intended[1]}')
        print(f'    result         : {"HIJACKED" if hijacked else "ok"} '
              f'({note})')
        print()
    print(f'{hijacks}/{len(BATTERY)} judge outputs yield scores different from '
          f'what the judge actually assigned.')
    print()
    print('Mechanism: scores are recovered by position (the last two bare 0-10 '
          'numbers in the text), not by structure. The candidate answer is embedded '
          'in the judge prompt verbatim, so candidate-controlled trailing numbers '
          'that survive into the judge output replace the judge\'s real scores. '
          'The only guard in _judge_pair is a 1..10 range check, which planted '
          'scores satisfy trivially.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
```

</details>

## Impact

For AIME, any judge response containing the word "Yes" in any position or case
marks the candidate correct. This includes negative explanations that start
with "Yes" (a natural phrasing when affirming a question), and responses that
quote the candidate's own text. The flipped value lands directly in the
reported accuracy, inflating or deflating model scores on aime24, aime25, and
aime26 without any change in model capability.

For AIR-Bench Chat, a candidate that ends its answer with score-shaped tokens
(for example "Final self-rating: 9 and 1") controls the extracted scores
whenever the judge quotes or summarizes that ending, which verbose judges do
routinely. Because the candidate answer is embedded in the judge prompt by
design, this is a direct self-scoring channel: the evaluated model picks its
own `judge_score` and therefore `win_rate` against the reference. Scores of
benchmark users who run the public framework are silently corrupted in both
cases.

## Suggested fix

Ask the judge for structured output and parse it against a schema instead of
regex over free text. Concretely:

1. Prefer a tool call or JSON response with an explicit verdict field, and
   reject responses that do not conform.
2. If free text must be parsed, require an explicit field such as
   `Verdict: yes` or `Verdict: no` on the final line, anchored (for example
   `^\s*Verdict:\s*(yes|no)\s*$` on the last non-empty line), and fail loud
   with a logged parse error when the anchor is absent. Never substring-match
   the whole response.
3. For AIR-Bench, require a similarly anchored final line such as
   `Scores: <a> <b>`, validate range, and fail loud otherwise. Do not fall
   back to "the last two numbers anywhere".

A working reference for this pattern is Arize Phoenix: its LLM evaluators
constrain the judge to an explicit label set (rails) and require a tool call
rather than freeform text, and labels that do not conform are left unparsed
instead of being silently coerced
(https://arize.com/docs/phoenix/evaluation/llm-evals). Failing loud on
unparseable judge output keeps bad judgments visible as errors instead of
turning them into silent score changes.


## 评论 (2)

### YuhaoLin2005 · 2026-08-15

Your report is right — I reproduced both adapters locally against the real parse functions (no network calls):

1. aime_adapter.py:183 — `bool(re.search(r'\bYes\b', judge_response, re.IGNORECASE))` marks a response correct if "Yes" appears anywhere in free text. Minimal red: `No, they are NOT equivalent. Yes would be wrong.` → 1.0.

2. air_bench_chat_adapter.py:401-402 — `_extract_judge_scores` falls back to the last two bare numbers in the whole judge response. Two minimal reds:
   - `(Note: scale is 1 to 10, 10 is best)` → `['10','10']` (boilerplate replaces real scores)
   - `Judge 9, model gpt-4` → `['9','4']` (metadata only, no scores present)

Neither adapter's parse path is unit-tested — coverage is e2e only (aime in tests/benchmark/test_eval.py, air_bench in tests/benchmark/test_vlm.py), and a wrong parse just yields a wrong score without failing the run.

Same class as a fix we did in coze-loop (#617): heuristics not anchored to the judge's actual decision structure. I'd be happy to own the fix direction and verification for both adapters and open a PR with red→green parse tests. Otherwise no action needed.

### atirna · 2026-08-16

I opened #1588 with exact response parsing for both judge formats, including explicit parse-failure metadata when a judge response is malformed. The targeted regression tests and repository lint pass.

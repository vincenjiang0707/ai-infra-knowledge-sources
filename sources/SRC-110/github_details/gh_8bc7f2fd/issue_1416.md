# [Issue #1416] when you exit during mid evaluation, eval metrics are not saved

source: https://github.com/modelscope/evalscope/issues/1416
state: closed | updated: 2026-07-08T06:37:34Z
labels: 

## 正文

when i exit in middle of evaluation, eval metrics in reports are not saved it starts from new again when i use --use-cache

for example with a dataset of 1000 tests, i exit at test 900 the metrics are not saved for it, when i restart it using --use-cache it will show only the metrics for the new 100 tests and not all 1000 tests



## 评论 (3)

### Yunnglin · 2026-06-16

Hi @shahidchdry, thanks for the report.

We tested `--use-cache` resume locally (gsm8k, interrupt at 10/20, resume) and metrics were correctly aggregated for all 20 samples. Could you provide:

1. Your exact commands (initial run + resume)
2. EvalScope version (`pip show evalscope`)
3. How you exited (Ctrl+C / kill / etc.)

This will help us reproduce the issue. Thanks!

### shahidchdry · 2026-06-17

original command : evalscope eval --model internlm/Intern-S2-Preview --api-url http://SERVER:8000/v1 --api-key na --datasets mmlu_pro --generation-config "timeout=3600,temperature=0.8,top_p=0.95,min_p=0,top_k=50,max_tokens=16384" --eval-batch-size 900 --dataset-args {"mmlu_pro": {"subset_list": ['law','engineering','economics', 'health', 'psychology', 'business', 'philosophy', 'history', 'other']}} --limit 100

resume command just had --use-cache outputs/run_name

its not unique to this it happened me in all runs from gpqa diamond, aime2026 etc

pip show evalscope returns this
 pip show evalscope
Name: evalscope
Version: 1.8.0
Summary: EvalScope: Lightweight LLMs Evaluation Framework
Home-page: https://github.com/modelscope/evalscope
Author: ModelScope team
Author-email: contact@modelscope.cn
License-Expression: Apache-2.0
Location: C:\Users\shahid\AppData\Roaming\Python\Python314\site-packages
Requires: aiohttp, colorlog, docstring_parser, dotenv, editdistance, jieba, jinja2, jsonlines, jsonschema, latex2sympy2_extended, litellm, Markdown, modelscope, more_itertools, nltk, openai, overrides, pandas, pillow, plotly, pydantic, pylatexenc, pyyaml, requests, rich, rouge-chinese, rouge-score, sacrebleu, sympy, tabulate, tqdm, transformers, word2number, zhconv
Required-by: 

i exit using ctrl c usually when benchmark goes on a loop

im using windows 11 and python 3.14

### Yunnglin · 2026-06-18

Thanks for the details. Please try the following:

1. Upgrade EvalScope to `1.8.1`, which includes a Windows cache writing fix.
2. Reduce `--eval-batch-size`; `900` is too high for this case, especially on Windows.
3. When resuming, add `--rerun-review` so the review/scoring step is regenerated from the cached predictions.

Example:

```bash
evalscope eval \
  --model internlm/Intern-S2-Preview \
  --api-url http://SERVER:8000/v1 \
  --api-key na \
  --datasets mmlu_pro \
  --generation-config "timeout=3600,temperature=0.8,top_p=0.95,min_p=0,top_k=50,max_tokens=16384" \
  --eval-batch-size 32 \
  --dataset-args '{"mmlu_pro":{"subset_list":["law","engineering","economics","health","psychology","business","philosophy","history","other"]}}' \
  --limit 100 \
  --use-cache outputs/run_name \
  --rerun-review
```

This issue should not be caused by `--use-cache` itself. Please retry with `1.8.1`, a smaller batch size, and `--rerun-review`.


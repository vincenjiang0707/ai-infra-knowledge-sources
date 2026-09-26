# [Issue #3289] MMLUSR tasks are broken

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3289
state: closed | updated: 2026-08-09T16:06:13Z
labels: validation

## 正文

Evaluations cannot be ran on MMLUSR tasks because the dataset names do not correspond to the [dataset schema on HuggingFace](https://huggingface.co/datasets/NiniCat/MMLU-SR).  

Suppose a user wants to run evals on a specific subtask, say, `mmlusr_answer_only_anatomy`:
```
python3 -m lm_eval --model dummy --tasks mmlusr_answer_only_anatomy --limit 1
```

The above command returns the following error:
```
...
  File "/Users/chrxu/Documents/lm-evaluation-harness/lm_eval/api/task.py", line 822, in __init__
    self.download(self.config.dataset_kwargs)
  File "/Users/chrxu/Documents/lm-evaluation-harness/lm_eval/api/task.py", line 929, in download
    self.dataset = datasets.load_dataset(
  File "/Users/chrxu/Documents/lm-evaluation-harness/.venv/lib/python3.10/site-packages/datasets/load.py", line 2062, in load_dataset
    builder_instance = load_dataset_builder(
  File "/Users/chrxu/Documents/lm-evaluation-harness/.venv/lib/python3.10/site-packages/datasets/load.py", line 1819, in load_dataset_builder
    builder_instance: DatasetBuilder = builder_cls(
  File "/Users/chrxu/Documents/lm-evaluation-harness/.venv/lib/python3.10/site-packages/datasets/builder.py", line 343, in __init__
    self.config, self.config_id = self._create_builder_config(
  File "/Users/chrxu/Documents/lm-evaluation-harness/.venv/lib/python3.10/site-packages/datasets/builder.py", line 570, in _create_builder_config
    raise ValueError(
ValueError: BuilderConfig 'mmlusr_answer_only_anatomy' not found. Available: ['answer_only', 'question_only', 'question_and_answer']
```

Happy to work on this issue and I already have a draft fix here: https://github.com/christinaexyou/lm-evaluation-harness/commit/998c7ae5d1516b53f117b810b4293c53c74f98c6

## 评论 (2)

### baberabb · 2025-09-10

Hi! Thanks for identifying that issue. And yes, will appreciate a PR!

### ayaangazali · 2026-08-01

Opened #3972 for this.

There turned out to be two layers. The `dataset_name` mismatch you identified is real, and behind it the `revision` pin from #3350 points at a loading-script revision, which `datasets>=4` refuses to run. So on current main the tasks stop at `RuntimeError: Dataset scripts are no longer supported` before the config name is even reached.

The repo still exposes per-subject CSVs, so each task now reads its own through `data_files` with explicit column names. Row counts for all 171 subjects match `cais/mmlu` on both test and dev, which they did not before.

Noted with AI help; the runs and the count comparison are mine.


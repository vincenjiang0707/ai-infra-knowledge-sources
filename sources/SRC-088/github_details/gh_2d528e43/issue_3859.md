# [Issue #3859] SCROLLS tasks fail to load with recent datasets (dataset scripts no longer supported)

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3859
state: closed | updated: 2026-08-09T16:15:59Z
labels: 

## 正文

The `scrolls_*` tasks fail at data loading on recent `datasets`. `tau/scrolls` is a script-based dataset, and `datasets` has removed support for dataset scripts (and `trust_remote_code`), so the load now raises.

Env: `datasets==5.0.0`, `lm_eval==0.4.13.dev0`

```python
from datasets import load_dataset
load_dataset("tau/scrolls", "qasper", split="validation")
# RuntimeError: Dataset scripts are no longer supported, but found scrolls.py
```

Same failure via `lm_eval --tasks scrolls_qasper`. It affects all seven scrolls tasks (`scrolls_govreport`, `scrolls_qasper`, `scrolls_narrativeqa`, `scrolls_qmsum`, `scrolls_quality`, `scrolls_summscreenfd`, `scrolls_contractnli`).

`lm_eval/tasks/scrolls/task.py` sets `DATASET_PATH = "tau/scrolls"`, and `_download_metric()` pulls `metrics/scrolls.py` from the same repo — both rely on the loading script that `datasets` no longer runs. `pyproject.toml` has `datasets>=2.16.0` with no upper bound, so a fresh install hits this.

Two ways forward:
- Pin `datasets` (e.g. `<4`) as a stopgap, though that holds back tasks needing newer `datasets`.
- Migrate scrolls to a parquet dataset on the Hub. There's no clean labeled mirror right now, so this means converting the gold-bearing splits and re-implementing the metric (also script-based). Same root cause as #1083.

Happy to help with the migration if that's the preferred route.


## 评论 (2)

### chuenchen309 · 2026-07-16

Confirmed, and I dug into the fix surface a bit since the obvious "just switch to parquet" path turns out not to be available.

**Root cause** is `_SCROLLSTask.DATASET_PATH = "tau/scrolls"` (`lm_eval/tasks/scrolls/task.py:117`) — a script-based dataset (`scrolls.py`), which `datasets` refuses to load once script support / `trust_remote_code` is removed. All seven `scrolls_*` tasks inherit this path, hence the uniform failure.

**The easy fix isn't there:** I checked the Hub API — `tau/scrolls` has **no `refs/convert/parquet` branch** (`GET /api/datasets/tau/scrolls/refs` → `"converts": []`). Datasets that fail the script conversion don't get the auto-parquet export, so there's no drop-in parquet revision to point `DATASET_PATH` at. So this needs one of:
- a maintained parquet mirror of the seven configs (govreport/qasper/narrativeqa/qmsum/quality/summscreenfd/contractnli), then repoint `DATASET_PATH` + set `DATASET_NAME` per task; or
- loading the raw per-config files directly via `data_files=` instead of the script.

**One thing that should still be fine:** `_download_metric()` (task.py:45-51) uses `hf_hub_download(repo_id="tau/scrolls", ...)` to fetch the metric file — that's a plain file download, not a scripted `load_dataset`, so the scoring side shouldn't need to move even if the data source does. Only `DATASET_PATH` is the blocker.

Happy to help put together a parquet-mirror-based fix if the maintainers are OK with that direction (it's the cleaner of the two, but it does mean hosting the converted configs somewhere stable).

### ayaangazali · 2026-08-03

Opened #3975 for this.

It avoids vendoring the loader. `tau/scrolls` has no parquet conversion, but it does still publish the data itself next to the script: one `<name>.zip` per subtask holding `<name>/{train,validation,test}.jsonl` with the same `id`/`pid`/`input`/`output` fields the tasks already use. Reading those members through `data_files` is enough, and since `DATASET_NAME` already equals the zip basename it is a single change in `_SCROLLSTask`.

Verified the internal paths for all seven subtasks and ran six of them end to end, with split sizes matching the published SCROLLS numbers. `narrativeqa` is the exception, its zip is 8.4 GB and I could not pull it here, so a second pair of eyes on that one would help.

@Chessing234 you closed #3872 earlier today, so I hope this is not stepping on anything. Say the word if you would rather take it.

Put together with AI assistance; the runs and checks are my own.


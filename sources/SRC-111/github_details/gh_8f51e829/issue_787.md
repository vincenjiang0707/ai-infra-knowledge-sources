# [Issue #787] Benchmark hangs forever (scheduler/worker deadlock) when dataset has no mappable columns — should fail fast instead

source: https://github.com/vllm-project/guidellm/issues/787
state: closed | updated: 2026-06-18T00:49:13Z
labels: good first issue, bug, escape

## 正文

## Describe the bug

When the input dataset contains only columns that `GenerativeColumnMapper` has no candidate for (e.g. a single `messages` column), `guidellm benchmark run` prints `Setup complete, starting benchmarks...` and then hangs forever. No requests are ever sent, no error is raised, and the process never exits — in containerized/CI environments it only dies when an external timeout (e.g. Kubernetes `activeDeadlineSeconds`) kills it.

Expected behavior: setup should fail fast with a clear error like "no mappable text/image/video/audio columns found in dataset (columns: ['messages'])".

## Environment

- guidellm: 0.6.0
- Python: 3.10 (Linux)
- Backend: any OpenAI-compatible server (reproduced against `guidellm mock-server` and against vLLM)

## To Reproduce

```bash
# data.jsonl — a column name that is not in GenerativeColumnMapper's candidates
printf '%s\n' '{"messages":[{"role":"user","content":"hello"}]}' > data.jsonl

guidellm mock-server --host 127.0.0.1 --port 18999 &

timeout 120 guidellm benchmark run \
  --target http://127.0.0.1:18999 \
  --model mock \
  --request-format /v1/chat/completions \
  --backend-kwargs '{"validate_backend": false}' \
  --profile concurrent --rate 2 --max-seconds 8 \
  --data data.jsonl \
  --output-dir ./out --outputs json
# → prints "Setup complete, starting benchmarks..." then hangs until killed (exit 124)
```

The same dataset with the column renamed to `prompt` (a `text_column` candidate) completes normally, so the trigger is purely the unmappable column name, not the request format.

## What seems to happen

`GenerativeColumnMapper.datasets_mappings()` (`guidellm/data/preprocessors/mappers.py`) finds no match for any column type, returning empty mappings. Downstream, requests carry no content columns, and the scheduler/worker processes end up idle waiting on each other (confirmed with py-spy: main process and all worker processes parked in idle waits — a lost-wakeup deadlock). `--max-seconds` never fires because the benchmark clock seemingly only starts once requests flow.

## Suggested fix

Validate the resolved column mappings after `datasets_mappings()`: if no text/image/video/audio column was mapped for any dataset, raise a `ValueError` listing the dataset's actual column names and the supported candidates. This turns a silent multi-process hang into an immediate, actionable error.

Happy to provide more detail (py-spy dumps) if useful.

## 评论 (1)

### jaredoconnell · 2026-06-11

Can you test this on main? There should be a fix that's already there.

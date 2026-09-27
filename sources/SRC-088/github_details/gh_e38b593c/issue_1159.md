# [Issue #1159] prepare_data silently drops remaining conversations when the render server dies mid-run

source: https://github.com/vllm-project/speculators/issues/1159
state: open | updated: 2026-09-26T09:09:47Z
labels: 

## 正文

**What happens.** On `speculators` main (`9865418`), if the `/v1/chat/completions/render` endpoint becomes unreachable while `build_speculator_training_dataset` is running — the server is killed mid-run, or `--render-endpoint` points at something that stops answering — the run **completes successfully and hands back a training set missing every conversation after the failure**. Each affected conversation is caught by the broad `except Exception` in `_render_conversation_rows` (preprocessing.py) and dropped; the run keeps going and returns without raising. The only signals are per-row `Failed to process conversation {idx}` error logs and one aggregate `{N}/{M} conversations produced no training rows` warning — whose text ("no assistant turn with context, unstable template, or fully truncated") doesn't mention the endpoint at all. If every conversation is lost you eventually hit the `No samples remain` ValueError; if only some are lost, there is no error.

**Repro** (on main, `9865418`):

1. Start a render server answering `/v1/chat/completions/render` (e.g. `vllm serve <model> --enable-scale-out`), or point at any working `--render-endpoint`.
2. Run a prepare over a small multi-conversation dataset — `build_speculator_training_dataset(ds, processor, render_endpoint=<url>)` with `ds` holding 2 conversations.
3. Kill the render server after the first conversation renders (before the second).
4. Observe: the run finishes with fewer rows and **no error**.

**Outcome** (2-conversation dataset, server killed after the first renders):

```
Request aborted (attempt 1/4): [Errno 111] Connection refused. Retrying in 2s...
Request aborted (attempt 2/4): [Errno 111] Connection refused. Retrying in 4s...
Request aborted (attempt 3/4): [Errno 111] Connection refused. Retrying in 8s...
Request timed out after 4 attempts: [Errno 111] Connection refused
Failed to process conversation 1: ConnectError: [Errno 111] Connection refused
1/2 conversations produced no training rows (no assistant turn with context, unstable template, or fully truncated)
>>> (harness) returned 1 row, no exception, 14.2s
```

The second conversation is gone; the run returns without raising, leaving a partial dataset and no error.

**Cost.** Each connection error runs the full retry loop (~14s of backoff per render call) before the row is dropped, so a large corpus also burns substantial time before finishing.

**Versions:** speculators `9865418` (main). Reproduced against a stub render endpoint — the drop is in speculators' own code, so it is independent of the vLLM version.

**Relation to #1117.** #1117 fixes the *launch* cause (missing `--enable-scale-out`). This is a different case: a server that dies mid-run, or a misconfigured external `--render-endpoint`.

**Minimal fix.** In `_render_conversation_rows`, re-raise `httpx.TransportError` (connection refused/timeout, once retries are exhausted) and the route-absent statuses 404/405/501 ahead of the broad `except`, so a systemic failure aborts with an actionable message instead of being swallowed as a per-row drop (requires `render_client` to surface the status, which today lives only in the exception message). Per-row failures keep drop-and-continue.

Happy to send a PR if this is wanted.

## 评论 (1)

### ChaShaoBao-web · 2026-09-26

Hi, I'd like to work on this issue if it's still available. I plan to make systemic render endpoint failures abort the dataset build instead of silently returning partial results, while preserving skip-and-continue behavior for conversation-specific errors. I'll also add regression tests with a mocked render endpoint. Before I start, could you confirm that this failure classification and scope match the intended behavior? I'm happy to adjust the approach based on your feedback.

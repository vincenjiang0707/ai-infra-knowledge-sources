# [Issue #4185] [Bug] DeepSeek-V4-Flash: request abort causes stale KV completion event and crashes EngineCore with LMCacheMPConnector

source: https://github.com/LMCache/LMCache/issues/4185
state: open | updated: 2026-09-27T01:56:10Z
labels: stale

## 正文

## Label

- `bug`
- `vLLM`
- `LMCacheMPConnector`
- `DeepSeek`
- `KV Cache`
- `Onboarding`

Related to LMCache Onboarding: https://github.com/LMCache/LMCache/issues/1882

## Describe the bug

We are serving `DeepSeek-V4-Flash` using vLLM with `LMCacheMPConnector`.

When a client disconnects during streaming generation, vLLM aborts the request normally. However, after the request has been removed from the vLLM scheduler's `self.requests`, LMCache may still report a delayed `finished_sending` or `finished_recving` event for that request.

When vLLM processes this stale request ID, the following assertion fails:

```python
assert req_id in self.requests
```

This terminates the entire EngineCore, all workers, and the API server.

The observed sequence is:

```text
Client disconnects
→ vLLM aborts the request
→ Request is removed from scheduler.requests
→ Asynchronous LMCache KV operation finishes later
→ LMCache reports finished_sending/finished_recving
→ vLLM cannot find the request ID
→ AssertionError
→ EngineCore exits
```

## To Reproduce

1. Start the LMCache MP service at:

```text
tcp://127.0.0.1:9997
```

2. Start vLLM with the following configuration:

```bash
PYTHONHASHSEED=0 vllm serve /data/models/DeepSeek-V4-Flash \
  --trust-remote-code \
  --kv-cache-dtype fp8 \
  --block-size 256 \
  --enable-chunked-prefill \
  --gpu-memory-utilization 0.93 \
  --enable-expert-parallel \
  --tensor-parallel-size 8 \
  --data-parallel-size 1 \
  --prefix-caching-hash-algo sha256_cbor \
  --tokenizer-mode deepseek_v4 \
  --tool-call-parser deepseek_v4 \
  --enable-auto-tool-choice \
  --reasoning-parser deepseek_v4 \
  --default-chat-template-kwargs '{"thinking": true}' \
  --attention-config '{"use_fp4_indexer_cache": false}' \
  --speculative-config '{"method":"mtp","num_speculative_tokens":3}' \
  --enable-prompt-tokens-details \
  --max-num-seqs 8 \
  --kv-cache-metrics \
  --enable-log-requests \
  --kv-transfer-config '{
    "kv_connector":"LMCacheMPConnector",
    "kv_connector_module_path":"lmcache.integration.vllm.lmcache_mp_connector",
    "kv_role":"kv_both",
    "kv_connector_extra_config":{
      "lmcache.mp.host":"tcp://127.0.0.1",
      "lmcache.mp.port":9997
    }
  }' \
  --port 8001
```

3. Send multiple concurrent streaming requests to `/v1/chat/completions`.

4. Disconnect or cancel one client while generation or KV transfer is in progress.

5. vLLM first prints the expected abort message:

```text
Request chatcmpl-... aborted.
```

6. Shortly afterward, EngineCore crashes:

```text
EngineCore encountered a fatal error.

File ".../vllm/v1/core/sched/scheduler.py", line 1782,
in update_from_output
    self._update_from_kv_xfer_finished(kv_connector_output)

File ".../vllm/v1/core/sched/scheduler.py", line 2500,
in _update_from_kv_xfer_finished
    assert req_id in self.requests

AssertionError
```

7. The API server returns HTTP 500 and shuts down all workers:

```text
vllm.v1.engine.exceptions.EngineDeadError:
EngineCore encountered an issue.

POST /v1/chat/completions HTTP/1.1
500 Internal Server Error
```

## Expected behavior

- Client disconnection should abort only the affected request.
- Aborting one request should not terminate EngineCore.
- If an asynchronous LMCache KV operation is still running, the request and its KV blocks should remain valid until the operation completes.
- `finished_sending` and `finished_recving` should be reported at most once for each request ID.
- LMCache should not return request IDs that have already been removed.
- Delayed completion events for canceled requests should be filtered or handled safely.
- Other active requests should continue running normally.

## Screenshots

No screenshots are currently available.

Relevant log:

```text
Request chatcmpl-9051503eef476119 aborted.

EngineCore encountered a fatal error.

File "/usr/local/lib/python3.12/dist-packages/vllm/v1/core/sched/scheduler.py",
line 2500, in _update_from_kv_xfer_finished
    assert req_id in self.requests

AssertionError
```

A complete log can be provided if needed.

## Desktop (please complete the following information)

This is a server-side issue and is unrelated to a desktop browser.

- OS: Linux Ubuntu 22.04
- Python: 3.11
- GPU: `H20 * 8
- CUDA: `<13.1>`
- vLLM version: `<0.25.1>`
- LMCache version: `<0.5.1>`
- Model: DeepSeek-V4-Flash
- Parallel configuration: TP=8, DP=1, Expert Parallel enabled
- KV cache dtype: FP8
- Block size: 256

Version commands:

```bash
vllm --version
uv pip show --system vllm lmcache
nvidia-smi
```

## Smartphone (please complete the following information)

Not applicable.

- Device: N/A
- OS: N/A
- Browser: N/A
- Version: N/A

## Additional context

We also tried switching to vLLM's built-in LMCache MP connector by setting:

```bash
export LMCACHE_USE_UPSTREAM_MP=1
```

and removing:

```json
"kv_connector_module_path":
"lmcache.integration.vllm.lmcache_mp_connector"
```

After switching, the built-in connector failed while processing the DeepSeek-V4 KV cache layout:

```text
RuntimeError: Worker failed with error
'kv must have shape
(num_blocks, page_block_size, h_kv, bytes_per_token)'
```

DeepSeek-V4 uses multiple hybrid and compressed KV cache layouts, including:

- c4a
- c128a
- sliding-window KV
- indexer KV
- compressor state
- packed FP8 KV layout

Our current observations are:

```text
External LMCacheMPConnector:
Supports the DeepSeek-V4 KV layout well enough to run,
but may report stale or duplicate KV completion events after abort.

vLLM built-in LMCacheMPConnectorUpstream:
Uses different request lifecycle handling,
but cannot process the DeepSeek-V4 KV cache shape.
```

We would appreciate clarification on the following questions:

1. Does the external `LMCacheMPConnector` officially support DeepSeek-V4 hybrid KV cache groups?
2. Which LMCache version is compatible with the current vLLM version and DeepSeek-V4?
3. Has the stale `finished_sending`/`finished_recving` event after abort been fixed in a newer release?
4. Should `get_finished()` deduplicate completion events?
5. Should `get_finished()` only return request IDs previously provided through `finished_req_ids_from_engine`?
6. Is there a recommended configuration for `TP=8/DP=1` or `TP=4/DP=2` with DeepSeek-V4?

Our current workaround is to disable LMCache completely, preventing delayed LMCache KV completion events from crashing EngineCore.
````

## 评论 (3)

### zhengfeihe · 2026-07-22

Hi～ (My two cents 

> 1. Does the external `LMCacheMPConnector` officially support DeepSeek-V4 hybrid KV cache groups?

Yes.

> 2. Which LMCache version is compatible with the current vLLM version and DeepSeek-V4?

Yes, 0.5.1 is fine. No version change is needed here.

> 3. Has the stale `finished_sending`/`finished_recving` event after abort been fixed in a newer release?

Not yet, but https://github.com/LMCache/LMCache/pull/4136 is a pending fix for exactly this. Feel free to try the
`fix/vllm-abort-during-retrieve` branch.

> 4. Should `get_finished()` deduplicate completion events?

Yes.

> 5. Should `get_finished()` only return request IDs previously provided through `finished_req_ids_from_engine`?

Yes.

> 6. Is there a recommended configuration for `TP=8/DP=1` or `TP=4/DP=2` with DeepSeek-V4?

The one thing that comes to mind is adding `--no-separate-object-groups` to the **LMCache server** command, see 
https://github.com/LMCache/LMCache/issues/4179

### yoonhoqpt · 2026-07-28

Thanks for documenting this. Did the cancellation failure affect a staging or operational workload, and did your team already have restart/cancellation tests before encountering it?

### github-actions[bot] · 2026-09-27

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.

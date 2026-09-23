# [Issue #4971] [Bug] Mooncake async migration can hang forever and make Decode unavailable

source: https://github.com/InternLM/lmdeploy/issues/4971
state: open | updated: 2026-09-15T08:00:36Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

In LMDeploy v0.17.0, when DistServe is configured with `MigrationBackend.Mooncake` and `LMDEPLOY_USE_ASYNC_MIGRATION=1`, a normal external Proxy `/v1/completions` request can hang in the Decode-side Mooncake migration path.

The Mooncake async migration branch creates an asyncio `Future`, runs `_migrate()` in an executor, and then awaits that `Future`. However, the created `Future` has no completion source: it is never completed with `set_result()` or `set_exception()`. If `_migrate()` finishes successfully, `p2p_migrate()` still waits forever on the unfinished `Future`.

In my test, this left Decode with a pending request, made subsequent normal requests time out, and finally made the Decode node unhealthy and invisible from Proxy node status.

## Detail

Analyzed version:

- LMDeploy v0.17.0
- Source snapshot used for analysis: `lmdeploy-main-src/lmdeploy-main`

Relevant source path:

- `lmdeploy/pytorch/disagg/backend/mooncake.py`
- `lmdeploy/pytorch/engine/engine_loop.py`

Relevant control flow in `mooncake.py`:

```python
async def p2p_migrate(self, assignment: MigrationAssignment, async_op: bool = False):
    if not LMDEPLOY_USE_ASYNC_MIGRATION:
        self._migrate(assignment)
    else:
        import asyncio
        loop = asyncio.get_event_loop()
        future = loop.create_future()

        await loop.run_in_executor(None, self._migrate, assignment)

        result = await future
        if result != 0:
            raise RuntimeError(f'Failed to perform async transfer: {result}')
```

The issue is that `future` is created but never completed. The executor result from `_migrate()` is not used to complete `future`, and there is no callback that calls `future.set_result()` or `future.set_exception()`.

The Decode migration path calls this backend migration from `engine_loop.py`. Therefore, when Mooncake async migration is enabled, a normal Proxy request can enter the migration path, finish `_migrate()`, and then hang forever at `await future`.

### Reproduction

**Test environment**:

- LMDeploy v0.17.0
- 1 Prefill + 1 Decode DistServe deployment
- Model: `Qwen2.5-0.5B-Instruct`
- `migration_backend=Mooncake`
- `migration_protocol=RDMA`
- `LMDEPLOY_USE_ASYNC_MIGRATION=1`
- Client traffic was sent to the normal Proxy `/v1/completions` endpoint.

**Trigger request**:

```bash
curl --max-time 20 \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "Qwen2.5-0.5B-Instruct",
    "prompt": "LC3 audit request: please answer with one short sentence.",
    "max_tokens": 8,
    "stream": false
  }' \
  http://127.0.0.1:19100/v1/completions
```

Observed result for the first normal request:

```text
http=000 time=20.002793 exit_code=28
```

This means the client did not receive an HTTP response and timed out after 20 seconds.

Key Decode log evidence:

```text
[LC3_AUDIT] p2p_migrate_enter remote_engine_id=http://127.0.0.1:19101 async_env='1' async_op=False batch_len=24
[LC3_AUDIT] async_future_created future_id=127245638503728 done=False
[LC3_AUDIT] _migrate_begin remote_engine_id=http://127.0.0.1:19101 remote_url='192.168.55.134:39100' batch_len=24
[LC3_AUDIT] _migrate_done remote_engine_id=http://127.0.0.1:19101 batch_len=24
[LC3_AUDIT] migrate_returned_before_uncompleted_future future_id=127245638503728 executor_result=0 done=False
```

The logs show that `_migrate()` completed and returned `0`, but the Future was still not done. Across the captured logs, the following marker never appeared:

```text
[LC3_AUDIT] uncompleted_future_resumed
```

After waiting 30 seconds, Proxy node status still showed Decode with one unfinished request:

```json
{
  "http://127.0.0.1:19101": {
    "role": 2,
    "models": ["Qwen2.5-0.5B-Instruct"],
    "unfinished": 0,
    "speed": null
  },
  "http://127.0.0.1:19102": {
    "role": 3,
    "models": ["Qwen2.5-0.5B-Instruct"],
    "unfinished": 1,
    "speed": null
  }
}
```

A second normal Proxy `/v1/completions` request also timed out:

```text
http=000 time=10.002063 exit_code=28
```

Final health state:

```text
Prefill:
{"status":"healthy","message":"PyTorch engine is healthy."}
http=200

Decode:
{"status":"unhealthy","message":"Backend has dispatched request handle(s), but schedule metrics report no active or waiting sequences."}
http=503
```

Final Proxy node status only showed Prefill. Decode disappeared:

```json
{
  "http://127.0.0.1:19101": {
    "role": 2,
    "models": ["Qwen2.5-0.5B-Instruct"],
    "unfinished": 0,
    "speed": null
  }
}
```

## Impact

When Mooncake backend async migration is enabled, an external client that can send normal completion requests to the DistServe Proxy can trigger a Decode-side migration hang.

**Impact**:

- Normal Proxy `/v1/completions` requests can hang without receiving a response.
- Decode can keep an unfinished request pending indefinitely.
- Subsequent normal requests can also time out.
- Decode `/health` can become HTTP 503.
- Proxy can lose the Decode node from `/nodes/status`, causing service degradation or denial of service.

### Environment

```Shell
Target version: LMDeploy v0.17.0
Model: Qwen2.5-0.5B-Instruct
Python: 3.12.3 (main, Jul 15 2026, 23:46:41) [GCC 13.3.0]
CUDA available: True
GPU 0: NVIDIA A100 80GB PCIe
GPU 0 Compute Capability: 8.0
CUDA_HOME: /usr/local/cuda
NVCC: Cuda compilation tools, release 13.0, V13.0.88
CUDA Driver Version: 590.48.01
PyTorch: 2.13.0+cu130
sglang: 0.5.19
sglang-kernel: 0.4.6.post1
flashinfer_python: 0.6.18
flashinfer_cubin: 0.6.18
flashinfer_jit_cache: 0.6.18+cu130
triton: 3.7.1
transformers: 5.12.1
numpy: 2.3.5
aiohttp: 3.14.3
fastapi: 0.141.1
huggingface_hub: 1.30.0
interegular: 0.3.3
modelscope: 1.39.1
orjson: 3.12.0
outlines: 0.1.11
packaging: 26.3
psutil: 7.2.2
pydantic: 2.13.5
python-multipart: 0.0.32
pyzmq: 27.2.0
uvicorn: 0.52.4
uvloop: 0.22.1
xgrammar: 0.2.1
openai: 2.6.1
tiktoken: 0.14.0
torchcodec: 0.15.0+cu130
ulimit soft: 1024
```

### Error traceback

```Shell

```

## 评论 (2)

### caikun-pjlab · 2026-09-15

Thank you for your feedback. Currently, enabling Mooncake Store and PD disaggregation simultaneously is not supported. We will address this in our future work.

### JPengLi · 2026-09-15

Hi @caikun-pjlab . Thank you for the quick response. 
This is not a Mooncake Store issue. The root cause is in LMDeploy's `lmdeploy/pytorch/disagg/backend/mooncake.py`, where `p2p_migrate()` creates an `asyncio.Future` under `LMDEPLOY_USE_ASYNC_MIGRATION` but never calls `future.set_result()`, causing the coroutine to hang forever after `_migrate()` returns. The fix is to use the executor result directly (as the DLSlime backend already does) instead of awaiting an unresolved Future.

Thanks again for looking into this.

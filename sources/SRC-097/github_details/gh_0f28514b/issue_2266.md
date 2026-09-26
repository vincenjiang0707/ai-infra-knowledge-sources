# [Issue #2266] nixl_agent.get_xfer_telemetry() raises nixlNoTelemetryError from Python wrapper; needs None-return behavior or explicit opt-out flag

source: https://github.com/ai-dynamo/nixl/issues/2266
state: open | updated: 2026-09-21T13:58:12Z
labels: 

## 正文

## Title
`nixl_agent.get_xfer_telemetry()` raises `nixlNoTelemetryError` from Python wrapper; needs None-return behavior or explicit opt-out flag

## Body

### Problem
The Python wrapper at `src/api/python/_api.py:690` (`nixl_agent.get_xfer_telemetry()`) calls into the C++ binding `self.agent.getXferTelemetry(handle._handle)` directly without a `try/except`. When the underlying backend cannot populate telemetry (e.g., UCX without `NIXL_TELEMETRY_ENABLE=1`, OBJ in some configurations), the C++ binding raises `NIXL_ERR_NO_TELEMETRY`, which becomes `nixlNoTelemetryError` in Python (see `src/bindings/python/nixl_bindings.cpp:135`). This is a footgun for downstream callers like vLLM: `NixlBaseConnectorWorker` calls `get_xfer_telemetry()` unconditionally per DONE handle (file `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py:3015`), so if `None` is returned `record_transfer(None)` raises `AttributeError` (caught by surrounding `try/except`, request marked as failed transfer); if `nixlNoTelemetryError` propagates it follows the same `try/except` path with the same outcome. In Dynamo P/D disaggregation, every "failed" KV transfer causes the frontend to return HTTP 500 to the client. With UCX backend (the default), this is **100% of requests**, not just intermittent failures.

### Suggested approaches
**Option A (Python wrapper guard, recommended)**: add `try/except` in the Python wrapper to return `None` on `nixlNoTelemetryError`, unifying the contract across backends:

```python
# src/api/python/_api.py:690
def get_xfer_telemetry(self, handle: nixl_xfer_handle) -> nixlBind.nixlXferTelemetry | None:
    """..."""
    try:
        return self.agent.getXferTelemetry(handle._handle)
    except nixlBind.nixlNoTelemetryError:
        return None
```

The docstring should explicitly note that `None` is returned when telemetry capture is not enabled on the agent (i.e., when `nixl_agent_config(capture_telemetry=False)` was used, or when the active backend cannot allocate telemetry buffers).

**Option B (C++ telemetry off switch)**: add a `nixl_agent_config(enable_telemetry: bool = True)` flag that unconditionally disables telemetry allocation across all backends. Callers like vLLM can then opt out at agent construction, and `get_xfer_telemetry` would return `None` consistently across all backends. This is more invasive but matches the pattern already used for `capture_telemetry` (see `src/api/python/_api.py:155,169,179,228`).

### Use case
Dynamo P/D disaggregation on NVIDIA H200 hardware with DeepSeek-V4.1-Flash FP8 (510 GB). Telemetry metrics are nice-to-have for observability; not having them must NOT prevent inference from succeeding.

### Reproduction
```python
import nixl_cu13 as nixl

agent = nixl.nixl_agent("foo", nixl.nixl_agent_config(backends=["UCX"]))
# Note: UCX does not auto-enable telemetry capture.
# ... register memory, do a transfer ...
try:
    t = agent.get_xfer_telemetry(handle)
    # Expected: returns nixlXferTelemetry.
    # Actual (UCX): raises nixlNoTelemetryError.
except nixl_cu13.nixlNoTelemetryError:
    print("Backend does not support telemetry; Python wrapper should return None")
```

### Companion PR
A minimal fix in vLLM is being submitted in parallel as [vllm-project/vllm#57403](https://github.com/vllm-project/vllm/pull/57403), which guards `record_transfer` against `None`. That PR alone does not unify the contract across NIXL backends; fixing it here would let vLLM and other downstream consumers write a single uniform code path.

### Impact
- vLLM upstream PR is filed (see link above).
- Dynamo P/D inference is unusable on UCX without telemetry workaround.
- Any user of NIXL Python wrapper that touches `get_xfer_telemetry` likely needs similar None-guard logic.


## 评论 (1)

### cyclinder · 2026-09-18

Thanks for the detailed report! I agree Option A is the right fix here — "telemetry not available" is an expected state (telemetry is off by default via `capture_telemetry=False`), so it should be expressed as a `None` return rather than an exception. Option B doesn't really address the core issue since telemetry allocation is already opt-in; the problem is that calling `get_xfer_telemetry()` with it disabled raises.

I'd like to submit a PR implementing Option A: wrap the call in the Python wrapper with `try/except nixlBind.nixlNoTelemetryError: return None`, update the return type annotation to `nixlXferTelemetry | None`, and document the `None` case in the docstring.

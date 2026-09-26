# [Issue #4247] [Bug]: Ascend sync batch outer timeout returns before transfer quiescence without a retained handle

source: https://github.com/kvcache-ai/Mooncake/issues/4247
state: open | updated: 2026-09-24T08:29:11Z
labels: 

## 正文

### Bug Report

#### Summary

`batch_transfer_sync_read` can return `-1` at its outer deadline while an Ascend transfer executor remains active and later writes into the registered destination buffers. The synchronous Python API returns neither a retained batch handle nor a quiescence guarantee, so a caller cannot infer that it is safe to reuse/unregister memory from that return value.

**`freeBatchID` returning `BatchBusy` for unfinished tasks is correct contract behavior, not the bug.** The issue is that the outer synchronous wrapper ignores that outcome and returns a failure without giving the caller a way to track/drain the outstanding operation.

#### Environment and version evidence

Sanitized excerpt only, based on preserved evidence; `collect_env.py` was **not run** for this submission.

- Ascend A3, Mooncake NPU package `0.3.11.post1`; inspected source `e9c61075720039bcfc5fffd19f847608402be3d0`.
- Public image tag `quay.nju.edu.cn/ascend/vllm-ascend:v0.26.0rc1-a3`.
- Application context: DSV4 Flash W8A8, 16 logical NPUs per P/D role, P DP4/TP4 and D DP16/TP1, dspark 5 speculative tokens, max model length 524288. The device experiment below does not load the model.
- The original incident binary hash was not preserved. The rebuilt environment uses the same image tag; its package/source and the two C++ log line numbers align with the pinned revision. This is not byte-for-byte proof of the incident binary or a reproduction on clean current main.

#### Source contract

Pinned references:

- [`transfer_engine_py.cpp`](https://github.com/kvcache-ai/Mooncake/blob/e9c61075720039bcfc5fffd19f847608402be3d0/mooncake-integration/transfer_engine/transfer_engine_py.cpp#L100): `MC_TRANSFER_TIMEOUT` is **seconds**, clamped to at least 5, default 30. In `batchTransferSync`, the outer deadline is `base_seconds * 1e9 + total_length_bytes` nanoseconds (lines 547–558); the clock starts before the retry loop. On expiry it attempts `freeBatchID`, ignores its status, and returns `-1`.
- [`transport.cpp`](https://github.com/kvcache-ai/Mooncake/blob/e9c61075720039bcfc5fffd19f847608402be3d0/mooncake-transfer-engine/src/transport/transport.cpp#L42): `freeBatchID` returns `BatchBusy` while tasks are unfinished; it is not cancellation.
- [`transfer_executor_base.cpp`](https://github.com/kvcache-ai/Mooncake/blob/e9c61075720039bcfc5fffd19f847608402be3d0/mooncake-transfer-engine/src/transport/ascend_transport/ascend_direct_transport/transfer_executor_base.cpp#L75): `ASCEND_TRANSFER_TIMEOUT` belongs to the Ascend executor and uses **milliseconds**. `120000` is 120 seconds; it does not replace the outer Python-wrapper deadline.

Thus a roughly 30-second outer failure is compatible with the default wrapper deadline even when the executor timeout is 120 seconds. It does not establish a HIXL hardware timeout or that the executor variable was ignored.

#### Controlled real-device reproduction

This was a preserved isolated experiment using registered NPU buffers, the actual synchronous binding and Ascend transport. **The test-only shim delays before submitting to the real transfer call; it is not a real network hang or an injected HIXL failure.** After sleeping 8 seconds it forwards to the real underlying Ascend transfer implementation. Source/destination use two local NPU devices in separate processes with localhost handshake, not business data.

Procedure/pseudocode (not a complete runnable device harness; the shim/build/bootstrap code is omitted to keep the report small):

```python
# Both processes: initialize TransferEngine with protocol='ascend',
# P2PHANDSHAKE on 127.0.0.1, and register an aligned 2 MiB NPU buffer.
# Source buffer is filled with 37; destination is filled with guard byte 7.
# Keep owning tensors, engine, registrations, and source process alive.
# Before engine construction:
MC_TRANSFER_TIMEOUT = '5'          # seconds; outer wrapper
ASCEND_TRANSFER_TIMEOUT = '120000' # milliseconds; executor
# ASCEND_USE_ASYNC_TRANSFER is absent.
# Test shim around the real synchronous Ascend call:
#   active += 1; sleep(8); rc = real_call(original_args); active -= 1
# Counters are an independent test oracle, not a completion mechanism
# used by the candidate wrapper.
offsets = [4096, 16384]
t0 = monotonic()
ret = engine.batch_transfer_sync_read(
    source_localhost_session,
    [destination_base + x for x in offsets],
    [source_base + x for x in offsets],
    [4096, 4096],
)
print(ret, monotonic() - t0)
# Original: inspect without freeing/reusing; wait for independent completion.
# Verify both payload regions eventually contain 37, all guards remain 7.
# Never unregister/reuse while quiescence is unknown.
```

Two preserved original-wrapper observations, kept separate:

| Observation | Result |
| --- | --- |
| Original controlled-delay case | outer return `-1` at **5.001454489 s**; destination still sentinel at return; later data and guards correct; registered buffers retained, no deallocation/reuse |
| Separate original retained-buffer control | outer return `-1` at **5.001174747 s**; underlying real call returned `0` at **8.196125938 s**; guards correct; buffers retained |

This establishes a late write after the outer return in the controlled-delay experiment. It does **not** establish that late writes caused the historical model crash, nor that an arbitrary `FAILED` state means the device is quiet.

#### Local candidate results, not an upstream fix

A local experimental patch changes only the synchronous batch wrapper and Ascend `SyncTransferExecutor` path. It introduces a candidate ABI marker and proposes:

- `0`: all tasks completed, batch free succeeded, logical deadline not exceeded.
- `-2`: logical failure, but all tasks of this call's single submitted batch reached `COMPLETED` and batch free succeeded; **not successful KV reception**.
- `-1`: quiescence unknown (or pre-submit validation failure); conservatively retain memory/ownership. The unknown batch/descriptors are intentionally retained rather than falsely reclaimed.

It removes outer resubmission, avoids retry/disconnect after a potentially submitted `TransferSync` error, and allows a further 30-second drain budget on a monotonic clock, sleeping 1 ms between polls. Pre-submission connection failures remain a distinct case. These semantics are a local proposal, not existing upstream API guarantees.

Final rebuilt **pybind11 2.x** candidate device validation:

| Case | First return / elapsed | Immediate reuse after proven completion | Guards / activity | Process cleanup |
| --- | --- | --- | --- | --- |
| Success control | `0`, **0.184765403 s** | `0`, **0.001082279 s** | correct; 2 total calls, 0 active | source exit 0, destination exit 0 |
| Controlled 8 s delay, outer 5 s | `-2`, **8.199669426 s** | `0`, **0.001104310 s** | correct; 2 total calls, 0 active | source exit 0, destination exit 0 |

The candidate did not use the shim completion oracle. For the reuse check the destination was re-filled with guard byte 9 and delay disabled; transferred payloads were 37. Buffers were unregistered and engines/tensors cleaned up after the checks. The final tested candidate engine SHA-256 was `01ada948aa64376b46fc492293ec50528a8729e5b2810a76de5ab942d8f41619`; transport SHA-256 was `6345f6f97497f61e2dbdcde37bb10adbc713d1e658fbc3a3d25d152026d439fd`. These identify **candidate artifacts**, not the original incident binary.

Preserved CPU verification compiled the two actual changed C++ functions with deterministic fake dependencies using C++20 and warning-as-error checks, then passed **14 deterministic cases** (compile exit 0, test exit 0): actual outer wrapper and actual synchronous executor, unsafe retry/free checks, and bounded unknown drain. Those earlier CPU results did not themselves validate NPU execution; the device table above is a separate later validation. No NPU or production tests were newly run to prepare this report.

#### Limitations and requested contract clarification

This candidate is **not production-ready**. The drain budget is bounded only between engine calls and cannot interrupt a blocking submit/status/free call. Real HIXL failure cancellation is unproven; `FAILED`, process exit, or a local exception is not proof of remote/device quiescence. Unknown batches intentionally retain resources; no safe automatic reclamation API is claimed. A `-2` only covers its own batch, not parallel batches, ranks, or a whole worker. Async APIs, single-transfer APIs, general notify side effects, and global P/D fencing remain outside the candidate's validated scope.

Would an explicit retained handle plus wait/drain/cancel contract, or a documented distinction between drained logical failure and unknown physical completion, be appropriate for this synchronous API? Callers need to preserve source and destination lifetimes until all relevant activity is proven quiet. Increasing either timeout alone does not define that lifetime contract.

The original NPU 507035 crash/root cause is **not proven or stably reproduced** by these tests. I can provide a sanitized full device harness and candidate diff if useful; this issue publishes only synthetic evidence, not deployment files or model data.

Related: [#1845](https://github.com/kvcache-ai/Mooncake/issues/1845) discusses QP/endpoint retention after transfer failures; this report specifically covers the synchronous wrapper returning before an Ascend operation finishes and the missing caller-visible lifecycle handle. Related Ascend symptom reports [vllm-ascend#5660](https://github.com/vllm-project/vllm-ascend/issues/5660) and [#13439](https://github.com/vllm-project/vllm-ascend/issues/13439) do not establish a shared root cause.

Related caller-side report: [vllm-ascend#17044](https://github.com/vllm-project/vllm-ascend/issues/17044) isolates the Hybrid connector's missing failed-block reporting after a negative transfer. It is a separate logical failure-contract issue; fixing it alone does not establish transport quiescence.

### Before submitting...

- [x] Ensure you searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)


## 评论 (2)

### github-actions[bot] · 2026-09-21

Thanks for opening this issue, @bluryar!

| Field | Value |
|-------|-------|
| **Issue** | #4247 |
| **GitHub user ID** | `48168490` |
| **Reporter** | @bluryar |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### ascend-direct-dev · 2026-09-24

Thanks for the detailed report and the controlled repro — very helpful.

关于同步路径超时后的生命周期：classic TE 确实是「外层 sync wrapper + 各 transport 后台线程」这套结构，Ascend Direct 也一样。当前没有更干净的 cancel / drain / 保留 handle 方案可以马上落地。

补充一点超时默认值：`ASCEND_TRANSFER_TIMEOUT` **默认是 10s**（`InitParams::transfer_timeout = 10000` ms）；外层 `MC_TRANSFER_TIMEOUT` 默认约 30s。在默认配置下外层已经大于 Ascend 侧。若自行调大 `ASCEND_TRANSFER_TIMEOUT`（例如到 120s）或压小 `MC_TRANSFER_TIMEOUT`，就会出现你复现里外层先返回、底层仍可能写缓冲的窗口。

现阶段更务实的做法是：**由上层保证 `MC_TRANSFER_TIMEOUT`（秒）> `ASCEND_TRANSFER_TIMEOUT`（毫秒换算后的秒）**，并在外层超时/失败后，在 quiescence 未知时不要复用或注销目标缓冲。更完整的 sync API 生命周期合约（保留 handle / drain / cancel，或区分已排空 vs 未知）值得后续单独讨论，但暂时还不在我们这边的修复计划里。

Also note: the original NPU crash attribution isn't established by the controlled delay experiment — we treat that separately.

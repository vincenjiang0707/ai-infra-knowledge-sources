# [Issue #2501] [Bug]: DummyClient::register_buffer fails for buffers outside pre-mapped shared memory segments

source: https://github.com/kvcache-ai/Mooncake/issues/2501
state: closed | updated: 2026-09-23T03:15:42Z
labels: bug, stale, auto-closed

## 正文

### Bug Report


## Summary

When using SGLang with EAGLE speculative decoding and Mooncake SSD offload (L3 HiCache), the `DummyClient::register_buffer()` returns `-1` for EAGLE's DRAFT KV pool buffer because it is allocated outside the shared memory segments that mooncake_client pre-mapped during initialization. This makes EAGLE + Mooncake L3 combination completely unusable.

## Environment

- **SGLang**: v0.5.13
- **Mooncake Transfer Engine (CUDA13)**: v0.3.11.post1
- **CUDA**: 13.0 (Driver 535.129.03)
- **GPU**: 8x H100 (TP=8)
- **Model**: Qwen3.5-397B-A17B-FP8
- **mooncake_client mode**: standalone (DummyClient), `--threads 8`
- **SSD**: Local PCIe NVMe (`/kv-cache-volume`)

## Steps to Reproduce

1. Start mooncake_master and mooncake_client (standalone mode)
2. Start SGLang server with EAGLE speculative decoding + HiCache + Mooncake storage backend:
   ```
   --speculative-algorithm EAGLE
   --speculative-num-steps 3
   --speculative-eagle-topk 1
   --speculative-num-draft-tokens 4
   --enable-hierarchical-cache
   --hicache-storage-backend mooncake
   --hicache-storage-backend-extra-config '{"standalone_storage": true, "client_server_address": "127.0.0.1:50052"}'
   ```
3. SGLang crashes during initialization when registering the DRAFT pool buffer

## Expected Behavior

`register_buffer` should accept buffers that are not within pre-mapped shared memory segments, either by dynamically registering a new segment or by allowing the buffer to be registered without segment constraints.

## Actual Behavior

SGLang crashes during initialization when registering the DRAFT pool buffer:

```
[2026-06-16 11:13:33 TP4] Failed to register buffer, error code: -1
[2026-06-16 11:13:33 TP4] Scheduler hit an exception: Traceback (most recent call last):
  File "/sgl-workspace/sglang/python/sglang/srt/managers/scheduler.py", line xxx, in xxx
    ...
  File "/sgl-workspace/sglang/python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py", line 637, in register_mem_host_pool_v2
    super().register_buffer(host_pool.kv_buffer)
  File "/sgl-workspace/sglang/python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py", line 294, in register_buffer
    ret_code = self.store.register_buffer(ptr, size)
  File "/sgl-workspace/sglang/python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py", line 297, in register_buffer
    raise RuntimeError(
RuntimeError: Failed to register buffer to Mooncake Store, error code: -1
[2026-06-16 11:13:33] Received sigquit from a child process. It usually means the child failed.
[2026-06-16 11:13:33 TP5] Failed to register buffer, error code: -1
[2026-06-16 11:13:33 TP5] Scheduler hit an exception: Traceback (most recent call last):
    ...
RuntimeError: Failed to register buffer to Mooncake Store, error code: -1
[2026-06-16 11:13:33] Received sigquit from a child process. It usually means the child failed.
[2026-06-16 11:13:33 TP7] Failed to register buffer, error code: -1
[2026-06-16 11:13:33 TP7] Scheduler hit an exception: Traceback (most recent call last):
    ...
RuntimeError: Failed to register buffer to Mooncake Store, error code: -1
[2026-06-16 11:13:33] Received sigquit from a child process. It usually means the child failed.
```

Multiple TP ranks fail simultaneously (TP4, TP5, TP7 in this case). The mooncake_client log shows no errors — RPC operations (PutStart, GetReplicaList, Ping) all succeed. The failure is isolated to the `register_buffer` call.

### Before submitting...

- [x] Ensure you searched for relevant issues and read the [documentation]

## 评论 (3)

### github-actions[bot] · 2026-06-16

Thanks for opening this issue, @HyeonjeCho!

| Field | Value |
|-------|-------|
| **Issue** | #2501 |
| **GitHub user ID** | `147108419` |
| **Reporter** | @HyeonjeCho |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### github-actions[bot] · 2026-09-15

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.

### github-actions[bot] · 2026-09-23

Closing due to 3 months of inactivity. If this is still relevant, please comment and we can reopen.

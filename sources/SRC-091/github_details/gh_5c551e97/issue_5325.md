# [Issue #5325] [Bug][MP] nixl_store L2 adapter doesn't clear status bitmap when data failed to load

source: https://github.com/LMCache/LMCache/issues/5325
state: closed | updated: 2026-09-26T00:06:10Z
labels: bug

## 正文

**Label**
Please label your issue with "bug" and any other relevant labels so that it can easily be easily categorized under [LMCache Onboarding](https://github.com/LMCache/LMCache/issues/1882)

**Describe the bug**
When `nixl_store` L2 adapter encounters a remote load failure, the exception thrown by nixl is caught and logged, but the status bitmap remains set.

In [NixlStoreL2Adapter._execute_load_in_loop](https://github.com/LMCache/LMCache/blob/dev/lmcache/v1/distributed/l2_adapters/nixl_store_l2_adapter.py#L853-L908):

```python3
try:
    # ...
    for i, key in enumerate(keys):
        # ...
        bitmap.set(i)
        accessed_keys.append(key)
    # ...
    await self.nixl_agent.post_non_blocking(handle)
    # Handle should be released when there's an exception as well
    self.nixl_agent.release_handle(handle)
    # ...
except Exception:
    logger.exception("NIXL load task %d failed", task_id)
    # bitmap and accessed_keys should be cleared when there's a failure

if accessed_keys:
    self._notify_keys_accessed(accessed_keys)
with self._lock:
    self._completed_load_tasks[task_id] = bitmap
self._signal_load_event()
```

vLLM would treat KV data as correctly loaded, which would cause external cache hit rate accounting to be inaccurate, and may make later inferencing output to be incorrect.

**To Reproduce**
Steps to reproduce the behavior:
1. Start LMCache with L2 adapter set to `nixl_store`, with OBJ backend and point to an S3 endpoint, and `--l2-store-policy=skip_l1`.
2. Start vLLM, use LMCache for KV cache offloading with `VLLM_BATCH_INVARIANT=1` and internal prefix caching disabled with `--no-enable-prefix-caching`.
3. Run two passes of [async_request.py](blob/dev/.buildkite/correctness/async_request.py), let LMCache populate remote cache, record the results to `lmcache_mp_nixl_store_cold.txt` and `lmcache_mp_nixl_store_warm.txt`.
5. Intercept GetObject calls to the S3 endpoint, run another pass of [async_request.py](blob/dev/.buildkite/correctness/async_request.py), log output to `lmcache_mp_nixl_store_failed.txt`. LMCache would log load failures to console output, vLLM would report unrealistically high cache hit rate.
6. Compare the results using [compare_files.py](blob/dev/.buildkite/correctness/compare_files.py), result would be:
  - `lmcache_mp_nixl_store_cold.txt` and `lmcache_mp_nixl_store_warm.txt` matches each other.
  - `lmcache_mp_nixl_store_failed.txt` would be different from the other two.

It's basically the same process as [vllm-correctness.sh](blob/dev/.buildkite/scripts/vllm-correctness.sh), except we intercept GetObject calls, and test the fail path of `nixl_store` L2 adapter instead.

With the ShareGPT dataset, we were seeing:
```
$ python3 compare_files.py --file1 lmcache_mp_nixl_store_cold.txt --file2 lmcache_mp_nixl_store_failed.txt
====== Statistics ======
Common IDs: 100
Identical IDs: 93
Different IDs: 7

—— Identical IDs ——
# omitted

—— Different IDs ——
chatcmpl-WJidmXp_0
chatcmpl-J410gdS_2
chatcmpl-J410gdS_3
chatcmpl-aFQ1wf6_0
chatcmpl-J410gdS_7
chatcmpl-J410gdS_6
chatcmpl-vH787Fr_0

—— Only in File 1 ——

—— Only in File 2 ——
```

**Expected behavior**
All three recorded result files should match each other, and vLLM should report 0% cache hit rate for the third pass.

**Additional context**
This issue was first discovered by [Anish Sana](mailto:anish.sana@hpe.com) under HPE's internal testing.

## 评论 (1)

### chunxiaozheng · 2026-09-24

@RedL0tus Thanks for your feedback, I will take a look.

# [Issue #5371] [Bug] fs_native L2: files left by a previous process are never counted toward max_capacity_gb or evicted (disk grows unbounded across restarts)

source: https://github.com/LMCache/LMCache/issues/5371
state: open | updated: 2026-09-26T20:13:53Z
labels: 

## 正文

## Summary

With the `fs_native` L2 adapter, chunk files persist across a server restart and are still served (lookup is a `stat` on the file), but the new process never registers them. They don't count toward `max_capacity_gb`, and the eviction policy never sees them, so **they are never evicted**. Each restart can strand up to a full cap of untracked files, and disk usage grows without bound until the filesystem fills.

## Observed

`lmcache/vllm-openai` image, LMCache `0.5.6rc1` (commit `9a7b6050`), MP server with:

```
--l2-adapter '{"type":"fs_native","base_path":"/lmcache/l2","num_workers":32,"use_odirect":true,
  "max_capacity_gb":1000,"eviction":{"eviction_policy":"LRU","trigger_watermark":0.9,"eviction_ratio":0.1}}'
```

1. Wrote ~1.2 TB of KV. LRU eviction worked as documented: usage hit the 0.9 watermark three times and dropped to 871 GB each time (`L2 usage 0.90 above watermark 0.90; triggering eviction`).
2. Restarted the server with the same `base_path`: 298,340 files, 911.7 GB on disk.
3. After the restart, `GET /status` reported `l2_eviction_controller.adapters[0].total_bytes_used = 0`.
4. Requests over the pre-restart prefixes were served from those files: 16.76M tokens, every full chunk, `lookup_hit_l2_tokens_total` +16,760,832. After that, tracked usage was 0.49 GB, i.e. only the new writes, while 911.7 GB of served files stayed untracked.

## Root cause (on `dev` at dc68527c)

- Byte accounting and eviction order are fed only by stores that the current process completes: `_notify_keys_stored` in `l2_adapters/base.py`, called from the native adapter's store completions. Neither `fs_native_l2_adapter.py` nor `native_connector_l2_adapter.py` scans `base_path` at startup.
- Reads of pre-existing files fire `on_l2_keys_accessed`, and `LRUEvictionPolicy.on_keys_touched` ignores keys it doesn't track (`if key in self._order`).
- `NativeConnectorL2Adapter` decrements usage on delete only for keys in `_key_sizes`, i.e. stored by this process.
- Re-storing an existing key is a no-op on disk (`csrc/storage_backends/fs/connector.cpp`: "Skip if already stored on disk").

RFC #4738 mentions this in passing ("Restart recovery: ... Existing files on disk are not automatically registered again"), but as part of a larger multi-disk design, and there is no standalone bug for it.

## Impact

With `max_capacity_gb` sized to the disk (the natural configuration), one restart with a full cache followed by a refill exceeds the disk. Any deployment that restarts routinely (rollouts, crashes) accumulates untracked files. Operators have to choose between wiping `base_path` on every start, which loses the persistence, and eventually running out of space.

## Proposed fix (prototyped, tested)

File names are already reversible: `fs_l2_adapter._filename_to_object_key` inverts the names the C++ connector writes. The prototype:

- adds `L2AdapterInterface.recover_persisted_objects() -> int` (default no-op), delegated by the serde and fault-inject wrappers;
- `StorageManager` calls it for each adapter **after** the L2 eviction states have registered their listeners, at init and in `add_l2_adapter`;
- `NativeConnectorL2Adapter` takes an optional `persisted_object_scanner`. `recover_persisted_objects` records each object in `_key_sizes` (so eviction deletes decrement usage) and announces it through `_notify_keys_stored`. It goes newest-first, so LRU's reverse insertion puts the oldest file at the eviction head. Keys already tracked are skipped;
- `fs_native` gains `recover_on_start` (default `true`) and a scanner that `os.scandir`s `base_path`. It decodes `.data` names, takes `st_size` and `st_mtime`, and skips `.tmp` files, undecodable names and directories.

Tests: 13 new (scanner, adapter recovery/ordering/delete/double-count, config, and `StorageManager` end-to-end: leftover files are accounted, over-cap leftovers are evicted oldest-first, `recover_on_start: false` keeps today's behaviour). The existing tests in `test_native_connector_l2_adapter`, `test_fs_native_l2_adapter_config`, `test_runtime_adapters`, `test_l2_adapter_base`, `test_fault_inject_l2_adapter`, `test_storage_manager_l2_keys` and `test_l2_adapter_factory` still pass (185 passed). Run on the 0.5.6rc1 commit; the patch also applies cleanly to current `dev`.

**Validated on a real cache:** 0.5.6rc1 plus the patch, restarted over the 911.7 GB directory above, with the cap lowered to 800 GiB:

```
fs_native: found 298492 persisted objects (849.44 GiB) in /lmcache/l2 in 3.0 s (0 entries skipped)
L2 adapter 0: registered 298492 objects recovered from persistent storage (usage 912076931072 bytes)
L2 usage 1.06 above watermark 0.90; triggering eviction.
L2 usage 0.96 above watermark 0.90; triggering eviction.
```

- **Settled usage:** 0.86. The disk went from 912.2 GB to 738.85 GB, with 738.78 GB tracked, within 0.01% of `du`.
- **Oldest first:** the evicted files were the oldest by mtime; the newest were kept.

Open questions for maintainers:

- **Default:** should `recover_on_start` default to `true`? It changes startup behaviour, since eviction can run immediately when leftovers exceed the watermark.
- **Scan cost:** the scan is synchronous at startup. ~300k files took 3.0 s to scan plus 0.5 s to register here; a very large directory might want a background scan.
- **Other adapters:** the same gap likely applies to other persistent adapters, e.g. `fs` and `nixl_store`; the hook is generic.

Happy to open a PR.


## 评论 (1)

### OscarSavNS · 2026-09-26

Fix proposed in #5372.

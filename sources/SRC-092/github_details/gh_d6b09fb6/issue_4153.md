# [Issue #4153] [Bug]: Incorrect external prefix-cache reuse (out-of-order / off-topic responses) when partial hash hits are enabled for models with large attention blocks (e.g. GLM-5.3-Flash)

source: https://github.com/kvcache-ai/Mooncake/issues/4153
state: open | updated: 2026-09-17T04:20:54Z
labels: bug

## 正文

### Bug Report

**Target repo:** kvcache-ai/Mooncake
**Related issues:** #3048 (same symptom), #2827 (KV-integrity contamination in SSD offload path)

---

## Related issues (checked before filing)

- **#3048 — [Bug]: 有人遇到过模型答非所问吗** (open, H20 + mooncake as KV offload causing off-topic/wrong answers; reproduced with DeepSeek-V4-Flash). Same symptom as this report, but no root cause was confirmed there — maintainers attributed it to vLLM `400 Bad Request` and it remains open/undiagnosed. This report provides a concrete mechanism (partial hash hits on large-attention-block models).
- **#2827 — [Bug]: [SSD] DSV4 enable SSD offload，stress testing, repeat offloading the same batch key, lead to OBJECT_ALREADY_EXISTS/persist failed/INVALID_KEY** (open). A confirmed KV-integrity bug in the SSD offload path (concurrent duplicate offload → `OBJECT_ALREADY_EXISTS` → whole-batch persist failure → Master/SSD metadata divergence → `INVALID_KEY` on read → cross-request KV contamination).

This issue is filed as a distinct report because, unlike #3048, it identifies a mechanical defect (partial-hash-hit mapping coarse existence onto full-block reuse) with code path and repro; it references #2827 as the related SSD-offload contamination case.

**Checklist**
- [x] vLLM version: `v0.1.dev20051+g487ecf187` (custom build based on official `vllm/vllm-openai:glm53-flash-cu129`)
- [x] Hardware: 8× NVIDIA H20 (cu129), 4×TP per instance
- [x] Mooncake: standalone-store (mc-master + mc-client, 1 TiB shared segment + SSD offload)
- [x] Scenario: two vLLM instances (GPU0-3 / GPU4-7) sharing one mooncake KV segment for cross-instance prefix reuse

---

## Summary

When the Mooncake KV connector enables **partial hash hits** for a model whose **attention block size is much larger than the prefix-hash block size**, in-flight requests can silently reuse a *partial block* from another request. The reused KV block is **not content-identical**, so the model attends over mismatched cached state and produces **out-of-order / off-topic / garbled** responses (observed: a Chinese fault-ticket task returned a long English "reasoning"-style dump that clearly belonged to a different request).

## Environment

- Model: GLM-5.3-Flash0831 (Glm5NextForConditionalGeneration, MLA, MTP speculative 2)
- Serving: `--enable-prefix-caching --max-model-len 200K --gpu-memory-utilization 0.92 --speculative-config '{"method":"mtp","num_speculative_tokens":2}'`
- KV transfer:
  ```
  --kv-transfer-config '{"kv_connector":"MooncakeStoreConnector","kv_buffer_device":"cuda","kv_buffer_size":1000000000.0,"kv_role":"kv_both"}'
  ```
- Two instances share one mooncake segment (cross-instance reuse).
- Observed runtime block sizes:
  - `Setting kv cache block size to 64` → prefix-hash block size = **64**
  - `Setting attention block size to 1152` → attention/KV block size = **1152**
  - `Mamba cache mode is set to 'align' for Glm5Next... when prefix caching is enabled`

## Key observation at failure time

`mc-master` admin metrics during the failure window:

```
Mem Storage: 940.90 GB / 1.00 TB (91.9%)
Keys: 127075
Eviction: Success/Attempts=22/1217          # ~98% of evictions FAILED
SSD Storage: 973.60 GB / 2.00 TB
```

Model logs:

```
External prefix cache hit rate: 59-65%
Mooncake load tier summary: batch_keys=36 memory_keys=36 ... success_keys=36 failed_keys=0   (full memory-tier external hit, 526 MB KV reused)
```

A request at the same timestamp returned a multi-KB English reasoning/tooling dump (`gorilla agent mindset`, `127.0.0.1:8644`, `PHP`, `browser repair`, `shopping cart`, `philosophical`, ...) that was unrelated to the actual prompt — classic cross-request KV contamination.

## Root cause analysis (code)

The Mooncake connector mirrors vLLM core's `enable_partial_hash_hits` (`vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/coordinator.py`):

```python
def partial_hash_hits_enabled(kv_cache_groups, hash_block_size) -> bool:
    return any(
        isinstance(spec := _unwrap_spec(g.kv_cache_spec), MambaSpec)
        and spec.mamba_cache_mode == "align"
        and spec.block_size > hash_block_size
        for g in kv_cache_groups
    )
```

For GLM, `hash_block_size == 64` and the mamba/attention block is aligned to `1152`, so `1152 > 64` → **partial hash hits are enabled**.

The connector's external lookup reports a hit at the **64-token chunk granularity**:

```python
def get_cached_block(self, block_hash, group_ids):
    ...
    h = bytes(block_hash)
    if all((g, h) in self._exists for g in group_ids):
        return [self._present_block] * len(group_ids)   # reuse the whole 1152 block
    return None
```

and alignment:

```python
def align_lookup_length(self, length):
    alignment = self.hash_block_size if self.enable_partial_hash_hits else self.lcm_block_size
    return length // alignment * alignment
```

But the unit that is actually **reused / offloaded is the full 1152-token KV block**. When two requests share a prefix only to a 64-token boundary (but diverge within the same 1152-token block), the connector reports a "hit" and the scheduler reuses a block whose remaining tokens are from a **different request** → mismatched KV → wrong hidden states → garbled / off-topic generation.

In vLLM core, partial-hash handling is safe because the core owns the block pool and can reconstruct/verify the actually-matching sub-blocks. The Mooncake connector's mirror appears to map a coarse chunk existence check onto full-block reuse without that guarantee.

It is aggravated by the shared-store being ~92% full with eviction mostly failing (`attempts=1217, success=22`), which destabilizes the existence mirror and increases spurious/over-long hits, and by high external hit rates (59-65%) across many concurrent requests sharing a long agent system-prompt.

## Expected behavior

External prefix KV reuse should only be reported when the **full KV block** being reused is byte-identical to the current request's tokens at that position. Partial (sub-block) hits must not cause reuse of a mismatched full block.

## Steps to reproduce

1. Serve GLM-5.3-Flash (or any model with large attention block, e.g. 1152, and small hash block, e.g. 64) with:
   - `--enable-prefix-caching`
   - Mooncake `kv_role=kv_both`, two instances sharing one segment.
2. Send two different requests that share a long prefix but diverge **within the same 1152-token block** (e.g. same system prompt; different user task/question).
3. Observe the second request reusing external KV (`External prefix cache hit rate > 0`, `memory_keys>0`) and generating content that belongs to the first request.

## Workaround

Setting `--prefix-match-unit 1152` forces `hash_block_size == attention block size`, making `block_size > hash_block_size` false → `partial_hash_hits_enabled` returns false → only full, content-identical 1152-token blocks are reused, eliminating the contamination. It keeps prefix caching and cross-instance reuse (for fully identical prefixes), at the cost of a coarser (1152-token) matching granularity and a small loss of reuse on non-1152-multiple shared tails.

## Suggested fix (connector side)

In `partial_hash_hits_enabled`/`get_cached_block`/`align_lookup_length`, do **not** report a partial (sub-block) hit unless the full reused KV block is content-identical to the current request at that position. Concretely:
- Either treat the existence check at full-block (attention block) granularity regardless of `hash_block_size`, so a partial match cannot map onto a mismatched full block; or
- Gate partial hits so they only apply when `hash_block_size` is a divisor that coincides with the actual reusable KV block content boundaries, and verify content identity before reuse.

This likely affects MLA / multi-KV-group models (e.g. GLM5Next, DeepSeek V4-Flash) when `prefix-hash block (64) != attention block (1152)`. A secondary contributor worth noting alongside #2827 is the shared-store being near-full with SSD offload eviction mostly failing, which can also destabilize object existence and enable longer-than-valid reuse.

### Before submitting...

- [ ] Ensure you searched for relevant issues and read the [documentation]

## 评论 (9)

### github-actions[bot] · 2026-09-16

Thanks for opening this issue, @MarkLiJing!

| Field | Value |
|-------|-------|
| **Issue** | #4153 |
| **GitHub user ID** | `21461558` |
| **Reporter** | @MarkLiJing |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### he-yufeng · 2026-09-16

Confirmed the mechanism at code level on current vllm main (00972dfd7), and it is more specific than a plain full-block over-fetch: the contamination lands through the mamba state tail, which is the part that cannot self-heal.

The chain: `_tail_key_boundaries` (worker.py) handles the case where hit_length falls inside a physical block whose store key sits at a coarser boundary by scanning FORWARD from the hit boundary to a stored hash and returning that later boundary (`boundary_tokens = (hash_idx + 1) * hash_block_size`, which can exceed hit_length up to the 1152 block end). The recv side (`KVCacheStoreRecvingThread._handle_request`) then replaces the tail chunk's hash with the hash at that later boundary and fetches the whole store object written at it. For attention KV the over-fetched suffix is mostly benign because B's recompute overwrites it before it can influence earlier positions. For an align-mode mamba group the loaded object is a fixed-size recurrent state: the state at boundary 1152 encodes request A's entire prefix including the suffix B never shared, B continues the recurrence from it with its own tokens, and no later recompute can flush that out. That matches your runtime evidence exactly (coherent English reasoning dump unrelated to the prompt, only on the hybrid model).

On the adjacent work: #50359 is a different layer — it revalidates the reconciled joint hit boundary so a group cannot report a hit its own keys do not reach (FA 64 / Mamba 48 down to 32), but it does not touch this tail over-fetch. #53730 predates the current `_tail_key_boundaries` implementation on main (which arrived with #56513) and reads as superseded by it. So this defect is currently unowned.

A fix has to stop the tail load whenever the exact hit boundary is not itself stored for a non-sliceable state group; attention groups can additionally bound the fetch to hit_length to kill the waste. I am working on it, with a regression reproducing the H=64 / B=1152 geometry and the mamba-state contamination, and will link the PR here. Your store-pressure observations (92% full, eviction 22/1217) are a separate but real amplifier and worth their own look once the correctness hole is closed.


### he-yufeng · 2026-09-16

Correction to part of my earlier analysis, in the open: after walking the store-key geometry, the tail over-fetch I described cannot actually produce the contamination, and I do not want a wrong mechanism standing unchallenged.

Why it falls apart: store keys are per-64-chunk (`PoolKey.build_key_string(prefix, chunk_hash.hex())`), and hashes are cumulative over the prefix. For the forward scan in `_tail_key_boundaries` to find a boundary beyond hit_length, a later hash index within the same physical block would have to be stored while the intermediate chunk hashes miss. With cumulative hashing, a matching later hash forces every intermediate prefix to match too, which would have extended hit_length to that point in the first place. Contradiction both for full attention and for the align-mode mamba tail. The forward scan is dead code under this hashing model, not the contamination vector.

What still stands from the evidence: the contamination is real (your runtime dumps prove cross-request KV reuse), it correlates with partial-hash hits on the H=64 / B=1152 hybrid geometry, and #50359 does not cover it. The remaining candidate layers, in the order I am checking them next:

1. Local-pool stale content on partial hits: a recycled 1152-token block with only its first 64 chunks refilled from the store, the rest holding a previous occupant's KV. Attention overwrites it on recompute; a recurrent mamba state does not get that chance.
2. Store key aliasing under memory pressure: your master metrics show ~92% capacity with eviction succeeding 22/1217, a plausible amplifier for stale or aliased existence entries feeding the `_exists` mirror.

I am building the local repro at the exact H=64 / B=1152 hybrid geometry to separate these two, and will report which layer it lands in. If you can share one more data point in the meantime, it would discriminate them cheaply: whether the off-topic dumps appear only on requests whose hit_length fell strictly inside a 1152 block (partial) versus full-block hits.


### he-yufeng · 2026-09-16

Geometry probes against current vllm main (b0898a493) are in, and they clear the connector:

- Variant shaped like the fine-grained store (FA keyed at every 64-token sub-boundary, mamba keyed at block and sub-boundaries): B sharing exactly the first 64 tokens of A gets joint hit_length = 64 and both groups' tail boundaries come back HIT-EXACT at 64. The mamba state B would load at that boundary encodes only the shared prefix, so it is correct.
- Variant shaped like production (FA objects keyed only at full 1152 blocks): the joint reconciliation returns 0, because A's full-block key cannot match B's divergent suffix, so nothing is reused at all. No over-fetch, no inflation.

Block hashes chain over the parent block (hash_block_tokens takes parent_block_hash), so exact-prefix matching is sound end to end. With the connector ruled out by direct probes, the remaining vector is store-side: at your ~92% full master with eviction succeeding 22/1217, the duplicate-offload and eviction-race family is what can make a key serve bytes that do not belong to it. That is the same defect family as #2827 (concurrent duplicate offload -> OBJECT_ALREADY_EXISTS -> master/SSD metadata divergence -> cross-request KV), and #3135 (merged today) makes re-offload of persisted keys idempotent in BatchOffload, which closes one of its producers.

Concrete next step I'd suggest: rerun the failing workload with #3135 in. If contamination still appears, the remaining hole is eviction-race aliasing (a key mapping to a replica that was evicted and reallocated under pressure), which needs an integrity check on the master/SSD key-to-replica mapping rather than anything in the connector. I will keep the probe geometry around and can extend it to the eviction-race case next.


### he-yufeng · 2026-09-16

Store-side follow-up to the connector probes above. I audited the read path on the Mooncake store at current main (ffe01351), because that is the layer the contamination has to come from once the connector is clean.

What is guarded:

- Every memory-resident read path carries the master read lease: `GetReplicaList` grants a 10s lease by default (`DEFAULT_DEFAULT_KV_LEASE_TTL`, types.h:84), the master eviction loop skips keys with unexpired leases, and the client converts a read that outlived its lease into a loud `LEASE_EXPIRED` after the transfer (`client_service.cpp:1377`, `:1422`, `:1576`, `:1826`). Within the lease a memory replica cannot be evicted, past the lease the read fails loudly. No silent window there.

What is not guarded:

- The connector loads through `batch_get_into_multi_buffers`. Its MEMORY/NOF and DISK/DFS sub-paths delegate to the guarded `Client::BatchGet`, but LOCAL_DISK (SSD offload) replicas go through the offload RPC branch (`real_client.cpp:6477` -> `:6510` -> `:6772`) which has no master read-lease check at all. The only guards on that branch are the offload-side `gc_ttl` elapsed check (`:7413`, and only when the batch is not node-local) and the optional object CRC behind `MOONCAKE_STORE_CHECKSUM` (`environ.cpp:204`, default off).

So in an offload-enabled deployment under eviction churn (your 92% full pool with 22/1217 evicted), an offload read that outlives its 10s master lease, or that races an eviction plus backing-slot reuse, can complete as success with bytes that no longer belong to the key, and nothing on that path would notice. That is the only silent channel I have found that matches the symptom (attention sinks plus garbage inside the shared prefix region).

Three data points would confirm or kill this theory from your side:

1. Is the deployment running with SSD offload enabled, and with what `client_buffer_gc_ttl_ms`?
2. Do the worker logs contain `lease_expired_before_data_transfer_completed` or `OBJECT_HAS_LEASE` warnings around the incident window? Their absence on a memory-resident read would itself be evidence the reads went through the offload branch.
3. Is `MOONCAKE_STORE_CHECKSUM` set? If it is off (the default), the last safety net on the offload path is also down.
4. Which store build is the deployment on, relative to two recent fixes? #3929 (merged 2026-09-11) closed a silent data-integrity bug where a batch get containing the same key twice left one occurrence's buffer unwritten while reporting success, which would surface downstream exactly as stale foreign bytes in a KV block. #3135 (merged today) made re-offload of an already-persisted key an idempotent skip, closing a duplicate-offload producer. If the build predates #3929, that alone is a sufficient explanation and the eviction angle becomes secondary.

On my side I am now probing the last link: whether the offload file storage reuses a freed object slot for a different key's bytes while a read of the old object is still in flight. Will report back with a synthetic slow-read race probe.

(This analysis was assisted by Kimi K3; all cited lines were re-read and verified on the pinned commits.)


### he-yufeng · 2026-09-16

Follow-up on the promised slot-reuse probe. I went through the offload file backend instead of building the race harness, because the layout settles the question by construction:

- The backend stores one file per object at a key-derived path (`ResolvePathFromKey`), holds a striped per-path lock across create+write and across evict+delete, and reads open the path fresh.
- Evicting a key removes its file. An in-flight read that already opened the file keeps reading the old inode's bytes (POSIX fd semantics), so it still gets the correct content; a read that arrives after the delete fails open with a loud `FILE_OPEN_FAIL`. There is no region-level slot that a different key's bytes could move into.
- Same-path rewrite requires the same key, and the connector keys are content-addressed on both sides: on the write path the key hash chains every token up to the stored span (`worker.py` builds `key_hash` from `block_hashes[valid_end // hash_block_size - 1]` with the payload spanning exactly that range), so identical key means identical bytes.

So the offload-slot-alias channel I offered to probe does not exist in this design; a synthetic race probe would demonstrate nothing. With the memory path lease-guarded and the offload file path fail-loud-or-correct, the silent channel that still matches your symptom byte for byte is the duplicate-key batch read fixed in #3929: one unwritten buffer reported as success, and the GPU slot then serves whatever a previous request left in it. If your build predates 2026-09-11, that is the first thing to rule out by upgrading; the version question from my previous comment is now the decisive one.


### he-yufeng · 2026-09-16

One more connector layer closed. Beyond the earlier hit/tail-boundary probes, I checked the hit-to-mask mapping and the load payload shape on upstream/main @ b0898a493 with the same bare-worker geometry (A stores a full 1152-token block; B shares exactly the first 64 tokens):

- `find_longest_cache_hit` returns `hit_length=64` with per-group masks marking exactly chunk 0 for both the FA group and the mamba-align group. No group marks anything past the 64-token hit, so the mapping cannot round a partial hit up to a full 1152-token reuse.
- On the load path, `process_tokens` keys the span by the hash at its end (`block_hashes[end // hash_block_size - 1]`) and `prepare_values` sizes the fetch by the whole physical block, so the value read under the 64-boundary key is the writer's own stored slot; the key's hash chain covers exactly the stored span on the write side too, so identical key means identical bytes.

With lookup, hit, mask, tail-key, and payload shape all checking out, I have no connector-side mechanism left that matches your symptom, and the memory-tier tier summary in your log (`memory_keys=36, failed_keys=0`) puts the polluted read on the memory path rather than the SSD-offload path. The version question from my earlier comment is now the decisive fork: pre-#3929 builds report duplicate keys in one load batch as success while leaving one occurrence's buffer unwritten, which surfaces exactly as foreign bytes in a KV block. #4164 (conductor `PrefixCacheTable` token clamp) is a real fix but SGLang-chain-shaped; it does not intersect your vLLM deployment.


### MarkLiJing · 2026-09-17

1. SSD offload & client_buffer_gc_ttl_ms
SSD offload is enabled:

mc-master: --enable_offload=true --offload_on_evict=true --eviction_high_watermark_ratio=0.95 --promotion_on_hit=true --promotion_admission_threshold=1
mc-client: --enable_offload=true --start_offload_rpc_server=true, MOONCAKE_OFFLOAD_FILE_STORAGE_PATH=/data/file_storage (XFS RAID on /dev/md0), global_segment_size=1099511627776 (1 TiB)
client_buffer_gc_ttl_ms is not set (left at the store default; I can read the compiled default and report it if useful).

2. Lease warnings in the incident window
I grepped the captured worker/store logs for lease_expired_before_data_transfer_completed and OBJECT_HAS_LEASE around the incident: neither appeared. The polluted load was on the memory tier (Mooncake load tier summary: batch_keys=36 memory_keys=36 ... failed_keys=0, 526 MB reused) and no lease warning accompanied it.

3. MOONCAKE_STORE_CHECKSUM
not set → the offload-path CRC safety net is down.

4. Store build vs #3929 / #3135
The store in the deployment is mooncake-transfer-engine 0.3.12.post1 (PyPI release 2026-07-25). This predates #3929 (merged 2026-09-11)​ and #3135 (merged 2026-09-16). Image: vllm/vllm-openai:glm53-flash-cu129-mooncake-kvpoolfixed (the only local patch is a GLM multi-KV-group compat shim, unrelated to #3929).

This is consistent with your decisive check: a pre-#3929 build, where a batch get containing the same key more than once reports success while leaving one occurrence's buffer unwritten — surfacing as foreign stale bytes in a KV block on the memory path. We will upgrade to a store build containing #3929 (and #3135) and re-run the failing workload, and report whether contamination persists.

### he-yufeng · 2026-09-17

That build date is the answer. `0.3.12.post1` (2026-07-25) carries #3929 live in your deployment, on exactly the tier your logs point at.

For the record, the mechanism fits your symptom byte for byte. Your load batches come from requests that share a long system prompt, so the same block keys appear more than once in a single `batch_get_into_multi_buffers` call (two overlapping requests in flight, or one prompt with repeated content blocks). Pre-#3929, a batch get with a duplicate key transferred only the first occurrence and reported success for the rest, leaving the remaining destination buffers untouched: the GPU KV slots for those blocks kept whatever a previous request had written there. Attention then reads them as valid prefix KV, which is precisely "attention sinks plus garbage in the shared-prefix region" on the memory tier, no lease warning, checksum irrelevant.

Your upgrade should close it. On re-run:

- If the workload is clean, the case is settled as #3929 and the eviction-churn details were just pressure on the trigger, not the mechanism.
- If anything persists, that would be genuinely new information: it would put the suspicion back on the read path below the connector, and the next thing I'd want is the same joint-hit probe you saw me run, but pointed at your exact key/buffer geometry from the incident request.

One related note since you run `offload_on_evict=true` with a 98% eviction-failure rate: #3135 (also post-dates your build) made re-offload of an already-persisted key an idempotent skip, closing a duplicate-offload producer that could poison the SSD side the same way. It is not needed for the memory-tier case here, but you get it in the same upgrade.

Thanks for running down the four data points so quickly.


# [Issue #5230] MP mode (LMCacheMPConnector) ignores save_decode_cache and stores decode KV, causing unbounded L1/L2 writes and premature eviction

source: https://github.com/LMCache/LMCache/issues/5230
state: open | updated: 2026-09-21T00:09:53Z
labels: 

## 正文

**Label**
LMCache Onboarding (#1882) · MP mode · bug

**Summary**
In MP mode, the vLLM-side LMCacheMPConnector stores every full chunk of prompt + generated tokens with no save_decode_cache gate and no cap at the prompt length. The chunk that straddles the prompt→output boundary is completed during decode by sampled (non-deterministic) output tokens, so it hashes differently on every request. The result is a brand-new KV chunk stored per request even when the prompt set is fixed and fully cached — so the cache keeps writing after warmup, L1 fills and evicts, and shared L2 (e.g. S3) fills up. The documented save_decode_cache=false (which is the default) is honored by the in-process LMCacheConnectorV1 but not by LMCacheMPConnector.

**Details**
- The store decision runs in vLLM's vendored connector vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py (factory maps "LMCacheMPConnector" here; no kv_connector_module_path is needed to trigger it). The editable lmcache_mp_connector.py is not the code that runs.
- Offending logic in LMCacheMPRequestMetadata.GetStoreMetadata:
_computed_blocks = tracker.num_scheduled_tokens // vllm_block_size + max(
    tracker.num_vllm_hit_blocks, tracker.num_lmcache_hit_blocks)
min_available_blocks = min(len(tracker.block_hashes),
```bash
                           len(tracker.allocated_block_ids), computed_blocks)
num_staging_blocks = min_available_blocks - tracker.num_stored_blocks
num_chunks = num_staging_blocks // blocks_in_chunk     # stores EVERY full chunk
token_ids = list(tracker.all_token_ids)                # includes generated tokens_
```
- Trigger condition: with r = templated_prompt_len mod chunk_size, a decode chunk is written whenever r + OSL >= chunk_size; the number stored per request is floor((r + OSL) / chunk_size). For Llama-3.1 chat (template overhead ≈ 34 tokens) with chunk_size=256, OSL=250 writes 1 unique chunk/request; OSL=100 writes 0.
- lmcache.skip_save per-request (kv_transfer_params) does not help: it is not honored by the MP connector (the MP config docs explicitly warn against relying on it), and even where honored it disables all saving (prefill too).
- Versions checked: reproduced on vllm==0.26.0; source of the latest release v0.29.0 is identical (same GetStoreMetadata, no gate) — so it is not fixed upstream.

**Steps / Reproduction (if applicable)**
- Start an MP server: lmcache server --host 0.0.0.0 --port 6555 --chunk-size 256 --l1-size-gb 60 --eviction-policy LRU --eviction-trigger-watermark 1.0.
- Start vLLM with --kv-transfer-config '{"kv_connector":"LMCacheMPConnector","kv_role":"kv_both","kv_connector_extra_config":{"lmcache.mp.server_urls":["tcp://localhost:6555"]}}' (Llama-3.1-8B-Instruct).
- Replay a fixed set of prompts (e.g. aiperf ... --random-seed 42 --num-dataset-entries 50 --endpoint-type chat --isl 8192 --isl-stddev 0 --osl 250 --extra-inputs '{"ignore_eos": true, "min_tokens": 250}') so the working set fits in L1 and no eviction should occur.
- Observe: after the first pass the server keeps logging Stored 256 tokens at ~request rate, L1 memory usage 1.00 above watermark … triggering eviction fires, and external prefix-cache hit rate plateaus below 100%. With --osl 100 (so r+OSL < 256) the writes stop after the first pass and no eviction occurs — confirming the boundary/decode-chunk mechanism.

**Expected Outcome / Goal**
With save_decode_cache=false (the default), MP mode should not store decode KV. A fully-cached, replayed prompt set should be reads-only after the first pass regardless of OSL — no per-request stores, no eviction. save_decode_cache should be honored in MP mode (or the MP connector should cap stores at the prompt length by default)

**Actual Outcome (if applicable)**
MP mode stores the decode/boundary chunk on every request (unbounded, unique writes), fills L1 and shared L2, and triggers eviction even when the unique working set easily fits — because the MP connector stores all full chunks of prompt + generated tokens and ignores save_decode_cache.


## 评论 (2)

### sssqqeer · 2026-09-18

Hi, I'd like to take this. I've reproduced the extra store when decode tokens complete a partial prompt chunk, and I have a local fix with regression tests. The fix limits stores to complete prompt chunks by default, with an explicit option to keep decode caching enabled. I'll finish the end-to-end validation before opening the PR.

### stefanskiasan · 2026-09-21

**Confirming this on an MLA model, where the write amplification is far worse — plus a regression test**

We hit this on GLM-5.3 (DeepSeek-V3-style MLA, 92 layers, fp8 KV) running `lmcache_driven` with TP=4 on MI350X.

**Why MLA makes this expensive.** With MLA the per-token KV is `kv_lora_rank 512 + qk_rope 64 = 576` values per layer. At fp8 across 92 layers that is **47.3 KiB per token** — we measured exactly that (1.09 TiB across 97,148 chunk files at 256 tokens each). So a single 900k-token context is **42 GiB**, and every superfluous chunk store is immediately costly.

**What we measured in production**, before capping:

| | |
|---|---:|
| L2 write load | **1.24 TiB/h** |
| per store request | 20.4 chunks = **5219 tokens** |
| external prefix cache hit rate | **1.2 %** |

The telling number is the second row. 5219 tokens per store request is not a prompt length — it is an *output* length. That was the clue that led us here.

**The fix we shipped locally** is the cap from #5239, applied to `GetStoreMetadata` in `lmcache_mp_metadata.py`: the tracker records `request.num_prompt_tokens` at construction, and the upper bound becomes `min(len(all_token_ids), num_prompt_tokens)` unless an env switch restores the old behaviour.

**A unit test that pins the behaviour** — it builds a tracker by hand, so it needs no GPU and no server:

```python
CHUNK, PROMPT, GENERATED = 256, 1024, 2048

def chunks(prompt, total):
    t = LMCacheMPRequestTracker.__new__(LMCacheMPRequestTracker)
    t.all_token_ids = list(range(total))
    t.num_prompt_tokens = prompt
    t.allocated_block_ids = {0: list(range(1, total // 64 + 2))}
    t.num_stored_tokens = 0
    t.num_scheduled_tokens = total
    t.num_vllm_hit_tokens = t.num_lmcache_hit_tokens = 0
    t.mm_adjusted_prompt_ids, t.cache_salt, t.request_id = [], "", "probe"
    r = LMCacheMPRequestMetadata.GetStoreMetadata(t, CHUNK, [64])
    return 0 if r is None else (r.op.end - r.op.start) // CHUNK

assert chunks(PROMPT, PROMPT + GENERATED) == PROMPT // CHUNK        # 4, not 12
assert chunks(PROMPT, PROMPT) == PROMPT // CHUNK                    # prompt-only unchanged
```

Results here: **4 chunks with the cap, 12 without**, and prompt-only stores are untouched. Happy to open this as a PR against the #5239 branch if that would help.

**One observation that may be worth a separate issue.** While chasing this we found that the `fs` L2 adapter declares no capacity at all — `FSL2AdapterConfig` accepts only `base_path`, `relative_tmp_dir`, `read_ahead_size`, `use_odirect`. Its own source comment spells out the consequence:

> the FS adapter declares no max capacity (default 0) so `supports_global_eviction` returns `False` … the eviction controller treats this as "no eviction signal" and skips the adapter entirely.

So with `type: "fs"` there is no eviction at all and the volume fills until it is full — for us that was ~300 GB/h before the decode fix, 1.3 TiB/h after load increased. `fs_native` takes `max_capacity_gb`, but per #4787 that only declares capacity for accounting unless an `eviction` block is also present. A warning at startup when an `fs` adapter is configured without any bound would have saved us a night.


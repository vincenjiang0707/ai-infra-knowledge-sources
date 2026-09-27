# [Issue #3917] [Bug] lmcache-mp (TRT-LLM): store/retrieve crash on non-chunk-aligned block lists (save_unfull_chunk=False)

source: https://github.com/LMCache/LMCache/issues/3917
state: open | updated: 2026-09-23T01:54:03Z
labels: 

## 正文

### Summary
With the TensorRT-LLM `lmcache-mp` connector and `save_unfull_chunk=False` (the default), any request whose prompt length isn't an exact multiple of `chunk_size` crashes the store (and retrieve), failing the request:

```
AssertionError: len(block_ids[0]) should be a multiple of total_blocks_per_chunk (8), but got 68
  File ".../lmcache/v1/multiprocess/modules/lmcache_driven_transfer.py", line 186, in downsample_and_stage_block_ids
    assert len(old_block_ids) % total_blocks_per_chunk == 0, (
```

### Environment
- LMCache 0.5.0
- TensorRT-LLM 1.3.0rc16, connector `lmcache-mp`
- gpt-oss-120b: `tokens_per_block=32`, `chunk_size=256` → 8 blocks per chunk

### Root cause
`downsample_and_stage_block_ids` (added in #3612 for sliding-window / multi-object-group support) asserts each group's block list is an exact multiple of `total_blocks_per_chunk`. But the engine hands it a block list covering *all* prompt tokens, so it can include a trailing **partial** chunk when the prompt length isn't a multiple of `chunk_size` (e.g. 8 full chunks = 64 blocks + a 4-block tail = 68 blocks, not a multiple of 8).

`num_chunks` (derived from the keys, which already honor `save_unfull_chunk=False`) counts only the whole chunks, and the caller's own underflow check already guarantees `len(block_ids) >= num_chunks * blocks_per_chunk`. Nothing trims the upper-bound partial before the assert, so any non-aligned prompt deterministically crashes.

### Reproduce
TRT-LLM + `connector: lmcache-mp`, `chunk_size=256`, `save_unfull_chunk=False` (default); send any prompt longer than one chunk whose length isn't a multiple of `chunk_size`. A single such request reliably reproduces the assert. (Short or chunk-aligned prompts, and pure cache hits, don't trigger it — likely why the E2E tests pass.)

I'll open a PR with a fix.


## 评论 (2)

### github-actions[bot] · 2026-08-27

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.

### git-jxj · 2026-09-23

The fix for this issue is still under review in #4879. Its current head is `71f1a064f`, and the GitHub Actions runs are awaiting maintainer approval. Please keep this issue open while that PR is evaluated; it will close automatically if the PR merges.


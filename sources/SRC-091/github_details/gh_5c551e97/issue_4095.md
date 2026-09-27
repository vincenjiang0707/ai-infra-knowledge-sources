# [Issue #4095] [Feature][MP] SGLang MP mode: async (non-blocking) store on request finish

source: https://github.com/LMCache/LMCache/issues/4095
state: open | updated: 2026-09-17T01:47:56Z
labels: stale

## 正文


**Label**
new feature as Mentioned in Q3 (roadmap #4025 )

**How it is related?**

I was reading through the SGLang MP integration and noticed the store on the request-finish path is synchronous. In `LMCacheMPConnector.store_kv` (`lmcache/integration/sglang/multi_process_adapter.py`) it waits on `.to_cuda_future(...).result(timeout=...)` before returning.

The SGLang side leans on that. In `LMCRadixCache.cache_finished_req` the MP branch stores, then immediately drops the lock and ends the session, and there's a comment saying as much:

> `# MP store_kv blocks until the daemon's signal event fires, so the slots are safe to evict immediately.`

The thing is, this store happens after the forward pass and nothing downstream actually waits for its result, so as far as I can tell the block is just wasted time where the scheduler sits idle. This looks like the store half of the "SGLang MP mode async store/retrieve" item in #4025.

**Solution I Thought**

I think MP store can be made non-blocking by reusing the same deferred pattern IP mode already uses. In IP mode, `cache_finished_req` fires the store on `store_stream`, keeps the node locked, stashes it in `_in_flight_nodes`, and later `evict()` does `store_stream.synchronize()` + `dec_lock_ref` to clean up. MP could do the same shape, except the "is it done?" check would be the daemon's completion signal instead of a CUDA stream sync.

Rough order I had in mind:

1. LMCache side — have `store_kv` submit and hand back a completion handle instead of blocking, plus a way to check/await it later.
2. SGLang side — in `cache_finished_req` (MP branch), keep the node locked and append to `_in_flight_nodes` instead of blocking and unlocking inline.
3. SGLang side — in `evict()`, wait on the daemon completion for those in-flight stores before releasing the locks.

I'd keep this to store only. Retrieve looks harder: `init_load_back` returns synchronously and the scheduler uses the result right away, so making retrieve async would need a new park-and-poll path in the SGLang scheduler. ( A bigger and complex for me 😅)

**Alternatives I have considered**

- Leaving store synchronous, which is obviously simplest but keeps the idle time and leaves this half of the roadmap item open.
- Fire-and-forget with no lock tracking, but that's unsafe since the slots could get evicted before the daemon finishes reading them.
- Adding a dedicated completion-poll hook in the SGLang scheduler, but that seems like overkill for store given `evict()` + `_in_flight_nodes` already give a natural place to reconcile. (May be Retrieve would actually need something like that.)


I'm happy to pick this up and split it into two PRs (the LMCache API change first, then the SGLang side that consumes it). Before I start though, does the scope sound right, and is anyone already working on it?

## 评论 (10)

### sahibpreetsingh12 · 2026-07-13

Tagging @maobaolong and @sammshen for your thoughts

### ApostaC · 2026-07-13

Also cc @Shaoting-Feng 

### Shaoting-Feng · 2026-07-14

Right now the store is synchronous. In general, your proposal sounds good to me. About "plus a way to check/await it later" for `store_kv`, is there any existing API that supports this?

### sahibpreetsingh12 · 2026-07-14

Thanks @Shaoting-Feng  No I dont think we need something new  since `store_kv` already builds a future via `to_cuda_future()` but consumes it with  `.result()`. The future already supports query and wait(), so the change will be to return it instead of blocking it.
What are your thoughts ?

### Shaoting-Feng · 2026-07-15

Looks good to me. Feel free to ping me when the PR is out.

### sahibpreetsingh12 · 2026-07-16

Perfect I will get back @Shaoting-Feng 
One question I had after seeing SGLANG Right now `store_kv` in `integration/sglang/multi_process_adapter.py` blocks until the daemon confirms the store is done. The problem is SGLang's **LMCRadixCache** depends on that blocking — it unlocks the KV slots right after the call, assuming the copy has finished. So if I just make store_kv non-blocking, an SGLang build without the matching change could unlock those slots mid-copy.

 Two possible ways I can go:
(a) Change store_kv in place to return the future instead of blocking, and coordinate it with a version bump so SGLang requires the LMCache release that has this change.
(b) Leave store_kv blocking and add a separate non-blocking method (e.g. store_kv_async) that returns the future, so nothing breaks and SGLang opts in when ready.

which one is your recommendation or if you have some other suggestion I am open to that?

### Shaoting-Feng · 2026-07-17

I prefer (b). For SGLang, I don't know when you PR will be merged. So it is good to keep it working even before SGLang PR is merged. After SGLang PR is merged, you can submit another PR on LMCache side to deprecate the old `store_kv`.

### sahibpreetsingh12 · 2026-07-18

perfect @Shaoting-Feng 

### sahibpreetsingh12 · 2026-07-18

@Shaoting-Feng I have raised the PR. Please let me know if any changes are required.
Thanks

### github-actions[bot] · 2026-09-17

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.

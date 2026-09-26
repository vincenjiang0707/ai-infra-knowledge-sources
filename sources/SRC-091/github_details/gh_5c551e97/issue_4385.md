# [Issue #4385] [Bug] Cross-request KV contamination with local disk backend: returning sessions answer with OTHER requests' content (v0.5.2, vLLM 0.26.0)

source: https://github.com/LMCache/LMCache/issues/4385
state: open | updated: 2026-09-24T15:35:24Z
labels: 

## 正文

Hi team,

First off, thanks for maintaining LMCache! 

I ran into a critical silent KV cache corruption issue where long-context sessions served from the disk tier end up getting KV cache belonging to *other* requests. 

Below are the details and reproduction steps.

---

### Bug Description

When using `local_cpu` + `local_disk` backends, long-context sessions returning after their KV cache has been paged to the disk tier receive KV data belonging to **other requests**. 

As a result, the model answers questions using facts from a completely different conversation (and sometimes includes fragments from unrelated concurrent short requests). No errors/warnings are logged—the corruption is entirely silent.

### Environment

- **LMCache Version:** 0.5.2 (latest)
- **vLLM Version:** 0.26.0 (matched per v0.5.2 release notes)
- **GPU:** Single GPU (24 GB)
- **OS:** Linux
- **Model:** `hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4` (FP16 KV)
- **Config:** 
  - `chunk_size`: 256
  - `local_cpu`: true, `max_local_cpu_size`: 8
  - `local_disk`: `file://...`, `max_local_disk_size`: 28 (sized large enough so eviction is never triggered, keeping issue #1981 out of scope)
- **Connector:** `{"kv_connector": "LMCacheConnectorV1", "kv_role": "kv_both"}`

### Steps to Reproduce

1. Created 6 distinct sessions of ~32K tokens each. Each session contains a unique needle (`"the vault code is ZK-600<i>"`) inserted at 10% depth (Needle-In-A-Haystack setup).
   - Total working set ≈ 24 GB KV, forcing most chunks onto the disk tier (`local_cpu` is limited to 8 GB).
2. Ran a 150-second mixed load:
   - The 6 long-context sessions periodically return (full prompt resent, prefix served via LMCache).
   - Concurrently, 3 background workers send short unrelated requests (`"the ticket number is TK-<k>..."`).
3. Verified the generated answers against each session's ground-truth needle.

### Observed Behavior

Returning sessions consistently answered with the **WRONG** session's needle. 

A single-return probe after the load test yielded:
- **Session 0:** Expected `ZK-6000` $\rightarrow$ Got `"ZK-6001. The ticket number is TK-"`
- **Session 2:** Expected `ZK-6002` $\rightarrow$ Got `"ZK-6000. ..."`
- **Sessions 3, 4, 5:** Expected `ZK-6003/4/5` $\rightarrow$ All got `"ZK-6001 ..."`

Notice that responses also contain text fragments from concurrent short requests (`"The ticket number is TK-"`), confirming KV cross-talk across completely independent requests.

Across the entire 150s window (138 total session returns), **only 14 answered with their own needle (~10% accuracy)**.

#### Sanity Checks / Controls
- **Clean Environment:** Successfully reproduced twice on a completely reset environment (fresh server processes, wiped store directories, 40GB free RAM, empty GPU memory).
- **Control Test:** Running the exact same benchmark harness on stock vLLM (no connector) and another KVConnector implementation yields **100% accuracy**, confirming the harness itself is clean.
- **Cold Run:** Cold runs (initial store population, few returns) do NOT show this bug—it only emerges once requests start being served back from the disk tier at scale.

### Expected Behavior

A returning request should only ever be served KV chunks derived from its own exact token prefix. If a key mismatch occurs, it should trigger a cache miss (recompute), never silently inject cross-talk/corrupted KV content.

---

### Additional Context

* Note: While isolating this, we also hit the eviction crash already tracked in #1981 (`FileNotFoundError` in `local_disk_backend.remove` during `batched_remove`) on a single-GPU setup, and left a comment there.
* I have the full benchmark script and logs ready if needed. Happy to share them to help debug!

Thanks again for looking into this!

## 评论 (2)

### zhengfeihe · 2026-08-02

Hi~ Thank you for the bug report!

However, it seems you are using LMCache in in-process mode, which will be deprecated soon. Could you try multi-process (MP) mode instead, which launches LMCache as a separate process? New model support and new storage backend features are mostly being added to MP mode.



### KPST-LAB · 2026-08-05

Thanks for the pointer! We re-ran the exact same reproduction benchmark under
MP mode as suggested (`lmcache server` over ZMQ + `LMCacheMPConnector`).

### Environment & Setup
* **Hardware:** Single NVIDIA RTX 4090 (24 GB)
* **Framework:** vLLM 0.26.0
* **Model:** `hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4` (FP16 KV)
* **vLLM Flags:** `--max-model-len 34000`, `--gpu-memory-utilization 0.90`
* **LMCache Config:** L1 = 8 GB CPU RAM (LRU), L2 = local-disk `fs` adapter
* **Testing Procedure:** Identical to the original report. Built 6 fully
  distinct ~32K-token sessions, ran a 150s warm mixed load (6 long sessions
  reconnecting continuously + 3 short-request clients), followed by 6 isolated
  warm reconnects. Checked every response against a planted fact in that
  session's context.

### Result
**The contamination does NOT reproduce under MP mode.** All 221 responses
across every phase were correct (184 + 31 mixed load, 6/6 isolated
diagnostics, zero cross-session contamination).

This confirms your reading: the issue is isolated to the current in-process
path (`LMCacheConnectorV1`) rather than the underlying architecture. MP mode
resolved the accuracy defect in our reproduction.

---

### Two Follow-up Points from the MP Run

1. **Default Path Risk:** Until the in-process path is actually removed or
   deprecated, standard users remain exposed. On v0.5.2, the documented
   `--kv-transfer-config` example is still the in-process connector. In our
   measurements, **89.9% (124/138) of warm reconnects returned content from a
   different session**. A warning in the docs or an early deprecation notice
   on the connector would protect users who haven't migrated yet.
2. **Docs / Implementation Mismatch:** While setting up MP mode, we hit a
   small schema mismatch: the `--l2-adapter` help text specifies
   `{"type":"fs","path":...}`, but the implementation actually requires
   `base_path`. Startup fails if you use the exact CLI example from the docs.

---

### Performance Context
For completeness, MP-mode throughput in our mixed-load scenario was noticeably
lower than the in-process path:
* **Short requests completed:** 416 → 184 (over 150s)
* **Reconnect latency (p50):** 0.78s → 4.92s

This overhead is expected given the extra IPC/process hop over ZMQ, but worth
noting for capacity planning and sizing.

Happy to share our full benchmark scripts and logs if they would be useful for
your team!

> Hi~ Thank you for the bug report!
> 
> However, it seems you are using LMCache in in-process mode, which will be deprecated soon. Could you try multi-process (MP) mode instead, which launches LMCache as a separate process? New model support and new storage backend features are mostly being added to MP mode.



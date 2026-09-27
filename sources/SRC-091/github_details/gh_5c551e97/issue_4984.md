# [Issue #4984] [Bug] LMCacheMPConnector + MTP: deterministic corruption on multi-step retrieves, Qwen3.8 hybrid (persists after #4253)

source: https://github.com/LMCache/LMCache/issues/4984
state: closed | updated: 2026-09-23T19:02:09Z
labels: 

## 正文

**Environment**

| | |
|---|---|
| Model | Qwen3.8-27B INT8-W8A16 (`Qwen3_5ForConditionalGeneration`, GDN hybrid) |
| vLLM | 0.27.1 and 0.28.0 (`lmcache/vllm-openai:latest` and `:v0.5.5rc5`) |
| LMCache | 0.5.4 and 0.5.5rc5 (`g3ba43aef`), `LMCacheMPConnector` via `kv_connector_module_path`, `kv_role: kv_both` |
| GPUs | 2x RTX 3090, TP=2, FlashInfer, `--kv-cache-dtype fp8_e4m3` |
| Server | `--chunk-size N --separate-object-groups --l1-size-gb 32 --eviction-policy LRU` (N=1568 no-MTP / 1616 with MTP, from vLLM's `Setting attention block size` line) |
| vLLM flags | `--enable-prefix-caching --mamba-cache-mode align --enable-chunked-prefill --max-num-batched-tokens 2N-1`, MTP `num_speculative_tokens: 4` when noted |

**Method:** store a long prompt, wait ~30s for async stores to drain, `POST /reset_prefix_cache` (dev mode, local APC only), resend the identical prompt at `temperature: 0`, compare full completion text.

**Results**

| Setup | Retrieve correctness |
|---|---|
| 0.5.4 stock, MTP on | flaky garbage (multilingual token salad) on multi-chunk retrieves |
| 0.5.5rc5 stock, MTP off | flaky garbage |
| 0.5.5rc5 + manual #4253 patch, MTP off | **9/9 bit-identical** (2/3/5-chunk prompts); 258k-token max-context retrieve in 2.4s, **bit-identical**, repeated twice |
| 0.5.5rc5 + manual #4253 patch, MTP on | **0/10 identical** — deterministic corruption on any retrieve spanning more than one scheduler step (single-step, <=2 chunks, fine) |

With the patch, the startup fingerprint is `{'mamba-unified-view': 48, 'subpaged-attention-view': 16}` (no MTP) / `: 17}` (MTP), matching the fixed signature from the #4247 thread — so the layout fix is active, and the MTP failure looks like a separate mode (draft-layer KV restore across steps?).

**Notes for anyone reproducing**
- Without a ~30s drain after the store, retrieves race in-flight async stores and mostly recompute (false "pass") — worth knowing when validating.
- vLLM 0.28.0 behaves the same as 0.27.1 in my runs.

Related: #4247, #4886, #4889, #4253 (unmerged — applied manually here from the PR diff).


## 评论 (5)

### zhengfeihe · 2026-09-07

Hi~ 

Thanks for the detailed report. I reproduced locally and I think it's a separate issue.

### kavehs87 · 2026-09-07

Follow-up with instrumented data — I think I can rule out hit-accounting on my setup.

Setup for this run: vLLM 0.28.0 + LMCache 0.5.5rc5 + manual #4253, Qwen3.8-27B-INT8-W8A16, TP=2, MTP n=4, chunk 1616. Startup fingerprint is `{'mamba-unified-view': 48, 'subpaged-attention-view': 17}` so the layout fix is active.

Repro is store 4538 tok fresh (~35s) -> 30s drain -> `reset_prefix_cache` (local only) -> resend same prompt. Retrieve finishes in ~1.5s but output differs.

I added temporary logging around `get_num_new_matched_tokens` / `GetRetrieveMetadata` and the hybrid fixed-point lookup. On the corrupting retrieve:

```
geometry role=SCHEDULER group_tokens_per_block=[1616, 1616, 1616, 1616] hit_alignment=1616
matched-tokens vllm_hit_in=0 vllm_hit_aligned=0 lmcache_hit=3232 need_to_load=3232 align=1616 req_nprompt=4538 req_nall=4538
retrieve-range start=0 end=3232 skip_first_n=0 vllm_hit=0 lmcache_hit=3232
server: Prefetch 6/8 retained keys (6 L1, 0 L2)
server: Retrieved 3232 tokens (both GPUs)
```

Registration shows groups 0-2 as 48 GDN layers `[NB, BS, NH, CS]` int8 and group 3 as 17 layers `[NB, 2, BS, NH, HS]` uint8, all `tokens_per_block=1616`.

So as far as I can tell the addressing is all consistent — aligned geometry, exact contiguous range [0,3232), correct byte counts transferred — and it still comes back garbage. That makes me doubt my earlier guess about max() of per-group hits, at least for this case.

What still fits everything I see:
- single-scheduler-step retrieves are bit-identical, multi-step with MTP corrupt 0/10 here
- same tests with MTP off were 9/9 identical including a 258k retrieve

So I'm now suspecting the MTP state pages themselves rather than the hit math — either what gets stored for GDN on an MTP step, or restoring it across steps. Happy to grab any other counters/traces that would help pin it down.


### zhengfeihe · 2026-09-07

@kavehs87  

Thanks for help checking, I think the cause is 

With MTP enabled, vLLM's scheduler merges the last full block of the prompt and the trailing partial block into **one** prefill step Without MTP these are two steps with a stop at the block boundary. Reference in `_mamba_block_aligned_split` inside `scheduler.py`

In align mode the GDN kernel writes one state per scheduler step, into the block slot of the step's last token. A slot gets a valid state only if some step ends exactly at that slot's boundary.

 Without MTP, prefill of a 4538-token prompt takes three steps and stops at every boundary, so slot 1 (boundary 3232) holds a real state:

      tokens      0        1616       3232       4538
                  |----------|----------|---------|
      MTP off     [ step 1  ][ step 2  ][ step 3 ]
      state slot       0          1          2       <- 3 states written
      Mamba list  [ A ,       B ,        C , ...]

  With MTP, `use_eagle()` makes the scheduler skip the last cacheable boundary, so step 2 runs from 1616 straight to 4538. No step ends at 3232, so no state is ever written for slot 1:

      tokens      0        1616       3232       4538
                  |----------|--------------------|
      MTP on      [ step 1  ][       step 2       ]
      state slot       0                     2       <- slot 1 never written
      Mamba list  [ A ,      NULL ,      C , ...]  (vLLM's own list)
      tracker     [ A ,       S1 ,       C , ...]  (LMCache's copy)

  vLLM handles this in its own block list: it writes the null block into slot 1 and moves the speculative scratch block `S1` that used to sit there to the tail. But the connector only receives the blocks appended at the tail (`new_block_ids = [S1, C]`), never the in-place null. LMCache's tracker is append-only, so its slot 1 still says `S1`.

  When the store for chunk 1 (tokens 1616-3232) runs, the tracker hands `S1` to the server as that chunk's recurrent state. `S1` was allocated as scratch space for the verify step and no prefill kernel ever wrote to it, so what gets stored is whatever the page held before. On the next hit the retrieve load  that object back into slot 1 and the model resumes from it.





### kavehs87 · 2026-09-07

good point! thanks for the clues i will check and report back. 

### kavehs87 · 2026-09-07

Update: validated the fix on my setup (Qwen3.8-27B, TP2, MTP n=4) by adapting the three hunks onto 0.5.5rc5 — the 0/10 multi-step retrieve case now comes back bit-identical, details with numbers posted on the PR.

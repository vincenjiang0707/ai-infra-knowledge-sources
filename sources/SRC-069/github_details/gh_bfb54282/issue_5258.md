# [Issue #5258] BatchPrefillWithPagedKVCacheWrapper(backend="cudnn") rejects return_lse=True: expects a padded (b, max_q, h) LSE, wrapper allocates [tokens, h]

source: https://github.com/flashinfer-ai/flashinfer/issues/5258
state: open | updated: 2026-09-21T21:57:47Z
labels: needs-triage

## 正文

`BatchPrefillWithPagedKVCacheWrapper(backend="cudnn").run(..., return_lse=True)` raises on `main`:

```
flashinfer/cudnn/prefill.py:951: ValueError: lse must have shape (num_sequences, max_token_per_sequence, h_qo)
```

The wrapper allocates (and documents) the LSE as `[total_tokens, num_qo_heads]`, which every other backend writes, and hands that buffer to `cudnn_batch_prefill_with_kv_cache`, whose paged path (no `batch_offsets_stats`) only accepts the padded `(num_sequences, max_token_per_sequence, h_qo)` form. The ragged wrapper is fine because it passes a stats ragged offset (`_cudnn_stats_offsets`) and cuDNN writes the packed layout directly. The paged wrapper needs the same: a token-unit stats offset (= `qo_indptr`) so cuDNN writes `[tokens, h]`, or a padded scratch + gather.

Repro: `tests/attention/test_lse_base.py::test_paged_lse_base[*-cudnn]` (strict xfail in #5257), or:

```python
w = flashinfer.BatchPrefillWithPagedKVCacheWrapper(ws, "NHD", backend="cudnn")
w.plan(qo_indptr, page_indptr, kv_indices, last_page_len, 8, 2, 128, 16, causal=True,
       q_data_type=torch.bfloat16, kv_data_type=torch.bfloat16,
       seq_lens=kv_lens, seq_lens_q=q_lens, max_token_per_sequence=64, max_sequence_kv=90, block_tables=block_tables)
out, lse = w.run(q, (k_cache, v_cache), return_lse=True)   # ValueError
```

SM100, cuDNN 9.27, cudnn-frontend 1.30, FlashInfer main `ed5f7b60`. Not reached by vLLM today (paged prefill `auto` resolves to fa2/fa3), so low urgency, but `backend="cudnn"` + `return_lse` is a documented combination.

<sub>note to self: claude::61d24ed2-7c90-4a97-9cbb-b91ae18136fd — "flashinfer frost prefill/GEMM enablement" · cwd /home/scratch.yanxu_libs/flashinfer</sub>


## 评论 (2)

### LiRunGuo · 2026-09-21

!claim

I'd like to take this. I reproduced it on H200 (SM90, cuDNN 9.24, cudnn-frontend 1.29, main @ `2268a1ae`+), so it isn't Blackwell-specific. While fixing it I found two more problems in the same call site.

**1. The reported bug.** The paged cuDNN call passes no stats ragged offset, so the low level only accepts the padded `(num_sequences, max_q_len, h_qo)` LSE. Passing the token-unit `qo_indptr` as `batch_offsets_stats` (what the ragged wrapper already does) makes cuDNN write the packed `[tokens, heads]` layout. After that change, LSE matches fa2 to 2e-3 (GQA 8/2 and MHA 8/8, causal and non-causal).

**2. Unreported: wrong output when `plan()` gets no `sm_scale`.** `run()` computes a defaulted local `sm_scale = 1/sqrt(head_dim)`, but the paged cuDNN call passes `self._sm_scale`, which is `None` in that case, so cuDNN applies no scaling. This is independent of `return_lse`:

| paged cuDNN vs fa2, bf16, 8/2 heads, head_dim 128, page 16 | out max abs diff |
|---|---|
| `sm_scale=None` (default), before | 3.48 |
| `sm_scale=1/sqrt(128)` explicit, before | 0.016 |
| `sm_scale=None`, after passing the defaulted scale | 0.016 |

`tests/attention/test_cudnn_prefill.py` always passes `sm_scale` explicitly, which is why it never showed up. (The ragged wrapper passes the local `sm_scale` and is fine.)

**3. The single-token GQA LSE bug (NVBug 6783545) also affects the paged kernel.** With every q_len == 1 and 8/2 heads, the packed LSE is only correct for the first head of each kv group (per-head max abs diff vs fa2: `[0.001, 7.5, 6.9, 7.2, 0.0, 7.4, 7.1, 7.2]`); MHA is fine. I see this on cuDNN 9.24, not only 9.26/9.27. The ragged wrapper already raises `NotImplementedError` for this case; I'll mirror that guard in the paged path so enabling the packed LSE doesn't trade a loud `ValueError` for a silently wrong LSE.

Also: `test_paged_lse_base[cudnn]` hands cuDNN an NHD-*shaped* cache, while the paged cuDNN path reads `shape[1]` as the kv head count (the `[pages, H_kv, page_size, D]` view `test_cudnn_prefill.py` builds). The strict xfail was hiding that; I'll fix the test input together with removing the xfail.

PR coming shortly.


### flashinfer-bot · 2026-09-21

Issue assigned to @LiRunGuo.

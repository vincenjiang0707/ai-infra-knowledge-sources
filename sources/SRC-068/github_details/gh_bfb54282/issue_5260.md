# [Issue #5260] Ragged prefill plan() accepts non-contiguous (strided) indptr tensors and returns wrong results

source: https://github.com/flashinfer-ai/flashinfer/issues/5260
state: open | updated: 2026-09-21T12:11:57Z
labels: needs-triage

## 正文

`BatchPrefillWithRaggedKVCacheWrapper.plan()` accepts non-contiguous GPU indptr tensors (e.g. a stride-2 view such as `indptr_full[::2]`) and produces incomplete / wrong attention output instead of rejecting or normalizing them. Contiguous copies of the same indptrs give correct results.

Reproduced on `main` at `24c30bdd` and on the #5245 head with the cuDNN override both enabled and disabled, so it is independent of backend selection: the indptr buffers are consumed by `plan()` (host copies / device pointers) with an implicit contiguity assumption and no check.

Expected: either `.contiguous()` the indptrs in `plan()` (they are tiny) or raise `ValueError` for non-contiguous input, like the existing dtype/device checks.

Found during the independent review of #5245 (see the review comment there); low urgency, frameworks pass contiguous indptrs today.

<sub>note to self: claude::61d24ed2-7c90-4a97-9cbb-b91ae18136fd — "flashinfer frost prefill/GEMM enablement" · cwd /home/scratch.yanxu_libs/flashinfer</sub>


## 评论 (2)

### LiRunGuo · 2026-09-21

!claim

I'd like to take this one. I reproduced it on H200 (SM90, main @ `28fae4f2`), and the impact is broader than the ragged wrapper: besides wrong output it also causes illegal memory accesses.

**Repro:** plan the same problem twice, once with contiguous metadata and once with stride-2 views holding identical values (`buf[::2]`, garbage in the gaps), then compare outputs. fp16, 8/2 heads, head_dim 128, page_size 16, 4 requests.

| wrapper / backend | strided metadata on CUDA | strided metadata on CPU |
|---|---|---|
| Ragged prefill, fa2 | illegal memory access | `PrefillSplitQOKVIndptr` check fails (reads the gap values) |
| Ragged prefill, fa3 | OK | `PrefillSM90Plan` check fails |
| Paged prefill, fa2 | illegal memory access | `PrefillSplitQOKVIndptr` check fails |
| Paged prefill, fa3 | wrong output (max abs diff 3.3) | `PrefillSM90Plan` check fails |
| Paged decode, CUDA cores | wrong output (max abs diff 3.0) | wrong output (max abs diff 4.6), no error |
| Paged decode, tensor cores | wrong output (max abs diff 2.6) | `PrefillSplitQOKVIndptr` check fails |

**Root cause:** there are two paths.
- CUDA inputs: in non-CUDA-graph mode, `plan()` does `self._*_indptr_buf = indptr.to(self.device)`. That is a no-op for a strided CUDA view, so the kernel gets a raw `data_ptr()` over strided memory. Meanwhile `indptr.to("cpu")` returns a *contiguous* host copy, so plan info and kernel disagree.
- CPU inputs: `.to("cpu")` is a no-op, so the strided host tensor goes straight to the C++ planner, which also reads it through `data_ptr()`.

The CUDA-graph path is unaffected because it uses `copy_()` into preallocated buffers.

**Plan:** call `.contiguous()` on the index tensors at the top of `plan()` (they're tiny, and `plan()` already copies them), covering ragged/paged prefill, paged decode, and the sparse wrappers in `sparse.py`, which use the same `.to(self.device)` pattern. I'll add a parametrized regression test. (The MLA planner already rejects non-contiguous metadata, so it's out of scope.)


### flashinfer-bot · 2026-09-21

Issue assigned to @LiRunGuo.

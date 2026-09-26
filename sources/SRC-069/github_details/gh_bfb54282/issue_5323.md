# [Issue #5323] SM120 sparse-MLA decode: no dispatch entry for page_block_size=32 (DeepSeek-V4.1-Flash, TP=8 and TP=4/PP=2, both fail identically)

source: https://github.com/flashinfer-ai/flashinfer/issues/5323
state: open | updated: 2026-09-19T00:12:15Z
labels: needs-triage

## 正文

## Problem

`DeepSeek-V4.1-Flash` fails to start on SM120 (RTX PRO 6000 Blackwell) with
a `ValueError` from `_sparse_mla_sm120.py` during KV-cache-size probing
(`determine_available_memory`), before any request is served. Confirmed
across two independent tensor/pipeline-parallel configurations with the
same result, ruling out TP degree as the cause.

## Root cause (traced on the vLLM side)

`compressed_block_size` is computed as:

    compressed_block_size = attn_metadata.block_size // self.compress_ratio

(`vllm/models/deepseek_v41/nvidia/flashinfer_sparse.py`)

`block_size` is fixed at 128 for this backend
(`FLASHINFER_MLA_SPARSE_DSV41.get_supported_kernel_block_sizes() -> [128]`,
not CLI-configurable). The crash's `page_block_size=32` therefore implies
`compress_ratio=4` on at least one attention layer of this checkpoint —
this is architecture-fixed, not a runtime/config choice.

The init-time check in `DeepseekV4FlashInferSM120Attention.__init__`
(`has_flashinfer_sparse_mla_sm120_config(padded_heads, required_topk)`)
passes for our shape — it only validates `(num_heads, topk)`, not
`page_block_size` — so the failure only surfaces later, inside the actual
kernel call.

## Environment

- Hardware: `g7e.48xlarge` (8x RTX PRO 6000 Server Edition Blackwell, SM120), AWS eu-central-1
- Image: `vllm/vllm-openai:nightly`
- vLLM: `0.29.1rc1.dev347+gdee37d891`
- FlashInfer: `flashinfer-jit-cache==0.6.18.post1` (per vLLM's `docker/Dockerfile` pin)
- Model: `deepseek-ai/DeepSeek-V4.1-Flash`, `--language-model-only --tokenizer-mode deepseek_v41`

## Repro 1: TP=8

    vllm serve deepseek-ai/DeepSeek-V4.1-Flash --tensor-parallel-size 8 \
      --language-model-only --tokenizer-mode deepseek_v41 --max-model-len 131072 \
      --max-num-seqs 128 --max-num-batched-tokens 16384 \
      --gpu-memory-utilization 0.90 --enable-auto-tool-choice \
      --reasoning-parser deepseek_v41 --tool-call-parser deepseek_v41

    ValueError: SM120 sparse-MLA has no decode kernel for this shape:
    num_tokens=32, num_heads=8, topk=128, d_qk=512, page_block_size=32,
    model_type=1, extra_topk=0. Supported decode shapes are enumerated in
    _DECODE_DSV4_DISPATCH and _DECODE_DSV3_2_DISPATCH.

## Repro 2: TP=4, PP=2 (same total 8 GPUs, different head/rank split)

Same command with `--tensor-parallel-size 4 --pipeline-parallel-size 2`.

    ValueError: SM120 sparse-MLA has no decode kernel for this shape:
    num_tokens=32, num_heads=16, topk=128, d_qk=512, page_block_size=32,
    model_type=1, extra_topk=0. Supported decode shapes are enumerated in
    _DECODE_DSV4_DISPATCH and _DECODE_DSV3_2_DISPATCH.

`num_heads` changed 8→16 exactly as expected from the TP change.
`page_block_size=32` did not move. This rules out `num_heads`/TP degree as
the blocking factor — `page_block_size=32` itself has no dispatch entry at
all, independent of `num_heads` or `topk`.

Also tried `VLLM_TRITON_MLA_SPARSE=1` as a runtime workaround — no effect,
backend selection logged as `FLASHINFER_MLA_SPARSE_DSV41` either way.

## Relation to existing issues/PRs

None of these cover `page_block_size=32` — all hold block size at 64 and
only vary `(num_heads, topk)`:

- #3989 (closed, superseded by #4380): adds `topk=256` dispatch entries for DSpark spec-decode, tested at `page_block_size=64`
- flashinfer#4380 (merged): adds `topk=192` for DSpark, same `page_block_size=64` assumption
- vllm-project/vllm#52499, #51538: fix DSpark spec-decode batch shaping, not plain-decode dispatch coverage

## Ask

Is `page_block_size=32` support for the SM120 sparse-MLA decode kernel
planned, or is 64 the only intended/supported page size for this
architecture on SM120? If the latter, `DeepSeek-V4.1-Flash` checkpoints
with a `compress_ratio=4` layer cannot run on SM120 at all today, and it'd
be worth a clearer error message than the current `ValueError` (the
init-time check in `flashinfer_sparse.py` already validates `(num_heads,
topk)` — extending it to also check `page_block_size` would at least fail
fast with a clear message instead of after model load).


## 评论 (1)

### jahnclawdmonet · 2026-09-19

The failing conjunct is `page_block_size`. In 0.6.18.post1 the decode predicate is

```python
def _decode_dsv4_dispatchable(num_tokens, num_heads, topk, d_qk, page_block_size, extra_topk=0):
    return (
        num_tokens <= _DECODE_MAX_TOKENS
        and d_qk == 512
        and page_block_size == _DECODE_DSV4_PAGE_BLOCK_SIZE
        and (num_heads, topk) in _DECODE_DSV4_DISPATCH
    )
```

`_DECODE_MAX_TOKENS` is 64, so your 32 passes, `d_qk` is 512, and `_DECODE_DSV4_DISPATCH` contains both `(8, 128)` from your TP=8 run and `(16, 128)` from the TP=4/PP=2 one. `page_block_size` is not an axis of either table at all: it is a module constant, `_DECODE_DSV4_PAGE_BLOCK_SIZE = 64`, compared with `==`, so 32 has nothing to match against. The message also prints `extra_topk`, but the dsv4 predicate takes that argument and never reads it.

This was lifted on main the same day you filed. PR #5197, merged 2026-09-18 06:53Z as `eb5f05be1`, replaces the fixed page size in `sparse_mla_sm120/execution/attention_plan.h`:

```cpp
constexpr bool main_page_supported(ModelType model, int page) {
  return runtime_page(model) ? page > 0 : page == FixedPageSize;
}
```

`runtime_page` returns true for `DSV4`; the condition for that branch is `page > 0`. On the Python side the dispatch set also became a predicate rather than a fixed pair list. It is not in a release yet: the newest tag is v0.7.0rc3 from 2026-09-16, two days before that merge.

I have not run your workload. This is from reading the dispatch chain at the version you pinned and at the merge commit.


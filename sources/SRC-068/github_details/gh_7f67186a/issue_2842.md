# [Issue #2842] splitkv early-exit path ignores unpadded_lse, writing -inf to the wrong LSE slot

source: https://github.com/Dao-AILab/flash-attention/issues/2842
state: open | updated: 2026-09-02T18:27:39Z
labels: 

## 正文

**Title:** splitkv early-exit path ignores `unpadded_lse`, writing `-inf` to the wrong LSE slot

**Repo:** Dao-AILab/flash-attention (also present in the vllm-project fork)

---

`flash_fwd_splitkv_kernel` computes the LSE write offset two different ways depending on
which exit it takes, and only one of them honours `params.unpadded_lse`.

**Normal exit** — `csrc/flash_attn/src/flash_fwd_kernel.h:1030`:

```cpp
const index_t row_offset_lseaccum = (Split || !params.unpadded_lse ?
        ((n_split_idx * params.b + bidb) * params.h + bidh) * params.seqlen_q
      : bidh * params.total_q + binfo.q_offset(params.seqlen_q, 1, bidb)
    ) + m_block * kBlockM;
```

**Early exit** (taken when `n_block_max <= n_block_min`, e.g. a zero-length or fully-masked
KV sequence) — `flash_fwd_kernel.h:552`:

```cpp
const index_t row_offset_lseaccum = ((n_split_idx * params.b + bidb) * params.h + bidh) * params.seqlen_q
    + m_block * kBlockM;
```

The ternary is missing. So when `unpadded_lse` is set and `Split` is false, the early exit
writes `-inf` into `params.softmax_lse_ptr` at a **dense** `(b, h, seqlen_q)` offset, while
the buffer is laid out **unpadded** as `(h, total_q)`. The two offsets coincide only when
`b == 1` and `seqlen_q == total_q`.

**Effect:** a varlen batch containing a zero-length (or fully masked) KV sequence writes
`-inf` into a different sequence's LSE slot, or out of bounds. `unpadded_lse` is set on the
varlen path, so any caller passing `return_softmax_lse=True` with a mixed batch is exposed.

**Why it is rarely seen:** early-exit CTAs finish almost immediately, so in practice the
correct value is usually written afterwards by the CTA that owns the slot, masking the race.
It is a genuine wrong-address write regardless of who wins.

**Fix:** apply the same ternary at `:552` as at `:1030`.

**Found while** validating a split-k change to `mha_varlen_fwd` in the vllm-project fork; this
bug is independent of that change and predates it. With split-k engaged the `-inf` is routed
correctly through the combine kernel, so the patched path does not hit it — this is about the
unsplit path.

**Not tested by:** the current suite never constructs a zero-length KV sequence in a varlen
batch with `return_softmax_lse=True`.


## 评论 (1)

### noonghunna · 2026-09-02

Cross-reference: the vLLM fork of this repo has an open fix for the same defect — [vllm-project/flash-attention#139](https://github.com/vllm-project/flash-attention/pull/139), which hit it as an illegal memory access on Qwen 235B across 8× L40S with DCP enabled. That report has a real-world crash where mine only has a code-path argument, so it is the better reference for anyone landing here.

The defect is present in this repository too — `csrc/flash_attn/src/flash_fwd_kernel.h:552` uses the dense offset unconditionally while `:1030` carries the `unpadded_lse` ternary — which is why I filed here as well. Closing this in favour of a PR here would be reasonable if a maintainer prefers; I'm happy to port #139's fix upstream if that helps.

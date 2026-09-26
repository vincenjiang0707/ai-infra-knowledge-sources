# [Issue #4658] [Feature Request] cute-dsl MLA decode: extend cum_seq_lens_q support (follow-up to #3131 / #3238)

source: https://github.com/flashinfer-ai/flashinfer/issues/4658
state: open | updated: 2026-09-25T02:16:47Z
labels: needs-triage, priority: should have (P1)

## 正文

#3131 noted that `is_var_seq` already exists but is "only used in cute-dsl
backend". #3238 added `cum_seq_lens_q`/`max_q_len` for the `trtllm-gen`
path, and explicitly rejects it for cute-dsl:

    if backend == "cute-dsl":
        raise ValueError("cute-dsl MLA does not support cum_seq_lens_q")

Now that trtllm-gen's varlen-query decode is landed and consumed downstream
(sgl-project/sglang#35807), is cum_seq_lens_q support for cute-dsl on the
roadmap, or is there a specific blocker?

Context: sglang requires cute-dsl (or tokenspeed) instead of trtllm-gen for
decode-context-parallelism (DCP) configs (arg_groups/overrides.py enforces
this for Kimi-K3), so DCP users currently can't benefit from the
varlen-decode fix that non-DCP trtllm-gen configs now get.

## 评论 (1)

### shyeh25 · 2026-08-21

cc @nvpohanh @leejnau 

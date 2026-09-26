# [Issue #2672] Any plans to support MLA bwd in FA4 on SM 100?

source: https://github.com/Dao-AILab/flash-attention/issues/2672
state: closed | updated: 2026-07-13T01:48:56Z
labels: 

## 正文

If so, what is the estimated timeline for the full support?

## 评论 (5)

### jayhshah · 2026-06-22

What MLA backward are you asking about? Prefill shape {hdim, hdimv} = {192, 128} has been supported for a while now, and on SM 100 we added support for sparse MLA backward for weight absorbed shape {hdim, hdimv} = {64, 512}, MQA 128 in PR https://github.com/Dao-AILab/flash-attention/pull/2621.

### joonyoo181 · 2026-06-24

hey, sorry I should have been more clear. I mean MLA bwd specifically for SM 100s. 

> Prefill shape {hdim, hdimv} = {192, 128} has been supported for a while now

Is this also supported on SM 100? I'm not seeing the code for it.. do you mind pointing me to the code?

### jayhshah · 2026-06-24

Just use the usual `flash_attn_func` or `flash_attn_varlen_func`. See tests for usage: https://github.com/Dao-AILab/flash-attention/blob/6a94f8b906cf5ab944385d64707f9387f3dd6be9/tests/cute/test_flash_attn.py#L148

### joonyoo181 · 2026-06-24

What about for weight absorbed path for dense MLA? it seems like there is no bwd code path for that 

### jayhshah · 2026-06-25

Yes, this is not planned.

# [Issue #4384] Deprecate jax.experimental.pallas GPU splash

source: https://github.com/AI-Hypercomputer/maxtext/issues/4384
state: closed | updated: 2026-07-24T10:09:20Z
labels: feature request

## 正文

### Feature or Model Request

The pallas kernel in jax.experimental.pallas.ops.gpu is not being maintained (imported [here](https://github.com/AI-Hypercomputer/maxtext/blob/3dc1efe1937cd8ec57d882b7a61498aefeab3ef4/src/maxtext/layers/attention_op.py#L30) in maxtext)

We should deprecate this option - potentially by migrating to [tokamax](https://github.com/openxla/tokamax/blob/7c63ff889cb940c3aa6f57fb2144250fd4c7e466/tokamax/_src/ops/attention/pallas_mosaic_gpu.py#L62) - although perhaps the existing transformer engine [option](https://github.com/AI-Hypercomputer/maxtext/blob/3dc1efe1937cd8ec57d882b7a61498aefeab3ef4/src/maxtext/layers/attention_op.py#L1051) is fine 

### Additional Context

_No response_

## 评论 (2)

### superbobry · 2026-07-14

@huytransformer I have a draft PR for this internally at Google. I will update the issue if we decide not to go with it (hopefully, today or tomorrow). Just mentioning to avoid duplicate work.

### huytransformer · 2026-07-14

SGTM!

# [Issue #3435] [Bug] ValueError: Cannot assign data value to static attribute 'decoder' in models.py:339

source: https://github.com/AI-Hypercomputer/maxtext/issues/3435
state: closed | updated: 2026-04-04T00:13:59Z
labels: bug

## 正文

### Bug report

A ValueError occurs during the initialization of the Transformer class in maxtext/models/models.py. The error is triggered because the decoder attribute is being treated as static metadata by Flax NNX, preventing its assignment to a dynamic ToNNX wrapper.

### Logs/Output

ValueError: Cannot assign data value of type '<class 'maxtext.layers.nnx_wrappers.ToNNX'>' to static attribute 'decoder' of Pytree type '<class 'maxtext.models.models.Transformer'>'. To override the status explicitly wrap the value with nnx.data on assignment:
 _.decoder = nnx.data(...)

### Environment Information

MaxText Branch: main (as of March 2026).

Hardware: Single-host TPU v5e 2*4

JAX Version: 0.4.25.

flax>=0.10.0

### Additional Context

_No response_

## 评论 (3)

### bvandermoon · 2026-03-17

Hey @karajendran, thank you for reporting this. Can you try pulling in the latest changes? This issue should be fixed by https://github.com/AI-Hypercomputer/maxtext/pull/3429

### RissyRan · 2026-03-30

Hi @bvandermoon I will assign this to you for now as you have involved. Please feel free to further triage. Thanks!

### bvandermoon · 2026-04-04

Marking this as fixed since the issue should be resolved. Please reopen if you see any issues

# [Issue #5381] test(gdn): fla_scatter_padded_pool clones away the padding, so the slot-slice fallback is never tested

source: https://github.com/flashinfer-ai/flashinfer/issues/5381
state: open | updated: 2026-09-21T19:15:20Z
labels: needs-triage

## 正文

### Summary

`test_gdn_decode_bf16_state_fla_scatter_padded_pool` does not exercise the padded pool. It builds a
correctly padded, non-contiguous pool, then calls `.clone()` on it — which contiguizes the tensor —
so the test compares the flat scatter path against itself.

As a consequence the slot-slice fallback (`per_token_pool_scatter_flat=False`,
`flashinfer/gdn_kernels/gdn_decode_bf16_state.py:1857-1860`) appears never to execute anywhere in
the GDN decode test suite.

### Where

`tests/gdn/test_decode_delta_rule.py`, in `test_gdn_decode_bf16_state_fla_scatter_padded_pool`:

```python
assert not pool_padded.is_contiguous()          # padded pool built correctly
...
# Under test: padded pool → slot-slice fallback
pool_under_test = pool_padded.clone()           # <-- contiguizes
gated_delta_rule_mtp(**common, initial_state_source=pool_under_test)
```

`Tensor.clone()` defaults to `memory_format=torch.preserve_format`, which only preserves strides for
tensors that are non-overlapping **and dense**. The padded pool is non-overlapping but not dense (it
has a gap of `pad_elts` between slots), so the clone comes back contiguous.

### Repro

```python
import torch
HV, V, K = 4, 8, 8
inner, pad, n = HV * V * K, 16, 6
big = torch.zeros(n * (inner + pad))
pool_padded = big.as_strided((n, HV, V, K), (inner + pad, V * K, K, 1))

print(pool_padded.stride(), pool_padded.is_contiguous())   # (272, 64, 8, 1) False
c = pool_padded.clone()
print(c.stride(), c.is_contiguous())                       # (256, 64, 8, 1) True
```

### Corroboration from kernel traces

Instrumenting the cache keys for a full run of the file, every case of this test carries
`pool_size_key=-1`, `pool_slot_stride=(-1,)`, `per_token_pool_scatter_flat=True` — the contiguous-pool
sentinels. No case in the 418-case baseline matrix reaches the `per_token_pool_scatter_flat=False`
branch.

### Suggested fix

Clone the backing allocation and re-derive the padded view, rather than cloning the view:

```python
pool_under_test = big.clone().as_strided(pool_padded.shape, pool_padded.stride())
```

and assert the property the test depends on, so it can't silently regress again:

```python
assert not pool_under_test.is_contiguous()
```

It would be worth confirming the fixed test actually fails if the slot-slice fallback is broken,
since that path has evidently never run in CI.

### Notes

Pre-existing; not introduced by #5379. Found while auditing test coverage for that PR.


## 评论 (2)

### SamMausberg · 2026-09-21

!claim

### flashinfer-bot · 2026-09-21

Issue assigned to @SamMausberg.

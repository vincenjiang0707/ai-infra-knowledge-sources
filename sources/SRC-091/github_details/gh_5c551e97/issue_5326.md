# [Issue #5326] [Documentation Request] vLLM kv_load_failure_policy doesn't apply to load failures in L2 adapters

source: https://github.com/LMCache/LMCache/issues/5326
state: open | updated: 2026-09-26T10:57:56Z
labels: 

## 正文

**Label**
Please label your issue so that it can easily be easily categorized under [LMCache Onboarding](https://github.com/LMCache/LMCache/issues/1882)

**Summary**
[kv_load_failure_policy](https://docs.vllm.ai/en/stable/api/vllm/config/kv_transfer/#vllm.config.kv_transfer.KVTransferConfig.kv_load_failure_policy) doesn't seem to apply to remote KV data load failures in L2 adapters.

**Details**
vLLM supports setting kv_load_failure_policy, which defines the behavior during KV load failures. However, this configuration option doesn't seem to apply to L2 adapters. We've tested the `nixl_store` L2 adapter and the `s3` L2 adapter with injected errors, and LMCache seems to treat L2 load failures as cache misses instead of failures.

is this an intentional design choice? It would be great to document the expected behavior of failures at different cache levels in LMCache.

**Steps / Reproduction (if applicable)**
1. Start LMCache with L2 adapter set to `nixl_store` with OBJ backend, or `s3`.
2. Start vLLM, use LMCache for KV cache offloading and internal prefix caching disabled with `--no-enable-prefix-caching`.
3. Send data to vLLM and Intercept all GetObject calls to the S3 endpoint.

**Expected Outcome / Goal**
With `"kv_load_failure_policy": "fail"`, requests with external cache hits should return error code.

**Actual Outcome (if applicable)**
LMCache log errors to the console, vLLM proceed to serve all requests with recomputed KV data as if it's only a cache miss.

**Additional Context**
This issue was first discovered by [Anish Sana](mailto:anish.sana@hpe.com) under HPE's internal testing.

## 评论 (2)

### neevmodh · 2026-09-26

I dug into this — can confirm the behavior with evidence rather than just a guess.

`kv_load_failure_policy` does not appear anywhere in LMCache's Python or C++ source (`lmcache/`, `csrc/`) at all — only in docs/examples as a value passed through to vLLM's `--kv-transfer-config` (e.g. `docs/source/mp/p2p.rst`), and it's always set to `"recompute"` in every example I could find. So this isn't a bug where LMCache reads the policy and applies it incorrectly — LMCache never reads it in the first place. The policy is entirely vLLM's to interpret, and LMCache's L2 adapters (including `nixl_store` and `s3`) have no branch that distinguishes "real load failure" from "key not present" — both surface the same way (miss → recompute), which matches what you observed.

So to answer your question directly: **no, this doesn't look like an intentional per-adapter design choice inside LMCache — it looks like the connector layer simply doesn't propagate a load-failure signal distinct from a cache-miss signal at all**, for any L2 adapter, not just the two you tested. Whether `"fail"` should be enforced at the LMCache connector boundary (raise/propagate an exception vLLM can map to an error response) or is intentionally left as vLLM's responsibility on the request path is a design call for a maintainer familiar with the vLLM connector contract — happy to help document whichever direction is confirmed, or take a stab at wiring the distinction through if that's the preferred fix.

### neevmodh · 2026-09-26

Opened #5364 documenting the findings from my earlier comment — clarifies in both the P2P and disaggregated-prefill docs that `kv_load_failure_policy` is passed through but not enforced by LMCache's own L2 adapters, and (from the disaggregated-prefill example specifically) that it's actually a `NixlConnector` setting in that config, not an `LMCacheMPConnector` one. Docs-only change — didn't attempt to change the actual enforcement behavior since that's a design call for a maintainer.
